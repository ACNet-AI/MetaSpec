#!/usr/bin/env python3
"""
Sync templates from spec-kit to MetaSpec library/sdd/spec-kit.

This script:
1. Fetches templates from GitHub's spec-kit repository
2. Converts them to Jinja2 format with MetaSpec variables
3. Generalizes project-specific references (CLI commands, directories)
4. Places them in library/sdd/spec-kit/ directory

Usage:
    python scripts/sync-spec-kit-templates.py

Features:
    - Automatic Jinja2 template conversion
    - Variable mapping for MetaSpec integration
    - Command reference generalization (/speckit.* → /{{ cli_prefix }}.*)
    - Directory reference generalization (.specify/ → .{{ specs_dir }}/)
"""

import re
import subprocess
import tempfile
from datetime import datetime
from pathlib import Path

# Configuration
SPEC_KIT_REPO = "https://github.com/github/spec-kit.git"
SPEC_KIT_TEMPLATES_PATH = "templates"
TARGET_DIR = Path(__file__).parent.parent / "src/metaspec/templates/library/sdd/spec-kit"

# Variable mappings from spec-kit to MetaSpec
VARIABLE_MAPPINGS = {
    # Add any specific variable transformations here
    # Example: "{{project_name}}" -> "{{name}}"
}


def clone_spec_kit(temp_dir: Path) -> Path:
    """Clone spec-kit repository to temporary directory."""
    print(f"📥 Cloning spec-kit from {SPEC_KIT_REPO}...")

    subprocess.run(
        ["git", "clone", "--depth", "1", SPEC_KIT_REPO, str(temp_dir)],
        check=True,
        capture_output=True,
    )

    return temp_dir / SPEC_KIT_TEMPLATES_PATH


def transform_template(content: str) -> str:
    """
    Transform spec-kit template to MetaSpec format.

    Adds Jinja2 variables and MetaSpec-specific context.
    Generalizes project-specific references for reusability.
    """
    # Add MetaSpec header if not present
    if not content.startswith("#"):
        header = """# Generated Template

**Project**: {{ name }}
**Version**: {{ version }}
**Domain**: {{ domain }}
**Date**: {{ date }}

---

"""
        content = header + content

    # Apply variable mappings
    for old_var, new_var in VARIABLE_MAPPINGS.items():
        content = content.replace(old_var, new_var)

    # === GENERALIZATION: Replace project-specific references ===

    # 1. Replace /speckit.* command references with variable
    # Examples: /speckit.specify, /speckit.plan, /speckit.tasks
    content = re.sub(
        r'/speckit\.(\w+)',
        r'/{{ cli_prefix }}.\1',
        content
    )

    # 2. Replace .specify/ directory references
    content = content.replace('.specify/', '.{{ specs_dir }}/')
    content = content.replace('`.specify/', '`.{{ specs_dir }}/')

    # 3. Replace standalone "spec-kit" references in descriptive text
    # But keep it in URLs and technical references
    content = re.sub(
        r'\bspec-kit\s+',
        r'{{ toolkit_name }} ',
        content,
        flags=re.IGNORECASE
    )

    return content


def sync_templates(source_dir: Path, target_dir: Path):
    """Sync templates from source to target directory."""

    if not source_dir.exists():
        print(f"❌ Source directory not found: {source_dir}")
        return

    # Ensure target directories exist
    (target_dir / "commands").mkdir(parents=True, exist_ok=True)
    (target_dir / "templates").mkdir(parents=True, exist_ok=True)

    synced_count = 0

    # Find all markdown files
    for source_file in source_dir.rglob("*.md"):
        # Determine if it's a command or template
        relative_path = source_file.relative_to(source_dir)

        # Skip certain files
        if source_file.name in ["README.md", "CONTRIBUTING.md"]:
            continue

        # Read and transform content
        content = source_file.read_text(encoding="utf-8")
        transformed_content = transform_template(content)

        # Determine target location based on source path
        # spec-kit structure: templates/commands/*.md → commands/
        #                    templates/*.md → templates/
        if "commands" in source_file.parts:
            target_subdir = "commands"
        else:
            target_subdir = "templates"

        # Add .j2 extension for Jinja2
        target_file = target_dir / target_subdir / f"{source_file.stem}.md.j2"

        # Write transformed template
        target_file.write_text(transformed_content, encoding="utf-8")
        print(f"✅ Synced: {relative_path} → {target_subdir}/{target_file.name}")
        synced_count += 1

    print(f"\n✨ Synced {synced_count} templates to {target_dir}")


def create_index_file(target_dir: Path):
    """Create an index file listing all available templates."""

    commands = sorted((target_dir / "commands").glob("*.j2"))
    templates = sorted((target_dir / "templates").glob("*.j2"))
    last_synced = datetime.fromtimestamp(Path(__file__).stat().st_mtime).strftime("%Y-%m-%d %H:%M:%S")

    index_content = f"""# Spec-Kit Templates

> **Synchronized from [spec-kit](https://github.com/github/spec-kit)**

**Lifecycle**: Greenfield (0→1)
**Best for**: Creating new features and projects from scratch

## Commands ({len(commands)})

"""

    for cmd in commands:
        name = cmd.stem.replace(".md", "")
        index_content += f"- `{name}` - {cmd.name}\n"

    index_content += f"\n## Templates ({len(templates)})\n\n"

    for tmpl in templates:
        name = tmpl.stem.replace("-template.md", "")
        index_content += f"- `{name}` - {tmpl.name}\n"

    index_content += f"""
## Usage

Templates are selected via `source` field in MetaSpecDefinition slash_commands:

```yaml
# Example: MetaSpecDefinition structure (created via interactive wizard)
slash_commands:
  - name: "specify"
    description: "Create feature specification"
    source: "sdd/spec-kit"

  - name: "plan"
    description: "Plan implementation"
    source: "sdd/spec-kit"
```

**Note**:
- Use `source: "sdd/spec-kit"` for explicit path
- Use `source: "dev"` as shorthand (defaults to `dev/spec-kit`)

## Updating

Run `python scripts/sync-spec-kit-templates.py` to sync latest templates from spec-kit.

**Last synced**: {last_synced}
"""

    (target_dir / "README.md").write_text(index_content, encoding="utf-8")
    print(f"📝 Created index: {target_dir / 'README.md'}")


def main():
    """Main sync process."""
    print("🔄 Syncing spec-kit templates to MetaSpec...\n")

    # Create temporary directory for cloning
    with tempfile.TemporaryDirectory() as temp_dir:
        temp_path = Path(temp_dir)

        try:
            # Clone spec-kit
            source_dir = clone_spec_kit(temp_path)

            # Sync templates
            sync_templates(source_dir, TARGET_DIR)

            # Create index
            create_index_file(TARGET_DIR)

            print("\n✅ Sync complete!")
            print(f"📂 Templates location: {TARGET_DIR}")

        except subprocess.CalledProcessError as e:
            print(f"❌ Git error: {e}")
            print("Make sure git is installed and you have internet connection.")
        except Exception as e:
            print(f"❌ Error: {e}")
            raise


if __name__ == "__main__":
    main()

