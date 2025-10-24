"""
Main CLI entry point for MetaSpec.
"""

import sys

import typer
from rich.console import Console

# Import command modules
from metaspec.cli.init import init_command
from metaspec.cli.spec import spec_command

app = typer.Typer(
    name="metaspec",
    help="MetaSpec - Meta-specification framework for generating Spec-Driven X (SD-X) toolkits",
    add_completion=False,
)
console = Console()


# Register commands (simple and focused)
app.command(name="init")(init_command)
app.command(name="spec")(spec_command)


@app.command("version")
def version_command():
    """
    Show version information.
    """
    console.print("MetaSpec version 0.1.0")


@app.callback()
def main_callback():
    """
    MetaSpec - Meta-framework for generating Spec-Driven toolkits.

    Generate complete, production-ready toolkits from YAML definitions.
    """
    pass


def main():
    """Main entry point for the CLI."""
    try:
        app()
    except KeyboardInterrupt:
        console.print("\n[yellow]Cancelled by user[/yellow]")
        sys.exit(130)
    except Exception as e:
        console.print(f"[red]Error:[/red] {e}", err=True)
        if "--debug" in sys.argv:
            raise
        sys.exit(1)


if __name__ == "__main__":
    main()




