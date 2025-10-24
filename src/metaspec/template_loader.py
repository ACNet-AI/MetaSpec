"""
Template loader for MetaSpec.

Loads Jinja2 templates from:
1. Embedded package resources (default)
2. Custom template directory (override via --templates flag)
"""

import importlib.resources
from pathlib import Path

from jinja2 import Environment, FileSystemLoader, PackageLoader


class TemplateLoader:
    """
    Load and manage Jinja2 templates for toolkit generation.

    Supports both embedded templates (default) and custom template directories.
    """

    def __init__(self, custom_template_dir: Path | None = None):
        """
        Initialize template loader.

        Args:
            custom_template_dir: Optional path to custom template directory.
                                 If provided, overrides embedded templates.
        """
        self.custom_template_dir = custom_template_dir
        self._env: Environment | None = None
        self._template_cache: dict[str, str] = {}

    def get_environment(self) -> Environment:
        """
        Get Jinja2 environment configured with appropriate loader.

        Returns:
            Jinja2 Environment instance
        """
        if self._env is None:
            if self.custom_template_dir:
                # Use custom template directory
                loader = FileSystemLoader(str(self.custom_template_dir))
            else:
                # Use embedded templates from package
                loader = PackageLoader("metaspec", "templates")

            self._env = Environment(
                loader=loader,
                trim_blocks=True,
                lstrip_blocks=True,
                keep_trailing_newline=True,
            )

        return self._env

    def load_template(self, template_name: str, domain: str = "base") -> str:
        """
        Load a template by name and domain.

        Args:
            template_name: Template filename (e.g., "AGENTS.md.j2")
            domain: Domain subdirectory (e.g., "base", "generic", "mcp")

        Returns:
            Template content as string

        Raises:
            FileNotFoundError: If template not found
        """
        cache_key = f"{domain}/{template_name}"

        # Check cache
        if cache_key in self._template_cache:
            return self._template_cache[cache_key]

        env = self.get_environment()

        # Try to load template
        template_path = f"{domain}/{template_name}"
        try:
            template = env.get_template(template_path)
            content = template.source
            self._template_cache[cache_key] = content
            return content
        except Exception as e:
            raise FileNotFoundError(
                f"Template not found: {template_path}\n"
                f"Domain: {domain}, Template: {template_name}\n"
                f"Error: {e}"
            ) from e

    def get_template_names(self, domain: str = "base") -> list[str]:
        """
        Get list of all template names for a domain.

        Args:
            domain: Domain subdirectory

        Returns:
            List of template filenames
        """
        if self.custom_template_dir:
            # List files in custom directory
            domain_dir = self.custom_template_dir / domain
            if not domain_dir.exists():
                return []
            return [f.name for f in domain_dir.glob("*.j2")]
        else:
            # List embedded templates
            try:
                # For Python 3.9+
                files = importlib.resources.files("metaspec").joinpath(
                    f"templates/{domain}"
                )
                if not files.is_dir():
                    return []
                return [f.name for f in files.iterdir() if f.name.endswith(".j2")]
            except AttributeError:
                # Fallback for older Python versions
                return []

    def render_template(self, template_name: str, domain: str, context: dict) -> str:
        """
        Render a template with given context.

        Args:
            template_name: Template filename
            domain: Domain subdirectory
            context: Template variables

        Returns:
            Rendered template content
        """
        env = self.get_environment()
        template_path = f"{domain}/{template_name}"
        template = env.get_template(template_path)
        return template.render(**context)

    def get_all_templates_for_domain(self, domain: str) -> dict[str, str]:
        """
        Get all templates for a given domain.

        Returns dict mapping template names to their rendered paths.

        Args:
            domain: Domain name (e.g., "generic", "mcp")

        Returns:
            Dict of {template_name: output_path}
        """
        templates = {}

        # Base templates (always included)
        base_templates = self.get_template_names("base")
        for template_name in base_templates:
            # Remove .j2 extension to get output filename
            output_name = template_name.replace(".j2", "")
            templates[f"base/{template_name}"] = output_name

        # Domain-specific templates
        domain_templates = self.get_template_names(domain)
        for template_name in domain_templates:
            output_name = template_name.replace(".j2", "")
            templates[f"{domain}/{template_name}"] = f"templates/{output_name}"

        return templates


def create_loader(custom_template_dir: Path | None = None) -> TemplateLoader:
    """
    Factory function to create a TemplateLoader instance.

    Args:
        custom_template_dir: Optional path to custom templates

    Returns:
        Configured TemplateLoader instance
    """
    return TemplateLoader(custom_template_dir=custom_template_dir)
