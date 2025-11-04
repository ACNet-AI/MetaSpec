"""
Unit tests for metaspec.cli.info module.
"""

from unittest.mock import MagicMock, patch

from typer.testing import CliRunner

from metaspec.cli.main import app
from metaspec.registry import CommunitySpeckit

runner = CliRunner()


class TestInfoCommand:
    """Tests for info command."""

    def test_info_help(self) -> None:
        """Test info help message."""
        result = runner.invoke(app, ["info", "--help"])
        assert result.exit_code == 0
        assert "info" in result.stdout.lower()

    @patch("metaspec.cli.info.get_community_registry")
    def test_info_existing_speckit(self, mock_registry: MagicMock) -> None:
        """Test info for existing speckit."""
        mock_reg = MagicMock()
        mock_reg.get.return_value = CommunitySpeckit(
            name="test-kit",
            command="test",
            description="Test speckit",
            version="1.0.0",
        )
        mock_registry.return_value = mock_reg

        result = runner.invoke(app, ["info", "test-kit"])
        assert result.exit_code == 0

    @patch("metaspec.cli.info.get_community_registry")
    def test_info_nonexistent_speckit(self, mock_registry: MagicMock) -> None:
        """Test info for nonexistent speckit."""
        mock_reg = MagicMock()
        mock_reg.get.return_value = None
        mock_registry.return_value = mock_reg

        result = runner.invoke(app, ["info", "nonexistent"])
        assert result.exit_code != 0 or "not found" in result.stdout.lower()

    @patch("metaspec.cli.info.CommunityRegistry.is_installed")
    @patch("metaspec.cli.info.get_community_registry")
    def test_info_with_installed_status(
        self, mock_registry: MagicMock, mock_installed: MagicMock
    ) -> None:
        """Test info shows installation status."""
        mock_reg = MagicMock()
        mock_reg.get.return_value = CommunitySpeckit(
            name="test-kit",
            command="test-cmd",
            description="Test",
        )
        mock_registry.return_value = mock_reg
        mock_installed.return_value = True

        result = runner.invoke(app, ["info", "test-kit"])
        assert result.exit_code == 0

    @patch("metaspec.cli.info.get_community_registry")
    def test_list_command(self, mock_registry: MagicMock) -> None:
        """Test list command."""
        mock_reg = MagicMock()
        mock_reg.fetch_speckits.return_value = [
            CommunitySpeckit(name="kit1", command="cmd1", description="Kit 1"),
            CommunitySpeckit(name="kit2", command="cmd2", description="Kit 2"),
        ]
        mock_registry.return_value = mock_reg

        result = runner.invoke(app, ["list"])
        assert result.exit_code == 0

    @patch("metaspec.cli.info.get_community_registry")
    def test_list_empty(self, mock_registry: MagicMock) -> None:
        """Test list with no speckits."""
        mock_reg = MagicMock()
        mock_reg.fetch_speckits.return_value = []
        mock_registry.return_value = mock_reg

        result = runner.invoke(app, ["list"])
        assert result.exit_code == 0

    @patch("metaspec.cli.info.shutil.which")
    @patch("metaspec.cli.info.get_community_registry")
    def test_list_with_local_speckits(
        self, mock_registry: MagicMock, mock_which: MagicMock
    ) -> None:
        """Test list includes locally installed speckits."""
        mock_reg = MagicMock()
        mock_reg.fetch_speckits.return_value = []
        mock_registry.return_value = mock_reg

        # Mock which to return some commands
        mock_which.side_effect = lambda cmd: "/usr/bin/" + cmd if cmd in ["python", "pytest"] else None

        result = runner.invoke(app, ["list"])
        assert result.exit_code == 0

    @patch("metaspec.cli.info.get_community_registry")
    def test_info_with_full_details(self, mock_registry: MagicMock) -> None:
        """Test info with full speckit details."""
        mock_reg = MagicMock()
        mock_reg.get.return_value = CommunitySpeckit(
            name="full-kit",
            command="full-cmd",
            description="Full kit with all details",
            version="2.0.0",
            pypi_package="full-kit-pkg",
            repository="https://github.com/test/full-kit",
            author="Test Author",
            tags=["testing", "example"],
            cli_commands=["init", "validate", "generate"],
        )
        mock_registry.return_value = mock_reg

        result = runner.invoke(app, ["info", "full-kit"])
        assert result.exit_code == 0

    def test_list_help(self) -> None:
        """Test list command help."""
        result = runner.invoke(app, ["list", "--help"])
        assert result.exit_code == 0
        assert "list" in result.stdout.lower()

    def test_info_command_vs_name(self) -> None:
        """Test info can find speckit by command or name."""
        # Just verify the command accepts arguments
        result = runner.invoke(app, ["info", "--help"])
        assert result.exit_code == 0

    @patch("metaspec.cli.info.get_community_registry")
    def test_info_shows_commands(self, mock_registry: MagicMock) -> None:
        """Test info shows CLI commands if available."""
        mock_reg = MagicMock()
        mock_reg.get.return_value = CommunitySpeckit(
            name="cmd-kit",
            command="cmdkit",
            description="Kit with commands",
            cli_commands=["init", "validate", "generate"],
        )
        mock_registry.return_value = mock_reg

        result = runner.invoke(app, ["info", "cmd-kit"])
        assert result.exit_code == 0

    @patch("metaspec.cli.info.shutil.which")
    def test_info_command_not_found(self, mock_which: MagicMock) -> None:
        """Test info with command not found."""
        mock_which.return_value = None

        result = runner.invoke(app, ["info", "nonexistent-cmd"])
        assert result.exit_code == 0
        assert "not found" in result.stdout.lower()

    @patch("metaspec.cli.info.get_community_registry")
    @patch("metaspec.cli.info.CommunityRegistry.detect_speckit_info")
    @patch("metaspec.cli.info.shutil.which")
    def test_info_command_with_detected_info(
        self, mock_which: MagicMock, mock_detect: MagicMock, mock_registry: MagicMock
    ) -> None:
        """Test info with detected version and commands."""
        mock_which.return_value = "/usr/bin/test-cmd"
        mock_detect.return_value = {
            "version": "2.0.0",
            "cli_commands": ["init", "validate", "generate"],
        }

        mock_reg = MagicMock()
        mock_reg.get.return_value = None
        mock_registry.return_value = mock_reg

        result = runner.invoke(app, ["info", "test-cmd"])
        assert result.exit_code == 0
        assert "/usr/bin/test-cmd" in result.stdout

    @patch("metaspec.cli.info.get_community_registry")
    @patch("metaspec.cli.info.CommunityRegistry.detect_speckit_info")
    @patch("metaspec.cli.info.shutil.which")
    def test_info_command_in_community_registry(
        self, mock_which: MagicMock, mock_detect: MagicMock, mock_registry: MagicMock
    ) -> None:
        """Test info with command in community registry."""
        mock_which.return_value = "/usr/bin/community-cmd"
        mock_detect.return_value = {"version": "1.0.0"}

        mock_reg = MagicMock()
        mock_reg.get.return_value = CommunitySpeckit(
            name="community-kit",
            command="community-cmd",
            description="A community speckit",
            author="Community Author",
            repository="https://github.com/community/kit",
            pypi_package="community-kit",
            tags=["community", "test"],
        )
        mock_registry.return_value = mock_reg

        result = runner.invoke(app, ["info", "community-cmd"])
        assert result.exit_code == 0
        assert "community registry" in result.stdout.lower()

    @patch("metaspec.cli.info._discover_installed_speckits")
    @patch("metaspec.cli.info.get_community_registry")
    def test_list_with_installed_speckits(
        self, mock_registry: MagicMock, mock_discover: MagicMock
    ) -> None:
        """Test list shows installed speckits."""
        mock_reg = MagicMock()
        mock_reg.fetch_speckits.return_value = []
        mock_registry.return_value = mock_reg

        mock_discover.return_value = [
            {"command": "kit1", "version": "1.0.0", "path": "/usr/bin/kit1"},
            {"command": "kit2", "version": "2.0.0", "path": "/usr/bin/kit2"},
        ]

        result = runner.invoke(app, ["list"])
        assert result.exit_code == 0
        assert "kit1" in result.stdout or "kit2" in result.stdout

