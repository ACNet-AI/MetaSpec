---
description: Execute specification writing by processing and completing all tasks from tasks.md
---

## User Input

```text
$ARGUMENTS
```

You **MUST** consider the user input before proceeding (if not empty).

## Outline

**Goal**: Execute specification writing tasks systematically, following task order, respecting dependencies, and tracking progress.

**Important**: This command runs AFTER `/metaspec.sds.tasks`. It is the execution engine for specification development.

---

### 📖 Navigation Guide (Quick Reference with Line Numbers)

**🎯 AI Token Optimization**: Use `read_file` with `offset` and `limit` to read only needed sections.

**Core Execution Flow** (Read sequentially):

| Step | Lines | Size | Priority | read_file Usage |
|------|-------|------|----------|-----------------|
| 1-3. Prerequisites & Context | 21-108 | 87 lines | 🔴 MUST READ | `read_file(target_file, offset=21, limit=87)` |
| 4. Execute Writing | 109-151 | 42 lines | 🔴 MUST READ | `read_file(target_file, offset=109, limit=42)` |
| **5. Task Execution Details** ⭐ | 152-619 | 467 lines | 🔴 **KEY** | See subsections below ⬇️ |
| 6-10. Checkpoints & Validation | 620-832 | 212 lines | 🟡 Important | `read_file(target_file, offset=620, limit=212)` |
| 11-13. Reporting & Propagation | 833-938 | 105 lines | 🟡 Important | `read_file(target_file, offset=833, limit=105)` |
| 14. Final Report | 939-1216 | 277 lines | 🟢 Reference | `read_file(target_file, offset=939, limit=277)` |

**📋 Section 5: Task Execution Details** (Most important - 467 lines):

| Task Type | Lines | Size | Usage |
|-----------|-------|------|-------|
| **Refactor Core Spec** | 152-295 | 143 lines | `read_file(target_file, offset=152, limit=143)` |
| Create Sub-Specs (PHASE) | 296-333 | 37 lines | `read_file(target_file, offset=296, limit=37)` |
| Create Sub-Specs (COMPONENT) | 334-358 | 24 lines | `read_file(target_file, offset=334, limit=24)` |
| Create Sub-Specs (SUPPORT) | 359-396 | 37 lines | `read_file(target_file, offset=359, limit=37)` |
| **Entity Templates** | 359-421 | 62 lines | `read_file(target_file, offset=359, limit=62)` |
| **Operation Templates** | 422-467 | 45 lines | `read_file(target_file, offset=422, limit=45)` |
| Validation Templates | 468-499 | 31 lines | `read_file(target_file, offset=468, limit=31)` |
| Example Templates | 500-535 | 35 lines | `read_file(target_file, offset=500, limit=35)` |
| Refinement Tasks | 536-619 | 83 lines | `read_file(target_file, offset=536, limit=83)` |

**💡 Typical Usage Patterns**:
```python
# Quick start: Read Prerequisites only (87 lines)
read_file(target_file, offset=21, limit=87)

# Core execution: Read Steps 1-4 (130 lines)
read_file(target_file, offset=21, limit=130)

# Refactoring guidance: Read Refactor section (143 lines)
read_file(target_file, offset=152, limit=143)

# Template reference: Read specific template (31-143 lines)
read_file(target_file, offset=422, limit=45)  # Operations
```

**Token Savings**: 
- Full file: 1216 lines (~4200 tokens)
- Prerequisites only: 87 lines (~300 tokens) → **93% savings**
- Refactor section: 143 lines (~500 tokens) → **88% savings**
- Template reference: 31-62 lines (~100-200 tokens) → **95% savings**

---

### Execution Flow

#### 1. Check Prerequisites

**Required files**:
- `specs/domain/001-{name}-spec/tasks.md` - Task breakdown
- `specs/domain/001-{name}-spec/plan.md` - Architecture plan
- `specs/domain/001-{name}-spec/spec.md` - Initial specification concept

**If missing**:
- Stop and instruct user to run `/metaspec.sds.tasks` first

#### 2. Load Specification Context

**Step 2a: Determine Current Specification**

Get current specification from Git branch or SPECIFY_FEATURE:
```bash
# From Git branch
current_spec=$(git branch --show-current)
# Or from environment variable
current_spec=$SPECIFY_FEATURE

# Example: "003-payment-processing"
```

**Step 2b: Read Current Specification Metadata**

Read frontmatter from current specification's spec.md:
```yaml
---
spec_id: 003-payment-processing
parent: 001-order-spec
root: 001-order-spec
type: parent
---
```

**Store context for sub-specification creation**:
- `current_id`: "003-payment-processing"
- `parent_id`: "001-order-spec" or null
- `root_id`: "001-order-spec"

**This context will be passed to specify** when creating sub-specifications:
- Sub-specifications will have: parent={current_id}, root={root_id}
- Example: If current=003, sub-specification 013 will have parent=003, root=001

**Step 2c: Read Planning Documents**

**Read all planning documents**:
- `specs/domain/{current_id}/tasks.md` - Task list (REQUIRED)
- `specs/domain/{current_id}/plan.md` - Architecture (REQUIRED)
- `specs/domain/{current_id}/spec.md` - Initial concept (REQUIRED)
- `/memory/constitution.md` - Design principles

**Extract key information**:
- Specification domain and purpose
- Entity definitions
- Validation rules (initial)
- Use cases
- Strategy (single spec vs. multi-spec)

#### 3. Parse tasks.md Structure

**Extract from tasks.md**:
- Phase list (Core, Phase, Component, Support, Cross-Ref)
- Task list per phase
- Task format: `- [ ] [TID] [P?] [LABEL] Description with path`
- Dependencies (sequential vs parallel)
- Checkpoints

**Build execution plan**:
```
Phase 1: Core Specification
  - SDS-T001 [CORE] Refactor to core specification
  
Phase 2: Phase Specifications (if multi-spec)
  - SDS-T002 [P] [PHASE] Create phase 1 specification
  - SDS-T003 [P] [PHASE] Create phase 2 specification
  ...

Phase 3: Supporting Specifications
  - SDS-T008 [SUPPORT] Create support specification 1
  ...

Phase 4: Cross-Reference Validation
  - SDS-T011 [REFINE] Validate integration
  ...
```

#### 4. Execute Specification Writing

**Execution rules**:

1. **Phase-by-phase**:
   - Complete Phase N before starting Phase N+1
   - Verify checkpoint after each phase

2. **Specification-first approach**:
   - Write complete specification sections
   - Include all required elements (entities, operations, validation, examples)
   - Ensure clarity and completeness

3. **Respect dependencies**:
   - Sequential tasks: Execute in order
   - Parallel tasks `[P]`: Can execute simultaneously
   - Core specification must be complete before sub-specifications

4. **Progress tracking**:
   - Mark completed tasks: `- [ ]` → `- [x]`
   - Report after each task
   - Save tasks.md after each phase

**Execution order**:

```
Phase 1: Core Specification
  → Execute SDS-T001 (refactor to core overview)
  → Checkpoint: Core specification defines integration points

Phase 2: Phase/Component Specifications (if multi-spec)
  → Execute SDS-T002, T003, T004... in parallel (phase specifications)
  → Checkpoint: All phase specifications complete

Phase 3: Supporting Specifications
  → Execute SDS-T008, T009... (supporting specifications)
  → Checkpoint: All supporting specifications complete

Phase 4: Cross-Reference Validation
  → Execute SDS-T011, T012, T013 (validation)
  → Checkpoint: All specifications integrated
```

#### 5. Task Execution Details

**For each task**:

1. **Parse task**:
   - Extract: Task ID, Label, Description, File path
   - Check: Is parallel `[P]`?
   - Check: Is checkpoint task?

2. **Execute task BASED ON LABEL**:
   
   **[CORE] - Core Specification Refactoring**:
   - Read existing `specs/domain/001-{name}-spec/spec.md`
   - Extract sections to keep (Overview, Glossary, Use Cases - high-level)
   - Identify sections to move to sub-specifications (detailed entities, operations)
   - Add integration points section referencing sub-specifications
   - Add dependency diagram showing specification structure
   - Target: 300-800 lines (overview only)
   
   **Output structure**:
   ```markdown
   # {Specification Name} Core Domain Specification
   
   **Version**: 1.0.0
   **Status**: Draft
   
   ## Specification Overview
   [Keep: High-level problem, solution, capabilities]
   
   ## Glossary
   [Keep: Key terms]
   
   ## Use Cases
   [Keep: High-level scenarios]
   
   ## Core Entities Overview
   [NEW: Brief entity descriptions, reference sub-specifications]
  - Entity 1: [Brief description] → See domain/002-{entity1}-specification
  - Entity 2: [Brief description] → See domain/003-{entity2}-specification
   
   ## Integration Points
   [NEW: How sub-specifications integrate]
   - Phase specifications: 002-007
   - Component specifications: 008-010
   - Supporting specifications: 011-013
   
   ## Specification Architecture
   [NEW: Dependency diagram from plan.md]
   
   ## Version History
   [Keep/Add: Version tracking]
   ```
   
   **[PHASE] - Phase Specification Creation (CREATE NEW FEATURE)**:
   
   **IMPORTANT**: This creates a NEW specification FEATURE, not just a file.
   
   **Step-by-step**:
   
   a. **Extract task context** (from tasks.md):
      ```
      - [ ] SDS-T002 [P] [PHASE] Create 013-credit-card-payment specification
        - Context: parent=003-payment-processing, root=001-order-spec
        - Specification: Credit card payment processing
        - Entities: CreditCardPayment, CardValidationResult
        - Operations: process_credit_card_payment, validate_card
      ```
   
   b. **Set environment variables** for specify:
      ```bash
      export PARENT_SPEC_ID="003-payment-processing"  # From task context
      export ROOT_SPEC_ID="001-order-spec"        # From task context
      export SPEC_NUMBER="013"                       # From task description
      ```
   
   c. **Call /metaspec.sds.specify internally**:
      - Pass task scope, entities, operations to specify
      - specify will detect context (PARENT_SPEC_ID set)
      - specify will create 013-credit-card-payment/ with correct frontmatter
      - specify generates spec.md with parent chain
   
   d. **Verify sub-specification created**:
      ```yaml
      # Generated in specs/domain/013-credit-card-payment/spec.md
      ---
      spec_id: 013-credit-card-payment
      parent: 003-payment-processing
      root: 001-order-spec
      type: leaf
      ---
      
      # Credit Card Payment Specification
      
      **Parent chain**: 001-order-spec > 003-payment-processing > 013-credit-card-payment
      ```
   
   e. **Update current specification** (003-payment-processing/spec.md):
      - Read current spec.md
      - Find or create "## Sub-Specifications" section
      - Add 013 to the table:
        ```markdown
        | ID | Payment Method | Status |
        |----|---------------|--------|
        | [013](../013-credit-card-payment/spec.md) | Credit Card | Stable |
        ```
      - Update type in frontmatter: `type: parent` (if not already)
   
   f. **Mark task complete**:
      - Update tasks.md: `- [ ]` → `- [x]`
   
   **Target**: Sub-specification with 500-1500 lines (complete specification)
   
   **[COMPONENT] / [SUPPORT] - Create Sub-Specification FEATURE**:
   
   **Same process as [PHASE] above**. Only differences are:
   
   | Type | Focus | Target Lines |
   |------|-------|--------------|
   | **[COMPONENT]** | Component interface, registration, validation | 500-1500 |
   | **[SUPPORT]** | Cross-cutting concerns (orchestration, artifacts) | 300-800 |
   
   **[REFINE] - Refinement/Validation Tasks**:
   - Update existing specification(s)
   - Add cross-references
   - Validate consistency (terminology, entity names)
   - Check dependencies (no cycles)
   - Ensure completeness

3. **Use Sub-Specification Template**:

```markdown
# {Sub-Specification Name} Domain Specification

**Version**: 1.0.0  
**Status**: Draft  
**Last Updated**: {date}

---

## Dependencies

**Domain Specifications**:
- **Depends on**: domain/001-{core}-spec

### Dependency Rationale

{Explain what this sub-specification depends on from core specification:}
- Entities used: [List core entities referenced]
- Operations extended: [List operations]
- Validation rules inherited: [List rules]

---

## Specification Overview

**Name**: {Sub-Specification Name}  
**Domain**: {Specific concern within main specification}  
**Purpose**: {What problem this sub-specification solves}

**Problem Statement**: {Detailed problem description}

**Solution**: {How this sub-specification addresses the problem}

**Scope**:
- ✅ Included: {What's in scope}
- ❌ Excluded: {What's out of scope}

---

## Glossary

{Terms specific to this sub-specification}

- **{Term 1}**: {Definition}
  - Example: {Example usage}
  
- **{Term 2}**: {Definition}

---

## Use Cases

### Use Case 1: {Scenario Name}

**Scenario**: {Description}

**Actors**:
- Actor 1: {Role}
- Actor 2: {Role}

**Flow**:
1. {Step 1}
2. {Step 2}
3. {Step 3}

**Specification Elements Used**:
- {Element 1}
- {Element 2}

**Outcome**: {Expected result}

---

## Core Entities

{Entities specific to this sub-specification}

### Entity: {EntityName}

**Purpose**: {What this entity represents}

**Schema**:
```yaml
entity_name:
  field1:
    type: string
    required: true
    description: {field description}
  field2:
    type: number
    required: false
    description: {field description}
    constraints:
      - {constraint 1}
      - {constraint 2}
```

**Validation Rules**:
- VR001: {Validation rule 1}
- VR002: {Validation rule 2}

**Example**:
```json
{
  "field1": "example value",
  "field2": 42
}
```

---

## Workflow

{If this sub-specification involves state transitions or lifecycle}

### State Machine: {Entity Name}

**States**:
- `state_1`: {State description}
- `state_2`: {State description}

**Initial State**: `{initial_state}`

**Allowed Transitions**:

#### `state_1` → `state_2`
- **Trigger**: {What causes this transition}
- **Precondition**: {What must be true}
- **Action**: {What happens}
- **Postcondition**: {Result state}

**Forbidden Transitions**:
- ❌ `state_x` → `state_y`: {Reason}

---

## Specification Operations

{Operations specific to this sub-specification}

### Operation: {operation_name}

**Purpose**: {What this operation does}

**Request Schema**:
```yaml
operation_request:
  param1:
    type: string
    required: true
  param2:
    type: object
    required: false
```

**Response Schema**:
```yaml
operation_response:
  result:
    type: string
  error:
    type: string
    required: false
```

**Validation Rules**:
- {Rule 1}
- {Rule 2}

**Example**:
```json
// Request
{
  "param1": "value"
}

// Response
{
  "result": "success"
}
```

---

## Validation Rules

### Entity Validation
1. **{Entity 1}**: {Validation rules}
2. **{Entity 2}**: {Validation rules}

### Operation Validation
1. **{Operation 1}**: {Validation rules}
2. **{Operation 2}**: {Validation rules}

### Cross-Entity Validation
1. {Rule 1}
2. {Rule 2}

---

## Error Handling

### Error Codes
- `E001`: {Error description}
- `E002`: {Error description}

### Error Response Format
```yaml
error_response:
  code: string
  message: string
  details: object (optional)
```

---

## Examples

### Example 1: {Scenario Name}

**Context**: {Setup}

**Request**:
```json
{example request}
```

**Response**:
```json
{example response}
```

**Validation**: ✅ All rules pass

### Example 2: {Error Scenario}

**Context**: {Setup with error condition}

**Request**:
```json
{example request}
```

**Response**:
```json
{error response}
```

**Validation**: ❌ {Which rule failed}

---

## Integration with Core Specification

### Entity References

**From Core Specification**:
- {Core Entity 1}: {How used in this sub-specification}
- {Core Entity 2}: {How used in this sub-specification}

### Operation Extensions

**Extends Core Operations**:
- {Core Operation 1}: {How extended}

**New Operations**:
- {New Operation 1}: {Why needed}

### Validation Rule Inheritance

**Inherited Rules**:
- {Core Rule 1}: Applied to {this entity}
- {Core Rule 2}: Applied to {this entity}

**Extended Rules**:
- {Extended Rule 1}: {How it extends core rule}

---

## Clarifications

### Session {date}

- **Q**: {Question about ambiguity}
  **A**: {Resolution}

---

## Version History

- **v1.0.0** ({date}): Initial sub-specification specification
  - Defined {N} entities
  - Specified {N} operations
  - Established {N} validation rules

---

**Specification Maintainers**: {Team}  
**Contributing**: See `/memory/specification-constitution.md`  
**License**: {License}
```

4. **Verify specification completeness**:
   
   **For Core Specification**:
   - [ ] Specification overview is clear and concise
   - [ ] Glossary includes all key terms
   - [ ] Use cases show specification value
   - [ ] Entity overview lists all entities
   - [ ] Integration points reference all sub-specifications
   - [ ] Dependency diagram is accurate
   - [ ] Size: 300-800 lines
   
   **For Sub-Specifications**:
   - [ ] Dependencies section references core specification
   - [ ] Purpose and scope are clear
   - [ ] Entities have complete schemas
   - [ ] Operations have request/response definitions
   - [ ] Validation rules are comprehensive
   - [ ] Examples demonstrate usage
   - [ ] Integration section explains core specification relationship
   - [ ] Size: 300-1500 lines (varies by type)
   
   **For Refinement Tasks**:
   - [ ] Cross-references are correct
   - [ ] Terminology is consistent
   - [ ] Dependencies are acyclic
   - [ ] Entity names match across specifications

5. **Mark complete**:
   - Update tasks.md: `- [ ] SDS-T001` → `- [x] SDS-T001`
   - Report: "✅ SDS-T001 complete: Created core specification overview"

6. **Handle errors**:
   - If task fails: Report error, suggest fix
   - If sequential task fails: Halt phase
   - If parallel task fails: Continue others, report at end

#### 6. Phase Checkpoints

**After each phase**:

1. **Verify checkpoint criteria**:
   - Phase 1: `✅ Core specification defines integration points clearly`
   - Phase 2: `✅ All phase/component specifications complete (500-1500 lines each)`
   - Phase 3: `✅ All supporting specifications complete (300-800 lines each)`
   - Phase 4: `✅ All specifications integrated and consistent`

2. **If checkpoint fails**:
   - Stop phase
   - Report failing criteria
   - Suggest fixes
   - Ask user: "Fix issues and continue? (yes/no)"

3. **If checkpoint passes**:
   - Report success
   - Save tasks.md
   - Proceed to next phase

#### 7. Progress Reporting

**After each task**:
```
✅ SDS-T002 complete: Created order-creation specification

📄 File created:
   specs/domain/002-order-creation-spec/spec.md
   
📊 Specification:
   - Entities: 4 (Order, CartItem, Customer, ValidationRule)
   - Operations: 3 (initialize_order, validate_cart, create_order)
   - Validation Rules: 15
   - Examples: 3
   - Size: 800 lines

✅ Quality checks:
   - Dependencies: ✅ References core specification
   - Entities: ✅ Complete schemas
   - Validation: ✅ Comprehensive rules
   - Examples: ✅ Demonstrates usage
   - Integration: ✅ Explains core specification relationship
```

**After each phase**:
```
✅ Phase 2 complete: Phase Specifications

📊 Summary:
   - Tasks: 7/7 complete
   - Time: 2.5 days
   
   Specifications created:
   - 002-order-creation-spec (800 lines) ✅
   - 003-payment-processing-spec (950 lines) ✅
   - 004-fulfillment-spec (850 lines) ✅
   - 005-shipping-spec (780 lines) ✅
   - 006-delivery-spec (720 lines) ✅
   - 007-returns-spec (680 lines) ✅
   - 008-refunds-spec (650 lines) ✅
   
   Checkpoint: ✅ All phase specifications complete
   
   Next: Phase 3 (Supporting Specifications)
```

**Overall progress**:
```
📊 Specification Progress: 7/13 tasks (54%)
   Phase 1: ✅ 1/1 (Core Specification)
   Phase 2: ✅ 6/6 (Phase Specifications)
   Phase 3: 🔄 0/3 (Supporting Specifications)
   Phase 4: ⏳ 0/3 (Cross-Reference Validation)
```

#### 8. Cross-Reference Validation

**After all specifications written**:

1. **Check core specification references**:
   - Verify all sub-specification references are correct
   - Ensure paths match actual files
   - Check version references

2. **Check sub-specification dependencies**:
   - Verify "Depends on" sections reference correct specifications
   - Check entity references are valid
   - Ensure operation references are correct

3. **Check terminology consistency**:
   - Glossary terms used consistently
   - Entity names match across specifications
   - No conflicting definitions

4. **Check dependency graph**:
   - Draw dependency graph
   - Verify no circular dependencies
   - Ensure core specification is at root

5. **Generate cross-reference report**:
```
✅ Cross-Reference Validation Complete

📊 Statistics:
   - Total specifications: 10
   - Core specification: 1
   - Sub-specifications: 9
   - Cross-references: 47

✅ Validation Results:
   - Dependency graph: ✅ Acyclic
   - Entity references: ✅ All valid (47/47)
   - Operation references: ✅ All valid (23/23)
   - Terminology: ✅ Consistent (52 terms)
   - File paths: ✅ All correct

📊 Dependency Summary:
   Core (001) → 9 sub-specifications
   - Phase specifications: 002-007 (6 specs)
   - Supporting specifications: 008-010 (3 specs)
   
   No circular dependencies detected ✅
```

#### 9. Completion Validation

**After all phases**:

1. **Verify completeness**:
   - [ ] All tasks marked `[x]`
   - [ ] All checkpoints passed
   - [ ] All specifications written
   - [ ] Cross-references validated
   - [ ] Constitution compliant

2. **Quality checks**:
   - Total specification size: {X} lines across {N} files
   - Each specification < 1500 lines
   - All entities have examples
   - All validation rules documented
   - Terminology consistent

3. **Constitution compliance**:
   - ✅ Minimal Viable Abstraction: Entities have 3-5 core fields
   - ✅ Specification-First: Specification defines WHAT, not HOW
   - ✅ Clear Boundaries: Sub-specifications have distinct responsibilities
   - ✅ Progressive Enhancement: MVP scope defined (P0 complete)
   - ✅ Domain Specificity: Domain constraints respected

4. **Generate report**:
   ```
   ✅ Domain specification complete
   
   📊 Summary:
   - Total specifications: 12
     - Core specification: 1 (650 lines)
     - Phase specifications: 7 (650-950 lines each)
     - Supporting specifications: 4 (550-700 lines each)
   - Total size: 8,200 lines
   - Time: 5 days
   
   📦 Specifications:
   - ✅ Core specification (001-order-spec)
   - ✅ Order creation phase (002-order-creation-spec)
   - ✅ Payment processing phase (003-payment-processing-spec)
   - ✅ Fulfillment phase (004-fulfillment-spec)
   - ✅ Shipping phase (005-shipping-spec)
   - ✅ Delivery phase (006-delivery-spec)
   - ✅ Returns phase (007-returns-spec)
   - ✅ Refunds phase (008-refunds-spec)
   - ✅ Payment gateway support (009-payment-gateway-spec)
   - ✅ Inventory sync support (010-inventory-sync-spec)
   - ✅ Notification support (011-notification-spec)
   - ✅ Audit log support (012-audit-spec)
   
   ✅ Quality Metrics:
   - Cross-references: 52 (all valid)
   - Dependencies: Acyclic (no cycles)
   - Terminology: Consistent (58 terms)
   - Examples: 31 (across all specs)
   - Validation rules: 172 (comprehensive)
   
   🎯 MVP Status:
   - v1.0.0 ready for publication
   - Core + P0 sub-specifications complete
   
   🔄 Next steps:
   1. Run /metaspec.sds.checklist to verify quality
   2. Run /metaspec.sds.analyze to check consistency
   3. Share with stakeholders for review
   4. Update CHANGELOG.md
   5. Create git tag v1.0.0
   
   💡 Suggested commit message:
      docs: complete specification system v1.0.0
   ```

#### 10. Incremental Saves

**Save progress frequently**:
- Save tasks.md after each phase
- Commit specifications after each checkpoint
- Push to git after significant milestones

**Suggested commit messages**:
```bash
git commit -m "docs: complete core specification overview (Phase 1)"
git commit -m "docs: add phase specifications (Phase 2)"
git commit -m "docs: add supporting specifications (Phase 3)"
git commit -m "docs: validate cross-references (Phase 4)"
```

#### 11. Generate Implementation Report

**Purpose**: Create detailed record of implementation work for tracking and quality assurance.

After all tasks complete, prepend this HTML comment to `specs/domain/{spec_id}/IMPLEMENTATION.md` (create if not exists):

```html
<!--
Specification Implementation Report
====================================
Spec: {spec_id} | Duration: {start_date} - {end_date} ({days}d) | Strategy: {Single | Multi-Spec}

Summary:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Tasks: {completed}/{total} ({percent}%) | By Phase: P1: {p1_done}/{p1}, P2: {p2_done}/{p2}, P3: {p3_done}/{p3}, P4: {p4_done}/{p4}, P5: {p5_done}/{p5}

Files:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Created: {created} specs ({total_lines} lines) | Updated: tasks.md, plan.md

Metrics:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Entities: {entities} | Operations: {ops} | Rules: {rules} | Examples: {examples}
Completeness: {percent}% | Cross-Refs: {✅ Valid | ⚠️ {count} issues}

Constitution: {✅ Compliant | ⚠️ Check: {issues}}

Next: Review consistency → Run analyze → Update toolkit → Update docs

Generated by: /metaspec.sds.implement
-->
```

**Also update tasks.md**:
Mark completed tasks with `[x]` and add completion notes.

#### 12. Consistency Propagation and Impact Analysis

**Purpose**: Verify implementation consistency across all files.

#### A. Specification Cross-Validation

```bash
# Validate all created specifications
for spec in specs/domain/*/spec.md; do
  echo "Checking: $spec"
  # Check YAML frontmatter
  grep -A 5 "^---$" "$spec" | head -6
  # Count entities, operations
  grep "^### Entity:" "$spec" | wc -l
  grep "^### Operation:" "$spec" | wc -l
done
```

**Verify**:
- [ ] All specs have valid YAML frontmatter
- [ ] Parent-child relationships correct
- [ ] Root specification consistent
- [ ] No orphaned specifications

#### B. Cross-Reference Validation

```bash
# Find all internal references
grep -r "\[.*\](\.\./.*/spec\.md)" specs/domain/*/spec.md

# Verify each reference exists
for ref in {list of references}; do
  if [ -f "$ref" ]; then
    echo "✅ $ref exists"
  else
    echo "❌ BROKEN: $ref"
  fi
done
```

**Action if broken**:
- Fix references immediately
- Re-check after fixes

#### C. Tasks Status Synchronization

```bash
# Verify all tasks marked complete
cat specs/domain/{spec_id}/tasks.md | grep "^\- \[ \]" || echo "All done!"
```

**Update tasks.md**:
- Mark all completed tasks with `[x]`
- Add completion timestamps
- Note any skipped tasks

#### D. Related Files Impact Check

```bash
# Check if toolkit specs need updates
find specs/toolkit/ -name "spec.md" -exec grep -l "{spec_id}" {} \;

# Check documentation
grep -l "{spec_id}" docs/*.md README.md 2>/dev/null
```

**If found**:
- Note which files need manual review
- Add to follow-up TODOs

#### 13. Completion Validation (Enhanced)

**Final quality checks before reporting completion**:

```bash
# Run comprehensive validation
/metaspec.sds.analyze
```

**Manual checks**:
- [ ] All specifications have examples
- [ ] All entities have complete field definitions
- [ ] All operations have request/response schemas
- [ ] All validation rules are testable
- [ ] Cross-references are bidirectional
- [ ] Terminology is consistent across specs
- [ ] No placeholder content remains
- [ ] Size targets met (specs within 600-1500 lines)

**Constitution alignment final check**:
- [ ] Specifications are minimal (no over-specification)
- [ ] Domain fidelity maintained (no implementation details)
- [ ] Validation rules are complete (all cases covered)
- [ ] Operations are well-defined (clear semantics)
- [ ] Entities are clear (unambiguous definitions)
- [ ] Extensibility considered (future-proof design)

#### 14. Report Completion (Enhanced)

Provide comprehensive implementation summary:

```
✅ Domain specification implementation complete

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

📊 Implementation Summary:
   Specification: {spec_id}
   Duration: {start_date} to {end_date} ({days} days)
   Strategy: {Single Spec | Multi-Spec}

   Tasks Completed: {completed}/{total} ({percentage}%)
   - Phase 1 (Core): {phase1_tasks} tasks ✅
   - Phase 2 (Phase Specs): {phase2_tasks} tasks ✅
   - Phase 3 (Supporting): {phase3_tasks} tasks ✅
   - Phase 4 (Cross-Refs): {phase4_tasks} tasks ✅
   - Phase 5 (Quality): {phase5_tasks} tasks ✅

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

📁 Files Created/Updated:

   **Created** ({count} specification files):
   ✅ Core: specs/domain/{core_id}/spec.md
      - {entity_count} entities, {operation_count} operations
      - {validation_count} validation rules, {example_count} examples
      - Size: {lines} lines ✅
   
   {FOR each sub-specification}:
   ✅ Sub: specs/domain/{sub_id}/spec.md
      - {entity_count} entities, {operation_count} operations
      - Size: {lines} lines ✅
   {END FOR}

   **Updated**:
   ✅ tasks.md: All tasks marked complete
   ✅ plan.md: Implementation notes added
   ✅ IMPLEMENTATION.md: Full report generated

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

✅ Validation Results:

   **Specification Quality**: {✅ Excellent | ⚠️ Good | ❌ Needs Work}
   - Total entities: {entity_count}
   - Total operations: {operation_count}
   - Total validation rules: {validation_count}
   - Total examples: {example_count}
   - Average size: {avg_lines} lines/spec

   **Cross-Reference Integrity**: {✅ Valid | ⚠️ Issues Found}
   - Internal references: {valid}/{total} ✅
   - External references: {valid}/{total} ✅
   {IF issues}:
   ⚠️  Broken references:
   - {reference_1} → {issue}
   - {reference_2} → {issue}
   Action: Fix before finalizing
   {END IF}

   **Constitution Compliance**: {✅ Fully Compliant | ⚠️ Minor Issues}
   - Entity Clarity: {✅ | ⚠️} {comment}
   - Validation Completeness: {✅ | ⚠️} {comment}
   - Operation Semantics: {✅ | ⚠️} {comment}
   - Implementation Neutrality: {✅ | ⚠️} {comment}
   - Extensibility Design: {✅ | ⚠️} {comment}
   - Domain Fidelity: {✅ | ⚠️} {comment}

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

🎯 Impact Analysis:

   **Related Files to Review**:
   {IF toolkit_impact}:
   🔧 Toolkit Specifications ({count}):
   - specs/toolkit/{toolkit_id}/spec.md - Update models to match entities
   {END IF}

   {IF doc_impact}:
   📚 Documentation ({count} files):
   - docs/{file}.md - Update specification references
   - README.md - Update overview with new specs
   {END IF}

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

📈 Metrics:

   **Size Distribution**:
   - Total lines: {total_lines}
   - Average: {avg_lines} lines/spec
   - Range: {min_lines} - {max_lines} lines
   - Target compliance: {in_range}/{total} specs ✅

   **Content Density**:
   - Entities per spec: {avg_entities}
   - Operations per spec: {avg_operations}
   - Validation rules per spec: {avg_validations}
   - Examples per spec: {avg_examples}

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

🔄 Next Steps:

   1. Run comprehensive analysis:
      → /metaspec.sds.analyze
      
   2. Generate quality checklist:
      → /metaspec.sds.checklist
      
   3. {IF toolkit_exists}:
      Update toolkit implementation:
      → /metaspec.sdd.implement
      {END IF}
      
   4. Update project documentation:
      - README.md with specification overview
      - AGENTS.md with specification usage guidance

⚠️  Follow-up TODOs:

   {IF cross_ref_issues}:
   - [ ] Fix broken cross-references: {list}
   {END IF}
   {IF size_issues}:
   - [ ] Review oversized specifications: {list}
   {END IF}
   {IF toolkit_impact}:
   - [ ] Update toolkit models and validators
   {END IF}
   {IF doc_impact}:
   - [ ] Update documentation files: {list}
   {END IF}
   - [ ] Run final quality check: /metaspec.sds.analyze
   - [ ] Generate quality report: /metaspec.sds.checklist

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

💡 Suggested Commit Message:

   docs(spec): complete {spec_id} specification implementation
   
   Implementation:
   - Strategy: {Single | Multi}-spec approach
   - Created: {count} specification files
   - Total: {entity_count} entities, {operation_count} operations
   - Size: {total_lines} lines
   
   Quality:
   - Cross-references: {valid}/{total} valid
   - Constitution: {✅ Compliant | ⚠️ Needs Review}
   - Size targets: {in_range}/{total} specs in range
   
   {IF issues}:
   Known Issues:
   - {issue_1}
   - {issue_2}
   {END IF}
```

## Important Notes

1. **Specification quality is paramount**
   - Write clear, comprehensive specifications
   - Include concrete examples
   - Document validation rules completely
   - Ensure terminology consistency

2. **Phase isolation**
   - Don't start Phase N+1 until Phase N complete
   - Verify checkpoint after each phase
   - Fix issues before proceeding

3. **Parallel execution**
   - Sub-specifications marked `[P]` can be written in parallel
   - Only if they are independent
   - Report all results together

4. **Constitution alignment**
   - Check principles after each phase
   - Ensure specifications are minimal and clear
   - Avoid over-specification

5. **Cross-reference integrity**
   - Validate references after all specifications written
   - Fix broken references immediately
   - Ensure dependency graph is acyclic

6. **Progress visibility**
   - Report after each task
   - Show percentage complete
   - Estimate time remaining

## Example: Phase 2 Execution

**Phase 2: Phase Specifications (7 specifications)**

```
Starting Phase 2: Phase Specifications (7 tasks, can be parallel)

✅ SDS-T002: Create order-creation specification
   File: specs/domain/002-order-creation-spec/spec.md
   Entities: 4 (Order, CartItem, Customer, ValidationRule)
   Operations: 3 (initialize_order, validate_cart, create_order)
   Validation rules: 15
   Examples: 3
   Size: 800 lines ✅

✅ SDS-T003: Create payment-processing specification
   File: specs/domain/003-payment-processing-spec/spec.md
   Entities: 5 (Payment, Transaction, PaymentMethod, Gateway, Receipt)
   Operations: 4 (authorize, capture, refund, verify)
   Validation rules: 18
   Examples: 4
   Size: 950 lines ✅

✅ SDS-T004: Create fulfillment specification
   File: specs/domain/004-fulfillment-spec/spec.md
   Entities: 5 (FulfillmentOrder, InventoryItem, PickList, PackingSlip, Warehouse)
   Operations: 4 (allocate_inventory, create_picklist, pack_items, mark_shipped)
   Validation rules: 16
   Examples: 3
   Size: 850 lines ✅

✅ SDS-T005: Create shipping specification
   [Similar details]
   Size: 780 lines ✅

✅ SDS-T006: Create delivery specification
   [Similar details]
   Size: 720 lines ✅

✅ SDS-T007: Create returns specification
   [Similar details]
   Size: 680 lines ✅

✅ SDS-T008: Create refunds specification
   [Similar details]
   Size: 650 lines ✅

✅ Phase 2 checkpoint: All phase specifications complete (600-1000 lines each)

Phase 2 complete: 7/7 tasks (2.5 days)

Next: Phase 3 (Supporting Specifications)
```


