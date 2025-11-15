---
description: Generate quality checklist for specification - validates specification quality, NOT implementation correctness
---

## Checklist Purpose: "Unit Tests for Domain Specifications"

**CRITICAL CONCEPT**: Checklists are **UNIT TESTS FOR SPECIFICATION WRITING** - they validate the quality, clarity, and completeness of specifications.

**NOT for implementation verification**:
- ❌ "Verify parser handles specification correctly"
- ❌ "Test validator catches specification violations"
- ❌ "Confirm toolkit implements specification"

**FOR specification quality validation**:
- ✅ "Are all specification entities clearly defined? [Completeness]"
- ✅ "Are operation schemas consistently specified? [Consistency]"
- ✅ "Are error codes documented with examples? [Completeness]"
- ✅ "Can 'must be valid' be objectively measured? [Clarity]"

---

## ⚠️ CRITICAL: This Command Does NOT Modify spec.md

**Checklist is a VALIDATION tool, NOT a modification tool.**

**What this command does**:
- ✅ Read `specs/domain/XXX-name/spec.md`
- ✅ Generate/update `checklists/comprehensive-quality.md`
- ✅ Identify issues (✅ Pass / ⚠️ Partial / ❌ Missing)
- ✅ Track improvement across iterations

**What this command does NOT do**:
- ❌ Modify `spec.md`
- ❌ Fix issues automatically
- ❌ Add missing fields or descriptions

**When issues are found, user should**:
- **Draft toolkit** (v0.x.x): Direct edit `spec.md` → Re-run checklist (update mode)
- **Released toolkit** (v1.x.x): Use `/metaspec.proposal` → `/metaspec.apply`

See `docs/evolution-guide.md` for decision guide.

## User Input

```text
$ARGUMENTS
```

You **MUST** consider the user input before proceeding (if not empty).

## Execution Flow

### 1. Check for existing checklist

**CRITICAL**: Before generating, check if checklist already exists:

```bash
ls specs/domain/XXX-name/checklists/
```

**If checklist exists**, ask user:

| Mode | Action | When to Use |
|------|--------|-------------|
| **update** | Update scores/status, add iteration section | Specification improved, want to track progress |
| **new** | Create new checklist (backup existing) | Complete restart, different focus |
| **append** | Add new checklist for different focus | Existing checklist still valid, new aspect |

**Default**: If user says "re-run", "verify improvement" → choose **update** mode

**If NO checklist exists** → proceed to step 2

---

### 2. Clarify intent

Generate up to 3 contextual clarifying questions based on user input:

**Example questions**:
- "Should this checklist focus on entity definitions, operations, or both?"
- "Is this for specification review (pre-toolkit) or specification validation (post-toolkit)?"
- "Should we include constitution alignment checks?"

**Present options as table**:
| Option | Focus | Why It Matters |
|--------|-------|----------------|
| A | Entity Definitions | Validates entity schemas, fields, constraints |
| B | Operations | Validates request/response schemas, error handling |
| C | Validation Rules | Validates rule completeness, consistency |
| D | All Above | Comprehensive specification quality check |

**Defaults if no interaction**:
- Focus: Entity Definitions + Operations
- Audience: Specification designer (self-review)
- Depth: Standard

### 3. Load specification context

**Read from**:
- `specs/domain/XXX-name/spec.md` (REQUIRED)
- `/memory/constitution.md` (REQUIRED)
- `specs/domain/XXX-name/checklists/` (REQUIRED - check existing checklists)
- `specs/domain/XXX-name/examples/` (if exists)
- `specs/domain/XXX-name/README.md` (if exists)

**DO NOT load** (these are toolkit-specific):
- ❌ plan.md (toolkit architecture)
- ❌ tasks.md (implementation tasks)
- ❌ Any files in `specs/toolkit/`

### 4. Generate or update checklist

#### Mode A: **new** mode (default if no existing checklist)

**Create**:
- Directory: `specs/domain/XXX-name/checklists/` (if not exists)
- Filename: `[domain].md` (e.g., `entity-design.md`, `operations.md`, `validation-rules.md`)
- Format: Sequential IDs starting from CHK001

#### Mode B: **update** mode (if checklist exists)

**Actions**:
1. Read existing checklist structure
2. Preserve all existing:
   - Item IDs (CHK001, CHK002, ...)
   - Categories
   - Evidence sections
   - Previous iteration results
3. Update:
   - ✅ Pass / ⚠️ Partial / ❌ Missing status
   - Evidence with new findings
4. Add **new section** at end:
   ```markdown
   ## 📊 Iteration N: [Date]
   
   ### Changes Since Last Check
   - [List specification improvements]
   
   ### Updated Scores
   - [Show before/after comparison]
   
   ### New Issues Found
   - [New checklist items if needed]
   ```

#### Mode C: **append** mode (different focus)

**Actions**:
1. Create new checklist file with different filename
2. Reference existing checklist: "See also: [existing-checklist].md"
3. Focus on new aspect (e.g., existing = entities, new = operations)

**Checklist Categories** (for specification specs):

#### **Entity Definition Quality**
Test if specification entities are complete, clear, and consistent:
- Are all specification entities clearly defined with purpose? [Completeness]
- Are all entity fields defined with explicit types? [Completeness]
- Are required vs optional fields clearly specified? [Clarity]
- Are field descriptions specific and measurable? [Clarity]
- Are field constraints documented (enum, format, range)? [Completeness]
- Are example values provided for all entities? [Coverage]
- Are entity relationships documented? [Completeness]

#### **Operation Specification Quality**
Test if specification operations are completely specified:
- Are all specification operations listed with clear purposes? [Completeness]
- Are request schemas defined for all operations? [Completeness]
- Are response schemas defined for all operations? [Completeness]
- Are success response formats documented? [Completeness]
- Are error response formats documented? [Completeness]
- Are operation constraints specified (timeouts, retries)? [Completeness]
- Are operation examples provided (success and error)? [Coverage]

#### **Validation Rules Quality**
Test if specification validation rules are specified:
- Are structural validation rules defined? [Completeness]
- Are semantic validation rules specified? [Completeness]
- Are domain-specific validation rules documented? [Coverage]
- Is validation logic consistent across similar fields? [Consistency]
- Are validation error formats specified? [Completeness]
- Are validation error codes defined? [Completeness]

#### **Error Handling Quality**
Test if specification error handling is comprehensive:
- Are all error codes defined? [Completeness]
- Are error response formats consistent? [Consistency]
- Are error messages descriptive and actionable? [Clarity]
- Are error scenarios documented for each operation? [Coverage]
- Are recovery strategies specified? [Completeness]

#### **Specification Examples Quality**
Test if specification examples are adequate:
- Are examples provided for all entities? [Coverage]
- Are examples provided for all operations? [Coverage]
- Do examples demonstrate typical use cases? [Coverage]
- Do examples cover error scenarios? [Coverage]
- Are examples valid against specification schemas? [Consistency]

#### **Schema Consistency**
Test if specification schemas are consistent:
- Is field naming consistent across entities (camelCase vs snake_case)? [Consistency]
- Are type definitions consistent across entities? [Consistency]
- Are required field patterns consistent? [Consistency]
- Are validation rules consistent across similar fields? [Consistency]

#### **Constitution Alignment**
Test if specification follows constitution principles:
- Does entity design follow Entity-First principle (3-5 core fields)? [Consistency, Constitution §I]
- Are field names self-explanatory? [Clarity, Constitution]
- Is specification minimal and extensible? [Completeness, Constitution]
- Are specifications AI-friendly (clear descriptions)? [Clarity, Constitution]
- Are domain standards followed? [Consistency, Constitution]

#### **Ambiguities & Gaps**
Test for specification issues:
- Are vague terms quantified ("valid", "appropriate")? [Ambiguity]
- Are conflicting requirements identified? [Conflict]
- Are missing definitions noted? [Gap]
- Are unresolved questions marked (TODO, TBD)? [Ambiguity]

#### **Workflow Design Quality** ⭐ NEW (v0.7.0+)
Test if specification defines complete user workflows:
- Does specification include "Workflow Specification" section? [Completeness, Constitution §II.7]
- Are at least 2 distinct workflow phases defined? [Completeness]
- Is each workflow phase mapped to specific operations? [Completeness]
- Are entry and exit criteria specified for each phase? [Clarity]
- Are phase transitions and dependencies documented? [Completeness]
- Are decision points and branching logic explained? [Clarity]
- Is an end-to-end workflow example provided? [Coverage]
- Are all operations referenced in at least one workflow phase? [Consistency]
- Is workflow purpose clearly stated (why this sequence)? [Clarity]
- Do workflow examples demonstrate typical user journeys? [Coverage]

**Purpose**: Ensures specifications define integrated workflows, not just isolated operations.

**Rationale**: Operations without workflow guidance are hard to use. Users need clear paths from start to finish. This aligns with MetaSpec's own workflow design (SDS/SDD).

### 5. Checklist Item Structure

**Pattern**:
```
- [ ] CHK### - [Question about specification quality]? [Quality Dimension, Traceability]
```

**Quality Dimensions**:
- [Completeness] - Are all specification elements defined?
- [Clarity] - Are specification elements specific and unambiguous?
- [Consistency] - Do specification elements align?
- [Measurability] - Can specification rules be verified?
- [Coverage] - Are all scenarios addressed?
- [Gap] - Is something missing?
- [Ambiguity] - Is something unclear?
- [Conflict] - Do elements contradict?

**Traceability Markers**:
- [Spec §Section] - References spec.md section
- [Constitution §Principle] - References constitution principle
- [Gap] - Missing specification element
- [Ambiguity] - Unclear specification element
- [Conflict] - Conflicting specification elements

### 6. Example Checklist Items

**Item Pattern**: Use question format testing requirement quality:
```
- [ ] CHK### - Are [aspect] defined/specified/documented for [scenario]? [Quality Dimension, Spec §Reference]
```

**Quality Dimensions**: Completeness, Clarity, Consistency, Coverage, Measurability, Traceability

---

#### Entity Definitions (5 core items)

```markdown
- [ ] CHK001 - Are all entity fields defined with explicit types (string, number, boolean, array, object)? [Completeness, Spec §Entities]
- [ ] CHK002 - Is the distinction between required and optional fields clearly specified? [Clarity, Spec §Entities]
- [ ] CHK003 - Are field constraints documented (enum values, format, ranges)? [Completeness, Spec §Entities]
- [ ] CHK004 - Are example values provided for entity fields? [Coverage, Spec §Entities]
- [ ] CHK005 - Does entity design follow Entity-First principle (3-5 core fields)? [Consistency, Constitution §I]
```

#### Operations (5 core items)

```markdown
- [ ] CHK006 - Are all operations listed with clear purpose statements? [Completeness, Spec §Operations]
- [ ] CHK007 - Are request and response schemas defined for operations? [Completeness, Spec §Operations]
- [ ] CHK008 - Are success and error response formats documented with examples? [Completeness, Spec §Operations]
- [ ] CHK009 - Are operation examples provided for typical use cases? [Coverage, Spec §Examples]
- [ ] CHK010 - Is operation naming convention consistent? [Consistency, Spec §Operations]
```

#### Validation Rules (4 core items)

```markdown
- [ ] CHK011 - Are structural validation rules (type, required) explicitly defined? [Completeness, Spec §Validation]
- [ ] CHK012 - Are semantic validation rules (cross-field, logic) specified? [Completeness, Spec §Validation]
- [ ] CHK013 - Are validation rules testable and objective? [Measurability, Spec §Validation]
- [ ] CHK014 - Are validation edge cases (empty, null, invalid) specified? [Coverage, Gap]
```

#### Error Handling (4 core items)

```markdown
- [ ] CHK015 - Are all error codes defined with clear meanings? [Completeness, Spec §Error Codes]
- [ ] CHK016 - Are error response formats consistent across operations? [Consistency, Spec §Error Handling]
- [ ] CHK017 - Are error messages descriptive and actionable? [Clarity, Spec §Error Messages]
- [ ] CHK018 - Are error examples provided for each error code? [Coverage, Spec §Examples]
```

#### Examples (4 core items)

```markdown
- [ ] CHK019 - Are examples provided for all specification entities? [Coverage, Spec §Examples]
- [ ] CHK020 - Are examples provided for all specification operations? [Coverage, Spec §Examples]
- [ ] CHK021 - Do examples cover both success and error scenarios? [Coverage, Spec §Examples]
- [ ] CHK022 - Are examples valid against specification schemas? [Consistency, Spec §Examples]
```

#### Constitution Alignment (4 core items)

```markdown
- [ ] CHK023 - Does specification follow Entity-First principle (minimal fields)? [Consistency, Constitution §I]
- [ ] CHK024 - Is specification minimal (only essential operations)? [Consistency, Constitution]
- [ ] CHK025 - Are specifications AI-friendly (clear descriptions, examples)? [Clarity, Constitution]
- [ ] CHK026 - Are domain standards followed (RFCs, conventions)? [Consistency, Constitution]
```

#### Workflow Design (10 core items) ⭐ NEW (v0.7.0+)

```markdown
- [ ] CHK027 - Does specification include a "Workflow Specification" section? [Completeness, Constitution §II.7]
- [ ] CHK028 - Are at least 2 distinct workflow phases defined? [Completeness, Spec §Workflow]
- [ ] CHK029 - Is each workflow phase mapped to specific operations? [Completeness, Spec §Workflow]
- [ ] CHK030 - Are entry criteria specified for each workflow phase? [Clarity, Spec §Workflow]
- [ ] CHK031 - Are exit criteria specified for each workflow phase? [Clarity, Spec §Workflow]
- [ ] CHK032 - Are phase transitions and dependencies documented? [Completeness, Spec §Workflow]
- [ ] CHK033 - Are decision points and branching logic explained? [Clarity, Spec §Workflow]
- [ ] CHK034 - Is an end-to-end workflow example provided? [Coverage, Spec §Workflow]
- [ ] CHK035 - Are all operations referenced in at least one workflow phase? [Consistency, Spec §Workflow]
- [ ] CHK036 - Do workflow examples demonstrate typical user journeys? [Coverage, Spec §Examples]
```

**Purpose**: Validates workflow completeness per Constitution Part II Principle 7.

**Why it matters**: Operations without workflow context are hard to use. Users need guidance on sequencing and relationships.

### 7. Anti-Examples: What NOT To Do

**❌ WRONG - Testing implementation**:
```markdown
- [ ] CHK001 - Verify toolkit parser handles specification correctly
- [ ] CHK002 - Test toolkit validator catches specification violations
- [ ] CHK003 - Confirm toolkit CLI works with specification
```

**✅ CORRECT - Testing specification quality**:
```markdown
- [ ] CHK001 - Are specification parsing requirements specified? [Completeness, Spec §Parser Requirements]
- [ ] CHK002 - Are specification validation rules documented? [Completeness, Spec §Validation Rules]
- [ ] CHK003 - Are specification CLI interactions defined? [Completeness, Spec §Specification Interface]
```

### 8. Write checklist file

- Write to `specs/domain/XXX-name/checklists/[domain].md`
- Use checklist-template structure
- Include metadata (purpose, created date, spec reference)
- Group items by category
- Number sequentially (CHK001, CHK002, ...)

### 9. Report completion

#### For **new** mode:

```
✅ Checklist generated: entity-design.md

📋 Summary:
- Focus: Entity Definition Quality
- Items: 10
- Categories: 3
- Traceability: 100% (all items reference spec/constitution)

📁 Location: specs/domain/XXX-name/checklists/entity-design.md

🎯 Purpose:
This checklist validates the quality of specification entity definitions in spec.md.
It does NOT test if toolkit implements specification, but whether the specification is:
- Complete (all entities defined)
- Clear (types, constraints explicit)
- Consistent (follows constitution)
- Measurable (examples provided)

🔄 Next steps:
1. Review checklist items
2. Update spec.md to address gaps
3. Re-run /metaspec.sds.clarify if ambiguities found
4. Use /metaspec.sds.analyze for deeper review

💡 Usage:
- During specification review: Check items before toolkit development
- After specification draft: Verify specification completeness
```

#### For **update** mode:

```
✅ Checklist updated: entity-design.md

📊 Iteration N Summary:
- Items updated: 8/10
- Improved: 5 items (❌ → ⚠️ or ✅)
- New issues: 2 items
- Still failing: 1 item

📈 Progress:
- Previous score: 60% (6/10 passing)
- Current score: 80% (8/10 passing)
- Improvement: +20%

📁 Location: specs/domain/XXX-name/checklists/entity-design.md

🎯 Key improvements detected:
- CHK001: ❌ → ✅ (entities now have purpose statements)
- CHK003: ⚠️ → ✅ (all fields now typed)
- CHK005: ❌ → ⚠️ (partial validation rules added)

⚠️ Still needs work:
- CHK007: Examples still missing for 2/5 entities

🔄 Next steps:
1. Review updated scores
2. Address remaining ❌ and ⚠️ items
3. Re-run checklist after next iteration
- Before release: Ensure specification is production-ready
```

## Important Notes

1. **Test the specification spec, not the implementation**
   - Ask: "Is X specified in specification?" not "Does toolkit implement X?"
   - Focus on specification quality, not toolkit correctness
   - Check completeness, clarity, consistency

2. **Traceability is mandatory**
   - Every item should reference [Spec §X], [Gap], [Constitution §Y]
   - Minimum 80% items with traceability markers
   - Makes it easy to find and fix specification issues

3. **Categories by quality dimension**
   - Group by: Completeness, Clarity, Consistency, Coverage
   - Not by: Implementation area (parser, validator, CLI)
   - Helps identify systematic specification quality issues

4. **Focus on specification-specific concerns**
   - Entity definition simplicity
   - Operation specification completeness
   - Validation rule clarity
   - Error handling consistency
   - Constitution alignment

5. **Multiple checklists allowed**
   - `entity-design.md` - Entity definition quality
   - `operations.md` - Operation specification quality
   - `validation.md` - Validation rules quality
   - `error-handling.md` - Error handling completeness
   - `constitution.md` - Constitution alignment
   - `examples.md` - Examples coverage

## Common Checklist Types

| Checklist | Focus | When to Use |
|-----------|-------|-------------|
| `entity-design.md` | Entity definitions | After /metaspec.sds.specify, before toolkit development |
| `operations.md` | Operation specifications | After /metaspec.sds.specify, before toolkit development |
| `validation.md` | Validation rules | After /metaspec.sds.clarify, before toolkit development |
| `error-handling.md` | Error handling | After /metaspec.sds.specify, before toolkit development |
| `constitution.md` | Constitution alignment | After /metaspec.sds.analyze, before toolkit development |
| `examples.md` | Examples coverage | After /metaspec.sds.specify, before release |


