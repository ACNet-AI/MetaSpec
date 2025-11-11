---
description: Archive a completed change proposal - move to history and update main specs
---

## User Input

```text
$ARGUMENTS
```

You **MUST** consider the user input before proceeding (if not empty).

## Goal

Archive a completed and applied change proposal, moving it to history and finalizing spec updates.

## Execution Flow

### 1. Validate proposal state

**Input**: Proposal ID (e.g., "2025-10-28-add-graphql-support")

**Check**:
- [ ] Proposal has been applied (`/metaspec:apply` completed)
- [ ] All tasks marked complete
- [ ] Tests passing
- [ ] Version bumped
- [ ] CHANGELOG updated

**If not applied**: Instruct user to run `/metaspec:apply` first

### 2. Merge spec deltas into main specs

**Update target spec** (based on proposal type):
- For `--type sds`: Update `specs/domain/XXX-name/spec.md`
- For `--type sdd`: Update `specs/toolkit/XXX-name/spec.md`

**Merge process**:
- Apply all changes from `spec-delta.md`
- Remove `[NEW]`, `[MODIFIED]`, `[DEPRECATED]` markers
- Update version metadata
- Add "Last updated" timestamp

**Result**: Main spec.md is now the source of truth

### 3. Move proposal to archive

**Create archive directory**:
```
changes/archive/[proposal-id]/
```

**Move files**:
```bash
mv changes/[proposal-id]/* changes/archive/[proposal-id]/
```

**Add completion metadata**:
- completion-date.txt
- applied-version.txt

### 4. Update proposal status

**In archived proposal.md**:
```markdown
**Status**: ~~Draft~~ → ~~Approved~~ → **Completed**
**Applied**: [DATE]
**Version**: v[X.Y.Z]
```

### 5. Create archive index

**Update `/changes/archive/INDEX.md`** (create if not exists):

```markdown
# Change Proposal Archive

## v[X.Y.Z] - [DATE]

- **[proposal-id]**: [Title]
  - Type: [type]
  - Breaking: [yes/no]
  - Applied: [date]
  - [Link](./[proposal-id]/proposal.md)

[... previous versions ...]
```

### 6. Clean up

**Remove active proposal directory**:
```bash
rm -rf changes/[proposal-id]/
```

**Verify**:
- Active proposal gone: `changes/[proposal-id]/` ✗
- Archive exists: `changes/archive/[proposal-id]/` ✅
- Main specs updated: `specs/spec.md` ✅
- Index updated: `changes/archive/INDEX.md` ✅

### 7. Create git tag (optional)

**If version bump**:
```bash
git tag -a v[X.Y.Z] -m "Release v[X.Y.Z]: [proposal title]"
```

### 8. Report

```
✅ Proposal archived: [proposal-id]

📦 Version Released: v[X.Y.Z]

📁 Archived to:
- changes/archive/[proposal-id]/

📝 Changes merged:
- spec.md updated
- CHANGELOG.md finalized
- Archive INDEX updated

🏷️ Git tag created: v[X.Y.Z]

🎉 Change complete!

📊 Proposal Lifecycle:
- Created: [date1] (/metaspec:proposal)
- Approved: [date2]
- Applied: [date3] (/metaspec:apply)
- Archived: [date4] (/metaspec:archive) ← Current

🔄 Next steps:
1. ✅ Commit changes
2. ✅ Push git tag: git push origin v[X.Y.Z]
3. ⏭️  Publish to PyPI (optional)
4. ⏭️  Announce release

💡 Suggested commit message:
   chore: archive proposal [proposal-id] (v[X.Y.Z])
```

## Important Notes

1. **Only archive after apply**
   - Must run `/metaspec:apply` first
   - All tasks complete
   - Tests passing
   - Don't archive draft proposals

2. **Archive is permanent record**
   - Keeps full history
   - Shows evolution of toolkit
   - Useful for understanding decisions

3. **Main specs become source of truth**
   - No more delta files
   - Clean specs without markers
   - Ready for next proposal

4. **Version control**
   - Git tag marks the release
   - Easy rollback if needed
   - Clear version history

5. **Multiple proposals**
   - Can have multiple active proposals
   - Archive completes one at a time
   - Independent workflows

## Directory Structure After Archive

```
[toolkit-name]/
├── specs/
│   └── spec.md                  # ← Updated with changes
│
├── changes/
│   ├── [other-active-proposal]/ # Other proposals still active
│   │
│   └── archive/
│       ├── INDEX.md             # ← Updated
│       │
│       ├── 2025-10-28-add-graphql-support/  # ← Archived
│       │   ├── proposal.md
│       │   ├── tasks.md
│       │   ├── impact.md
│       │   ├── specs/
│       │   ├── completion-date.txt
│       │   └── applied-version.txt
│       │
│       └── 2025-10-15-add-json-support/  # ← Previous archive
│           └── ...
│
├── src/
├── tests/
└── ...
```

## Example

**User**: `/metaspec:archive "2025-10-28-add-graphql-support"`

**Output**:
```
✅ Archiving proposal: add-graphql-support

✓ Validating proposal state...
  - Applied: ✅
  - Tasks complete: ✅ 10/10
  - Tests passing: ✅
  - Version bumped: ✅ v0.2.0
  - CHANGELOG updated: ✅

✓ Merging spec deltas...
  - spec.md: 3 additions, 1 modification, 0 removals

✓ Moving to archive...
  - Source: changes/2025-10-28-add-graphql-support/
  - Destination: changes/archive/2025-10-28-add-graphql-support/

✓ Updating archive index...
  - Added entry for v0.2.0

✓ Creating git tag...
  - Tag: v0.2.0
  - Message: "Release v0.2.0: Add GraphQL support"

✅ Proposal archived successfully!

📦 Release v0.2.0 finalized

📁 Archive location:
   changes/archive/2025-10-28-add-graphql-support/

🎉 Toolkit evolution complete!

📈 Toolkit History:
- v0.1.0 (2025-10-20): Initial release
- v0.2.0 (2025-10-28): Add GraphQL support  ← Current

🔄 Next: Publish v0.2.0 to PyPI or continue with next proposal
```

## Archive INDEX Example

```markdown
# Change Proposal Archive

## v0.2.0 - 2025-10-28

- **add-graphql-support**: Add GraphQL query testing support
  - Type: Feature
  - Breaking: No
  - Applied: 2025-10-28
  - [Proposal](./2025-10-28-add-graphql-support/proposal.md)

## v0.1.1 - 2025-10-25

- **fix-yaml-parsing**: Fix YAML parser line number tracking
  - Type: Fix
  - Breaking: No
  - Applied: 2025-10-25
  - [Proposal](./2025-10-25-fix-yaml-parsing/proposal.md)

## v0.1.0 - 2025-10-20

- Initial release (no proposals)
```

