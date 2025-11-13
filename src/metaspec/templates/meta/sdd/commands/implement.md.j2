---
description: Execute toolkit implementation by processing and completing all tasks from tasks.md
---

## User Input

```text
$ARGUMENTS
```

You **MUST** consider the user input before proceeding (if not empty).

## Outline

**Goal**: Execute implementation tasks systematically, following TDD approach, respecting dependencies, and tracking progress.

**Important**: This command runs AFTER `/metaspec:tasks`. It is the execution engine for toolkit development.

---

### 📖 Navigation Guide (Quick Reference with Line Numbers)

**🎯 AI Token Optimization**: Use `read_file` with `offset` and `limit` to read only needed sections.

**Core Execution Flow** (Read sequentially):

| Step | Lines | Size | Priority | read_file Usage |
|------|-------|------|----------|-----------------|
| 1-5. Prerequisites & Setup | 21-167 | 146 lines | 🔴 MUST READ | `read_file(target_file, offset=21, limit=146)` |
| 6. Execute Implementation | 168-209 | 41 lines | 🔴 MUST READ | `read_file(target_file, offset=168, limit=41)` |
| **7. Task Execution Details** ⭐ | 210-302 | 92 lines | 🔴 **KEY** | See subsections below ⬇️ |
| 8-10. Checkpoints & Reporting | 303-394 | 91 lines | 🟡 Important | `read_file(target_file, offset=303, limit=91)` |
| 11-13. Validation & Saves | 395-519 | 124 lines | 🟡 Important | `read_file(target_file, offset=395, limit=124)` |
| 14-15. Propagation & Validation | 520-646 | 126 lines | 🟡 Important | `read_file(target_file, offset=520, limit=126)` |
| 16. Final Report | 647-935 | 288 lines | 🟢 Reference | `read_file(target_file, offset=647, limit=288)` |

**📋 Section 7: Task Execution Details by Language** (92 lines):

| Component | Lines | Size | Usage |
|-----------|-------|------|-------|
| **Python Implementation** | 210-235 | 25 lines | `read_file(target_file, offset=210, limit=25)` |
| **TypeScript Implementation** | 236-261 | 25 lines | `read_file(target_file, offset=236, limit=25)` |
| **Go Implementation** | 262-285 | 23 lines | `read_file(target_file, offset=262, limit=23)` |
| **Rust Implementation** | 286-302 | 16 lines | `read_file(target_file, offset=286, limit=16)` |

**🎯 Phase-Specific Reading** (By component type):

| Phase | Lines | Size | Usage |
|-------|-------|------|-------|
| Setup & Models | 71-142, 210-235 | 97 lines | `read_file(target_file, offset=71, limit=71)` + `offset=210, limit=25` |
| Parser Development | 236-261 | 25 lines | `read_file(target_file, offset=236, limit=25)` |
| Validator Development | 262-285 | 23 lines | `read_file(target_file, offset=262, limit=23)` |
| CLI Development | 286-302 | 16 lines | `read_file(target_file, offset=286, limit=16)` |
| Testing & Docs | 303-362 | 59 lines | `read_file(target_file, offset=303, limit=59)` |

**💡 Typical Usage Patterns**:
```python
# Quick start: Read Prerequisites only (146 lines)
read_file(target_file, offset=21, limit=146)

# Python implementation: Read Python-specific guidance (25 lines)
read_file(target_file, offset=210, limit=25)

# Validation phase: Read validation guidance (124 lines)
read_file(target_file, offset=395, limit=124)

# Specific language: Jump to language section
read_file(target_file, offset=236, limit=25)  # TypeScript
read_file(target_file, offset=262, limit=23)  # Go
read_file(target_file, offset=286, limit=16)  # Rust
```

**Token Savings**: 
- Full file: 935 lines (~3200 tokens)
- Prerequisites only: 146 lines (~500 tokens) → **84% savings**
- Language-specific: 16-25 lines (~60-90 tokens) → **97% savings**
- Phase-specific: 59-97 lines (~200-330 tokens) → **90% savings**

---

### Execution Flow

#### 1. Check prerequisites

**Required files**:
- `specs/toolkit/XXX-name/tasks.md` - Task breakdown
- `specs/toolkit/XXX-name/plan.md` - Architecture design
- `specs/toolkit/XXX-name/spec.md` - Entity definitions

**If missing**:
- Stop and instruct user to run `/metaspec:tasks` first

#### 2. Check checklist status (if exists)

**If** `specs/toolkit/XXX-name/checklists/` directory exists:

1. Scan all checklist files (*.md)
2. Count for each checklist:
   - Total items: Lines matching `- [ ]` or `- [X]` or `- [x]`
   - Completed: Lines matching `- [X]` or `- [x]`
   - Incomplete: Lines matching `- [ ]`

3. Display status table:
   ```
   | Checklist | Total | Completed | Incomplete | Status |
   |-----------|-------|-----------|------------|--------|
   | entity-design.md | 10 | 10 | 0 | ✓ PASS |
   | validator-design.md | 8 | 5 | 3 | ✗ FAIL |
   ```

4. **If any incomplete**:
   - Display table
   - **STOP** and ask: "Some checklists are incomplete. Proceed anyway? (yes/no)"
   - Wait for user response
   - If "no": halt
   - If "yes": continue

5. **If all complete**:
   - Display table
   - Automatically proceed

#### 3. Load implementation context

**Read all design documents**:
- `specs/toolkit/XXX-name/tasks.md` - Task list (REQUIRED)
- `specs/toolkit/XXX-name/plan.md` - Architecture (REQUIRED)
- `specs/toolkit/XXX-name/spec.md` - Entity spec (REQUIRED)
- `specs/toolkit/XXX-name/architecture.md` - Component design (if exists)
- `specs/toolkit/XXX-name/parser-design.md` - Parser interfaces (if exists)
- `specs/toolkit/XXX-name/validator-design.md` - Validation layers (if exists)
- `/specs/research.md` - Domain standards (if exists)

#### 4. Project setup verification

**Verify/create ignore files**:

1. **Check if git repository**:
   ```bash
   git rev-parse --git-dir 2>/dev/null
   ```
   - If yes: Create/verify `.gitignore`

2. **Detect technology from plan.md**:
   - Python: Create/verify `.gitignore` for Python patterns

**Python .gitignore patterns**:
```
# Python
__pycache__/
*.py[cod]
*$py.class
*.so
.Python
env/
venv/
.venv/
ENV/
build/
develop-eggs/
dist/
downloads/
eggs/
.eggs/
lib/
lib64/
parts/
sdist/
var/
wheels/
*.egg-info/
.installed.cfg
*.egg

# Testing
.pytest_cache/
.coverage
htmlcov/
.tox/
.nox/

# IDEs
.vscode/
.idea/
*.swp
*.swo
*~

# OS
.DS_Store
Thumbs.db

# Environment
.env
.env.local
*.env
```

**If .gitignore exists**:
- Verify essential patterns
- Append missing patterns

**If .gitignore missing**:
- Create with full pattern set

#### 5. Parse tasks.md structure

**Extract from tasks.md**:
- Phase list (Setup, Models, Parser, Validator, CLI, Docs, Integration)
- Task list per phase
- Task format: `- [ ] [TID] [P?] [COMP] Description with path`
- Dependencies (sequential vs parallel)

**Build execution plan**:
```
Phase 1: Setup
  - T001 [SETUP] Create directory structure
  - T002 [SETUP] Initialize pyproject.toml
  - ...

Phase 2: Models
  - T008 [MODELS] Create models.py
  - T009 [MODELS] Define Entity
  - T010 [P] [TESTS] Create test_models.py  # Can parallelize
  - T011 [P] [TESTS] Test instantiation       # Can parallelize
  - ...

[Continue for all phases]
```

#### 6. Execute implementation

**Execution rules**:

1. **Phase-by-phase**:
   - Complete Phase N before starting Phase N+1
   - Verify checkpoint after each phase

2. **TDD approach**:
   - Execute test tasks before implementation tasks
   - Example: T010 (create test file) → T006 (implement)

3. **Respect dependencies**:
   - Sequential tasks: Execute in order
   - Parallel tasks `[P]`: Can execute simultaneously
   - Same file: Must be sequential

4. **Progress tracking**:
   - Mark completed tasks: `- [ ]` → `- [x]`
   - Report after each task
   - Save tasks.md after each phase

**Execution order**:

```
Phase 1: Setup
  → Execute T001, T002, T003... sequentially
  → Checkpoint: Project structure created

Phase 2: Models
  → Execute T008, T009 (create models.py, define entity)
  → Execute T010-T016 in parallel (all test tasks)
  → Checkpoint: Entity models working, tests passing

Phase 3: Parser
  → Execute T017-T020 (implement parser)
  → Execute T021-T024 in parallel (test tasks)
  → Checkpoint: Parser working, tests passing

[Continue for all phases]
```

#### 7. Task execution details (ENHANCED 🎯)

**CRITICAL**: Before executing tasks, determine the implementation language and architecture from specs:

```bash
# Extract implementation details from spec.md
grep -A 30 "^## Implementation" specs/toolkit/001-*/spec.md

# Key information to extract:
# - Primary Language: Python / TypeScript / Go / Rust
# - Key Dependencies: Frameworks and libraries
# - Core Components: Which are included (Parser, Validator, CLI, etc.)
# - File Structure: From plan.md
```

**For each task**:

1. **Parse task**:
   - Extract: Task ID, Component, Description, File path
   - Check: Is parallel `[P]`?
   - Check: Is checkpoint task?

2. **Execute task BASED ON LANGUAGE** (NEW 🎯):
   
   **Determine implementation approach**:
   - Read `specs/toolkit/001-*/spec.md` → Get primary language
   - Read `specs/domain/001-*/spec.md` → Get entity definitions
   - Read `specs/toolkit/001-*/plan.md` → Get architecture design
   
   **Generate code according to language**:
   
   **For Python**:
   - **SETUP tasks**: Create files/directories, initialize pyproject.toml
   - **MODELS tasks**: Generate Pydantic models from specification entities
   - **PARSER tasks**: Implement parse_spec() using PyYAML/pydantic-yaml
   - **VALIDATOR tasks**: Implement validation using Pydantic validators
   - **CLI tasks**: Create Typer commands, Rich output formatting
   - **TESTS tasks**: Write pytest tests
   - **DOCS tasks**: Write Markdown + docstrings
   
   **For TypeScript**:
   - **SETUP tasks**: Create files/directories, initialize package.json
   - **MODELS tasks**: Generate Zod schemas or interfaces from specification entities
   - **PARSER tasks**: Implement parseSpec() using js-yaml
   - **VALIDATOR tasks**: Implement validation using Zod/Yup
   - **CLI tasks**: Create Commander.js commands
   - **TESTS tasks**: Write Vitest/Jest tests
   - **DOCS tasks**: Write Markdown + TSDoc
   
   **For Go**:
   - **SETUP tasks**: Create files/directories, initialize go.mod
   - **MODELS tasks**: Generate Go structs from specification entities
   - **PARSER tasks**: Implement ParseSpec() using gopkg.in/yaml.v3
   - **VALIDATOR tasks**: Implement validation using validator package
   - **CLI tasks**: Create Cobra commands
   - **TESTS tasks**: Write Go tests
   - **DOCS tasks**: Write Markdown + godoc
   
   **For Rust**:
   - **SETUP tasks**: Create files/directories, initialize Cargo.toml
   - **MODELS tasks**: Generate Rust structs with Serde from specification entities
   - **PARSER tasks**: Implement parse_spec() using serde_yaml
   - **VALIDATOR tasks**: Implement validation using validator crate
   - **CLI tasks**: Create Clap commands
   - **TESTS tasks**: Write Rust tests
   - **DOCS tasks**: Write Markdown + rustdoc

   **Code Generation Strategy**:
   - Read domain/001-*/spec.md for entity definitions
   - Generate models/types/structs that match specification entities
   - Implement parser that creates instances of these models
   - Implement validator that enforces specification rules
   - Implement CLI commands defined in toolkit spec
   - Follow architecture from plan.md

3. **Verify task**:
   - **SETUP**: Files created, configs valid, dependencies installable
   - **MODELS**: Models instantiable, match specification entities
   - **PARSER**: Can parse valid/invalid specs, error handling works
   - **VALIDATOR**: Enforces all specification rules, error messages clear
   - **CLI**: Commands execute, help text clear, output formatted
   - **TESTS**: Tests pass, coverage adequate
   - **DOCS**: Documentation complete, examples work

4. **Mark complete**:
   - Update tasks.md: `- [ ] T001` → `- [x] T001`
   - Report: "✅ T001 complete: Created directory structure"

5. **Handle errors**:
   - If task fails: Report error, suggest fix
   - If sequential task fails: Halt phase
   - If parallel task fails: Continue others, report at end

#### 8. Phase checkpoints

**After each phase**:

1. **Verify checkpoint criteria**:
   - Phase 1: `✅ Project structure created, tests can run`
   - Phase 2: `✅ Entity models working, all tests passing`
   - Phase 3: `✅ Parser working, handles all error cases`
   - Phase 4: `✅ All validation layers working, error messages clear`
   - Phase 5: `✅ CLI working, init and validate commands functional`
   - Phase 6: `✅ Documentation complete, examples working`
   - Phase 7: `✅ All integration tests passing, constitution compliant`

2. **If checkpoint fails**:
   - Stop phase
   - Report failing criteria
   - Suggest fixes
   - Ask user: "Fix issues and continue? (yes/no)"

3. **If checkpoint passes**:
   - Report success
   - Save tasks.md
   - Proceed to next phase

#### 9. Progress reporting

**After each task**:
```
✅ T001 complete: Created directory structure
   Files created:
   - src/api_test_kit/
   - tests/unit/
   - tests/integration/
   - templates/
   - memory/
```

**After each phase**:
```
✅ Phase 1 complete: Project Setup
   Tasks: 7/7 complete
   Time: 5 minutes
   
   Checkpoint: ✅ Project structure created, tests can run
   
   Next: Phase 2 (Entity Models)
```

**Overall progress**:
```
📊 Implementation Progress: 14/59 tasks (24%)
   Phase 1: ✅ 7/7
   Phase 2: 🔄 7/9 (in progress)
   Phase 3: ⏳ 0/8
   Phase 4: ⏳ 0/13
   Phase 5: ⏳ 0/11
   Phase 6: ⏳ 0/5
   Phase 7: ⏳ 0/6
```

#### 10. Error handling

**Error types**:

1. **File creation error**:
   - Report: Cannot create file [path]
   - Suggest: Check permissions, disk space
   - Action: Fix and retry task

2. **Test failure**:
   - Report: Test [name] failed
   - Show: Test output, error message
   - Suggest: Fix implementation, rerun tests
   - Action: Fix and retry task

3. **Import error**:
   - Report: Cannot import [module]
   - Suggest: Check dependencies, install packages
   - Action: Fix dependencies, retry task

4. **Validation error**:
   - Report: Code doesn't match spec
   - Show: Spec requirement, actual implementation
   - Suggest: Adjust code to match spec
   - Action: Fix and retry task

5. **Constitution violation**:
   - Report: Implementation violates [principle]
   - Show: Principle text, violation
   - Suggest: Refactor to align with principle
   - Action: Ask user to approve deviation or fix

#### 11. Completion validation

**After all phases**:

1. **Verify completeness**:
   - [ ] All tasks marked `[x]`
   - [ ] All checkpoints passed
   - [ ] All tests passing
   - [ ] No linter errors
   - [ ] Constitution compliant

2. **Run final checks**:
   ```bash
   # Run tests
   pytest tests/ --cov

   # Run linter
   mypy src/ --strict
   ruff check src/

   # Test CLI
   [toolkit-name] --help
   [toolkit-name] init test.yaml
   [toolkit-name] validate test.yaml
   ```

3. **Constitution compliance**:
   - ✅ Entity-First: Model has 3-5 core fields
   - ✅ Validator Extensibility: register_validator() works
   - ✅ Spec-First: Users write specs first
   - ✅ AI-Agent Friendly: Error messages actionable
   - ✅ Progressive Enhancement: MVP feature set
   - ✅ Domain Specificity: Domain rules implemented

4. **Generate report**:
   ```
   ✅ Implementation complete
   
   📊 Summary:
   - Total tasks: 59/59 complete
   - Time: 3 days
   - Test coverage: 92%
   - Constitution: COMPLIANT
   
   📦 Deliverables:
   - ✅ Entity models (models.py)
   - ✅ Parser (parser.py)
   - ✅ Validator (validator.py)
   - ✅ CLI (cli.py)
   - ✅ Tests (90% coverage)
   - ✅ Documentation (README, AGENTS.md)
   
   🎯 MVP Status:
   - v0.1.0 ready for release
   - Features: init, validate commands
   - Quality: All tests passing
   
   🔄 Next steps:
   1. Run /metaspec:checklist to verify quality
   2. Test with real-world specs
   3. Update CHANGELOG.md
   4. Create git tag v0.1.0
   5. Publish to PyPI
   
   💡 Suggested commit message:
      feat: implement [toolkit-name] v0.1.0 MVP
   ```

#### 12. Incremental saves

**Save progress frequently**:
- Save tasks.md after each phase
- Commit code after each checkpoint
- Push to git after significant milestones

**Suggested commit messages**:
```bash
git commit -m "feat: complete Phase 1 (Project Setup)"
git commit -m "feat: implement entity models (Phase 2)"
git commit -m "feat: implement parser (Phase 3)"
git commit -m "feat: implement validator (Phase 4)"
git commit -m "feat: implement CLI commands (Phase 5)"
git commit -m "docs: add documentation (Phase 6)"
git commit -m "test: add integration tests (Phase 7)"
```

#### 13. Generate Implementation Report

**Purpose**: Create detailed record of toolkit implementation for quality assurance.

After all tasks complete, create `specs/toolkit/{toolkit_id}/IMPLEMENTATION.md` with HTML comment:

```html
<!--
Toolkit Implementation Report
==============================
Toolkit: {toolkit_id} | Language: {Python | TS | Go | Rust} | Architecture: {Monolithic | Modular | Plugin}
Duration: {start_date} - {end_date} ({days}d)

Summary:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Tasks: {completed}/{total} ({percent}%) | By Phase: Setup: {p1}/{p1t}, Models: {p2}/{p2t}, Parser: {p3}/{p3t}, Validator: {p4}/{p4t}, CLI: {p5}/{p5t}, Tests: {p6}/{p6t}, Docs: {p7}/{p7t}

Files:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Created: {created} files ({loc} LOC) | Updated: tasks.md, README.md, tests ({test_count} files)

Quality:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Test Coverage: {coverage}% | Tests: {unit_tests} unit, {integration_tests} integration, {✅ All pass | ⚠️ {failed} fail}
Linter: {✅ Clean | ⚠️ {count}W | ❌ {count}E} | Type Check: {✅ Pass | ⚠️ {count} issues}
Domain Spec: {implemented}/{total} entities, {implemented}/{total} operations, {implemented}/{total} rules
Completeness: {percent}% | Dependencies: {count} external

Constitution: {✅ Compliant | ⚠️ Check: {issues}}

Next: Run analyze → Fix issues → Publish → Update docs

Generated by: /metaspec.sdd.implement
-->
```

**Also update tasks.md**:
Mark all completed tasks with `[x]`.

#### 14. Consistency Propagation and Impact Analysis

**Purpose**: Verify implementation aligns with specifications and quality standards.

#### A. Domain Specification Compliance Check (CRITICAL)

```bash
# Compare implemented code with domain specification
cat specs/domain/{domain_spec_id}/spec.md

# Check entity implementation
grep "class.*Entity" src/{package}/*.py  # or .ts/.go
```

**Verify**:
- [ ] All domain entities have corresponding model classes
- [ ] All entity fields implemented correctly
- [ ] All domain operations have implementation
- [ ] All validation rules enforced in code

**Action if missing**:
- ⚠️ **CRITICAL**: Domain spec not fully implemented
- Add missing implementations

#### B. Toolkit Specification Alignment Check

```bash
# Verify components match toolkit spec
cat specs/toolkit/{toolkit_id}/spec.md
```

**Verify**:
- [ ] All specified components implemented
- [ ] Language matches spec (Python/TypeScript/Go/Rust)
- [ ] Architecture matches spec (Monolithic/Modular/Plugin)
- [ ] CLI commands match spec

#### C. Code Quality Checks

```bash
# Run linter
{IF Python}:
ruff check src/{package}/
mypy src/{package}/
{ELSE IF TypeScript}:
npm run lint
npm run type-check
{ELSE IF Go}:
go vet ./...
golangci-lint run
{ELSE IF Rust}:
cargo clippy
{END IF}

# Run tests
{IF Python}:
pytest tests/ -v --cov=src/{package}
{ELSE IF TypeScript}:
npm test
{ELSE IF Go}:
go test ./... -cover
{ELSE IF Rust}:
cargo test
{END IF}
```

**Quality gates**:
- [ ] No linter errors
- [ ] Type checking passes
- [ ] All tests passing
- [ ] Test coverage > 80%

#### D. Tasks Status Synchronization

```bash
# Mark all tasks complete in tasks.md
cat specs/toolkit/{toolkit_id}/tasks.md
```

**Update**:
- Mark all tasks `[x]`
- Add completion notes

#### E. Related Files Impact Check

```bash
# Check if domain spec or documentation needs updates
find specs/domain/ docs/ -type f -name "*.md"
```

**If toolkit changes affect**:
- Domain specification → Note for review
- Project documentation → Update README/AGENTS.md

#### 15. Completion Validation (Enhanced)

**Final quality checks**:

```bash
# Comprehensive validation
/metaspec.sdd.analyze
```

**Manual checks**:
- [ ] All CLI commands work correctly
- [ ] Parser handles all input formats
- [ ] Validator enforces all rules from domain spec
- [ ] Error messages are clear and helpful
- [ ] Examples in README work
- [ ] AGENTS.md has complete usage guide
- [ ] Package can be installed successfully

**Code quality final check**:
- [ ] No TODO/FIXME comments left
- [ ] All functions have docstrings
- [ ] All complex logic has comments
- [ ] No debug print statements
- [ ] No hardcoded values (use config)

**Constitution alignment final check**:
- [ ] Models defined before business logic (Entity-First)
- [ ] Validator is extensible (plugins/rules can be added)
- [ ] Implementation strictly follows domain spec (Spec-First)
- [ ] CLI is intuitive for AI agents (AI-Agent Friendly)
- [ ] MVP functional, advanced features optional (Progressive)
- [ ] Comprehensive test coverage (Automated Quality)

#### 16. Report Completion (Enhanced)

Provide comprehensive implementation summary:

```
✅ Toolkit implementation complete

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

📊 Implementation Summary:
   Toolkit: {toolkit_id}
   Language: {Python | TypeScript | Go | Rust}
   Architecture: {Monolithic | Modular | Plugin-based}
   Duration: {start_date} to {end_date} ({days} days)

   Tasks Completed: {completed}/{total} ({percentage}%)
   - Setup & Infrastructure: {phase1_tasks} tasks ✅
   - Entity Models: {phase2_tasks} tasks ✅
   - Parser: {phase3_tasks} tasks ✅
   - Validator: {phase4_tasks} tasks ✅
   - CLI Commands: {phase5_tasks} tasks ✅
   - Tests: {phase6_tasks} tasks ✅
   - Documentation: {phase7_tasks} tasks ✅

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

📁 Files Created/Updated:

   **Created** ({count} files, {loc} lines):
   ✅ Models: src/{package}/models.{ext}
      - {entity_count} entity classes
      - {lines} lines
   
   ✅ Parser: src/{package}/parser.{ext}
      - Parses {format} files
      - {lines} lines
   
   ✅ Validator: src/{package}/validator.{ext}
      - Enforces {rule_count} validation rules
      - {lines} lines
   
   ✅ CLI: src/{package}/cli.{ext}
      - {command_count} commands (init, validate, generate, etc.)
      - {lines} lines
   
   ✅ Tests: tests/ ({test_count} test files)
      - {unit_test_count} unit tests
      - {integration_test_count} integration tests
      - Coverage: {coverage}% ✅

   **Updated**:
   ✅ tasks.md: All tasks marked complete
   ✅ README.md: Usage guide and examples
   ✅ AGENTS.md: AI agent usage patterns
   ✅ IMPLEMENTATION.md: Full implementation report

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

✅ Validation Results:

   **Code Quality**: {✅ Excellent | ⚠️ Good | ❌ Needs Work}
   - Total LOC: {loc} lines
   - Source: {source_loc} lines
   - Tests: {test_loc} lines
   - Test coverage: {coverage}% ✅
   - Linter: {✅ No issues | ⚠️ {count} warnings}
   - Type checking: {✅ Passed | ⚠️ {count} issues}

   **Domain Specification Compliance**: {✅ Complete | ⚠️ Partial}
   - Domain Spec: specs/domain/{domain_spec_id}/spec.md
   - Entities: {implemented}/{total} implemented ({percentage}%)
   - Operations: {implemented}/{total} implemented ({percentage}%)
   - Validation rules: {implemented}/{total} enforced ({percentage}%)
   {IF incomplete}:
   ⚠️  Not fully implemented:
   - Missing: {list}
   - Action: Add in next iteration
   {END IF}

   **Toolkit Specification Alignment**: {✅ Aligned | ⚠️ Deviation}
   - Components: All specified components implemented ✅
   - Language: {language} matches spec ✅
   - Architecture: {type} matches spec ✅
   - CLI commands: {implemented}/{specified} ✅

   **Tests**: {✅ All Passing | ⚠️ {failed} Failing | ❌ Not Run}
   - Unit tests: {unit_passed}/{unit_total} passing
   - Integration tests: {int_passed}/{int_total} passing
   - Coverage: {coverage}% (target: >80%)
   {IF failing_tests}:
   ⚠️  Failing tests:
   - {test_1}: {reason}
   - {test_2}: {reason}
   Action: Fix before release
   {END IF}

   **Constitution Compliance**: {✅ Fully Compliant | ⚠️ Minor Issues}
   - Entity-First Design: {✅ | ⚠️} {comment}
   - Validator Extensibility: {✅ | ⚠️} {comment}
   - Spec-First Development: {✅ | ⚠️} {comment}
   - AI-Agent Friendly: {✅ | ⚠️} {comment}
   - Progressive Enhancement: {✅ | ⚠️} {comment}
   - Automated Quality: {✅ | ⚠️} {comment}

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

🎯 Impact Analysis:

   **Dependencies**:
   📦 External Packages ({count}):
   {FOR each dependency}:
   - {package}: {version}
   {END FOR}

   **Related Files to Review**:
   {IF domain_spec_impact}:
   📄 Domain Specification:
   - specs/domain/{domain_spec_id}/spec.md
   - Review if entity definitions need updates
   {END IF}

   {IF doc_impact}:
   📚 Documentation:
   - README.md: Updated with usage examples ✅
   - AGENTS.md: Added AI agent patterns ✅
   - docs/: {updated_count} files updated
   {END IF}

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

📈 Metrics:

   **Code Statistics**:
   - Total lines: {total_loc}
   - Source code: {source_loc} lines ({percentage}%)
   - Test code: {test_loc} lines ({percentage}%)
   - Documentation: {doc_loc} lines ({percentage}%)
   - Test-to-code ratio: 1:{ratio}

   **Complexity**:
   - Files: {file_count}
   - Classes: {class_count}
   - Functions: {function_count}
   - Average function length: {avg_lines} lines

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

🔄 Next Steps:

   1. Run final analysis:
      → /metaspec.sdd.analyze
      
   2. Generate quality checklist:
      → /metaspec.sdd.checklist
      
   3. Test installation:
      → pip install -e .  # or npm install / go build
      → {package-name} --help
      
   4. Verify CLI commands:
      → {package-name} init
      → {package-name} validate example.yaml
      → {package-name} generate

⚠️  Follow-up TODOs:

   {IF linter_issues}:
   - [ ] Fix linter warnings: {count} issues
   {END IF}
   {IF type_issues}:
   - [ ] Fix type-check issues: {count} issues
   {END IF}
   {IF failing_tests}:
   - [ ] Fix failing tests: {list}
   {END IF}
   {IF coverage_low}:
   - [ ] Improve test coverage: {current}% → 80%+
   {END IF}
   {IF incomplete_impl}:
   - [ ] Complete domain spec implementation: {missing_items}
   {END IF}
   - [ ] Run final quality check: /metaspec.sdd.analyze
   - [ ] Publish package (if ready)

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

💡 Suggested Commit Message:

   feat(toolkit): complete {toolkit_id} implementation
   
   Implementation:
   - Language: {language}
   - Architecture: {type}
   - Components: Parser, Validator, CLI, {others}
   - LOC: {source_loc} source, {test_loc} tests
   
   Quality:
   - Tests: {test_count} tests, {coverage}% coverage
   - Domain spec: {percentage}% implemented
   - Linter: {✅ Clean | ⚠️ {count} warnings}
   
   {IF issues}:
   Known Issues:
   - {issue_1}
   - {issue_2}
   {END IF}
```

## Important Notes

1. **TDD is mandatory**
   - Write tests before implementation
   - Run tests after each implementation
   - Maintain > 90% coverage

2. **Phase isolation**
   - Don't start Phase N+1 until Phase N complete
   - Verify checkpoint after each phase
   - Fix issues before proceeding

3. **Parallel execution**
   - Tasks marked `[P]` can run in parallel
   - Only if they touch different files
   - Report all results together

4. **Constitution alignment**
   - Check principles after each phase
   - Halt if violation detected
   - Get user approval for deviations

5. **Error recovery**
   - Clear error messages
   - Actionable suggestions
   - Allow user to fix and retry

6. **Progress visibility**
   - Report after each task
   - Show percentage complete
   - Estimate time remaining

## Example: Phase 2 Execution

**Phase 2: Entity Models**

```
Starting Phase 2: Entity Models (9 tasks)

✅ T008: Create src/api_test_kit/models.py
   File created: src/api_test_kit/models.py

✅ T009: Define APITest model
   Fields added:
   - name: str (required)
   - endpoint: str (required)
   - method: str (required)
   - headers: Optional[Dict]
   - body: Optional[Any]
   - assertions: Optional[List]

✅ T010: Add field validators
   Validators added:
   - method: Must be GET/POST/PUT/DELETE
   - endpoint: Must start with /

✅ T011: Add model methods
   Methods added:
   - model_dump()
   - model_validate()
   - model_json_schema()

✅ T012: Add docstrings
   Docstrings added for: APITest, all fields

🧪 Running test tasks in parallel...

✅ T013: Create tests/unit/test_models.py
✅ T014: Test APITest instantiation (3 test cases)
✅ T015: Test field validation (4 test cases)
✅ T016: Test model methods (3 test cases)

All tests passing: 10/10 ✅

✅ Phase 2 checkpoint: Entity models working, all tests passing

Phase 2 complete: 9/9 tasks (15 minutes)

Next: Phase 3 (Parser)
```

