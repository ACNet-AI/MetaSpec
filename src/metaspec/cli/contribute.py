"""
Community Contribution Command

Command for contributing speckits to the community registry.
"""

import json
import shutil
import sys
from pathlib import Path

import typer
from rich.console import Console
from rich.prompt import Confirm, Prompt

from metaspec.registry import CommunityRegistry, CommunitySpeckit

console = Console()


def contribute_command(
    command: str | None = typer.Option(
        None,
        "--command",
        "-c",
        help="Speckit command name (auto-detected if not provided)",
    ),
    interactive: bool = typer.Option(
        True,
        "--interactive/--no-interactive",
        help="Enable interactive prompts",
    ),
) -> None:
    """
    Generate metadata JSON for contributing to the community registry.

    This command helps you prepare your speckit for community contribution.

    Args:
        command: Speckit command name (auto-detected if installed)
        interactive: Enable interactive prompts (default: True)
    """
    console.print("[cyan]Contribute Speckit to Community[/cyan]\n")

    # Auto-detect command if not provided
    if command is None:
        if interactive:
            command = Prompt.ask("Speckit command name")
        else:
            console.print(
                "[red]Error: --command is required in non-interactive mode[/red]"
            )
            sys.exit(1)

    # Verify command exists
    if not shutil.which(command):
        console.print(
            f"[yellow]Warning: Command '{command}' not found in PATH[/yellow]"
        )
        if interactive:
            if not Confirm.ask("Continue anyway?", default=False):
                sys.exit(1)

    # Auto-detect info
    registry = CommunityRegistry()
    detected_info = (
        registry.detect_speckit_info(command) if shutil.which(command) else None
    ) or {}

    # Collect metadata
    if interactive:
        console.print("\n[cyan]Enter speckit information:[/cyan]")

        name = Prompt.ask("  Name", default=command)
        description = Prompt.ask("  Description")
        pypi_package = Prompt.ask("  PyPI package", default=name)
        repository = Prompt.ask("  Repository URL (optional)", default="")
        author = Prompt.ask("  Author name (optional)", default="")
        version = Prompt.ask("  Version", default=detected_info.get("version", "0.1.0"))

        # Tags
        console.print("\n  Tags (comma-separated, e.g. 'api,testing,validation'):")
        tags_input = Prompt.ask("  Tags", default="")
        tags = [t.strip() for t in tags_input.split(",") if t.strip()]

        # CLI commands
        detected_commands = detected_info.get("cli_commands", [])
        if detected_commands:
            console.print(f"\n  Detected commands: {', '.join(detected_commands)}")
            use_detected = Confirm.ask("  Use detected commands?", default=True)
            cli_commands = detected_commands if use_detected else []
        else:
            cli_commands = []

        if not cli_commands:
            console.print(
                "\n  CLI commands (comma-separated, e.g. 'init,validate,generate'):"
            )
            commands_input = Prompt.ask("  Commands", default="info")
            cli_commands = [c.strip() for c in commands_input.split(",") if c.strip()]
    else:
        # Non-interactive mode requires all info
        console.print("[red]Error: Interactive mode is required for contribute[/red]")
        console.print("Please run without --no-interactive flag")
        sys.exit(1)

    # Create metadata
    metadata = CommunitySpeckit(
        name=name,
        command=command,
        description=description,
        version=version,
        pypi_package=pypi_package if pypi_package else None,
        repository=repository if repository else None,
        author=author if author else None,
        tags=tags,
        cli_commands=cli_commands,
    )

    # Generate JSON file
    output_file = Path(f"{name}.json")
    with open(output_file, "w", encoding="utf-8") as f:
        json.dump(metadata.model_dump(), f, indent=2, ensure_ascii=False)

    console.print(f"\n[green]✓ Generated metadata:[/green] {output_file}")

    # Display next steps
    console.print("\n[cyan]Next steps to contribute to community:[/cyan]")
    console.print("  1. Review the generated JSON file")
    console.print("  2. Fork: https://github.com/ACNet-AI/awesome-spec-kits")
    console.print(f"  3. Add file: speckits/{output_file}")
    console.print("  4. Submit PR with your changes")
    console.print(
        "\n[dim]See: https://github.com/ACNet-AI/awesome-spec-kits/blob/main/CONTRIBUTING.md[/dim]"
    )
