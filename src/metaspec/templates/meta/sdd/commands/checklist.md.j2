---
description: Generate quality checklist for toolkit specification - validates requirement quality, NOT implementation correctness
---

## Checklist Purpose: "Unit Tests for Toolkit Specifications"

**CRITICAL CONCEPT**: Checklists are **UNIT TESTS FOR SPECIFICATION WRITING** - they validate the quality, clarity, and completeness of toolkit specifications.

**NOT for implementation verification**:
- ❌ "Verify parser handles YAML correctly"
- ❌ "Test validator catches errors"
- ❌ "Confirm CLI commands work"

**FOR specification quality validation**:
- ✅ "Are entity field types explicitly specified? [Clarity]"
- ✅ "Are validation rules consistently defined? [Consistency]"
- ✅ "Are error message formats specified? [Completeness]"
- ✅ "Can 'extensible validator' be objectively measured? [Measurability]"

## User Input

```text
$ARGUMENTS
```

You **MUST** consider the user input before proceeding (if not empty).

## Execution Flow

### 1. Check for existing checklist

**CRITICAL**: Before generating, check if checklist already exists:

```bash
ls specs/toolkit/XXX-name/checklists/
```

**If checklist exists**, ask user:

| Mode | Action | When to Use |
|------|--------|-------------|
| **update** | Update scores/status, add iteration section | Toolkit improved, want to track progress |
| **new** | Create new checklist (backup existing) | Complete restart, different focus |
| **append** | Add new checklist for different focus | Existing checklist still valid, new aspect |

**Default**: If user says "re-run", "verify improvement" → choose **update** mode

**If NO checklist exists** → proceed to step 2

---

### 2. Clarify intent

Generate up to 3 contextual clarifying questions based on user input:

**Example questions**:
- "Should this checklist focus on entity design, validation rules, or both?"
- "Is this for spec review (pre-planning) or implementation review (post-coding)?"
- "Should we include constitution alignment checks?"

**Present options as table**:
| Option | Focus | Why It Matters |
|--------|-------|----------------|
| A | Entity Design | Validates field definitions, types, examples |
| B | Validation Rules | Validates rule completeness, error messages |
| C | Workflow Design | Validates CLI commands, user flows |
| D | All Above | Comprehensive spec quality check |

**Defaults if no interaction**:
- Focus: Entity Design + Validation Rules
- Audience: Toolkit developer (self-review)
- Depth: Standard

### 3. Load toolkit context

**Read from**:
- `specs/toolkit/XXX-name/spec.md` (REQUIRED)
- `specs/toolkit/XXX-name/plan.md` (if exists)
- `/memory/constitution.md` (REQUIRED)
- `specs/toolkit/XXX-name/architecture.md` (if exists)

### 4. Generate checklist

**Create**:
- Directory: `specs/toolkit/XXX-name/checklists/` (if not exists)
- Filename: `[domain].md` (e.g., `entity-design.md`, `validation.md`, `workflow.md`)
- Format: Sequential IDs starting from CHK001

**Checklist Categories** (for toolkit specs):

#### **Entity Design Quality**
Test if entity definitions are complete, clear, and consistent:
- Are all entity fields defined with types? [Completeness]
- Are required vs optional fields clear? [Clarity]
- Are field descriptions specific and measurable? [Clarity]
- Are example values provided for all fields? [Coverage]
- Are field constraints documented (regex, enum, range)? [Completeness]

#### **Validation Rules Quality**
Test if validation requirements are specified:
- Are structural validation rules defined? [Completeness]
- Are semantic validation rules specified? [Completeness]
- Are domain-specific validation rules documented? [Coverage]
- Is validation logic consistent across similar fields? [Consistency]
- Are error message formats specified? [Completeness]

#### **Workflow Definition Quality**
Test if workflows are clear and complete:
- Are workflow steps clearly ordered? [Clarity]
- Are inputs/outputs specified for each step? [Completeness]
- Are CLI commands mapped to workflows? [Consistency]
- Are success indicators measurable? [Measurability]
- Are error scenarios documented? [Coverage]

#### **CLI Interface Quality**
Test if CLI design is specified:
- Are all commands listed with purposes? [Completeness]
- Are command options documented? [Completeness]
- Are examples provided for each command? [Coverage]
- Are exit codes specified? [Completeness]
- Is output format defined (text/JSON)? [Clarity]

#### **Constitution Alignment**
Test if spec follows constitution.md:
- Does entity design follow Entity-First principle? [Consistency]
- Does validator design support extensibility? [Completeness]
- Are error messages AI-friendly? [Clarity]
- Is MVP scope clear? [Completeness]
- Are domain constraints referenced? [Coverage]

#### **Acceptance Criteria Quality**
Test if quality criteria are measurable:
- Are performance targets quantified? [Measurability]
- Can "extensible" be objectively verified? [Clarity]
- Are success metrics specific (not vague)? [Measurability]
- Are quality gates defined? [Completeness]

#### **Edge Case Coverage**
Test if edge cases are addressed:
- Are empty spec scenarios defined? [Gap]
- Are invalid spec scenarios documented? [Coverage]
- Are parser error scenarios specified? [Completeness]
- Are validation edge cases documented? [Coverage]

#### **Dependencies & Assumptions**
Test if dependencies are clear:
- Are external dependencies documented? [Completeness]
- Are domain standards referenced (RFCs, specs)? [Traceability]
- Are assumptions explicitly stated? [Clarity]
- Are technology choices justified? [Traceability]

#### **Ambiguities & Conflicts**
Test for specification issues:
- Are vague terms quantified? [Ambiguity]
- Are conflicting requirements identified? [Conflict]
- Are missing definitions noted? [Gap]
- Are unresolved questions marked? [Ambiguity]

### 4. Checklist Item Structure

**Pattern**:
```
- [ ] CHK### - [Question about requirement quality]? [Quality Dimension, Traceability]
```

**Quality Dimensions**:
- [Completeness] - Are all requirements present?
- [Clarity] - Are requirements specific and unambiguous?
- [Consistency] - Do requirements align?
- [Measurability] - Can requirements be verified?
- [Coverage] - Are all scenarios addressed?
- [Gap] - Is something missing?
- [Ambiguity] - Is something unclear?
- [Conflict] - Do requirements contradict?

**Traceability Markers**:
- [Spec §Section] - References spec.md section
- [Plan §Section] - References plan.md section
- [Constitution §Principle] - References constitution principle
- [Gap] - Missing requirement
- [Ambiguity] - Unclear requirement
- [Conflict] - Conflicting requirements

### 5. Example Checklist Items

**Item Pattern**: Use question format testing specification quality:
```
- [ ] CHK### - Are [aspect] defined/specified/documented for [scenario]? [Quality Dimension, Spec §Reference]
```

**Quality Dimensions**: Completeness, Clarity, Consistency, Coverage, Measurability, Traceability

---

#### Entity Design (4 core items)

```markdown
- [ ] CHK001 - Are all entity fields defined with explicit types (string, number, boolean, array, object)? [Completeness, Spec §Entity Definitions]
- [ ] CHK002 - Are field descriptions specific enough to guide implementation? [Clarity, Spec §Entity Definitions]
- [ ] CHK003 - Are example values provided for every field? [Coverage, Spec §Entity Definitions]
- [ ] CHK004 - Does entity design follow Entity-First principle (3-5 core fields)? [Consistency, Constitution §I]
```

#### Validation Rules (4 core items)

```markdown
- [ ] CHK005 - Are structural and semantic validation rules explicitly defined? [Completeness, Spec §Validation]
- [ ] CHK006 - Are error messages AI-friendly (actionable, with fix suggestions)? [Consistency, Constitution §IV]
- [ ] CHK007 - Is custom validator registration mechanism defined? [Completeness, Constitution §II]
- [ ] CHK008 - Can validation rules be objectively tested? [Measurability, Spec §Validation]
```

#### Workflow (4 core items)

```markdown
- [ ] CHK009 - Are workflow steps clearly ordered with inputs and outputs specified? [Clarity, Spec §Workflow]
- [ ] CHK010 - Are CLI commands mapped to workflow steps? [Consistency, Spec §CLI Commands]
- [ ] CHK011 - Are success indicators measurable? [Measurability, Spec §Workflow]
- [ ] CHK012 - Is the init → validate → execute flow clearly defined? [Completeness, Spec §Workflow]
```

#### CLI Interface (4 core items)

```markdown
- [ ] CHK013 - Are all CLI commands listed with clear purposes and arguments? [Completeness, Spec §CLI]
- [ ] CHK014 - Are exit codes specified (0=success, 1=failure)? [Completeness, Spec §CLI]
- [ ] CHK015 - Are command examples provided? [Coverage, Spec §CLI]
- [ ] CHK016 - Is command naming consistent (init, validate, run)? [Consistency, Spec §CLI]
```

#### Constitution Alignment (4 core items)

```markdown
- [ ] CHK017 - Does entity design follow Entity-First principle (minimal fields)? [Consistency, Constitution §I]
- [ ] CHK018 - Does validator design support extensibility (custom validators)? [Consistency, Constitution §II]
- [ ] CHK019 - Are error messages AI-friendly (clear, actionable)? [Consistency, Constitution §IV]
- [ ] CHK020 - Is progressive enhancement path clear (MVP vs future features)? [Consistency, Constitution §V]
```

### 6. Anti-Examples: What NOT To Do

**❌ WRONG - Testing implementation**:
```markdown
- [ ] CHK001 - Verify parser loads YAML correctly
- [ ] CHK002 - Test validator catches missing required fields
- [ ] CHK003 - Confirm CLI init command creates file
```

**✅ CORRECT - Testing specification quality**:
```markdown
- [ ] CHK001 - Are parser error handling scenarios specified? [Completeness, Spec §Parser Design]
- [ ] CHK002 - Is validator behavior for missing fields documented? [Completeness, Spec §Validation Requirements]
- [ ] CHK003 - Is CLI init command output format specified? [Clarity, Spec §CLI Commands]
```

### 7. Write checklist file

- Write to `specs/toolkit/XXX-name/checklists/[domain].md`
- Use checklist-template structure
- Include metadata (purpose, created date, spec reference)
- Group items by category
- Number sequentially (CHK001, CHK002, ...)

### 8. Report completion

**For new checklist**:
```
✅ Checklist generated: entity-design.md

📋 Summary:
- Focus: Entity Design Quality
- Items: 10
- Categories: 3
- Traceability: 100% (all items reference spec/constitution)

📁 Location: specs/toolkit/XXX-name/checklists/entity-design.md

🎯 Purpose:
This checklist validates the quality of entity definitions in spec.md.
It does NOT test if the implementation works, but whether the specification is:
- Complete (all fields defined)
- Clear (types, constraints explicit)
- Consistent (follows constitution)
- Measurable (examples provided)

🔄 Next steps:
1. Review checklist items
2. Update spec.md to address gaps
3. Re-run /metaspec:clarify if ambiguities found
4. Use /metaspec:analyze for deeper review

💡 Usage:
- During spec review: Check items before /metaspec:plan
- After implementation: Verify spec matched reality
- Before release: Ensure spec is complete
```

**For update mode**:
```
✅ Checklist updated: comprehensive-quality.md

📊 Iteration 2 Summary:
- Items updated: 10/10
- Improved: 3 items (CHK001: ❌ → ✅, CHK003: ❌ → ⚠️, CHK005: ⚠️ → ✅)
- Still failing: 2 items (CHK002, CHK007)
- New items: 0

📈 Progress:
- Previous: 40% (4/10 passing)
- Current: 60% (6/10 passing)
- Improvement: +20%

🎯 Key improvements:
- ✅ CHK001: Entity field types now specified
- ✅ CHK005: Examples added for all entities
- ⚠️ CHK003: Partial validation rules (3/5 entities)

⚠️ Still needs work:
- ❌ CHK002: Field constraints missing (enum, regex)
- ❌ CHK007: Error messages lack specificity

🔄 Next steps:
1. Fix remaining failing items (2)
2. Complete partial validation rules (CHK003)
3. Run /metaspec.sdd.analyze to verify consistency
```

## Important Notes

1. **Test the spec, not the code**
   - Ask: "Is X specified?" not "Does X work?"
   - Focus on requirement quality, not implementation correctness
   - Check completeness, clarity, consistency

2. **Traceability is mandatory**
   - Every item should reference [Spec §X], [Gap], [Constitution §Y]
   - Minimum 80% items with traceability markers
   - Makes it easy to find and fix issues

3. **Categories by quality dimension**
   - Group by: Completeness, Clarity, Consistency, Coverage
   - Not by: Implementation area (parser, validator, CLI)
   - Helps identify systematic quality issues

4. **Focus on toolkit-specific concerns**
   - Entity design simplicity
   - Validation extensibility
   - Error message AI-friendliness
   - Constitution alignment
   - Domain specificity

5. **Multiple checklists allowed**
   - `entity-design.md` - Entity quality
   - `validation.md` - Validation rules quality
   - `workflow.md` - Workflow clarity
   - `cli.md` - CLI interface completeness
   - `constitution.md` - Constitution alignment

## Common Checklist Types

| Checklist | Focus | When to Use |
|-----------|-------|-------------|
| `entity-design.md` | Entity field definitions | After /metaspec:specify, before /metaspec:plan |
| `validation.md` | Validation rules quality | After /metaspec:clarify, before /metaspec:plan |
| `workflow.md` | Workflow clarity | After /metaspec:specify, before /metaspec:plan |
| `cli.md` | CLI interface completeness | After /metaspec:plan, before /metaspec:tasks |
| `constitution.md` | Constitution alignment | After /metaspec:plan, before /metaspec:implement |
| `architecture.md` | Architecture quality | After /metaspec:plan, before /metaspec:tasks |

