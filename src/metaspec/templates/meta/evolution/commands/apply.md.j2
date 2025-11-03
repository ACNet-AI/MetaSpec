---
description: Apply an approved change proposal - execute tasks and update specifications
---

## User Input

```text
$ARGUMENTS
```

You **MUST** consider the user input before proceeding (if not empty).

## Goal

Execute an approved change proposal by implementing tasks and updating specifications.

## Execution Flow

### 1. Load proposal

**Input**: Proposal ID from user (e.g., "2025-10-28-add-graphql-support")

**Read**:
- `changes/[proposal-id]/proposal.md`
- `changes/[proposal-id]/tasks.md`
- `changes/[proposal-id]/impact.md`
- `changes/[proposal-id]/specs/spec-delta.md`

**Validate**:
- Proposal status is "Approved"
- All approval checkboxes marked
- No merge conflicts with current specs

### 2. Check prerequisites

**Verify**:
- [ ] Proposal approved
- [ ] Impact assessed
- [ ] Migration guide prepared
- [ ] Tests planned
- [ ] Documentation planned

**If not approved**: Ask user to approve in proposal.md first

### 3. Execute tasks

**Follow tasks.md** in proposal:
- Phase 1: Update specifications
- Phase 2: Implement changes
- Phase 3: Update tests
- Phase 4: Update documentation

**Same process as** `/metaspec:implement`:
- TDD approach
- Mark tasks complete
- Report progress

### 4. Merge spec deltas

**Apply changes from** `spec-delta.md`:

**For ADD**:
```yaml
# Append to spec.md
- name: query
  type: string
  required: false
  description: GraphQL query
```

**For MODIFY**:
```yaml
# Update existing field
- name: endpoint
  type: string | object  # ← Changed from string
```

**For REMOVE**:
```yaml
# Comment out or remove
# - name: old_field  ← Deprecated in v0.2.0
```

### 5. Update version

**In files**:
- `pyproject.toml`: version = "[X.Y.Z]"
- `CHANGELOG.md`: Add entry for v[X.Y.Z]
- `spec.md`: Update version metadata

**Version bump**:
- From proposal/impact.md
- MAJOR | MINOR | PATCH

### 6. Update CHANGELOG.md

**Add entry**:
```markdown
## [X.Y.Z] - [DATE]

### Added
- [Feature 1 from proposal]
- [Feature 2 from proposal]

### Changed
- [Change 1 from proposal]

### Deprecated
- [Deprecation 1 from proposal]

### Removed
- [Removal 1 from proposal]

### Fixed
- [Fix 1 from proposal]
```

### 7. Validate

**Check**:
- [ ] All tasks complete
- [ ] Specs updated with deltas
- [ ] Version bumped correctly
- [ ] CHANGELOG updated
- [ ] Tests passing
- [ ] Constitution still compliant

**Run tests**:
```bash
pytest tests/ --cov
```

**Run linter**:
```bash
mypy src/ --strict
ruff check src/
```

### 8. Report

```
✅ Change proposal applied: [proposal-id]

📊 Summary:
- Tasks completed: [N]/[N]
- Specs updated: spec.md
- Version: v[OLD] → v[NEW]
- Tests: ✅ passing
- Linter: ✅ passing

📝 Changes:
- Added: [list]
- Modified: [list]
- Removed: [list]

📦 Next steps:
1. Test with real-world specs
2. Run /metaspec:archive "[proposal-id]" to finalize
3. Commit changes
4. Create git tag v[X.Y.Z]
5. Publish to PyPI

💡 Suggested commit message:
   feat: [proposal title] v[X.Y.Z]
```

## Important Notes

1. **Proposal must be approved**
   - Check proposal.md status
   - All approval items checked
   - No shortcuts

2. **Follow tasks sequentially**
   - Don't skip phases
   - Verify checkpoints
   - Mark tasks complete

3. **Merge conflicts**
   - If specs changed since proposal
   - Resolve manually
   - Re-validate proposal

4. **Version bump**
   - Follow semantic versioning
   - Update all version references
   - Document in CHANGELOG

5. **Testing is mandatory**
   - All tests must pass
   - No warnings allowed
   - Coverage maintained

## Example

**User**: `/metaspec:apply "2025-10-28-add-graphql-support"`

**Output**:
```
🔄 Applying proposal: add-graphql-support

📋 Proposal Status: Approved ✅
📋 Impact: MINOR version bump (v0.1.0 → v0.2.0)
📋 Breaking changes: No

Phase 1: Update Specifications
✅ T001: Update spec.md with GraphQL fields
✅ T002: Update validator-design.md with GraphQL validation

Phase 2: Implement Changes
✅ T003: Add query field to APITest model
✅ T004: Add GraphQL syntax validator
✅ T005: Update CLI to support GraphQL

Phase 3: Update Tests
✅ T006: Add tests for GraphQL query field
✅ T007: Add tests for GraphQL validation

Phase 4: Update Documentation
✅ T008: Update README.md with GraphQL examples
✅ T009: Update CHANGELOG.md
✅ T010: Add GraphQL example specs

🧪 Running tests...
✅ 45/45 tests passing
✅ Coverage: 94%

✅ Proposal applied successfully!

📦 Ready to archive and release v0.2.0

🔄 Next: /metaspec:archive "2025-10-28-add-graphql-support"
```

