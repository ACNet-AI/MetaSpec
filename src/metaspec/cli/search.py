"""
Community Search and Install Commands

Commands for discovering and installing speckits from the community registry.
"""

import sys

from rich.console import Console
from rich.table import Table

from metaspec.registry import get_community_registry

console = Console()


def search_command(query: str) -> None:
    """
    Search for speckits in the community registry.

    Args:
        query: Search term (searches in name, description, tags)
    """
    registry = get_community_registry()

    console.print(f"[cyan]Searching for '[bold]{query}[/bold]'...[/cyan]\n")

    results = registry.search(query)

    if not results:
        console.print("[yellow]No speckits found matching your query.[/yellow]")
        console.print("\nTry:")
        console.print("  • Different keywords")
        console.print('  • metaspec search "" to list all speckits')
        return

    # Display results
    table = Table(title=f"Found {len(results)} speckit(s)", show_header=True)
    table.add_column("Name", style="cyan", no_wrap=True)
    table.add_column("Description", style="white")
    table.add_column("Author", style="dim")
    table.add_column("Tags", style="yellow")

    for speckit in results:
        table.add_row(
            speckit.name,
            speckit.description,
            speckit.author or "—",
            ", ".join(speckit.tags) if speckit.tags else "—",
        )

    console.print(table)
    console.print("\n[dim]Install with:[/dim] metaspec install <name>")


def install_command(name: str) -> None:
    """
    Install a speckit from the community registry.

    Args:
        name: Speckit name or command to install
    """
    registry = get_community_registry()

    # Get speckit info
    speckit = registry.get(name)

    if speckit is None:
        console.print(
            f"[red]Error: Speckit '{name}' not found in community registry[/red]"
        )
        console.print("\nSearch for available speckits:")
        console.print(f'  metaspec search "{name}"')
        sys.exit(1)

    console.print(f"[cyan]Installing[/cyan] {speckit.name}...")
    console.print(f"[dim]Package:[/dim] {speckit.pypi_package or 'N/A'}")
    console.print(f"[dim]Author:[/dim] {speckit.author or 'N/A'}")

    if speckit.repository:
        console.print(f"[dim]Repository:[/dim] {speckit.repository}")

    console.print()

    # Install
    success, message = registry.install(name)

    if success:
        console.print(f"[green]✓[/green] {message}")

        # Verify installation
        if registry.is_installed(speckit.command):
            console.print(
                f"\n[green]✓ Command '[bold]{speckit.command}[/bold]' is now available[/green]"
            )

            # Try to detect version and commands
            info = registry.detect_speckit_info(speckit.command)
            if info:
                if "version" in info:
                    console.print(f"[dim]Version:[/dim] {info['version']}")
                if "cli_commands" in info:
                    console.print(
                        f"[dim]Commands:[/dim] {', '.join(info['cli_commands'])}"
                    )

            console.print("\n[cyan]Quick start:[/cyan]")
            console.print(f"  {speckit.command} --help")
        else:
            console.print(
                f"\n[yellow]Warning: Command '{speckit.command}' not found in PATH[/yellow]"
            )
            console.print("You may need to restart your shell or update PATH")
    else:
        console.print(f"[red]✗[/red] {message}")
        sys.exit(1)
