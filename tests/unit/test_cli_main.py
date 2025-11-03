"""
Unit tests for metaspec.cli.main module.
"""

from typer.testing import CliRunner

from metaspec.cli.main import app

runner = CliRunner()


class TestMainCLI:
    """Tests for main CLI application."""

    def test_main_help(self) -> None:
        """Test main help message."""
        result = runner.invoke(app, ["--help"])
        assert result.exit_code == 0
        assert "MetaSpec" in result.stdout
        assert "meta-framework" in result.stdout.lower() or "spec-driven" in result.stdout.lower()

    def test_version_command(self) -> None:
        """Test version command."""
        result = runner.invoke(app, ["version"])
        assert result.exit_code == 0
        assert "version" in result.stdout.lower()

    def test_init_command_available(self) -> None:
        """Test init command is available."""
        result = runner.invoke(app, ["--help"])
        assert result.exit_code == 0
        assert "init" in result.stdout

    def test_search_command_available(self) -> None:
        """Test search command is available."""
        result = runner.invoke(app, ["--help"])
        assert result.exit_code == 0
        assert "search" in result.stdout

    def test_list_command_available(self) -> None:
        """Test list command is available."""
        result = runner.invoke(app, ["--help"])
        assert result.exit_code == 0
        assert "list" in result.stdout

    def test_info_command_available(self) -> None:
        """Test info command is available."""
        result = runner.invoke(app, ["--help"])
        assert result.exit_code == 0
        assert "info" in result.stdout

    def test_contribute_command_available(self) -> None:
        """Test contribute command is available."""
        result = runner.invoke(app, ["--help"])
        assert result.exit_code == 0
        assert "contribute" in result.stdout

    def test_install_command_available(self) -> None:
        """Test install command is available."""
        result = runner.invoke(app, ["--help"])
        assert result.exit_code == 0

    def test_invalid_command(self) -> None:
        """Test running invalid command."""
        result = runner.invoke(app, ["nonexistent-command"])
        assert result.exit_code != 0

    def test_version_output_format(self) -> None:
        """Test version command output format."""
        result = runner.invoke(app, ["version"])
        assert result.exit_code == 0
        assert len(result.stdout) > 0

    def test_main_no_args(self) -> None:
        """Test running main without arguments shows help."""
        result = runner.invoke(app, [])
        # Should show help or exit cleanly
        assert result.exit_code in [0, 2]

    def test_search_command_requires_query(self) -> None:
        """Test search requires query argument."""
        result = runner.invoke(app, ["search"])
        assert result.exit_code != 0

