"""
Community Speckit Registry

Manages discovery and installation of community-contributed speckits.
"""

import json
import shutil
import subprocess
from pathlib import Path
from typing import Any

from pydantic import BaseModel, Field


class CommunitySpeckit(BaseModel):
    """Community speckit metadata."""

    name: str
    command: str
    description: str
    version: str | None = None
    pypi_package: str | None = Field(default=None, description="PyPI package name")
    repository: str | None = Field(default=None, description="GitHub repository URL")
    author: str | None = Field(default=None, description="Author name")
    tags: list[str] = Field(default_factory=list, description="Tags for categorization")
    cli_commands: list[str] = Field(
        default_factory=list, description="Available CLI commands"
    )


class CommunityRegistry:
    """
    Client for community speckit registry.

    Registry URL: https://raw.githubusercontent.com/ACNet-AI/awesome-spec-kits/main/speckits.json
    """

    DEFAULT_REGISTRY_URL = "https://raw.githubusercontent.com/ACNet-AI/awesome-spec-kits/main/speckits.json"

    def __init__(self, registry_url: str | None = None):
        """
        Initialize community registry client.

        Args:
            registry_url: Custom registry URL (default: GitHub awesome-spec-kits)
        """
        self.registry_url = registry_url or self.DEFAULT_REGISTRY_URL
        self.cache_dir = Path.home() / ".metaspec" / "cache"
        self.cache_dir.mkdir(parents=True, exist_ok=True)

    def fetch_speckits(self, use_cache: bool = True) -> list[CommunitySpeckit]:
        """
        Fetch speckits from community registry.

        Args:
            use_cache: Use cached data if available (default: True, 24h TTL)

        Returns:
            List of community speckits
        """
        import urllib.request
        from datetime import datetime, timedelta

        cache_path = self.cache_dir / "community_speckits.json"
        cache_ttl = timedelta(hours=24)

        # Check cache
        if use_cache and cache_path.exists():
            cache_age = datetime.now() - datetime.fromtimestamp(
                cache_path.stat().st_mtime
            )
            if cache_age < cache_ttl:
                try:
                    with open(cache_path, encoding="utf-8") as f:
                        data = json.load(f)
                        return [
                            CommunitySpeckit(**item)
                            for item in data.get("speckits", [])
                        ]
                except Exception:
                    pass  # Cache corrupted, refetch

        # Fetch from remote
        try:
            with urllib.request.urlopen(self.registry_url, timeout=5) as response:
                data = json.loads(response.read().decode("utf-8"))
                speckits = [
                    CommunitySpeckit(**item) for item in data.get("speckits", [])
                ]

                # Update cache
                with open(cache_path, "w", encoding="utf-8") as f:
                    json.dump(
                        {"speckits": [s.model_dump() for s in speckits]}, f, indent=2
                    )

                return speckits
        except Exception:
            # Fallback to cache if network fails
            if cache_path.exists():
                try:
                    with open(cache_path, encoding="utf-8") as f:
                        data = json.load(f)
                        return [
                            CommunitySpeckit(**item)
                            for item in data.get("speckits", [])
                        ]
                except Exception:
                    pass

            # No cache and network failed
            return []

    def search(self, query: str) -> list[CommunitySpeckit]:
        """
        Search community speckits by name, description, or tags.

        Args:
            query: Search query

        Returns:
            List of matching speckits
        """
        all_speckits = self.fetch_speckits()
        query_lower = query.lower()

        matches = []
        for speckit in all_speckits:
            if (
                query_lower in speckit.name.lower()
                or query_lower in speckit.description.lower()
                or query_lower in speckit.command.lower()
                or any(query_lower in tag.lower() for tag in speckit.tags)
            ):
                matches.append(speckit)

        return matches

    def get(self, name_or_command: str) -> CommunitySpeckit | None:
        """
        Get speckit by name or command.

        Args:
            name_or_command: Speckit name or command

        Returns:
            CommunitySpeckit if found, None otherwise
        """
        all_speckits = self.fetch_speckits()
        for speckit in all_speckits:
            if speckit.name == name_or_command or speckit.command == name_or_command:
                return speckit
        return None

    def install(self, name_or_command: str) -> tuple[bool, str]:
        """
        Install a speckit from community registry via pip.

        Args:
            name_or_command: Speckit name or command

        Returns:
            Tuple of (success: bool, message: str)
        """
        import sys

        # Find speckit in community
        speckit = self.get(name_or_command)

        if speckit is None:
            return False, f"Speckit '{name_or_command}' not found in community registry"

        if speckit.pypi_package is None:
            return False, f"Speckit '{speckit.name}' has no PyPI package defined"

        # Install via pip
        try:
            subprocess.run(
                [sys.executable, "-m", "pip", "install", speckit.pypi_package],
                check=True,
                capture_output=True,
            )
            return True, f"Successfully installed {speckit.pypi_package}"
        except subprocess.CalledProcessError as e:
            error_msg = e.stderr.decode() if e.stderr else str(e)
            return False, f"Failed to install {speckit.pypi_package}: {error_msg}"

    @staticmethod
    def detect_speckit_info(command: str) -> dict[str, Any] | None:
        """
        Detect speckit information by calling the command.

        Args:
            command: Command name

        Returns:
            Dict with detected info (version, cli_commands), or None if detection fails
        """
        info: dict[str, Any] = {}

        try:
            # Try --version
            result = subprocess.run(
                [command, "--version"],
                capture_output=True,
                text=True,
                timeout=2,
                check=False,
            )

            if result.returncode == 0:
                info["version"] = result.stdout.strip()

        except (FileNotFoundError, subprocess.TimeoutExpired):
            pass

        try:
            # Try --help to detect commands
            result = subprocess.run(
                [command, "--help"],
                capture_output=True,
                text=True,
                timeout=2,
                check=False,
            )

            if result.returncode == 0:
                commands = CommunityRegistry._parse_commands_from_help(result.stdout)
                if commands:
                    info["cli_commands"] = commands

        except (FileNotFoundError, subprocess.TimeoutExpired):
            pass

        return info if info else None

    @staticmethod
    def _parse_commands_from_help(help_text: str) -> list[str]:
        """
        Parse available commands from --help output.

        Args:
            help_text: Output from --help command

        Returns:
            List of command names
        """
        commands = []
        in_commands_section = False

        for line in help_text.split("\n"):
            # Look for Commands section (Typer format with box drawing)
            if "Commands:" in line or "╭─ Commands" in line:
                in_commands_section = True
                continue

            # End of commands section (box bottom or next section)
            if in_commands_section and (line.startswith("╰")):
                break

            # Parse command lines (format: "│ command_name  Description")
            if in_commands_section and line.strip().startswith("│"):
                # Remove box drawing characters
                content = line.strip().lstrip("│").strip()
                if content:
                    # First word is the command name
                    parts = content.split()
                    if parts:
                        cmd = parts[0].strip()
                        if cmd and not cmd.startswith("─"):
                            commands.append(cmd)

        return commands

    @staticmethod
    def is_installed(command: str) -> bool:
        """
        Check if a speckit command is installed.

        Args:
            command: Command name

        Returns:
            True if command exists in PATH
        """
        return shutil.which(command) is not None


# Global registry instance
_registry: CommunityRegistry | None = None


def get_community_registry() -> CommunityRegistry:
    """
    Get the global community registry instance.

    Returns:
        CommunityRegistry instance
    """
    global _registry
    if _registry is None:
        _registry = CommunityRegistry()
    return _registry
