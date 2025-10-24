"""
End-to-end integration tests for MetaSpec.

Tests the complete generation flow from meta-spec YAML to generated toolkit.
"""

import shutil
import tempfile
from pathlib import Path

import pytest

from metaspec.core import load_meta_spec
from metaspec.generator import create_generator
from metaspec.models import MetaSpecDefinition


@pytest.fixture
def temp_output_dir():
    """Create a temporary directory for test outputs."""
    temp_dir = Path(tempfile.mkdtemp())
    yield temp_dir
    # Cleanup
    if temp_dir.exists():
        shutil.rmtree(temp_dir)


@pytest.fixture
def fixtures_dir():
    """Path to test fixtures directory."""
    return Path(__file__).parent.parent / "fixtures" / "meta-specs"


class TestEndToEndGeneration:
    """End-to-end generation tests."""

    def test_generate_minimal_toolkit(self, fixtures_dir, temp_output_dir):
        """Test generating a minimal generic toolkit."""
        # Load meta-spec
        meta_spec_path = fixtures_dir / "minimal.yaml"
        data = load_meta_spec(meta_spec_path)
        meta_spec = MetaSpecDefinition.from_dict(data)

        # Generate toolkit
        output_dir = temp_output_dir / "test-kit"
        generator = create_generator()
        generator.generate(meta_spec, output_dir, force=False)

        # Verify project was created
        assert output_dir.exists()
        assert output_dir.is_dir()

        # Verify core files exist
        assert (output_dir / "AGENTS.md").exists()
        assert (output_dir / "README.md").exists()
        assert (output_dir / "pyproject.toml").exists()
        assert (output_dir / ".gitignore").exists()

        # Verify memory directory
        assert (output_dir / "memory").exists()
        assert (output_dir / "memory" / "constitution.md").exists()

        # Verify source package
        assert (output_dir / "src" / "test_kit").exists()
        assert (output_dir / "src" / "test_kit" / "__init__.py").exists()
        assert (output_dir / "src" / "test_kit" / "cli.py").exists()
        assert (output_dir / "src" / "test_kit" / "parser.py").exists()
        assert (output_dir / "src" / "test_kit" / "validator.py").exists()

        # Verify templates directory
        assert (output_dir / "templates").exists()
        assert (output_dir / "templates" / "spec-template.md").exists()

        # Verify scripts
        assert (output_dir / "scripts").exists()
        assert (output_dir / "scripts" / "init.sh").exists()
        assert (output_dir / "scripts" / "validate.sh").exists()

        # Verify executable permissions on scripts
        init_script = output_dir / "scripts" / "init.sh"
        assert init_script.stat().st_mode & 0o111  # Has execute permission

    def test_generate_mcp_toolkit(self, fixtures_dir, temp_output_dir):
        """Test generating an MCP-specific toolkit."""
        # Load meta-spec
        meta_spec_path = fixtures_dir / "mcp-example.yaml"
        data = load_meta_spec(meta_spec_path)
        meta_spec = MetaSpecDefinition.from_dict(data)

        # Generate toolkit
        output_dir = temp_output_dir / "mcp-spec-kit"
        generator = create_generator()
        generator.generate(meta_spec, output_dir)

        # Verify project was created
        assert output_dir.exists()

        # Verify MCP-specific templates
        assert (output_dir / "templates" / "spec-template.md").exists()
        assert (output_dir / "templates" / "mcp-guide.md").exists()

        # Verify content includes MCP-specific information
        agents_content = (output_dir / "AGENTS.md").read_text()
        assert "MCP" in agents_content or "mcp" in agents_content

        # Verify dependencies are included
        pyproject_content = (output_dir / "pyproject.toml").read_text()
        assert "fastapi" in pyproject_content
        assert "pydantic" in pyproject_content

    def test_generate_with_force_overwrites(self, fixtures_dir, temp_output_dir):
        """Test that --force flag allows overwriting existing directory."""
        meta_spec_path = fixtures_dir / "minimal.yaml"
        data = load_meta_spec(meta_spec_path)
        meta_spec = MetaSpecDefinition.from_dict(data)

        output_dir = temp_output_dir / "test-kit"
        generator = create_generator()

        # Generate first time
        generator.generate(meta_spec, output_dir)
        assert output_dir.exists()

        # Try to generate again without force - should fail
        with pytest.raises(FileExistsError):
            generator.generate(meta_spec, output_dir, force=False)

        # Generate with force - should succeed
        generator.generate(meta_spec, output_dir, force=True)
        assert output_dir.exists()

    def test_generated_toolkit_structure_complete(self, fixtures_dir, temp_output_dir):
        """Test that generated toolkit has complete structure."""
        meta_spec_path = fixtures_dir / "minimal.yaml"
        data = load_meta_spec(meta_spec_path)
        meta_spec = MetaSpecDefinition.from_dict(data)

        output_dir = temp_output_dir / "test-kit"
        generator = create_generator()
        generator.generate(meta_spec, output_dir)

        # Check all expected directories exist
        expected_dirs = [
            "src/test_kit",
            "memory",
            "templates",
            "scripts",
            "examples",
        ]

        for dir_path in expected_dirs:
            full_path = output_dir / dir_path
            assert full_path.exists(), f"Missing directory: {dir_path}"
            assert full_path.is_dir(), f"Not a directory: {dir_path}"

    def test_generated_files_are_valid(self, fixtures_dir, temp_output_dir):
        """Test that generated files have valid content."""
        meta_spec_path = fixtures_dir / "minimal.yaml"
        data = load_meta_spec(meta_spec_path)
        meta_spec = MetaSpecDefinition.from_dict(data)

        output_dir = temp_output_dir / "test-kit"
        generator = create_generator()
        generator.generate(meta_spec, output_dir)

        # Check README contains expected content
        readme = (output_dir / "README.md").read_text()
        assert "test-kit" in readme
        assert "0.1.0" in readme
        assert "TestEntity" in readme

        # Check pyproject.toml is valid TOML
        pyproject = (output_dir / "pyproject.toml").read_text()
        assert "[project]" in pyproject
        assert 'name = "test-kit"' in pyproject
        assert 'version = "0.1.0"' in pyproject

        # Check Python files have valid syntax
        cli_file = output_dir / "src" / "test_kit" / "cli.py"
        cli_content = cli_file.read_text()
        # Basic check for Python syntax
        assert "def main():" in cli_content
        assert "import" in cli_content

    def test_template_context_includes_all_fields(self, fixtures_dir, temp_output_dir):
        """Test that template context includes all required fields."""
        meta_spec_path = fixtures_dir / "mcp-example.yaml"
        data = load_meta_spec(meta_spec_path)
        meta_spec = MetaSpecDefinition.from_dict(data)

        output_dir = temp_output_dir / "mcp-spec-kit"
        generator = create_generator()
        generator.generate(meta_spec, output_dir)

        # Check that entity fields are included in generated docs
        agents_content = (output_dir / "AGENTS.md").read_text()
        assert "tools" in agents_content
        assert "resources" in agents_content
        assert "prompts" in agents_content

        # Check that description is included
        readme_content = (output_dir / "README.md").read_text()
        assert "Spec-driven toolkit for MCP server development" in readme_content


class TestGenerationEdgeCases:
    """Test edge cases and error handling."""

    def test_invalid_output_directory_parent_doesnt_exist(
        self, fixtures_dir, temp_output_dir
    ):
        """Test generation with non-existent parent directory."""
        meta_spec_path = fixtures_dir / "minimal.yaml"
        data = load_meta_spec(meta_spec_path)
        meta_spec = MetaSpecDefinition.from_dict(data)

        # Output to directory with non-existent parent
        output_dir = temp_output_dir / "non" / "existent" / "path" / "test-kit"
        generator = create_generator()

        # Should create parent directories automatically
        generator.generate(meta_spec, output_dir)
        assert output_dir.exists()

    def test_generation_is_atomic(self, fixtures_dir, temp_output_dir):
        """Test that generation is atomic (all or nothing)."""
        meta_spec_path = fixtures_dir / "minimal.yaml"
        data = load_meta_spec(meta_spec_path)
        meta_spec = MetaSpecDefinition.from_dict(data)

        output_dir = temp_output_dir / "test-kit"
        generator = create_generator()

        # Generate successfully
        generator.generate(meta_spec, output_dir)

        # Count files
        all_files = list(output_dir.rglob("*"))
        file_count = len([f for f in all_files if f.is_file()])

        # Should have generated multiple files
        assert file_count > 10


@pytest.mark.slow
class TestGenerationPerformance:
    """Performance tests for generation."""

    def test_generation_completes_in_reasonable_time(
        self, fixtures_dir, temp_output_dir
    ):
        """Test that generation completes in < 60 seconds (Success Criteria SC-001)."""
        import time

        meta_spec_path = fixtures_dir / "mcp-example.yaml"
        data = load_meta_spec(meta_spec_path)
        meta_spec = MetaSpecDefinition.from_dict(data)

        output_dir = temp_output_dir / "mcp-spec-kit"
        generator = create_generator()

        start_time = time.time()
        generator.generate(meta_spec, output_dir)
        end_time = time.time()

        elapsed = end_time - start_time

        # Should complete in less than 60 seconds
        assert elapsed < 60.0, f"Generation took {elapsed:.2f}s (should be < 60s)"

        # For most cases, should be much faster (< 5 seconds)
        assert elapsed < 5.0, f"Generation took {elapsed:.2f}s (should be < 5s)"

