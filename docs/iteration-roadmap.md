# Command Iteration Requirements Analysis

> **Goal**: Determine which commands need iteration support (update/new/append modes)

---

## 🎯 Decision Criteria

A command needs iteration support if:
1. ✅ **Generates output files** (not just modifies existing)
2. ✅ **Output is validation/analysis** (not creation)
3. ✅ **User will re-run to verify improvements**
4. ✅ **History comparison adds value**

A command does NOT need iteration if:
1. ❌ **Creates initial spec** (one-time creation)
2. ❌ **Modifies existing files directly** (use Evolution)
3. ❌ **Executes tasks** (action-oriented, not output-oriented)

---

## 📋 SDS Commands Analysis (5 total)

### ✅ 1. `/metaspec.sds.checklist` - Quality Checklist

**Status**: ✅ **Already Implemented** (v0.1.3+)

**Why needs iteration**:
- ✅ Generates `checklists/comprehensive-quality.md`
- ✅ User re-runs to verify protocol improvements
- ✅ Tracking: Iteration 1 vs Iteration 2 very valuable

**Modes**:
- `update`: Update scores, add Iteration N section
- `new`: Create new checklist (backup existing)
- `append`: Add new checklist for different focus

---

### ✅ 2. `/metaspec.sds.analyze` - Consistency Analysis

**Status**: ⚠️ **Needs Iteration Support**

**Current behavior**:
- Generates `analysis/consistency-report.md`
- Each run overwrites previous analysis

**Why needs iteration**:
- ✅ User improves protocol based on analysis
- ✅ Re-runs to verify issues are fixed
- ✅ Before/after comparison valuable
- ✅ Track: "Issue X: ❌ → ✅ (fixed in Iteration 2)"

**Recommended modes**:
- `update` (default): Update analysis, compare with previous iteration
- `new`: Generate fresh analysis
- `append`: Add supplementary analysis (e.g., focus on specific aspect)

**Example output**:
```markdown
# Protocol Consistency Analysis

## Iteration 1: 2025-11-03
- ❌ ISSUE-001: Field naming inconsistent (camelCase vs snake_case)
- ⚠️ ISSUE-002: Missing validation rules for 3/5 entities

## Iteration 2: 2025-11-05
- ✅ ISSUE-001: Fixed - All fields now use camelCase
- ⚠️ ISSUE-002: Partial - Validation rules added for 2/3 entities

### Progress
- Issues resolved: 1/2
- Issues improved: 1/2
- New issues: 0
```

---

### ✅ 3. `/metaspec.sds.clarify` - Resolve Ambiguities

**Status**: ⚠️ **Needs Iteration Support**

**Current behavior**:
- Identifies ambiguities in protocol spec
- Provides clarification suggestions
- No tracking of what was clarified

**Why needs iteration**:
- ✅ User clarifies some ambiguities
- ✅ Re-runs to find remaining issues
- ✅ Track: "Ambiguity X: Resolved in Iteration 2"
- ✅ Prevent re-reporting already clarified items

**Recommended modes**:
- `update` (default): Check for new ambiguities, mark resolved ones
- `new`: Fresh scan (ignore history)
- `append`: Focus on specific section

**Example output**:
```markdown
# Protocol Clarification Report

## Iteration 1: 2025-11-03
- ❌ AMB-001: "must be valid" - What does "valid" mean?
- ❌ AMB-002: "appropriate timeout" - What is appropriate?
- ❌ AMB-003: "error handling" - Which errors?

## Iteration 2: 2025-11-05
- ✅ AMB-001: RESOLVED - Added explicit validation criteria
- ✅ AMB-002: RESOLVED - Specified timeout range (100-5000ms)
- ❌ AMB-003: UNRESOLVED - Still needs clarification

### Progress
- Ambiguities resolved: 2/3
- Remaining: 1
```

---

### ❌ 4. `/metaspec.sds.specify` - Define Protocol Spec

**Status**: ❌ **Does NOT Need Iteration**

**Why NOT**:
- ❌ This is a **creation** command (generates initial spec.md)
- ❌ After creation, users **directly edit** spec.md
- ❌ For major changes, use **Evolution** (/metaspec.proposal)

**Workflow**:
```bash
$ /metaspec.sds.specify "Define MCP protocol"
  → Creates specs/protocol/001-mcp-protocol/spec.md
$ vim spec.md  # User edits directly
$ /metaspec.sds.checklist  # Validate (with iteration)
```

---

### ⚠️ 5. `/metaspec.sds.constitution` - Define Protocol Principles

**Status**: ⚠️ **Probably Does NOT Need Iteration**

**Why NOT**:
- ⚠️ Constitution is **long-term stable** (rarely changes)
- ⚠️ Changes should use **Evolution** (formal process)
- ⚠️ Not validation-oriented (creation-oriented)

**Exception**: If used to **audit constitution compliance**, then YES needs iteration.

**Decision**: **NOT needed** for now (creation-oriented)

---

## 📋 SDD Commands Analysis (8 total)

### ✅ 6. `/metaspec.sdd.checklist` - Quality Checklist (Toolkit)

**Status**: ⚠️ **Needs Iteration Support** (Same as SDS)

**Why needs iteration**:
- Same reasons as `/metaspec.sds.checklist`
- Validates toolkit specification quality
- User iterates to improve toolkit spec

**Recommended modes**: Same as SDS checklist

---

### ✅ 7. `/metaspec.sdd.analyze` - Consistency Analysis (Toolkit)

**Status**: ⚠️ **Needs Iteration Support** (Same as SDS)

**Why needs iteration**:
- Same reasons as `/metaspec.sds.analyze`
- Checks toolkit spec consistency
- Tracks improvements over iterations

**Recommended modes**: Same as SDS analyze

---

### ✅ 8. `/metaspec.sdd.clarify` - Resolve Ambiguities (Toolkit)

**Status**: ⚠️ **Needs Iteration Support** (Same as SDS)

**Why needs iteration**:
- Same reasons as `/metaspec.sds.clarify`
- Identifies toolkit spec ambiguities
- Tracks clarification progress

**Recommended modes**: Same as SDS clarify

---

### ⚠️ 9. `/metaspec.sdd.plan` - Plan Toolkit Architecture

**Status**: ⚠️ **Maybe Needs Iteration**

**Current behavior**:
- Generates `plan.md` with architecture design
- Tech stack, file structure, component interfaces

**Why MIGHT need iteration**:
- ⚠️ User might refine architecture
- ⚠️ Track: "Plan v1 vs Plan v2"
- ⚠️ Compare different architectural approaches

**Why MIGHT NOT**:
- ⚠️ Major plan changes should use **Evolution**
- ⚠️ Plan is more "creation" than "validation"

**Decision**: **Low priority** - Nice to have, but not critical

**If implemented**:
- `update`: Refine existing plan
- `new`: Create alternative plan
- `append`: Add detailed section (e.g., security considerations)

---

### ⚠️ 10. `/metaspec.sdd.tasks` - Break Down Implementation

**Status**: ⚠️ **Maybe Needs Iteration**

**Current behavior**:
- Generates `tasks.md` with implementation breakdown
- Task dependencies, priorities, estimates

**Why MIGHT need iteration**:
- ⚠️ User adjusts task breakdown as work progresses
- ⚠️ Track: "Original estimate vs actual"

**Why MIGHT NOT**:
- ⚠️ Tasks are **executed and marked complete** (not re-generated)
- ⚠️ Task changes handled by Evolution

**Decision**: **Low priority** - Tasks are execution-oriented, not validation-oriented

---

### ❌ 11. `/metaspec.sdd.specify` - Define Toolkit Spec

**Status**: ❌ **Does NOT Need Iteration** (Same as SDS)

**Why NOT**: Same reasons as `/metaspec.sds.specify`

---

### ❌ 12. `/metaspec.sdd.implement` - Build Toolkit Code

**Status**: ❌ **Does NOT Need Iteration**

**Why NOT**:
- ❌ This is an **execution** command (writes code files)
- ❌ Not validation-oriented
- ❌ Code changes use Git (not iteration tracking)

---

### ❌ 13. `/metaspec.sdd.constitution` - Define Toolkit Principles

**Status**: ❌ **Does NOT Need Iteration** (Same as SDS)

**Why NOT**: Same reasons as `/metaspec.sds.constitution`

---

## 📊 Summary Table

| Command | Iteration Support | Priority | Reason |
|---------|------------------|----------|--------|
| **SDS Commands** |
| `sds.checklist` | ✅ Implemented | ✅ DONE | Quality validation |
| `sds.analyze` | ⚠️ Needs | 🔥 **HIGH** | Consistency tracking |
| `sds.clarify` | ⚠️ Needs | 🔥 **HIGH** | Ambiguity tracking |
| `sds.specify` | ❌ No | - | Creation command |
| `sds.constitution` | ❌ No | - | Stable, use Evolution |
| **SDD Commands** |
| `sdd.checklist` | ⚠️ Needs | 🔥 **HIGH** | Quality validation |
| `sdd.analyze` | ⚠️ Needs | 🔥 **HIGH** | Consistency tracking |
| `sdd.clarify` | ⚠️ Needs | 🔥 **HIGH** | Ambiguity tracking |
| `sdd.plan` | ⚠️ Maybe | 🟡 **MEDIUM** | Architecture refinement |
| `sdd.tasks` | ⚠️ Maybe | 🟡 **LOW** | Execution-oriented |
| `sdd.specify` | ❌ No | - | Creation command |
| `sdd.implement` | ❌ No | - | Execution command |
| `sdd.constitution` | ❌ No | - | Stable, use Evolution |

---

## 🎯 Recommendation

### Phase 1: High Priority (Immediate)

**Implement iteration support for**:
1. ✅ `/metaspec.sds.checklist` - **DONE** ✨
2. 🔥 `/metaspec.sds.analyze` - **TODO**
3. 🔥 `/metaspec.sds.clarify` - **TODO**
4. 🔥 `/metaspec.sdd.checklist` - **TODO**
5. 🔥 `/metaspec.sdd.analyze` - **TODO**
6. 🔥 `/metaspec.sdd.clarify` - **TODO**

**Rationale**: These are **validation/analysis** commands that users re-run frequently to verify improvements.

---

### Phase 2: Medium Priority (Optional)

**Consider iteration support for**:
7. 🟡 `/metaspec.sdd.plan` - **MAYBE**
8. 🟡 `/metaspec.sdd.tasks` - **MAYBE**

**Rationale**: These are more creation-oriented, but refinement tracking could be useful.

---

### Phase 3: Not Needed

**Do NOT implement for**:
- ❌ `specify` commands (creation-oriented)
- ❌ `implement` (execution-oriented)
- ❌ `constitution` (stable, use Evolution)

---

## 🔧 Implementation Pattern

For each command needing iteration support, follow this pattern:

### 1. Update Command Template

```markdown
### 1. Check for existing output (NEW!)

**CRITICAL**: Before generating, check if output already exists:

```bash
ls specs/protocol/XXX-name/[output-directory]/
```

**If exists**, ask user:

| Mode | Action | When to Use |
|------|--------|-------------|
| **update** | Update results, add iteration section | Protocol improved, want to track progress |
| **new** | Create new output (backup existing) | Complete restart, different focus |
| **append** | Add supplementary analysis | Existing output still valid, new aspect |

**Default**: If user says "re-run", "verify improvement" → choose **update** mode
```

### 2. Add Iteration Tracking Section

```markdown
## 📊 Iteration N: [Date]

### Changes Since Last Check
- [List protocol improvements]

### Updated Results
- [Show before/after comparison]

### New Issues Found
- [New items if needed]
```

### 3. Update Report Format

```markdown
#### For **update** mode:

```
✅ Analysis updated: consistency-report.md

📊 Iteration N Summary:
- Items updated: 8/10
- Improved: 5 issues (❌ → ⚠️ or ✅)
- New issues: 2
- Still failing: 1

📈 Progress:
- Previous: 60% (6/10 passing)
- Current: 80% (8/10 passing)
- Improvement: +20%
```

---

## 📋 Next Steps

1. ✅ `sds.checklist` - **DONE** (v0.1.3+)
2. 🔥 Implement for `analyze` and `clarify` (SDS + SDD)
3. 🟡 Consider for `plan` and `tasks`
4. 📚 Update documentation with iteration best practices

---

## 🎉 Impact

**After Phase 1 completion**:
- ✅ 6/16 commands have iteration support (38%)
- ✅ All validation/analysis commands covered
- ✅ Consistent user experience across similar commands
- ✅ Complete iteration awareness throughout MetaSpec

