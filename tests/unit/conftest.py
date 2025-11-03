"""
Pytest configuration and fixtures for unit tests.
"""

import pytest
from pathlib import Path

from metaspec.models import (
    Command,
    EntityDefinition,
    Field,
    MetaSpecDefinition,
    Option,
    SlashCommand,
)


@pytest.fixture
def sample_field() -> Field:
    """Sample field for testing."""
    return Field(name="name", type="string", description="Entity name")


@pytest.fixture
def sample_entity() -> EntityDefinition:
    """Sample entity definition for testing."""
    return EntityDefinition(
        name="TestEntity",
        fields=[
            Field(name="id", type="string", description="Unique identifier"),
            Field(name="name", type="string", description="Entity name"),
            Field(name="active", type="boolean", description="Is active"),
        ],
    )


@pytest.fixture
def sample_command() -> Command:
    """Sample CLI command for testing."""
    return Command(
        name="validate",
        description="Validate spec file",
        options=[
            Option(name="input", type="string", required=True, description="Input file"),
            Option(name="strict", type="boolean", required=False, description="Strict mode"),
        ],
    )


@pytest.fixture
def sample_slash_command() -> SlashCommand:
    """Sample slash command for testing."""
    return SlashCommand(
        name="specify",
        description="Create specification",
        source="generic",
    )


@pytest.fixture
def sample_meta_spec(sample_entity: EntityDefinition, sample_command: Command) -> MetaSpecDefinition:
    """Sample MetaSpecDefinition for testing."""
    return MetaSpecDefinition(
        name="test-spec-kit",
        version="0.1.0",
        description="Test specification toolkit",
        domain="testing",
        entity=sample_entity,
        cli_commands=[sample_command],
        slash_commands=[
            SlashCommand(name="specify", description="Create spec", source="generic")
        ],
        dependencies=["pydantic>=2.0.0", "typer>=0.9.0"],
    )


@pytest.fixture
def temp_output_dir(tmp_path: Path) -> Path:
    """Temporary output directory for testing."""
    output_dir = tmp_path / "test-output"
    output_dir.mkdir()
    return output_dir

