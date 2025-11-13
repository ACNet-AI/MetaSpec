---
description: Generate actionable task breakdown for specification work based on architecture plan
---

## User Input

```text
$ARGUMENTS
```

You **MUST** consider the user input before proceeding (if not empty).

## Outline

**Goal**: Break down specification work into specific, executable tasks organized by sub-specification and ordered by dependencies.

**Important**: This command runs AFTER `/metaspec.sds.plan`. It transforms architecture plan into actionable specification tasks.

---

### 📖 Navigation Guide (Quick Reference with Line Numbers)

**🎯 AI Token Optimization**: Use `read_file` with `offset` and `limit` to read only needed sections.

**Core Flow** (Read sequentially):

| Step | Lines | Size | Priority | read_file Usage |
|------|-------|------|----------|-----------------|
| 1-3. Load & Rules | 21-141 | 120 lines | 🔴 MUST READ | `read_file(target_file, offset=21, limit=120)` |
| 4. Single Spec Strategy | 142-189 | 47 lines | 🟡 Important | `read_file(target_file, offset=142, limit=47)` |
| **5. Multi-Spec Strategy** ⭐ | 190-278 | 88 lines | 🔴 **KEY** | `read_file(target_file, offset=190, limit=88)` |
| 6. Sub-Spec Template | 279-346 | 67 lines | 🔴 **KEY** | `read_file(target_file, offset=279, limit=67)` |
| 7-9. Generate & Validate | 347-490 | 143 lines | 🟡 Important | `read_file(target_file, offset=347, limit=143)` |
| 10-11. Propagation & Report | 491-645 | 154 lines | 🟡 Important | `read_file(target_file, offset=491, limit=154)` |
| 12. Final Report | 646-824 | 178 lines | 🟢 Reference | `read_file(target_file, offset=646, limit=178)` |

**📋 Task Templates** (Jump to specific template):

| Template Type | Lines | Size | Usage |
|---------------|-------|------|-------|
| **Single Spec Refinement** | 825-833 | 8 lines | `read_file(target_file, offset=825, limit=8)` |
| **Core Specification** | 834-843 | 9 lines | `read_file(target_file, offset=834, limit=9)` |
| **Phase Specification** ⭐ | 844-855 | 11 lines | `read_file(target_file, offset=844, limit=11)` |
| **Component Specification** | 856-868 | 12 lines | `read_file(target_file, offset=856, limit=12)` |
| **Supporting Specification** | 869-909 | 40 lines | `read_file(target_file, offset=869, limit=40)` |

**🎯 Phase Workflows** (Multi-spec patterns):

| Phase | Lines | Size | Usage |
|-------|-------|------|-------|
| Phase 1: Core Spec | 910-918 | 8 lines | `read_file(target_file, offset=910, limit=8)` |
| Phase 2: Lifecycle Phases | 919-946 | 27 lines | `read_file(target_file, offset=919, limit=27)` |
| Phase 3: Supporting Specs | 947-972 | 25 lines | `read_file(target_file, offset=947, limit=25)` |
| Phase 4: Cross-Reference | 973-993 | 20 lines | `read_file(target_file, offset=973, limit=20)` |

**💡 Typical Usage Patterns**:
```python
# Quick start: Read core flow (120 lines)
read_file(target_file, offset=21, limit=120)

# Multi-spec strategy: Read Step 5 + 6 (155 lines)
read_file(target_file, offset=190, limit=155)

# Specific template: Read template only (8-40 lines)
read_file(target_file, offset=844, limit=11)  # Phase template

# Phase pattern: Read specific phase (8-27 lines)
read_file(target_file, offset=919, limit=27)  # Phase 2
```

**Token Savings**: 
- Full file: 993 lines (~3400 tokens)
- Core flow: 120 lines (~410 tokens) → **88% savings**
- Multi-spec strategy: 155 lines (~530 tokens) → **84% savings**
- Template only: 8-40 lines (~30-140 tokens) → **96-99% savings**

---

### Execution Flow

#### 1. Load Planning Context

**Step 1a: Determine Current Specification**

Get current specification from Git branch or SPECIFY_FEATURE:
```bash
# From Git branch
current_spec=$(git branch --show-current)
# Or from environment variable
current_spec=$SPECIFY_FEATURE

# Example: "003-payment-processing"
```

**Step 1b: Read Current Specification Metadata**

Read frontmatter from current specification's spec.md:
```yaml
---
spec_id: 003-payment-processing
parent: 001-order-spec
root: 001-order-spec
type: parent
---
```

**Store context**:
- `current_id`: "003-payment-processing"
- `parent_id`: "001-order-spec" or null
- `root_id`: "001-order-spec"

**This is important for**:
- Determining numbering for sub-specifications
- Constructing parent chains
- Understanding hierarchy depth

**Step 1c: Load Planning Documents**

**Required**:
- `specs/domain/{current_id}/plan.md` - Architecture plan
- `specs/domain/{current_id}/spec.md` - Domain specification

**Extract from plan.md**:
- Split decision (single spec vs. sub-specifications)
- Sub-specification list (if splitting)
- Dependencies between sub-specifications
- Implementation order (Phase 1, 2, 3...)
- Priority levels (P0, P1, P2)
- Recommended numbering for sub-specifications

#### 2. Determine Task Strategy

**Strategy A: Single Specification Refinement**

**When**: plan.md recommends keeping single spec (< 1500 lines)

**Tasks**:
- Refine existing spec.md sections
- Add missing details
- Expand validation rules
- Add examples
- Improve clarity

**Task count**: 5-15 tasks (section refinements)

**Strategy B: Multi-Specification Development**

**When**: plan.md recommends splitting (1500+ lines)

**Tasks**:
- Create core specification (overview)
- Create each sub-specification
- Define cross-references
- Ensure consistency
- Validate dependencies

**Task count**: 15-50 tasks (N sub-specs × 3-5 tasks each)

#### 3. Task Generation Rules

**Checklist Format (REQUIRED)**:

Every task MUST follow:
```
- [ ] [TaskID] [P] [SPEC] Description with spec path
  - Context: parent={parent}, root={root}
  - Details: ...
```

**Format Components**:
1. **Checkbox**: `- [ ]` (markdown checkbox)
2. **Task ID**: SDS-T001, SDS-T002... (sequential, execution order)
3. **[P] marker**: ONLY if parallelizable (independent sub-specs)
4. **[SPEC] label**: [CORE], [PHASE], [COMPONENT], [SUPPORT], [REFINE]
5. **Description**: Clear action with spec file path
6. **Context** (NEW for sub-specifications): parent and root IDs
7. **Details**: Scope, entities, operations

**Examples for Creating Sub-Specifications** (NEW):
- ✅ `- [ ] SDS-T002 [P] [PHASE] Create 013-credit-card-payment specification`
  - Context: parent=003-payment-processing, root=001-order-spec
  - Specification: Credit card payment processing
  - Entities: CreditCardPayment, CardValidationResult
  - Operations: process_credit_card_payment, validate_card

- ✅ `- [ ] SDS-T003 [P] [PHASE] Create 014-digital-wallet-payment specification`
  - Context: parent=003-payment-processing, root=001-order-spec
  - Specification: Digital wallet payment (PayPal, Apple Pay, Google Pay)
  - Entities: WalletPayment, WalletProvider
  - Operations: process_wallet_payment, link_wallet

**Examples for Refining Current Specification**:
- ✅ `- [ ] SDS-T001 [CORE] Refactor current specification to overview`
  - Keep: Overview, common concepts
  - Remove: Detailed implementations (move to sub-specifications)
  - Add: Sub-specification index

**Legacy format** (still valid for non-splitting scenarios):
- ✅ `- [ ] SDS-T001 [REFINE] Expand Specification Overview section`
- ❌ `- [ ] Write specification` (missing ID, SPEC label, file path)

#### 4. Task Organization for Single Spec (Strategy A)

**Phase 1: Section Refinement**

- [ ] SDS-T001 [REFINE] Expand Specification Overview section
  - Add detailed problem statement
  - Clarify solution approach
  - Define scope boundaries

- [ ] SDS-T002 [REFINE] Enhance Glossary section
  - Add missing terms
  - Provide concrete examples for each term
  - Ensure consistency with entity definitions

- [ ] SDS-T003 [REFINE] Elaborate Use Cases section
  - Add 2-3 additional use cases
  - Detail actor interactions
  - Show specification element usage

- [ ] SDS-T004 [REFINE] Detail Core Entities section
  - Expand entity schemas with all fields
  - Add field-level validation rules
  - Provide entity examples

- [ ] SDS-T005 [REFINE] Complete Validation Rules section
  - Enumerate all validation rules
  - Provide error code taxonomy
  - Add validation examples

- [ ] SDS-T006 [REFINE] Expand Examples section
  - Add basic examples (simple scenarios)
  - Add advanced examples (complex scenarios)
  - Add anti-patterns (what NOT to do)

**Phase 2: Quality Assurance**

- [ ] SDS-T007 [REFINE] Review for consistency
  - Check entity references
  - Verify validation rule completeness
  - Ensure terminology consistency

- [ ] SDS-T008 [REFINE] Add cross-references
  - Link related sections
  - Reference external standards
  - Document version compatibility

**Checkpoint**: Single specification complete and comprehensive (800-1500 lines)

#### 5. Task Organization for Multi-Spec (Strategy B)

**Phase 1: Core Specification Creation**

**Goal**: Create overview specification that integrates all sub-specifications

- [ ] SDS-T001 [CORE] Refactor existing spec.md to core specification overview
  - Keep: Specification Overview, Glossary, Use Cases (high-level)
  - Remove: Detailed entity definitions (move to sub-specs)
  - Add: Integration points to sub-specifications
  - Target size: 300-800 lines

**Checkpoint**: Core specification defines integration points

**Phase 2: Phase-Specific Specifications** (if using Lifecycle pattern)

**Goal**: Create detailed specifications for each lifecycle phase

- [ ] SDS-T002 [P] [PHASE] Create specs/domain/002-{phase1}-spec/spec.md
  - Define phase purpose and objectives
  - Detail phase entry/exit criteria
  - Specify phase-specific entities
  - Define phase operations
  - Add phase validation rules
  - Provide phase examples
  - Reference: Core specification for integration

- [ ] SDS-T003 [P] [PHASE] Create specs/domain/003-{phase2}-spec/spec.md
  [Same structure as SDS-T002]

- [ ] SDS-T004 [P] [PHASE] Create specs/domain/004-{phase3}-spec/spec.md
  [Same structure as SDS-T002]

[... Continue for all phases ...]

**Checkpoint**: All phase specifications complete (500-1500 lines each)

**Phase 3: Component Specifications** (if using Component pattern)

**Goal**: Create detailed specifications for each component type

- [ ] SDS-T008 [P] [COMPONENT] Create specs/domain/00X-{component1}-spec/spec.md
  - Define component purpose
  - Specify component interface
  - Detail component registration pattern
  - Define component validation rules
  - Provide component examples

- [ ] SDS-T009 [P] [COMPONENT] Create specs/domain/00X-{component2}-spec/spec.md
  [Same structure]

**Checkpoint**: All component specifications complete

**Phase 4: Supporting Specifications**

**Goal**: Create cross-cutting concern specifications

- [ ] SDS-T012 [SUPPORT] Create specs/domain/00X-{support1}-spec/spec.md
  - Define supporting system purpose
  - Specify interfaces and patterns
  - Detail integration with core entities
  - Provide usage examples

- [ ] SDS-T013 [SUPPORT] Create specs/domain/00X-{support2}-spec/spec.md
  [Same structure]

**Checkpoint**: All supporting specifications complete

**Phase 5: Cross-Reference Validation**

**Goal**: Ensure all sub-specifications are properly integrated

- [ ] SDS-T016 [REFINE] Validate core specification integration points
  - Check all sub-spec references are correct
  - Ensure dependency graph is acyclic
  - Verify version compatibility statements

- [ ] SDS-T017 [REFINE] Add cross-references in sub-specifications
  - Each sub-spec references core specification
  - Sub-specs reference related sub-specs where needed
  - Cross-references use correct paths

- [ ] SDS-T018 [REFINE] Ensure terminology consistency
  - Glossary terms used consistently
  - Entity names match across specifications
  - No conflicting definitions

**Checkpoint**: All specifications properly integrated

#### 6. Sub-Specification Template

**For each sub-specification task, use this template**:

```markdown
**Task**: Create specs/domain/00X-{name}-spec/spec.md

**Structure**:
```markdown
# {Sub-Specification Name} Domain Specification

**Version**: 1.0.0
**Status**: Draft
**Dependencies**: domain/001-{core}-spec

---

## Specification Overview

**Purpose**: [Specific concern this sub-specification addresses]

**Scope**: [What's included and excluded]

**Dependencies**: 
- **Depends on**: domain/001-{core}-spec
- **Uses entities from**: [Entity references]
- **Extends**: [What it extends from core]

---

## Entities

[Define entities specific to this sub-specification]

---

## Operations

[Define operations specific to this sub-specification]

---

## Validation Rules

[Define validation rules specific to this sub-specification]

---

## Examples

[Provide examples demonstrating this sub-specification]

---

## Integration with Core Specification

[Explain how this sub-specification integrates with core specification]
```

**Estimated size**: 500-1500 lines

**Priority**: [P0/P1/P2]

**Dependencies**: 
- Must complete: SDS-T001 (core specification)
- Can parallelize with: [Other sub-spec tasks]
```

#### 7. Dependency Tracking

**Component Dependencies**:

```
For Single Spec (Strategy A):
REFINE Phase 1 → REFINE Phase 2 (Sequential)

For Multi-Spec (Strategy B):
CORE → PHASE/COMPONENT → SUPPORT → CROSS-REF
  ↓
All PHASE tasks can be parallel
All COMPONENT tasks can be parallel
```

**Parallel Opportunities**:

**Strategy A (Single Spec)**:
- Limited parallelization (sections in same file)
- Best: Sequential refinement

**Strategy B (Multi-Spec)**:
- Phase specifications can be written in parallel
- Component specifications can be written in parallel
- Supporting specifications can be written after phases/components

#### 8. Generate tasks.md

**Structure**:
```markdown
# Domain Specification Tasks: [Specification Name]

## Overview
- **Total Tasks**: [N]
- **Strategy**: [Single Spec Refinement / Multi-Spec Development]
- **Estimated Time**: [X] days

## Dependencies

[Dependency diagram from plan.md]

## Phase 1: [Phase Name]
**Goal**: [Phase objective]
**Dependencies**: [Previous phases]

### Tasks
- [ ] SDS-T001 [LABEL] Description with path
- [ ] SDS-T002 [LABEL] Description with path
...

**Checkpoint**: [Checkpoint criteria]

## Phase 2: [Phase Name]
...

## Parallel Execution Opportunities

**Within Phase 2**:
```bash
# Can run in parallel:
- SDS-T002 (phase 1 specification)
- SDS-T003 (phase 2 specification)
- SDS-T004 (phase 3 specification)
```

## MVP Scope

**Minimum Viable Specification** (for initial release):
- Phase 1: Core specification ✅
- Phase 2: Critical sub-specifications (P0) ✅

**Deferred to v1.1**:
- Phase 3: Important sub-specifications (P1)
- Phase 4: Nice-to-have sub-specifications (P2)

## Quality Standards

### Specification Size Targets
- **Core specification**: 300-800 lines
- **Sub-specification**: 500-1500 lines
- **Total**: <10,000 lines

### Completeness Criteria
- [ ] All entities have complete schemas
- [ ] All validation rules are enumerated
- [ ] All operations have request/response definitions
- [ ] All use cases have examples
- [ ] All terms in glossary are used consistently

### Cross-Reference Validation
- [ ] Dependencies form DAG (no cycles)
- [ ] All entity references are valid
- [ ] All operation references are valid
- [ ] Version compatibility is documented
```

#### 9. Generate tasks.md File

- Write to `specs/domain/001-{name}-spec/tasks.md`
- Use task template structure
- Include all phases
- Add checkpoint criteria
- Document dependencies
- Show parallel opportunities

#### 9.5. Generate Task Generation Report

**Purpose**: Create detailed metadata about the task breakdown for tracking and analysis.

Prepend this as an HTML comment at the top of `tasks.md`:

```html
<!--
Task Generation Report
======================
Spec: {spec_id} | Date: {ISO_DATE} | Strategy: {Single | Multi-Spec}

Summary:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Total: {total} tasks | By Priority: P0: {p0}, P1: {p1}, P2: {p2}
By Type: Core: {core}, Sub-specs: {sub}, Cross-refs: {cross}, QA: {qa}

Execution:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
5 Phases | Parallel: Phase 2 ({N} specs) + Phase 3 ({N} specs) | Time savings: {percent}%

MVP (v1.0.0):
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Core + P0 sub-specs ({count} tasks) | Effort: {X} days | Files: {count}
Future: v1.1 (P1, +{X}d), v1.2 (P2, +{X}d)

Constitution: {✅ Compliant | ⚠️ Check: {issues}}

Generated by: /metaspec.sds.tasks
-->
```

**Report format rules**:
- Include actual counts (not placeholders)
- List specific dependencies by Task ID
- Calculate parallel opportunities percentage
- Show clear phase boundaries
- Reference constitution principles explicitly

#### 10. Validation

**Check**:
- [ ] All tasks have format: `- [ ] [TID] [P?] [LABEL] Description with path`
- [ ] Task IDs are sequential (SDS-T001, SDS-T002...)
- [ ] Dependencies are clear and acyclic
- [ ] Each phase has checkpoint
- [ ] MVP scope is defined
- [ ] Parallel opportunities identified
- [ ] File paths are correct (specs/domain/00X-{name}/spec.md)

#### 10.5. Consistency Propagation and Impact Analysis

**Purpose**: Ensure task breakdown aligns with plan, specification, and constitution principles.

Check and update dependent files:

#### A. Plan Alignment Check

**Critical**: Tasks MUST match architecture plan.

```bash
# Read plan document
cat specs/domain/{spec_id}/plan.md
```

**Verify**:
- [ ] Task count matches plan estimate (±20%)
- [ ] Sub-specification list matches plan.md
- [ ] Dependencies match plan's execution order
- [ ] Priority levels (P0/P1/P2) align with plan
- [ ] MVP scope aligns with plan's Phase 1

**Action if mismatch**:
- ⚠️ **CRITICAL**: Plan and tasks are out of sync
- Re-read plan.md and regenerate tasks
- Document why there's a mismatch in tasks.md

#### B. Specification Alignment Check

**Critical**: Tasks MUST cover all specification content.

```bash
# Read current specification
cat specs/domain/{spec_id}/spec.md
```

**Verify**:
- [ ] All entities in spec.md have corresponding tasks
- [ ] All operations have tasks for definition
- [ ] All validation rules have tasks for specification
- [ ] All examples have tasks for documentation
- [ ] Specification size estimate matches task scope

**Action if missing coverage**:
- ⚠️ **WARNING**: Tasks incomplete
- Add missing tasks to appropriate phases
- Document additions in Task Generation Report

#### C. Related Domain Specifications Check

**Purpose**: Check for dependencies on other specifications.

```bash
# Find all other domain specifications
find specs/domain/ -name "spec.md" | grep -v "{spec_id}"
```

**For each related spec**:
- **Check** if current tasks reference it
- **Check** if it references current specification
- **Add** cross-reference tasks if needed

**Note to tasks.md**:
```markdown
## Related Specifications
- specs/domain/{related_id}/spec.md - {How they relate}
```

#### D. Toolkit Specifications Check

**Purpose**: Identify if tasks impact toolkit development.

```bash
# Check for toolkit specs
ls specs/toolkit/
```

**If toolkit specs exist**:
- **Note** toolkit specs that may need updates
- **Add** note to tasks.md about toolkit impact

```markdown
## Toolkit Impact
- specs/toolkit/{toolkit_id}/spec.md may need updates after SDS-T00X
```

#### E. MetaSpec Commands Check

**Purpose**: Check if custom slash commands are affected.

```bash
# Check for custom commands
ls .metaspec/commands/ 2>/dev/null || echo "No custom commands"
```

**If custom commands exist**:
- **Check** if they reference this specification
- **Add** update tasks if needed

#### F. Documentation Check

```bash
# Check documentation that may reference this specification
grep -l "{spec_id}" docs/*.md README.md 2>/dev/null || echo "No docs"
```

**If found**:
- **Add** task to update documentation
- **Example**: `SDS-TXXX [DOC] Update {doc_file} with new specification structure`

#### 11. Generate Validation Report

After consistency checks, generate a validation report:

```markdown
## Validation Report

**Task Structure**: ✅ Valid
- All tasks follow format
- Task IDs sequential
- Dependencies acyclic

**Plan Alignment**: {✅ Aligned | ⚠️ Mismatched}
- Task count: {actual} vs {planned} (difference: {±X%})
- {IF mismatch}: Re-generation recommended

**Specification Coverage**: {✅ Complete | ⚠️ Incomplete}
- Entities: {X/Y} covered
- Operations: {X/Y} covered
- Validation rules: {X/Y} covered
{IF incomplete}:
- Missing: {list missing items}

**Constitution Compliance**: ✅ Compliant
- All Part II principles addressed
- Progressive Enhancement: MVP-first approach
- Domain Fidelity: Domain semantics preserved

**Impact Analysis**:
- Related specs: {count} specifications
- Toolkit impact: {Yes | No}
- Documentation updates: {count} files
```

#### 12. Report Completion (Enhanced)

Provide comprehensive summary with validation results and impact analysis:

```
✅ Domain specification task breakdown complete

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

📊 Task Summary:
   Specification: {spec_id}
   Strategy: {Single Spec | Multi-Spec}
   Generated: {date}

   Total Tasks: {total_count}
   - Core Specification: {core_count} tasks
   - Sub-Specifications: {sub_count} tasks ({N} sub-specs)
   - Cross-References: {cross_count} tasks
   - Quality Checks: {quality_count} tasks

   Priority Distribution:
   - P0 (Critical): {p0_count} tasks → MVP
   - P1 (High): {p1_count} tasks → v1.1
   - P2 (Medium): {p2_count} tasks → v1.2

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

✅ Validation Results:

   **Task Structure**: ✅ Valid
   - Format: All tasks follow standard format
   - IDs: Sequential (SDS-T001 to SDS-T{N})
   - Dependencies: Acyclic, {X} sequential, {Y} parallel

   **Plan Alignment**: {✅ Aligned | ⚠️ Deviation}
   - Task count: {actual} vs {planned_estimate} ({±X%})
   {IF deviation > 20%}:
   ⚠️  Significant deviation detected
   - Reason: {Why task count differs from plan}
   - Action: Review plan.md or regenerate tasks
   {END IF}

   **Specification Coverage**: {✅ Complete | ⚠️ Gaps}
   - Entities: {covered}/{total} covered ({percentage}%)
   - Operations: {covered}/{total} covered ({percentage}%)
   - Validation Rules: {covered}/{total} covered ({percentage}%)
   {IF gaps exist}:
   ⚠️  Coverage gaps detected:
   - Missing: {list entities/operations without tasks}
   - Action: Added tasks {task_ids} to address gaps
   {END IF}

   **Constitution Compliance**: ✅ Compliant
   - Progressive Enhancement: MVP-first (P0 → P1 → P2)
   - Minimal Viable Abstraction: {task_count} tasks (not over-engineered)
   - Domain Fidelity: All tasks preserve domain semantics

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

🎯 Impact Analysis:

   **Files Created/Updated**:
   ✅ Created:
   - specs/domain/{spec_id}/tasks.md (this file)

   **Related Files to Review**:
   {IF related_specs > 0}:
   📄 Related Specifications ({count}):
   - specs/domain/{related_id_1}/spec.md - {relationship}
   - specs/domain/{related_id_2}/spec.md - {relationship}
   {END IF}

   {IF toolkit_impact}:
   🔧 Toolkit Impact:
   - specs/toolkit/{toolkit_id}/spec.md - May need updates
   {END IF}

   {IF doc_impact}:
   📚 Documentation Impact ({count} files):
   - {doc_file_1} - References this specification
   - {doc_file_2} - May need updates
   {END IF}

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

🔀 Execution Plan:

   **Sequential Dependencies**:
   1. Phase 1: SDS-T001 (Core) → Must complete first
   {IF multi_spec}:
   2. Phase 2: Core must complete before sub-specs
   3. Phase 4: Sub-specs must complete before cross-refs
   {END IF}

   **Parallel Opportunities**:
   {IF phase2_parallel}:
   ⚡ Phase 2: {N} sub-specs can run in parallel
      - Estimated time saving: {percentage}% ({days} days)
      - Parallelizable: {task_list}
   {END IF}
   {IF phase3_parallel}:
   ⚡ Phase 3: {N} support specs can run in parallel
      - Estimated time saving: {percentage}% ({days} days)
   {END IF}

   **Checkpoints**:
   - After Phase 1: Core specification ready
   {IF multi_spec}:
   - After Phase 2: All sub-specifications ready
   - After Phase 4: Cross-references complete
   {END IF}
   - After Phase {N}: Ready for review

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

📦 Release Planning:

   **MVP (v1.0.0)** - P0 Tasks:
   - Tasks: {p0_count} tasks
   - Scope: Core + Critical sub-specifications
   - Estimated effort: {X} days
   - Target files: {count} specification files

   **v1.1.0** - P1 Tasks:
   - Tasks: {p1_count} tasks
   - Additional effort: +{Y} days
   - Total: {X+Y} days from start

   **v1.2.0** - P2 Tasks:
   - Tasks: {p2_count} tasks
   - Additional effort: +{Z} days
   - Total: {X+Y+Z} days from start

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

📁 Generated Files:
   - specs/domain/{spec_id}/tasks.md (with Task Generation Report)

🔄 Next Steps:
   1. Review tasks.md structure and dependencies
   2. Adjust task priorities if needed (edit tasks.md manually)
   3. Run: /metaspec.sds.implement
      → This will execute tasks in dependency order

⚠️  Follow-up TODOs:
   {IF plan_deviation}:
   - [ ] Review why task count differs from plan.md estimate
   {END IF}
   {IF coverage_gaps}:
   - [ ] Verify added tasks {task_ids} address coverage gaps
   {END IF}
   {IF related_specs}:
   - [ ] Review related specifications for consistency
   {END IF}
   {IF toolkit_impact}:
   - [ ] Update toolkit specifications after implementation
   {END IF}

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

💡 Suggested Commit Message:

   docs(spec): add task breakdown for {spec_id}
   
   Task Summary:
   - Strategy: {Single | Multi}-spec approach
   - Total: {count} tasks ({p0} P0, {p1} P1, {p2} P2)
   - Parallel: {N} sub-specs can run in parallel
   - MVP: {p0_count} tasks for v1.0.0
   
   {IF validation_warnings}:
   Notes:
   - {validation_warning_1}
   - {validation_warning_2}
   {END IF}
```

## Task Templates

### Single Spec Refinement Task Template
```
- [ ] SDS-T00X [REFINE] Expand [Section Name] section:
  - Add: [specific content to add]
  - Clarify: [ambiguous points to resolve]
  - Examples: [number] examples to provide
  - Target: [X]-[Y] lines
```

### Core Specification Task Template
```
- [ ] SDS-T001 [CORE] Refactor to core specification overview:
  - Keep: High-level overview, glossary, use cases
  - Move to sub-specs: Detailed entity definitions
  - Add: Integration points to [N] sub-specifications
  - Add: Dependency diagram
  - Target: 300-800 lines
```

### Phase Specification Task Template
```
- [ ] SDS-T00X [P] [PHASE] Create [Phase Name] specification:
  - File: specs/domain/00X-{phase}-spec/spec.md
  - Dependencies: domain/001-core-spec
  - Entities: [List phase-specific entities]
  - Operations: [List phase operations]
  - Validation: [Phase-specific rules]
  - Examples: [Number] examples
  - Target: 500-1500 lines
```

### Component Specification Task Template
```
- [ ] SDS-T00X [P] [COMPONENT] Create [Component Type] specification:
  - File: specs/domain/00X-{component}-spec/spec.md
  - Dependencies: domain/001-core-spec
  - Purpose: [Component purpose]
  - Interface: [Component interface definition]
  - Registration: [How components are registered]
  - Validation: [Component-specific rules]
  - Examples: [Number] examples
  - Target: 500-1500 lines
```

### Supporting Specification Task Template
```
- [ ] SDS-T00X [SUPPORT] Create [Support System] specification:
  - File: specs/domain/00X-{support}-spec/spec.md
  - Dependencies: domain/001-core-spec, [others]
  - Purpose: [Cross-cutting concern addressed]
  - Interfaces: [System interfaces]
  - Integration: [How it integrates with entities]
  - Examples: [Number] examples
  - Target: 300-800 lines
```

## Important Notes

1. **Specification-based organization**
   - Not code-based (that's SDD)
   - Organize by specification concerns (phases, components, layers)
   - Each specification is independently readable

2. **Documentation quality matters**
   - Each specification should be comprehensive
   - Examples are mandatory, not optional
   - Validation rules must be complete

3. **Follow architecture plan**
   - Tasks implement plan.md structure
   - Respect dependencies from plan
   - Follow priority levels (P0, P1, P2)

4. **Parallel execution**
   - Sub-specifications can be written in parallel
   - Different writers can work on different specs
   - Core specification must be complete first

5. **MVP first**
   - Focus on P0 sub-specifications
   - Defer P1/P2 specs to later versions
   - Get working specification quickly

## Example: E-commerce Order Specification Tasks

### Phase 1: Core Specification
```
- [ ] SDS-T001 [CORE] Refactor to core specification overview
  - Keep: Overview, glossary, use cases
  - Move: Phase details to phase specifications
  - Add: 7 phase integration points
  - Target: 650 lines
```

### Phase 2: Lifecycle Phase Specifications (P0)
```
- [ ] SDS-T002 [P] [PHASE] Create order-creation specification
  - File: specs/domain/002-order-creation-spec/spec.md
  - Order initialization rules
  - Cart to order transformation
  - Customer validation
  - Target: 800 lines

- [ ] SDS-T003 [P] [PHASE] Create payment-processing specification
  - File: specs/domain/003-payment-processing-spec/spec.md
  - Payment method specifications
  - Transaction flow
  - Security requirements
  - Target: 950 lines

- [ ] SDS-T004 [P] [PHASE] Create fulfillment specification
  - File: specs/domain/004-fulfillment-spec/spec.md
  - Inventory allocation
  - Pick-pack-ship workflow
  - Quality checks
  - Target: 850 lines

[... SDS-T005-008 for shipping, delivery, returns, refunds phases ...]
```

**Checkpoint**: All 7 phase specifications complete (600-1000 lines each)

### Phase 3: Supporting Specifications (P1)
```
- [ ] SDS-T009 [SUPPORT] Create payment-gateway specification
  - File: specs/domain/009-payment-gateway-spec/spec.md
  - Gateway integration patterns
  - Webhook specifications
  - Retry mechanisms
  - Target: 700 lines

- [ ] SDS-T010 [SUPPORT] Create inventory-sync specification
  - File: specs/domain/010-inventory-sync-spec/spec.md
  - Real-time sync mechanisms
  - Conflict resolution
  - Cache strategies
  - Target: 650 lines

- [ ] SDS-T011 [SUPPORT] Create notification specification
  - File: specs/domain/011-notification-spec/spec.md
  - Email/SMS templates
  - Trigger conditions
  - Delivery guarantees
  - Target: 550 lines
```

**Checkpoint**: All supporting specifications complete

### Phase 4: Cross-Reference Validation
```
- [ ] SDS-T012 [REFINE] Validate core specification integration
  - Check 10 sub-spec references
  - Verify dependency DAG
  - Update version compatibility

- [ ] SDS-T013 [REFINE] Add cross-references
  - Phase specifications → Core specification
  - Phase specifications → Supporting specifications
  - Bidirectional references

- [ ] SDS-T014 [REFINE] Ensure consistency
  - Glossary terms usage
  - Entity naming (Order, Payment, Shipment)
  - Validation rule references
```

**Checkpoint**: All specifications integrated and consistent


