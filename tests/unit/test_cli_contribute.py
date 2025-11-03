"""
Unit tests for metaspec.cli.contribute module.
"""

from unittest.mock import MagicMock, patch

from typer.testing import CliRunner

from metaspec.cli.main import app

runner = CliRunner()


class TestContributeCommand:
    """Tests for contribute command."""

    def test_contribute_help(self) -> None:
        """Test contribute help message."""
        result = runner.invoke(app, ["contribute", "--help"])
        assert result.exit_code == 0
        assert "contribute" in result.stdout.lower()

    def test_contribute_command_option(self) -> None:
        """Test contribute has command option."""
        result = runner.invoke(app, ["contribute", "--help"])
        assert result.exit_code == 0
        assert "--command" in result.stdout

    @patch("metaspec.cli.contribute.CommunityRegistry.detect_speckit_info")
    def test_contribute_command_not_found(self, mock_detect: MagicMock) -> None:
        """Test contribute with command that doesn't exist."""
        mock_detect.return_value = None
        
        result = runner.invoke(app, ["contribute", "nonexistent-command"])
        # Should fail or warn
        assert result.exit_code != 0 or "not found" in result.stdout.lower()

    def test_contribute_requires_command(self) -> None:
        """Test that contribute requires a command argument."""
        result = runner.invoke(app, ["contribute"])
        # Should fail without command
        assert result.exit_code != 0

    def test_contribute_interactive_flag(self) -> None:
        """Test contribute has interactive flag."""
        result = runner.invoke(app, ["contribute", "--help"])
        assert result.exit_code == 0
        assert "interactive" in result.stdout.lower()

    def test_contribute_command_description(self) -> None:
        """Test contribute shows proper description."""
        result = runner.invoke(app, ["contribute", "--help"])
        assert result.exit_code == 0
        assert "community" in result.stdout.lower() or "registry" in result.stdout.lower()

