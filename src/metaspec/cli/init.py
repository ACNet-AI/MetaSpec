"""
Init command for MetaSpec CLI.

Implements unified `metaspec init` command that directly creates toolkit projects.
"""

import io
import shutil
import subprocess
import sys
from pathlib import Path

import typer
from rich.console import Console
from rich.panel import Panel
from rich.progress import Progress, SpinnerColumn, TextColumn
from rich.prompt import Confirm, Prompt
from ruamel.yaml import YAML

from metaspec.core import load_meta_spec
from metaspec.generator import create_generator
from metaspec.models import MetaSpecDefinition

# Domain templates (from new_cmd)
DOMAIN_TEMPLATES = {
    "generic": {
        "name": "spec-kit",
        "description": "Generic spec-driven toolkit",
        "entity_name": "Entity",
        "fields": [
            {"name": "name", "type": "string", "required": True, "description": "Entity name"},
        ],
        "commands": [
            {"name": "init", "description": "Initialize new spec file"},
            {"name": "validate", "description": "Validate spec file"},
            {"name": "generate", "description": "Generate from spec"},
        ],
        "dependencies": ["pydantic>=2.0.0", "typer>=0.9.0", "ruamel.yaml>=0.18.0"],
    },
    "mcp": {
        "name": "mcp-spec-kit",
        "description": "Spec-driven toolkit for MCP server development",
        "entity_name": "MCPServer",
        "fields": [
            {"name": "name", "type": "string", "required": True, "description": "Server name"},
            {"name": "version", "type": "string", "required": True, "description": "Server version"},
            {"name": "capabilities", "type": "array", "required": False, "description": "Server capabilities"},
        ],
        "commands": [
            {"name": "init", "description": "Initialize new MCP server spec"},
            {"name": "validate", "description": "Validate MCP server spec"},
            {"name": "generate", "description": "Generate MCP server code"},
        ],
        "dependencies": ["pydantic>=2.0.0", "typer>=0.9.0", "ruamel.yaml>=0.18.0"],
    },
    "web": {
        "name": "web-spec-kit",
        "description": "Spec-driven toolkit for web component development",
        "entity_name": "Component",
        "fields": [
            {"name": "name", "type": "string", "required": True, "description": "Component name"},
            {"name": "props", "type": "object", "required": False, "description": "Component props"},
            {"name": "styles", "type": "object", "required": False, "description": "Component styles"},
        ],
        "commands": [
            {"name": "init", "description": "Initialize new component spec"},
            {"name": "validate", "description": "Validate component spec"},
            {"name": "generate", "description": "Generate component code"},
        ],
        "dependencies": ["pydantic>=2.0.0", "typer>=0.9.0", "ruamel.yaml>=0.18.0"],
    },
    "ai": {
        "name": "ai-agent-kit",
        "description": "Spec-driven toolkit for AI agent development",
        "entity_name": "Agent",
        "fields": [
            {"name": "name", "type": "string", "required": True, "description": "Agent name"},
            {"name": "model", "type": "string", "required": True, "description": "LLM model"},
            {"name": "capabilities", "type": "array", "required": True, "description": "Agent capabilities"},
        ],
        "commands": [
            {"name": "init", "description": "Initialize new AI agent spec"},
            {"name": "validate", "description": "Validate AI agent spec"},
            {"name": "generate", "description": "Generate AI agent code"},
        ],
        "dependencies": ["pydantic>=2.0.0", "typer>=0.9.0", "openai>=1.0.0", "ruamel.yaml>=0.18.0"],
    },
}

app = typer.Typer()
console = Console()


@app.command("init")
def init_command(
    name: str = typer.Argument(
        None,
        help="Toolkit name (e.g., 'my-spec-kit'). If not provided, starts interactive mode.",
    ),
    template: str | None = typer.Option(
        None,
        "--template",
        "-t",
        help="Use domain template (generic, mcp, web, ai) - skips interactive mode",
    ),
    output: Path | None = typer.Option(
        None,
        "--output",
        "-o",
        help="Output directory (default: ./<name>)",
    ),
    spec_kit: bool = typer.Option(
        False,
        "--spec-kit",
        help="Initialize with spec-kit capabilities (spec-driven development)",
    ),
    dry_run: bool = typer.Option(
        False,
        "--dry-run",
        help="Preview generation without creating files",
    ),
    force: bool = typer.Option(
        False,
        "--force",
        "-f",
        help="Overwrite existing output directory",
    ),
):
    """
    Create a new spec-driven toolkit (interactive or template-based).

    This command combines toolkit definition and generation in one step:
    1. Define toolkit (interactive wizard or template)
    2. Generate complete project structure
    3. Optionally initialize with spec-kit

    Examples:
        # Interactive mode (recommended for first time)
        metaspec init

        # Quick start with template
        metaspec init my-api-toolkit --template api
        metaspec init mcp-server --template mcp --spec-kit

        # Preview before creating
        metaspec init my-spec-kit --template generic --dry-run

        # Specify custom output directory
        metaspec init my-spec-kit -o ./custom-path
    """
    try:
        # Determine toolkit name
        toolkit_name = name

        # Mode 1: Template mode (fast path)
        if template:
            if not toolkit_name:
                toolkit_name = _prompt_toolkit_name_simple(template)

            meta_spec = _create_from_template(template, toolkit_name)

        # Mode 2: Interactive mode
        elif not toolkit_name:
            console.print(Panel.fit(
                "[bold cyan]MetaSpec - Create Spec-Driven Toolkit[/bold cyan]\n\n"
                "This wizard will guide you through creating a toolkit.\n"
                "Press Ctrl+C at any time to cancel.",
                border_style="cyan"
            ))

            meta_spec = _interactive_wizard()
            toolkit_name = meta_spec.name

        # Mode 3: Name only (use interactive with pre-filled name)
        else:
            console.print(Panel.fit(
                f"[bold cyan]Creating: {toolkit_name}[/bold cyan]\n\n"
                "Please provide additional information:",
                border_style="cyan"
            ))

            meta_spec = _interactive_wizard(pre_filled_name=toolkit_name)

        # Determine output directory
        if output is None:
            output = Path(f"./{toolkit_name}")

        # Check if directory exists
        if output.exists() and not force and not dry_run:
            console.print(f"\n[red]Error:[/red] Directory '{output}' already exists")
            console.print("Use [cyan]--force[/cyan] to overwrite or choose a different name")
            raise typer.Exit(1)

        # Show preview if dry-run
        if dry_run:
            _show_preview(meta_spec, output, spec_kit)
            console.print("\n[dim]This was a dry-run. No files were created.[/dim]")
            console.print(f"[dim]Run without --dry-run to create: {output}[/dim]")
            raise typer.Exit(0)

        # Generate toolkit
        console.print("\n[bold]Generating toolkit...[/bold]")

        with Progress(
            SpinnerColumn(),
            TextColumn("[progress.description]{task.description}"),
            console=console,
        ) as progress:
            gen_task = progress.add_task("Generating files...", total=None)

            # Create generator
            generator = create_generator()

            # Generate project
            project = generator.generate(
                meta_spec=meta_spec,
                output_dir=output,
                force=force,
                dry_run=False,
                with_spec_kit=False,  # We'll handle spec-kit separately
            )

            progress.update(gen_task, completed=True)
            console.print(f"[green]✓[/green] Generated {len(project.files)} files")

            # Initialize spec-kit if requested
            if spec_kit:
                speckit_task = progress.add_task("Initializing spec-kit...", total=None)

                # Check if specify command is available
                if not shutil.which("specify"):
                    console.print(
                        "\n[red]✗[/red] spec-kit not installed\n\n"
                        "To use --spec-kit, please install spec-kit first:\n"
                        "  pip install git+https://github.com/github/spec-kit.git\n\n"
                        "Or continue without spec-kit capabilities."
                    )
                    sys.exit(1)

                # Run specify init in the output directory
                try:
                    subprocess.run(
                        ["specify", "init"],
                        cwd=output,
                        check=True,
                        capture_output=True,
                        text=True,
                    )
                    progress.update(speckit_task, completed=True)
                    console.print("[green]✓[/green] Initialized spec-kit")
                except subprocess.CalledProcessError as e:
                    console.print(
                        f"\n[red]✗[/red] Failed to initialize spec-kit: {e.stderr}"
                    )
                    sys.exit(1)

        # Success message
        _show_success(meta_spec, output, spec_kit)

        sys.exit(0)

    except KeyboardInterrupt:
        console.print("\n[yellow]Cancelled by user[/yellow]")
        sys.exit(130)
    except Exception as e:
        console.print(f"\n[red]Unexpected error:[/red] {type(e).__name__}: {e}")
        if "--debug" in sys.argv:
            raise
        sys.exit(1)


def _create_from_template(template: str, toolkit_name: str) -> MetaSpecDefinition:
    """Create MetaSpecDefinition from template."""
    if template not in DOMAIN_TEMPLATES:
        console.print(f"[red]Error:[/red] Unknown template '{template}'")
        console.print(f"Available templates: {', '.join(DOMAIN_TEMPLATES.keys())}")
        raise typer.Exit(1)

    console.print(f"\n[dim]Using template: {template}[/dim]")

    # Get template data
    template_data = DOMAIN_TEMPLATES[template].copy()
    template_data["name"] = toolkit_name

    # Create MetaSpecDefinition from template data
    yaml = YAML()
    yaml_str = io.StringIO()
    yaml.dump(template_data, yaml_str)
    yaml_str.seek(0)

    meta_spec = load_meta_spec(yaml_str)
    return meta_spec


def _interactive_wizard(pre_filled_name: str | None = None) -> MetaSpecDefinition:
    """Run interactive wizard to create MetaSpecDefinition."""
    # Step 1: Basic Information
    console.print("\n[bold]Step 1/5: Basic Information[/bold]")
    console.print("─" * 60)

    domain = _prompt_domain()

    if pre_filled_name:
        toolkit_name = pre_filled_name
        console.print(f"Name: [cyan]{toolkit_name}[/cyan]")
    else:
        toolkit_name = _prompt_toolkit_name(domain)

    description = _prompt_description()

    # Step 2: Entity Design
    console.print("\n[bold]Step 2/5: Entity Design[/bold]")
    console.print("─" * 60)

    entity_name, entity_fields = _prompt_entity_design(domain)

    # Step 3: Commands
    console.print("\n[bold]Step 3/5: Command Definition[/bold]")
    console.print("─" * 60)

    commands = _prompt_commands()

    # Step 4: Dependencies
    console.print("\n[bold]Step 4/5: Dependencies[/bold]")
    console.print("─" * 60)

    dependencies = _prompt_dependencies(domain)

    # Step 5: Review
    console.print("\n[bold]Step 5/5: Review[/bold]")
    console.print("─" * 60)

    _show_summary(toolkit_name, domain, entity_name, len(entity_fields), len(commands))

    if not Confirm.ask("\n[cyan]Create toolkit with these settings?[/cyan]", default=True):
        console.print("[yellow]Cancelled by user[/yellow]")
        raise typer.Exit(0)

    # Generate meta-spec in memory (not saved to file)
    temp_output = io.StringIO()

    # Use the _generate_meta_spec_yaml logic but write to StringIO
    yaml = YAML()
    yaml.default_flow_style = False

    meta_spec_dict = {
        "name": toolkit_name,
        "version": "0.1.0",
        "domain": domain,
        "lifecycle": "greenfield",
        "description": description,
        "entity": {
            "name": entity_name,
            "fields": entity_fields,
        },
        "commands": commands,
        "dependencies": dependencies,
    }

    yaml.dump(meta_spec_dict, temp_output)
    temp_output.seek(0)

    meta_spec = load_meta_spec(temp_output)
    return meta_spec


def _prompt_toolkit_name_simple(domain: str) -> str:
    """Simple prompt for toolkit name."""
    default_name = f"{domain}-toolkit" if domain != "generic" else "my-spec-kit"

    while True:
        name = Prompt.ask(
            "Toolkit name",
            default=default_name
        )

        # Validate name
        if not name:
            console.print("[red]Name cannot be empty[/red]")
            continue

        if not name.replace("-", "").replace("_", "").isalnum():
            console.print("[red]Name must contain only alphanumeric characters, hyphens, and underscores[/red]")
            continue

        return name


def _show_preview(meta_spec: MetaSpecDefinition, output_dir: Path, spec_kit: bool):
    """Show preview of what will be generated."""
    console.print()
    console.print(
        Panel.fit(
            f"[bold cyan]Preview: {meta_spec.name}[/bold cyan]\n\n"
            f"[bold]Version:[/bold] {meta_spec.version}\n"
            f"[bold]Domain:[/bold] {meta_spec.domain}\n"
            f"[bold]Output:[/bold] {output_dir}\n"
            f"[bold]Spec-Kit:[/bold] {'Enabled' if spec_kit else 'Disabled'}",
            title="[bold]Toolkit Preview[/bold]",
            border_style="cyan"
        )
    )

    console.print("\n[bold]What will be generated:[/bold]")
    console.print("  📁 Project structure with CLI, parser, validator")
    console.print("  📝 README.md and AGENTS.md")
    console.print("  🐍 Python package with pyproject.toml")
    console.print("  📋 Templates and constitution")
    if spec_kit:
        console.print("  ✨ Spec-Kit integration (specs/ directory)")


def _show_success(meta_spec: MetaSpecDefinition, output_dir: Path, spec_kit: bool):
    """Show success message with next steps."""
    next_steps = [
        f"cd {output_dir.name}",
        "pip install -e .",
        f"{meta_spec.name.replace('-', '_')} --help",
    ]

    if spec_kit:
        next_steps.insert(1, "# Spec-driven development enabled!")
        next_steps.insert(2, "# Edit specs/spec.md to define requirements")

    console.print()
    console.print(
        Panel(
            f"[green]✓ Successfully created toolkit![/green]\n\n"
            f"[bold]Name:[/bold] {meta_spec.name}\n"
            f"[bold]Version:[/bold] {meta_spec.version}\n"
            f"[bold]Domain:[/bold] {meta_spec.domain}\n"
            f"[bold]Location:[/bold] {output_dir}\n"
            f"[bold]Spec-Kit:[/bold] {'Enabled' if spec_kit else 'Disabled'}\n\n"
            f"[dim]Next steps:[/dim]\n"
            + "\n".join(f"  {step}" for step in next_steps),
            title="[bold green]Toolkit Created[/bold green]",
            border_style="green",
        )
    )


# ============================================================================
# Helper Functions (from new_cmd.py)
# ============================================================================

def _prompt_domain() -> str:
    """Prompt for domain selection."""
    domains = {
        "1": ("generic", "Generic toolkit for any domain"),
        "2": ("mcp", "MCP server development"),
        "3": ("web", "Web development (components, APIs, etc.)"),
        "4": ("ai", "AI agent development"),
    }

    console.print("\n[cyan]Available domains:[/cyan]")
    for key, (domain, desc) in domains.items():
        console.print(f"  {key}. [bold]{domain}[/bold] - {desc}")

    choice = Prompt.ask(
        "\n[cyan]Select domain[/cyan]",
        choices=list(domains.keys()),
        default="1"
    )

    return domains[choice][0]


def _prompt_toolkit_name(domain: str) -> str:
    """Prompt for toolkit name."""
    default_name = f"{domain}-spec-kit" if domain != "generic" else "spec-kit"

    name = Prompt.ask(
        "\n[cyan]Toolkit name[/cyan] (lowercase-with-dashes)",
        default=default_name
    )

    # Validate name format
    if not name.replace("-", "").replace("_", "").isalnum():
        console.print("[yellow]Warning: Name should only contain letters, numbers, hyphens, and underscores[/yellow]")

    return name


def _prompt_description() -> str:
    """Prompt for description."""
    return Prompt.ask(
        "\n[cyan]Brief description[/cyan]",
        default="Spec-driven toolkit"
    )


def _prompt_entity_design(domain: str) -> tuple[str, list[dict]]:
    """Prompt for entity design."""
    # Suggest entity name based on domain
    suggestions = {
        "generic": "Entity",
        "mcp": "MCPServer",
        "web": "Component",
        "ai": "Agent"
    }

    entity_name = Prompt.ask(
        "\n[cyan]Main entity name[/cyan] (what does your toolkit manage?)",
        default=suggestions.get(domain, "Entity")
    )

    console.print(f"\n[cyan]Define fields for '{entity_name}':[/cyan]")
    console.print("[dim]Tips: Start with 3-5 essential fields. You can add more later.[/dim]")

    fields = []

    # Common required fields
    console.print("\n[dim]Adding common required fields...[/dim]")
    fields.append({
        "name": "name",
        "type": "string",
        "required": True,
        "description": f"{entity_name} name"
    })

    # Add custom fields
    console.print("\n[cyan]Add custom fields (press Enter with empty name to finish):[/cyan]")

    while True:
        field_name = Prompt.ask("\n  Field name", default="")

        if not field_name:
            break

        field_type = Prompt.ask(
            "  Field type",
            choices=["string", "number", "boolean", "array", "object"],
            default="string"
        )

        required = Confirm.ask("  Required?", default=False)

        description = Prompt.ask("  Description", default=f"{field_name} value")

        fields.append({
            "name": field_name,
            "type": field_type,
            "required": required,
            "description": description
        })

        console.print(f"[green]  ✓ Added field: {field_name} ({field_type})[/green]")

    return entity_name, fields


def _prompt_commands() -> list[dict]:
    """Prompt for command definitions."""
    console.print("\n[cyan]Define commands for your toolkit:[/cyan]")
    console.print("[dim]Common commands: init, validate, generate[/dim]")

    commands = []

    # Default commands
    default_commands = [
        {"name": "init", "description": "Initialize new spec file"},
        {"name": "validate", "description": "Validate spec file"},
        {"name": "generate", "description": "Generate from spec"},
    ]

    if Confirm.ask("\n[cyan]Use default commands (init, validate, generate)?[/cyan]", default=True):
        commands = default_commands
        console.print("[green]✓ Added 3 default commands[/green]")
    else:
        console.print("\n[cyan]Add custom commands (press Enter with empty name to finish):[/cyan]")

        while True:
            cmd_name = Prompt.ask("\n  Command name", default="")

            if not cmd_name:
                break

            cmd_desc = Prompt.ask("  Description", default=f"{cmd_name} operation")

            commands.append({
                "name": cmd_name,
                "description": cmd_desc
            })

            console.print(f"[green]  ✓ Added command: {cmd_name}[/green]")

    return commands


def _prompt_dependencies(domain: str) -> list[str]:
    """Prompt for dependencies."""
    console.print("\n[cyan]Python dependencies:[/cyan]")

    # Default dependencies
    defaults = [
        "pydantic>=2.0.0",
        "typer>=0.9.0",
        "ruamel.yaml>=0.18.0"
    ]

    console.print("\n[dim]Recommended dependencies:[/dim]")
    for dep in defaults:
        console.print(f"  • {dep}")

    if Confirm.ask("\n[cyan]Use recommended dependencies?[/cyan]", default=True):
        return defaults

    console.print("\n[cyan]Enter dependencies (one per line, empty to finish):[/cyan]")
    deps = []

    while True:
        dep = Prompt.ask("  Dependency", default="")
        if not dep:
            break
        deps.append(dep)

    return deps if deps else defaults


def _show_summary(name: str, domain: str, entity: str, field_count: int, command_count: int) -> None:
    """Show summary of configuration."""
    console.print("\n[cyan]Summary:[/cyan]")
    console.print(f"  • Toolkit: [bold]{name}[/bold]")
    console.print(f"  • Domain: [bold]{domain}[/bold]")
    console.print(f"  • Entity: [bold]{entity}[/bold] ({field_count} fields)")
    console.print(f"  • Commands: {command_count}")

