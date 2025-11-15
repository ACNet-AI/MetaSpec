"""
Community Contribution Command

Command for contributing speckits to the community registry.
"""

import json
import sys
import tomllib
import webbrowser
from pathlib import Path
from urllib.parse import urlencode

import typer
from rich.console import Console
from rich.panel import Panel

from metaspec.registry import CommunitySpeckit
from metaspec.validation import SpeckitValidator

console = Console()


def contribute_command(
    open_browser: bool = typer.Option(
        False,
        "--open",
        help="Open GitHub issue page in browser after validation",
    ),
    check_only: bool = typer.Option(
        False,
        "--check-only",
        help="Only validate requirements without opening browser",
    ),
    save_json: bool = typer.Option(
        False,
        "--save-json",
        help="Save metadata to JSON file (for preview)",
    ),
) -> None:
    """
    Validate and submit your speckit to the community registry.

    This command validates your speckit and helps you contribute it to
    awesome-spec-kits. The bot will automatically extract metadata from
    your repository.

    Args:
        open_browser: Open pre-filled GitHub issue page
        check_only: Only validate, don't open browser
        save_json: Save metadata JSON for preview (optional)
    """
    console.print("[cyan]🚀 Contribute Speckit to Community[/cyan]\n")

    # Step 1: Validate speckit requirements
    validator = SpeckitValidator()
    validation_result = validator.validate()
    validator.display_results(validation_result)

    # If check-only mode, exit after validation
    if check_only:
        sys.exit(0 if validation_result.passed else 1)

    # If validation failed, cannot continue
    if not validation_result.passed:
        console.print()
        console.print("[yellow]⚠️  Please fix the issues above before contributing[/yellow]")
        console.print("\n[dim]Tip: Re-run validation with --check-only[/dim]")
        sys.exit(1)

    console.print()

    # Step 2: Extract repository information
    repo_url = _extract_repository_url()
    if not repo_url:
        console.print("[red]❌ Could not detect repository URL[/red]")
        console.print("\n💡 Please add repository URL to pyproject.toml:")
        console.print('   [project.urls]')
        console.print('   repository = "https://github.com/user/repo"')
        sys.exit(1)

    # Step 3: Extract metadata for preview
    metadata_info = _extract_metadata_info()

    # Display what the bot will extract
    console.print("[cyan]📊 Bot will extract:[/cyan]")
    info_panel = Panel(
        f"[white]Repository:[/white] {repo_url}\n"
        f"[white]Name:[/white] {metadata_info.get('name', 'N/A')}\n"
        f"[white]Version:[/white] {metadata_info.get('version', 'N/A')}\n"
        f"[white]Description:[/white] {metadata_info.get('description', 'N/A')}\n"
        f"[white]CLI Commands:[/white] {', '.join(metadata_info.get('cli_commands', [])) or 'N/A'}",
        title="📋 Metadata Preview",
        border_style="cyan",
    )
    console.print(info_panel)

    # Step 4: Generate issue URL
    speckit_name = metadata_info.get("name", Path.cwd().name)
    issue_url = _generate_issue_url(repo_url, speckit_name)

    # Step 5: Save JSON if requested
    if save_json:
        metadata = CommunitySpeckit(
            name=metadata_info.get("name", ""),
            command=metadata_info.get("command", ""),
            description=metadata_info.get("description", ""),
            version=metadata_info.get("version", "0.1.0"),
            repository=repo_url,
            cli_commands=metadata_info.get("cli_commands", []),
        )
        output_file = Path(f"{metadata_info.get('name', 'speckit')}.json")
        with open(output_file, "w", encoding="utf-8") as f:
            json.dump(metadata.model_dump(exclude_none=True), f, indent=2, ensure_ascii=False)
        console.print(f"\n[green]✅ Saved preview:[/green] {output_file}")
        console.print("[dim]Note: This is for preview only. The bot extracts metadata from your repo.[/dim]")

    # Step 6: Important reminder about required checkboxes
    console.print()
    reminder_panel = Panel(
        "[green]✅ We've already validated these (you can check them immediately):[/green]\n"
        "[dim]✓ pyproject.toml with name, version, description[/dim]\n"
        "[dim]✓ README.md documentation[/dim]\n"
        "[dim]✓ CLI commands in [project.scripts][/dim]\n"
        "[dim]✓ Open source license[/dim]\n\n"
        "[yellow]⚠️  Please confirm manually on GitHub:[/yellow]\n"
        "[white]✓ I am the maintainer or have permission to register this speckit[/white]\n\n"
        "[dim]Note: GitHub requires all 5 boxes checked, even though we've verified 4.\n"
        "This is a GitHub security limitation (can't pre-check required boxes via URL).[/dim]",
        title="📋 GitHub Issue Checkboxes",
        border_style="cyan",
    )
    console.print(reminder_panel)

    # Step 7: Open browser or show URL
    console.print()
    if open_browser:
        console.print("[cyan]🌐 Opening GitHub in your browser...[/cyan]")
        try:
            webbrowser.open(issue_url)
            console.print("[green]✅ Browser opened![/green]")
        except Exception as e:
            console.print(f"[yellow]⚠️  Could not open browser: {e}[/yellow]")
            console.print(f"\n[cyan]📋 Registration URL:[/cyan]\n{issue_url}")
    else:
        console.print("[cyan]📋 Next step: Create registration issue[/cyan]")
        console.print(f"\n{issue_url}")
        console.print("\n💡 [dim]Tip: Use --open to open in browser automatically[/dim]")

    console.print()
    console.print("[green]🎉 Ready to contribute![/green]")
    console.print("\n[dim]What happens next:[/dim]")
    console.print("[dim]  1. Check the 5 required checkboxes[/dim]")
    console.print("[dim]  2. Submit the Issue[/dim]")
    console.print("[dim]  3. Bot validates your repository[/dim]")
    console.print("[dim]  4. Bot extracts metadata from pyproject.toml[/dim]")
    console.print("[dim]  5. Bot creates PR automatically[/dim]")
    console.print("[dim]  6. Maintainers review and merge[/dim]")


def _extract_repository_url() -> str | None:
    """Extract repository URL from pyproject.toml or git remote."""
    # Try pyproject.toml first
    pyproject_path = Path("pyproject.toml")
    if pyproject_path.exists():
        try:
            with open(pyproject_path, "rb") as f:
                data = tomllib.load(f)
            urls = data.get("project", {}).get("urls", {})
            repo_url_raw = (
                urls.get("Repository")
                or urls.get("repository")
                or urls.get("Source")
                or urls.get("source")
                or urls.get("Homepage")
                or urls.get("homepage")
            )
            if repo_url_raw and isinstance(repo_url_raw, str) and "github.com" in repo_url_raw:
                return str(repo_url_raw).rstrip("/")
        except Exception:
            pass

    # Try git remote
    import subprocess
    try:
        result = subprocess.run(
            ["git", "remote", "get-url", "origin"],
            capture_output=True,
            text=True,
            check=False,
        )
        if result.returncode == 0:
            remote_url = result.stdout.strip()
            # Convert git URL to HTTPS
            if remote_url.startswith("git@github.com:"):
                remote_url = remote_url.replace("git@github.com:", "https://github.com/")
            if remote_url.endswith(".git"):
                remote_url = remote_url[:-4]
            if "github.com" in remote_url:
                return remote_url.rstrip("/")
    except Exception:
        pass

    return None


def _extract_metadata_info() -> dict:
    """Extract metadata from pyproject.toml."""
    pyproject_path = Path("pyproject.toml")
    if not pyproject_path.exists():
        return {}

    try:
        with open(pyproject_path, "rb") as f:
            data = tomllib.load(f)

        project = data.get("project", {})
        scripts = project.get("scripts", {})

        return {
            "name": project.get("name", ""),
            "version": project.get("version", ""),
            "description": project.get("description", ""),
            "command": list(scripts.keys())[0] if scripts else "",
            "cli_commands": list(scripts.keys()),
        }
    except Exception:
        return {}


def _generate_issue_url(repo_url: str, speckit_name: str) -> str:
    """Generate pre-filled GitHub issue URL for awesome-spec-kits."""
    base_url = "https://github.com/ACNet-AI/awesome-spec-kits/issues/new"

    # Use the correct issue template name (GitHub Issue Forms)
    # Template file: .github/ISSUE_TEMPLATE/register-speckit.yml
    params = {
        "template": "register-speckit.yml",  # Correct template name
        "title": f"[Register] {speckit_name}",  # Issue title
        "repository": repo_url,  # Matches "id: repository" in template
    }

    return f"{base_url}?{urlencode(params)}"
