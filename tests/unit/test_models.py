"""
Unit tests for metaspec.models module.
"""

from pathlib import Path

import pytest

from metaspec.models import (
    Command,
    EntityDefinition,
    Field,
    MetaSpecDefinition,
    Option,
    SlashCommand,
    SpecKitProject,
)


class TestField:
    """Tests for Field dataclass."""

    def test_field_creation(self, sample_field: Field) -> None:
        """Test creating a field."""
        assert sample_field.name == "name"
        assert sample_field.type == "string"
        assert sample_field.description == "Entity name"

    def test_field_optional_fields(self) -> None:
        """Test field with optional fields."""
        field = Field(name="test")
        assert field.name == "test"
        assert field.type is None
        assert field.description is None


class TestEntityDefinition:
    """Tests for EntityDefinition dataclass."""

    def test_entity_creation(self, sample_entity: EntityDefinition) -> None:
        """Test creating an entity definition."""
        assert sample_entity.name == "TestEntity"
        assert len(sample_entity.fields) == 3
        assert sample_entity.fields[0].name == "id"

    def test_entity_fields_access(self, sample_entity: EntityDefinition) -> None:
        """Test accessing entity fields."""
        field_names = [f.name for f in sample_entity.fields]
        assert "id" in field_names
        assert "name" in field_names
        assert "active" in field_names


class TestOption:
    """Tests for Option dataclass."""

    def test_option_creation(self) -> None:
        """Test creating an option."""
        opt = Option(name="test", type="string", required=True, description="Test option")
        assert opt.name == "test"
        assert opt.type == "string"
        assert opt.required is True
        assert opt.description == "Test option"

    def test_option_defaults(self) -> None:
        """Test option default values."""
        opt = Option(name="test", type="string")
        assert opt.required is False
        assert opt.description is None


class TestCommand:
    """Tests for Command dataclass."""

    def test_command_creation(self, sample_command: Command) -> None:
        """Test creating a command."""
        assert sample_command.name == "validate"
        assert sample_command.description == "Validate spec file"
        assert sample_command.options is not None
        assert len(sample_command.options) == 2

    def test_command_without_options(self) -> None:
        """Test command without options."""
        cmd = Command(name="test", description="Test command")
        assert cmd.name == "test"
        assert cmd.options is None


class TestSlashCommand:
    """Tests for SlashCommand dataclass."""

    def test_slash_command_creation(self, sample_slash_command: SlashCommand) -> None:
        """Test creating a slash command."""
        assert sample_slash_command.name == "specify"
        assert sample_slash_command.description == "Create specification"
        assert sample_slash_command.source == "generic"

    def test_slash_command_default_source(self) -> None:
        """Test slash command default source."""
        cmd = SlashCommand(name="test", description="Test")
        assert cmd.source == "generic"


class TestMetaSpecDefinition:
    """Tests for MetaSpecDefinition dataclass."""

    def test_meta_spec_creation(self, sample_meta_spec: MetaSpecDefinition) -> None:
        """Test creating a meta spec definition."""
        assert sample_meta_spec.name == "test-spec-kit"
        assert sample_meta_spec.version == "0.1.0"
        assert sample_meta_spec.domain == "testing"

    def test_meta_spec_entity(self, sample_meta_spec: MetaSpecDefinition) -> None:
        """Test meta spec entity."""
        assert sample_meta_spec.entity.name == "TestEntity"
        assert len(sample_meta_spec.entity.fields) == 3

    def test_meta_spec_commands(self, sample_meta_spec: MetaSpecDefinition) -> None:
        """Test meta spec commands."""
        assert sample_meta_spec.cli_commands is not None
        assert len(sample_meta_spec.cli_commands) == 1
        assert sample_meta_spec.cli_commands[0].name == "validate"

    def test_meta_spec_slash_commands(self, sample_meta_spec: MetaSpecDefinition) -> None:
        """Test meta spec slash commands."""
        assert sample_meta_spec.slash_commands is not None
        assert len(sample_meta_spec.slash_commands) == 1
        assert sample_meta_spec.slash_commands[0].name == "specify"

    def test_meta_spec_dependencies(self, sample_meta_spec: MetaSpecDefinition) -> None:
        """Test meta spec dependencies."""
        assert sample_meta_spec.dependencies is not None
        assert "pydantic>=2.0.0" in sample_meta_spec.dependencies
        assert "typer>=0.9.0" in sample_meta_spec.dependencies

    def test_from_dict_minimal(self) -> None:
        """Test creating MetaSpecDefinition from minimal dict."""
        data = {
            "name": "test-kit",
            "entity": {
                "name": "TestEntity",
                "fields": [
                    {"name": "id", "type": "string", "description": "ID"}
                ]
            }
        }
        meta_spec = MetaSpecDefinition.from_dict(data)
        assert meta_spec.name == "test-kit"
        assert meta_spec.version == "0.1.0"  # default
        assert meta_spec.domain == "generic"  # default
        assert meta_spec.entity.name == "TestEntity"

    def test_from_dict_with_all_fields(self) -> None:
        """Test creating MetaSpecDefinition from complete dict."""
        data = {
            "name": "full-kit",
            "version": "1.0.0",
            "domain": "testing",
            "description": "Full test kit",
            "entity": {
                "name": "FullEntity",
                "fields": [
                    {"name": "id", "type": "string", "description": "ID"},
                    {"name": "name", "type": "string"}
                ]
            },
            "cli_commands": [
                {
                    "name": "test",
                    "description": "Test command",
                    "options": [
                        {
                            "name": "input",
                            "type": "string",
                            "required": True,
                            "description": "Input file"
                        }
                    ]
                }
            ],
            "slash_commands": [
                {
                    "name": "test-slash",
                    "description": "Test slash command",
                    "source": "testing"
                }
            ],
            "dependencies": ["custom-dep>=1.0.0"]
        }
        meta_spec = MetaSpecDefinition.from_dict(data)
        assert meta_spec.name == "full-kit"
        assert meta_spec.version == "1.0.0"
        assert meta_spec.domain == "testing"
        assert meta_spec.description == "Full test kit"
        assert len(meta_spec.entity.fields) == 2
        assert len(meta_spec.cli_commands) == 1
        assert meta_spec.cli_commands[0].name == "test"
        assert len(meta_spec.cli_commands[0].options) == 1
        assert len(meta_spec.slash_commands) == 1
        assert meta_spec.slash_commands[0].source == "testing"
        assert "custom-dep>=1.0.0" in meta_spec.dependencies

    def test_from_dict_without_options(self) -> None:
        """Test from_dict with command without options."""
        data = {
            "name": "simple-kit",
            "entity": {
                "name": "SimpleEntity",
                "fields": [{"name": "id"}]
            },
            "cli_commands": [
                {
                    "name": "simple",
                    "description": "Simple command"
                }
            ]
        }
        meta_spec = MetaSpecDefinition.from_dict(data)
        assert len(meta_spec.cli_commands) == 1
        assert meta_spec.cli_commands[0].options is None


class TestSpecKitProject:
    """Tests for SpecKitProject dataclass."""

    def test_project_creation(self, tmp_path: Path) -> None:
        """Test creating a project."""
        root = tmp_path / "test-project"
        files = {
            Path("README.md"): "# Test",
            Path("setup.py"): "# Setup",
        }
        project = SpecKitProject(root_path=root, files=files)
        assert project.root_path == root
        assert len(project.files) == 2

    def test_project_files_access(self, tmp_path: Path) -> None:
        """Test accessing project files."""
        root = tmp_path / "test-project"
        files = {
            Path("file1.py"): "# File 1",
            Path("file2.py"): "# File 2",
        }
        project = SpecKitProject(root_path=root, files=files)
        file_paths = list(project.files.keys())
        assert Path("file1.py") in file_paths
        assert Path("file2.py") in file_paths

    def test_project_with_directories(self, tmp_path: Path) -> None:
        """Test project with directories."""
        root = tmp_path / "test-project"
        directories = [Path("src"), Path("tests"), Path("docs")]
        project = SpecKitProject(root_path=root, directories=directories)
        assert len(project.directories) == 3
        assert Path("src") in project.directories

    def test_project_with_executable_files(self, tmp_path: Path) -> None:
        """Test project with executable files."""
        root = tmp_path / "test-project"
        executable_files = [Path("scripts/init.sh"), Path("scripts/setup.sh")]
        project = SpecKitProject(root_path=root, executable_files=executable_files)
        assert len(project.executable_files) == 2
        assert Path("scripts/init.sh") in project.executable_files

    def test_write_to_disk_basic(self, tmp_path: Path) -> None:
        """Test writing project to disk."""
        root = tmp_path / "new-project"
        files = {
            Path("README.md"): "# Test Project",
            Path("src/main.py"): "print('hello')",
        }
        directories = [Path("tests"), Path("docs")]

        project = SpecKitProject(
            root_path=root,
            files=files,
            directories=directories
        )
        project.write_to_disk()

        # Verify root exists
        assert root.exists()
        # Verify files written
        assert (root / "README.md").exists()
        assert (root / "README.md").read_text() == "# Test Project"
        assert (root / "src/main.py").exists()
        # Verify directories created
        assert (root / "tests").exists()
        assert (root / "docs").exists()

    def test_write_to_disk_with_executables(self, tmp_path: Path) -> None:
        """Test writing project with executable files."""
        root = tmp_path / "exec-project"
        files = {
            Path("script.sh"): "#!/bin/bash\necho test",
        }
        executable_files = [Path("script.sh")]

        project = SpecKitProject(
            root_path=root,
            files=files,
            executable_files=executable_files
        )
        project.write_to_disk()

        script_path = root / "script.sh"
        assert script_path.exists()
        # Check executable permissions (0o755 = rwxr-xr-x)
        import stat
        mode = script_path.stat().st_mode
        assert mode & stat.S_IXUSR  # User execute
        assert mode & stat.S_IRUSR  # User read
        assert mode & stat.S_IWUSR  # User write

    def test_write_to_disk_force_overwrite(self, tmp_path: Path) -> None:
        """Test force overwrite existing directory."""
        root = tmp_path / "existing-project"
        root.mkdir()
        existing_file = root / "existing.txt"
        existing_file.write_text("old content")

        files = {
            Path("new.txt"): "new content",
        }

        project = SpecKitProject(root_path=root, files=files)
        # Should succeed with force=True
        project.write_to_disk(force=True)

        assert (root / "new.txt").exists()
        assert (root / "new.txt").read_text() == "new content"

    def test_write_to_disk_fails_without_force(self, tmp_path: Path) -> None:
        """Test that writing fails if directory exists and force=False."""
        root = tmp_path / "existing-project"
        root.mkdir()

        files = {Path("file.txt"): "content"}
        project = SpecKitProject(root_path=root, files=files)

        # Should raise FileExistsError
        with pytest.raises(FileExistsError) as exc_info:
            project.write_to_disk(force=False)
        assert "already exists" in str(exc_info.value)

    def test_write_to_disk_nested_directories(self, tmp_path: Path) -> None:
        """Test writing files in nested directories."""
        root = tmp_path / "nested-project"
        files = {
            Path("src/core/main.py"): "main code",
            Path("tests/unit/test_main.py"): "test code",
        }

        project = SpecKitProject(root_path=root, files=files)
        project.write_to_disk()

        assert (root / "src/core/main.py").exists()
        assert (root / "tests/unit/test_main.py").exists()
        assert (root / "src/core/main.py").read_text() == "main code"

