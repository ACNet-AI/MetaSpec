"""
Data models for MetaSpec.

Core workflow: MetaSpecDefinition → Generator → SpecKitProject

This module defines the core data structures:

1. MetaSpecDefinition (Input)
   - Defines what speckit to generate
   - Created via interactive wizard or template
   - Command-first approach: speckit = entity + commands

2. SpecKitProject (Output)
   - Represents generated speckit structure
   - Contains files, directories, executable scripts
   - Ready to write to disk
"""

from dataclasses import dataclass, field
from pathlib import Path
from typing import Any

# ============================================================================
# Entity 1: MetaSpecDefinition (Input)
# ============================================================================


@dataclass
class Field:
    """Entity field definition."""

    name: str
    type: str | None = None
    description: str | None = None


@dataclass
class EntityDefinition:
    """Core entity definition for the domain."""

    name: str
    fields: list[Field]


@dataclass
class Option:
    """Command option definition."""

    name: str
    type: str
    required: bool = False
    description: str | None = None


@dataclass
class Command:
    """CLI command definition."""

    name: str
    description: str
    options: list[Option] | None = None


@dataclass
class SlashCommand:
    """AI slash command definition for use in AI editors (Cursor, Claude, etc.)."""

    name: str
    description: str
    source: str = "generic"  # Source library: "generic", "mcp", "testing", etc.


@dataclass
class MetaSpecDefinition:
    """
    Represents a validated meta-spec definition.

    This is the input to the generation process.
    Created via interactive wizard or template mode.
    """

    # Required fields
    name: str
    entity: EntityDefinition

    # Optional fields with defaults
    version: str = "0.1.0"
    domain: str = "generic"
    description: str | None = None
    cli_commands: list[Command] = field(default_factory=list)
    slash_commands: list[SlashCommand] = field(default_factory=list)
    dependencies: list[str] = field(
        default_factory=lambda: [
            "pydantic>=2.0.0",
            "typer>=0.9.0",
        ]
    )

    @staticmethod
    def from_dict(data: dict[str, Any]) -> "MetaSpecDefinition":
        """Create MetaSpecDefinition from dictionary data."""
        # Parse entity
        entity_data = data["entity"]
        fields = [
            Field(
                name=f["name"],
                type=f.get("type"),
                description=f.get("description"),
            )
            for f in entity_data["fields"]
        ]
        entity = EntityDefinition(name=entity_data["name"], fields=fields)

        # Parse CLI commands (use defaults if not provided)
        kwargs = {
            "name": data["name"],
            "entity": entity,
        }

        # Optional fields with explicit values override defaults
        if "version" in data:
            kwargs["version"] = data["version"]
        if "domain" in data:
            kwargs["domain"] = data["domain"]
        if "description" in data:
            kwargs["description"] = data["description"]
        if "dependencies" in data:
            kwargs["dependencies"] = data["dependencies"]

        # Parse CLI commands if provided
        if "cli_commands" in data:
            cli_commands = []
            for cmd_data in data["cli_commands"]:
                options = None
                if "options" in cmd_data:
                    options = [
                        Option(
                            name=opt["name"],
                            type=opt["type"],
                            required=opt.get("required", False),
                            description=opt.get("description"),
                        )
                        for opt in cmd_data["options"]
                    ]
                cli_commands.append(
                    Command(
                        name=cmd_data["name"],
                        description=cmd_data["description"],
                        options=options,
                    )
                )
            kwargs["cli_commands"] = cli_commands

        # Parse slash commands if provided
        if "slash_commands" in data:
            slash_commands = []
            for sc_data in data["slash_commands"]:
                slash_commands.append(
                    SlashCommand(
                        name=sc_data["name"],
                        description=sc_data["description"],
                        source=sc_data.get("source", "generic"),
                    )
                )
            kwargs["slash_commands"] = slash_commands

        return MetaSpecDefinition(**kwargs)


# ============================================================================
# Entity 2: SpecKitProject (Output)
# ============================================================================


@dataclass
class SpecKitProject:
    """
    Represents a generated spec-driven speckit project.

    This is the output of the generation process.
    """

    root_path: Path
    files: dict[Path, str] = field(default_factory=dict)  # Relative path -> content
    directories: list[Path] = field(default_factory=list)  # Relative paths
    executable_files: list[Path] = field(default_factory=list)  # Relative paths

    def write_to_disk(self, force: bool = False) -> None:
        """
        Write all files and directories to disk.

        Args:
            force: If True, overwrite existing directory

        Raises:
            FileExistsError: If root_path exists and force=False
        """
        # Check if directory exists
        if self.root_path.exists() and not force:
            raise FileExistsError(
                f"Output directory already exists: {self.root_path}\n"
                "Use --force flag to overwrite."
            )

        # Create root directory
        self.root_path.mkdir(parents=True, exist_ok=True)

        # Create all directories
        for dir_path in self.directories:
            full_path = self.root_path / dir_path
            full_path.mkdir(parents=True, exist_ok=True)

        # Write all files
        for file_path, content in self.files.items():
            full_path = self.root_path / file_path
            # Ensure parent directory exists
            full_path.parent.mkdir(parents=True, exist_ok=True)
            full_path.write_text(content, encoding="utf-8")

        # Set executable permissions
        for file_path in self.executable_files:
            full_path = self.root_path / file_path
            if full_path.exists():
                full_path.chmod(0o755)  # rwxr-xr-x
