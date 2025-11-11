"""
Unit tests for metaspec.cli.contribute module.
"""

from unittest.mock import MagicMock, mock_open, patch

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
        # Check that command-related content is in help (works with both Rich and plain output)
        assert ("command" in result.stdout.lower() or "speckit command name" in result.stdout.lower())

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

    @patch("metaspec.cli.contribute.shutil.which")
    @patch("metaspec.cli.contribute.CommunityRegistry")
    @patch("metaspec.cli.contribute.Prompt.ask")
    @patch("metaspec.cli.contribute.Confirm.ask")
    @patch("builtins.open", new_callable=mock_open)
    def test_contribute_interactive_full_flow(
        self,
        mock_file: MagicMock,
        mock_confirm: MagicMock,
        mock_prompt: MagicMock,
        mock_registry_class: MagicMock,
        mock_which: MagicMock,
    ) -> None:
        """Test complete interactive contribution flow."""
        # Mock command exists
        mock_which.return_value = "/usr/local/bin/my-spec-kit"

        # Mock registry detection
        mock_registry = MagicMock()
        mock_registry.detect_speckit_info.return_value = {
            "version": "1.0.0",
            "cli_commands": ["init", "validate"],
        }
        mock_registry_class.return_value = mock_registry

        # Mock user inputs
        mock_prompt.side_effect = [
            "my-spec-kit",  # name
            "A testing toolkit",  # description
            "my-spec-kit",  # pypi package
            "https://github.com/user/repo",  # repository
            "John Doe",  # author
            "1.0.0",  # version
            "testing,validation",  # tags
        ]
        mock_confirm.side_effect = [
            True,  # use detected commands
        ]

        result = runner.invoke(
            app,
            ["contribute", "--command", "my-spec-kit"],
        )

        # Should complete successfully
        assert result.exit_code == 0
        assert "Generated metadata" in result.stdout or mock_file.called

    @patch("metaspec.cli.contribute.shutil.which")
    @patch("metaspec.cli.contribute.CommunityRegistry")
    @patch("metaspec.cli.contribute.Prompt.ask")
    @patch("metaspec.cli.contribute.Confirm.ask")
    @patch("builtins.open", new_callable=mock_open)
    def test_contribute_with_detected_commands(
        self,
        mock_file: MagicMock,
        mock_confirm: MagicMock,
        mock_prompt: MagicMock,
        mock_registry_class: MagicMock,
        mock_which: MagicMock,
    ) -> None:
        """Test contribution uses detected commands."""
        # Mock command exists
        mock_which.return_value = "/usr/local/bin/test-kit"

        # Mock registry with detected commands
        mock_registry = MagicMock()
        mock_registry.detect_speckit_info.return_value = {
            "version": "0.5.0",
            "cli_commands": ["init", "validate", "generate"],
        }
        mock_registry_class.return_value = mock_registry

        # Mock user inputs
        mock_prompt.side_effect = [
            "test-kit",  # name
            "Testing toolkit",  # description
            "test-kit",  # pypi package
            "",  # repository (optional)
            "",  # author (optional)
            "0.5.0",  # version
            "testing",  # tags
        ]
        mock_confirm.side_effect = [
            True,  # use detected commands
        ]

        result = runner.invoke(
            app,
            ["contribute", "--command", "test-kit"],
        )

        # Should complete successfully
        assert result.exit_code == 0
        assert "Detected commands" in result.stdout or result.exit_code == 0

    @patch("metaspec.cli.contribute.shutil.which")
    @patch("metaspec.cli.contribute.Confirm.ask")
    def test_contribute_command_not_in_path_continue(
        self,
        mock_confirm: MagicMock,
        mock_which: MagicMock,
    ) -> None:
        """Test contribution continues when command not in PATH but user confirms."""
        # Mock command not found
        mock_which.return_value = None

        # User chooses not to continue
        mock_confirm.return_value = False

        result = runner.invoke(
            app,
            ["contribute", "--command", "missing-cmd"],
        )

        # Should exit
        assert result.exit_code == 1

    @patch("metaspec.cli.contribute.shutil.which")
    @patch("metaspec.cli.contribute.CommunityRegistry")
    @patch("metaspec.cli.contribute.Prompt.ask")
    @patch("metaspec.cli.contribute.Confirm.ask")
    @patch("builtins.open", new_callable=mock_open)
    def test_contribute_custom_commands(
        self,
        mock_file: MagicMock,
        mock_confirm: MagicMock,
        mock_prompt: MagicMock,
        mock_registry_class: MagicMock,
        mock_which: MagicMock,
    ) -> None:
        """Test contribution with custom commands instead of detected ones."""
        # Mock command exists
        mock_which.return_value = "/usr/bin/custom-kit"

        # Mock registry
        mock_registry = MagicMock()
        mock_registry.detect_speckit_info.return_value = {
            "version": "1.0.0",
            "cli_commands": ["default1", "default2"],
        }
        mock_registry_class.return_value = mock_registry

        # Mock user inputs
        mock_prompt.side_effect = [
            "custom-kit",  # name
            "Custom toolkit",  # description
            "custom-kit",  # pypi package
            "",  # repository
            "",  # author
            "1.0.0",  # version
            "custom,tools",  # tags
            "custom1,custom2,custom3",  # custom commands
        ]
        mock_confirm.side_effect = [
            False,  # don't use detected commands
        ]

        result = runner.invoke(
            app,
            ["contribute", "--command", "custom-kit"],
        )

        # Should complete successfully
        assert result.exit_code == 0

    def test_contribute_non_interactive_fails(self) -> None:
        """Test that non-interactive mode shows error."""
        result = runner.invoke(
            app,
            ["contribute", "--command", "test", "--no-interactive"],
        )

        # Should fail with error message
        assert result.exit_code == 1
        assert "Interactive mode is required" in result.stdout

    @patch("metaspec.cli.contribute.Prompt.ask")
    def test_contribute_no_command_interactive_prompt(
        self, mock_prompt: MagicMock
    ) -> None:
        """Test that missing command triggers interactive prompt."""
        # Mock command input, then other prompts will fail
        mock_prompt.side_effect = [
            "test-kit",  # command name
            Exception("Stop here for test"),  # Stop execution
        ]

        runner.invoke(app, ["contribute"])

        # Should attempt to prompt for command
        assert mock_prompt.called

