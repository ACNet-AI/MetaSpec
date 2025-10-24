"""
Data models for MetaSpec.

This module defines the core data structures used throughout MetaSpec:
- MetaSpecDefinition: Input (parsed YAML configuration)
- TemplateContext: Processing (variables for rendering)
- ToolkitProject: Output (generated project structure)
"""

from dataclasses import dataclass, field
from datetime import datetime
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
class TemplateConfig:
    """Template configuration."""

    custom: list[str] | None = None


@dataclass
class MetaSpecDefinition:
    """
    Represents a parsed and validated meta-spec.yaml file.

    This is the input to the generation process.
    """

    name: str
    version: str
    domain: str
    lifecycle: str
    entity: EntityDefinition
    description: str | None = None
    commands: list[Command] | None = None
    templates: TemplateConfig | None = None
    dependencies: list[str] | None = None

    @staticmethod
    def from_dict(data: dict[str, Any]) -> "MetaSpecDefinition":
        """Create MetaSpecDefinition from parsed YAML dict."""
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

        # Parse commands (optional)
        commands = None
        if "commands" in data:
            commands = []
            for cmd_data in data["commands"]:
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
                commands.append(
                    Command(
                        name=cmd_data["name"],
                        description=cmd_data["description"],
                        options=options,
                    )
                )

        # Parse template config (optional)
        templates = None
        if "templates" in data:
            templates = TemplateConfig(custom=data["templates"].get("custom"))

        return MetaSpecDefinition(
            name=data["name"],
            version=data["version"],
            domain=data["domain"],
            lifecycle=data["lifecycle"],
            entity=entity,
            description=data.get("description"),
            commands=commands,
            templates=templates,
            dependencies=data.get("dependencies"),
        )


# ============================================================================
# Entity 2: TemplateContext (Processing)
# ============================================================================


class TemplateContext:
    """
    Variables passed to Jinja2 templates during rendering.

    This is a temporary entity that exists only during generation.
    """

    @staticmethod
    def from_meta_spec(meta_spec: MetaSpecDefinition) -> dict[str, Any]:
        """
        Create template context from MetaSpecDefinition.

        Returns a dict that can be unpacked as **context for template rendering.
        """
        # Convert name to Python package name (snake_case)
        package_name = meta_spec.name.replace("-", "_").lower()

        # Ensure description exists
        description = (
            meta_spec.description or f"Spec-driven toolkit for {meta_spec.domain}"
        )

        # Convert entity to dict for template access
        entity_dict = {
            "name": meta_spec.entity.name,
            "fields": [
                {
                    "name": f.name,
                    "type": f.type or "str",
                    "description": f.description or "",
                }
                for f in meta_spec.entity.fields
            ],
        }

        # Convert commands to list of dicts
        commands_list = []
        if meta_spec.commands:
            for cmd in meta_spec.commands:
                cmd_dict = {
                    "name": cmd.name,
                    "description": cmd.description,
                    "options": [],
                }
                if cmd.options:
                    cmd_dict["options"] = [
                        {
                            "name": opt.name,
                            "type": opt.type,
                            "required": opt.required,
                            "description": opt.description or "",
                        }
                        for opt in cmd.options
                    ]
                commands_list.append(cmd_dict)

        return {
            "name": meta_spec.name,
            "package_name": package_name,
            "version": meta_spec.version,
            "description": description,
            "domain": meta_spec.domain,
            "lifecycle": meta_spec.lifecycle,
            "entity": entity_dict,
            "commands": commands_list,
            "dependencies": meta_spec.dependencies or [],
            "year": datetime.now().year,
            "date": datetime.now().date().isoformat(),
            "metaspec_version": "0.1.0",  # TODO: Get from package metadata
        }


# ============================================================================
# Entity 3: ToolkitProject (Output)
# ============================================================================


@dataclass
class ToolkitProject:
    """
    Represents a generated toolkit project.

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

