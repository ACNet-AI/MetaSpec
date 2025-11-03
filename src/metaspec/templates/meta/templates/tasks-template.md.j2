# Implementation Tasks: [TOOLKIT_NAME]

**Date**: [DATE]  
**Status**: Not Started  
**Plan**: [link to plan.md]  
**Spec**: [link to spec.md]

---

## Overview

**Total Tasks**: [N]  
**Components**: SETUP, MODELS, PARSER, VALIDATOR, CLI, TESTS, DOCS, INTEGRATION  
**Estimated Time**: [X] days  
**MVP Scope**: Phases 1-5 (v0.1.0)

---

## Dependencies

```
SETUP (Phase 1)
  ↓
MODELS (Phase 2)
  ↓
PARSER (Phase 3)
  ↓
VALIDATOR (Phase 4)
  ↓
CLI (Phase 5)
  ↓
DOCS (Phase 6)
  ↓
INTEGRATION (Phase 7)
```

**Component Dependencies**:
- MODELS: Depends on SETUP
- PARSER: Depends on SETUP
- VALIDATOR: Depends on MODELS
- CLI: Depends on PARSER, VALIDATOR
- TESTS: Can run in parallel with implementation
- DOCS: Depends on CLI
- INTEGRATION: Depends on all components

---

## Phase 1: Project Setup ([SETUP])

**Goal**: Initialize project structure and tooling  
**Dependencies**: None  
**Status**: [ ] Not Started | [ ] In Progress | [x] Complete

### Tasks

- [ ] T001 [SETUP] Create directory structure:
  ```
  [toolkit-name]/
  ├── src/[toolkit_name]/
  ├── tests/unit/
  ├── tests/integration/
  ├── tests/fixtures/
  ├── templates/
  └── memory/
  ```

- [ ] T002 [SETUP] Initialize pyproject.toml with:
  - Project metadata (name, version, description)
  - Dependencies (pydantic, typer, pyyaml)
  - Dev dependencies (pytest, mypy, black, ruff)
  - Entry points (CLI command)

- [ ] T003 [SETUP] Configure pytest in pyproject.toml:
  - Test directory: tests/
  - Coverage settings
  - Markers

- [ ] T004 [SETUP] Create .gitignore:
  - Python cache files
  - Virtual environments
  - IDE files
  - Build artifacts

- [ ] T005 [SETUP] Create README.md skeleton:
  - Installation section
  - Usage section
  - Examples section
  - Contributing section

- [ ] T006 [SETUP] Create CHANGELOG.md:
  - Initial version entry
  - Unreleased section

- [ ] T007 [SETUP] Initialize git repository:
  - git init
  - Initial commit

**Checkpoint**: ✅ Project structure created, pytest can run, git initialized

---

## Phase 2: Entity Models ([MODELS])

**Goal**: Define Pydantic models for domain entities  
**Dependencies**: Phase 1 complete  
**Status**: [ ] Not Started | [ ] In Progress | [ ] Complete

### Tasks

- [ ] T008 [MODELS] Create src/[toolkit_name]/models.py

- [ ] T009 [MODELS] Define [PRIMARY_ENTITY] model:
  - Field: [field_1] ([type], required=[yes/no])
  - Field: [field_2] ([type], required=[yes/no])
  - Field: [field_3] ([type], required=[yes/no])
  - Field: [field_4] ([type], required=[yes/no])
  - Field: [field_5] ([type], required=[yes/no])

- [ ] T010 [MODELS] Add field validators:
  - Validator: [field_1] validation rule
  - Validator: [field_2] validation rule
  - Validator: [field_3] validation rule

- [ ] T011 [MODELS] Add model methods:
  - model_dump(): Export to dict
  - model_validate(): Parse from dict
  - model_json_schema(): Generate JSON Schema

- [ ] T012 [MODELS] Add docstrings to model and fields

- [ ] T013 [P] [TESTS] Create tests/unit/test_models.py

- [ ] T014 [P] [TESTS] Test [PRIMARY_ENTITY] instantiation:
  - Test with valid data
  - Test with all fields
  - Test with only required fields

- [ ] T015 [P] [TESTS] Test field validation:
  - Test missing required field raises error
  - Test invalid field type raises error
  - Test [field_1] validator rule
  - Test [field_2] validator rule

- [ ] T016 [P] [TESTS] Test model methods:
  - Test model_dump() output
  - Test model_validate() parsing
  - Test model_json_schema() structure

**Checkpoint**: ✅ Entity models defined, all tests passing, JSON Schema exported

---

## Phase 3: Parser ([PARSER])

**Goal**: Implement YAML/JSON file parser  
**Dependencies**: Phase 1 complete  
**Status**: [ ] Not Started | [ ] In Progress | [ ] Complete

### Tasks

- [ ] T017 [PARSER] Create src/[toolkit_name]/parser.py

- [ ] T018 [PARSER] Implement parse_spec(file_path: Path) -> Dict:
  - Load file with ruamel.yaml (preserves line numbers)
  - Support both .yaml and .json extensions
  - Return parsed dict
  - Raise ParseError on failures

- [ ] T019 [PARSER] Add error handling:
  - FileNotFoundError → ParseError with clear message
  - YAMLError → ParseError with line number
  - EmptyFileError → ParseError with init suggestion
  - JSONDecodeError → ParseError with syntax error

- [ ] T020 [PARSER] Create src/[toolkit_name]/errors.py:
  - Define ParseError exception
  - Define ValidationError exception
  - Add error message formatter

- [ ] T021 [P] [TESTS] Create tests/unit/test_parser.py

- [ ] T022 [P] [TESTS] Create test fixtures:
  - tests/fixtures/valid_specs/simple.yaml
  - tests/fixtures/valid_specs/complex.yaml
  - tests/fixtures/invalid_specs/missing_field.yaml
  - tests/fixtures/invalid_specs/wrong_type.yaml
  - tests/fixtures/invalid_specs/invalid_syntax.yaml

- [ ] T023 [P] [TESTS] Test parse_spec():
  - Test parse valid YAML
  - Test parse valid JSON
  - Test parse file not found
  - Test parse invalid YAML syntax
  - Test parse empty file

- [ ] T024 [P] [TESTS] Test error messages:
  - Test ParseError includes file path
  - Test ParseError includes line number (if YAML)
  - Test ParseError includes fix suggestion

**Checkpoint**: ✅ Parser working, handles all file formats, clear error messages

---

## Phase 4: Validator ([VALIDATOR])

**Goal**: Implement multi-layer validation  
**Dependencies**: Phase 2 complete  
**Status**: [ ] Not Started | [ ] In Progress | [ ] Complete

### Tasks

- [ ] T025 [VALIDATOR] Create src/[toolkit_name]/validator.py

- [ ] T026 [VALIDATOR] Implement Layer 1 (Structural):
  - Use Pydantic model.model_validate()
  - Catch ValidationError
  - Format Pydantic errors into ValidationResult

- [ ] T027 [VALIDATOR] Implement Layer 2 (Semantic):
  - Rule: [semantic_rule_1]
  - Rule: [semantic_rule_2]
  - Rule: [semantic_rule_3]
  - Return ValidationResult with errors

- [ ] T028 [VALIDATOR] Implement Layer 3 (Domain):
  - Rule: [domain_rule_1 from research.md]
  - Rule: [domain_rule_2 from research.md]
  - Rule: [domain_rule_3 from research.md]
  - Return ValidationResult with errors

- [ ] T029 [VALIDATOR] Create ValidationResult class:
  - is_valid: bool
  - errors: List[ValidationError]
  - warnings: List[ValidationWarning]

- [ ] T030 [VALIDATOR] Format error messages:
  - Include: Entity, Field, Value, Issue, Expected, Fix, Example
  - Use consistent format from validator-design.md
  - Ensure AI-friendly (actionable, clear)

- [ ] T031 [VALIDATOR] Add extensibility:
  - register_validator(name, func) function
  - _custom_validators dict
  - Apply custom validators after Layer 3

- [ ] T032 [P] [TESTS] Create tests/unit/test_validator.py

- [ ] T033 [P] [TESTS] Test Layer 1 (Structural):
  - Test valid entity passes
  - Test missing required field fails
  - Test wrong type fails
  - Test invalid enum value fails

- [ ] T034 [P] [TESTS] Test Layer 2 (Semantic):
  - Test [semantic_rule_1]
  - Test [semantic_rule_2]
  - Test [semantic_rule_3]

- [ ] T035 [P] [TESTS] Test Layer 3 (Domain):
  - Test [domain_rule_1]
  - Test [domain_rule_2]
  - Test [domain_rule_3]

- [ ] T036 [P] [TESTS] Test custom validators:
  - Test register_validator()
  - Test custom validator execution
  - Test custom validator error formatting

- [ ] T037 [P] [TESTS] Test error message format:
  - Test error includes all required fields
  - Test fix suggestion is actionable
  - Test example is provided

**Checkpoint**: ✅ All validation layers working, error messages clear, extensible

---

## Phase 5: CLI ([CLI])

**Goal**: Implement command-line interface  
**Dependencies**: Phase 3, Phase 4 complete  
**Status**: [ ] Not Started | [ ] In Progress | [ ] Complete

### Tasks

- [ ] T038 [CLI] Create src/[toolkit_name]/cli.py

- [ ] T039 [CLI] Create Typer app:
  - app = typer.Typer()
  - Add help text
  - Add version callback

- [ ] T040 [CLI] Implement `init` command:
  - @app.command()
  - Argument: output_file (Path)
  - Option: --template (str, default="default")
  - Option: --force (bool)
  - Load template from templates/spec-template.yaml
  - Write to output_file
  - Print success message

- [ ] T041 [CLI] Implement `validate` command:
  - @app.command()
  - Argument: spec_file (Path)
  - Option: --strict (bool)
  - Option: --format (text|json)
  - Call parser.parse_spec()
  - Parse into model
  - Call validator.validate_spec()
  - Format and print results
  - Exit code: 0 (success), 1 (failure)

- [ ] T042 [CLI] Implement output formatters:
  - format_text(result): Human-readable output
  - format_json(result): JSON output
  - Use rich/colorama for colored text (optional)

- [ ] T043 [CLI] Add entry point in pyproject.toml:
  - [project.scripts]
  - [toolkit-name] = "[toolkit_name].cli:app"

- [ ] T044 [P] [TESTS] Create templates/spec-template.yaml:
  - Minimal example entity
  - Comments explaining each field
  - Based on spec.md examples

- [ ] T045 [P] [TESTS] Create tests/integration/test_cli.py

- [ ] T046 [P] [TESTS] Test `init` command:
  - Test creates file
  - Test file contains template content
  - Test --force overwrites existing file
  - Test without --force fails if file exists

- [ ] T047 [P] [TESTS] Test `validate` command:
  - Test with valid spec (exit 0)
  - Test with invalid spec (exit 1)
  - Test --format text
  - Test --format json
  - Test file not found

- [ ] T048 [P] [TESTS] Test output formatting:
  - Test success message format
  - Test error message format
  - Test JSON output structure

**Checkpoint**: ✅ CLI working, init and validate commands functional, tests passing

---

## Phase 6: Documentation & Examples ([DOCS])

**Goal**: Create comprehensive documentation  
**Dependencies**: Phase 5 complete  
**Status**: [ ] Not Started | [ ] In Progress | [ ] Complete

### Tasks

- [ ] T049 [P] [DOCS] Update README.md:
  - Installation instructions (pip, uv, pipx)
  - Quick start guide
  - Usage examples for each command
  - API reference (if applicable)
  - Contributing guide

- [ ] T050 [P] [DOCS] Update AGENTS.md:
  - How AI agents should use toolkit
  - Common workflows
  - Error handling guidance
  - Examples of toolkit usage

- [ ] T051 [P] [DOCS] Create example specs:
  - examples/simple.yaml (minimal example)
  - examples/complex.yaml (full-featured example)
  - examples/README.md (explains examples)

- [ ] T052 [P] [DOCS] Add docstrings:
  - Module docstrings (purpose, usage)
  - Class docstrings (responsibility, attributes)
  - Function docstrings (params, returns, raises)
  - Use Google or NumPy style

- [ ] T053 [P] [DOCS] Update memory/constitution.md:
  - Add implementation notes section
  - Document any constitution deviations
  - Explain design decisions

**Checkpoint**: ✅ Documentation complete, examples working, docstrings added

---

## Phase 7: Integration & Polish ([INTEGRATION])

**Goal**: Integration testing and final polish  
**Dependencies**: All previous phases complete  
**Status**: [ ] Not Started | [ ] In Progress | [ ] Complete

### Tasks

- [ ] T054 [INTEGRATION] Create tests/integration/test_end_to_end.py:
  - Test full workflow: init → edit → validate
  - Test with valid spec
  - Test with invalid spec
  - Test error recovery

- [ ] T055 [INTEGRATION] Performance testing:
  - Test validation < 100ms (typical spec)
  - Test validation < 1s (1000-entity spec)
  - Test memory < 50MB

- [ ] T056 [INTEGRATION] Error message review:
  - Verify all errors have fix suggestions
  - Verify all errors have examples
  - Verify errors are AI-friendly
  - Test with actual AI agent

- [ ] T057 [INTEGRATION] Constitution compliance check:
  - ✅ Entity-First: Model has 3-5 core fields
  - ✅ Validator Extensibility: register_validator() works
  - ✅ Spec-First: Users write specs, not code
  - ✅ AI-Agent Friendly: Error messages actionable
  - ✅ Progressive Enhancement: MVP shipped, features deferred
  - ✅ Domain Specificity: Domain rules from research.md

- [ ] T058 [INTEGRATION] Code quality check:
  - Run mypy --strict (no errors)
  - Run black (code formatted)
  - Run ruff (linting pass)
  - Test coverage > 90%

- [ ] T059 [INTEGRATION] Final testing:
  - Install in fresh virtualenv
  - Test all commands
  - Test with real-world specs
  - Verify documentation accuracy

**Checkpoint**: ✅ All integration tests passing, constitution compliant, ready for release

---

## Parallel Execution Opportunities

### Within Phases

**Phase 2 (MODELS)**:
```bash
# Can run in parallel after T012:
- T013: Create test file
- T014: Test instantiation
- T015: Test validation
- T016: Test methods
```

**Phase 3 (PARSER)**:
```bash
# Can run in parallel after T020:
- T021: Create test file
- T022: Create fixtures
- T023: Test parsing
- T024: Test errors
```

**Phase 4 (VALIDATOR)**:
```bash
# Can run in parallel after T031:
- T032: Create test file
- T033-T037: All test tasks
```

**Phase 5 (CLI)**:
```bash
# Can run in parallel after T043:
- T044: Create template
- T045-T048: All test tasks
```

**Phase 6 (DOCS)**:
```bash
# All docs tasks can run in parallel:
- T049-T053: All doc tasks
```

### Across Phases

```bash
# After Phase 2, can start:
- Phase 3 (PARSER)    # No dependency on MODELS
- Phase 4 (VALIDATOR) # Depends on MODELS

# After Phase 3 and 4, can start:
- Phase 5 (CLI)

# Phase 6 (DOCS) can start anytime after Phase 5
# Phase 7 (INTEGRATION) requires all phases complete
```

---

## MVP Scope (v0.1.0)

**Goal**: Ship working toolkit with core functionality

**Included Phases**:
- ✅ Phase 1: Setup
- ✅ Phase 2: Models
- ✅ Phase 3: Parser
- ✅ Phase 4: Validator (Layers 1-2)
- ✅ Phase 5: CLI (init + validate only)
- ✅ Phase 6: Basic docs

**Deferred to v0.2.0**:
- ⏭️ Phase 4: Domain validation (Layer 3)
- ⏭️ Phase 5: Additional CLI commands
- ⏭️ Phase 6: Comprehensive docs
- ⏭️ Phase 7: Performance optimization

**Estimated Time**: [X] days

---

## Implementation Strategy

### 1. TDD Approach
- Write tests before implementation
- Red → Green → Refactor cycle
- Maintain > 90% test coverage

### 2. Component Isolation
- Complete one component fully before next
- Checkpoint after each phase
- Don't start Phase N+1 until Phase N complete

### 3. Early Integration
- Run integration tests frequently
- Test CLI with real specs early
- Catch integration issues quickly

### 4. Constitution Alignment
- Check principles after each phase
- Document any deviations
- Justify complexity increases

### 5. Incremental Delivery
- Ship MVP (v0.1.0) first
- Gather user feedback
- Add features based on feedback

---

## Progress Tracking

**Overall Status**: [ ] 0% → [ ] 25% → [ ] 50% → [ ] 75% → [ ] 100%

**Phase Completion**:
- [ ] Phase 1: Setup (7 tasks)
- [ ] Phase 2: Models (9 tasks)
- [ ] Phase 3: Parser (8 tasks)
- [ ] Phase 4: Validator (13 tasks)
- [ ] Phase 5: CLI (11 tasks)
- [ ] Phase 6: Docs (5 tasks)
- [ ] Phase 7: Integration (6 tasks)

**Total**: 0 / [N] tasks complete

---

**Last Updated**: [DATE]  
**Status**: Not Started | In Progress | Complete

