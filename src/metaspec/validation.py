"""
Validation logic for MetaSpec definitions.

This module provides validation functions and fix suggestions for common errors.
"""

from typing import Any

from metaspec.errors import ErrorLevel, ValidationError

# Supported domains and lifecycles
SUPPORTED_DOMAINS = ["generic", "mcp", "web", "ai"]
SUPPORTED_LIFECYCLES = ["greenfield", "brownfield"]

# Required fields
REQUIRED_FIELDS = ["name", "version", "domain", "lifecycle", "entity"]
ENTITY_REQUIRED_FIELDS = ["name", "fields"]


def validate_meta_spec_structure(data: dict[str, Any]) -> list[ValidationError]:
    """
    Validate the structure of a meta-spec definition.

    Args:
        data: Parsed YAML data

    Returns:
        List of validation errors
    """
    errors = []

    # Check required fields
    errors.extend(_check_required_fields(data))

    # Check field types
    errors.extend(_check_field_types(data))

    # Check enums (domain, lifecycle)
    errors.extend(_check_enum_values(data))

    # Validate entity structure
    if "entity" in data and isinstance(data["entity"], dict):
        errors.extend(_validate_entity(data["entity"]))

    # Validate commands (if present)
    if "commands" in data:
        errors.extend(_validate_commands(data["commands"]))

    # Validate dependencies (if present)
    if "dependencies" in data:
        errors.extend(_validate_dependencies(data["dependencies"]))

    return errors


def _check_required_fields(data: dict[str, Any]) -> list[ValidationError]:
    """Check that all required fields are present."""
    errors = []

    for field in REQUIRED_FIELDS:
        if field not in data:
            error = ValidationError(
                message=f"Missing required field: '{field}'",
                field=field,
                error_code="MISSING_REQUIRED_FIELD",
                suggestion=_get_missing_field_suggestion(field),
            )
            errors.append(error)

    return errors


def _check_field_types(data: dict[str, Any]) -> list[ValidationError]:
    """Check that fields have correct types."""
    errors = []

    # name should be string
    if "name" in data and not isinstance(data["name"], str):
        errors.append(
            ValidationError(
                message=f"Field 'name' must be a string, got {type(data['name']).__name__}",
                field="name",
                error_code="WRONG_TYPE",
                suggestion="Use a string value like 'my-spec-kit' or 'my_spec_kit'",
            )
        )

    # version should be string
    if "version" in data and not isinstance(data["version"], str):
        errors.append(
            ValidationError(
                message=f"Field 'version' must be a string, got {type(data['version']).__name__}",
                field="version",
                error_code="WRONG_TYPE",
                suggestion='Use semantic version string like "0.1.0" (quoted)',
            )
        )

    # domain should be string
    if "domain" in data and not isinstance(data["domain"], str):
        errors.append(
            ValidationError(
                message=f"Field 'domain' must be a string, got {type(data['domain']).__name__}",
                field="domain",
                error_code="WRONG_TYPE",
                suggestion=f"Use one of: {', '.join(SUPPORTED_DOMAINS)}",
            )
        )

    # entity should be dict/object
    if "entity" in data and not isinstance(data["entity"], dict):
        errors.append(
            ValidationError(
                message=f"Field 'entity' must be an object, got {type(data['entity']).__name__}",
                field="entity",
                error_code="WRONG_TYPE",
                suggestion="Define entity as: entity:\\n  name: EntityName\\n  fields: [...]",
            )
        )

    return errors


def _check_enum_values(data: dict[str, Any]) -> list[ValidationError]:
    """Check that enum fields have valid values."""
    errors = []

    # Check domain
    if "domain" in data and isinstance(data["domain"], str):
        if data["domain"] not in SUPPORTED_DOMAINS:
            errors.append(
                ValidationError(
                    message=f"Invalid domain: '{data['domain']}'",
                    field="domain",
                    error_code="INVALID_ENUM",
                    suggestion=f"Use one of: {', '.join(SUPPORTED_DOMAINS)}",
                )
            )

    # Check lifecycle
    if "lifecycle" in data and isinstance(data["lifecycle"], str):
        if data["lifecycle"] not in SUPPORTED_LIFECYCLES:
            errors.append(
                ValidationError(
                    message=f"Invalid lifecycle: '{data['lifecycle']}'",
                    field="lifecycle",
                    error_code="INVALID_ENUM",
                    suggestion=f"Use one of: {', '.join(SUPPORTED_LIFECYCLES)}",
                )
            )

    return errors


def _validate_entity(entity: dict[str, Any]) -> list[ValidationError]:
    """Validate entity structure."""
    errors = []

    # Check required entity fields
    for field in ENTITY_REQUIRED_FIELDS:
        if field not in entity:
            errors.append(
                ValidationError(
                    message=f"Entity missing required field: '{field}'",
                    field=f"entity.{field}",
                    error_code="MISSING_REQUIRED_FIELD",
                    suggestion=_get_entity_field_suggestion(field),
                )
            )

    # Validate entity name
    if "name" in entity:
        if not isinstance(entity["name"], str):
            errors.append(
                ValidationError(
                    message=f"Entity name must be string, got {type(entity['name']).__name__}",
                    field="entity.name",
                    error_code="WRONG_TYPE",
                    suggestion="Use PascalCase like 'MyEntity' or 'MCPServer'",
                )
            )
        elif not entity["name"][0].isupper():
            errors.append(
                ValidationError(
                    message=f"Entity name should start with uppercase: '{entity['name']}'",
                    field="entity.name",
                    error_code="NAMING_CONVENTION",
                    level=ErrorLevel.WARNING,
                    suggestion="Use PascalCase convention (e.g., 'MyEntity')",
                )
            )

    # Validate fields
    if "fields" in entity:
        if not isinstance(entity["fields"], list):
            errors.append(
                ValidationError(
                    message="Entity fields must be a list",
                    field="entity.fields",
                    error_code="WRONG_TYPE",
                    suggestion="Define as list: fields:\\n  - name: field1\\n  - name: field2",
                )
            )
        elif len(entity["fields"]) == 0:
            errors.append(
                ValidationError(
                    message="Entity must have at least one field",
                    field="entity.fields",
                    error_code="EMPTY_LIST",
                    suggestion="Add at least one field definition",
                )
            )
        else:
            # Validate individual fields
            for idx, field in enumerate(entity["fields"]):
                if not isinstance(field, dict):
                    errors.append(
                        ValidationError(
                            message=f"Field {idx} must be an object",
                            field=f"entity.fields[{idx}]",
                            error_code="WRONG_TYPE",
                        )
                    )
                elif "name" not in field:
                    errors.append(
                        ValidationError(
                            message=f"Field {idx} missing required 'name'",
                            field=f"entity.fields[{idx}].name",
                            error_code="MISSING_REQUIRED_FIELD",
                            suggestion="Add: name: field_name",
                        )
                    )

    return errors


def _validate_commands(commands: Any) -> list[ValidationError]:
    """Validate commands list."""
    errors = []

    if not isinstance(commands, list):
        errors.append(
            ValidationError(
                message="Commands must be a list",
                field="commands",
                error_code="WRONG_TYPE",
            )
        )
        return errors

    for idx, cmd in enumerate(commands):
        if not isinstance(cmd, dict):
            errors.append(
                ValidationError(
                    message=f"Command {idx} must be an object",
                    field=f"commands[{idx}]",
                    error_code="WRONG_TYPE",
                )
            )
            continue

        # Check required command fields
        if "name" not in cmd:
            errors.append(
                ValidationError(
                    message=f"Command {idx} missing required 'name'",
                    field=f"commands[{idx}].name",
                    error_code="MISSING_REQUIRED_FIELD",
                )
            )

        if "description" not in cmd:
            errors.append(
                ValidationError(
                    message=f"Command {idx} missing required 'description'",
                    field=f"commands[{idx}].description",
                    error_code="MISSING_REQUIRED_FIELD",
                )
            )

    return errors


def _validate_dependencies(dependencies: Any) -> list[ValidationError]:
    """Validate dependencies list."""
    errors = []

    if not isinstance(dependencies, list):
        errors.append(
            ValidationError(
                message="Dependencies must be a list",
                field="dependencies",
                error_code="WRONG_TYPE",
                suggestion="Define as list: dependencies:\\n  - package>=1.0.0",
            )
        )
        return errors

    for idx, dep in enumerate(dependencies):
        if not isinstance(dep, str):
            errors.append(
                ValidationError(
                    message=f"Dependency {idx} must be a string",
                    field=f"dependencies[{idx}]",
                    error_code="WRONG_TYPE",
                    suggestion="Use pip requirement format: 'package>=1.0.0'",
                )
            )

    return errors


# ============================================================================
# Fix Suggestions
# ============================================================================


def _get_missing_field_suggestion(field: str) -> str:
    """Get suggestion for missing required field."""
    suggestions = {
        "name": "Add: name: your-toolkit-name",
        "version": 'Add: version: "0.1.0"',
        "domain": f"Add: domain: {SUPPORTED_DOMAINS[0]} (or: {', '.join(SUPPORTED_DOMAINS[1:])})",
        "lifecycle": f"Add: lifecycle: {SUPPORTED_LIFECYCLES[0]}",
        "entity": "Add: entity:\\n  name: YourEntity\\n  fields:\\n    - name: field1",
    }
    return suggestions.get(field, f"Add required field: {field}")


def _get_entity_field_suggestion(field: str) -> str:
    """Get suggestion for missing entity field."""
    suggestions = {
        "name": "Add entity name: name: MyEntity",
        "fields": "Add entity fields: fields:\\n  - name: id\\n    type: str",
    }
    return suggestions.get(field, f"Add required entity field: {field}")


def format_validation_errors(
    errors: list[ValidationError], max_errors: int = 10
) -> str:
    """
    Format validation errors for display.

    Args:
        errors: List of validation errors
        max_errors: Maximum number of errors to display

    Returns:
        Formatted error string
    """
    if not errors:
        return "✅ No validation errors"

    lines = [f"Found {len(errors)} validation error(s):\n"]

    for idx, error in enumerate(errors[:max_errors]):
        lines.append(f"{idx + 1}. {error}")

    if len(errors) > max_errors:
        lines.append(f"\n... and {len(errors) - max_errors} more error(s)")

    return "\n".join(lines)

