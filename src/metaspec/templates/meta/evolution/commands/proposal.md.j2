---
description: Create a change proposal for toolkit evolution - manages spec changes, tasks, and impact analysis
---

## User Input

```text
$ARGUMENTS
```

You **MUST** consider the user input before proceeding (if not empty).

## Goal

Create a structured change proposal for evolving an existing toolkit. This is for **Brownfield** scenarios where the toolkit already exists and needs improvements.

## Execution Flow

### 1. Understand change request

**Parse user input** for:
- What needs to change (entity, validation, CLI, etc.)
- Why the change is needed (user feedback, new requirements)
- Impact scope (breaking vs non-breaking)

**Example requests**:
- "Add GraphQL support to API Test Kit"
- "Add custom assertion types to validator"
- "Support JSON input in addition to YAML"

### 2. Create proposal directory

**Structure**:
```
changes/
└── [proposal-id]/
    ├── proposal.md       # Change description
    ├── tasks.md          # Implementation tasks
    ├── impact.md         # Impact analysis
    └── specs/           # Spec deltas
        └── spec-delta.md
```

**Proposal ID**: `[date]-[short-name]`
- Example: `2025-10-28-add-graphql-support`

### 3. Generate proposal.md

**Content**:
```markdown
# Change Proposal: [Title]

**ID**: [proposal-id]
**Date**: [DATE]
**Status**: Draft
**Type**: Feature | Enhancement | Fix | Breaking Change

## Summary

[One-paragraph description of the change]

## Motivation

**Why is this change needed?**
- User feedback: [citations]
- New requirements: [description]
- Technical debt: [issues]

## Proposed Changes

### Entity Changes
- Add field: [field_name] ([type], [required/optional])
- Modify field: [field_name] ([what changes])
- Remove field: [field_name] ([why deprecated])

### Validation Changes
- Add rule: [rule_description]
- Modify rule: [what changes]
- Remove rule: [why deprecated]

### CLI Changes
- Add command: [command_name]
- Modify command: [what changes]
- Remove command: [why deprecated]

### Workflow Changes
- Add workflow: [workflow_name]
- Modify workflow: [what changes]

## Impact Analysis

**Breaking Changes**: Yes | No

**Affected Components**:
- Models: [impact]
- Parser: [impact]
- Validator: [impact]
- CLI: [impact]
- Tests: [impact]

**Migration Required**: Yes | No
- [Migration steps if yes]

**Version Bump**: MAJOR | MINOR | PATCH
- Rationale: [explanation]

## Constitution Alignment

**Principles Affected**:
- Entity-First: [how change aligns]
- Validator Extensibility: [how change aligns]
- AI-Agent Friendly: [how change aligns]

**Violations**: None | [list if any]

## Implementation Plan

**Estimated Effort**: [X] days

**Phases**:
1. Update specs (1 day)
2. Implement changes (2 days)
3. Update tests (1 day)
4. Update docs (0.5 days)

## Risks

**Technical Risks**:
- [Risk 1]: [mitigation]
- [Risk 2]: [mitigation]

**User Impact**:
- [Impact 1]: [mitigation]

## Alternatives Considered

1. **Alternative 1**: [description]
   - Pros: [list]
   - Cons: [list]
   - Why rejected: [reason]

2. **Alternative 2**: [description]
   - Pros: [list]
   - Cons: [list]
   - Why rejected: [reason]

## Approval

- [ ] Constitution compliant
- [ ] Impact assessed
- [ ] Migration path defined
- [ ] Tests planned
- [ ] Documentation planned

**Approved by**: [Name/Date]
**Status**: Draft | Approved | Rejected
```

### 4. Generate specs/spec-delta.md

**Content**:
```markdown
# Toolkit Spec Delta: [proposal-id]

**Base Version**: v[X.Y.Z]
**Target Version**: v[X.Y+1.Z]

## Entity Changes

### [Entity Name]

**ADD** field `[field_name]`:
```yaml
- name: [field_name]
  type: [type]
  required: [true/false]
  description: [description]
  example: [example]
```

**MODIFY** field `[field_name]`:
- Before: `type: string`
- After: `type: string | object`
- Rationale: [why]

**REMOVE** field `[field_name]`:
- Deprecated in: v[X.Y.Z]
- Removed in: v[X.Y+1.Z]
- Migration: [how to migrate]

## Validation Changes

**ADD** rule:
- Rule: [description]
- Layer: Structural | Semantic | Domain
- Error message: [format]

**MODIFY** rule:
- Before: [old rule]
- After: [new rule]
- Rationale: [why]

## CLI Changes

**ADD** command `[name]`:
- Purpose: [description]
- Usage: `toolkit [command] [args]`
- Options: [list]

## Workflow Changes

**ADD** workflow step:
- Step: [description]
- Input: [what]
- Output: [what]
```

### 5. Generate tasks.md

**Content**: Similar to regular tasks.md, but only for this change

```markdown
# Implementation Tasks: [proposal-id]

## Phase 1: Update Specifications
- [ ] T001 Update spec.md with delta
- [ ] T002 Update architecture.md if needed
- [ ] T003 Update constitution if needed

## Phase 2: Implement Changes
- [ ] T004 [MODELS] Add/modify entity fields
- [ ] T005 [VALIDATOR] Add/modify validation rules
- [ ] T006 [CLI] Add/modify commands

## Phase 3: Update Tests
- [ ] T007 [TESTS] Add tests for new fields
- [ ] T008 [TESTS] Update existing tests

## Phase 4: Update Documentation
- [ ] T009 Update README.md
- [ ] T010 Update CHANGELOG.md
- [ ] T011 Update examples
```

### 6. Generate impact.md

**Content**:
```markdown
# Impact Analysis: [proposal-id]

## Breaking Changes

**Summary**: [Yes/No - description]

**Affected APIs**:
- Entity field `[name]`: [how broken]
- Validation rule `[name]`: [how broken]
- CLI command `[name]`: [how broken]

## Migration Guide

**For users**:
```yaml
# Before
name: test
endpoint: /api/users
method: GET

# After
name: test
endpoint: /api/users
method: GET
assertions:  # NEW field
  - status: 200
```

**Code changes required**: Yes | No
- [Description if yes]

## Version Bump Rationale

**Proposed**: v[X.Y.Z] → v[X.Y+1.Z]

**Reasoning**:
- Breaking change: No → MINOR
- New feature: Yes → MINOR
- Bug fix: No → (would be PATCH)

## Compatibility

**Backward Compatible**: Yes | No

**Forward Compatible**: Yes | No

**Deprecation Timeline**:
- v[X.Y.Z]: Deprecate [feature]
- v[X.Y+1.Z]: Remove [feature]
```

### 7. Report

```
✅ Change proposal created

📋 Proposal: [proposal-id]
- Title: [title]
- Type: [type]
- Breaking: [yes/no]
- Version bump: [MAJOR|MINOR|PATCH]

📁 Files created:
- changes/[proposal-id]/proposal.md
- changes/[proposal-id]/tasks.md
- changes/[proposal-id]/impact.md
- changes/[proposal-id]/specs/spec-delta.md

🔄 Next steps:
1. Review proposal in changes/[proposal-id]/
2. Get approval from stakeholders
3. Run /metaspec:apply "[proposal-id]" to implement
4. Run /metaspec:archive "[proposal-id]" when complete

💡 To cancel: Delete changes/[proposal-id]/ directory
```

## Important Notes

1. **For brownfield only**
   - Toolkit must already exist
   - Use for incremental improvements
   - Not for initial development

2. **Semantic versioning**
   - Breaking change → MAJOR bump
   - New feature → MINOR bump
   - Bug fix → PATCH bump

3. **Impact analysis is critical**
   - Identify all breaking changes
   - Provide migration guides
   - Consider user impact

4. **Constitution compliance**
   - Changes must align with principles
   - Document any deviations
   - Get approval for violations

---

## ⚠️ When to Use Evolution vs Direct Edit

**Use Evolution (/metaspec.proposal) when**:
- ✅ Toolkit is released/published (v1.x.x) - ANY change requires Evolution
- ✅ Breaking changes (add required field, change field type, remove field)
- ✅ Major features (add new entity, new validation layer, new CLI command)
- ✅ Need impact analysis and version control

**Direct edit spec.md when**:
- ✅ Toolkit is draft (v0.x.x)
- ✅ Minor, non-breaking changes (fix typos, add examples, improve descriptions)
- ✅ Fast iteration during development
- ✅ Then validate with `/metaspec.sds.checklist` (update mode)

**Decision rule**:
```
Is toolkit released (v1.x.x)?
  YES → Always use Evolution
  NO  → Is it breaking or major feature?
    YES → Use Evolution
    NO  → Direct edit + checklist
```

See `docs/evolution-guide.md` for complete decision guide.

## Example

**User**: `/metaspec:proposal "Add GraphQL support to API Test Kit"`

**Output**:
```
✅ Change proposal created: 2025-10-28-add-graphql-support

📋 Proposal Summary:
- Add GraphQL query testing
- New entity fields: query, variables
- New validation: GraphQL syntax
- Breaking: No
- Version: v0.2.0 (MINOR bump)

📁 Review proposal:
- changes/2025-10-28-add-graphql-support/proposal.md

🔄 Next: Review and approve, then run /metaspec:apply
```

