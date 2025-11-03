"""
Speckit Information Commands

Commands for listing and inspecting installed speckits.
"""

import os
import shutil
import subprocess
from pathlib import Path

from rich.console import Console
from rich.table import Table

from metaspec.registry import CommunityRegistry, get_community_registry

console = Console()


def list_command() -> None:
    """
    List all installed speckits.

    Automatically scans PATH for *-speckit and *-spec-kit commands.
    """
    console.print("[cyan]Scanning for installed speckits...[/cyan]\n")

    # Scan PATH for speckit commands
    speckits = _discover_installed_speckits()

    if not speckits:
        console.print("[yellow]No speckits found.[/yellow]")
        console.print("\nInstall speckits:")
        console.print("  metaspec search <query>")
        console.print("  metaspec install <name>")
        return

    # Display results
    table = Table(title=f"Installed Speckits ({len(speckits)})", show_header=True)
    table.add_column("Command", style="cyan", no_wrap=True)
    table.add_column("Version", style="white")
    table.add_column("Location", style="dim")

    for speckit in speckits:
        table.add_row(
            speckit["command"], speckit.get("version", "unknown"), speckit["path"]
        )

    console.print(table)
    console.print("\n[dim]Get details:[/dim] metaspec info <command>")
    console.print("[dim]Use directly:[/dim] <command> --help")


def info_command(command: str) -> None:
    """
    Show detailed information about a speckit.

    Args:
        command: Speckit command name
    """
    # Check if installed
    command_path = shutil.which(command)

    if command_path is None:
        console.print(f"[red]Error: Command '{command}' not found[/red]")
        console.print("\nSearch for it:")
        console.print(f'  metaspec search "{command}"')
        return

    console.print(f"[cyan]Speckit Information:[/cyan] [bold]{command}[/bold]\n")

    # Detect info
    registry = CommunityRegistry()
    detected = registry.detect_speckit_info(command)

    # Display basic info
    console.print(f"[bold]Command:[/bold] {command}")
    console.print(f"[bold]Location:[/bold] {command_path}")

    if detected:
        if "version" in detected:
            console.print(f"[bold]Version:[/bold] {detected['version']}")

        if "cli_commands" in detected and detected["cli_commands"]:
            console.print("\n[bold]Available Commands:[/bold]")
            for cmd in detected["cli_commands"]:
                console.print(f"  • {cmd}")

    # Check if in community registry
    community_registry = get_community_registry()
    community_speckit = community_registry.get(command)

    if community_speckit:
        console.print("\n[green]✓ Found in community registry[/green]")
        console.print(f"[bold]Name:[/bold] {community_speckit.name}")
        console.print(f"[bold]Description:[/bold] {community_speckit.description}")

        if community_speckit.author:
            console.print(f"[bold]Author:[/bold] {community_speckit.author}")

        if community_speckit.repository:
            console.print(f"[bold]Repository:[/bold] {community_speckit.repository}")

        if community_speckit.pypi_package:
            console.print(
                f"[bold]PyPI:[/bold] https://pypi.org/project/{community_speckit.pypi_package}"
            )

        if community_speckit.tags:
            console.print(f"[bold]Tags:[/bold] {', '.join(community_speckit.tags)}")

    # Usage hint
    console.print("\n[cyan]Usage:[/cyan]")
    console.print(f"  {command} --help")


def _discover_installed_speckits() -> list[dict]:
    """
    Discover installed speckits by scanning PATH.

    Returns:
        List of dicts with command, path, and optional version info
    """
    speckits = []
    seen_commands = set()

    # Get PATH directories
    path_dirs = os.environ.get("PATH", "").split(os.pathsep)

    for path_dir in path_dirs:
        try:
            path = Path(path_dir)
            if not path.exists() or not path.is_dir():
                continue

            # Look for *-speckit and *-spec-kit files
            for file in path.iterdir():
                if not file.is_file():
                    continue

                name = file.name

                # Check if it matches speckit naming pattern
                if not (
                    name.endswith("-speckit")
                    or name.endswith("-spec-kit")
                    or "-speckit-" in name
                    or "-spec-kit-" in name
                ):
                    continue

                # Skip if already seen
                if name in seen_commands:
                    continue

                # Check if executable
                if not os.access(file, os.X_OK):
                    continue

                seen_commands.add(name)

                # Try to get version
                version = "unknown"
                try:
                    result = subprocess.run(
                        [str(file), "--version"],
                        capture_output=True,
                        text=True,
                        timeout=1,
                        check=False,
                    )
                    if result.returncode == 0:
                        version = result.stdout.strip()
                except (subprocess.TimeoutExpired, FileNotFoundError):
                    pass

                speckits.append(
                    {
                        "command": name,
                        "path": str(file),
                        "version": version,
                    }
                )

        except (PermissionError, OSError):
            continue

    # Sort by command name
    speckits.sort(key=lambda x: x["command"])

    return speckits
