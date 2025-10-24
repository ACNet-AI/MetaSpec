"""
Error types for MetaSpec validation.

This module defines error classes and types for validation failures.
"""

from dataclasses import dataclass
from enum import Enum


class ErrorLevel(Enum):
    """Validation error severity levels."""

    ERROR = "error"
    WARNING = "warning"
    INFO = "info"


@dataclass
class ValidationError:
    """
    Represents a validation error with location and suggestion.

    Attributes:
        message: Error message
        line: Line number (1-indexed, 0 if unknown)
        column: Column number (1-indexed, 0 if unknown)
        field: Field path (e.g., "entity.fields[0].name")
        error_code: Error code for categorization
        suggestion: Optional fix suggestion
        level: Error severity level
    """

    message: str
    line: int = 0
    column: int = 0
    field: str | None = None
    error_code: str | None = None
    suggestion: str | None = None
    level: ErrorLevel = ErrorLevel.ERROR

    def __str__(self) -> str:
        """Format error as human-readable string."""
        location = ""
        if self.line > 0:
            location = f"Line {self.line}"
            if self.column > 0:
                location += f", Column {self.column}"
            location += ": "

        field_info = f" (field: {self.field})" if self.field else ""

        parts = [f"{location}{self.message}{field_info}"]

        if self.suggestion:
            parts.append(f"💡 Suggestion: {self.suggestion}")

        return "\n   ".join(parts)


@dataclass
class ValidationResult:
    """
    Result of validation with errors and warnings.

    Attributes:
        success: True if validation passed
        errors: List of validation errors
        warnings: List of validation warnings
        data: Parsed data (if validation succeeded)
    """

    success: bool
    errors: list[ValidationError]
    warnings: list[ValidationError]
    data: dict | None = None

    @property
    def has_errors(self) -> bool:
        """Check if there are any errors."""
        return len(self.errors) > 0

    @property
    def has_warnings(self) -> bool:
        """Check if there are any warnings."""
        return len(self.warnings) > 0

    @property
    def total_issues(self) -> int:
        """Total number of issues (errors + warnings)."""
        return len(self.errors) + len(self.warnings)


class MetaSpecValidationError(Exception):
    """
    Exception raised when meta-spec validation fails.

    This is used for fatal errors that prevent further processing.
    """

    def __init__(self, message: str, errors: list[ValidationError] | None = None):
        self.message = message
        self.errors = errors or []
        super().__init__(message)


class SchemaValidationError(MetaSpecValidationError):
    """Raised when JSON Schema validation fails."""

    pass


class YAMLParseError(MetaSpecValidationError):
    """Raised when YAML parsing fails."""

    pass

