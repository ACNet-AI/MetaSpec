"""
Generator for creating toolkit projects from meta-spec definitions.

This module implements the core generation logic that transforms
MetaSpecDefinition into complete ToolkitProject structures.
"""

from pathlib import Path

from metaspec.models import MetaSpecDefinition, TemplateContext, ToolkitProject
from metaspec.template_loader import TemplateLoader


class Generator:
    """
    Generate complete toolkit projects from meta-spec definitions.

    The generation process:
    1. Validate output directory
    2. Load templates for domain
    3. Create template context
    4. Render all templates
    5. Build ToolkitProject structure
    6. Write to disk (atomic)
    """

    def __init__(self, custom_template_dir: Path | None = None):
        """
        Initialize generator.

        Args:
            custom_template_dir: Optional path to custom templates
        """
        self.template_loader = TemplateLoader(custom_template_dir)

    def generate(
        self,
        meta_spec: MetaSpecDefinition,
        output_dir: Path,
        force: bool = False,
        dry_run: bool = False,
        with_spec_kit: bool = False,
    ) -> ToolkitProject:
        """
        Generate a complete toolkit from meta-spec definition.

        Args:
            meta_spec: Parsed and validated meta-spec definition
            output_dir: Output directory path
            force: If True, overwrite existing directory
            dry_run: If True, only return project structure without writing
            with_spec_kit: If True, include spec-kit capabilities (greenfield)

        Returns:
            Generated ToolkitProject

        Raises:
            FileExistsError: If output_dir exists and force=False (when not dry_run)
        """
        # Step 1: Check output directory (skip in dry_run mode)
        if not dry_run and output_dir.exists() and not force:
            raise FileExistsError(
                f"Output directory already exists: {output_dir}\n"
                "Use --force flag to overwrite."
            )

        # Step 2: Select templates by domain
        template_map = self._select_templates(meta_spec.domain)

        # Step 3: Create TemplateContext
        context = TemplateContext.from_meta_spec(meta_spec)

        # Step 4: Render all templates
        rendered_files = self._render_templates(template_map, context)

        # Step 5: Build ToolkitProject
        project = self._construct_project(
            output_dir=output_dir,
            package_name=context["package_name"],
            rendered_files=rendered_files,
            with_spec_kit=with_spec_kit,
        )

        # Step 6: Write to disk (atomic) - skip in dry_run mode
        if not dry_run:
            # Note: write_to_disk already includes executable permissions
            project.write_to_disk(force=force)

        return project

    def _select_templates(self, domain: str) -> dict[str, str]:
        """
        Select templates based on domain.

        Args:
            domain: Domain identifier (generic, mcp, etc.)

        Returns:
            Dict mapping template paths to output file paths
        """
        template_map = {}

        # Base templates (always included)
        base_templates = [
            ("AGENTS.md.j2", "AGENTS.md"),
            ("README.md.j2", "README.md"),
            ("pyproject.toml.j2", "pyproject.toml"),
            ("constitution.md.j2", "memory/constitution.md"),
            (".gitignore.j2", ".gitignore"),
        ]

        for template_name, output_path in base_templates:
            template_map[f"base/{template_name}"] = output_path

        # Domain-specific templates
        domain_templates = self.template_loader.get_template_names(domain)
        for template_name in domain_templates:
            # Remove .j2 extension
            output_name = template_name.replace(".j2", "")

            # Place domain templates in templates/ subdirectory
            if domain != "base":
                output_path = f"templates/{output_name}"
            else:
                output_path = output_name

            template_map[f"{domain}/{template_name}"] = output_path

        return template_map

    def _render_templates(
        self, template_map: dict[str, str], context: dict
    ) -> dict[str, str]:
        """
        Render all templates with context.

        Args:
            template_map: Dict of {template_path: output_path}
            context: Template variables

        Returns:
            Dict of {output_path: rendered_content}
        """
        rendered = {}

        for template_path, output_path in template_map.items():
            # Parse template path: "domain/template.j2"
            parts = template_path.split("/")
            if len(parts) != 2:
                continue

            domain, template_name = parts

            # Render template
            content = self.template_loader.render_template(
                template_name=template_name,
                domain=domain,
                context=context,
            )

            rendered[output_path] = content

        return rendered

    def _construct_project(
        self,
        output_dir: Path,
        package_name: str,
        rendered_files: dict[str, str],
        with_spec_kit: bool = False,
    ) -> ToolkitProject:
        """
        Construct ToolkitProject from rendered templates.

        Args:
            output_dir: Output directory
            package_name: Python package name
            rendered_files: Dict of {relative_path: content}
            with_spec_kit: If True, include spec-kit capabilities

        Returns:
            ToolkitProject instance
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
        files[cli_path] = self._create_cli_stub(package_name)

        # Create parser.py stub
        parser_path = src_dir / "parser.py"
        files[parser_path] = self._create_parser_stub(package_name)

        # Create validator.py stub
        validator_path = src_dir / "validator.py"
        files[validator_path] = self._create_validator_stub(package_name)

        # Create scripts directory
        scripts_dir = Path("scripts")
        directories.add(scripts_dir)

        # Create shell scripts
        init_script = scripts_dir / "init.sh"
        files[init_script] = self._create_init_script(package_name)
        executable_files.append(init_script)

        validate_script = scripts_dir / "validate.sh"
        files[validate_script] = self._create_validate_script(package_name)
        executable_files.append(validate_script)

        # Note: Spec-kit initialization (if with_spec_kit=True) is handled
        # by the CLI after project generation via `specify init`

        # Additional directories
        directories.add(Path("templates"))
        directories.add(Path("memory"))
        directories.add(Path("examples"))

        return ToolkitProject(
            root_path=output_dir,
            files=files,
            directories=sorted(directories),
            executable_files=executable_files,
        )

    def _create_cli_stub(self, package_name: str) -> str:
        """Create CLI module stub."""
        return f'''"""
CLI for {package_name}.
"""

import typer
from rich.console import Console

app = typer.Typer(name="{package_name}")
console = Console()


@app.command()
def init(spec_file: str):
    """Initialize a new specification."""
    console.print(f"[green]Initializing:[/green] {{spec_file}}")
    # TODO: Implement initialization


@app.command()
def validate(spec_file: str):
    """Validate a specification."""
    console.print(f"[green]Validating:[/green] {{spec_file}}")
    # TODO: Implement validation


@app.command()
def generate(spec_file: str, output: str = "./output"):
    """Generate code from specification."""
    console.print(f"[green]Generating:[/green] {{spec_file}} → {{output}}")
    # TODO: Implement generation


def main():
    """Main entry point."""
    app()


if __name__ == "__main__":
    main()
'''

    def _create_parser_stub(self, package_name: str) -> str:
        """Create parser module stub."""
        return f'''"""
Specification parser for {package_name}.
"""

from pathlib import Path
from typing import Dict, Any


def parse_spec(spec_file: Path) -> Dict[str, Any]:
    """
    Parse specification file.

    Args:
        spec_file: Path to specification file

    Returns:
        Parsed specification as dict
    """
    # TODO: Implement parsing
    pass
'''

    def _create_validator_stub(self, package_name: str) -> str:
        """Create validator module stub."""
        return f'''"""
Specification validator for {package_name}.
"""

from typing import Dict, Any, List


class ValidationError:
    """Validation error."""

    def __init__(self, message: str, line: int = 0):
        self.message = message
        self.line = line


def validate_spec(spec_data: Dict[str, Any]) -> List[ValidationError]:
    """
    Validate specification data.

    Args:
        spec_data: Parsed specification

    Returns:
        List of validation errors (empty if valid)
    """
    # TODO: Implement validation
    return []
'''

    def _create_init_script(self, package_name: str) -> str:
        """Create initialization script."""
        return f'''#!/bin/bash
# Initialization script for {package_name}

set -e

echo "Initializing {package_name}..."

# Install dependencies
pip install -e .

echo "✓ {package_name} initialized successfully!"
'''

    def _create_validate_script(self, package_name: str) -> str:
        """Create validation script."""
        return f'''#!/bin/bash
# Validation script for {package_name}

set -e

if [ -z "$1" ]; then
    echo "Usage: ./validate.sh <spec-file>"
    exit 1
fi

echo "Validating $1..."
{package_name} validate "$1"
'''


def create_generator(custom_template_dir: Path | None = None) -> Generator:
    """
    Factory function to create a Generator instance.

    Args:
        custom_template_dir: Optional path to custom templates

    Returns:
        Configured Generator instance
    """
    return Generator(custom_template_dir=custom_template_dir)

