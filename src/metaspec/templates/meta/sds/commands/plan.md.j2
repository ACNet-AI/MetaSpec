---
description: Plan specification structure by analyzing complexity and organizing sub-specifications
---

## User Input

```text
$ARGUMENTS
```

You **MUST** consider the user input before proceeding (if not empty).

## Outline

**Goal**: Analyze specification complexity and plan the specification structure, including identifying necessary sub-specifications and their dependencies.

**Important**: This command runs AFTER `/metaspec.sds.specify` when initial specification concept is defined. It determines whether the specification needs to be split into multiple sub-specifications.

### Execution Flow

#### 1. Load Specification Context

**Step 1a: Determine Current Specification**

Get current specification from Git branch or SPECIFY_FEATURE:
```bash
# From Git branch
current_spec=$(git branch --show-current)
# Or from environment variable
current_spec=$SPECIFY_FEATURE

# Example: "003-payment-processing"
```

**Step 1b: Read Domain Specification**

Read the spec.md for current specification:
```bash
# Read the spec.md
cat specs/domain/${current_spec}/spec.md
```

**Step 1c: Extract Metadata** (from YAML frontmatter)

Parse frontmatter to understand context:
```yaml
---
spec_id: 003-payment-processing
parent: 001-order-spec
root: 001-order-spec
type: parent  # or leaf or root
---
```

**Store context**:
- `current_id`: spec_id (e.g., "003-payment-processing")
- `parent_id`: parent (e.g., "001-order-spec" or null)
- `root_id`: root (e.g., "001-order-spec")
- `current_type`: type (e.g., "parent", "leaf", "root")

**This tells us**:
- Where this specification is in the hierarchy
- Can inform numbering for sub-specifications
- Understand if this is already a sub-specification (can have sub-sub-specifications)

**Step 1d: Extract Specification Content**

From spec.md body, extract:
- Specification name and domain
- Core entities defined
- Operations/interfaces
- Lifecycle phases (if any)
- Validation rules
- Use cases
- Current document length (line count)

#### 2. Analyze Specification Complexity

**Complexity Assessment Criteria**:

1. **Entity Count**:
   - Simple: 1-5 entities
   - Medium: 6-15 entities
   - Complex: 16+ entities
   
2. **Lifecycle Phases**:
   - None: Stateless specification
   - Few (1-3): Simple workflow
   - Many (4+): Complex lifecycle requiring phase-specific specs

3. **Document Length**:
   - Small: <500 lines
   - Medium: 500-1500 lines
   - Large: 1500+ lines (⚠️ Consider splitting)

4. **Domain Scope**:
   - Narrow: Single concern (file operations, authentication)
   - Broad: Multiple concerns (full development lifecycle, enterprise integration)

5. **Interdependencies**:
   - Standalone: No external specifications
   - Dependent: References other specifications
   - Ecosystem: Part of multi-specification system

**Decision Matrix**:

| Complexity Level | Document Length | Recommendation |
|-----------------|----------------|----------------|
| Simple | <500 lines | ✅ Single spec sufficient |
| Medium | 500-1500 lines | ⚠️ Consider sub-specifications for major sections |
| Complex | 1500+ lines | ❌ MUST split into sub-specifications |

**Calculate Complexity Score**:
```
complexity_score = 
  (line_count / 600) * 0.4 +
  (entity_count / 6) * 0.3 +
  (operation_count / 12) * 0.3

If complexity_score < 1.0: KEEP_SINGLE (< 1500 lines typically)
If complexity_score < 2.0: CONSIDER_SPLIT (1500-3000 lines)
If complexity_score >= 2.0: MUST_SPLIT (> 3000 lines)

Note: Adjusted to align with 1500-line threshold mentioned in Decision Matrix
```

#### 3. Make Decision

**Output format (both cases)**:
```
Specification Analysis: {spec_id}

📊 Complexity Assessment:
   - Lines: {line_count}
   - Entities: {entity_count}
   - Operations: {operation_count}
   - Complexity Score: {score:.2f}
```

---

**If complexity_score < 1.0** (Simple):

**DO NOT create plan.md**. Instead, output:

```
✅ Decision: KEEP SINGLE SPECIFICATION

Reason: Specification is manageable (complexity: {score:.2f})

This specification does not need to be split into sub-specifications.
It is a **leaf specification** - a complete, self-contained specification.

Next Steps:
✅ Specification is ready
✅ No need for /metaspec.sds.tasks or /metaspec.sds.implement
✅ Proceed to use this specification as-is

(No plan.md file created)
```

**Exit without creating plan.md** ← IMPORTANT

---

**If complexity_score >= 1.0** (Medium or Complex):

**DO create plan.md**. Output:

```
❌ Decision: SPLIT INTO SUB-SPECIFICATIONS

Reason: {complexity_score >= 1.0: moderate} or {>= 2.0: high complexity}

This specification should be split into sub-specifications for better maintainability.

Next Steps:
1. Review the generated plan.md
2. Run /metaspec.sds.tasks to break down work
3. Run /metaspec.sds.implement to create sub-specifications

Generating plan.md...
```

Continue to Step 4 to generate plan.md.

---

#### 4. Identify Sub-Specification Pattern (Only if splitting)

**Common Sub-Specification Patterns**:

##### Pattern A: Lifecycle Phase Specifications

**When to use**: Specification defines 4+ lifecycle phases

**Example** (Order Management Specification):
```
Core Specification (001-order-management-spec)
  ↓ References
Phase Specifications:
  - 002-order-creation-spec
  - 003-payment-processing-spec
  - 004-fulfillment-spec
  - 005-shipping-spec
  - 006-delivery-spec
  - 007-returns-spec
```

**Other examples**: Development workflows, deployment pipelines, data processing stages

**Benefits**:
- Each phase has detailed methodology
- Phase-specific validation rules
- Independent evolution of phases

##### Pattern B: Component Type Specifications

**When to use**: Specification defines multiple component types (3+)

**Example** (Plugin System Specification):
```
Core Specification (001-plugin-system-spec)
  ↓ References
Component Specifications:
  - 002-plugin-interface-spec
  - 003-hook-system-spec
  - 004-event-bus-spec
  - 005-configuration-spec
```

**Benefits**:
- Deep component specifications
- Component-specific validation
- Modular specification evolution

##### Pattern C: Cross-Cutting Concern Specifications

**When to use**: Specification has supporting systems used across entities

**Example** (API Specification):
```
Core Specification (001-api-spec)
  ↓ References
Supporting Specifications:
  - 002-authentication-spec
  - 003-error-handling-spec
  - 004-versioning-spec
  - 005-rate-limiting-spec
```

**Benefits**:
- Reusable across entities
- Consistent patterns
- Clear separation of concerns

##### Pattern D: Layered Architecture Specifications

**When to use**: Specification has distinct architectural layers

**Example** (Communication Specification):
```
Core Specification (001-messaging-spec)
  ↓ References
Layer Specifications:
  - 002-transport-layer-spec (HTTP, WebSocket, gRPC)
  - 003-message-format-spec (JSON, Protobuf)
  - 004-security-layer-spec (TLS, Authentication)
  - 005-reliability-spec (Retry, Circuit Breaker)
```

**Benefits**:
- Layer independence
- Technology alternatives
- Clear boundaries

#### 4. Design Specification Architecture

**Create architecture plan**:

```markdown
# Specification Architecture Plan

## Overview
- **Specification Name**: {name}
- **Domain**: {domain}
- **Complexity**: [Simple/Medium/Complex]
- **Primary Pattern**: [Lifecycle/Component/CrossCutting/Layered]

## Core Specification (001-{name}-spec)

**Purpose**: High-level overview and integration point

**Scope**:
- Specification overview and problem statement
- Glossary of key terms
- Use cases
- Entity overview (high-level, not detailed)
- Integration points to sub-specifications
- Validation overview

**Size**: 300-800 lines (overview only)

## Sub-Specifications

### Sub-Spec 1: {name} (002-{name})

**Purpose**: [specific concern]

**Dependencies**: 
- Depends on: 001-core-spec

**Scope**:
- [Entity/Phase/Component] detailed definition
- Detailed schemas and field specifications
- Specific validation rules
- Concrete examples
- Error handling specifics

**Estimated Size**: [X] lines

**Priority**: P0 (Critical) / P1 (Important) / P2 (Nice-to-have)

### Sub-Spec 2: {name} (003-{name})

[Same structure as Sub-Spec 1]

## Dependency Graph

```mermaid
graph TD
    001[Core Specification] --> 002[Sub-Spec 1]
    001 --> 003[Sub-Spec 2]
    002 --> 005[Sub-Spec 4]
    003 --> 005
    001 --> 004[Sub-Spec 3]
```

## Implementation Order

**Phase 1: Core Foundation**
- [ ] 001-core-spec (base specification)

**Phase 2: Primary Specifications** (P0)
- [ ] 002-{name} (critical dependency)
- [ ] 003-{name} (critical dependency)

**Phase 3: Supporting Specifications** (P1)
- [ ] 004-{name} (important feature)
- [ ] 005-{name} (important feature)

**Phase 4: Advanced Specifications** (P2)
- [ ] 006-{name} (nice-to-have)

## Cross-References

**How sub-specifications reference core**:
```markdown
## Dependencies
- **Depends on**: domain/001-core-spec
- **Uses entities from**: Core Specification (Server, Client)
- **Extends validation from**: Core Specification Section 5.2
```

## Success Criteria

- [ ] Core specification defines integration points clearly
- [ ] Each sub-specification has clear scope
- [ ] Dependencies are acyclic (no circular references)
- [ ] Total specification size manageable (<10 sub-specs ideal)
- [ ] Each sub-specification can evolve independently
```

#### 5. Refinement: Evaluate Alternatives

**Question to consider**:

1. **Is splitting necessary?**
   - Current spec length: [X] lines
   - Is it already readable and maintainable?
   - Would splitting add unnecessary complexity?

2. **Is the split logical?**
   - Do sub-specifications have clear boundaries?
   - Are dependencies minimal and clear?
   - Can each sub-spec stand alone?

3. **Is this future-proof?**
   - Can new phases/components be added easily?
   - Does the structure support specification evolution?
   - Are there natural extension points?

**Recommendation**:
- ✅ Proceed with split if specification is 1500+ lines
- ⚠️ Defer split if specification is 500-1500 lines (manageable as single spec)
- ✅ Keep single spec if specification is <500 lines

#### 6. Generate plan.md

**Output location**: `specs/domain/001-{name}-spec/plan.md`

**Structure**:
```markdown
# [Specification Name] - Architecture Plan

**Version**: 1.0.0  
**Created**: {date}  
**Status**: Draft

---

## Specification Complexity Assessment

### Metrics
- **Entity Count**: [N] entities
- **Lifecycle Phases**: [N] phases
- **Document Length**: [N] lines
- **Domain Scope**: [Narrow/Broad]
- **Interdependencies**: [Standalone/Dependent/Ecosystem]

### Complexity Rating
[Simple/Medium/Complex]

### Recommendation
[Keep single spec / Split into sub-specifications]

**Rationale**: {Why this decision}

---

## Specification Architecture (IF SPLITTING)

[Include sections from Step 4: Design Specification Architecture]

---

## Specification Structure (IF KEEPING SINGLE SPEC)

### Suggested Organization
```markdown
001-{name}-spec/spec.md:
  1. Specification Overview (lines 1-50)
  2. Glossary (lines 51-100)
  3. Use Cases (lines 101-200)
  4. Core Entities (lines 201-500)
     - Entity 1 (detailed)
     - Entity 2 (detailed)
     - ...
  5. Lifecycle/Workflow (lines 501-800)
  6. Operations (lines 801-1000)
  7. Validation Rules (lines 1001-1200)
  8. Examples (lines 1201-1400)
```

---

## Implementation Strategy

[From Step 4: Implementation Order]

---

## Quality Guidelines

### Specification Size Targets
- **Core specification**: 300-800 lines (overview)
- **Sub-specification**: 500-1500 lines (detailed)
- **Total system**: <10,000 lines

### Maintainability Principles
1. Each specification should be readable in <30 minutes
2. Dependencies should form a DAG (no cycles)
3. Common patterns should be in core specification
4. Each sub-spec should be independently testable

### Evolution Strategy
- Core specification changes require major version bump
- Sub-specification changes can be independent
- Deprecation policy: 12 months notice
- Migration guides required for breaking changes
```

#### 7. Generate Planning Report (NEW)

**Purpose**: Provide comprehensive planning summary.

**After generating plan.md**, create HTML comment and prepend to file:

```html
<!--
Specification Planning Report
=============================
Spec: {spec_id} | Date: {ISO_DATE}
Decision: {KEEP_SINGLE | SPLIT} | Complexity: {Simple | Medium | Complex} (score: {score:.2f})

Metrics:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Lines: {line_count} | Entities: {entity_count} | Operations: {operation_count}

{IF SPLIT}:
Sub-Specs: {count} (P0: {count}, P1: {count}, P2: {count})
Pattern: {Lifecycle | Component | CrossCutting | Layered}
Phases: Phase 1 (Core) → Phase 2 (Primary) → Phase 3 (Supporting) → Phase 4 (Advanced)

{IF KEEP_SINGLE}:
Organization: Single spec with {section_count} sections ({lines} lines)

Next: {IF SPLIT}Tasks → Implement sub-specs{END}{IF KEEP_SINGLE}Proceed with development{END}

Generated by: /metaspec.sds.plan
-->
```

#### 8. Validation Checklist (NEW)

**Purpose**: Ensure planning quality.

Run these critical validation checks:

- [ ] **Complexity Assessment**: Data-driven (metrics + score), decision matrix applied
- [ ] **Decision Justification**: Clear rationale for SPLIT or KEEP_SINGLE
- [ ] **Sub-Specs** (if SPLIT): Logical boundaries, no overlap, dependencies form DAG, priorities assigned
- [ ] **Implementation Phases**: Logical order, dependencies honored
- [ ] **Constitution Compliance**: Minimal abstraction (split only if >1500 lines), domain specificity
- [ ] **Maintainability**: Readable (<30 min), independent, testable
- [ ] **Planning Report**: Prepended at top of plan.md
- [ ] **File Path**: specs/domain/{spec_id}/plan.md

### Generate Validation Report

```markdown
Planning Validation Report
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Planning Quality: ✅ PASSED ({score}/7 checks)
- Complexity assessment: ✅
- Decision justification: ✅
{IF SPLIT}:
- Sub-spec boundaries: ✅
- Dependencies: ✅
- Scope definition: ✅
- Implementation phases: ✅
- Pattern appropriateness: ✅
{IF KEEP_SINGLE}:
- Organization structure: ✅

Constitution Compliance: ✅ PASSED (2/2 principles)
- Minimal abstraction: ✅
- Domain specificity: ✅

Maintainability: ✅ PASSED (4/4 checks)
- Readability: ✅
- Independence: ✅
- Testability: ✅
- Documentation: ✅

Overall: {IF all pass: ✅ PLAN APPROVED | IF issues: ⚠️  NEEDS REFINEMENT}

{IF issues}:
⚠️  Issues to Address:
- {Issue 1}
- {Issue 2}

💡 Recommendations:
- {Recommendation 1}
- {Recommendation 2}
```

#### 9. Finalize Plan

**If plan looks good**:
- Prepend Planning Report to plan.md
- Save to `specs/domain/001-{name}-spec/plan.md`
- Proceed to `/metaspec.sds.tasks`

**If plan needs refinement**:
- Discuss issues with user
- Adjust sub-specification boundaries
- Re-evaluate dependencies
- Regenerate plan.md with updates
- Re-run validation

#### 10. Report Completion (Enhanced)

```
✅ Specification architecture plan complete

📁 Location:
   specs/domain/001-{name}-spec/plan.md

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

📋 Planning Assessment:
   Specification: {name}
   Complexity: {Simple (< 1.0) | Medium (1.0-2.0) | Complex (> 2.0)}
   Complexity Score: {score:.2f}
   Decision: {KEEP_SINGLE | SPLIT}

   Metrics:
   - Document Length: {line_count} lines
   - Entity Count: {entity_count}
   - Operation Count: {operation_count}

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

📊 Architecture Summary:

{IF KEEP_SINGLE}:
   Type: Single Specification
   - Estimated size: {lines} lines
   - Sections: {section_count}
   - Maintainability: High (manageable as single spec)
   - Rationale: {Complexity score < 1.0 | Document length < 1500 lines}

{IF SPLIT}:
   Type: Modular Architecture
   - Core Specification: 001-{name}-spec (overview)
   - Sub-Specifications: {count} sub-specs
     * P0 (Critical): {count} specs
     * P1 (Important): {count} specs
     * P2 (Nice-to-have): {count} specs
   - Pattern: {Lifecycle | Component | CrossCutting | Layered}
   - Total Estimated Size: {lines} lines across {count} files
   - Maintainability: High (modular, independent evolution)
   - Rationale: {Complexity score >= 1.0 | Document length > 1500 lines}

   Sub-Specifications:
   {FOR each sub-spec}:
   - {number}-{name}
     * Priority: {P0 | P1 | P2}
     * Estimated Size: {lines} lines
     * Dependencies: {list or "None"}
   ...

   Implementation Phases:
   - Phase 1 (Core): {spec list}
   - Phase 2 (Primary): {spec list}
   - Phase 3 (Supporting): {spec list}
   {IF P2 exists}:
   - Phase 4 (Advanced): {spec list}

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

✅ Validation Results: {IF all pass: APPROVED | IF issues: NEEDS REFINEMENT}

   Planning Quality: ✅ ({score}/7 checks)
   - Complexity assessment: ✅
   - Decision justification: ✅
   {IF SPLIT}:
   - Sub-spec boundaries: ✅
   - Dependencies: ✅
   - Scope definition: ✅
   - Implementation phases: ✅
   - Pattern appropriateness: ✅
   {IF KEEP_SINGLE}:
   - Organization structure: ✅

   Constitution Compliance: ✅ (2/2 principles)
   - Minimal abstraction: ✅
   - Domain specificity: ✅

   Maintainability: ✅ (4/4 checks)
   - Readability: ✅
   - Independence: ✅
   - Testability: ✅
   - Documentation: ✅

{IF issues}:
   ⚠️  Issues to Address:
   - {Issue 1}
   - {Issue 2}

{IF recommendations}:
   💡 Recommendations:
   - {Recommendation 1}
   - {Recommendation 2}

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

🔄 Next Steps:

{IF SPLIT}:
   Immediate:
   1. Review sub-specification boundaries with stakeholders
   2. Verify dependency graph is acyclic
   3. Confirm implementation phase priorities
   
   Development:
   - Run /metaspec.sds.tasks to create implementation tasks
   - Run /metaspec.sds.implement to generate sub-specifications
   - Track progress for each sub-spec (P0 → P1 → P2)

{IF KEEP_SINGLE}:
   Immediate:
   1. Review proposed specification structure
   2. Confirm section organization
   
   Development:
   - Proceed with specification development
   - No splitting needed (manageable as single spec)
   - Can add sub-specifications later if complexity grows

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

💡 Suggested commit message:
   {IF SPLIT}:
   docs(plan): add modular architecture plan for {spec-name}
   
   - Split into {count} sub-specifications
   - Pattern: {pattern}
   - Implementation phases: {phase_count}
   - Total estimated size: {lines} lines
   
   {IF KEEP_SINGLE}:
   docs(plan): add specification plan for {spec-name}
   
   - Keep as single specification
   - Estimated size: {lines} lines
   - Organized into {section_count} sections
```

## Key Principles

1. **Data-Driven Decisions**
   - Use objective metrics (entity count, document length)
   - Don't split prematurely
   - Consider maintainability vs. fragmentation trade-offs

2. **Clear Boundaries**
   - Each sub-specification has distinct responsibility
   - Minimal cross-references between sub-specs
   - Dependencies form a clear hierarchy

3. **Future-Proof**
   - Structure supports adding new phases/components
   - Evolution doesn't require restructuring
   - Extension points are explicit

4. **Pragmatic**
   - Split only when necessary (1500+ lines)
   - Keep related concerns together
   - Balance granularity with usability

## Examples

### Example 1: Simple Specification (Keep Single Spec)

**Authentication Specification**:
- Entities: 3 (User, Token, Session)
- Document length: 450 lines
- **Decision**: Keep as single spec
- **Rationale**: Small, focused domain; splitting would add unnecessary complexity

### Example 2: Complex Specification (Split)

**E-commerce Order Specification**:
- Entities: 15+ (Order, Payment, Inventory, Shipping, Customer, etc.)
- Lifecycle phases: 7 (Creation → Returns)
- Document length: 2800+ lines
- **Decision**: Split into 12 sub-specifications
  - Core: 001-order-spec (overview)
  - Phases: 002-008 (phase-specific specifications)
  - Support: 009-012 (payment, inventory, notification, audit)
- **Rationale**: Each phase has complex business rules; single spec would be unmanageable

**Alternative example**: Large development workflow specification (6+ phases), healthcare patient journey specification (10+ stages)

### Example 3: Medium Specification (Defer Split)

**File System Specification**:
- Entities: 8 (File, Directory, Permission, etc.)
- Document length: 900 lines
- **Decision**: Keep single spec for now, plan for future split
- **Rationale**: Currently manageable; can split later if grows beyond 1500 lines

## Important Notes

1. **Splitting is a design decision, not implementation**
   - Planning doesn't create files
   - `/metaspec.sds.implement` actually writes specifications
   - Plan guides the implementation process

2. **Avoid premature splitting**
   - Start with single spec unless clearly necessary
   - Split when specification exceeds 1500 lines
   - Splitting too early adds complexity

3. **Think about consumers**
   - Will users read the entire specification?
   - Do different audiences need different specifications?
   - Is modular documentation valuable?

4. **Consider evolution**
   - Will parts of the specification evolve at different rates?
   - Do some sections need stricter stability guarantees?
   - Is independent versioning valuable?


