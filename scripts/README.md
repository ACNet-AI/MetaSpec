# MetaSpec Scripts

This directory contains utility scripts for MetaSpec maintenance and development.

## sync-spec-kit-templates.py

Automatically sync development templates from [spec-kit](https://github.com/github/spec-kit) repository.

### What it does

1. Clones the spec-kit repository
2. Extracts templates from `templates/` directory
3. Converts them to Jinja2 format with MetaSpec variables
4. Places them in `src/metaspec/templates/library/sdd/spec-kit/`

### Usage

```bash
# Run the sync script
python scripts/sync-spec-kit-templates.py

# Or with uv
uv run scripts/sync-spec-kit-templates.py
```

### Requirements

- Git installed and available in PATH
- Internet connection to clone spec-kit repo
- Python 3.10+

### Output Structure

```
src/metaspec/templates/library/sdd/spec-kit/
├── commands/          # AI command instructions
│   ├── constitution.md.j2
│   ├── specify.md.j2
│   └── ...
├── templates/         # Output format templates
│   ├── spec-template.md.j2
│   ├── plan-template.md.j2
│   └── ...
└── README.md          # Index of synced templates
```

### Configuration

Edit `sync-spec-kit-templates.py` to customize:

- `SPEC_KIT_REPO`: Source repository URL
- `TARGET_DIR`: Destination directory
- `VARIABLE_MAPPINGS`: Variable name transformations

### Notes

- Existing files will be overwritten
- Manual edits to synced files will be lost
- Review changes after sync before committing

## sync-openspec-templates.py

Automatically sync specification evolution templates from [OpenSpec](https://github.com/Fission-AI/OpenSpec) repository.

### What it does

1. Clones the OpenSpec repository
2. Extracts slash command templates from `src/core/templates/slash-command-templates.ts`
3. Expands TypeScript template variables recursively
4. Converts them to Jinja2 Markdown format
5. Places them in `src/metaspec/templates/library/sdd/openspec/`

### Usage

```bash
# Run the sync script
python scripts/sync-openspec-templates.py

# Or with uv
uv run scripts/sync-openspec-templates.py
```

### Requirements

- Git installed and available in PATH
- Internet connection to clone OpenSpec repo
- Python 3.10+

### Output Structure

```
src/metaspec/templates/library/sdd/openspec/
├── commands/          # Slash command templates
│   ├── proposal.md.j2 # Create change proposals
│   ├── apply.md.j2    # Implement changes
│   └── archive.md.j2  # Archive completed changes
├── templates/         # (Reserved for output templates)
└── README.md          # Index of synced templates
```

### Configuration

Edit `sync-openspec-templates.py` to customize:

- `OPENSPEC_REPO`: Source repository URL
- `TARGET_DIR`: Destination directory
- `SLASH_COMMANDS`: Commands to extract

### Notes

- OpenSpec uses TypeScript template strings with variable interpolation
- Script handles `${variable}` expansion automatically
- Escaped backticks in content are preserved correctly
- Existing files will be overwritten
- Review changes after sync before committing

