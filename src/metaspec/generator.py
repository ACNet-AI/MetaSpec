"""
Generator for creating speckit projects from meta-spec definitions.

This module implements the core generation logic that transforms
MetaSpecDefinition into complete SpecKitProject structures.
"""

import re
import textwrap
from datetime import datetime
from importlib.metadata import version
from pathlib import Path
from typing import Any

from jinja2 import (
    BaseLoader,
    Environment,
    FileSystemLoader,
    PackageLoader,
    TemplateNotFound,
)

from metaspec.models import MetaSpecDefinition, SpecKitProject


class Generator:
    """
    Generate complete speckit projects from meta-spec definitions.

    The generation process:
    1. Validate output directory
    2. Select templates
    3. Create template context
    4. Render all templates
    5. Build SpecKitProject structure
    6. Write to disk (atomic)
    """

    def __init__(self, custom_template_dir: Path | None = None):
        """
        Initialize generator with Jinja2 environment.

        Args:
            custom_template_dir: Optional path to custom templates
        """
        # Initialize Jinja2 environment
        loader: BaseLoader
        if custom_template_dir:
            loader = FileSystemLoader(str(custom_template_dir))
        else:
            loader = PackageLoader("metaspec", "templates")

        self.env = Environment(
            loader=loader,
            trim_blocks=True,
            lstrip_blocks=True,
            keep_trailing_newline=True,
        )

    def generate(
        self,
        meta_spec: MetaSpecDefinition,
        output_dir: Path,
        force: bool = False,
        dry_run: bool = False,
    ) -> SpecKitProject:
        """
        Generate a complete speckit from meta-spec definition.

        Args:
            meta_spec: Parsed and validated meta-spec definition
            output_dir: Output directory path
            force: If True, overwrite existing directory
            dry_run: If True, only return project structure without writing

        Returns:
            Generated SpecKitProject

        Raises:
            FileExistsError: If output_dir exists and force=False (when not dry_run)
        """
        # Step 1: Check output directory (skip in dry_run mode)
        if not dry_run and output_dir.exists() and not force:
            raise FileExistsError(
                f"Output directory already exists: {output_dir}\n"
                "Use --force flag to overwrite."
            )

        # Step 2: Select templates
        template_map = self._select_templates(meta_spec)

        # Step 3: Create template context
        context = self._create_template_context(meta_spec)

        # Step 4: Render all templates
        rendered_files = self._render_templates(template_map, context)

        # Step 5: Build SpecKitProject
        project = self._construct_project(
            output_dir=output_dir,
            package_name=context["package_name"],
            rendered_files=rendered_files,
            context=context,
        )

        # Step 6: Write to disk (atomic) - skip in dry_run mode
        if not dry_run:
            # Note: write_to_disk already includes executable permissions
            project.write_to_disk(force=force)

        return project

    def _get_metaspec_version(self) -> str:
        """
        Get the MetaSpec package version from metadata.

        Returns:
            Version string (e.g., "0.5.1")
        """
        try:
            return version("meta-spec")
        except Exception:
            # Fallback to a default version if package metadata is not available
            return "0.0.0"

    def _create_template_context(self, meta_spec: MetaSpecDefinition) -> dict[str, Any]:
        """
        Create template rendering context from MetaSpecDefinition.

        Args:
            meta_spec: The speckit definition

        Returns:
            Dict with all variables needed for template rendering
        """
        # Convert name to Python package name (snake_case)
        # Replace any non-alphanumeric characters (except underscores) with underscores
        package_name = re.sub(r"[^a-z0-9_]", "_", meta_spec.name.lower())
        # Remove leading/trailing underscores and collapse multiple underscores
        package_name = re.sub(r"_{2,}", "_", package_name).strip("_")

        # Ensure description exists
        description = (
            meta_spec.description or f"Spec-driven speckit for {meta_spec.domain}"
        )

        # Convert entity to dict for template access
        entity_dict = {
            "name": meta_spec.entity.name,
            "fields": [
                {
                    "name": f.name,
                    "type": f.type or "str",
                    "description": f.description or "",
                }
                for f in meta_spec.entity.fields
            ],
        }

        # Convert CLI commands to list of dicts
        cli_commands_list: list[dict[str, Any]] = []
        if meta_spec.cli_commands:
            for cmd in meta_spec.cli_commands:
                cmd_dict: dict[str, Any] = {
                    "name": cmd.name,
                    "description": cmd.description,
                    "options": [],
                }
                if cmd.options:
                    cmd_dict["options"] = [
                        {
                            "name": opt.name,
                            "type": opt.type,
                            "required": opt.required,
                            "description": opt.description or "",
                        }
                        for opt in cmd.options
                    ]
                cli_commands_list.append(cmd_dict)

        # Convert slash commands to list of dicts
        slash_commands_list = []
        if meta_spec.slash_commands:
            for sc in meta_spec.slash_commands:
                slash_commands_list.append(
                    {
                        "name": sc.name,
                        "description": sc.description,
                        "source": sc.source,
                    }
                )

        return {
            "name": meta_spec.name,
            "package_name": package_name,
            "version": meta_spec.version,
            "description": description,
            "domain": meta_spec.domain,
            "entity": entity_dict,
            "cli_commands": cli_commands_list,
            "slash_commands": slash_commands_list,
            "dependencies": meta_spec.dependencies or [],
            "year": datetime.now().year,
            "date": datetime.now().date().isoformat(),
            "metaspec_version": self._get_metaspec_version(),
        }

    def _select_templates(self, meta_spec: MetaSpecDefinition) -> dict[str, str]:
        """
        Select templates for speckit generation based on meta_spec configuration.

        Structure:
        - base/ → speckit root files (README, AGENTS.md, etc.)
        - library/templates/ → speckit/templates/ (dynamically based on slash_commands)
        - meta/commands/ → speckit/.metaspec/commands/ (for speckit developers)

        Args:
            meta_spec: MetaSpecDefinition to determine which templates to include

        Returns:
            Dict mapping template paths to output file paths
        """
        template_map = {}

        # 1. Base templates (speckit project files)
        base_templates = [
            ("base/AGENTS.md.j2", "AGENTS.md"),
            ("base/README.md.j2", "README.md"),
            ("base/CHANGELOG.md.j2", "CHANGELOG.md"),
            ("base/pyproject.toml.j2", "pyproject.toml"),
            ("base/constitution.md.j2", "memory/constitution.md"),
            ("base/.gitignore.j2", ".gitignore"),
            ("base/specs/README.md.j2", "specs/README.md"),  # specs/ directory guide
            ("base/templates/README.md.j2", "templates/README.md"),  # templates/ directory guide
            (
                "base/scripts/bash/create-new-feature.sh.j2",
                "scripts/bash/create-new-feature.sh",
            ),  # Phase 2: feature management
        ]
        for template_path, output_path in base_templates:
            template_map[template_path] = output_path

        # 2. Library templates (dynamically based on slash_commands)
        # Only copy templates and commands that are referenced by slash commands
        if meta_spec.slash_commands:
            # Define command-to-subdirectory mapping for library/generic
            generic_command_map = {
                # Greenfield commands (8)
                "constitution": "greenfield",
                "specify": "greenfield",
                "clarify": "greenfield",
                "plan": "greenfield",
                "tasks": "greenfield",
                "generate": "greenfield",
                "validate": "greenfield",
                "analyze": "greenfield",
                # Brownfield commands (3)
                "proposal": "brownfield",
                "apply": "brownfield",
                "archive": "brownfield",
            }

            for sc in meta_spec.slash_commands:
                # Use source field from slash command (defaults to "generic")
                source = f"library/{sc.source}"

                # For library/generic, check if command needs subdirectory routing
                if sc.source == "generic" and sc.name in generic_command_map:
                    subdir = generic_command_map[sc.name]
                    source = f"library/generic/{subdir}"

                # Copy template file (required)
                # Organize by source to maintain specification system boundaries
                template_name = f"{sc.name}-template.md"
                source_template = f"{source}/templates/{template_name}.j2"
                output_template = f"templates/{sc.source}/templates/{template_name}"
                template_map[source_template] = output_template

                # Copy command file (optional - some sources like "generic" may not have commands)
                # Organize by source to avoid naming conflicts
                command_name = f"{sc.name}.md"
                source_command = f"{source}/commands/{command_name}.j2"
                output_command = f"templates/{sc.source}/commands/{command_name}"
                # Only add to template_map if command file exists
                # The actual existence check happens during rendering, where missing files are skipped
                template_map[source_command] = output_command

        # 3. MetaSpec commands and templates for speckit development → .metaspec/
        # These provide AI-assisted workflow for developing the speckit itself
        # Three-layer architecture:
        #   - SDS (Spec-Driven Specification): 8 commands for specification definition
        #   - SDD (Spec-Driven Development): 8 commands for toolkit development
        #   - Evolution: 3 shared commands for specification evolution

        # SDS commands (8): Domain specification definition
        # File naming: metaspec.sds.{command}.md to use /metaspec.sds.{command} prefix
        sds_commands = [
            "constitution",  # Define specification design principles
            "specify",  # Define specification entities and operations
            "clarify",  # Resolve specification ambiguities
            "plan",  # Plan specification architecture and sub-specifications
            "tasks",  # Break down specification work
            "implement",  # Write specification documents
            "checklist",  # Generate quality checklist for specification
            "analyze",  # Check specification consistency
        ]

        for cmd in sds_commands:
            source_path = f"meta/sds/commands/{cmd}.md.j2"
            output_path = f".metaspec/commands/metaspec.sds.{cmd}.md"
            template_map[source_path] = output_path

        # SDD commands (8): Toolkit development workflow
        # File naming: metaspec.sdd.{command}.md to use /metaspec.sdd.{command} prefix
        sdd_commands = [
            "constitution",  # Define toolkit principles
            "specify",  # Define toolkit specifications
            "clarify",  # Resolve toolkit ambiguities
            "plan",  # Plan implementation
            "tasks",  # Break down tasks
            "implement",  # Execute implementation
            "checklist",  # Validate quality
            "analyze",  # Check consistency
        ]

        for cmd in sdd_commands:
            source_path = f"meta/sdd/commands/{cmd}.md.j2"
            output_path = f".metaspec/commands/metaspec.sdd.{cmd}.md"
            template_map[source_path] = output_path

        # Evolution commands (3): Shared specification evolution commands
        # File naming: metaspec.evolution.{command}.md (unified naming pattern)
        # These commands support both SDS and SDD through --type parameter
        evolution_commands = [
            "proposal",  # Propose changes (SDS or SDD)
            "apply",  # Apply changes
            "archive",  # Archive changes
        ]

        for cmd in evolution_commands:
            source_path = f"meta/evolution/commands/{cmd}.md.j2"
            output_path = f".metaspec/commands/metaspec.evolution.{cmd}.md"
            template_map[source_path] = output_path

        # MetaSpec README.md (Developer guide for speckit developers)
        template_map["base/.metaspec/README.md.j2"] = ".metaspec/README.md"

        # MetaSpec templates (output formats for MetaSpec commands)
        metaspec_templates = [
            "constitution-template.md",  # Constitution template
            "spec-template.md",  # Spec template
            "plan-template.md",  # Plan template
            "tasks-template.md",  # Tasks template
            "checklist-template.md",  # Checklist template
        ]

        for tpl in metaspec_templates:
            source_path = f"meta/templates/{tpl}.j2"
            output_path = f".metaspec/templates/{tpl}"
            template_map[source_path] = output_path

        return template_map

    def _render_templates(
        self, template_map: dict[str, str], context: dict
    ) -> dict[str, str]:
        """
        Render all templates with context using Jinja2.

        Args:
            template_map: Dict of {template_path: output_path}
            context: Template variables

        Returns:
            Dict of {output_path: rendered_content}

        Raises:
            TemplateNotFound: If a required template file is missing
        """
        rendered = {}

        for template_path, output_path in template_map.items():
            try:
                # Render template using Jinja2 environment
                template = self.env.get_template(template_path)
                content = template.render(**context)
                rendered[output_path] = content
            except TemplateNotFound as e:
                # Command files from library are optional (e.g., library/generic/commands/)
                # Skip silently if not found
                if (
                    template_path.startswith("library/")
                    and "/commands/" in template_path
                ):
                    continue

                # All other templates are required
                raise TemplateNotFound(
                    f"Template not found: {template_path}\n"
                    f"Expected location: templates/{template_path}\n"
                    f"This may indicate a missing template file or incorrect template path."
                ) from e

        return rendered

    def _construct_project(
        self,
        output_dir: Path,
        package_name: str,
        rendered_files: dict[str, str],
        context: dict[str, Any] | None = None,
    ) -> SpecKitProject:
        """
        Construct SpecKitProject from rendered templates.

        Args:
            output_dir: Output directory
            package_name: Python package name
            rendered_files: Dict of {relative_path: content}
            context: Template context for additional file generation

        Returns:
            SpecKitProject instance
        """
        files = {}
        directories = set()
        executable_files = []

        # Add rendered files
        for relative_path, content in rendered_files.items():
            path = Path(relative_path)
            files[path] = content

            # Track directory
            if path.parent != Path("."):
                directories.add(path.parent)

        # Add source package structure
        src_dir = Path("src") / package_name
        directories.add(src_dir)

        # Create __init__.py
        init_path = src_dir / "__init__.py"
        files[init_path] = f'"""Package: {package_name}"""\n\n__version__ = "0.1.0"\n'

        # Create cli.py stub
        cli_path = src_dir / "cli.py"
        cli_commands = context.get("cli_commands", []) if context else []
        files[cli_path] = self._create_cli_stub(package_name, cli_commands)

        # Create scripts directory
        scripts_dir = Path("scripts")
        directories.add(scripts_dir)
        directories.add(scripts_dir / "bash")  # Phase 2: bash scripts subdirectory

        # Create shell scripts
        init_script = scripts_dir / "init.sh"
        files[init_script] = self._create_init_script(package_name)
        executable_files.append(init_script)

        # Phase 2: Mark create-new-feature.sh as executable (from base templates)
        feature_script = scripts_dir / "bash" / "create-new-feature.sh"
        if feature_script in files:
            executable_files.append(feature_script)

        # Additional directories
        directories.add(Path("templates"))
        # Note: templates/{source}/commands/ and templates/{source}/templates/
        # are automatically tracked via files dict (Line 414-416)
        directories.add(Path("memory"))
        directories.add(Path("examples"))
        directories.add(Path("specs"))  # Phase 2: Specifications directory
        directories.add(Path(".metaspec/commands"))  # MetaSpec development commands
        directories.add(Path(".metaspec/templates"))  # MetaSpec development templates

        return SpecKitProject(
            root_path=output_dir,
            files=files,
            directories=sorted(directories),
            executable_files=executable_files,
        )

    def _create_cli_stub(self, package_name: str, commands: list[dict]) -> str:
        """
        Create CLI module stub with dynamic commands.

        Args:
            package_name: Name of the package
            commands: List of command definitions from cli_commands
        """
        # Generate command functions dynamically
        command_functions = []
        for cmd in commands:
            cmd_name = cmd["name"]
            cmd_desc = cmd["description"]

            # Special handling for info command (no parameters)
            if cmd_name == "info":
                command_functions.append(
                    textwrap.dedent(f'''
                    @app.command()
                    def {cmd_name}():
                        """{cmd_desc}"""
                        console.print("[cyan]Speckit:[/cyan] {package_name}")
                        console.print("[yellow]No functionality implemented yet.[/yellow]")
                        console.print("\\nNext steps:")
                        console.print("  1. Use /metaspec.specify to define your specification")
                        console.print("  2. Use /metaspec.implement to add CLI commands")
                        console.print("  3. See AGENTS.md for AI-assisted development guide")
                ''').strip()
                )
            else:
                # Generate function with options if present
                params_list = ["spec_file: str"]
                option_prints = ['console.print(f"[green]{cmd_name.title()}:[/green] {{spec_file}}")']

                if cmd.get("options"):
                    for opt in cmd["options"]:
                        opt_name = opt["name"]
                        opt_type = opt["type"]
                        opt_required = opt.get("required", False)

                        # Build parameter declaration
                        if opt_required:
                            params_list.append(f"{opt_name}: {opt_type}")
                        else:
                            # Optional parameter with default None
                            params_list.append(f"{opt_name}: {opt_type} = None")

                        # Add print statement for the option
                        option_prints.append(f'console.print(f"[blue]{opt_name.title()}:[/blue] {{{opt_name}}}")')

                params = ", ".join(params_list)
                option_code = "\n                        ".join(option_prints)

                command_functions.append(
                    textwrap.dedent(f'''
                    @app.command()
                    def {cmd_name}({params}):
                        """{cmd_desc}"""
                        {option_code}
                        # TODO: Implement {cmd_name}
                ''').strip()
                )

        # If no commands defined, provide a helpful message
        if not command_functions:
            command_functions.append(
                textwrap.dedent('''
                @app.command()
                def info():
                    """Show speckit information."""
                    console.print("[yellow]No commands defined yet.[/yellow]")
                    console.print("Use MetaSpec commands (/metaspec.*) to define and implement CLI commands.")
            ''').strip()
            )

        # Indent each command function
        indented_commands = "\n\n".join(command_functions)

        # Build the CLI module without dedent to preserve formatting
        return f'''"""
CLI for {package_name}.
"""

import typer
from rich.console import Console

app = typer.Typer(
    name="{package_name}",
    no_args_is_help=True,
    add_completion=False,
)
console = Console()

@app.callback(invoke_without_command=True)
def callback(ctx: typer.Context):
    """
    {package_name} - Specification toolkit

    Use --help with commands for more information.
    """
    # If no subcommand is provided, show help
    if ctx.invoked_subcommand is None:
        console.print(ctx.get_help())

{indented_commands}

def main():
    """Main entry point."""
    app()


if __name__ == "__main__":
    main()
'''

    def _create_init_script(self, package_name: str) -> str:
        """Create initialization script using uv."""
        return textwrap.dedent(f"""\
            #!/bin/bash
            # Initialization script for {package_name}

            set -e

            echo "Initializing {package_name}..."

            # Check if uv is installed
            if command -v uv &> /dev/null; then
                echo "Using uv for faster installation..."
                uv sync
            else
                echo "uv not found, falling back to pip..."
                echo "Tip: Install uv for faster dependency management: curl -LsSf https://astral.sh/uv/install.sh | sh"
                pip install -e .
            fi

            echo "✓ {package_name} initialized successfully!"
            echo ""
            echo "Next steps:"
            echo "  - Run '{package_name} --help' to see available commands"
            echo "  - Check README.md for usage instructions"
            echo "  - Read AGENTS.md for AI-assisted development guide"
        """)


def create_generator(custom_template_dir: Path | None = None) -> Generator:
    """
    Factory function to create a Generator instance.

    Args:
        custom_template_dir: Optional path to custom templates

    Returns:
        Configured Generator instance
    """
    return Generator(custom_template_dir=custom_template_dir)
