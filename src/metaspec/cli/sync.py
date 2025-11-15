"""
Sync command for updating MetaSpec commands in generated speckits.
"""

import shutil
import tomllib
from datetime import datetime
from pathlib import Path

import typer
from rich.console import Console
from rich.panel import Panel
from rich.table import Table

from metaspec import __version__ as current_version

console = Console()


def sync_command(
    check_only: bool = typer.Option(
        False,
        "--check-only",
        "-c",
        help="Check version without updating"
    ),
    force: bool = typer.Option(
        False,
        "--force",
        "-f",
        help="Force update even if versions match"
    ),
) -> None:
    """
    Sync MetaSpec commands to the latest version.

    Updates .metaspec/commands/ with the latest command documents
    from the installed MetaSpec version. Automatically creates backups.

    Example:
        $ cd my-speckit
        $ metaspec sync
    """
    # Step 1: Verify we're in a speckit directory
    if not Path("pyproject.toml").exists():
        console.print(
            "[red]Error:[/red] Not in a speckit directory (pyproject.toml not found)",
            style="red"
        )
        console.print("\n💡 Run this command from your speckit root directory")
        raise typer.Exit(1)

    # Step 2: Read generated_by version
    generated_version = _read_generated_version()

    if generated_version is None:
        console.print(
            "[yellow]Warning:[/yellow] Could not detect MetaSpec version",
            style="yellow"
        )
        console.print("This speckit may have been generated with an older MetaSpec")
        if not typer.confirm("\nContinue anyway?", default=False):
            raise typer.Exit(0)
        generated_version = "unknown"

    # Step 3: Compare versions
    console.print(Panel(
        f"[cyan]MetaSpec installed:[/cyan] {current_version}\n"
        f"[cyan]Speckit generated with:[/cyan] {generated_version}",
        title="🔍 Version Check",
        border_style="cyan"
    ))

    if generated_version == current_version and not force:
        console.print("\n✅ Already up to date!")
        return

    if generated_version == "unknown":
        console.print("\n⚠️  [yellow]Cannot determine if update is needed[/yellow]")
    elif generated_version > current_version:
        console.print(
            f"\n⚠️  [yellow]Speckit was generated with newer MetaSpec ({generated_version})[/yellow]"
        )
        console.print("Consider upgrading MetaSpec: [cyan]pip install --upgrade meta-spec[/cyan]")

    if check_only:
        if generated_version < current_version:
            console.print(
                f"\n💡 Run [cyan]metaspec sync[/cyan] to update to v{current_version}"
            )
        raise typer.Exit(0)

    # Step 4: Confirm update
    if not typer.confirm(f"\nUpdate commands to v{current_version}?", default=True):
        console.print("Cancelled")
        raise typer.Exit(0)

    # Step 5: Backup existing commands
    metaspec_dir = Path(".metaspec")
    commands_dir = metaspec_dir / "commands"

    if not commands_dir.exists():
        console.print(
            f"[red]Error:[/red] {commands_dir} not found",
            style="red"
        )
        raise typer.Exit(1)

    backup_dir = metaspec_dir / f"commands.backup-{datetime.now().strftime('%Y%m%d-%H%M%S')}"

    console.print(f"\n📦 Backing up to {backup_dir.name}...")
    shutil.copytree(commands_dir, backup_dir)
    console.print("   ✅ Backup complete")

    # Step 6: Get new commands from installed MetaSpec
    try:
        from jinja2 import FileSystemLoader, PackageLoader

        import metaspec
        from metaspec.generator import Generator
        gen = Generator()

        # Support both FileSystemLoader and PackageLoader
        if isinstance(gen.env.loader, FileSystemLoader):
            template_dir = Path(gen.env.loader.searchpath[0]) / "meta"
        elif isinstance(gen.env.loader, PackageLoader):
            # Use package location for editable installs
            template_dir = Path(metaspec.__file__).parent / "templates" / "meta"
        else:
            raise RuntimeError(f"Unsupported loader type: {type(gen.env.loader)}")

        if not template_dir.exists():
            raise RuntimeError(f"Template directory not found: {template_dir}")

    except Exception as e:
        console.print(
            "[red]Error:[/red] Could not locate MetaSpec templates: " + str(e),
            style="red"
        )
        raise typer.Exit(1) from e

    # Step 7: Copy new commands
    console.print("\n🔄 Updating commands...")

    updated_files = []
    for command_group in ["sds", "sdd", "evolution"]:
        source_dir = template_dir / command_group / "commands"
        if not source_dir.exists():
            continue

        for source_file in source_dir.glob("*.md.j2"):
            # Remove .j2 extension for destination
            # Unified naming: metaspec.{group}.{command}.md
            dest_file = commands_dir / f"metaspec.{command_group}.{source_file.stem}"

            # Read and render template (basic rendering, no complex logic)
            content = source_file.read_text()
            # Simple variable substitution for static content
            content = content.replace("{{ metaspec_version }}", current_version)

            dest_file.write_text(content)
            updated_files.append(dest_file.name)

    # Step 7.5: Clean up old Evolution naming (v0.5.x → v0.6.x migration)
    # Remove old naming pattern from pre-v0.6.0 versions
    old_evolution_files = ["metaspec.apply.md", "metaspec.archive.md", "metaspec.proposal.md"]
    for old_file_name in old_evolution_files:
        old_file = commands_dir / old_file_name
        if old_file.exists():
            console.print(f"   🧹 Removing old naming (v0.5.x): {old_file_name}")
            old_file.unlink()

    # Step 7.6: Update .metaspec/README.md (critical for consistency)
    readme_source = template_dir.parent / "base" / ".metaspec" / "README.md.j2"
    readme_dest = metaspec_dir / "README.md"
    if readme_source.exists():
        console.print(f"   📝 Updating {readme_dest.name}...")
        content = readme_source.read_text()
        # Render with speckit name from pyproject.toml
        try:
            with open("pyproject.toml", "rb") as f:
                import tomllib
                data = tomllib.load(f)
                speckit_name = data.get("project", {}).get("name", "this speckit")
                content = content.replace("{{ name }}", speckit_name)
                content = content.replace("{{ metaspec_version }}", current_version)
        except Exception:
            # Fallback if pyproject.toml can't be read
            content = content.replace("{{ name }}", "this speckit")
            content = content.replace("{{ metaspec_version }}", current_version)

        readme_dest.write_text(content)
        updated_files.append(readme_dest.name)
        console.print(f"   ✅ Updated {readme_dest.name}")

    # Step 8: Update version in pyproject.toml
    _update_generated_version(current_version)

    # Step 9: Show results
    console.print(f"   ✅ Updated {len(updated_files)} command files")

    # Create summary table
    table = Table(title="\n📊 Sync Summary", show_header=True, header_style="bold cyan")
    table.add_column("Item", style="cyan")
    table.add_column("Details", style="white")

    table.add_row("Previous version", generated_version)
    table.add_row("Current version", current_version)
    table.add_row("Files updated", str(len(updated_files)))
    table.add_row("Backup location", backup_dir.name)

    console.print(table)

    console.print("\n✅ [green]Sync complete![/green]")
    console.print("\n💡 Next steps:")
    console.print("   • Review changes: [cyan]git diff .metaspec/[/cyan]")
    console.print("   • View changelog: [cyan]https://github.com/ACNet-AI/MetaSpec/blob/main/CHANGELOG.md[/cyan]")
    console.print(f"   • Rollback if needed: [cyan]mv {backup_dir} {commands_dir}[/cyan]")


def _read_generated_version() -> str | None:
    """Read the MetaSpec version from pyproject.toml."""
    try:
        with open("pyproject.toml", "rb") as f:
            data = tomllib.load(f)
            version = data.get("tool", {}).get("metaspec", {}).get("generated_by")
            return str(version) if version is not None else None
    except Exception:
        return None


def _update_generated_version(version: str) -> None:
    """Update the generated_by version in pyproject.toml."""
    try:
        pyproject_path = Path("pyproject.toml")
        content = pyproject_path.read_text()

        # Simple regex replacement
        import re
        content = re.sub(
            r'(generated_by\s*=\s*")[^"]*(")',
            rf'\g<1>{version}\g<2>',
            content
        )

        pyproject_path.write_text(content)
    except Exception as e:
        console.print(f"[yellow]Warning:[/yellow] Could not update version in pyproject.toml: {e}")

