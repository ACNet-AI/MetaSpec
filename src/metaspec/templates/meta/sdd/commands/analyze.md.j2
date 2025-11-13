---
description: Perform cross-artifact consistency analysis across toolkit specifications - read-only analysis before implementation
---

## User Input

```text
$ARGUMENTS
```

You **MUST** consider the user input before proceeding (if not empty).

## Goal

Identify inconsistencies, ambiguities, and gaps across toolkit specification artifacts before implementation. **READ-ONLY** analysis - no file modifications.

## Operating Constraints

**STRICTLY READ-ONLY**: Do NOT modify any files. Output structured analysis report only.

**Constitution Authority**: constitution.md is non-negotiable. Constitution violations are CRITICAL and require spec adjustment.

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
| Empty, "full", "complete", "comprehensive", or other | **Full Mode** | Complete toolkit analysis (default) |

#### Mode Descriptions

**Quick Mode** ⚡ (< 2 min, ~500 tokens):
- Purpose: Fast structural integrity validation for toolkit specs
- Checks: 3 essential dimensions only
  1. Frontmatter Validation  
  2. Dependency Check (Does toolkit spec reference domain spec?)
  3. Architecture File Integrity (plan.md, tasks.md exist?)
- Skip: Deep semantic analysis
- Use when: Daily development, quick validation, pre-commit checks

**Focused Mode** 🎯 (3-5 min, dimension-specific):
- Purpose: Deep analysis of single dimension
- Checks: Only the specified dimension
- Dimension mapping:
  - "dependency", "dependencies", "domain" → Domain Spec Compliance
  - "architecture", "arch" → Architecture Consistency
  - "tasks" → Task Breakdown Quality
  - "constitution", "principles" → Constitution Alignment
  - "completeness" → Specification Completeness
  - "cross-artifacts" → Cross-Artifact Consistency
- Use when: Fixing specific issues, targeted improvement

**Full Mode** 📊 (5-10 min, comprehensive):
- Purpose: Complete toolkit specification quality analysis
- Checks: All dimensions
- Use when: Major releases, complete review, initial analysis

**Mode selection example**:
```
User: "/metaspec.sdd.analyze quick" → Quick Mode
User: "/metaspec.sdd.analyze check dependencies" → Focused Mode (Domain Spec Compliance)
User: "/metaspec.sdd.analyze" → Full Mode (default)
```

**Display selected mode**:
```
🔍 Analysis Mode: Quick Mode ⚡
📋 Checking: Frontmatter, Dependencies, Architecture Files
⏱️  Expected time: < 2 minutes
```

---

### 2. Check for existing analysis

**CRITICAL**: Before generating, check if analysis already exists:

```bash
ls specs/toolkit/XXX-name/analysis/
```

**If analysis exists**, ask user:

| Mode | Action | When to Use |
|------|--------|-------------|
| **update** | Update results, add iteration section | Toolkit improved, want to track progress |
| **new** | Create new analysis (backup existing) | Complete restart, different focus |
| **append** | Add supplementary analysis | Existing analysis still valid, new aspect |

**Default**: If user says "re-run", "verify improvement" → choose **update** mode

**If NO analysis exists** → proceed to step 2

---

### 2. Identify Feature Type and Load Artifacts

**🏗️ Two-Feature Architecture Check**

**Step 1a: Determine Feature Context**
- Check current directory structure
- Identify if analyzing Feature 1 (Specification) or Feature 2 (Toolkit)

**Step 1b: Load Appropriate Artifacts**

**For Feature 1 (Specification Spec)**:
- **Required**:
  - `specs/domain/001-{domain}-spec/spec.md` (specification definition)
  - `/memory/constitution.md` (domain principles)
- **Optional**:
  - `specs/domain/001-{domain}-spec/checklists/`
- **Skip**: plan.md, tasks.md (not needed for specification specs)

**For Feature 2 (Toolkit Spec)**:
- **Required**:
  - `specs/toolkit/001-toolkit/spec.md` (toolkit definition)
  - `specs/toolkit/001-toolkit/plan.md` (architecture)
  - `specs/toolkit/001-toolkit/tasks.md` (task breakdown)
  - `specs/domain/001-{domain}-spec/spec.md` (dependency!)
  - `/memory/constitution.md` (design principles)
- **Optional**:
  - `specs/toolkit/001-toolkit/architecture.md`
  - `specs/toolkit/001-toolkit/research.md`

**If Feature 1 missing for Feature 2**: 
⚠️ **CRITICAL**: "Feature 2 depends on Feature 1 but `specs/domain/001-*` not found!"

### 3. Build semantic models

**Extract from spec.md**:
- Entity fields (name, type, required, description)
- Validation rules (structural, semantic, domain)
- Workflows (steps, inputs, outputs)
- CLI commands (name, purpose, options)
- Quality criteria

**Extract from plan.md**:
- Architecture components (parser, validator, CLI)
- Tech stack (Python, Pydantic, Typer)
- File structure
- Constitution alignment

**Extract from tasks.md**:
- Task IDs and descriptions
- Phase grouping
- File paths
- Dependencies

**Extract from constitution**:
- Six principles (Entity-First, Validator Extensibility, etc.)
- MUST/SHOULD requirements

### 4. Quick Mode Checks (if Quick Mode selected)

**IF mode = Quick Mode**, execute ONLY these 3 checks and skip to Step 6 (report generation):

#### Quick-A. Frontmatter Validation

**Purpose**: Verify toolkit spec has valid YAML frontmatter

**Check spec.md frontmatter**:
```bash
# Extract frontmatter from specs/toolkit/001-xxx/spec.md
yq eval '.' specs/toolkit/001-xxx/spec.md
```

**Required fields for toolkit spec**:
- `spec_id`: Must exist
- `spec_type`: Should be 'toolkit'
- `version`: Must exist
- `dependencies`: Must list at least one domain spec

**Report**:
```
✅ PASS: Toolkit spec has valid frontmatter
  - spec_id: 001-mcp-parser
  - spec_type: toolkit
  - version: 0.1.0
  - dependencies: [domain/001-mcp-spec]

OR

❌ FAIL: Frontmatter issues found
  - Missing 'dependencies' field → CRITICAL: Must reference domain spec
  - Missing 'version' field
```

#### Quick-B. Dependency Check (Domain Spec Reference)

**Purpose**: Verify toolkit spec declares dependency on domain spec

**Check dependencies section**:
```bash
# Check if spec.md has Dependencies section
grep -A 5 "## Dependencies" specs/toolkit/001-xxx/spec.md

# Verify referenced spec exists
ls specs/domain/001-xxx-spec/spec.md
```

**Validate**:
- ✅ Has "Dependencies" section in spec.md
- ✅ Lists at least one domain spec
- ✅ Referenced domain spec exists
- ✅ Domain spec file is valid (can be read)

**Report**:
```
✅ PASS: Toolkit correctly references domain spec
  - Dependency declared: domain/001-mcp-spec
  - Domain spec exists: ✅
  - Domain spec valid: ✅

OR

❌ CRITICAL: No domain spec dependency found
  - specs/toolkit/001-parser/spec.md missing "Dependencies" section
  - ACTION: Run /metaspec.sdd.specify and add domain spec reference
  - Cannot proceed: Toolkit without specification violates Spec-Driven principle

OR

❌ HIGH: Referenced domain spec doesn't exist
  - Declared dependency: domain/001-api-spec
  - File not found: specs/domain/001-api-spec/spec.md
  - ACTION: Run /metaspec.sds.specify to create domain spec first
```

#### Quick-C. Architecture File Integrity

**Purpose**: Verify required toolkit files exist and are readable

**Check file existence**:
```bash
# Required files for toolkit
ls specs/toolkit/001-xxx/spec.md      # Toolkit specification
ls specs/toolkit/001-xxx/plan.md      # Architecture plan (if planned)
ls specs/toolkit/001-xxx/tasks.md     # Implementation tasks (if tasked)
```

**Validate**:
- ✅ spec.md exists and is readable
- ✅ plan.md exists (if spec mentions architecture)
- ✅ tasks.md exists (if spec mentions implementation)
- ✅ Files are not empty
- ✅ Files are valid markdown

**Report**:
```
✅ PASS: All required files present
  - spec.md: ✅ (1250 lines)
  - plan.md: ✅ (850 lines)
  - tasks.md: ✅ (420 lines)

OR

⚠️ WARNING: Missing optional files
  - spec.md: ✅
  - plan.md: ❌ Not found (run /metaspec.sdd.plan to create)
  - tasks.md: ❌ Not found (run /metaspec.sdd.tasks to create)
  
Recommendation: Create plan and tasks before implementation

OR

❌ FAIL: Required file missing
  - spec.md: ❌ Not found
  - ACTION: Run /metaspec.sdd.specify to create toolkit spec
```

**Quick Mode Report Format**:
```markdown
# Quick Toolkit Analysis Report ⚡

**Date**: [DATE] | **Mode**: Quick | **Toolkit**: [NAME]

**Summary**:
- ✅ Frontmatter: Valid
- ✅ Domain Dependency: Valid (references domain/001-mcp-spec)
- ✅ Architecture Files: All present

**Total Time**: 30 seconds

---

## ✅ All Structural Checks Passed

**Dependency**:
- Domain Spec: specs/domain/001-mcp-spec/spec.md ✅

**Files**:
- spec.md: ✅ (1250 lines)
- plan.md: ✅ (850 lines)
- tasks.md: ✅ (420 lines)

**Next Steps**:
- For detailed analysis, run: `/metaspec.sdd.analyze`
- For specific dimension, run: `/metaspec.sdd.analyze check [dimension]`
```

**If issues found**:
```markdown
# Quick Toolkit Analysis Report ⚡

**Date**: [DATE] | **Mode**: Quick | **Toolkit**: [NAME]

**Summary**:
- ❌ Frontmatter: Missing dependencies field
- ❌ Domain Dependency: No domain spec referenced  
- ⚠️  Architecture Files: plan.md and tasks.md missing

**Total Issues**: 3 (1 CRITICAL, 2 WARNING)

---

## ❌ Critical Issues Found

### 1. Missing Domain Spec Dependency (CRITICAL)

**Issue**: Toolkit spec doesn't reference any domain specification

**Impact**: Violates Spec-Driven Development principle
- Toolkit without specification is not a valid speckit
- Cannot validate correctness against specification
- Implementation has no reference

**Action Required**:
1. Identify domain specification this toolkit supports
2. If domain spec doesn't exist:
   - Run `/metaspec.sds.specify` to create it first
3. Update toolkit spec.md:
   - Add "Dependencies" section
   - Reference domain spec (e.g., "Depends on: domain/001-api-spec")
4. Update frontmatter dependencies field

### 2. Missing Architecture Files (WARNING)

**Issue**: plan.md and tasks.md not found

**Impact**: 
- Cannot implement without plan and tasks
- No architecture design guidance
- No task breakdown

**Action Recommended**:
1. Run `/metaspec.sdd.plan` to create architecture plan
2. Run `/metaspec.sdd.tasks` to break down implementation tasks
3. Then proceed with `/metaspec.sdd.implement`

---

## 🔄 Next Steps

1. **Fix CRITICAL issues first** (domain spec dependency)
2. **Create missing files** (plan, tasks)
3. **Re-run quick check**: `/metaspec.sdd.analyze quick`
4. **When resolved**, run full analysis: `/metaspec.sdd.analyze`
```

**END Quick Mode** - Skip to Step 6 (Generate Report)

---

### 5. Full/Focused Mode Detection Passes

**IF mode = Full Mode OR Focused Mode**, execute these detection passes:

**Note**: In Focused Mode, only execute the selected dimension.

#### A. Feature Dependency Validation (Feature 2 Only)

**For Feature 2 (Toolkit Spec)** - Check dependency on Feature 1:

**Check**:
1. ✅ Feature 1 exists: `specs/domain/001-{domain}-spec/spec.md`
2. ✅ Feature 2 declares dependency:
   - Has a "Dependencies" section
   - References "001-{domain}-spec"
3. ✅ Feature 2 components reference Feature 1:
   - Validator references Feature 1 validation rules
   - Parser handles Feature 1 entities
4. ✅ Feature 1 and Feature 2 naming consistency:
   - Domain names match
   - Entity references consistent

**Report**:
```
❌ CRITICAL: Feature 2 lacks "Dependencies" section in spec.md
   → ACTION REQUIRED: Add Dependencies section before /metaspec.sdd.implement
   → This violates the Spec-Driven principle
   → Toolkit without specification is not a valid speckit

❌ CRITICAL: Feature 1 (specification) does not exist
   → ACTION REQUIRED: Run /metaspec.sds.specify first to define specification
   → Cannot proceed with toolkit development without specification
   
❌ HIGH: Feature 2 Validator doesn't reference Feature 1 validation rules
   → ACTION RECOMMENDED: Update Validator section to reference specification rules

✅ Feature 1 exists: specs/domain/001-mcp-spec/spec.md
✅ Feature 2 declares dependency: "Depends on: 001-mcp-spec"
✅ Validator references Feature 1: "Validates against MCP specification rules"
```

**CRITICAL errors must be fixed before implementation.**

**Skip this check for Feature 1** (Specification specs don't have dependencies)

#### B. Entity Definition Quality

**Check**:
- All fields have types specified
- Required vs optional is clear
- Field descriptions are specific
- Example values provided
- Validation rules documented

**Report**:
```
❌ MEDIUM: Field 'headers' missing type specification [spec.md §Entity Definitions]
❌ HIGH: Field 'assertions' has vague description "List of assertions" - no format specified [spec.md §Entity Definitions]
✅ Field 'method' well-defined: type=string, required=true, enum=[GET,POST,PUT,DELETE]
```

#### C. Validation Rule Consistency

**Check**:
- All entity fields have validation rules
- Error message formats consistent
- Validation layers (1/2/3) mapped to implementation
- Custom validator mechanism specified

**Report**:
```
❌ HIGH: Field 'endpoint' lacks validation rule in spec.md but mentioned in validator-design.md [Inconsistency]
✅ All validation rules have corresponding tasks in tasks.md Phase 4
```

#### D. Workflow Completeness

**Check**:
- All CLI commands mapped to workflows
- Workflow steps have clear inputs/outputs
- Success indicators measurable
- Error scenarios documented

**Report**:
```
❌ CRITICAL: CLI command 'execute' in spec.md has no corresponding workflow [Gap]
✅ Workflow "Test Execution" maps to tasks T040-T041 in tasks.md
```

#### E. Constitution Alignment

**Check spec.md against constitution**:
- Entity-First: 3-5 core fields? ✅/❌
- Validator Extensibility: Plugin system specified? ✅/❌
- Spec-First: Users write specs first? ✅/❌
- AI-Agent Friendly: Error messages actionable? ✅/❌
- Progressive Enhancement: MVP scope clear? ✅/❌
- Domain Specificity: Domain rules documented? ✅/❌

**Report**:
```
❌ CRITICAL: Entity has 8 required fields, violates Entity-First principle (3-5 core fields) [Constitution §I]
❌ HIGH: No custom validator registration mechanism specified, violates Validator Extensibility [Constitution §II]
✅ Error message format is AI-friendly with examples [Constitution §IV]
```

#### F. Task Coverage

**Check**:
- All entities have model tasks
- All validation rules have validator tasks
- All CLI commands have CLI tasks
- All components have test tasks

**Report**:
```
❌ HIGH: Validation rule "endpoint must start with /" has no corresponding task [Gap]
✅ Entity 'APITest' covered by tasks T008-T016
✅ CLI command 'validate' covered by tasks T040-T041
```

#### G. Cross-Reference Integrity

**Check**:
- Files referenced in tasks exist in file structure
- Components referenced in plan exist in spec
- Validation rules in spec exist in validator-design
- CLI commands in spec exist in tasks

**Report**:
```
❌ MEDIUM: Task T015 references src/api_test_kit/errors.py but not in file structure [Plan §Project Structure]
✅ All validation rules cross-referenced between spec and plan
```

#### H. Ambiguity Detection

**Check for vague terms**:
- "Fast", "scalable", "robust", "simple", "easy"
- Missing quantification in quality criteria
- Unresolved placeholders (TODO, TBD, ???)

**Report**:
```
❌ HIGH: Quality criterion "validation should be fast" lacks quantification [spec.md §Quality Criteria]
  Recommendation: Specify "<100ms for typical spec"
❌ MEDIUM: "Simple error messages" is vague [spec.md §Validation Requirements]
  Recommendation: Define error message format with examples
```

#### I. Terminology Consistency

**Check**:
- Same concept named consistently (entity vs model vs schema)
- Field names consistent (endpoint vs url vs path)
- Command names consistent (init vs initialize vs create)

**Report**:
```
❌ LOW: spec.md uses "entity", plan.md uses "model" [Terminology Drift]
  Recommendation: Standardize on "entity" (matches constitution)
✅ All field names consistent across spec and plan
```

#### K. Cross-Artifact Consistency (⭐ NEW - MetaSpec specific)

**SDD Layer Cross-Document Analysis** (spec-kit inspired, MetaSpec adapted):

**Check toolkit/spec.md ↔ domain/spec.md** (⭐ Critical for MetaSpec):
- ✅ All domain entities referenced in toolkit spec "Dependencies" section
- ✅ Toolkit spec correctly describes domain entities it will parse/validate
- ✅ Validation rules in toolkit spec align with domain spec validation rules
- ✅ Operations in toolkit spec cover all domain spec operations
- ✅ Error codes in toolkit spec align with domain spec error codes

**Check toolkit/spec.md ↔ toolkit/plan.md**:
- ✅ All entities in spec have corresponding components in plan
- ✅ Parser component in plan covers all spec operations
- ✅ Validator component in plan covers all spec validation rules
- ✅ CLI commands in spec match CLI design in plan
- ✅ Tech stack in plan supports spec requirements

**Check toolkit/spec.md ↔ toolkit/tasks.md** (Coverage Analysis):
- ✅ Each spec entity has >=1 implementation task
- ✅ Each spec operation has >=1 parser task
- ✅ Each spec validation rule has >=1 validator task
- ✅ Each CLI command has >=1 CLI task
- ✅ No orphaned tasks (tasks with no spec reference)

**Coverage Summary Table**:
```
| Domain Spec Section | Toolkit Spec Reference | Plan Component | Task Coverage | Status |
|-------------------|----------------------|---------------|--------------|--------|
| Entity 'Tool' | ✅ §Dependencies | ✅ Parser.Tool | ✅ T001-T003 | ✅ PASS |
| Operation 'list' | ✅ §Parser Requirements | ✅ Parser.list() | ✅ T010 | ✅ PASS |
| Validation 'required' | ❌ Not mentioned | ⚠️ Validator (generic) | ❌ No task | ❌ CRITICAL |
```

**Metrics**:
- Domain Spec Coverage: 8/10 entities (80%)
- Spec → Plan Alignment: 12/15 components (80%)
- Spec → Tasks Coverage: 25/30 requirements (83%)

**Report**:
```
❌ CRITICAL: Domain spec 'Resource' entity not referenced in toolkit spec §Dependencies [Cross-Layer Gap]
  Recommendation: Add Resource parsing requirements to toolkit spec
❌ HIGH: Spec requires 'uniqueness' validation but no validator task in tasks.md [Coverage Gap]
  Recommendation: Add task "Implement uniqueness validator" 
❌ MEDIUM: Plan.md defines 'SchemaValidator' but spec.md doesn't mention schema validation [Plan Drift]
  Recommendation: Update spec to include schema validation requirements
✅ All CLI commands in spec have corresponding plan components and tasks
```

### 5. Severity assignment

**CRITICAL**: Constitution violation, missing core artifact, blocking gap
**HIGH**: Inconsistency, ambiguous requirement, missing coverage
**MEDIUM**: Terminology drift, underspecified item, minor gap
**LOW**: Style improvement, minor redundancy

### 6. Generate analysis report

**Output format** (token-efficient, table-based):

```markdown
# Toolkit Specification Analysis Report

**Date**: [DATE] | **Feature**: [NAME] v[VERSION]

**Summary Statistics**:
- Total Issues: [N] ([X] CRITICAL, [Y] HIGH, [Z] MEDIUM, [W] LOW)
- Artifacts Analyzed: spec.md, plan.md, tasks.md, constitution.md
- Constitution Compliance: ✅ PASS | ❌ FAIL ([N] violations)
- Cross-Document Coverage: [X]%

---

## 📊 Iteration N: [DATE] (if update mode)

**ONLY include this section when mode = `update`**

### Changes Since Last Analysis
- [List toolkit improvements made]
- [What sections were modified]

### Updated Results
**Issues Resolved**:
- ✅ C1: Entity reduced to 5 required fields
- ✅ H1: Assertion syntax defined

**Issues Still Open**:
- ❌ C2: 'execute' command still lacks workflow

**New Issues Found**:
- ❌ M5: New inconsistency between spec and plan

### Progress Comparison
| Metric | Iteration N-1 | Iteration N | Change |
|--------|---------------|-------------|--------|
| Total Issues | 12 | 9 | -3 ✅ |
| Critical | 2 | 1 | -1 ✅ |
| High | 4 | 3 | -1 ✅ |
| Medium | 5 | 4 | -1 ✅ |
| Low | 1 | 1 | 0 |
| Constitution Compliance | ❌ FAIL | ❌ FAIL | - |

**Overall Progress**: +25% improvement (resolved 3/12 issues)

---

## Findings Summary

**⚠️ Output Limit**: Showing top 50 findings. Additional issues aggregated in overflow summary below.

| ID | Severity | Category | Location | Summary | Recommendation |
|----|----------|----------|----------|---------|----------------|
| C1 | CRITICAL | Constitution | spec.md §Entity | 8 required fields violates Entity-First (3-5 max) | Make 5 fields optional |
| C2 | CRITICAL | Workflow | spec.md §CLI | 'execute' command has no workflow | Add workflow or remove command |
| H1 | HIGH | Validation | spec.md §Entity | Field 'assertions' format unspecified | Define assertion syntax |
| H2 | HIGH | Constitution | plan.md §Validator | No custom validator mechanism | Add register_validator() interface |
| M1 | MEDIUM | Consistency | Multiple | "entity" vs "model" terminology drift | Standardize on "entity" |
| M2 | MEDIUM | Ambiguity | spec.md §Quality | "Fast validation" lacks quantification | Specify "<100ms" |
| L1 | LOW | Style | spec.md | Minor formatting inconsistency | Update formatting |

**Note**: If total findings > 50, group remaining by category in "Overflow Summary" section below.

---

## Overflow Summary (if findings > 50)

**Additional Issues by Category**:
- Entity Quality: +4 issues (mostly documentation gaps)
- Validation Rules: +6 issues (underspecified rules)
- CLI Interface: +3 issues (missing examples)

**Total Overflow**: 13 issues (not shown in detail above)

**Recommendation**: Focus on top 50 findings first. Run analyze again after fixes to surface next batch.

---

## Coverage Analysis

**Entity Coverage**:
- APITest: ✅ Tasks T008-T016 (complete)

**Validation Rule Coverage**:
- Structural validation: ✅ Task T026
- Semantic validation: ✅ Task T027
- Domain validation: ✅ Task T028
- Endpoint rule: ❌ No task (GAP)

**CLI Command Coverage**:
- init: ✅ Task T040
- validate: ✅ Task T041

**Component Coverage**:
- Parser: ✅ Tasks T017-T024
- Validator: ✅ Tasks T025-T037
- CLI: ✅ Tasks T038-T048

---

## Constitution Alignment

| Principle | Status | Evidence |
|-----------|--------|----------|
| I. Entity-First | ❌ FAIL | 8 required fields (max 5) |
| II. Validator Extensibility | ❌ FAIL | No plugin system specified |
| III. Spec-First | ✅ PASS | Users write specs first |
| IV. AI-Agent Friendly | ✅ PASS | Error messages actionable |
| V. Progressive Enhancement | ✅ PASS | MVP scope clear |
| VI. Domain Specificity | ✅ PASS | Domain rules documented |

**Overall**: ❌ FAIL (2/6 principles violated)

---

## Metrics

- Total Entity Fields: 6
- Total Validation Rules: 8
- Total CLI Commands: 2
- Total Tasks: 59
- Entity Coverage: 100%
- Validation Coverage: 87% (7/8 rules)
- CLI Coverage: 100%
- Constitution Compliance: 67% (4/6 principles)

---

## Cross-Artifact Analysis (⭐ NEW - MetaSpec specific)

**Cross-Layer Analysis** (toolkit ↔ domain):

**Domain Spec → Toolkit Spec Coverage**:
| Domain Entity | Toolkit Spec Reference | Status |
|--------------|----------------------|--------|
| Tool | ✅ §Dependencies | ✅ PASS |
| Resource | ❌ Not mentioned | ❌ FAIL |
| Server | ✅ §Parser Requirements | ✅ PASS |

**Toolkit Spec → Plan Alignment**:
| Spec Requirement | Plan Component | Status |
|-----------------|---------------|--------|
| Parse Tool entity | ✅ Parser.Tool | ✅ PASS |
| Validate required fields | ✅ Validator.structural | ✅ PASS |
| Custom validators | ❌ No plugin system | ❌ FAIL |
| CLI init command | ✅ CLI.init() | ✅ PASS |

**Spec → Tasks Coverage**:
| Spec Section | Task Coverage | Gap |
|--------------|--------------|-----|
| Entity parsing | ✅ T001-T003 | - |
| Validation rules | ⚠️ T026-T028 | Missing: uniqueness validation |
| CLI commands | ✅ T040-T041 | - |

**Metrics**:
- Domain Spec Coverage: 2/3 entities (67%) ⚠️
- Spec → Plan Alignment: 3/4 requirements (75%) ⚠️
- Spec → Tasks Coverage: 29/30 requirements (97%) ✅

**Critical Gaps**:
1. Domain 'Resource' entity not addressed in toolkit
2. Custom validator mechanism specified but not designed
3. Uniqueness validation rule missing implementation

---

## Recommendations

### Immediate Actions (CRITICAL)

1. **Reduce required fields** (C1):
   - Make 3 fields optional (headers, body, assertions)
   - Keep only: name, endpoint, method as required

2. **Add workflow for 'execute' command** (C2):
   - Document execute workflow in spec.md
   - Add corresponding tasks to tasks.md

### High Priority Actions

1. **Specify assertion format** (H1):
   - Define assertion syntax in spec.md
   - Add examples: "status: 200", "body.length > 0"

2. **Add custom validator mechanism** (H2):
   - Specify register_validator() in validator-design.md
   - Add implementation task to tasks.md

### Medium Priority Actions

1. **Standardize terminology** (M1):
   - Replace "model" with "entity" in plan.md

2. **Quantify quality criteria** (M2):
   - Specify "<100ms" for validation performance

---

## Next Steps

- [ ] If CRITICAL issues exist: Fix before /metaspec:implement
- [ ] If HIGH issues exist: Consider fixing before /metaspec:implement
- [ ] MEDIUM/LOW issues: Can fix during or after implementation

**Recommendation**: 
⚠️ Do NOT proceed to /metaspec:implement until CRITICAL issues (C1, C2) are resolved.

Run /metaspec:clarify or manually edit spec.md to address issues.

---

**Generated**: [DATE]
**Report Version**: 1.0
```

### 7. Offer remediation

**Ask user**:
```
Would you like me to suggest concrete fixes for the top 5 issues?
(I will NOT apply them automatically - you can review and decide)
```

**If user says yes**:
```
## Suggested Remediation

### C1: Reduce required fields

**File**: spec.md §Entity Definitions

**Current**:
```yaml
entity:
  name: APITest
  fields:
    - name: name
      type: string
      required: true
    - name: endpoint
      type: string
      required: true
    - name: method
      type: string
      required: true
    - name: headers
      type: object
      required: true   # ← Change to false
    - name: body
      type: object
      required: true   # ← Change to false
    - name: assertions
      type: array
      required: true   # ← Change to false
```

**Recommended**:
```yaml
entity:
  name: APITest
  fields:
    - name: name
      type: string
      required: true
    - name: endpoint
      type: string
      required: true
    - name: method
      type: string
      required: true
    - name: headers
      type: object
      required: false   # ← Optional
    - name: body
      type: object
      required: false   # ← Optional
    - name: assertions
      type: array
      required: false   # ← Optional
```

**Rationale**: Follows Entity-First principle (3 core fields + 3 optional)

---

[Continue for other issues...]
```

## Important Notes

1. **Read-only analysis**
   - No file modifications
   - Only output report
   - User decides on remediation

2. **Constitution is authority**
   - Violations are always CRITICAL
   - Spec must adjust, not constitution
   - No silent ignoring of principles

3. **Focus on high-signal findings**
   - Limit to 50 issues max
   - Prioritize by severity
   - Aggregate remainder

4. **Coverage is key**
   - Every entity needs tasks
   - Every validation rule needs tasks
   - Every CLI command needs tasks
   - Every component needs tests

5. **Quantify vague terms**
   - "Fast" → "<100ms"
   - "Simple" → "3-5 fields"
   - "Extensible" → "register_validator() API"
   - "AI-friendly" → "Include fix examples"

## Example Output

```
✅ Analysis complete

📊 Summary:
- Total Issues: 12
  - CRITICAL: 2
  - HIGH: 4
  - MEDIUM: 5
  - LOW: 1

❌ Constitution Compliance: FAIL (2 violations)

📁 Report: /specs/analysis-report.md

⚠️ Recommendation:
DO NOT proceed to /metaspec:implement until CRITICAL issues resolved.

🔄 Next steps:
1. Fix C1: Reduce required fields (spec.md)
2. Fix C2: Add execute workflow (spec.md)
3. Fix H1: Specify assertion format (spec.md)
4. Re-run /metaspec:analyze to verify fixes

💡 Run: /metaspec:clarify to refine ambiguous sections
```

