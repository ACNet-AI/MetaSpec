"""
Unit tests for metaspec.cli.search module.
"""

from unittest.mock import MagicMock, patch

from typer.testing import CliRunner

from metaspec.cli.main import app
from metaspec.registry import CommunitySpeckit

runner = CliRunner()


class TestSearchCommand:
    """Tests for search command."""

    def test_search_help(self) -> None:
        """Test search help message."""
        result = runner.invoke(app, ["search", "--help"])
        assert result.exit_code == 0
        assert "search" in result.stdout.lower()

    @patch("metaspec.cli.search.get_community_registry")
    def test_search_with_results(self, mock_registry: MagicMock) -> None:
        """Test search command with results."""
        mock_reg = MagicMock()
        mock_reg.search.return_value = [
            CommunitySpeckit(name="test-kit", command="test", description="Test kit"),
        ]
        mock_registry.return_value = mock_reg
        
        result = runner.invoke(app, ["search", "test"])
        assert result.exit_code == 0

    @patch("metaspec.cli.search.get_community_registry")
    def test_search_no_results(self, mock_registry: MagicMock) -> None:
        """Test search with no results."""
        mock_reg = MagicMock()
        mock_reg.search.return_value = []
        mock_registry.return_value = mock_reg
        
        result = runner.invoke(app, ["search", "nonexistent"])
        assert result.exit_code == 0
        assert "no speckits found" in result.stdout.lower() or "found 0" in result.stdout.lower()

    @patch("metaspec.cli.search.get_community_registry")
    def test_install_command(self, mock_registry: MagicMock) -> None:
        """Test install command."""
        mock_reg = MagicMock()
        mock_reg.install.return_value = (True, "Successfully installed")
        mock_registry.return_value = mock_reg
        
        result = runner.invoke(app, ["install", "test-kit"])
        # Should attempt installation
        assert result.exit_code == 0 or "install" in result.stdout.lower()

    @patch("metaspec.cli.search.get_community_registry")
    def test_install_failure(self, mock_registry: MagicMock) -> None:
        """Test install failure."""
        mock_reg = MagicMock()
        mock_reg.install.return_value = (False, "Installation failed")
        mock_registry.return_value = mock_reg
        
        result = runner.invoke(app, ["install", "nonexistent"])
        # Should show error
        assert result.exit_code != 0 or "fail" in result.stdout.lower()

    def test_search_requires_query(self) -> None:
        """Test search requires a query argument."""
        result = runner.invoke(app, ["search"])
        # Should fail without query
        assert result.exit_code != 0

    @patch("metaspec.cli.search.get_community_registry")
    def test_search_multiple_results(self, mock_registry: MagicMock) -> None:
        """Test search with multiple results."""
        mock_reg = MagicMock()
        mock_reg.search.return_value = [
            CommunitySpeckit(name="kit1", command="cmd1", description="Kit 1"),
            CommunitySpeckit(name="kit2", command="cmd2", description="Kit 2"),
            CommunitySpeckit(name="kit3", command="cmd3", description="Kit 3"),
        ]
        mock_registry.return_value = mock_reg
        
        result = runner.invoke(app, ["search", "kit"])
        assert result.exit_code == 0

    def test_install_help(self) -> None:
        """Test install command help."""
        result = runner.invoke(app, ["install", "--help"])
        assert result.exit_code == 0
        assert "install" in result.stdout.lower()

    @patch("metaspec.cli.search.get_community_registry")
    def test_install_not_found(self, mock_registry: MagicMock) -> None:
        """Test install with speckit not found."""
        mock_reg = MagicMock()
        mock_reg.get.return_value = None
        mock_registry.return_value = mock_reg
        
        result = runner.invoke(app, ["install", "nonexistent"])
        assert result.exit_code != 0
        assert "not found" in result.stdout.lower()

    @patch("metaspec.cli.search.get_community_registry")
    def test_install_success_with_verification(
        self, mock_registry: MagicMock
    ) -> None:
        """Test successful install with command verification."""
        mock_reg = MagicMock()
        mock_reg.get.return_value = CommunitySpeckit(
            name="test-kit",
            command="test-cmd",
            description="Test",
            pypi_package="test-kit-pkg",
            repository="https://github.com/test/test-kit",
            author="Test Author",
        )
        mock_reg.install.return_value = (True, "Successfully installed")
        mock_reg.is_installed.return_value = True
        mock_reg.detect_speckit_info.return_value = {
            "version": "1.0.0",
            "cli_commands": ["init", "validate"],
        }
        mock_registry.return_value = mock_reg
        
        result = runner.invoke(app, ["install", "test-kit"])
        assert result.exit_code == 0
        assert "successfully" in result.stdout.lower() or "✓" in result.stdout

    @patch("metaspec.cli.search.get_community_registry")
    def test_install_success_command_not_in_path(
        self, mock_registry: MagicMock
    ) -> None:
        """Test install success but command not in PATH."""
        mock_reg = MagicMock()
        mock_reg.get.return_value = CommunitySpeckit(
            name="test-kit",
            command="test-cmd",
            description="Test",
        )
        mock_reg.install.return_value = (True, "Successfully installed")
        mock_reg.is_installed.return_value = False
        mock_registry.return_value = mock_reg
        
        result = runner.invoke(app, ["install", "test-kit"])
        assert result.exit_code == 0
        assert "warning" in result.stdout.lower() or "path" in result.stdout.lower()

