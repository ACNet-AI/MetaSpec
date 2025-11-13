---
description: Execute the implementation planning workflow to design toolkit architecture, including parser, validator, and CLI components
---

## User Input

```text
$ARGUMENTS
```

You **MUST** consider the user input before proceeding (if not empty).

## Outline

**Goal**: Transform the specification into a concrete implementation plan with architecture design, component interfaces, and file structure.

**Important**: This command runs AFTER `/metaspec.specify` and `/metaspec.clarify`. It focuses on HOW to implement, not WHAT to build.

**🏗️ Two-Feature Architecture Awareness**

This command must handle two types of specifications:

**Feature 1 (Specification Spec)**: Usually doesn't need a plan.md
- Domain specifications are primarily **documentation**
- No code implementation needed for the specification itself
- **Skip plan generation** unless explicitly requested

**Feature 2 (Toolkit Spec)**: Requires a plan.md
- Defines how to implement Parser, Validator, CLI
- Needs detailed architecture and technical design
- **This is the primary use case for `/metaspec.plan`**

---

### 📖 Navigation Guide (Quick Reference with Line Numbers)

**🎯 AI Token Optimization**: Use `read_file` with `offset` and `limit` to read only needed sections.

**Core Flow** (Read sequentially):

| Step | Lines | Size | Priority | read_file Usage |
|------|-------|------|----------|-----------------|
| 1-2. Load & Validate | 35-68 | 33 lines | 🔴 MUST READ | `read_file(target_file, offset=35, limit=33)` |
| **3. Extract Implementation** ⭐ | 69-98 | 29 lines | 🔴 **KEY** | `read_file(target_file, offset=69, limit=29)` |
| **4. Technical Context** ⭐ | 99-164 | 65 lines | 🔴 **KEY** | See language-specific below ⬇️ |
| 5. Project Structure | 165-220 | 55 lines | 🟡 Important | `read_file(target_file, offset=165, limit=55)` |
| **6-7. Architecture Design** ⭐ | 221-505 | 284 lines | 🔴 **KEY** | See subsections below ⬇️ |
| 8-11. Validate & Report | 506-613 | 107 lines | 🟡 Important | `read_file(target_file, offset=506, limit=107)` |
| 12. Final Report | 614-774 | 160 lines | 🟢 Reference | `read_file(target_file, offset=614, limit=160)` |

**🌐 Section 4: Language-Specific Technical Context** (65 lines):

| Language | Lines | Size | Usage |
|----------|-------|------|-------|
| Python Context | 99-115 | 16 lines | `read_file(target_file, offset=99, limit=16)` |
| TypeScript Context | 116-131 | 15 lines | `read_file(target_file, offset=116, limit=15)` |
| Go Context | 132-147 | 15 lines | `read_file(target_file, offset=132, limit=15)` |
| Rust Context | 148-164 | 16 lines | `read_file(target_file, offset=148, limit=16)` |

**🏗️ Section 6-7: Architecture Design** (284 lines):

| Component | Lines | Size | Usage |
|-----------|-------|------|-------|
| Research Phase | 221-280 | 59 lines | `read_file(target_file, offset=221, limit=59)` |
| Architecture Overview | 287-361 | 74 lines | `read_file(target_file, offset=287, limit=74)` |
| Parser Design | 362-417 | 55 lines | `read_file(target_file, offset=362, limit=55)` |
| Validator Design | 418-505 | 87 lines | `read_file(target_file, offset=418, limit=87)` |

**📋 Templates** (At end of file):

| Template | Lines | Size | Usage |
|----------|-------|------|-------|
| Technical Context Template | 775-783 | 8 lines | `read_file(target_file, offset=775, limit=8)` |
| Research Phase Template | 784-806 | 22 lines | `read_file(target_file, offset=784, limit=22)` |
| Architecture Template | 807-854 | 47 lines | `read_file(target_file, offset=807, limit=47)` |

**💡 Typical Usage Patterns**:
```python
# Quick start: Load + Extract (62 lines)
read_file(target_file, offset=35, limit=62)

# Language-specific: Read only Python context (16 lines)
read_file(target_file, offset=99, limit=16)

# Component-specific: Read Parser design only (55 lines)
read_file(target_file, offset=362, limit=55)

# Architecture: Read full design (284 lines)
read_file(target_file, offset=221, limit=284)

# Template reference: Read specific template (8-47 lines)
read_file(target_file, offset=807, limit=47)  # Architecture
```

**Token Savings**: 
- Full file: 854 lines (~2900 tokens)
- Core flow: 62 lines (~210 tokens) → **93% savings**
- Language-specific: 15-16 lines (~55 tokens) → **98% savings** 🏆
- Component-specific: 55-87 lines (~190-300 tokens) → **90-94% savings**
- Template only: 8-47 lines (~30-160 tokens) → **95-99% savings**

---

### Execution Flow

#### 1. Identify Feature Type and Load Context

**Step 1a: Determine which Feature** you're planning:
- Check current directory: `specs/domain/001-*` or `specs/toolkit/001-*`?
- Read spec.md to understand if it's specification or toolkit

**Step 1b: For Feature 2 (Toolkit Spec)**:
- ✅ Read `specs/toolkit/001-toolkit/spec.md` (the WHAT)
- ✅ **Verify Feature 1 exists**: Check `specs/domain/001-{domain}-spec/spec.md`
- ✅ Read `/memory/constitution.md` (the principles)
- ✅ Create `specs/toolkit/001-toolkit/plan.md` (the HOW)

**Step 1c: For Feature 1 (Specification Spec)** :
- ⚠️ **Ask user**: "Feature 1 is a domain specification and typically doesn't need a plan.md. Are you sure you want to create one?"
- If yes, proceed with simplified planning
- If no, suggest: "Run `/metaspec.plan` in Feature 2 (toolkit spec) instead"

#### 2. Validate Dependencies (Feature 2 Only)

**For Feature 2 (Toolkit Spec)**:

**Critical Validation**:
1. ✅ Feature 1 spec exists at `specs/domain/001-{domain}-spec/spec.md`
2. ✅ Feature 2 spec declares dependency in a **Dependencies** section:
   ```markdown
   ## Dependencies
   - **Depends on**: 001-{domain}-spec
   ```
3. ✅ Components reference Feature 1 validation rules

**If dependencies missing**:
- ⚠️ **Stop and alert**: "Feature 2 must depend on Feature 1. Please update spec.md to add Dependencies section."
- Provide template for adding dependencies

#### 3. Extract Implementation Details from spec.md (NEW 🎯)

**CRITICAL**: Read the "## Implementation" section from `specs/toolkit/001-*/spec.md`:

```bash
# Extract implementation details
grep -A 50 "^## Implementation" specs/toolkit/001-*/spec.md
```

**Extract**:
1. **Primary Language**: Python / TypeScript / Go / Rust / Other
2. **Rationale**: Why this language was chosen
3. **Key Dependencies**: What frameworks/libraries
4. **Structure**: Monolithic / Modular / Plugin-based
5. **Core Components**: Which are included (Parser, Validator, CLI, Generator, SDK)
6. **Extensibility**: How users can extend the toolkit

**Example extracted data**:
```markdown
Primary Language: Python 3.10+
Rationale: Target Python developers, rich ecosystem (Pydantic, Typer)
Key Dependencies:
  - Pydantic 2.0+ (data validation)
  - Typer 0.9+ (CLI)
  - PyYAML (YAML parsing)
Structure: Modular
Core Components: Parser ✓, Validator ✓, CLI ✓, Generator ✗, SDK ✗
Extensibility: Custom validator plugins via entry points
```

#### 4. Fill Technical Context Based on Language

**IMPORTANT**: Design architecture based on the **chosen language** from spec.md, not hardcoded Python.

**For Python Stack**:
```markdown
**Language**: Python {version from spec.md}
**Parser**: PyYAML / ruamel.yaml / pydantic-yaml
**Validator**: Pydantic 2.0+ / marshmallow / cerberus
**CLI Framework**: Typer / Click / argparse
**Testing**: pytest / unittest
**Type Checking**: mypy --strict / pyright
**Package Manager**: pip / poetry / uv
**Documentation**: Markdown + docstrings + Sphinx
```

**For TypeScript Stack**:
```markdown
**Language**: TypeScript {version from spec.md}
**Parser**: js-yaml / yaml / json5
**Validator**: Zod / Yup / io-ts / ajv
**CLI Framework**: Commander.js / yargs / oclif
**Testing**: Vitest / Jest / Mocha
**Type Checking**: tsc --strict
**Package Manager**: npm / pnpm / yarn
**Documentation**: Markdown + TSDoc + TypeDoc
```

**For Go Stack**:
```markdown
**Language**: Go {version from spec.md}
**Parser**: gopkg.in/yaml.v3 / encoding/json
**Validator**: go-playground/validator / go-ozzo/ozzo-validation
**CLI Framework**: cobra / urfave/cli / flag
**Testing**: testing package / testify
**Type Checking**: Built-in
**Package Manager**: go modules
**Documentation**: Markdown + godoc
```

**For Rust Stack**:
```markdown
**Language**: Rust {version from spec.md}
**Parser**: serde_yaml / serde_json
**Validator**: validator / garde
**CLI Framework**: clap / structopt
**Testing**: Built-in test framework
**Type Checking**: Built-in
**Package Manager**: cargo
**Documentation**: Markdown + rustdoc
```

**Custom Context** (from spec.md):
```markdown
**Domain**: [from spec.md]
**Primary Entity**: [from specification spec]
**Validation Strategy**: [from spec.md - based on specification rules]
**Performance Targets**: [from spec.md quality criteria]
**Extensibility Requirements**: [from spec.md - plugin system/hooks]
```

**Mark unknowns as**:
```
[NEEDS CLARIFICATION: specific question]
```

#### 4. Constitution Check

**Extract from constitution.md**:
- Entity-First Design requirements
- Validator Extensibility requirements
- AI-Agent Friendly requirements
- Progressive Enhancement plan
- Domain Specificity constraints

**Evaluate gates**:
- Does planned architecture follow constitution?
- Are there justified exceptions?
- Document any violations with rationale

**GATE**: Must pass before Phase 0 research.

#### 5. Project Structure

**Define toolkit file structure**:

```
[toolkit-name]/
├── README.md
├── AGENTS.md
├── CHANGELOG.md
├── pyproject.toml
├── memory/
│   └── constitution.md
├── specs/
│   ├── spec.md
│   ├── plan.md                    # This file
│   ├── research.md               # Phase 0 output
│   ├── architecture.md           # Phase 1 output
│   └── parser-design.md          # Phase 1 output
├── templates/
│   └── spec-template.yaml        # User spec template
├── src/
│   └── [toolkit_name]/
│       ├── __init__.py
│       ├── models.py             # Pydantic models
│       ├── parser.py             # YAML/JSON parser
│       ├── validator.py          # Validation logic
│       ├── cli.py                # Typer CLI
│       └── errors.py             # Error types
└── tests/
    ├── unit/
    │   ├── test_parser.py
    │   ├── test_validator.py
    │   └── test_models.py
    ├── integration/
    │   └── test_cli.py
    └── fixtures/
        ├── valid_specs/
        └── invalid_specs/
```

#### 6. Phase 0: Domain Research

**Goal**: Research domain standards and conventions before designing architecture.

**Research Tasks**:

1. **Domain Standards**:
   - Task: "Research {domain} industry standards and specifications"
   - Example: For API Testing → REST/GraphQL standards, HTTP RFCs
   - Example: For Design Systems → W3C design tokens, CSS specs

2. **Reference Implementations**:
   - Task: "Find existing {domain} tools and analyze their approaches"
   - Example: For API Testing → analyze Postman, REST Client, etc.
   - Example: For Design Systems → analyze Figma Tokens, Style Dictionary

3. **Validation Patterns**:
   - Task: "Research common validation patterns for {domain}"
   - Example: For API Testing → assertion types, matcher patterns
   - Example: For Design Systems → token naming conventions

4. **Error Message Best Practices**:
   - Task: "Research effective error messages for {domain} tooling"
   - Focus on AI-friendliness and actionable feedback

**Research agents** (run parallel web searches):
```
For each research task:
  - Search for relevant standards, RFCs, or specs
  - Identify common patterns in existing tools
  - Document findings in research.md
```

**Output**: `/specs/research.md`

**Format**:
```markdown
# Domain Research: [Toolkit Name]

## Domain Standards
- Standard 1: {name} - [URL] - [relevance]
- Standard 2: ...

## Reference Implementations
- Tool 1: {name} - [approach] - [lessons learned]
- Tool 2: ...

## Validation Patterns
- Pattern 1: [description] - [example]
- Pattern 2: ...

## Error Message Insights
- Insight 1: [description]
- Insight 2: ...

## Recommendations
- Recommendation 1: [what to adopt]
- Recommendation 2: [what to avoid]
```

#### 7. Phase 1: Architecture Design

**Prerequisites**: research.md complete, no NEEDS CLARIFICATION remaining

**Generate 3 documents**:

##### 6.1 Architecture Overview (`/specs/architecture.md`)

**Content**:
```markdown
# Architecture: [Toolkit Name]

## Component Diagram
[Describe how components interact]

User writes spec.yaml
  ↓
CLI (cli.py) reads file
  ↓
Parser (parser.py) loads YAML
  ↓
Models (models.py) validate structure
  ↓
Validator (validator.py) checks rules
  ↓
CLI outputs results

## Component Responsibilities

### Parser (parser.py)
- Load YAML/JSON files
- Handle file I/O errors
- Preserve line numbers for error reporting
- Return raw dict/list

### Models (models.py)
- Define Pydantic models for entities
- Handle type coercion
- Provide field descriptions
- Export JSON Schema

### Validator (validator.py)
- Structural validation (Pydantic)
- Semantic validation (custom rules)
- Domain-specific validation
- Generate actionable error messages
- Support custom validator plugins

### CLI (cli.py)
- Define commands (init, validate, etc.)
- Handle arguments and options
- Format output (text, JSON)
- Manage exit codes

### Errors (errors.py)
- Custom exception types
- Error formatting utilities
- Fix suggestion generation

## Data Flow

1. User Input → File Path
2. Parser → Raw Data (dict/list)
3. Models → Validated Entity
4. Validator → Validation Result
5. CLI → Formatted Output

## Extension Points

1. Custom Validators:
   - register_validator(name, func)
   - Validator plugins via entry points

2. Custom Commands:
   - Typer command registration
   - Plugin CLI commands

3. Custom Output Formatters:
   - register_formatter(name, func)
```

##### 6.2 Parser Design (`/specs/parser-design.md`)

**Content**:
```markdown
# Parser Design: [Toolkit Name]

## Parser Interface

```python
def parse_spec(file_path: Path) -> Dict[str, Any]:
    """Parse specification file.
    
    Args:
        file_path: Path to YAML/JSON file
        
    Returns:
        Parsed specification as dict
        
    Raises:
        ParseError: If file invalid or syntax error
    """
```

## Error Handling

### File Not Found
```
❌ Error: Specification file not found
  File: spec.yaml
  Current directory: /Users/dev/project
  Fix: Check file path or create file with 'toolkit init spec.yaml'
```

### Invalid YAML
```
❌ Error: Invalid YAML syntax
  File: spec.yaml
  Line: 5
  Issue: Unexpected indentation
  Fix: Ensure consistent indentation (2 or 4 spaces)
```

### Empty File
```
❌ Error: Specification file is empty
  File: spec.yaml
  Fix: Initialize with 'toolkit init spec.yaml' or copy example
```

## Implementation Notes
- Use ruamel.yaml for line number preservation
- Cache parsed specs for performance
- Support both YAML and JSON formats
- Validate UTF-8 encoding
```

##### 6.3 Validator Design (`/specs/validator-design.md`)

**Content**:
```markdown
# Validator Design: [Toolkit Name]

## Validation Layers

### Layer 1: Structural Validation (Pydantic)
- Field types match
- Required fields present
- Enum values valid
- Array/object structures correct

### Layer 2: Semantic Validation (Custom)
- Cross-field dependencies
- Unique constraints
- Reference integrity
- Logic consistency

### Layer 3: Domain Validation (Domain-Specific)
- [Domain rule 1 from research]
- [Domain rule 2 from research]
- [Domain rule 3 from research]

## Validator Interface

```python
class ValidationResult:
    is_valid: bool
    errors: List[ValidationError]
    warnings: List[ValidationWarning]

def validate_spec(entity: EntityModel) -> ValidationResult:
    """Validate entity against all rules.
    
    Args:
        entity: Parsed and type-checked entity
        
    Returns:
        Validation result with errors/warnings
    """
```

## Error Message Format

```
❌ Error: [Error Type]
  Entity: [entity_name]
  Field: [field_path]
  Value: [actual_value]
  Issue: [what's wrong]
  Expected: [what should be]
  Fix: [how to fix it]
  Example: [correct example]
```

## Custom Validator Registration

```python
# In validator.py
_custom_validators: Dict[str, Callable] = {}

def register_validator(name: str, validator: Callable) -> None:
    """Register custom validator."""
    _custom_validators{name} = validator

# User code
from my_toolkit.validator import register_validator

def validate_custom_rule(value, context):
    # Custom validation logic
    return True, None  # is_valid, error_message

register_validator("custom_rule", validate_custom_rule)
```

## Performance Targets
- < 100ms for typical spec (from constitution)
- < 1s for 1000-entity spec
- Memory: < 50MB

## Extensibility
- Plugin system via entry points
- Custom rule registration
- Domain-specific validator subclasses
```

#### 8. Re-evaluate Constitution Check

After Phase 1 design:
- Review architecture against constitution
- Check Entity-First: Is entity model minimal?
- Check Validator Extensibility: Are extension points clear?
- Check AI-Agent Friendly: Are error messages actionable?
- Document any justified deviations

#### 9. Generate Planning Report (NEW)

**Purpose**: Provide comprehensive toolkit planning summary.

**After generating all planning files**, create HTML comment and prepend to plan.md:

```html
<!--
Toolkit Implementation Planning Report
======================================
Toolkit: {spec_id} | Date: {ISO_DATE}
Language: {Python | TypeScript | Go | Rust} | Architecture: {Monolithic | Modular | Plugin-based}

Components:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Parser ({lib}), Models ({framework}), Validator, CLI ({tool}){IF generator}, Generator{END}{IF SDK}, SDK{END}

Tech Stack:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Language: {version} | Testing: {tool} | Type Checking: {tool}
Key Libraries: {count} | Extension Points: {count}

Files Generated:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
plan.md, research.md, architecture.md, {component}-design.md files

Constitution: {✅ Compliant | ⚠️ Check: {issues}}

Next: Review design → Run tasks → Create structure → Set up dev env

Generated by: /metaspec.sdd.plan
-->
```

#### 10. Validation Checklist (NEW)

**Purpose**: Ensure toolkit planning quality.

Run these critical validation checks:

- [ ] **Research & Architecture**: Phase 0 (research.md) + Phase 1 (architecture.md, component designs) completed
- [ ] **Tech Stack**: Language choice justified, all dependencies identified and available
- [ ] **Component Designs**: Parser, Validator designs documented with extension mechanisms
- [ ] **Constitution Compliance**: Entity-First, Spec-First, AI-Agent Friendly, Progressive Enhancement, Automated Quality
- [ ] **Implementation Feasibility**: Architecture realistic, dependencies complete, performance targets achievable
- [ ] **Planning Report**: Prepended at top of plan.md
- [ ] **File Path**: specs/toolkit/{spec_id}/plan.md

### Generate Validation Report

```markdown
Planning Validation Report
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Planning Quality: ✅ PASSED ({score}/5 checks)
- Technical context: ✅
- Research completion: ✅
- Architecture design: ✅
- Component designs: ✅
- Tech stack selection: ✅

Constitution Compliance: ✅ PASSED (6/6 principles)
- Entity-First Design: ✅
- Validator Extensibility: ✅
- Spec-First Development: ✅
- AI-Agent Friendly: ✅
- Progressive Enhancement: ✅
- Automated Quality: ✅

Implementation Feasibility: ✅ PASSED (3/3 checks)
- Language ecosystem: ✅
- Architecture feasibility: ✅
- Dependency completeness: ✅

Overall: {IF all pass: ✅ PLAN APPROVED | IF issues: ⚠️  NEEDS REFINEMENT}

{IF issues}:
⚠️  Issues to Address:
- {Issue 1}
- {Issue 2}

💡 Recommendations:
- {Recommendation 1}
- {Recommendation 2}
```

#### 11. Finalize Plan

**If plan looks good**:
- Prepend Planning Report to plan.md
- All planning files saved
- Proceed to `/metaspec.sdd.tasks`

**If plan needs refinement**:
- Discuss issues with user
- Refine architecture or component designs
- Update planning files
- Re-run validation

#### 12. Output and Report (Enhanced)

**Files Created**:
- `specs/toolkit/XXX-name/plan.md` (with Planning Report prepended)
- `specs/toolkit/XXX-name/research.md` (Phase 0 output)
- `specs/toolkit/XXX-name/architecture.md` (Phase 1 output)
- `specs/toolkit/XXX-name/parser-design.md` (Phase 1 output)
- `specs/toolkit/XXX-name/validator-design.md` (Phase 1 output)

**Report**:
```
✅ Toolkit implementation plan complete

📁 Location:
   specs/toolkit/XXX-name/plan.md

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

📋 Planning Summary:
   Toolkit: {name}
   Domain: {domain}
   Primary Language: {Python | TypeScript | Go | Rust}
   Architecture: {Monolithic | Modular | Plugin-based}
   Primary Entity: {entity}

🔧 Components Planned:
   - Parser: {language parser library}
   - Models: {Pydantic | Zod | Struct-based}
   - Validator: {validation approach}
   - CLI: {Typer | Commander | Cobra | Clap}
   {IF generator}:
   - Generator: {template engine}
   {IF SDK}:
   - SDK: {public API}

📚 Tech Stack:
   Language: {language + version}
   Key Dependencies:
   - {library 1}: {purpose}
   - {library 2}: {purpose}
   ...

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

📁 Generated Files:
   - plan.md (comprehensive implementation plan)
   - research.md (Phase 0: Domain research)
   - architecture.md (Phase 1: Architecture design)
   - parser-design.md (Phase 1: Parser specification)
   - validator-design.md (Phase 1: Validator specification)

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

✅ Validation Results: {IF all pass: APPROVED | IF issues: NEEDS REFINEMENT}

   Planning Quality: ✅ ({score}/5 checks)
   - Technical context: ✅
   - Research completion: ✅
   - Architecture design: ✅
   - Component designs: ✅
   - Tech stack selection: ✅

   Constitution Compliance: ✅ (6/6 principles)
   - Entity-First Design: ✅
   - Validator Extensibility: ✅
   - Spec-First Development: ✅
   - AI-Agent Friendly: ✅
   - Progressive Enhancement: ✅
   - Automated Quality: ✅

   Implementation Feasibility: ✅ (3/3 checks)
   - Language ecosystem: ✅
   - Architecture feasibility: ✅
   - Dependency completeness: ✅

{IF issues}:
   ⚠️  Issues to Address:
   - {Issue 1}
   - {Issue 2}

{IF recommendations}:
   💡 Recommendations:
   - {Recommendation 1}
   - {Recommendation 2}

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

📊 Project Structure (Planned):
   Source: src/{toolkit_name}/
   - __init__.py
   - models.py (from domain spec entities)
   - parser.py (from parser-design.md)
   - validator.py (from validator-design.md)
   - cli.py (from architecture.md)
   {IF components}:
   - {additional files based on components}

   Tests: tests/
   - unit/ (component tests)
   - integration/ (end-to-end tests)
   - fixtures/ (test data)

   Templates: templates/ (if generator)
   Documentation: specs/ (planning files)

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

🔄 Next Steps:

   Immediate:
   1. Review planning files with team
   2. Verify all design decisions
   3. Confirm tech stack availability

   Development:
   - Run /metaspec.sdd.tasks to break down implementation
   - Run /metaspec.sdd.implement to start building
   - Set up development environment
   - Create project structure

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

💡 Suggested commit message:
   docs(plan): add implementation plan for {toolkit-name}
   
   - Language: {language}
   - Components: {count} ({component list})
   - Architecture: {Monolithic | Modular | Plugin-based}
   - Phase 0: Research complete
   - Phase 1: Design complete
```

## Key Rules

1. **No implementation code**
   - This is design, not implementation
   - Show interfaces, not full code
   - Use pseudocode when helpful

2. **Follow constitution**
   - Every design decision must align
   - Document justified exceptions
   - Re-check after Phase 1

3. **Research first**
   - Phase 0 must complete before Phase 1
   - Resolve all NEEDS CLARIFICATION
   - Base design on research findings

4. **Concrete, not vague**
   - Specific file names
   - Clear component responsibilities
   - Actionable error message examples

5. **Extension points first**
   - Design for extensibility from start
   - Clear plugin interfaces
   - Documented registration mechanisms

## Example: API Test Kit Plan

### Technical Context
```markdown
**Domain**: API Testing
**Primary Entity**: APITest
**Validation Strategy**: JSON Schema (structure) + custom rules (assertions)
**Performance Targets**: < 100ms validation, < 5s for 100 tests
**Extensibility**: Custom assertion types, request/response hooks
```

### Research Phase (research.md)
```markdown
## Domain Standards
- RFC 7231 (HTTP/1.1 Semantics): HTTP methods, status codes
- OpenAPI 3.1: API specification format
- JSON Schema: Data validation

## Reference Implementations
- Postman: Collection runner, assertion library
- Rest Assured: Fluent assertion API
- Tavern: YAML-based test definitions

## Validation Patterns
- Assertion library: status, body, headers, performance
- Matcher syntax: exact, contains, regex, jsonpath
- Chaining: multiple assertions per test

## Recommendations
- Adopt HTTP method enum from RFC 7231
- Use JSONPath for body assertions
- Support custom assertion registration
```

### Architecture (architecture.md)
```markdown
## Component Diagram
User writes test.yaml
  ↓
CLI reads file
  ↓
Parser loads YAML
  ↓
APITestModel validates structure
  ↓
Validator checks HTTP semantics
  ↓
CLI outputs validation result / executes test

## Extension Points
1. Custom Assertions: register_assertion("custom", func)
2. Request Hooks: before_request(request) → request
3. Response Hooks: after_response(response) → response
```

## Important Notes

1. **This is toolkit architecture, not end-user app**
   - Design parser/validator, not API endpoints
   - Design CLI commands, not web UI
   - Design entity models, not database schemas

2. **Research is critical**
   - Don't guess domain standards
   - Find and reference actual specs (RFCs, W3C, etc.)
   - Learn from existing tools in the domain

3. **Extension points are mandatory**
   - Constitution requires extensibility
   - Design plugin interfaces early
   - Document registration mechanisms

4. **Error messages are design artifacts**
   - Not implementation details
   - Must be AI-friendly (constitution requirement)
   - Include examples in design docs

5. **Performance targets from constitution**
   - Validation: < 100ms (standard)
   - Memory: < 50MB (standard)
   - Document if different targets needed

