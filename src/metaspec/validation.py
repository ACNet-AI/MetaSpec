"""
Speckit Validation Module

Validates speckit projects meet community standards and requirements.
"""

import subprocess
import tomllib
from dataclasses import dataclass
from pathlib import Path

from rich.console import Console
from rich.table import Table

console = Console()


@dataclass
class ValidationCheck:
    """Single validation check result."""

    name: str
    passed: bool
    message: str
    fix_suggestion: str | None = None


@dataclass
class ValidationResult:
    """Complete validation result for a speckit."""

    checks: list[ValidationCheck]
    passed: bool
    warnings: list[str]

    @property
    def success_rate(self) -> float:
        """Calculate percentage of passed checks."""
        if not self.checks:
            return 0.0
        return len([c for c in self.checks if c.passed]) / len(self.checks) * 100


class SpeckitValidator:
    """Validates speckit projects for community contribution."""

    def __init__(self, project_dir: Path | None = None):
        """
        Initialize validator.

        Args:
            project_dir: Project directory to validate (default: current directory)
        """
        self.project_dir = project_dir or Path.cwd()

    def validate(self) -> ValidationResult:
        """
        Run all validation checks.

        Returns:
            ValidationResult with all check results
        """
        checks = [
            self._check_pyproject_toml(),
            self._check_readme(),
            self._check_license(),
            self._check_cli_entry(),
            self._check_github_repository(),
        ]

        passed = all(c.passed for c in checks)
        warnings = [c.message for c in checks if not c.passed]

        return ValidationResult(checks=checks, passed=passed, warnings=warnings)

    def _check_pyproject_toml(self) -> ValidationCheck:
        """Check if pyproject.toml exists and is valid."""
        pyproject_path = self.project_dir / "pyproject.toml"

        if not pyproject_path.exists():
            return ValidationCheck(
                name="pyproject.toml",
                passed=False,
                message="pyproject.toml not found",
                fix_suggestion="Create pyproject.toml with project metadata",
            )

        try:
            with open(pyproject_path, "rb") as f:
                data = tomllib.load(f)

            # Check required fields
            project = data.get("project", {})
            required_fields = ["name", "version", "description"]
            missing = [f for f in required_fields if f not in project]

            if missing:
                return ValidationCheck(
                    name="pyproject.toml",
                    passed=False,
                    message=f"Missing required fields: {', '.join(missing)}",
                    fix_suggestion=f"Add {', '.join(missing)} to [project] section",
                )

            return ValidationCheck(
                name="pyproject.toml",
                passed=True,
                message=f"Valid (name: {project['name']}, version: {project['version']})",
            )

        except Exception as e:
            return ValidationCheck(
                name="pyproject.toml",
                passed=False,
                message=f"Invalid TOML: {e!s}",
                fix_suggestion="Fix TOML syntax errors",
            )

    def _check_readme(self) -> ValidationCheck:
        """Check if README.md exists."""
        readme_variants = ["README.md", "README.MD", "readme.md", "Readme.md"]
        readme_path = None

        for variant in readme_variants:
            path = self.project_dir / variant
            if path.exists():
                readme_path = path
                break

        if not readme_path:
            return ValidationCheck(
                name="README.md",
                passed=False,
                message="README.md not found",
                fix_suggestion="Create README.md with project documentation",
            )

        # Check if README is not empty
        content = readme_path.read_text(encoding="utf-8").strip()
        if len(content) < 100:
            return ValidationCheck(
                name="README.md",
                passed=False,
                message="README.md is too short (< 100 characters)",
                fix_suggestion="Add more documentation to README.md",
            )

        return ValidationCheck(
            name="README.md",
            passed=True,
            message=f"Found ({len(content)} characters)",
        )

    def _check_license(self) -> ValidationCheck:
        """Check if LICENSE file exists."""
        license_variants = ["LICENSE", "LICENSE.md", "LICENSE.txt", "license", "License"]
        license_path = None

        for variant in license_variants:
            path = self.project_dir / variant
            if path.exists():
                license_path = path
                break

        if not license_path:
            return ValidationCheck(
                name="LICENSE",
                passed=False,
                message="LICENSE file not found",
                fix_suggestion="Add LICENSE file (e.g., MIT, Apache-2.0)",
            )

        return ValidationCheck(
            name="LICENSE",
            passed=True,
            message="Found",
        )

    def _check_cli_entry(self) -> ValidationCheck:
        """Check if CLI entry point is defined."""
        pyproject_path = self.project_dir / "pyproject.toml"

        if not pyproject_path.exists():
            return ValidationCheck(
                name="CLI Entry Point",
                passed=False,
                message="No pyproject.toml to check",
                fix_suggestion="Create pyproject.toml first",
            )

        try:
            with open(pyproject_path, "rb") as f:
                data = tomllib.load(f)

            # Check for scripts entry
            scripts = data.get("project", {}).get("scripts", {})
            if not scripts:
                return ValidationCheck(
                    name="CLI Entry Point",
                    passed=False,
                    message="No CLI entry points defined",
                    fix_suggestion="Add [project.scripts] with CLI command",
                )

            command_names = list(scripts.keys())
            return ValidationCheck(
                name="CLI Entry Point",
                passed=True,
                message=f"Found: {', '.join(command_names)}",
            )

        except Exception as e:
            return ValidationCheck(
                name="CLI Entry Point",
                passed=False,
                message=f"Error reading pyproject.toml: {e!s}",
            )

    def _check_github_repository(self) -> ValidationCheck:
        """Check if project has a GitHub repository configured."""
        # First try pyproject.toml
        pyproject_path = self.project_dir / "pyproject.toml"

        if pyproject_path.exists():
            try:
                with open(pyproject_path, "rb") as f:
                    data = tomllib.load(f)

                urls = data.get("project", {}).get("urls", {})
                repo_url = (
                    urls.get("Repository")
                    or urls.get("repository")
                    or urls.get("Source")
                    or urls.get("source")
                )

                if repo_url and "github.com" in repo_url:
                    return ValidationCheck(
                        name="GitHub Repository",
                        passed=True,
                        message=f"Found: {repo_url}",
                    )
            except Exception:
                pass

        # Try git remote
        try:
            result = subprocess.run(
                ["git", "remote", "get-url", "origin"],
                cwd=self.project_dir,
                capture_output=True,
                text=True,
                check=False,
            )

            if result.returncode == 0:
                remote_url = result.stdout.strip()
                if "github.com" in remote_url:
                    return ValidationCheck(
                        name="GitHub Repository",
                        passed=True,
                        message=f"Found: {remote_url}",
                    )

        except Exception:
            pass

        return ValidationCheck(
            name="GitHub Repository",
            passed=False,
            message="No GitHub repository URL found",
            fix_suggestion=(
                "Add repository URL to pyproject.toml [project.urls] "
                "or set git remote: git remote add origin <url>"
            ),
        )

    def display_results(self, result: ValidationResult) -> None:
        """
        Display validation results in a formatted table.

        Args:
            result: Validation result to display
        """
        table = Table(title="\n📋 Speckit Validation Results", show_header=True)
        table.add_column("Check", style="cyan", width=20)
        table.add_column("Status", width=10)
        table.add_column("Details", style="white")

        for check in result.checks:
            status = "✅ Pass" if check.passed else "❌ Fail"
            status_style = "green" if check.passed else "red"

            table.add_row(
                check.name,
                f"[{status_style}]{status}[/{status_style}]",
                check.message,
            )

        console.print(table)

        # Display summary
        success_rate = result.success_rate
        if result.passed:
            console.print(
                f"\n[green]✅ All checks passed! ({success_rate:.0f}%)[/green]"
            )
            console.print("[dim]Ready to contribute to awesome-spec-kits[/dim]")
        else:
            console.print(
                f"\n[yellow]⚠️  Some checks failed ({success_rate:.0f}% passed)[/yellow]"
            )
            console.print("\n[cyan]💡 Suggested fixes:[/cyan]")

            for check in result.checks:
                if not check.passed and check.fix_suggestion:
                    console.print(f"\n[yellow]•[/yellow] {check.name}:")
                    console.print(f"  [dim]→[/dim] {check.fix_suggestion}")

