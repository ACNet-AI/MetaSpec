---
description: Generate actionable, dependency-ordered task breakdown for toolkit implementation based on architecture design
---

## User Input

```text
$ARGUMENTS
```

You **MUST** consider the user input before proceeding (if not empty).

## Outline

**Goal**: Break down the implementation plan into specific, executable tasks organized by component and ordered by dependencies.

**Important**: This command runs AFTER `/metaspec:plan`. It transforms architecture design into actionable tasks.

### Execution Flow

#### 1. Load design documents

**Required**:
- `specs/toolkit/XXX-name/plan.md` (tech stack, architecture, structure)
- `specs/toolkit/XXX-name/spec.md` (entities, workflows, CLI commands)

**Optional**:
- `specs/toolkit/XXX-name/architecture.md` (component design)
- `specs/toolkit/XXX-name/parser-design.md` (parser interfaces)
- `specs/toolkit/XXX-name/validator-design.md` (validator layers)
- `/specs/research.md` (domain standards)

#### 2. Extract key information

**From spec.md**:
- Primary entity structure
- CLI commands list
- Workflows (init → validate → execute)
- Quality criteria

**From plan.md**:
- Tech stack (Python, Pydantic, Typer)
- Project structure (src/, tests/, templates/)
- Component responsibilities
- Extension points

**From architecture.md** (if exists):
- Component interfaces
- Data flow
- Extension mechanisms

#### 3. Task generation rules

**Checklist Format (REQUIRED)**:

Every task MUST follow:
```
- [ ] [TaskID] [P] [Component] Description with file path
```

**Format Components**:
1. **Checkbox**: `- [ ]` (markdown checkbox)
2. **Task ID**: T001, T002, T003... (sequential, execution order)
3. **[P] marker**: ONLY if parallelizable (different files, no dependencies)
4. **[Component] label**: [SETUP], [MODELS], [PARSER], [VALIDATOR], [CLI], [TESTS], [DOCS]
5. **Description**: Clear action with exact file path

**Examples**:
- ✅ `- [ ] T001 [SETUP] Create project structure per implementation plan`
- ✅ `- [ ] T005 [P] [MODELS] Define APITest entity in src/api_test_kit/models.py`
- ✅ `- [ ] T012 [PARSER] Implement parse_spec() in src/api_test_kit/parser.py`
- ❌ `- [ ] Create parser` (missing ID, Component, file path)
- ❌ `T001 [PARSER] Create parser` (missing checkbox)

#### 4. Task organization

**Phase 1: Project Setup**
- Create directory structure
- Initialize pyproject.toml
- Set up testing framework
- Create templates/
- Initialize git

**Phase 2: Entity Models ([MODELS])**
- Define Pydantic models for primary entity
- Add field validators
- Generate JSON Schema
- Create model tests

**Phase 3: Parser ([PARSER])**
- Implement YAML/JSON parsing
- Add error handling
- Preserve line numbers
- Create parser tests

**Phase 4: Validator ([VALIDATOR])**
- Layer 1: Structural validation (Pydantic)
- Layer 2: Semantic validation (custom rules)
- Layer 3: Domain validation (from research.md)
- Error message formatting
- Create validator tests

**Phase 5: CLI ([CLI])**
- Implement `init` command
- Implement `validate` command
- Implement additional commands
- Add output formatters
- Create CLI tests

**Phase 6: Documentation & Examples**
- Write README.md
- Update AGENTS.md
- Create example specs
- Add docstrings

**Phase 7: Integration & Polish**
- Integration testing
- Performance testing
- Error message review
- Constitution compliance check

#### 5. Dependency tracking

**Component Dependencies**:
```
SETUP → MODELS → PARSER → VALIDATOR → CLI → DOCS → INTEGRATION
  ↓        ↓        ↓         ↓         ↓
TESTS    TESTS    TESTS     TESTS    TESTS
```

**Parallel Opportunities**:
- Within MODELS: Multiple entity files
- Within TESTS: Test files for different components
- Within DOCS: Documentation files

#### 6. Generate tasks.md

**Structure**:
```markdown
# Implementation Tasks: [Toolkit Name]

## Overview
- Total Tasks: [N]
- Components: [SETUP, MODELS, PARSER, VALIDATOR, CLI, TESTS, DOCS]
- Estimated Time: [X] days

## Dependencies
[Component dependency diagram]

## Phase 1: Project Setup ([SETUP])
**Goal**: Initialize project structure and tooling
**Dependencies**: None

### Tasks
- [ ] T001 [SETUP] Create directory structure
- [ ] T002 [SETUP] Initialize pyproject.toml
- [ ] T003 [SETUP] Configure pytest
- [ ] T004 [SETUP] Create .gitignore
- [ ] T005 [SETUP] Initialize git repository

**Checkpoint**: Project structure created, tests can run

## Phase 2: Entity Models ([MODELS])
**Goal**: Define Pydantic models for domain entities
**Dependencies**: Phase 1 complete

### Tasks
- [ ] T006 [MODELS] Create src/[toolkit]/models.py
- [ ] T007 [MODELS] Define [Entity] model with fields
- [ ] T008 [MODELS] Add field validators
- [ ] T009 [MODELS] Add model_dump() and model_validate()
- [ ] T010 [P] [TESTS] Create tests/unit/test_models.py
- [ ] T011 [P] [TESTS] Test [Entity] instantiation
- [ ] T012 [P] [TESTS] Test field validation

**Checkpoint**: Entity models working, passing all tests

[... other phases ...]

## Parallel Execution Opportunities

**Within Phase 2 (MODELS)**:
```bash
# Can run in parallel:
- T010 (create test file)
- T011 (test instantiation)
- T012 (test validation)
```

**Across Phases**:
```bash
# After Phase 2, can parallelize:
- Phase 3 (PARSER) tests
- Phase 4 (VALIDATOR) tests
```

## MVP Scope

**Minimum Viable Toolkit** (for initial release):
- Phase 1: Setup ✅
- Phase 2: Models ✅
- Phase 3: Parser ✅
- Phase 4: Validator (Layers 1-2) ✅
- Phase 5: CLI (init + validate commands only) ✅
- Phase 6: Basic README ✅

**Deferred to v0.2**:
- Phase 4: Domain validation (Layer 3)
- Phase 5: Additional CLI commands
- Phase 6: Comprehensive docs
- Phase 7: Performance optimization

## Implementation Strategy

1. **TDD Approach**: Write tests before implementation
2. **Component Isolation**: Complete one component fully before starting next
3. **Early Integration**: Test component integration early
4. **Constitution Alignment**: Check principles after each phase

```

#### 7. Task Details

**For each task, specify**:

**SETUP tasks**:
- Create directory: Exact path
- Create file: Template or content
- Configure tool: Config options

**MODELS tasks**:
- Entity definition: Field names, types, descriptions
- Validators: Validation rules from spec.md
- Tests: Test cases from entity examples

**PARSER tasks**:
- Parse function: Interface from parser-design.md
- Error handling: Error types from parser-design.md
- Tests: Valid/invalid spec fixtures

**VALIDATOR tasks**:
- Layer 1: Pydantic validation (automatic)
- Layer 2: Custom rules from spec.md
- Layer 3: Domain rules from research.md
- Tests: Validation scenarios

**CLI tasks**:
- Command definition: Typer command with options
- Output formatting: Text and JSON formats
- Tests: CLI invocation tests

**DOCS tasks**:
- README sections: Usage, installation, examples
- AGENTS.md updates: Toolkit usage guidance
- Examples: Valid spec examples

#### 8. Generate tasks.md file

- Write to `specs/toolkit/XXX-name/tasks.md`
- Use tasks-template structure
- Include all phases
- Add checkpoint criteria
- Document dependencies
- Show parallel opportunities

#### 8.5. Generate Task Generation Report

**Purpose**: Create detailed metadata about toolkit implementation task breakdown.

Prepend this as an HTML comment at the top of `tasks.md`:

```html
<!--
Toolkit Task Generation Report
===============================
Toolkit: {toolkit_id} | Date: {ISO_DATE} | Language: {Python | TS | Go | Rust}

Summary:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Total: {total} tasks | By Component: Setup: {setup}, Models: {models}, Parser: {parser}, Validator: {validator}, CLI: {cli}, Tests: {tests}, Docs: {docs}

Execution:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
7 Phases | Critical Path: SETUP → MODELS → PARSER → VALIDATOR → CLI
Parallel: Tests + Docs | Time savings: {percent}%

MVP (v0.1.0):
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Parser + Validator + Basic CLI ({count} tasks) | Effort: {X} days
Future: v0.2 (Generator, +{X}d), v1.0 (Full feature set, +{Y}d)

Constitution: {✅ Compliant | ⚠️ Check: {issues}}

Generated by: /metaspec.sdd.tasks
-->
```

**Report format rules**:
- Include actual counts and language choice
- Show clear component dependencies
- Calculate parallel opportunities
- Reference domain specification dependency
- Verify Part III constitution compliance

#### 9. Validation

**Check**:
- [ ] All tasks have format: `- [ ] [TID] [P?] [COMP] Description with path`
- [ ] Task IDs are sequential
- [ ] Dependencies are clear
- [ ] Each phase has checkpoint
- [ ] MVP scope is defined
- [ ] Parallel opportunities identified
- [ ] File paths are absolute or relative to project root

#### 9.5. Consistency Propagation and Impact Analysis

**Purpose**: Ensure task breakdown aligns with toolkit spec, plan, and domain specification.

Check and update dependent files:

#### A. Toolkit Spec Alignment Check (CRITICAL)

```bash
# Read toolkit specification
cat specs/toolkit/{toolkit_id}/spec.md
```

**Verify**:
- [ ] All components in spec.md have corresponding tasks
- [ ] Task count matches plan estimate (±20%)
- [ ] Language choice matches spec (Python/TypeScript/Go/Rust)
- [ ] Architecture type matches (Monolithic/Modular/Plugin-based)
- [ ] All dependencies listed in spec are covered by setup tasks

**Action if mismatch**:
- ⚠️ **CRITICAL**: Spec and tasks misaligned
- Re-read spec.md and regenerate tasks

#### B. Domain Specification Dependency Check (CRITICAL)

```bash
# Read domain specification (REQUIRED dependency)
cat specs/domain/{domain_spec_id}/spec.md
```

**Verify**:
- [ ] Domain entities have corresponding model tasks
- [ ] Domain operations have validator tasks
- [ ] Domain validation rules have implementation tasks
- [ ] All entity fields are parsable

**Action if missing**:
- ⚠️ **CRITICAL**: Domain spec not fully covered
- Add missing model/validator tasks

#### C. Implementation Plan Alignment Check

```bash
# Read implementation plan
cat specs/toolkit/{toolkit_id}/plan.md
```

**Verify**:
- [ ] Tech stack in tasks matches plan (frameworks, libraries)
- [ ] File structure matches plan's architecture
- [ ] Component interfaces match plan's design

#### D. Source Code Structure Check

```bash
# Check if src/ directory exists
ls src/{package_name}/ 2>/dev/null || echo "New project"
```

**If existing project**:
- **Check** for files that need updating
- **Add** refactoring tasks if needed

#### E. Related Toolkit Specifications Check

```bash
# Find other toolkit specs
find specs/toolkit/ -name "spec.md" | grep -v "{toolkit_id}"
```

**For each related toolkit**:
- **Check** for overlapping functionality
- **Add** integration tasks if needed

#### F. Documentation Check

```bash
# Check documentation
grep -l "{toolkit_id}" docs/*.md README.md AGENTS.md 2>/dev/null || echo "No docs yet"
```

**If found**:
- **Add** documentation update tasks

#### 10. Generate Validation Report

```markdown
## Validation Report

**Task Structure**: ✅ Valid
- Format: All tasks follow standard
- IDs: Sequential (SDD-T001 to SDD-T{N})
- Dependencies: Clear critical path

**Toolkit Spec Alignment**: {✅ Aligned | ⚠️ Mismatched}
- Components: {actual} vs {planned}
- Language: {language} ✓
- Architecture: {type} ✓

**Domain Spec Coverage**: {✅ Complete | ⚠️ Incomplete}
- Entities: {X/Y} have model tasks ({percentage}%)
- Operations: {X/Y} have validator tasks ({percentage}%)
{IF incomplete}: Missing: {list}

**Plan Alignment**: {✅ Aligned | ⚠️ Deviation}
- Tech stack matches plan ✓
- File structure aligned ✓

**Constitution Compliance**: ✅ Compliant
- Entity-First Design: Models before logic ✓
- Spec-First Development: Implementation follows spec ✓
- Progressive Enhancement: MVP-first approach ✓
```

#### 11. Report Completion (Enhanced)

Provide comprehensive summary with validation results and impact analysis:

```
✅ Toolkit implementation task breakdown complete

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

📊 Task Summary:
   Toolkit: {toolkit_id}
   Language: {Python | TypeScript | Go | Rust}
   Architecture: {Monolithic | Modular | Plugin-based}
   Generated: {date}

   Total Tasks: {total_count}
   - Setup & Infrastructure: {setup_count} tasks
   - Models & Entities: {models_count} tasks
   - Parser: {parser_count} tasks
   - Validator: {validator_count} tasks
   - CLI: {cli_count} tasks
   - Tests: {tests_count} tasks
   - Documentation: {docs_count} tasks

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

✅ Validation Results:

   **Task Structure**: ✅ Valid
   - Format: All tasks follow SDD-TXXX [COMP] format
   - IDs: Sequential (SDD-T001 to SDD-T{N})
   - Dependencies: Clear critical path defined

   **Toolkit Spec Alignment**: {✅ Aligned | ⚠️ Mismatched}
   - Components: {actual} vs {planned} components
   - Language: {language} ✓
   - Architecture: {type} ✓
   {IF mismatch}:
   ⚠️  Alignment issues:
   - {Issue description}
   - Action: {Corrective action taken}
   {END IF}

   **Domain Spec Coverage**: {✅ Complete | ⚠️ Incomplete}
   - Domain Spec: specs/domain/{domain_spec_id}/spec.md
   - Entities covered: {X}/{Y} ({percentage}%)
   - Operations covered: {X}/{Y} ({percentage}%)
   {IF incomplete}:
   ⚠️  Coverage gaps:
   - Missing: {list of missing entities/operations}
   - Added tasks: {task_ids} to address gaps
   {END IF}

   **Plan Alignment**: {✅ Aligned | ⚠️ Deviation}
   - Tech stack: {matches | deviates} from plan
   - File structure: {aligned | needs adjustment}
   - Task count: {actual} vs {estimate} ({±X%})

   **Constitution Compliance**: ✅ Compliant
   - Entity-First Design: Models before logic ✓
   - Spec-First Development: Implementation follows spec ✓
   - Progressive Enhancement: MVP → v1.0.0 ✓
   - Automated Quality: {test_count} test tasks included ✓

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

🎯 Impact Analysis:

   **Files Created/Updated**:
   ✅ Created:
   - specs/toolkit/{toolkit_id}/tasks.md (this file)

   **Dependencies** (CRITICAL):
   📄 Domain Specification:
   - specs/domain/{domain_spec_id}/spec.md (REQUIRED)
   - Must exist before implementation

   {IF related_toolkits}:
   🔧 Related Toolkits ({count}):
   - specs/toolkit/{related_id}/spec.md - {relationship}
   {END IF}

   **Source Code Impact**:
   {IF new_project}:
   📦 New Project:
   - Will create: src/{package_name}/
   - Structure: {component_list}
   {ELSE}:
   📝 Existing Project:
   - Will update: {file_count} files
   - May refactor: {refactor_areas}
   {END IF}

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

🔀 Execution Plan:

   **Critical Path** (Sequential):
   1. Setup → Infrastructure, dependencies
   2. Models → Entity definitions from domain spec
   3. Parser → Parse {format} files
   4. Validator → Validate against spec rules
   5. CLI → User interface commands

   **Parallel Opportunities**:
   {IF has_parallel}:
   ⚡ Tests: Can run parallel with implementation
      - Estimated time saving: {percentage}% ({days} days)
   ⚡ Documentation: Can run parallel with tests
      - Estimated time saving: {percentage}% ({days} days)
   {END IF}

   **Checkpoints**:
   - After Phase 2: Models defined and tested
   - After Phase 4: Core validation working
   - After Phase 5: CLI functional
   - After Phase 6: Full test coverage
   - After Phase 7: Documentation complete

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

📦 Release Planning:

   **MVP (v0.1.0)** - Basic Functionality:
   - Components: Parser + Validator + Basic CLI
   - Commands: init, validate
   - Estimated effort: {X} days
   - Goal: Working toolkit for basic use cases

   **v0.2.0** - Enhanced Features:
   - Components: Generator + Advanced validation
   - Estimated effort: +{Y} days
   - Goal: Feature-complete toolkit

   **v1.0.0** - Production Ready:
   - Components: Full CLI + Comprehensive docs
   - Estimated effort: +{Z} days
   - Goal: Production-ready release

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

📁 Generated Files:
   - specs/toolkit/{toolkit_id}/tasks.md (with Task Generation Report)

🔄 Next Steps:
   1. Review tasks.md structure
   2. Verify domain specification exists: specs/domain/{domain_spec_id}/spec.md
   3. Run: /metaspec.sdd.implement
      → This will execute implementation tasks

⚠️  Follow-up TODOs:
   {IF spec_mismatch}:
   - [ ] Resolve toolkit spec alignment issues
   {END IF}
   {IF coverage_gaps}:
   - [ ] Verify domain spec coverage is complete
   {END IF}
   {IF plan_deviation}:
   - [ ] Review why task count differs from plan estimate
   {END IF}
   {IF related_toolkits}:
   - [ ] Check integration with related toolkits
   {END IF}

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

💡 Suggested Commit Message:

   docs(toolkit): add task breakdown for {toolkit_id}
   
   Toolkit: {language}-based {type} architecture
   Components: {component_list}
   Total: {count} tasks
   
   MVP (v0.1.0): {mvp_components}
   Dependencies: specs/domain/{domain_spec_id}/spec.md
   
   {IF validation_warnings}:
   Notes:
   - {warning_1}
   - {warning_2}
   {END IF}
```

## Task Templates

### SETUP Task Template
```
- [ ] T001 [SETUP] Create directory structure:
  - src/[toolkit_name]/
  - tests/unit/
  - tests/integration/
  - templates/
  - memory/
```

### MODELS Task Template
```
- [ ] T006 [MODELS] Define [Entity] model in src/[toolkit]/models.py:
  - Field: name (string, required)
  - Field: [field2] ([type], [required/optional])
  - Validator: [rule1]
  - Validator: [rule2]
```

### PARSER Task Template
```
- [ ] T012 [PARSER] Implement parse_spec() in src/[toolkit]/parser.py:
  - Load YAML/JSON from file path
  - Handle file not found error
  - Handle invalid syntax error
  - Return dict or raise ParseError
```

### VALIDATOR Task Template
```
- [ ] T018 [VALIDATOR] Implement Layer 2 validation in src/[toolkit]/validator.py:
  - Rule: [semantic_rule_1]
  - Rule: [semantic_rule_2]
  - Generate ValidationResult with errors
  - Include fix suggestions in errors
```

### CLI Task Template
```
- [ ] T025 [CLI] Implement `validate` command in src/[toolkit]/cli.py:
  - Argument: spec_file (Path)
  - Option: --strict (bool)
  - Option: --format (text|json)
  - Call parser.parse_spec()
  - Call validator.validate_spec()
  - Output results
  - Exit code: 0 (success), 1 (failure)
```

### TEST Task Template
```
- [ ] T010 [P] [TESTS] Create tests/unit/test_models.py:
  - Test: valid_entity_instantiation
  - Test: missing_required_field_raises_error
  - Test: invalid_field_type_raises_error
  - Test: field_validator_rules
```

## Important Notes

1. **Component-based organization**
   - Not user-story-based (that's for applications)
   - Organize by toolkit components (Parser, Validator, CLI)
   - Each component is independently testable

2. **TDD is recommended**
   - Write tests before implementation
   - Each component has unit tests
   - Integration tests after all components

3. **Follow architecture design**
   - Tasks implement architecture.md designs
   - Parser follows parser-design.md
   - Validator follows validator-design.md

4. **Constitution compliance**
   - Check after each phase
   - Ensure Entity-First (simple models)
   - Ensure Validator Extensibility (plugin system)
   - Ensure AI-Agent Friendly (error messages)

5. **MVP first**
   - Focus on init + validate commands
   - Defer advanced features to v0.2
   - Get working toolkit quickly

## Example: API Test Kit Tasks

### Phase 2: Entity Models
```
- [ ] T006 [MODELS] Create src/api_test_kit/models.py
- [ ] T007 [MODELS] Define APITest model:
  - name: str (required)
  - endpoint: str (required)
  - method: str (required, enum: GET/POST/PUT/DELETE)
  - headers: Optional[Dict[str, str]]
  - body: Optional[Any]
  - assertions: Optional[List[str]]
- [ ] T008 [MODELS] Add method validator (must be valid HTTP method)
- [ ] T009 [MODELS] Add endpoint validator (must start with /)
- [ ] T010 [P] [TESTS] Create tests/unit/test_models.py
- [ ] T011 [P] [TESTS] Test APITest with valid data
- [ ] T012 [P] [TESTS] Test APITest with invalid method
- [ ] T013 [P] [TESTS] Test APITest with invalid endpoint
```

**Checkpoint**: APITest model working, all tests passing

### Phase 3: Parser
```
- [ ] T014 [PARSER] Create src/api_test_kit/parser.py
- [ ] T015 [PARSER] Implement parse_spec(file_path):
  - Load YAML with ruamel.yaml
  - Return dict
  - Raise ParseError on failures
- [ ] T016 [PARSER] Add error handling:
  - FileNotFoundError → clear message
  - YAMLError → show line number
  - EmptyFileError → suggest init command
- [ ] T017 [P] [TESTS] Create tests/unit/test_parser.py
- [ ] T018 [P] [TESTS] Test parse valid YAML
- [ ] T019 [P] [TESTS] Test parse invalid YAML
- [ ] T020 [P] [TESTS] Test parse missing file
```

**Checkpoint**: Parser working, handles all error cases

