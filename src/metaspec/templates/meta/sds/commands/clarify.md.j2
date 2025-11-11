---
description: Identify underspecified areas in the toolkit specification by asking targeted clarification questions about entity design, validation rules, and workflows
---

## User Input

```text
$ARGUMENTS
```

You **MUST** consider the user input before proceeding (if not empty).

## Outline

**Goal**: Detect and reduce ambiguity or missing decisions in the toolkit specification, focusing on entity design, validation rules, workflows, and CLI interface.

**Important**: This command runs BEFORE `/metaspec:plan`. Clear specifications lead to better implementation architecture.

### Execution Flow

#### 1. Check for existing clarification

**CRITICAL**: Before generating, check if clarification report already exists:

```bash
ls specs/domain/XXX-name/clarifications/
```

**If clarification exists**, ask user:

| Mode | Action | When to Use |
|------|--------|-------------|
| **update** | Update status, mark resolved ambiguities | Specification clarified, want to track progress |
| **new** | Create new clarification (backup existing) | Complete restart, different focus |
| **append** | Add supplementary clarification | Existing report still valid, new aspect |

**Default**: If user says "re-run", "check again" → choose **update** mode

**If NO clarification exists** → proceed to step 2

---

#### 2. Load toolkit specification

- Read `specs/domain/XXX-name/spec.md`
- If missing, instruct user to run `/metaspec:specify` first
- Parse current entity definitions, workflows, validation rules

#### 3. Perform ambiguity scan

Scan the specification using this **speckit-specific taxonomy**. Mark each category: **Clear** / **Partial** / **Missing**.

##### **Entity Design Clarity**
- Are all entity fields clearly defined with types?
- Are required vs optional fields clear?
- Are field descriptions specific enough?
- Are example values provided?
- Are field constraints documented (e.g., regex patterns, enum values)?
- Is the rationale for each field explained?

##### **Validation Rules Completeness**
- Are structural validation rules defined?
- Are semantic validation rules specified?
- Are domain-specific validation rules documented?
- Are error messages formats specified?
- Are validation error fix suggestions included?
- Is validation performance target specified?

##### **Workflow Definitions**
- Are workflow steps clearly ordered?
- Are inputs/outputs specified for each step?
- Are CLI commands mapped to workflow steps?
- Are success indicators defined?
- Are error scenarios documented?
- Are example usages complete?

##### **CLI Interface Design**
- Are all commands listed with purposes?
- Are command options documented?
- Are examples provided for each command?
- Are exit codes specified?
- Is output format defined?
- Are interactive vs non-interactive modes clear?

##### **Domain Constraints**
- Are domain-specific rules documented?
- Are industry standards referenced (e.g., RFC numbers)?
- Are domain conventions explained?
- Are domain terminology definitions provided?
- Are domain-specific validation rules justified?

##### **Extensibility Points**
- Are custom validator hooks specified?
- Are plugin interfaces defined?
- Are extension points documented?
- Are extensibility examples provided?

##### **Error Handling**
- Are error message formats specified?
- Are error recovery suggestions included?
- Are edge cases documented?
- Are validation failure scenarios covered?

##### **Performance Requirements**
- Are validation performance targets specified?
- Are memory usage limits defined?
- Are scalability targets documented?

##### **AI-Agent Friendliness**
- Are examples provided for every concept?
- Are error messages actionable?
- Are naming conventions consistent?
- Is implicit behavior avoided?

##### **Constitution Alignment**
- Does entity design follow Entity-First principle?
- Does validation support extensibility?
- Is spec-first workflow clear?
- Are quality criteria measurable?

For each category with **Partial** or **Missing** status, add to clarification queue (unless low-impact).

#### 4. Generate prioritized clarification queue

**Constraints**:
- Maximum 5 questions total
- Each question must be answerable with:
  - Multiple choice (2-5 options), OR
  - Short answer (<=5 words)
- Only include high-impact questions that affect:
  - Entity structure
  - Validation logic
  - Workflow design
  - CLI interface
  - Constitution alignment

**Prioritization** (Impact × Uncertainty):
1. **Critical**: Entity field types, required fields, validation rules
2. **High**: Workflow steps, CLI commands, error messages
3. **Medium**: Performance targets, extensibility design
4. **Low**: Naming preferences, example choices

**Exclude**:
- Already-answered questions
- Implementation details (e.g., which Python library to use)
- Questions better suited for `/metaspec:plan`

#### 5. Interactive questioning loop

**Present ONE question at a time**:

**For multiple-choice questions**:

1. **Analyze all options** and determine the **most suitable** based on:
   - Entity-First principle (simple over complex)
   - Validator Extensibility (flexible over rigid)
   - AI-Agent Friendly (clear over clever)
   - Domain standards (conventional over novel)

2. **Present recommendation**:
   ```
   **Recommended:** Option [X] - [1-2 sentence reasoning]
   ```

3. **Show all options** as table:
   | Option | Description |
   |--------|-------------|
   | A | [Description] |
   | B | [Description] |
   | C | [Description] |

4. **Prompt user**:
   ```
   Reply with option letter (e.g., "A"), accept recommendation ("yes"/"recommended"), or provide short answer.
   ```

**For short-answer questions**:

1. **Provide suggestion**:
   ```
   **Suggested:** [your answer] - [brief reasoning]
   ```

2. **Format constraint**:
   ```
   Format: Short answer (<=5 words). Accept suggestion ("yes"/"suggested") or provide your own.
   ```

**After user answers**:
- If "yes"/"recommended"/"suggested" → use your recommendation
- Validate answer (matches option or <=5 words)
- If ambiguous, ask for clarification (doesn't count as new question)
- Record answer in memory
- Move to next question

**Stop when**:
- All critical ambiguities resolved, OR
- User signals done ("done", "good", "no more"), OR
- 5 questions asked

#### 6. Integrate answers incrementally

**After EACH accepted answer**:

1. **Update Clarifications section**:
   - Create `## Clarifications` if missing
   - Add `### Session YYYY-MM-DD` for today
   - Append: `- Q: [question] → A: [answer]`

2. **Update relevant sections**:

   | Answer Type | Update Location |
   |-------------|-----------------|
   | Entity field clarification | Update **Entity Definitions** table |
   | Validation rule | Update **Validation Requirements** |
   | Workflow step | Update **Workflow Definitions** |
   | CLI command detail | Update **CLI Commands** |
   | Domain constraint | Update **Domain-Specific Validation** |
   | Error message format | Update **Validation Requirements** |
   | Performance target | Update **Quality Criteria** |

3. **Replace ambiguous text**:
   - If answer invalidates earlier vague statement, replace it
   - Remove contradictory text
   - Keep only one source of truth

4. **Save immediately**:
   - Write updated spec to `specs/domain/XXX-name/spec.md`
   - Atomic overwrite
   - Preserve formatting

#### 7. Validation (after each update)

- [ ] Clarifications section has one bullet per answer
- [ ] Total questions ≤ 5
- [ ] No lingering vague placeholders
- [ ] No contradictory statements
- [ ] Valid Markdown structure
- [ ] Consistent terminology

#### 8. Report completion

**For new clarification**:
```
✅ Clarification complete

📊 Questions asked: [N] / 5

📝 Sections updated:
- Entity Definitions
- Validation Requirements
- [Other sections]

📋 Coverage Summary:

| Category | Status |
|----------|--------|
| Entity Design | ✅ Resolved |
| Validation Rules | ✅ Resolved |
| Workflow Definitions | ⏭️ Deferred |
| CLI Interface | ✅ Clear |
| Domain Constraints | ⚠️ Outstanding |
| ... | ... |

Status legend:
- ✅ Resolved: Was partial/missing, now addressed
- ⏭️ Deferred: Exceeds quota or better for /metaspec:plan
- ✅ Clear: Already sufficient
- ⚠️ Outstanding: Still partial/missing but low impact

🔄 Recommendation:
[Proceed to /metaspec:plan | Run /metaspec:clarify again | Address outstanding items]

📁 Updated: specs/domain/XXX-name/spec.md

💡 Next step: /metaspec:plan
```

**For update mode**:
```
✅ Clarification updated: ambiguity-report.md

📊 Iteration 2 Summary:
- Ambiguities checked: 10
- Resolved: 3 (AMB-001, AMB-002, AMB-003)
- Still outstanding: 2 (AMB-004, AMB-005)
- New ambiguities: 1 (AMB-006)

📈 Progress:
- Previous: 5 outstanding ambiguities
- Current: 3 outstanding ambiguities
- Improvement: -40% ambiguities

🎯 Key improvements:
- ✅ AMB-001: "must be valid" → JSON Schema Draft 7
- ✅ AMB-002: "appropriate timeout" → 100-5000ms
- ✅ AMB-003: "error handling" → E001-E010 error codes

⚠️ Still needs clarification:
- ❌ AMB-004: "capabilities" field lacks definition
- ❌ AMB-005: "permissions" scope unclear
- ❌ AMB-006: NEW - "metadata" format unspecified

🔄 Next steps:
1. Clarify remaining ambiguities (3)
2. Run /metaspec.sds.analyze to verify consistency
3. Consider /metaspec:plan once ambiguities < 2
```

### Special Cases

#### No ambiguities found

```
✅ No critical ambiguities detected

All specification categories are clear:
- ✅ Entity Design: Complete
- ✅ Validation Rules: Complete
- ✅ Workflows: Complete
- ✅ CLI Interface: Complete
- ✅ Domain Constraints: Complete

🔄 Recommendation: Proceed to /metaspec:plan
```

#### User stops early

If user says "stop"/"done"/"proceed" before 5 questions:
- Save current progress
- Report questions answered so far
- Show coverage summary
- Recommend next action

#### High-impact items deferred

If quota reached with critical items unresolved:
```
⚠️ Warning: Critical items remain unresolved

Deferred items (exceeded 5-question limit):
1. [Item 1]: [Why critical]
2. [Item 2]: [Why critical]

Options:
A. Continue to /metaspec:plan (accept higher implementation risk)
B. Run /metaspec:clarify again to address deferred items
C. Update spec.md manually then continue

**Recommended:** Option B - addressing these before planning will reduce rework
```

## Example Questions for Speckits

### Entity Design

**Q**: Should the [PRIMARY_ENTITY] entity support nested objects?

**Recommended**: Option B - Keep flat for MVP, add nesting in v0.2

| Option | Description |
|--------|-------------|
| A | Yes, support nested objects from start |
| B | No, keep flat structure for MVP |
| C | Support one level of nesting only |

**Q**: What field types are needed?

**Suggested**: string, number, boolean, array - <covers 90% of use cases, extensible later>

Format: Short answer (<=5 words)

### Validation Rules

**Q**: Should validation be strict or permissive by default?

**Recommended**: Option A - Strict by default (fail fast, clear errors)

| Option | Description |
|--------|-------------|
| A | Strict - fail on any unknown field |
| B | Permissive - warn on unknown fields |
| C | Configurable via --strict flag |

**Q**: What's the validation performance target?

**Suggested**: <100ms per spec - <industry standard for CLI tools>

Format: Short answer (<=5 words)

### Workflow Design

**Q**: Should `init` command create interactive wizard or static template?

**Recommended**: Option B - Static template (simpler, AI-friendly)

| Option | Description |
|--------|-------------|
| A | Interactive wizard with prompts |
| B | Static template user fills in |
| C | Both modes (--interactive flag) |

### CLI Interface

**Q**: What should `validate` command output on success?

**Recommended**: Option A - Concise success (good UX, clear feedback)

| Option | Description |
|--------|-------------|
| A | "✅ Validation passed: spec.yaml" |
| B | Detailed report with all checks |
| C | Silent (exit code 0 only) |

### Domain Constraints

**Q**: For API Test Kit - should we support GraphQL or REST only?

**Recommended**: Option B - REST only for MVP (focus, simpler)

| Option | Description |
|--------|-------------|
| A | REST and GraphQL from start |
| B | REST only, GraphQL in v0.3 |
| C | GraphQL only (modern focus) |

## Important Notes

1. **Focus on toolkit design, not implementation**
   - Ask about entity structure, not Python classes
   - Ask about validation rules, not Pydantic validators
   - Ask about workflows, not code architecture

2. **Respect constitution principles**
   - Entity-First: Prefer simpler entity designs
   - Validator Extensibility: Prefer flexible validation
   - AI-Agent Friendly: Prefer clear error messages
   - Progressive Enhancement: Prefer MVP-first approaches

3. **One question at a time**
   - Never show all questions at once
   - Never reveal future questions
   - Wait for user answer before proceeding

4. **Incremental updates**
   - Save spec after EACH answer
   - Don't batch updates
   - Minimize context loss risk

5. **Actionable questions only**
   - Every question must affect design decisions
   - Avoid trivial preferences
   - Avoid implementation details

## Context Priority

If user provides context in `$ARGUMENTS`, prioritize clarifications for:
- Mentioned entities
- Mentioned workflows
- Mentioned concerns (e.g., "worried about performance")
- Explicit unknowns (e.g., "not sure about validation")

