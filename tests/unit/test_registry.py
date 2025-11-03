"""
Unit tests for metaspec.registry module.
"""

from pathlib import Path
from unittest.mock import MagicMock, patch

import pytest

from metaspec.registry import CommunityRegistry, CommunitySpeckit, get_community_registry


class TestCommunitySpeckit:
    """Tests for CommunitySpeckit model."""

    def test_speckit_creation(self) -> None:
        """Test creating a community speckit."""
        speckit = CommunitySpeckit(
            name="test-speckit",
            command="test-cmd",
            description="Test speckit",
            version="1.0.0",
            pypi_package="test-speckit",
            repository="https://github.com/test/test-speckit",
            author="Test Author",
            tags=["testing", "example"],
            cli_commands=["init", "validate"],
        )
        assert speckit.name == "test-speckit"
        assert speckit.command == "test-cmd"
        assert speckit.version == "1.0.0"
        assert len(speckit.tags) == 2
        assert len(speckit.cli_commands) == 2

    def test_speckit_minimal(self) -> None:
        """Test creating a minimal speckit."""
        speckit = CommunitySpeckit(
            name="minimal",
            command="minimal-cmd",
            description="Minimal speckit",
        )
        assert speckit.name == "minimal"
        assert speckit.version is None
        assert speckit.tags == []
        assert speckit.cli_commands == []


class TestCommunityRegistry:
    """Tests for CommunityRegistry class."""

    def test_registry_creation(self) -> None:
        """Test creating a community registry."""
        registry = CommunityRegistry()
        assert registry is not None

    def test_registry_cache_dir(self) -> None:
        """Test registry cache directory is created."""
        registry = CommunityRegistry()
        assert registry.cache_dir.exists()

    @patch("metaspec.registry.subprocess.run")
    def test_detect_speckit_info_version(self, mock_run: MagicMock) -> None:
        """Test detecting speckit version."""
        mock_run.return_value = MagicMock(
            returncode=0,
            stdout="1.0.0",
        )
        
        info = CommunityRegistry.detect_speckit_info("test-cmd")
        assert info is not None
        assert info.get("version") == "1.0.0"

    @patch("metaspec.registry.subprocess.run")
    def test_detect_speckit_info_commands(self, mock_run: MagicMock) -> None:
        """Test detecting speckit commands."""
        # First call for --version
        version_result = MagicMock(returncode=1)
        # Second call for --help with proper Typer format
        help_result = MagicMock(
            returncode=0,
            stdout="Commands:\n│ init       Initialize\n│ validate   Validate\n│ generate   Generate\n",
        )
        mock_run.side_effect = [version_result, help_result]
        
        info = CommunityRegistry.detect_speckit_info("test-cmd")
        assert info is not None
        assert "cli_commands" in info
        assert "init" in info["cli_commands"]

    @patch("metaspec.registry.subprocess.run")
    def test_detect_speckit_info_not_found(self, mock_run: MagicMock) -> None:
        """Test detecting speckit that doesn't exist."""
        mock_run.side_effect = FileNotFoundError()
        
        info = CommunityRegistry.detect_speckit_info("nonexistent")
        assert info is None

    def test_parse_commands_from_help(self) -> None:
        """Test parsing commands from help text."""
        help_text = """
Usage: test-cmd [OPTIONS] COMMAND

Commands:
│ init       Initialize a new spec
│ validate   Validate spec file
│ generate   Generate code from spec
"""
        commands = CommunityRegistry._parse_commands_from_help(help_text)
        assert "init" in commands
        assert "validate" in commands
        assert "generate" in commands

    def test_parse_commands_empty_help(self) -> None:
        """Test parsing commands from empty help text."""
        commands = CommunityRegistry._parse_commands_from_help("")
        assert commands == []

    @patch("metaspec.registry.subprocess.run")
    @patch.object(CommunityRegistry, "get")
    def test_install_speckit_success(self, mock_get: MagicMock, mock_run: MagicMock) -> None:
        """Test successful speckit installation."""
        mock_run.return_value = MagicMock(returncode=0)
        
        speckit = CommunitySpeckit(
            name="test",
            command="test",
            description="Test",
            pypi_package="test-speckit",
        )
        mock_get.return_value = speckit
        
        registry = CommunityRegistry()
        success, message = registry.install("test")
        assert success is True
        assert "installed" in message.lower()

    @patch("metaspec.registry.subprocess.run")
    @patch.object(CommunityRegistry, "get")
    def test_install_speckit_failure(self, mock_get: MagicMock, mock_run: MagicMock) -> None:
        """Test failed speckit installation."""
        import subprocess
        mock_run.side_effect = subprocess.CalledProcessError(1, "pip install")
        
        speckit = CommunitySpeckit(
            name="test",
            command="test",
            description="Test",
            pypi_package="test-speckit",
        )
        mock_get.return_value = speckit
        
        registry = CommunityRegistry()
        success, message = registry.install("test")
        assert success is False
        assert "failed" in message.lower()

    @patch.object(CommunityRegistry, "fetch_speckits")
    def test_search_speckits_empty(self, mock_fetch: MagicMock) -> None:
        """Test searching speckits with no results."""
        mock_fetch.return_value = []
        
        registry = CommunityRegistry()
        results = registry.search("nonexistent")
        assert results == []

    @patch.object(CommunityRegistry, "fetch_speckits")
    def test_list_all_speckits_empty(self, mock_fetch: MagicMock) -> None:
        """Test listing all speckits when registry is empty."""
        mock_fetch.return_value = []
        
        registry = CommunityRegistry()
        speckits = registry.fetch_speckits()
        assert speckits == []

    @patch("urllib.request.urlopen")
    def test_fetch_speckits_from_remote(self, mock_urlopen: MagicMock, tmp_path: Path) -> None:
        """Test fetching speckits from remote registry."""
        from unittest.mock import MagicMock
        import json
        
        # Mock response data
        response_data = {
            "speckits": [
                {
                    "name": "test-kit",
                    "command": "test-cmd",
                    "description": "Test speckit",
                }
            ]
        }
        
        # Mock urlopen response
        mock_response = MagicMock()
        mock_response.read.return_value = json.dumps(response_data).encode()
        mock_response.__enter__.return_value = mock_response
        mock_urlopen.return_value = mock_response
        
        # Use custom cache dir to avoid conflicts
        registry = CommunityRegistry()
        registry.cache_dir = tmp_path / "cache"
        registry.cache_dir.mkdir(parents=True, exist_ok=True)
        
        speckits = registry.fetch_speckits(use_cache=False)
        assert len(speckits) == 1
        assert speckits[0].name == "test-kit"

    @patch("urllib.request.urlopen")
    def test_fetch_speckits_uses_cache(self, mock_urlopen: MagicMock, tmp_path: Path) -> None:
        """Test that fetch_speckits uses cache when available."""
        import json
        
        # Create cache file
        cache_dir = tmp_path / "cache"
        cache_dir.mkdir()
        cache_file = cache_dir / "community_speckits.json"
        cache_data = {
            "speckits": [
                {
                    "name": "cached-kit",
                    "command": "cached-cmd",
                    "description": "Cached speckit",
                }
            ]
        }
        cache_file.write_text(json.dumps(cache_data))
        
        registry = CommunityRegistry()
        registry.cache_dir = cache_dir
        
        # Should use cache without calling urlopen
        speckits = registry.fetch_speckits(use_cache=True)
        assert len(speckits) == 1
        assert speckits[0].name == "cached-kit"
        mock_urlopen.assert_not_called()

    @patch.object(CommunityRegistry, "fetch_speckits")
    def test_get_speckit_by_name(self, mock_fetch: MagicMock) -> None:
        """Test getting speckit by name."""
        mock_fetch.return_value = [
            CommunitySpeckit(name="kit1", command="cmd1", description="Kit 1"),
            CommunitySpeckit(name="kit2", command="cmd2", description="Kit 2"),
        ]
        
        registry = CommunityRegistry()
        speckit = registry.get("kit1")
        assert speckit is not None
        assert speckit.name == "kit1"

    @patch.object(CommunityRegistry, "fetch_speckits")
    def test_get_speckit_by_command(self, mock_fetch: MagicMock) -> None:
        """Test getting speckit by command."""
        mock_fetch.return_value = [
            CommunitySpeckit(name="kit1", command="cmd1", description="Kit 1"),
        ]
        
        registry = CommunityRegistry()
        speckit = registry.get("cmd1")
        assert speckit is not None
        assert speckit.command == "cmd1"

    @patch.object(CommunityRegistry, "fetch_speckits")
    def test_get_speckit_not_found(self, mock_fetch: MagicMock) -> None:
        """Test getting non-existent speckit."""
        mock_fetch.return_value = []
        
        registry = CommunityRegistry()
        speckit = registry.get("nonexistent")
        assert speckit is None

    @patch.object(CommunityRegistry, "fetch_speckits")
    def test_search_by_keyword(self, mock_fetch: MagicMock) -> None:
        """Test searching speckits by keyword."""
        mock_fetch.return_value = [
            CommunitySpeckit(name="python-kit", command="pykit", description="Python toolkit"),
            CommunitySpeckit(name="rust-kit", command="rustkit", description="Rust toolkit"),
        ]
        
        registry = CommunityRegistry()
        results = registry.search("python")
        assert len(results) == 1
        assert results[0].name == "python-kit"

    def test_is_installed_true(self) -> None:
        """Test is_installed returns True for existing command."""
        # Test with a command that definitely exists
        assert CommunityRegistry.is_installed("python") or CommunityRegistry.is_installed("python3")

    def test_is_installed_false(self) -> None:
        """Test is_installed returns False for non-existent command."""
        assert not CommunityRegistry.is_installed("definitely-not-a-real-command-12345")

    @patch("urllib.request.urlopen")
    def test_fetch_speckits_network_error_fallback_cache(
        self, mock_urlopen: MagicMock, tmp_path: Path
    ) -> None:
        """Test fallback to cache when network fails."""
        import json
        
        # Create cache file
        cache_dir = tmp_path / "cache"
        cache_dir.mkdir()
        cache_file = cache_dir / "community_speckits.json"
        cache_data = {
            "speckits": [
                {
                    "name": "fallback-kit",
                    "command": "fallback-cmd",
                    "description": "Fallback speckit",
                }
            ]
        }
        cache_file.write_text(json.dumps(cache_data))
        
        # Mock network failure
        mock_urlopen.side_effect = Exception("Network error")
        
        registry = CommunityRegistry()
        registry.cache_dir = cache_dir
        
        # Should fallback to cache
        speckits = registry.fetch_speckits(use_cache=False)
        assert len(speckits) == 1
        assert speckits[0].name == "fallback-kit"

    @patch("urllib.request.urlopen")
    def test_fetch_speckits_corrupted_cache(
        self, mock_urlopen: MagicMock, tmp_path: Path
    ) -> None:
        """Test handling corrupted cache file."""
        import json
        
        # Create corrupted cache file
        cache_dir = tmp_path / "cache"
        cache_dir.mkdir()
        cache_file = cache_dir / "community_speckits.json"
        cache_file.write_text("not valid json {}")
        
        # Mock successful response
        response_data = {
            "speckits": [
                {
                    "name": "new-kit",
                    "command": "new-cmd",
                    "description": "New speckit",
                }
            ]
        }
        mock_response = MagicMock()
        mock_response.read.return_value = json.dumps(response_data).encode()
        mock_response.__enter__.return_value = mock_response
        mock_urlopen.return_value = mock_response
        
        registry = CommunityRegistry()
        registry.cache_dir = cache_dir
        
        # Should refetch from network since cache is corrupted
        speckits = registry.fetch_speckits(use_cache=True)
        assert len(speckits) == 1
        assert speckits[0].name == "new-kit"

    @patch("metaspec.registry.subprocess.run")
    @patch.object(CommunityRegistry, "get")
    def test_install_not_found(self, mock_get: MagicMock, mock_run: MagicMock) -> None:
        """Test installing speckit that doesn't exist."""
        mock_get.return_value = None
        
        registry = CommunityRegistry()
        success, message = registry.install("nonexistent")
        assert success is False
        assert "not found" in message.lower()

    @patch("metaspec.registry.subprocess.run")
    @patch.object(CommunityRegistry, "get")
    def test_install_no_pypi_package(self, mock_get: MagicMock, mock_run: MagicMock) -> None:
        """Test installing speckit without pypi_package."""
        speckit = CommunitySpeckit(
            name="test",
            command="test",
            description="Test",
            pypi_package=None,
        )
        mock_get.return_value = speckit
        
        registry = CommunityRegistry()
        success, message = registry.install("test")
        assert success is False
        assert "pypi package" in message.lower()

    def test_get_community_registry_singleton(self) -> None:
        """Test that get_community_registry returns singleton."""
        registry1 = get_community_registry()
        registry2 = get_community_registry()
        assert registry1 is registry2

    @patch.object(CommunityRegistry, "fetch_speckits")
    def test_search_with_tags(self, mock_fetch: MagicMock) -> None:
        """Test searching speckits with tags."""
        mock_fetch.return_value = [
            CommunitySpeckit(
                name="python-kit",
                command="pykit",
                description="Python toolkit",
                tags=["python", "dev"],
            ),
            CommunitySpeckit(
                name="rust-kit",
                command="rustkit",
                description="Rust toolkit",
                tags=["rust", "systems"],
            ),
        ]
        
        registry = CommunityRegistry()
        results = registry.search("dev")
        assert len(results) >= 1
        assert any("dev" in s.tags for s in results if s.tags)

    @patch("urllib.request.urlopen")
    def test_fetch_speckits_network_fail_corrupted_cache(
        self, mock_urlopen: MagicMock, tmp_path: Path
    ) -> None:
        """Test network failure with corrupted cache returns empty list."""
        # Mock network failure
        mock_urlopen.side_effect = Exception("Network error")
        
        # Create corrupted cache file
        cache_dir = tmp_path / "cache"
        cache_dir.mkdir()
        cache_file = cache_dir / "community_speckits.json"
        cache_file.write_text("corrupted { json")
        
        registry = CommunityRegistry()
        registry.cache_dir = cache_dir
        
        # Should return empty list when network fails and cache is corrupted
        result = registry.fetch_speckits(use_cache=True)
        assert result == []

    def test_speckit_repr(self) -> None:
        """Test CommunitySpeckit string representation."""
        speckit = CommunitySpeckit(
            name="test-kit",
            command="test-cmd",
            description="Test description",
        )
        repr_str = repr(speckit)
        assert "CommunitySpeckit" in repr_str or "test-kit" in repr_str

