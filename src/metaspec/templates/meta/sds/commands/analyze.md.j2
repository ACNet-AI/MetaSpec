---
description: Perform specification quality analysis - read-only analysis for specification consistency
---

## User Input

```text
$ARGUMENTS
```

You **MUST** consider the user input before proceeding (if not empty).

## Goal

Identify inconsistencies, ambiguities, and gaps in domain specifications. **READ-ONLY** analysis - no file modifications.

**Focus**: Domain specification quality (WHAT the specification is), NOT toolkit implementation (HOW to implement).

## Operating Constraints

**STRICTLY READ-ONLY**: Do NOT modify any files. Output structured analysis report only.

**Constitution Authority**: constitution.md defines specification design principles. Violations are CRITICAL.

## Operating Principles

### Context Efficiency (inspired by spec-kit)

- **Minimal high-signal tokens**: Focus on actionable findings, not exhaustive documentation
- **Progressive disclosure**: Load artifacts incrementally; don't dump all content into analysis
- **Token-efficient output**: Limit findings to 50 items; aggregate remainder in overflow summary
- **Deterministic results**: Rerunning without changes should produce consistent IDs and counts

## Execution Flow

### 1. Parse Analysis Mode

**CRITICAL**: Determine analysis mode from user input before proceeding.

#### Mode Detection (from $ARGUMENTS)

Parse user intent to select appropriate analysis mode:

| User Input Keywords | Mode Selected | Purpose |
|-------------------|---------------|---------|
| "quick", "fast", "lightweight", "brief", "rapid" | **Quick Mode** | Fast structural integrity checks (< 2 min) |
| "only [dimension]", "just [dimension]", "check [dimension]", "focus on [dimension]" | **Focused Mode** | Deep dive into specific dimension |
| Empty, "full", "complete", "comprehensive", or other | **Full Mode** | Complete 10-dimension analysis (default) |

#### Mode Descriptions

**Quick Mode** ⚡ (< 2 min, ~500 tokens):
- Purpose: Fast structural integrity validation
- Checks: 3 essential dimensions only
  1. Frontmatter Validation
  2. Cross-Reference Integrity  
  3. Dependency Graph Check
- Skip: Deep semantic analysis (7 dimensions)
- Use when: Daily development, quick validation, pre-commit checks

**Focused Mode** 🎯 (3-5 min, dimension-specific):
- Purpose: Deep analysis of single dimension
- Checks: Only the specified dimension
- Dimension mapping:
  - "entity", "entities" → Entity Definition Quality (A)
  - "validation", "rules" → Validation Rule Completeness (B)
  - "operations", "ops" → Operations Completeness (C)
  - "schema", "consistency" → Schema Consistency (D)
  - "errors", "error-handling" → Error Handling (E)
  - "examples" → Examples Completeness (F)
  - "dependencies", "deps", "cross-ref" → Cross-Entity Dependencies (G)
  - "constitution", "principles" → Constitution Alignment (H)
  - "ambiguity", "vague" → Ambiguity Detection (I)
  - "terminology", "naming" → Terminology Consistency (J)
  - "artifacts", "cross-artifacts" → Cross-Artifact Consistency (K)
  - "workflow", "workflows", "user-journey" → Workflow Completeness (L) ⭐ NEW (v0.7.0+)
- Use when: Fixing specific issues, targeted improvement

**Full Mode** 📊 (5-10 min, comprehensive):
- Purpose: Complete specification quality analysis
- Checks: All 12 dimensions (A-L) ⭐ Updated (v0.7.0+)
- Use when: Major releases, complete review, initial analysis

**Mode selection example**:
```
User: "/metaspec.sds.analyze quick" → Quick Mode
User: "/metaspec.sds.analyze check entities" → Focused Mode (Entity Quality)
User: "/metaspec.sds.analyze" → Full Mode (default)
```

**Display selected mode**:
```
🔍 Analysis Mode: Quick Mode ⚡
📋 Checking: Frontmatter, Cross-References, Dependencies
⏱️  Expected time: < 2 minutes
```

---

### 2. Check for existing analysis

**CRITICAL**: Before generating, check if analysis already exists:

```bash
ls specs/domain/XXX-name/analysis/
```

**If analysis exists**, ask user:

| Mode | Action | When to Use |
|------|--------|-------------|
| **update** | Update results, add iteration section | Specification improved, want to track progress |
| **new** | Create new analysis (backup existing) | Complete restart, different focus |
| **append** | Add supplementary analysis | Existing analysis still valid, new aspect |

**Default**: If user says "re-run", "verify improvement" → choose **update** mode

**If NO analysis exists** → proceed to step 2

---

### 2. Load Specification Artifacts

**Required Files**:
- `specs/domain/XXX-{name}/spec.md` - Domain specification
- `/memory/constitution.md` - Specification design principles

**Optional Files**:
- `specs/domain/XXX-{name}/README.md` - Specification overview
- `specs/domain/XXX-{name}/examples/` - Specification examples
- `specs/domain/XXX-{name}/checklists/` - Specification quality checklists

**DO NOT load** (these are toolkit-specific):
- ❌ plan.md (toolkit architecture)
- ❌ tasks.md (implementation tasks)
- ❌ Any files in `specs/toolkit/`

### 3. Build Semantic Models

**Create internal representations** (do not include raw artifacts in output):

**From spec.md**:
- Entity inventory: `{name, fields[], requiredFields[], hasExamples, hasValidation}`
- Operation inventory: `{name, hasRequestSchema, hasResponseSchema, hasErrorCases}`
- Validation rule inventory: `{entity, field, rule, isSpecific, errorCode}`
- Error code inventory: `{code, description, hasExample}`

**From constitution.md**:
- Principle inventory: `{name, type: MUST/SHOULD, category, checkPattern}`

**Analysis focus**: Extract minimal context needed for quality checks, not full content.

### 4. Quick Mode Checks (if Quick Mode selected)

**IF mode = Quick Mode**, execute ONLY these 3 checks and skip to Step 6 (report generation):

#### Quick-A. Frontmatter Validation

**Purpose**: Verify YAML frontmatter structure and required fields

**Check each spec.md**:
```bash
# Extract frontmatter
yq eval '.' specs/domain/*/spec.md

# Verify required fields
- spec_id: Must exist, format: NNN-name
- parent: Must exist (or null if root)
- root: Must exist (spec_id of root specification)
- type: Must be 'root' | 'parent' | 'leaf'
```

**Validate logic**:
- ✅ Root specs: parent = null, type = root
- ✅ Leaf specs: parent != null, type = leaf
- ✅ Parent specs: parent != null, type = parent, has sub-specifications
- ✅ spec_id matches directory name
- ✅ root reference points to valid spec

**Report**:
```
✅ PASS: All 5 specs have valid frontmatter
OR
❌ FAIL: 2 frontmatter issues found
  - specs/domain/003-payment/spec.md: Missing 'parent' field
  - specs/domain/005-shipping/spec.md: spec_id '004-shipping' doesn't match directory name
```

#### Quick-B. Cross-Reference Integrity

**Purpose**: Verify all internal links resolve correctly

**Extract all references**:
```bash
# Find all markdown links to other specs
grep -r "\[.*\](\.\./.*/spec\.md)" specs/domain/

# Pattern: [Link Text](../XXX-name/spec.md)
# Pattern: [Link Text](../XXX-name/spec.md#section)
```

**Verify each reference**:
- ✅ Target file exists
- ✅ If anchor specified (#section), verify section exists in target
- ✅ Relative path resolves correctly

**Report**:
```
✅ PASS: All 12 cross-references valid
OR
❌ FAIL: 3 broken references found
  - specs/domain/002-order/spec.md:45
    → [Payment Spec](../010-payment/spec.md)
    → ERROR: File ../010-payment/spec.md does not exist
  
  - specs/domain/003-payment/spec.md:78
    → [Order Entity](../002-order/spec.md#entity-order)
    → ERROR: Anchor #entity-order not found in target
```

#### Quick-C. Dependency Graph Check

**Purpose**: Verify parent-child relationships and detect cycles

**Build dependency graph**:
```
For each spec in specs/domain/*/:
  Extract: spec_id, parent, root
  Build graph: spec_id → parent
```

**Validate graph**:
- ✅ All parent references point to existing specs
- ✅ All root references point to existing specs
- ✅ No circular dependencies (A → B → A)
- ✅ Root specs have no parent
- ✅ Leaf specs have no children

**Report**:
```
✅ PASS: Dependency graph valid (5 specs, 1 root, 3 parents, 1 leaf)

Specification Tree:
001-order-spec (root)
  ├── 002-order-creation (leaf)
  ├── 003-payment (parent)
  │   ├── 013-credit-card (leaf)
  │   └── 014-digital-wallet (leaf)
  └── 004-fulfillment (leaf)

OR

❌ FAIL: Dependency issues found
  - specs/domain/005-shipping/spec.md: parent='099-logistics' but spec doesn't exist
  - Circular dependency detected: 002 → 005 → 002
```

**Quick Mode Report Format**:
```markdown
# Quick Analysis Report ⚡

**Date**: [DATE] | **Mode**: Quick | **Specification**: [NAME]

**Summary**:
- ✅ Frontmatter: Valid (5/5 specs)
- ✅ Cross-References: Valid (12/12 links)  
- ✅ Dependencies: Valid (no cycles, 5 specs)

**Total Time**: 45 seconds

---

## ✅ All Structural Checks Passed

**Next Steps**:
- For detailed quality analysis, run: `/metaspec.sds.analyze`
- For specific dimension check, run: `/metaspec.sds.analyze check [dimension]`
```

**If issues found in Quick Mode**:
```markdown
# Quick Analysis Report ⚡

**Date**: [DATE] | **Mode**: Quick | **Specification**: [NAME]

**Summary**:
- ✅ Frontmatter: Valid (5/5 specs)
- ❌ Cross-References: 3 broken links found
- ⚠️  Dependencies: 1 issue found

**Total Issues**: 4 (3 broken links, 1 dependency issue)

---

## ❌ Structural Issues Found

### Cross-Reference Issues (3)

| File | Line | Issue | Target |
|------|------|-------|--------|
| 002-order/spec.md | 45 | File not found | ../010-payment/spec.md |
| 003-payment/spec.md | 78 | Anchor not found | ../002-order/spec.md#entity-order |
| 005-shipping/spec.md | 102 | File not found | ../020-tracking/spec.md |

**Recommendation**: Fix broken links before proceeding

### Dependency Issues (1)

- specs/domain/005-shipping/spec.md: parent='099-logistics' doesn't exist

**Recommendation**: Update frontmatter with correct parent spec_id

---

## 🔄 Next Steps

1. **Fix issues above** (estimated time: 10-15 min)
2. **Re-run quick check**: `/metaspec.sds.analyze quick`
3. **When structural issues resolved**, run full analysis: `/metaspec.sds.analyze`
```

**END Quick Mode** - Skip to Step 6 (Generate Report)

---

### 5. Full/Focused Mode Detection Passes

**IF mode = Full Mode OR Focused Mode**, execute these detection passes:

**Note**: In Focused Mode, only execute the selected dimension.

#### A. Entity Definition Quality

**Check each entity**:
- ✅ Entity has clear purpose statement
- ✅ All fields have type specified
- ✅ Required vs optional is clear
- ✅ Field descriptions are specific (not vague)
- ✅ Field constraints documented (enum, format, range)
- ✅ Example values provided

**Report**:
```
❌ MEDIUM: Entity 'Server' field 'capabilities' missing type specification [spec.md §Entities]
❌ HIGH: Entity 'Tool' field 'inputSchema' has vague description "Schema for input" - should specify JSON Schema format [spec.md §Entities]
✅ Entity 'Resource' field 'uri' well-defined: type=string, required=true, format=URI
```

#### B. Validation Rule Completeness

**Check**:
- ✅ Each entity has validation rules section
- ✅ All required fields have validation rules
- ✅ Validation rules are specific (not "must be valid")
- ✅ Cross-entity validation documented
- ✅ Error messages defined for rule violations

**Report**:
```
❌ HIGH: Entity 'Tool' field 'name' lacks validation rule [spec.md §Validation Rules]
  Recommendation: Add "Tool name must be unique within server"
❌ MEDIUM: Validation rule "inputSchema must be valid" is vague [spec.md §Validation Rules]
  Recommendation: Specify "must conform to JSON Schema Draft 7"
✅ All validation rules have corresponding error codes
```

#### C. Specification Operations Completeness

**Check each operation**:
- ✅ Operation purpose clearly stated
- ✅ Request schema defined
- ✅ Response schema defined
- ✅ Success response documented
- ✅ Error responses documented
- ✅ Operation constraints specified

**Report**:
```
❌ CRITICAL: Operation 'tools/call' missing response schema [spec.md §Operations]
❌ HIGH: Operation 'initialize' doesn't document error scenarios [spec.md §Operations]
✅ Operation 'tools/list' has complete request/response schemas
```

#### D. Schema Consistency

**Check**:
- ✅ Entity schemas use consistent field naming (camelCase vs snake_case)
- ✅ Type definitions are consistent across entities
- ✅ Required fields are consistent with operation schemas
- ✅ No conflicting constraints across specs

**Report**:
```
❌ LOW: Entity 'Server' uses 'server_id', Entity 'Tool' uses 'toolId' [Naming Inconsistency]
  Recommendation: Standardize on camelCase or snake_case
✅ All type definitions consistent (string, number, boolean, object, array)
```

#### E. Error Handling Completeness

**Check**:
- ✅ Error codes defined
- ✅ Error response format specified
- ✅ Error messages are descriptive
- ✅ Error scenarios documented for each operation
- ✅ Recovery guidance provided

**Report**:
```
❌ HIGH: Error code 'E001' has no description [spec.md §Error Handling]
❌ MEDIUM: Error response format doesn't include 'details' field for debugging [spec.md §Error Handling]
✅ Error code 'E003' well-documented: "Tool not found - verify tool name"
```

#### F. Examples Completeness

**Check**:
- ✅ Each entity has example instance
- ✅ Each operation has request/response example
- ✅ Examples are valid against schemas
- ✅ Examples cover success and error cases
- ✅ Complex scenarios illustrated

**Report**:
```
❌ HIGH: Entity 'Resource' has no example instance [spec.md §Examples]
❌ MEDIUM: Operation 'tools/call' only shows success case, no error example [spec.md §Examples]
✅ Entity 'Tool' has complete example with all fields
```

#### G. Cross-Entity Dependencies

**Check**:
- ✅ Referenced entities exist
- ✅ Field references are valid (e.g., "references Tool.id")
- ✅ Dependency constraints documented
- ✅ Circular dependencies identified

**Report**:
```
❌ HIGH: Entity 'Prompt' references 'Tool.name' but Tool entity has 'id' not 'name' [spec.md §Entities]
✅ All entity references are valid
```

#### H. Constitution Alignment (Specification-Specific)

**Check specification against constitution**:
- ✅ Entity-First: Entities have 3-5 core fields?
- ✅ Clear Semantics: Field names self-explanatory?
- ✅ Minimal Viable: Specification includes only essential operations?
- ✅ Extensibility: Specification allows for future extensions?
- ✅ AI-Friendly: Schema descriptions clear for AI agents?
- ✅ Domain Standards: Follows established domain conventions?

**Report**:
```
❌ CRITICAL: Entity 'Server' has 8 required fields, violates Entity-First principle (3-5 max) [Constitution]
❌ HIGH: Field name 'opts' is not self-explanatory, violates Clear Semantics [Constitution]
✅ Specification follows REST-like operation naming conventions
```

#### I. Ambiguity Detection

**Check for vague terms**:
- ❌ "Appropriate", "suitable", "reasonable", "valid"
- ❌ "Should be fast", "must be secure"
- ❌ Unresolved placeholders (TODO, TBD, ???)
- ❌ Missing quantification

**Report**:
```
❌ HIGH: "inputSchema must be valid" - what validation standard? [spec.md §Validation Rules]
  Recommendation: Specify "must conform to JSON Schema Draft 7"
❌ MEDIUM: "Server should respond quickly" lacks quantification [spec.md §Operations]
  Recommendation: Define timeout (e.g., "<500ms for tool list")
```

#### J. Terminology Consistency

**Check**:
- ✅ Same concept named consistently (tool vs function vs method)
- ✅ Field names consistent (id vs identifier vs ID)
- ✅ Operation names consistent (list vs get vs query)

**Report**:
```
❌ LOW: Entity 'Server' uses 'version', Entity 'Tool' uses 'toolVersion' [Terminology Drift]
  Recommendation: Standardize on 'version' for all entities
✅ All operation names use verb-noun pattern
```

#### K. Cross-Artifact Consistency (⭐ NEW - MetaSpec specific)

**SDS Layer Internal Consistency**:

**Check spec.md ↔ examples/**:
- ✅ Each entity has example file in examples/
- ✅ Example entities match spec.md schema
- ✅ Example field values conform to spec constraints
- ✅ Examples demonstrate all operations

**Check spec.md ↔ checklists/**:
- ✅ Checklist items reference existing spec sections
- ✅ Checklist covers all entities defined in spec
- ✅ Checklist covers all operations defined in spec
- ✅ No checklist items for non-existent spec elements

**Check spec.md ↔ constitution.md**:
- ✅ All constitution principles addressed in spec
- ✅ Spec design follows constitution requirements
- ✅ Constitution violations explicitly justified

**Report**:
```
❌ HIGH: Entity 'Resource' defined in spec.md but no example in examples/ [Cross-Artifact Gap]
  Recommendation: Add examples/resource-example.yaml
❌ MEDIUM: Checklist item CHK015 references spec.md §Authentication but section doesn't exist [Broken Reference]
  Recommendation: Update checklist or add Authentication section
✅ All entities have examples
✅ All checklist items have valid spec references
```

#### L. Workflow Completeness ⭐ NEW (v0.7.0+)

**Check specification workflow definition** (per Constitution Part II Principle 7):

**Check spec.md for Workflow Specification section**:
- ✅ "Workflow Specification" section exists
- ✅ At least 2 distinct workflow phases defined
- ✅ Each phase has clear purpose statement
- ✅ Entry and exit criteria specified for each phase
- ✅ Operations mapped to specific workflow phases
- ✅ Phase transitions and dependencies documented
- ✅ Decision points and branching logic explained
- ✅ End-to-end workflow example provided
- ✅ All operations referenced in at least one workflow phase

**Check workflow quality**:
- ✅ Workflow demonstrates integrated user journey (not just operation list)
- ✅ Phase sequence is logical and complete
- ✅ No "orphan" operations without workflow context
- ✅ Workflow examples match specification operations

**Severity Rules**:
- **CRITICAL**: No "Workflow Specification" section (Constitution §II.7 violation)
- **HIGH**: Workflow section exists but <2 phases OR operations not mapped
- **MEDIUM**: Workflow exists but missing entry/exit criteria or examples
- **LOW**: Workflow complete but could be clearer (e.g., better decision point docs)

**Report**:
```
❌ CRITICAL: Missing "Workflow Specification" section [Constitution §II.7]
  Recommendation: Add workflow section defining user journey phases
❌ HIGH: Only 1 workflow phase defined, need at least 2 [Spec §Workflow]
  Recommendation: Break workflow into distinct phases (e.g., Planning → Execution → Analysis)
❌ HIGH: 3 operations not referenced in any workflow phase [Spec §Workflow]
  Operations: /marketing.project, /marketing.product, /marketing.channel
  Recommendation: Map all operations to workflow phases
❌ MEDIUM: Workflow Phase 2 missing exit criteria [Spec §Workflow]
  Recommendation: Define when Phase 2 is complete
✅ All workflow phases have clear purposes
✅ End-to-end workflow example provided
```

**Score Calculation** (15% weight):
```
Workflow Score = (Checks Passed / Total Checks) * 15%
Example: 6/9 checks passed = (6/9) * 15% = 10%
```

**Why it matters**: Operations without workflow context are "tool boxes", not "workflow systems". Users need guidance on sequencing and relationships (per marketing-spec-kit feedback).

### 6. Severity Assignment (Full/Focused Mode only)

**CRITICAL**: Constitution violation, missing operation schema, undefined entities
**HIGH**: Missing validation rules, incomplete error handling, ambiguous requirements
**MEDIUM**: Terminology drift, missing examples, underspecified constraints
**LOW**: Style improvement, minor inconsistency

### 7. Generate Analysis Report

**Report generation varies by mode:**

#### A. Quick Mode Report (already defined in Step 4)

Quick Mode uses simplified report format defined in Step 4. No additional report generation needed.

#### B. Focused Mode Report

**IF mode = Focused Mode**, generate dimension-specific report:

```markdown
# Focused Analysis Report 🎯

**Date**: [DATE] | **Mode**: Focused ([Dimension Name])  
**Specification**: [NAME] v[VERSION]

**Dimension**: [Selected Dimension Name]
**Analysis Time**: [X] minutes

---

## Summary

**Issues Found**: [N] ([X] CRITICAL, [Y] HIGH, [Z] MEDIUM, [W] LOW)

[Dimension-specific summary table]

---

## Detailed Findings

[Only findings for selected dimension, full detail]

---

## Recommendations

**Immediate Actions** (CRITICAL/HIGH):
1. [Action 1]
2. [Action 2]

**Improvements** (MEDIUM/LOW):
1. [Improvement 1]
2. [Improvement 2]

---

## Next Steps

- Fix issues above
- Re-run focused check: `/metaspec.sds.analyze check [dimension]`
- When satisfied, run full analysis: `/metaspec.sds.analyze`
```

#### C. Full Mode Report

**IF mode = Full Mode**, generate comprehensive report:

**Output format** (token-efficient, table-based):

```markdown
# Domain Specification Analysis Report 📊

**Date**: [DATE] | **Mode**: Full Analysis  
**Specification**: [NAME] v[VERSION]

**Summary Statistics**:
- Total Issues: [N] ([X] CRITICAL, [Y] HIGH, [Z] MEDIUM, [W] LOW)
- Entities Analyzed: [N]
- Operations Analyzed: [N]
- Constitution Compliance: ✅ PASS | ❌ FAIL ([N] violations)

**Analyzed Files**: spec.md, constitution.md

---

## 📊 Iteration N: [DATE] (if update mode)

**ONLY include this section when mode = `update`**

### Changes Since Last Analysis
- [List specification improvements made]
- [What sections were modified]

### Updated Results
**Issues Resolved**:
- ✅ C1: Response schema added for 'tools/call'
- ✅ H1: Validation rule added for inputSchema

**Issues Still Open**:
- ❌ C2: Tool entity still has 8 required fields

**New Issues Found**:
- ❌ M5: New ambiguity detected in 'capabilities' field

### Progress Comparison
| Metric | Iteration N-1 | Iteration N | Change |
|--------|---------------|-------------|--------|
| Total Issues | 15 | 12 | -3 ✅ |
| Critical | 2 | 1 | -1 ✅ |
| High | 5 | 4 | -1 ✅ |
| Medium | 6 | 5 | -1 ✅ |
| Low | 2 | 2 | 0 |
| Constitution Compliance | ❌ FAIL | ❌ FAIL | - |

**Overall Progress**: +20% improvement (resolved 3/15 issues)

---

## Findings Summary

**⚠️ Output Limit**: Showing top 50 findings. Additional issues aggregated in overflow summary below.

| ID | Severity | Category | Location | Summary | Recommendation |
|----|----------|----------|----------|---------|----------------|
| C1 | CRITICAL | Constitution | spec.md §Entities | Entity 'Server' has 8 required fields (max 5) | Make 3 fields optional |
| C2 | CRITICAL | Schema | spec.md §Operations | Operation 'tools/call' missing response schema | Define response schema with result/error fields |
| H1 | HIGH | Validation | spec.md §Entities | Field 'inputSchema' validation rule missing | Add "must conform to JSON Schema Draft 7" |
| H2 | HIGH | Error Handling | spec.md §Operations | Operation 'initialize' missing error scenarios | Document timeout, invalid params errors |
| M1 | MEDIUM | Examples | spec.md §Examples | Entity 'Resource' has no example | Add example with typical values |
| M2 | MEDIUM | Ambiguity | spec.md §Validation | "Must be valid" is vague | Specify validation standard |
| L1 | LOW | Terminology | spec.md §Entities | Entity 'Server' uses 'version', 'Tool' uses 'toolVersion' | Standardize on 'version' |

**Note**: If total findings > 50, group remaining by category in "Overflow Summary" section below.

---

## Overflow Summary (if findings > 50)

**Additional Issues by Category**:
- Entity Quality: +5 issues (mostly missing examples)
- Validation Rules: +3 issues (underspecified rules)
- Examples: +7 issues (missing edge case examples)

**Total Overflow**: 15 issues (not shown in detail above)

**Recommendation**: Focus on top 50 findings first. Run analyze again after fixes to surface next batch.

---

## Entity Quality Analysis

| Entity | Fields | Required | Examples | Validation Rules | Status |
|--------|--------|----------|----------|------------------|--------|
| Server | 5 | 3 | ✅ | ✅ | ✅ PASS |
| Tool | 6 | 8 (⚠️) | ✅ | ❌ Missing | ❌ FAIL |
| Resource | 4 | 2 | ❌ Missing | ✅ | ⚠️ PARTIAL |

---

## Operations Quality Analysis

| Operation | Request Schema | Response Schema | Error Cases | Examples | Status |
|-----------|---------------|-----------------|-------------|----------|--------|
| initialize | ✅ | ✅ | ❌ Missing | ✅ | ⚠️ PARTIAL |
| tools/list | ✅ | ✅ | ✅ | ✅ | ✅ PASS |
| tools/call | ✅ | ❌ Missing | ✅ | ❌ Missing | ❌ FAIL |

---

## Validation Rules Coverage

| Entity | Total Fields | Fields with Rules | Coverage | Status |
|--------|--------------|-------------------|----------|--------|
| Server | 5 | 5 | 100% | ✅ PASS |
| Tool | 6 | 4 | 67% | ❌ FAIL |
| Resource | 4 | 4 | 100% | ✅ PASS |

**Missing Rules**:
- Tool.inputSchema: No format validation specified
- Tool.name: No uniqueness constraint specified

---

## Constitution Alignment

| Principle | Status | Evidence |
|-----------|--------|----------|
| Entity-First (3-5 core fields) | ❌ FAIL | Tool has 8 required fields |
| Clear Semantics | ⚠️ PARTIAL | Field 'opts' unclear |
| Minimal Viable | ✅ PASS | Only essential operations |
| Extensibility | ✅ PASS | Supports custom capabilities |
| AI-Friendly | ✅ PASS | Clear descriptions |
| Domain Standards | ✅ PASS | Follows JSON-RPC patterns |

**Overall**: ❌ FAIL (1 critical violation)

---

## Cross-Artifact Analysis (⭐ NEW)

**Specification Internal Consistency**:

**spec.md ↔ examples/ Coverage**:
| Entity | Has Example | Example Valid | Status |
|--------|-------------|---------------|--------|
| Server | ✅ | ✅ | ✅ PASS |
| Tool | ✅ | ✅ | ✅ PASS |
| Resource | ❌ | - | ❌ FAIL |

**spec.md ↔ checklists/ Coverage**:
| Checklist Item | Spec Reference | Reference Valid | Status |
|---------------|----------------|-----------------|--------|
| CHK001 | spec.md §Entities | ✅ | ✅ PASS |
| CHK015 | spec.md §Authentication | ❌ Section missing | ❌ FAIL |

**spec.md ↔ constitution.md Alignment**:
- Principles Addressed: 5/6 (83%)
- Constitution Violations: 1 (Entity-First)

**Summary**:
- Examples Coverage: 2/3 entities (67%) ⚠️
- Checklist Validity: 95% references valid ✅
- Constitution Compliance: ❌ FAIL (1 violation)

---

## Recommendations

### Immediate Actions (CRITICAL)

1. **Define response schema for 'tools/call'** (C1):
   ```yaml
   tools_call_response:
     result: any
     error: 
       code: string
       message: string
   ```

2. **Reduce Tool entity required fields** (C2):
   - Make optional: description, tags, permissions

### High Priority Actions

1. **Add validation rule for inputSchema** (H1):
   - Specify: "Must conform to JSON Schema Draft 7"
   - Add error code: E005 "Invalid input schema format"

2. **Document error scenarios for initialize** (H2):
   - Timeout (E001): "Server initialization timeout (>5s)"
   - Invalid params (E002): "Invalid server configuration"

### Medium Priority Actions

1. **Add example for Resource entity** (M1)
2. **Clarify vague validation rules** (M2)

---

## Next Steps

- [ ] **If CRITICAL issues exist**: Fix before proceeding to toolkit development
- [ ] **If HIGH issues exist**: Consider fixing to ensure specification clarity
- [ ] **MEDIUM/LOW issues**: Can be addressed during toolkit implementation

**Recommendation**: 
⚠️ Fix CRITICAL issues (C1, C2) before running /metaspec.sdd.specify

Specification is the foundation. A clear specification enables better toolkit implementation.

Run /metaspec.sds.clarify or manually edit spec.md to address issues.

---

**Generated**: [DATE]
**Report Version**: 1.0
```

### 7. Offer Remediation

**Ask user**:
```
Would you like me to suggest concrete fixes for the top 5 issues?
(I will NOT apply them automatically - you can review and decide)
```

**If user says yes**, provide detailed recommendations for each issue.

## Important Notes

1. **Specification-Focused Analysis**
   - Only analyze domain specifications
   - Do NOT check toolkit implementation details
   - Do NOT reference plan.md, tasks.md, or src/ code
   - Focus: WHAT the specification is, not HOW to implement it

2. **Constitution Authority**
   - Constitution violations are always CRITICAL
   - Specification must adjust, not constitution
   - Specification-specific principles apply

3. **Read-Only Analysis**
   - No file modifications
   - Only output report
   - User decides on remediation

4. **Clarity is Key**
   - Every entity must be clear
   - Every operation must be specified
   - Every validation rule must be concrete
   - No vague terms tolerated

5. **Examples Matter**
   - Examples prove the specification is usable
   - Missing examples = specification gap
   - Examples should cover edge cases

## Example Output

**For new analysis**:
```
✅ Specification Analysis Complete

📊 Summary:
- Total Issues: 8
  - CRITICAL: 2
  - HIGH: 3
  - MEDIUM: 2
  - LOW: 1

❌ Constitution Compliance: FAIL (1 violation)

📁 Report: /specs/domain/analysis-report.md

⚠️ Recommendation:
Fix CRITICAL issues before toolkit development.

🔄 Next steps:
1. Fix C1: Define response schema for 'tools/call'
2. Fix C2: Reduce Tool entity required fields
3. Fix H1: Add inputSchema validation rule
4. Re-run /metaspec.sds.analyze to verify fixes

💡 Run: /metaspec.sds.clarify to refine ambiguous sections
```

**For update mode**:
```
✅ Analysis updated: consistency-report.md

📊 Iteration 2 Summary:
- Issues updated: 8/8
- Improved: 3 issues (C1: ❌ → ✅, H1: ❌ → ✅, H2: ❌ → ⚠️)
- Still critical: 1 issue (C2: ❌)
- New issues: 1 (M5: Ambiguity in 'capabilities')

📈 Progress:
- Previous: 8 total issues (2 critical)
- Current: 6 total issues (1 critical)
- Improvement: -25% issues, -50% critical

🎯 Key improvements:
- ✅ C1: Response schema added for 'tools/call'
- ✅ H1: Validation rule added for inputSchema
- ⚠️ H2: Partial error handling added

⚠️ Still needs work:
- ❌ C2: Tool entity still has 8 required fields (should be ≤5)
- ❌ M5: NEW - 'capabilities' field lacks definition

🔄 Next steps:
1. Fix remaining critical issue (C2)
2. Clarify 'capabilities' field definition (M5)
3. Complete error handling (H2)
```
