# OpenSpec Templates

> **Synchronized from [OpenSpec](https://github.com/Fission-AI/OpenSpec)**

**Lifecycle**: Brownfield (1→n)
**Best for**: Collaborative specification evolution

## Commands (3)

- `apply` - apply.md.j2
- `archive` - archive.md.j2
- `proposal` - proposal.md.j2

## Templates (0)


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

**Last synced**: 2025-11-03 15:25:52
