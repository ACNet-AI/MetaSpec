"""
Main CLI entry point for MetaSpec.
"""

import sys

import typer
from rich.console import Console

from metaspec.cli.contribute import contribute_command
from metaspec.cli.info import info_command, list_command
from metaspec.cli.init import init_command
from metaspec.cli.search import install_command, search_command
from metaspec.cli.sync import sync_command

app = typer.Typer(
    name="metaspec",
    help="MetaSpec - Meta-specification framework for generating Spec-Driven X (SD-X) toolkits",
    add_completion=False,
)
console = Console()


# Register commands
app.command(name="init")(init_command)
app.command(name="search")(search_command)
app.command(name="install")(install_command)
app.command(name="contribute")(contribute_command)
app.command(name="list")(list_command)
app.command(name="info")(info_command)
app.command(name="sync")(sync_command)


@app.command("version")
def version_command() -> None:
    """
    Show version information.
    """
    from metaspec import __version__
    console.print(f"MetaSpec version {__version__}")


@app.callback()
def main_callback() -> None:
    """
    MetaSpec - Meta-framework for generating Spec-Driven toolkits.

    Generate complete, production-ready toolkits from YAML definitions.
    """
    pass


def main() -> None:
    """Main entry point for the CLI."""
    try:
        app()
    except KeyboardInterrupt:
        console.print("\n[yellow]Cancelled by user[/yellow]")
        sys.exit(130)
    except Exception as e:
        console.print(f"[red]Error:[/red] {e}", style="red")
        if "--debug" in sys.argv:
            raise
        sys.exit(1)


if __name__ == "__main__":
    main()
