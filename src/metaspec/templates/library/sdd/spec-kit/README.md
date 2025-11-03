# Spec-Kit Templates

> **Synchronized from [spec-kit](https://github.com/github/spec-kit)**

**Lifecycle**: Greenfield (0→1)
**Best for**: Creating new features and projects from scratch

## Commands (8)

- `analyze` - analyze.md.j2
- `checklist` - checklist.md.j2
- `clarify` - clarify.md.j2
- `constitution` - constitution.md.j2
- `implement` - implement.md.j2
- `plan` - plan.md.j2
- `specify` - specify.md.j2
- `tasks` - tasks.md.j2

## Templates (5)

- `agent-file` - agent-file-template.md.j2
- `checklist` - checklist-template.md.j2
- `plan` - plan-template.md.j2
- `spec` - spec-template.md.j2
- `tasks` - tasks-template.md.j2

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

**Last synced**: 2025-11-03 15:25:44
