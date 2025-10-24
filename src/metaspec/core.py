"""
MetaSpec core functionality - Load and validate meta-spec definitions
"""
from pathlib import Path

import yaml

from metaspec.errors import MetaSpecValidationError, YAMLParseError
from metaspec.models import MetaSpecDefinition
from metaspec.validation import validate_meta_spec_structure


def load_meta_spec(yaml_path: str | Path) -> MetaSpecDefinition:
    """
    Load and parse meta-spec YAML file into MetaSpecDefinition.

    Args:
        yaml_path: Path to YAML file or file-like object (StringIO)

    Returns:
        Parsed and validated MetaSpecDefinition

    Raises:
        FileNotFoundError: File does not exist
        YAMLParseError: YAML syntax error
        MetaSpecValidationError: Validation failed
    """
    # Handle file-like objects (StringIO)
    if hasattr(yaml_path, 'read'):
        try:
            data = yaml.safe_load(yaml_path)
        except yaml.YAMLError as e:
            error_msg = f"YAML parsing error: {e}"
            raise YAMLParseError(error_msg) from e
    else:
        # Handle file paths
        yaml_path = Path(yaml_path)

        if not yaml_path.exists():
            raise FileNotFoundError(f"Meta-spec file not found: {yaml_path}")

        try:
            with open(yaml_path, encoding="utf-8") as f:
                data = yaml.safe_load(f)
        except yaml.YAMLError as e:
            error_msg = f"YAML parsing error: {e}"
            raise YAMLParseError(error_msg) from e

    # Validate structure
    errors = validate_meta_spec_structure(data)
    error_list = [e for e in errors if e.level.value == "error"]

    if error_list:
        error_messages = "\n".join(str(e) for e in error_list)
        raise MetaSpecValidationError(
            f"Meta-spec validation failed:\n{error_messages}",
            errors=error_list
        )

    # Convert to MetaSpecDefinition
    return MetaSpecDefinition.from_dict(data)
