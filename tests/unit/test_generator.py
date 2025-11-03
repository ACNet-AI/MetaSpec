"""
Unit tests for metaspec.generator module.
"""

from pathlib import Path
from unittest.mock import MagicMock, patch

import pytest

from metaspec.generator import Generator, create_generator
from metaspec.models import MetaSpecDefinition, SpecKitProject


class TestGenerator:
    """Tests for Generator class."""

    def test_generator_creation(self) -> None:
        """Test creating a generator."""
        gen = Generator()
        assert gen.env is not None

    def test_generator_with_custom_template_dir(self, tmp_path: Path) -> None:
        """Test creating a generator with custom template directory."""
        template_dir = tmp_path / "templates"
        template_dir.mkdir()
        gen = Generator(custom_template_dir=template_dir)
        assert gen.env is not None

    @patch.object(Generator, "_render_templates")
    def test_generate_basic_project(
        self, mock_render: MagicMock, sample_meta_spec: MetaSpecDefinition, temp_output_dir: Path
    ) -> None:
        """Test generating a basic project."""
        # Mock the template rendering to avoid needing actual templates
        mock_render.return_value = {
            "README.md": "# Test",
            "pyproject.toml": "[project]",
        }
        
        gen = Generator()
        project = gen.generate(
            meta_spec=sample_meta_spec,
            output_dir=temp_output_dir,
            force=False,
            dry_run=True,  # Don't actually write files
        )
        assert isinstance(project, SpecKitProject)
        assert project.root_path == temp_output_dir
        assert len(project.files) > 0

    @patch.object(Generator, "_render_templates")
    def test_generate_creates_readme(
        self, mock_render: MagicMock, sample_meta_spec: MetaSpecDefinition, temp_output_dir: Path
    ) -> None:
        """Test that generation creates README.md."""
        mock_render.return_value = {
            "README.md": "# Test",
            "pyproject.toml": "[project]",
        }
        
        gen = Generator()
        project = gen.generate(
            meta_spec=sample_meta_spec,
            output_dir=temp_output_dir,
            dry_run=True,
        )
        file_paths = [str(p) for p in project.files.keys()]
        assert any("README.md" in p for p in file_paths)

    @patch.object(Generator, "_render_templates")
    def test_generate_creates_pyproject(
        self, mock_render: MagicMock, sample_meta_spec: MetaSpecDefinition, temp_output_dir: Path
    ) -> None:
        """Test that generation creates pyproject.toml."""
        mock_render.return_value = {
            "README.md": "# Test",
            "pyproject.toml": "[project]",
        }
        
        gen = Generator()
        project = gen.generate(
            meta_spec=sample_meta_spec,
            output_dir=temp_output_dir,
            dry_run=True,
        )
        file_paths = [str(p) for p in project.files.keys()]
        assert any("pyproject.toml" in p for p in file_paths)

    @patch.object(Generator, "_render_templates")
    def test_generate_creates_agents_md(
        self, mock_render: MagicMock, sample_meta_spec: MetaSpecDefinition, temp_output_dir: Path
    ) -> None:
        """Test that generation creates AGENTS.md."""
        mock_render.return_value = {
            "README.md": "# Test",
            "AGENTS.md": "# Agents",
        }
        
        gen = Generator()
        project = gen.generate(
            meta_spec=sample_meta_spec,
            output_dir=temp_output_dir,
            dry_run=True,
        )
        file_paths = [str(p) for p in project.files.keys()]
        assert any("AGENTS.md" in p for p in file_paths)

    @patch.object(Generator, "_render_templates")
    def test_generate_with_force_flag(
        self, mock_render: MagicMock, sample_meta_spec: MetaSpecDefinition, temp_output_dir: Path
    ) -> None:
        """Test generation with force flag."""
        mock_render.return_value = {"README.md": "# Test"}
        
        gen = Generator()
        # Create a file in output directory
        existing_file = temp_output_dir / "existing.txt"
        existing_file.write_text("existing content")
        
        # Generate with force=True
        project = gen.generate(
            meta_spec=sample_meta_spec,
            output_dir=temp_output_dir,
            force=True,
            dry_run=True,
        )
        assert isinstance(project, SpecKitProject)


class TestCreateGenerator:
    """Tests for create_generator helper function."""

    def test_create_generator_default(self) -> None:
        """Test creating generator with defaults."""
        gen = create_generator()
        assert isinstance(gen, Generator)
        assert gen.env is not None

    def test_create_generator_with_custom_dir(self, tmp_path: Path) -> None:
        """Test creating generator with custom template directory."""
        template_dir = tmp_path / "templates"
        template_dir.mkdir()
        gen = create_generator(custom_template_dir=template_dir)
        assert isinstance(gen, Generator)


class TestGeneratorRealScenarios:
    """Tests for Generator with more realistic scenarios."""

    @patch.object(Generator, "_render_templates")
    def test_generate_writes_to_disk(
        self, mock_render: MagicMock, sample_meta_spec: MetaSpecDefinition, tmp_path: Path
    ) -> None:
        """Test that generate writes files when dry_run=False."""
        mock_render.return_value = {
            "README.md": "# Test",
        }
        
        output_dir = tmp_path / "real-project"
        gen = Generator()
        project = gen.generate(
            meta_spec=sample_meta_spec,
            output_dir=output_dir,
            dry_run=False,
        )
        
        # Should write to disk
        assert output_dir.exists()
        assert (output_dir / "README.md").exists()

    @patch.object(Generator, "_render_templates")
    def test_generate_fails_on_existing_dir(
        self, mock_render: MagicMock, sample_meta_spec: MetaSpecDefinition, tmp_path: Path
    ) -> None:
        """Test that generate fails when directory exists without force."""
        output_dir = tmp_path / "existing"
        output_dir.mkdir()
        
        gen = Generator()
        
        with pytest.raises(FileExistsError) as exc_info:
            gen.generate(
                meta_spec=sample_meta_spec,
                output_dir=output_dir,
                dry_run=False,
                force=False,
            )
        assert "already exists" in str(exc_info.value)

    def test_create_template_context(
        self, sample_meta_spec: MetaSpecDefinition
    ) -> None:
        """Test creating template context."""
        gen = Generator()
        context = gen._create_template_context(sample_meta_spec)
        
        assert context["name"] == "test-spec-kit"
        assert context["version"] == "0.1.0"
        assert context["package_name"] == "test_spec_kit"
        assert "entity" in context
        assert "cli_commands" in context
        assert context["entity"]["name"] == "TestEntity"

    def test_select_templates(
        self, sample_meta_spec: MetaSpecDefinition
    ) -> None:
        """Test selecting templates."""
        gen = Generator()
        template_map = gen._select_templates(sample_meta_spec)
        
        assert isinstance(template_map, dict)
        assert len(template_map) > 0
        # Should include base templates
        assert any("README" in str(k) for k in template_map.keys())

    @patch.object(Generator, "_render_templates")
    def test_construct_project(
        self, mock_render: MagicMock, sample_meta_spec: MetaSpecDefinition, tmp_path: Path
    ) -> None:
        """Test constructing project structure."""
        rendered_files = {
            "README.md": "# Test",
            "src/main.py": "print('hello')",
        }
        
        gen = Generator()
        context = gen._create_template_context(sample_meta_spec)
        
        project = gen._construct_project(
            output_dir=tmp_path / "test-project",
            package_name="test_package",
            rendered_files=rendered_files,
            context=context,
        )
        
        assert isinstance(project, SpecKitProject)
        assert len(project.files) > 0
        assert len(project.directories) > 0

    def test_render_templates_error_handling(
        self, sample_meta_spec: MetaSpecDefinition
    ) -> None:
        """Test render templates with missing required template."""
        from jinja2 import TemplateNotFound

        gen = Generator()
        context = gen._create_template_context(sample_meta_spec)
        
        # Create a template map with a non-existent template (not optional)
        template_map = {
            "nonexistent/required.md.j2": "output/required.md",
        }
        
        with pytest.raises(TemplateNotFound):
            gen._render_templates(template_map, context)

    def test_render_templates_optional_commands(
        self, sample_meta_spec: MetaSpecDefinition
    ) -> None:
        """Test render templates skips optional command files."""
        gen = Generator()
        context = gen._create_template_context(sample_meta_spec)
        
        # Create a template map with optional command file that doesn't exist
        template_map = {
            "library/generic/commands/optional.md.j2": "commands/optional.md",
        }
        
        # Should not raise error for missing optional command files
        rendered = gen._render_templates(template_map, context)
        
        # Should skip the missing optional file
        assert "commands/optional.md" not in rendered

    def test_render_templates_success(
        self, sample_meta_spec: MetaSpecDefinition
    ) -> None:
        """Test successful template rendering."""
        gen = Generator()
        context = gen._create_template_context(sample_meta_spec)
        
        # Use existing templates
        template_map = {
            "library/generic/greenfield/templates/spec-template.md.j2": "specs/spec.md",
        }
        
        rendered = gen._render_templates(template_map, context)
        
        # Should successfully render the template
        assert "specs/spec.md" in rendered
        assert len(rendered["specs/spec.md"]) > 0

    def test_construct_project_with_commands(
        self, sample_meta_spec: MetaSpecDefinition, tmp_path: Path
    ) -> None:
        """Test project construction with CLI commands."""
        from metaspec.models import Command
        
        # Add a command to meta spec
        sample_meta_spec.cli_commands = [
            Command(name="info", description="Show info"),
            Command(name="validate", description="Validate spec"),
        ]
        
        gen = Generator()
        context = gen._create_template_context(sample_meta_spec)
        
        rendered_files = {
            "README.md": "# Test",
            "pyproject.toml": "[project]\nname='test'",
        }
        
        project = gen._construct_project(
            output_dir=tmp_path / "test",
            package_name="test_pkg",
            rendered_files=rendered_files,
            context=context,
        )
        
        assert isinstance(project, SpecKitProject)
        assert len(project.files) >= 2

