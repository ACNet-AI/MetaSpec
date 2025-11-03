#!/usr/bin/env python3
"""
Sync templates from OpenSpec to MetaSpec library/sdd/openspec.

This script:
1. Fetches templates from OpenSpec repository (TypeScript source)
2. Extracts slash command content from TypeScript strings
3. Converts them to Jinja2 Markdown format
4. Generalizes project-specific references to make templates reusable
5. Places them in library/sdd/openspec/ directory

Usage:
    python scripts/sync-openspec-templates.py

Features:
    - Automatic variable expansion for TypeScript template strings
    - Recursive ${variable} reference resolution
    - Project-specific reference generalization (CLI names, directories)
    - Jinja2 variable injection for reusability
"""

import re
import subprocess
import tempfile
from datetime import datetime
from pathlib import Path

# Configuration
OPENSPEC_REPO = "https://github.com/Fission-AI/OpenSpec.git"
OPENSPEC_TEMPLATES_PATH = "src/core/templates"
TARGET_DIR = Path(__file__).parent.parent / "src/metaspec/templates/library/sdd/openspec"

# Slash commands to extract from OpenSpec
SLASH_COMMANDS = ["proposal", "apply", "archive"]


def clone_openspec(temp_dir: Path) -> Path:
    """Clone OpenSpec repository to temporary directory."""
    print(f"📥 Cloning OpenSpec from {OPENSPEC_REPO}...")

    subprocess.run(
        ["git", "clone", "--depth", "1", OPENSPEC_REPO, str(temp_dir)],
        check=True,
        capture_output=True,
    )

    return temp_dir / OPENSPEC_TEMPLATES_PATH


def extract_slash_command_content(ts_file: Path) -> dict[str, str]:
    """
    Extract slash command content from TypeScript template file.

    Returns dict mapping command name to content string.
    """
    content = ts_file.read_text(encoding="utf-8")

    # First, extract all const variables with their template string content
    variables = {}

    # Match: const varName = `template string`;
    # This pattern handles escaped backticks \` inside the template string
    var_pattern = r"const\s+(\w+)\s*=\s*`((?:[^`\\]|\\.)*)`;?"
    for match in re.finditer(var_pattern, content, re.DOTALL):
        var_name = match.group(1)
        var_content = match.group(2)
        variables[var_name] = var_content

    # Function to recursively expand ${var} references
    def expand_variables(text: str, depth: int = 0) -> str:
        if depth > 10:  # Prevent infinite recursion
            return text

        # Find ${varName} patterns
        var_ref_pattern = r'\$\{(\w+)\}'

        def replace_var(match):
            var_name = match.group(1)
            if var_name in variables:
                # Recursively expand the referenced variable
                return expand_variables(variables[var_name], depth + 1)
            return match.group(0)  # Keep original if not found

        return re.sub(var_ref_pattern, replace_var, text)

    # Now process each command
    commands = {}

    # Find the slashCommandBodies object
    # Pattern: proposal: [proposalGuardrails, proposalSteps, proposalReferences].join('\n\n'),
    for cmd in SLASH_COMMANDS:
        pattern = rf"{cmd}:\s*\[([\w,\s]+)\]\.join\(['\"]\\n\\n['\"]\)"
        match = re.search(pattern, content)

        if match:
            # Get the variable names
            var_names = [v.strip() for v in match.group(1).split(',')]

            # Extract and expand content from these variables
            parts = []
            for var_name in var_names:
                if var_name in variables:
                    # Expand variable references
                    expanded = expand_variables(variables[var_name])
                    parts.append(expanded)

            # Join parts
            if parts:
                commands[cmd] = "\n\n".join(parts)

    return commands


def convert_to_jinja2_template(command_name: str, content: str) -> str:
    """
    Convert OpenSpec command content to MetaSpec Jinja2 template format.
    Generalizes project-specific references to make templates reusable.
    """
    # Add MetaSpec header
    header_template = """# Generated Template

**Project**: {{{{ name }}}}
**Version**: {{{{ version }}}}
**Domain**: {{{{ domain }}}}
**Date**: {{{{ date }}}}

---

---
description: {description}
---

## User Input

```text
$ARGUMENTS
```

You **MUST** consider the user input before proceeding (if not empty).

## {command_title}

"""

    # Create GENERALIZED descriptions (removed "OpenSpec-managed projects")
    descriptions = {
        "proposal": "Create a change proposal for specification evolution and team collaboration",
        "apply": "Implement an approved change proposal - track tasks and execute planned changes",
        "archive": "Archive a completed change - move to archive and update specifications"
    }

    titles = {
        "proposal": "Creating Change Proposals",
        "apply": "Implementing Changes",
        "archive": "Archiving Changes"
    }

    description = descriptions.get(command_name, "Command for specification-driven development")
    title = titles.get(command_name, "Command")

    header = header_template.format(description=description, command_title=title)

    # Clean up the content
    # Remove \` escapes
    content = content.replace("\\`", "`")

    # Remove \n escape sequences (they're already newlines)
    content = content.replace("\\n", "\n")

    # Remove {{ variable }} references from TypeScript string interpolation
    # These aren't meant to be Jinja2 variables
    content = re.sub(r'\{\{\s*(\w+)\s*\}\}', r'[\1]', content)

    # === GENERALIZATION: Replace project-specific references ===

    # 1. Replace "openspec" CLI commands with variable (in backticks)
    content = re.sub(
        r'`openspec\s+(\w+)',
        r'`{{ cli_name }} \1',
        content
    )

    # 2. Replace "openspec/" directory paths with variable (in backticks)
    content = re.sub(
        r'`openspec/([^`]+)`',
        r'`{{ specs_dir }}/\1`',
        content
    )

    # 3. Replace standalone "openspec" references in commands (no backticks)
    content = re.sub(
        r'\bopenspec\s+(list|show|validate|update|archive)\b',
        r'{{ cli_name }} \1',
        content
    )

    # 4. Replace directory structure references (without backticks)
    content = re.sub(
        r'\bopenspec/(changes|specs|project\.md|AGENTS\.md)',
        r'{{ specs_dir }}/\1',
        content
    )

    # 5. Replace "OpenSpec conventions" with generic term
    content = content.replace("OpenSpec conventions", "project conventions")
    content = content.replace("OpenSpec-managed", "spec-driven")

    # 6. Replace remaining standalone "openspec/" or "openspec`" references
    content = re.sub(r'\bopenspec/\b', r'{{ specs_dir }}/', content)
    content = re.sub(r'`openspec`', r'`{{ specs_dir }}`', content)
    content = re.sub(r'the `openspec/`', r'the `{{ specs_dir }}/`', content)

    # 7. Handle edge cases in parentheses or quotes
    content = content.replace('the `openspec/', 'the `{{ specs_dir }}/')
    content = content.replace('inside the `openspec/', 'inside the `{{ specs_dir }}/')
    content = content.replace('`ls openspec`', '`ls {{ specs_dir }}`')
    content = re.sub(r'run `ls openspec`', r'run `ls {{ specs_dir }}`', content)

    return header + content + "\n"


def sync_templates(source_dir: Path, target_dir: Path):
    """Sync templates from source to target directory."""

    if not source_dir.exists():
        print(f"❌ Source directory not found: {source_dir}")
        return

    # Ensure target directories exist
    (target_dir / "commands").mkdir(parents=True, exist_ok=True)
    (target_dir / "templates").mkdir(parents=True, exist_ok=True)

    # Read the slash-command-templates.ts file
    slash_cmd_file = source_dir / "slash-command-templates.ts"

    if not slash_cmd_file.exists():
        print(f"❌ Template file not found: {slash_cmd_file}")
        return

    print(f"\n📖 Extracting slash commands from {slash_cmd_file.name}...")

    # Extract command content
    commands = extract_slash_command_content(slash_cmd_file)

    synced_count = 0

    # Convert each command to Jinja2 template
    for cmd_name, cmd_content in commands.items():
        # Convert to Jinja2 template
        template_content = convert_to_jinja2_template(cmd_name, cmd_content)

        # Write to commands directory
        target_file = target_dir / "commands" / f"{cmd_name}.md.j2"
        target_file.write_text(template_content, encoding="utf-8")

        print(f"✅ Synced: {cmd_name} → commands/{target_file.name}")
        synced_count += 1

    print(f"\n✨ Synced {synced_count} slash commands to {target_dir}")


def create_index_file(target_dir: Path):
    """Create an index file listing all available templates."""

    commands = sorted((target_dir / "commands").glob("*.j2"))
    templates = sorted((target_dir / "templates").glob("*.j2"))
    last_synced = datetime.fromtimestamp(Path(__file__).stat().st_mtime).strftime("%Y-%m-%d %H:%M:%S")

    index_content = f"""# OpenSpec Templates

> **Synchronized from [OpenSpec](https://github.com/Fission-AI/OpenSpec)**

**Lifecycle**: Brownfield (1→n)
**Best for**: Collaborative specification evolution

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

These templates are used when generating speckits with `source: "sdd/openspec"`:

```yaml
# Example: MetaSpecDefinition configuration
slash_commands:
  - name: "propose"
    description: "Create change proposal"
    source: "sdd/openspec"

  - name: "archive"
    description: "Archive completed change"
    source: "sdd/openspec"
```

**Note**:
- OpenSpec focuses on specification evolution and team collaboration
- Use for Brownfield (1→n) scenarios where specs evolve over time
- Complements spec-kit which focuses on Greenfield (0→1) development

## About OpenSpec

OpenSpec is a specification-driven development tool that manages:
- **Changes**: Proposals for specification updates
- **Specs**: Current state of requirements
- **Archive**: History of completed changes

**Three-stage workflow**:
1. **Creating Changes**: Propose spec modifications
2. **Implementing Changes**: Execute approved proposals
3. **Archiving Changes**: Record completion and update specs

## Updating

Run `python scripts/sync-openspec-templates.py` to sync latest templates from OpenSpec.

**Last synced**: {last_synced}
"""

    (target_dir / "README.md").write_text(index_content, encoding="utf-8")
    print(f"📝 Created index: {target_dir / 'README.md'}")


def main():
    """Main sync process."""
    print("🔄 Syncing OpenSpec templates to MetaSpec...\n")

    # Create temporary directory for cloning
    with tempfile.TemporaryDirectory() as temp_dir:
        temp_path = Path(temp_dir)

        try:
            # Clone OpenSpec
            source_dir = clone_openspec(temp_path)

            # Sync templates
            sync_templates(source_dir, TARGET_DIR)

            # Create index
            create_index_file(TARGET_DIR)

            print("\n✅ Sync complete!")
            print(f"📂 Templates location: {TARGET_DIR}")
            print("\n💡 Next steps:")
            print(f"   1. Review generated templates in {TARGET_DIR}/commands/")
            print("   2. Test with: metaspec init --help")
            print("   3. Use in meta-spec with: source: 'sdd/openspec'")

        except subprocess.CalledProcessError as e:
            print(f"❌ Git error: {e}")
            print("Make sure git is installed and you have internet connection.")
        except Exception as e:
            print(f"❌ Error: {e}")
            raise


if __name__ == "__main__":
    main()

