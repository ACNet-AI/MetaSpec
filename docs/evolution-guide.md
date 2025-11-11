# When to Use Evolution vs Direct Edit

> **Decision Guide**: When should you use `/metaspec.proposal` (Evolution) vs directly editing `spec.md`?

---

## 🎯 Quick Decision Tree

```
Need to change specification?
    ↓
    ├─ Is this a RELEASED/PUBLISHED toolkit?
    │   ├─ YES → Use /metaspec.proposal (Evolution)
    │   └─ NO → Is it a breaking change or major feature?
    │       ├─ YES → Use /metaspec.proposal (Evolution)
    │       └─ NO → Direct edit + /metaspec.sds.checklist
    │
    └─ Just validating quality? (no changes needed)
        └─ Use /metaspec.sds.checklist or /metaspec.sds.analyze
```

---

## 📊 Detailed Decision Matrix

| Scenario | Toolkit Status | Change Type | Method | Why |
|----------|----------------|-------------|--------|-----|
| 🟢 Fix typos, improve descriptions | Draft | Non-breaking | **Direct edit** | Low risk, fast iteration |
| 🟢 Add examples | Draft | Non-breaking | **Direct edit** | Enhances clarity, no spec change |
| 🟢 Add missing field descriptions | Draft | Non-breaking | **Direct edit** | Completing spec, not changing |
| 🟡 Add new optional field | Draft | Non-breaking | **Direct edit** (small) or **Evolution** (if complex) | Depends on complexity |
| 🟡 Add new required field | Draft | Breaking | **Evolution** (if near release) or **Direct edit** (if early draft) | Breaking needs tracking |
| 🔴 Add new entity | Draft or Released | Breaking | **Evolution** | Major change, needs review |
| 🔴 Modify existing field type | Draft or Released | Breaking | **Evolution** | Breaking change, needs impact analysis |
| 🔴 Any change to released toolkit | **Released** | Any | **Evolution** | Version control required |

---

## 🚦 Clear Rules

### Rule 1: Released/Published Toolkit

**If toolkit is released or published, ALWAYS use Evolution:**

```bash
# Toolkit is v1.0.0 and published to community
# User wants to add a new field

❌ WRONG: Direct edit specs/domain/XXX/spec.md
✅ RIGHT: /metaspec.proposal "Add new field"
```

**Why**: 
- Version control required
- Impact analysis needed
- Users may depend on current version
- CHANGELOG and migration guide necessary

---

### Rule 2: Draft Toolkit - Major Changes

**If change is breaking or adds major feature, use Evolution:**

```bash
# Toolkit is still in draft (v0.1.0)
# User wants to add a new entity or change field type

❌ WRONG: Direct edit (for breaking changes)
✅ RIGHT: /metaspec.proposal "Add new entity" or "Change field type"
```

**Why**:
- Breaking changes need impact analysis
- Major features need structured planning
- Evolution provides tasks breakdown
- Creates audit trail

**Breaking change examples**:
- Add new required field
- Change field type (string → object)
- Remove existing field
- Rename field
- Change validation rules that reject previously valid inputs

**Major feature examples**:
- Add new entity
- Add new validation layer
- Add new CLI command
- Add new workflow

---

### Rule 3: Draft Toolkit - Minor Improvements

**If change is minor and non-breaking, direct edit is OK:**

```bash
# Toolkit is in draft (v0.1.0)
# User wants to fix typos, add examples, improve descriptions

✅ RIGHT: Direct edit specs/domain/XXX/spec.md
✅ THEN: /metaspec.sds.checklist (update mode) to verify
```

**Why**:
- Fast iteration during development
- Low risk of breaking anything
- Overhead of Evolution not justified
- Still validated by checklist

**Minor improvement examples**:
- Fix typos in descriptions
- Add examples
- Improve field descriptions
- Add optional field (with default value)
- Clarify ambiguous wording
- Add comments or notes

---

## 🔄 Workflow Examples

### Workflow 1: Draft Toolkit - Iterative Refinement

```bash
1. User writes initial specification spec
   $ vim specs/domain/001-mcp-spec/spec.md

2. User validates quality
   $ /metaspec.sds.checklist
   → Result: ❌ CHK003 - Missing field types

3. User fixes directly (minor improvement)
   $ vim specs/domain/001-mcp-spec/spec.md
   # Add missing type definitions

4. User re-validates
   $ /metaspec.sds.checklist
   → AI detects existing checklist
   → Asks: update/new/append?
   → User chooses: update
   → Result: CHK003: ❌ → ✅ (Iteration 2 added)

5. Repeat until quality is satisfactory
```

**Key**: Direct edit + checklist for fast iteration in draft phase.

---

### Workflow 2: Draft Toolkit - Major Feature Addition

```bash
1. User has a working draft specification (v0.2.0)

2. User wants to add GraphQL support (major feature)
   $ /metaspec.proposal "Add GraphQL query support" --type sds

3. AI generates proposal with:
   - New entity fields
   - New validation rules
   - Impact analysis
   - Tasks breakdown

4. User reviews and approves in proposal.md

5. AI executes tasks
   $ /metaspec.apply 2025-11-05-add-graphql

6. Changes applied, version bumped to v0.3.0

7. User archives
   $ /metaspec.archive 2025-11-05-add-graphql
```

**Key**: Evolution for structured, trackable major changes.

---

### Workflow 3: Released Toolkit - Any Change

```bash
1. Toolkit is released (v1.0.0)

2. User discovers missing validation rule (minor, but needs tracking)
   $ /metaspec.proposal "Add email validation rule" --type sds

3. Even though it's minor, use Evolution because:
   - Toolkit is released
   - Users depend on current version
   - Need CHANGELOG entry
   - Need version bump (v1.0.0 → v1.0.1)

4. Execute and archive as normal
```

**Key**: Released toolkits ALWAYS use Evolution, even for minor changes.

---

## 🎯 Command Layer vs Evolution Layer

### Command Layer (Checklist, Analyze)

**Purpose**: Validate specification quality, **NOT modify specs**

**Commands**:
- `/metaspec.sds.checklist` - Generate/update quality checklist
- `/metaspec.sds.analyze` - Analyze consistency and completeness
- `/metaspec.sds.clarify` - Resolve ambiguities

**Output**:
- `checklists/comprehensive-quality.md` (validation results)
- `analysis/consistency-report.md` (analysis results)

**NEVER modifies**: `spec.md`

**When to use**:
- Validate spec quality
- Track improvement over iterations
- Identify issues before implementation

---

### Evolution Layer (Proposal, Apply, Archive)

**Purpose**: Modify specification with controlled process

**Commands**:
- `/metaspec.proposal` - Create change proposal
- `/metaspec.apply` - Execute approved changes
- `/metaspec.archive` - Archive completed changes

**Output**:
- `changes/[proposal-id]/proposal.md` (what to change)
- `changes/[proposal-id]/specs/spec-delta.md` (changes to apply)
- Eventually merges into `spec.md`

**Modifies**: `spec.md` (after approval)

**When to use**:
- Released toolkit (any change)
- Draft toolkit (major/breaking changes)
- Need impact analysis
- Need version control

---

## ⚠️ Anti-Patterns

### ❌ Anti-Pattern 1: Using Evolution for Minor Tweaks in Draft

```bash
# Toolkit is v0.1.0, user wants to fix a typo

❌ WRONG:
$ /metaspec.proposal "Fix typo in description" --type sds
# Overhead: proposal.md, tasks.md, impact.md, approval process

✅ RIGHT:
$ vim specs/domain/001-xxx/spec.md  # Fix typo
$ /metaspec.sds.checklist  # Validate
```

**Why wrong**: Overhead not justified for minor changes in draft phase.

---

### ❌ Anti-Pattern 2: Direct Edit for Released Toolkit

```bash
# Toolkit is v1.0.0 and published

❌ WRONG:
$ vim specs/domain/001-xxx/spec.md  # Add new field
$ git commit -m "Add new field"

✅ RIGHT:
$ /metaspec.proposal "Add new field" --type sds
# Generates impact analysis, version bump, CHANGELOG
```

**Why wrong**: Users depend on current version, need proper version control.

---

### ❌ Anti-Pattern 3: Using Checklist to Modify Specs

```bash
❌ WRONG:
$ /metaspec.sds.checklist
# User expects checklist to fix issues in spec.md

✅ RIGHT:
$ /metaspec.sds.checklist
# → Identifies issues
# → User fixes via direct edit (draft) or Evolution (released)
# → Re-run checklist to verify
```

**Why wrong**: Checklist is validation tool, not modification tool.

---

## 📋 Summary

### Direct Edit

**When**:
- ✅ Draft toolkit
- ✅ Minor, non-breaking changes
- ✅ Fast iteration needed

**Examples**:
- Fix typos
- Add examples
- Improve descriptions
- Add optional fields

---

### Evolution (/metaspec.proposal)

**When**:
- ✅ Released toolkit (any change)
- ✅ Breaking changes
- ✅ Major features
- ✅ Need audit trail

**Examples**:
- Add new entity
- Change field types
- Remove fields
- Add required fields
- Released toolkit updates

---

### Command Layer (Checklist, Analyze)

**When**:
- ✅ Validate quality
- ✅ Track improvement
- ✅ Identify issues
- ✅ NOT for making changes

**Examples**:
- Quality checks
- Consistency analysis
- Ambiguity detection
- Progress tracking

---

## 🔮 Future Enhancement

Consider adding a command to help decide:

```bash
$ /metaspec.recommend-workflow "I want to add a new field"

📋 Analysis:
- Toolkit status: Draft (v0.2.0)
- Change type: Add field
- Breaking: No (optional field)

✅ Recommendation: Direct edit + checklist
✅ Alternative: Evolution (if complex or near release)

🔄 Suggested workflow:
1. Edit specs/domain/001-xxx/spec.md
2. Run /metaspec.sds.checklist (update mode)
3. Verify: CHK###: ❌ → ✅
```

This could reduce confusion further.

