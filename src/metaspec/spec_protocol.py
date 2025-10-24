"""
Spec Toolkit Protocol

Defines the standard interface that all spec toolkits should follow.
This enables MetaSpec to manage and orchestrate different spec tools uniformly.
"""

from typing import Protocol, runtime_checkable


@runtime_checkable
class SpecToolkitProtocol(Protocol):
    """
    Protocol that all spec toolkits should implement.

    This allows MetaSpec to:
    - Discover available toolkits
    - Route commands to the appropriate toolkit
    - Provide a unified interface for all spec tools
    """

    @property
    def name(self) -> str:
        """Toolkit name (e.g., 'spec-kit', 'openspec', 'api-spec-kit')"""
        ...

    @property
    def version(self) -> str:
        """Toolkit version (e.g., '0.1.0')"""
        ...

    @property
    def description(self) -> str:
        """Short description of the toolkit"""
        ...

    @property
    def commands(self) -> list[str]:
        """List of available commands (e.g., ['init', 'validate', 'generate'])"""
        ...

    def execute(self, command: str, args: list[str]) -> int:
        """
        Execute a command with the given arguments.

        Args:
            command: Command name to execute
            args: Command arguments

        Returns:
            Exit code (0 for success, non-zero for failure)
        """
        ...


class BuiltinToolkit:
    """
    Built-in toolkit adapter for existing tools (spec-kit, openspec).

    Wraps external commands to conform to the SpecToolkitProtocol.
    """

    def __init__(
        self,
        name: str,
        version: str,
        description: str,
        command: str,
        available_commands: list[str],
    ):
        self._name = name
        self._version = version
        self._description = description
        self._command = command
        self._commands = available_commands

    @property
    def name(self) -> str:
        return self._name

    @property
    def version(self) -> str:
        return self._version

    @property
    def description(self) -> str:
        return self._description

    @property
    def commands(self) -> list[str]:
        return self._commands

    @property
    def command_name(self) -> str:
        """The actual command to execute (e.g., 'specify', 'openspec')"""
        return self._command

    def execute(self, command: str, args: list[str]) -> int:
        """Execute the command by calling the external tool"""
        import subprocess

        try:
            result = subprocess.run(
                [self._command, command, *args],
                check=False,
            )
            return result.returncode
        except FileNotFoundError:
            return 127  # Command not found


# Built-in toolkits registry
BUILTIN_TOOLKITS = {
    "spec-kit": BuiltinToolkit(
        name="spec-kit",
        version="unknown",  # Will be detected at runtime
        description="Spec-driven development (greenfield)",
        command="specify",
        available_commands=["init", "spec", "plan", "tasks"],
    ),
    "openspec": BuiltinToolkit(
        name="openspec",
        version="unknown",  # Will be detected at runtime
        description="Spec-driven updates (brownfield)",
        command="openspec",
        available_commands=["init", "analyze", "plan", "implement"],
    ),
}

