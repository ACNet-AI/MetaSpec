"""
Unit tests for metaspec.cli.contribute module.
"""

from pathlib import Path
from unittest.mock import MagicMock, patch

from typer.testing import CliRunner

from metaspec.cli.main import app
from metaspec.validation import ValidationCheck, ValidationResult

runner = CliRunner()


def create_passing_validation_result() -> ValidationResult:
    """Create a passing validation result for tests."""
    checks = [
        ValidationCheck(
            name="pyproject.toml",
            passed=True,
            message="Valid (name: test, version: 1.0.0)",
        ),
        ValidationCheck(
            name="README.md",
            passed=True,
            message="Found (100 characters)",
        ),
        ValidationCheck(
            name="LICENSE",
            passed=True,
            message="Found",
        ),
        ValidationCheck(
            name="CLI Entry Point",
            passed=True,
            message="Found: test-command",
        ),
        ValidationCheck(
            name="GitHub Repository",
            passed=True,
            message="Found: https://github.com/test/repo",
        ),
    ]
    return ValidationResult(checks=checks, passed=True, warnings=[])


def create_failing_validation_result() -> ValidationResult:
    """Create a failing validation result for tests."""
    checks = [
        ValidationCheck(
            name="pyproject.toml",
            passed=False,
            message="Not found",
        ),
    ]
    return ValidationResult(checks=checks, passed=False, warnings=[])


class TestContributeCommand:
    """Tests for contribute command."""

    def test_contribute_help(self) -> None:
        """Test contribute help message."""
        result = runner.invoke(app, ["contribute", "--help"])
        assert result.exit_code == 0
        assert "contribute" in result.stdout.lower()

    def test_contribute_has_open_flag(self) -> None:
        """Test contribute has --open flag."""
        result = runner.invoke(app, ["contribute", "--help"])
        assert result.exit_code == 0
        assert "open" in result.stdout.lower()

    def test_contribute_has_check_only_flag(self) -> None:
        """Test contribute has --check-only flag."""
        result = runner.invoke(app, ["contribute", "--help"])
        assert result.exit_code == 0
        # Rich may add ANSI codes that break up the string, so check both parts
        stdout_lower = result.stdout.lower()
        assert "check" in stdout_lower and "only" in stdout_lower

    def test_contribute_has_save_json_flag(self) -> None:
        """Test contribute has --save-json flag."""
        result = runner.invoke(app, ["contribute", "--help"])
        assert result.exit_code == 0
        # Rich may add ANSI codes that break up the string, so check both parts
        stdout_lower = result.stdout.lower()
        assert "save" in stdout_lower and "json" in stdout_lower

    def test_contribute_command_description(self) -> None:
        """Test contribute shows proper description."""
        result = runner.invoke(app, ["contribute", "--help"])
        assert result.exit_code == 0
        assert "community" in result.stdout.lower() or "registry" in result.stdout.lower()

    @patch("metaspec.cli.contribute.SpeckitValidator")
    def test_contribute_check_only_passing(
        self,
        mock_validator_class: MagicMock,
    ) -> None:
        """Test contribute with --check-only and passing validation."""
        mock_validator = mock_validator_class.return_value
        mock_validator.validate.return_value = create_passing_validation_result()

        result = runner.invoke(app, ["contribute", "--check-only"])

        assert result.exit_code == 0
        assert mock_validator.validate.called
        assert mock_validator.display_results.called

    @patch("metaspec.cli.contribute.SpeckitValidator")
    def test_contribute_check_only_failing(
        self,
        mock_validator_class: MagicMock,
    ) -> None:
        """Test contribute with --check-only and failing validation."""
        mock_validator = mock_validator_class.return_value
        mock_validator.validate.return_value = create_failing_validation_result()

        result = runner.invoke(app, ["contribute", "--check-only"])

        assert result.exit_code == 1
        assert mock_validator.validate.called

    @patch("metaspec.cli.contribute.SpeckitValidator")
    @patch("metaspec.cli.contribute._extract_repository_url")
    @patch("metaspec.cli.contribute._extract_metadata_info")
    def test_contribute_default_flow(
        self,
        mock_extract_metadata: MagicMock,
        mock_extract_repo: MagicMock,
        mock_validator_class: MagicMock,
    ) -> None:
        """Test contribute default flow (validation + URL display)."""
        # Setup mocks
        mock_validator = mock_validator_class.return_value
        mock_validator.validate.return_value = create_passing_validation_result()
        mock_extract_repo.return_value = "https://github.com/test/repo"
        mock_extract_metadata.return_value = {
            "name": "test-spec",
            "version": "1.0.0",
            "description": "Test description",
            "cli_commands": ["test"],
        }

        result = runner.invoke(app, ["contribute"])

        assert result.exit_code == 0
        assert "Bot will extract" in result.stdout
        assert "https://github.com/test/repo" in result.stdout
        assert "Next step" in result.stdout
        assert mock_extract_repo.called

    @patch("metaspec.cli.contribute.SpeckitValidator")
    @patch("metaspec.cli.contribute._extract_repository_url")
    def test_contribute_no_repository(
        self,
        mock_extract_repo: MagicMock,
        mock_validator_class: MagicMock,
    ) -> None:
        """Test contribute when repository URL cannot be detected."""
        mock_validator = mock_validator_class.return_value
        mock_validator.validate.return_value = create_passing_validation_result()
        mock_extract_repo.return_value = None

        result = runner.invoke(app, ["contribute"])

        assert result.exit_code == 1
        assert "Could not detect repository URL" in result.stdout
        assert "pyproject.toml" in result.stdout

    @patch("metaspec.cli.contribute.SpeckitValidator")
    @patch("metaspec.cli.contribute._extract_repository_url")
    @patch("metaspec.cli.contribute._extract_metadata_info")
    @patch("metaspec.cli.contribute.webbrowser.open")
    def test_contribute_with_open_flag(
        self,
        mock_webbrowser: MagicMock,
        mock_extract_metadata: MagicMock,
        mock_extract_repo: MagicMock,
        mock_validator_class: MagicMock,
    ) -> None:
        """Test contribute with --open flag opens browser."""
        # Setup mocks
        mock_validator = mock_validator_class.return_value
        mock_validator.validate.return_value = create_passing_validation_result()
        mock_extract_repo.return_value = "https://github.com/test/repo"
        mock_extract_metadata.return_value = {
            "name": "test-spec",
            "version": "1.0.0",
            "description": "Test description",
            "cli_commands": ["test"],
        }

        result = runner.invoke(app, ["contribute", "--open"])

        assert result.exit_code == 0
        assert mock_webbrowser.called
        assert "Browser opened" in result.stdout or "Opening GitHub" in result.stdout

    @patch("metaspec.cli.contribute.SpeckitValidator")
    @patch("metaspec.cli.contribute._extract_repository_url")
    @patch("metaspec.cli.contribute._extract_metadata_info")
    @patch("builtins.open")
    @patch("metaspec.cli.contribute.json.dump")
    def test_contribute_with_save_json_flag(
        self,
        mock_json_dump: MagicMock,
        mock_open: MagicMock,
        mock_extract_metadata: MagicMock,
        mock_extract_repo: MagicMock,
        mock_validator_class: MagicMock,
    ) -> None:
        """Test contribute with --save-json flag saves metadata."""
        # Setup mocks
        mock_validator = mock_validator_class.return_value
        mock_validator.validate.return_value = create_passing_validation_result()
        mock_extract_repo.return_value = "https://github.com/test/repo"
        mock_extract_metadata.return_value = {
            "name": "test-spec",
            "version": "1.0.0",
            "description": "Test description",
            "command": "test",
            "cli_commands": ["test"],
        }

        result = runner.invoke(app, ["contribute", "--save-json"])

        assert result.exit_code == 0
        assert "Saved preview" in result.stdout
        assert mock_json_dump.called

    @patch("metaspec.cli.contribute.SpeckitValidator")
    def test_contribute_failing_validation_stops(
        self,
        mock_validator_class: MagicMock,
    ) -> None:
        """Test contribute stops if validation fails."""
        mock_validator = mock_validator_class.return_value
        mock_validator.validate.return_value = create_failing_validation_result()

        result = runner.invoke(app, ["contribute"])

        assert result.exit_code == 1
        assert "Please fix the issues" in result.stdout


class TestExtractRepositoryUrl:
    """Tests for _extract_repository_url helper function."""

    @patch("metaspec.cli.contribute.Path")
    @patch("builtins.open")
    @patch("metaspec.cli.contribute.tomllib.load")
    def test_extract_from_pyproject_toml(
        self,
        mock_toml_load: MagicMock,
        mock_open: MagicMock,
        mock_path: MagicMock,
    ) -> None:
        """Test extracting repository URL from pyproject.toml."""
        from metaspec.cli.contribute import _extract_repository_url

        # Setup mocks
        mock_path_instance = MagicMock(spec=Path)
        mock_path_instance.exists.return_value = True
        mock_path.return_value = mock_path_instance

        mock_toml_load.return_value = {
            "project": {
                "urls": {
                    "repository": "https://github.com/test/repo",
                }
            }
        }

        with patch("metaspec.cli.contribute.Path", return_value=mock_path_instance):
            result = _extract_repository_url()

        assert result == "https://github.com/test/repo"

    @patch("metaspec.cli.contribute.Path")
    def test_extract_from_git_remote(
        self,
        mock_path: MagicMock,
    ) -> None:
        """Test extracting repository URL from git remote."""
        from metaspec.cli.contribute import _extract_repository_url

        # Setup mocks - pyproject.toml doesn't exist
        mock_path_instance = MagicMock(spec=Path)
        mock_path_instance.exists.return_value = False
        mock_path.return_value = mock_path_instance

        # Mock subprocess.run (imported inside the function)
        with patch("metaspec.cli.contribute.Path", return_value=mock_path_instance):
            with patch("subprocess.run") as mock_subprocess:
                mock_subprocess.return_value = MagicMock(
                    returncode=0,
                    stdout="https://github.com/test/repo.git\n",
                )
                result = _extract_repository_url()

        assert result == "https://github.com/test/repo"

    @patch("metaspec.cli.contribute.Path")
    def test_extract_returns_none_when_not_found(
        self,
        mock_path: MagicMock,
    ) -> None:
        """Test _extract_repository_url returns None when not found."""
        from metaspec.cli.contribute import _extract_repository_url

        mock_path_instance = MagicMock(spec=Path)
        mock_path_instance.exists.return_value = False

        with patch("metaspec.cli.contribute.Path", return_value=mock_path_instance):
            with patch("subprocess.run") as mock_subprocess:
                mock_subprocess.return_value = MagicMock(returncode=1)
                result = _extract_repository_url()

        assert result is None


class TestExtractMetadataInfo:
    """Tests for _extract_metadata_info helper function."""

    @patch("metaspec.cli.contribute.Path")
    @patch("builtins.open")
    @patch("metaspec.cli.contribute.tomllib.load")
    def test_extract_metadata_from_pyproject(
        self,
        mock_toml_load: MagicMock,
        mock_open: MagicMock,
        mock_path: MagicMock,
    ) -> None:
        """Test extracting metadata from pyproject.toml."""
        from metaspec.cli.contribute import _extract_metadata_info

        # Setup mocks
        mock_path_instance = MagicMock(spec=Path)
        mock_path_instance.exists.return_value = True
        mock_path.return_value = mock_path_instance

        mock_toml_load.return_value = {
            "project": {
                "name": "test-spec",
                "version": "1.0.0",
                "description": "Test description",
                "scripts": {
                    "test-cmd": "module:main",
                },
            }
        }

        with patch("metaspec.cli.contribute.Path", return_value=mock_path_instance):
            result = _extract_metadata_info()

        assert result["name"] == "test-spec"
        assert result["version"] == "1.0.0"
        assert result["description"] == "Test description"
        assert result["cli_commands"] == ["test-cmd"]


class TestGenerateIssueUrl:
    """Tests for _generate_issue_url helper function."""

    def test_generate_issue_url_format(self) -> None:
        """Test issue URL format is correct."""
        from metaspec.cli.contribute import _generate_issue_url

        repo_url = "https://github.com/test/repo"
        speckit_name = "test-speckit"
        result = _generate_issue_url(repo_url, speckit_name)

        assert "github.com/ACNet-AI/awesome-spec-kits/issues/new" in result
        assert "template=register-speckit.yml" in result  # Correct template name
        assert "title=%5BRegister%5D+test-speckit" in result  # [Register] test-speckit
        assert "repository=https%3A%2F%2Fgithub.com%2Ftest%2Frepo" in result
