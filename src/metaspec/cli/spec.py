"""
Spec command - Unified interface for managing and using spec toolkits.

This command provides:
1. Discovery of available spec toolkits
2. Unified interface to execute toolkit commands
3. Extension point for custom toolkits (future)
"""

import subprocess

import typer
from rich.console import Console
from rich.table import Table

from metaspec.spec_protocol import BUILTIN_TOOLKITS

console = Console()


def spec_command(
    toolkit: str | None = typer.Argument(
        None,
        help="Toolkit name (e.g., spec-kit, openspec, api-spec-kit)",
    ),
    command: str | None = typer.Argument(
        None,
        help="Command to execute in the toolkit",
    ),
    args: list[str] = typer.Argument(
        None,
        help="Additional arguments to pass to the command",
    ),
    list_toolkits: bool = typer.Option(
        False,
        "--list",
        "-l",
        help="List all available spec toolkits",
    ),
    info: str | None = typer.Option(
        None,
        "--info",
        "-i",
        help="Show detailed information about a toolkit",
    ),
) -> None:
    """
    Manage and use spec toolkits.

    MetaSpec provides a unified interface to work with various spec toolkits:
    - Built-in: spec-kit, openspec
    - Custom: Any toolkit created with MetaSpec

    Examples:
        # List available toolkits
        metaspec spec --list

        # Get info about a toolkit
        metaspec spec --info spec-kit

        # Use spec-kit
        metaspec spec spec-kit init
        metaspec spec spec-kit spec

        # Use openspec
        metaspec spec openspec analyze
        metaspec spec openspec plan

        # Use custom toolkit (if installed)
        metaspec spec api-spec-kit init my-api.yaml
    """
    # Handle --list flag
    if list_toolkits:
        _list_toolkits()
        return

    # Handle --info flag
    if info:
        _show_toolkit_info(info)
        return

    # Execute toolkit command
    if not toolkit:
        console.print("[red]Error: Toolkit name is required[/red]")
        console.print("\nUse [cyan]metaspec spec --list[/cyan] to see available toolkits")
        raise typer.Exit(1)

    if not command:
        console.print(f"[red]Error: Command is required for toolkit '{toolkit}'[/red]")
        console.print(f"\nUse [cyan]metaspec spec --info {toolkit}[/cyan] to see available commands")
        raise typer.Exit(1)

    # Execute the command
    exit_code = _execute_toolkit_command(toolkit, command, args or [])
    if exit_code != 0:
        raise typer.Exit(exit_code)


def _list_toolkits() -> None:
    """List all available spec toolkits"""
    console.print("\n[bold]📦 Available Spec Toolkits[/bold]\n")

    # Built-in toolkits
    console.print("[bold cyan]Built-in:[/bold cyan]")
    table = Table(show_header=True, header_style="bold")
    table.add_column("Name", style="cyan")
    table.add_column("Description")
    table.add_column("Status")

    for name, toolkit in BUILTIN_TOOLKITS.items():
        # Check if command is available
        status = _check_command_available(toolkit.command_name)
        table.add_row(
            name,
            toolkit.description,
            status,
        )

    console.print(table)

    # Custom toolkits (future)
    console.print("\n[bold cyan]Custom:[/bold cyan]")
    console.print("  [dim]No custom toolkits installed[/dim]")
    console.print("  [dim]Create your own with: metaspec init my-spec-kit[/dim]\n")


def _show_toolkit_info(toolkit_name: str) -> None:
    """Show detailed information about a specific toolkit"""
    if toolkit_name in BUILTIN_TOOLKITS:
        toolkit = BUILTIN_TOOLKITS[toolkit_name]
        console.print(f"\n[bold]📋 Toolkit: {toolkit.name}[/bold]\n")
        console.print(f"Description: {toolkit.description}")
        console.print(f"Command: [cyan]{toolkit.command_name}[/cyan]")
        console.print("\nAvailable commands:")
        for cmd in toolkit.commands:
            console.print(f"  • [cyan]{cmd}[/cyan]")
        console.print(f"\nUsage: [cyan]metaspec spec {toolkit_name} <command>[/cyan]\n")
    else:
        console.print(f"[red]Error: Toolkit '{toolkit_name}' not found[/red]")
        console.print("\nUse [cyan]metaspec spec --list[/cyan] to see available toolkits")
        raise typer.Exit(1)


def _execute_toolkit_command(toolkit_name: str, command: str, args: list[str]) -> int:
    """Execute a command in the specified toolkit"""
    # Check if it's a built-in toolkit
    if toolkit_name in BUILTIN_TOOLKITS:
        toolkit = BUILTIN_TOOLKITS[toolkit_name]

        # Check if command is available
        if not _is_command_available(toolkit.command_name):
            console.print(
                f"[red]Error: '{toolkit.command_name}' command not found[/red]\n"
            )
            console.print(f"Please install {toolkit_name} first:")
            if toolkit_name == "spec-kit":
                console.print("  pip install git+https://github.com/github/spec-kit.git")
            elif toolkit_name == "openspec":
                console.print("  pip install git+https://github.com/Fission-AI/OpenSpec.git")
            return 127

        # Execute the command
        console.print(f"[dim]→ Executing: {toolkit.command_name} {command} {' '.join(args)}[/dim]\n")
        return toolkit.execute(command, args)

    # Try to execute as custom toolkit (assume command exists)
    try:
        console.print(f"[dim]→ Trying custom toolkit: {toolkit_name} {command} {' '.join(args)}[/dim]\n")
        result = subprocess.run(
            [toolkit_name, command, *args],
            check=False,
        )
        return result.returncode
    except FileNotFoundError:
        console.print(f"[red]Error: Toolkit '{toolkit_name}' not found[/red]")
        console.print("\nMake sure:")
        console.print(f"  1. The toolkit is installed: pip install {toolkit_name}")
        console.print("  2. Or use: metaspec spec --list to see available toolkits")
        return 127


def _check_command_available(command: str) -> str:
    """Check if a command is available in PATH"""
    if _is_command_available(command):
        return "[green]✓ Installed[/green]"
    return "[yellow]○ Not installed[/yellow]"


def _is_command_available(command: str) -> bool:
    """Check if a command exists in PATH"""
    try:
        result = subprocess.run(
            [command, "--version"],
            capture_output=True,
            check=False,
            timeout=2,
        )
        return result.returncode == 0
    except (FileNotFoundError, subprocess.TimeoutExpired):
        return False

