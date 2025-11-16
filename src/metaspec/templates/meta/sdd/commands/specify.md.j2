---
description: Define toolkit specification (SDD - Spec-Driven Development)
---

## User Input

```text
$ARGUMENTS
```

You **MUST** consider the user input before proceeding (if not empty).

## Outline

The text the user typed after `/metaspec.sdd.specify` is the **toolkit specification description**. 

**PURPOSE: Toolkit Specification (SDD)** 🎯

This command is for defining **toolkit implementation specifications**:
- Focus: HOW to implement the toolkit
- Output: `specs/toolkit/001-{name}/spec.md`
- Must depend on specification specs
- Implementation-focused

**NOT for specification definition** - Use `/metaspec.sds.specify` for that.

---

### 📖 Navigation Guide (Quick Reference with Line Numbers)

**🎯 AI Token Optimization**: Use `read_file` with `offset` and `limit` to read only needed sections.

**Core Flow** (Read sequentially):

| Step | Lines | Size | read_file Usage |
|------|-------|------|-----------------|
| 1. Setup & Verify | 55-111 | 56 lines | `read_file(target_file, offset=55, limit=56)` |
| 2. Gather Content | 112-191 | 79 lines | `read_file(target_file, offset=112, limit=79)` |
| 3. Generate Sections | 192-1772 | 1580 lines | See components below ⬇️ **LARGE** |
| 4. Write File | 1773-1821 | 48 lines | `read_file(target_file, offset=1773, limit=48)` |
| 5-9. Validate & Report | 1822-2338 | 516 lines | `read_file(target_file, offset=1822, limit=516)` |

**📋 Key Components in Step 3** (Jump to specific components):

| Component | Lines | Size | Priority | Usage |
|-----------|-------|------|----------|-------|
| Overview & Dependencies | 196-298 | 102 lines | 🔴 MUST READ | `read_file(target_file, offset=196, limit=102)` |
| Component 1: Parser | 303-344 | 41 lines | 🟢 Optional | `read_file(target_file, offset=303, limit=41)` |
| Component 2: Validator | 345-389 | 44 lines | 🟢 Optional | `read_file(target_file, offset=345, limit=44)` |
| **Component 3: CLI Commands** ⭐ | 390-663 | 273 lines | 🔴 **KEY** | `read_file(target_file, offset=390, limit=273)` |
| **Component 4: Slash Commands** ⭐⭐ | 664-1612 | 948 lines | 🔴 **LARGE** | See subsections below ⬇️ |
| Component 5: Generator | 1613-1639 | 26 lines | 🟢 Optional | `read_file(target_file, offset=1613, limit=26)` |
| Architecture & Requirements | 1640-1772 | 132 lines | 🟡 Important | `read_file(target_file, offset=1640, limit=132)` |

**🎨 Component 4: Slash Commands Subsections** (Most requested - 948 lines total):

| Subsection | Lines | Size | Usage |
|------------|-------|------|-------|
| Overview & Frontmatter | 664-721 | 57 lines | `read_file(target_file, offset=664, limit=57)` |
| Dual-Source Architecture | 722-766 | 44 lines | `read_file(target_file, offset=722, limit=44)` |
| **Source 1: Custom Commands** ⭐ | 767-1016 | 249 lines | `read_file(target_file, offset=767, limit=249)` |
| Command Templates (3 types) | 1083-1333 | 250 lines | `read_file(target_file, offset=1083, limit=250)` |
| Command Inventory | 1334-1412 | 78 lines | `read_file(target_file, offset=1334, limit=78)` |
| **Source 2: Library Commands** ⭐ | 1413-1559 | 146 lines | `read_file(target_file, offset=1413, limit=146)` |
| Strategy & Integration | 1560-1612 | 52 lines | `read_file(target_file, offset=1560, limit=52)` |

**💡 Typical Usage Patterns**:
```python
# Minimal: Read only Steps 1-2 (135 lines)
read_file(target_file, offset=55, limit=135)

# CLI Design: Read Component 3 (273 lines)
read_file(target_file, offset=390, limit=273)

# Slash Commands Overview: Read Component 4 intro (101 lines)
read_file(target_file, offset=664, limit=101)

# Custom Slash Commands: Read Source 1 (249 lines)
read_file(target_file, offset=767, limit=249)

# Library Slash Commands: Read Source 2 (146 lines)
read_file(target_file, offset=1413, limit=146)
```

**Token Savings**: 
- Full file: 2339 lines (~8000 tokens)
- Targeted reading: 135-500 lines (~500-2000 tokens)
- **Savings: 70-94% tokens** 🎉

---

Follow this execution flow:

### 1. Determine Toolkit and Load Existing Specification

**Step 1a: Verify Specification Dependency (REQUIRED)**

```bash
# Check if specification specs exist
ls specs/domain/ | grep -E '^[0-9]{3}-'
```

**CRITICAL REQUIREMENT**: Toolkit specs MUST depend on at least one specification spec.

If no specification specs exist, **STOP** and show this error:

```
❌ ERROR: Cannot create toolkit without domain specification

MetaSpec is a Spec-Driven framework. Every toolkit MUST depend on a specification.

The specification defines WHAT (domain specification).
The toolkit defines HOW (implementation).

Please run this command first:
  /metaspec.sds.specify "Define {domain} specification"

Then return to create toolkit with:
  /metaspec.sdd.specify "Create {toolkit} for {domain}"

Why this matters:
- Specification is the specification (core asset)
- Toolkit is the implementation (supporting tool)
- Without specification, this becomes a generic code generator
- MetaSpec's value is in spec-driven development
```

**Do not proceed** if no specification specs exist.

**Step 1b: Generate Toolkit Name**

Based on user input, generate:
- Short name: `{domain}-{component}`
- Example: "api-validator", "graphql-parser", "spec-analyzer"
- Check existing `specs/toolkit/` directory structure

**Step 1c: Find Next Available Number**

```bash
# List existing toolkit specs
ls specs/toolkit/ | grep -E '^[0-9]{3}-' | sort -n
# Find next number (e.g., if 001, 002 exist, use 003)
```

**Step 1d: Load Existing or Create New**

- Check for `specs/toolkit/{number}-{name}/spec.md`
- If exists, load for updating
- If new, create new directory structure

### 2. Gather Toolkit Specification Content

**Focus**: Define how to implement tools to support the specification.

**Critical Questions**:

1. **Dependencies**: Which specification specs does this toolkit support?
   - **REQUIRED**: Must reference at least one `domain/XXX-` spec
   - Example: "Depends on: domain/001-api-specification"
   
2. **Toolkit Purpose**: What does this toolkit do?
   - Example: "Parse and validate specification documents"
   
3. **Implementation Language** (NEW - CRITICAL 🎯):
   - **Primary language**: Python / TypeScript / Go / Rust / Other?
   - **Rationale**: Why this language?
     - Target user community (Python devs, TS/JS devs, etc.)
     - Ecosystem fit (existing tools, libraries)
     - Performance requirements
     - Deployment constraints
   - **Secondary languages**: Any additional language support needed?
   
4. **Required Components** (NEW - CRITICAL 🎯):
   Determine which components are needed for this toolkit:
   
   - [ ] **Parser** - Parse specifications from files
     - Needed if: Users write specs in files (YAML/JSON/TOML)
     - Not needed if: Specs are generated programmatically
   
   - [ ] **Validator** - Validate against specification rules
     - Needed if: Need to enforce specification compliance
     - Always recommended for spec-driven toolkits
   
   - [ ] **CLI** - Command-line interface
     - Needed if: Users interact via terminal
     - Provides: init, validate, generate commands
   
   - [ ] **Generator** - Generate code/docs from specs
     - Needed if: Want to automate code generation
     - Examples: Generate TypeScript types, Python classes
   
   - [ ] **SDK/Library** - Programmatic API
     - Needed if: Other tools need to integrate
     - Provides: Python/TS/Go module for importing
   
   **Which are MVP (must have) vs. future enhancements (nice to have)?**
   
5. **Architecture Direction** (NEW 🎯):
   - **Structure**: Monolithic / Modular / Plugin-based?
   - **Dependencies**: What frameworks/libraries?
     - Examples: Pydantic (Python), Zod (TypeScript), encoding/json (Go)
   - **Extensibility**: Plugin system / Hooks / Base classes?
   
6. **Parser Component** (if needed): How will specifications be parsed?
   - Input formats (YAML, JSON, TOML, other)?
   - Output format (Objects, AST, IR)?
   
7. **Validator Component** (if needed): What validation will it perform?
   - Must validate against specification rules
   - What error messages/codes?
   
8. **CLI Commands** (if needed): What commands will users run?
   - Example: `{toolkit-name} init`, `validate`, `generate`
   - What are the inputs/outputs for each command?

9. **Generator Component** (if needed): What will it generate?
   - Output formats: Code (Python/TS/Go), Docs (MD), Config (JSON/YAML)?
   - Templates: Built-in / User-provided / Both?

10. **SDK/Library** (if needed): Will there be programmatic APIs?
    - Public API surface: What functions/classes?
    - Integration: How will other tools use this?

**Important Notes**:
- This is SDD (Spec-Driven Development) - focus on implementation
- Must explicitly depend on specification specs
- For specification definition, use `/metaspec.sds.specify` instead

**If user input is vague**, make informed guesses based on domain standards and document assumptions.

### 3. Generate Toolkit Specification Content

Generate **Toolkit Implementation Specification** with these sections:

#### **Dependencies Section** (REQUIRED - CRITICAL)

**First and foremost**, declare dependencies on domain specifications:

```markdown
## Dependencies

**Domain Specifications**:
- **domain/001-{domain}-specification** - {Brief description of what specification defines}

### Dependency Rationale

{Explain how this toolkit depends on the specification:}
- Which specification entities are parsed/validated?
- Which specification rules are enforced?
- How does the toolkit implement specification operations?

**Important**: 
- This toolkit MUST reference at least one domain specification
- Changes to specification may require updates to this toolkit
- Without specification dependency, this violates the Spec-Driven principle
```

**CRITICAL**: This Dependencies section is mandatory. Toolkit without specification is not a valid speckit.

#### **Toolkit Overview**
```markdown
## Overview

**Name**: {Toolkit Name}
**Version**: {version}
**Status**: Draft | In Development | Stable
**Created**: {date}

**Purpose**: {What this toolkit does}

**Target Specification**: Implements support for domain/001-{domain}-spec

**Primary Use Cases**:
1. {Use case 1}
2. {Use case 2}
3. {Use case 3}

**Example**:
```bash
# How users will use this toolkit
{toolkit-name} init spec.yaml
{toolkit-name} validate spec.yaml
{toolkit-name} generate --output ./generated
```
\```

#### **Implementation Details** (NEW 🎯)
```markdown
## Implementation

### Language & Ecosystem

**Primary Language**: {Python / TypeScript / Go / Rust / Other}

**Rationale**: 
{Why this language was chosen:}
- Target user community: {who will use this}
- Ecosystem fit: {existing tools and libraries}
- Performance considerations: {if relevant}
- Deployment needs: {pip / npm / binary / etc.}

**Key Dependencies**:
- {Framework/library 1}: {Purpose}
- {Framework/library 2}: {Purpose}
- {Framework/library 3}: {Purpose}

### Architecture

**Structure**: {Monolithic / Modular / Plugin-based}

**Core Components**:
- [ ] Parser - {Brief description}
- [ ] Validator - {Brief description}
- [ ] CLI - {Brief description}
- [ ] Generator - {Brief description if included}
- [ ] SDK - {Brief description if included}

**Extensibility**:
{How will users extend this toolkit:}
- Plugin system / Custom validators / Hooks / etc.

**File Structure** (Preliminary):
```
src/
  {package_name}/
    __init__.py         # Package initialization
    models.py           # Data models (if needed)
    parser.py           # Parser component (if needed)
    validator.py        # Validator component (if needed)
    cli.py              # CLI component (if needed)
    generator.py        # Generator component (if needed)
    api.py              # SDK interface (if needed)
```

Note: Actual structure will be refined in `/metaspec.sdd.plan`
\```

#### **Component Specifications**

Define each toolkit component:

##### **Component 1: Parser**

```markdown
### Parser Component

**Purpose**: Parse user specifications into validated objects

**Input Formats**:
- YAML (primary)
- JSON (alternative)
- Python dict (programmatic)

**Output Format**:
- Validated Python object
- AST representation (if needed)

**Parsing Steps**:
1. Load file (YAML/JSON)
2. Validate schema structure
3. Transform to internal representation
4. Return parsed object or errors

**Error Handling**:
- `ParseError`: Invalid YAML/JSON syntax
- `SchemaError`: Missing required fields
- `TypeE Error`: Incorrect field types

**API**:
```python
from {toolkit_name}.parser import parse_spec

# Parse from file
spec = parse_spec("spec.yaml")

# Parse from string
spec = parse_spec(yaml_string, format="yaml")

# Parse from dict
spec = parse_spec(spec_dict, format="dict")
```
\```

##### **Component 2: Validator**

```markdown
### Validator Component

**Purpose**: Validate specifications against specification rules (from domain/001-xxx)

**Validation Rules** (Reference specification spec):
1. {Rule from domain/001-xxx}
2. {Rule from domain/001-xxx}
3. {Rule from domain/001-xxx}

**Validation Levels**:
- **Error**: Violations that prevent usage
- **Warning**: Issues that should be fixed
- **Info**: Suggestions for improvement

**Validation Output**:
```python
ValidationResult(
    valid: bool,
    errors: List[ValidationError],
    warnings: List[ValidationWarning],
    info: List[ValidationInfo]
)
```

**Error Messages**:
- Clear, actionable error messages
- Point to exact location in spec
- Suggest fixes when possible

**API**:
```python
from {toolkit_name}.validator import validate_spec

# Validate parsed spec
result = validate_spec(spec)

if not result.valid:
    for error in result.errors:
        print(f"{error.location}: {error.message}")
```
\```

##### **Component 3: CLI Commands**

**CRITICAL**: CLI commands come from **Toolkit Purpose**, NOT from specification workflow.

```markdown
### CLI Commands

**Key Distinction**:
- **Slash Commands** → From specification workflow (define-requirements, create-design)
- **CLI Commands** → From toolkit function (init, check, list, validate)

---

**STEP 1: Define Toolkit Type**

**Question: What type of tool is this toolkit?**

Select primary toolkit type(s):

- [ ] **Generator/Scaffolder** - Creates projects, initializes structures
  - Example: Specify (`specify init`), MetaSpec (`metaspec init`)
  
- [ ] **Environment Checker** - Verifies system setup, dependencies
  - Example: Specify (`specify check`)
  
- [ ] **Validator** - Validates against specification schemas
  - Example: OpenSpec (`openspec validate`)
  
- [ ] **Query/Reference Tool** - Provides specification information
  - Example: OpenSpec (`openspec show`, `openspec list`)
  
- [ ] **State Manager** - Manages project/spec state
  - Example: OpenSpec (`openspec update`)
  
- [ ] **Community Platform** - Connects to package registry
  - Example: MetaSpec (`metaspec search`, `metaspec install`)

---

**STEP 2: CLI Command Naming Principles**

#### 🏆 Golden Reference: GitHub spec-kit

**Before designing commands, study the gold standard**: [GitHub spec-kit](https://github.com/github/spec-kit)

**Why spec-kit is the reference**:
- ✅ Only 2 commands: `init`, `check`
- ✅ Minimalist but feature-complete
- ✅ Excellent user experience
- ✅ Widely adopted in production

**Key lessons**:
1. `init` provides complete project initialization
2. `check` unifies ALL validation functions (not split into validate/verify/lint)
3. Extend via parameters, don't create new commands
4. Command names are natural and intuitive

**Design principle**: Unless you have a compelling reason, follow spec-kit's minimalist design

---

#### Core Naming Principles

**1. Prioritize Industry Best Practices**

Some command names are **industry standards**, not "fixed names to avoid":

| Standard Command | Use For | Examples |
|-----------------|---------|----------|
| `init` | Project generation | spec-kit, MetaSpec, Specify |
| `check`/`validate` | Validation/verification | spec-kit, OpenSpec |
| `list`/`show` | Query/display | OpenSpec, MetaSpec |
| `search`/`install` | Community platform | MetaSpec, npm, pip |

**✅ DO**: Use standard names when they fit  
**❌ DON'T**: Create unnecessary variations (`examine`, `inspect`, `verify`) just to be "different"

**2. Prefer Unified Commands (spec-kit approach)**

❌ **Don't**: `validate-req`, `validate-design`, `validate-project` (3 commands)  
✅ **Do**: `check <target> [--type TYPE]` (1 unified command)

💡 **See detailed guidelines** in "Unified vs Specialized Commands" section below

---

#### Real Project Examples

| Project | Toolkit Type | Actual Commands | Insight |
|---------|-------------|-----------------|---------|
| **🏆 spec-kit** (GitHub) | Workflow Tool | `init` - Initialize project<br>`check` - Unified validation | **Gold standard**: 2 commands, minimalist design |
| **Specify** | Generator<br>+ Checker | `init` - Create project<br>`check` - Verify tools | Follows spec-kit pattern |
| **OpenSpec** | Validator<br>+ Query<br>+ Manager | `validate` - Check proposal<br>`list` - Show proposals<br>`show` - Display details<br>`update` - Sync state | State-management oriented |
| **MetaSpec** | Generator<br>+ Community | `init` - Generate speckit<br>`search` - Find packages<br>`install` - Get from community<br>`contribute` - Share speckit<br>`list`, `info`, `version` | Community platform (7 commands justified) |

**Key Insight**: spec-kit shows that 2 well-designed commands can be complete

---

#### Unified vs Specialized Commands

**Critical design decision**: When to combine functions into one command vs splitting into multiple commands

**When to UNIFY into one command** ✅:

**1. Similar functions, different objects**
```bash
# ❌ Over-specialized (3 commands)
validate-requirements
validate-design
validate-project

# ✅ Unified (1 command)
check <target> [--type TYPE]
```

**2. Sequential workflow, users run together**
```bash
# ❌ Split (2 commands)
validate
check-transition

# ✅ Unified (1 command)
check [--phase PHASE]
```

**3. Same underlying logic**
```bash
# ❌ Separated (multiple commands)
list-servers
list-tools
list-resources

# ✅ Unified (1 command)
list <entity-type>
```

**When to SPLIT into separate commands** ✅:

**1. Completely different functions**
```bash
# ✅ Keep separate
init      # Creates project
check     # Validates project
# These are fundamentally different operations
```

**2. Different user contexts**
```bash
# ✅ Keep separate  
search    # Browse community (discovery)
install   # Get package (action)
# Users have different mindsets for these
```

**3. Different permission levels**
```bash
# ✅ Keep separate
validate  # Read-only
publish   # Requires credentials
```

**Real-world example: spec-kit's `check` command**

spec-kit unifies ALL validation into one command:
```bash
check requirements
check design  
check project
check transition
# All use the same underlying validation logic
```

This is better than:
```bash
# ❌ Over-engineered
validate-requirements
validate-design
validate-project
check-transition
```

**Command Count Guidance**:

| Toolkit Type | Recommended Count | Rationale |
|-------------|------------------|-----------|
| **Workflow Tool** | 1-2 commands | spec-kit model: `init` + unified `check` |
| **Validator + Query** | 2-3 commands | Add `list`/`show` if needed |
| **Community Platform** | 5-7 commands | Social features need dedicated commands |

⚠️ **Warning**: If you have >7 commands, reconsider if some can be unified

---

**STEP 3: Specification-Influenced CLI Parameters**

**Specification content can influence command parameters** (not command names):

**If specification defines entity types**:
```bash
# Specification has: Server, Tool, Resource entities
{toolkit-name} show <entity-type>     # show server | tool | resource
{toolkit-name} init <entity-type>     # init server | tool
```

**If specification has structured sections**:
```bash
# Specification has: Overview, Entities, Operations, Examples sections
{toolkit-name} docs [section]         # docs entities | docs operations
```

**If specification defines workflow phases**:
```bash
# Specification has: Phase 1, Phase 2, Phase 3
{toolkit-name} status                 # Show current phase
{toolkit-name} next                   # Move to next phase
```

**Key Principle**: 
- Specification influences **parameters and options**
- NOT command names (those come from toolkit purpose)
- Use specification's actual terminology in parameters

---

**STEP 4: Define CLI Implementation**

**For each derived command, specify**:

```markdown
### Command: {command-name}

**Purpose**: {What this command does}

**Usage**:
\```bash
{toolkit-name} {command} [arguments] [options]
\```

**Arguments**:
- arg1: (required) Description
- arg2: (optional) Description

**Options**:
- --option1: Description
- --option2: Description

**Example**:
\```bash
{toolkit-name} {command} example-arg --option1 value
\```

**Implementation Notes**:
- Uses: {library/framework}
- Output: {format}
- Exit codes: 0 (success), 1 (error)
```

---

**CLI vs Slash Commands Summary**

**Key Distinction**:
- **CLI Commands**: Independent tools for developers (validate, list, docs)
- **Slash Commands**: AI execution guides (see **Component 4: Slash Commands** for details)

**Relationship**: Separated by design - no direct calls between them.

**CLI Implementation**: typer (Python) or commander (Node.js) with rich formatting.

```

---

##### **Component 4: Slash Commands - Spec-Driven Execution (CRITICAL for AI-Oriented Tools)**

**Component Structure**:
- **Overview**: What Slash Commands are and dual-source architecture
- **[Source 1](#source-1-specification-derived-commands-custom)**: Specification-Derived Commands (7-STEP process)
- **[Source 2](#source-2-library-selected-commands-reusable)**: Library-Selected Commands (Selection & Adaptation)

**CRITICAL UNDERSTANDING**: Slash Commands are **NOT** CLI usage manuals. They are **spec-driven execution guides** that embed specification knowledge and guide AI to produce spec-compliant outputs.

```markdown
### Slash Commands

**What they are**: Spec-driven execution guides with embedded specification knowledge
**Where they go**: `templates/{source}/commands/` directory (organized by specification system source)  
**How AI uses them**: Via `/` prefix in AI chat (Cursor, Windsurf, etc.)
**Core purpose**: Guide AI to **produce outputs that comply with domain specifications**

**Key Distinction**:
- ❌ **NOT**: "How to call CLI commands" (wrapper documentation)
- ✅ **YES**: "How to execute according to specification specs" (spec-driven guidance)

**When to Include**:
- ✅ Primary users are AI agents
- ✅ Tool enforces a specific specification/specification
- ✅ Outputs must comply with validation rules
- ✅ Multi-step workflows require specification knowledge

---

### 📋 Frontmatter Fields (YAML Metadata)

All slash commands support frontmatter metadata (inspired by [Claude Code slash commands](https://code.claude.com/docs/en/slash-commands)):

| Field | Required | Description | Example |
|-------|----------|-------------|---------|
| `description` | ✅ Yes | Brief description (shown in `/help`) | `"Create feature specification"` |
| `argument-hint` | ⚠️ Recommended | Show expected arguments | `[feature-description]` or `[pr-number] [priority]` |
| `scripts` | Optional | Cross-platform scripts | `sh: scripts/bash/script.sh`<br>`ps: scripts/powershell/script.ps1` |
| `allowed-tools` | Optional | Restrict tools (security) | `Bash(git:*), FileEdit(specs/*)` |
| `model` | Optional | Specify AI model | `claude-3-5-sonnet-20241022` |

**Argument Access Patterns**:
- `$ARGUMENTS` - All arguments as single string (e.g., "arg1 arg2 arg3")
- `$1`, `$2`, `$3` - Individual positional arguments (like shell scripts)
- `{ARGS}` - Escaped for safe script execution

**Example frontmatter**:
\```yaml
---
description: Review pull request with priority
argument-hint: [pr-number] [priority] [assignee]
allowed-tools: Bash(git:*), FileEdit(docs/*)
model: claude-3-5-sonnet-20241022
---
\```

---

### 🎯 Dual-Source Architecture (Composable Spec Systems)

**IMPORTANT**: Slash Commands come from **TWO sources** and can be **composed**:

#### Source 1: Specification-Derived (Custom)
- **From**: SDS domain specification (`specs/domain/`)
- **Nature**: Dynamic, specification-specific, tailored
- **Process**: Analyze specification → Derive commands
- **Examples**: `get-template`, `validate`, workflow actions

#### Source 2: Library-Selected (Reusable)
- **From**: MetaSpec template library (`library/`)
- **Nature**: Pre-built, domain-specific, reusable
- **Process**: Select specification system → Adapt to toolkit
- **Examples**: Generic SD-X, Spec-Kit workflow, OpenSpec evolution

#### Composition Strategy

```
Choose one or combine:

Option A: Specification-Only (Custom)
  → Derive all commands from specification
  → Fully tailored to domain
  → Example: Domain-specific commands from specification phases

Option B: Library-Only (Reusable)
  → Use pre-built spec system
  → Quick start, proven patterns
  → Example: Generic SD-X workflow

Option C: Composed (Recommended)
  → Base: Library spec system
  → Extension: Specification-derived commands
  → Example: Generic workflow + specification-specific commands
```

**MetaSpec's Composability**:
- MetaSpec itself uses `meta/` spec system (19 commands)
- Spec-Kit uses `library/sdd/spec-kit/` spec system
- OpenSpec uses `library/sdd/openspec/` spec system
- Your speckit can choose/compose these systems

---

#### Source 1: Specification-Derived Commands (Custom)

**Overview**: Derive commands by analyzing your domain specification and extracting domain-specific terminology.

---

### 🚨 CRITICAL: Determine Toolkit Type First ⭐ NEW (v0.7.2+)

**Before analyzing specification**, determine toolkit type to avoid generating wrong command patterns.

#### Type A: Data-Access Toolkit (Rare)

**Purpose**: Provide API access to existing data  
**Examples**: REST API client, Database ORM  
**Commands**: Entity operations (CRUD)  
**Pattern**: `/{domain}.{entity}.{operation}`

```bash
# Example: API client
/api.user.get
/api.user.create
/api.post.list
```

**When to use**:
- ❌ Toolkit accesses existing data store
- ❌ Provides CRUD operations on data
- ❌ Not for specification creation

#### Type B: Workflow-Guidance Toolkit (Speckit Standard) ⭐ RECOMMENDED

**Purpose**: Guide users to create and manage specifications  
**Examples**: spec-kit, MetaSpec, domain-specific speckits  
**Commands**: Workflow actions  
**Pattern**: `/{domain}spec.{action}` or `/{domain}.{action}`

```bash
# Example: spec-kit (real project - adapt to your domain)
/speckit.constitution
/speckit.specify
/speckit.clarify
/speckit.plan
/speckit.tasks
/speckit.implement
/speckit.checklist
/speckit.analyze
```

**When to use**:
- ✅ Toolkit guides specification creation (THIS IS WHAT YOU WANT!)
- ✅ Provides workflow commands
- ✅ Follows spec-kit / MetaSpec pattern
- ✅ Reference: MetaSpec itself uses this pattern

#### How to Choose?

**Ask yourself**:

Q: Is this toolkit helping users **create specifications**?  
✅ YES → **Type B: Workflow-Guidance** (Use workflow commands)  
❌ NO → Continue to next question

Q: Is this toolkit providing **API access** to existing data?  
✅ YES → **Type A: Data-Access** (Use entity operations)  
❌ NO → Type B is correct

**Default for Speckits**: ✅ **Type B: Workflow-Guidance**

**🎯 Key Insight**: 
- Domain spec's **entities** = specification structure (WHAT to specify)
- Toolkit's **commands** = workflow actions (HOW to create specs)
- **NOT**: Entity CRUD operations

---

**CHECKPOINT** ⚠️

**Before proceeding to STEP 1, confirm toolkit type**:

- [ ] I have determined this is Type B: Workflow-Guidance toolkit
- [ ] I understand domain entities are specification structures, not data objects
- [ ] I will derive workflow commands, not entity operations
- [ ] I have reviewed MetaSpec's own command structure as reference

**If you selected Type A**: This is rare for speckits. Double-check your decision.

**If you selected Type B**: ✅ Continue to STEP 1 (most common for speckits)

---

**STEP 1: Analyze Domain Specification**

**Before defining Slash Commands**, analyze the SDS domain specification in `specs/domain/`.

**Questions to Ask**:

1. **Specification Complexity**
   - [ ] Does the specification define complex rules and constraints?
   - [ ] Will AI need to reference these rules repeatedly?
   - **If YES** → Need commands to access specification knowledge

2. **Specification Structure** (For Reference Only)
   - [ ] Does the specification define multiple entity types?
   - [ ] Do entities have specific structures (schemas, fields, validation)?
   - **Purpose**: Understand specification complexity
   - **⚠️ CRITICAL - For Type B (Workflow-Guidance) Toolkits**:
     - Entities are **specification structures**, not data objects
     - ❌ Do NOT generate entity operation commands
     - ✅ Instead, generate workflow commands that guide users to create these entities
   - **Example**:
     - Domain spec defines: Project, Campaign, Channel entities
     - ❌ Wrong: Generate `/domain.project`, `/domain.campaign` commands (entity operations)
     - ✅ Right: Generate `/domainspec.constitution`, `/domainspec.specify` commands (workflow actions, adapted from spec-kit pattern)

3. **Validation Rules**
   - [ ] Does the specification specify validation constraints?
   - [ ] Must outputs be validated against schemas?
   - **If YES** → Need validation commands

4. **Workflows & Phases** ⭐ CRITICAL FOR TYPE B

   **For Type B (Workflow-Guidance) toolkits - THIS IS WHAT YOU WANT!**
   
   - [ ] Does the specification define a multi-phase workflow?
   - [ ] Are there specific actions in each phase?
   - **If YES** → ✅ **Derive workflow commands from these phases**
   
   **How to Derive** (MetaSpec's Own Pattern - Dogfooding):
   
   ```
   Specification Workflow Phase → Command Verb → Command Name
   ────────────────────────────────────────────────────────────
   CONSTITUTION principles      → constitution  → /metaspec.sds.constitution
   SPECIFY requirements         → specify       → /metaspec.sds.specify
   CLARIFY ambiguities          → clarify       → /metaspec.sds.clarify
   PLAN architecture            → plan          → /metaspec.sds.plan
   CREATE tasks                 → tasks         → /metaspec.sds.tasks
   IMPLEMENT solution           → implement     → /metaspec.sds.implement
   CHECK quality                → checklist     → /metaspec.sds.checklist
   ANALYZE results              → analyze       → /metaspec.sds.analyze
   ```
   
   **Key Principle**: If specification phases are **verb-able actions**, derive commands directly.
   
   **Example - spec-kit Pattern** (Adapt to Your Domain):
   ```
   Specification Workflow Phase → Command Verb → Command Name
   ────────────────────────────────────────────────────────────
   CONSTITUTION principles      → constitution  → /speckit.constitution
   SPECIFY requirements         → specify       → /speckit.specify
   CLARIFY ambiguities          → clarify       → /speckit.clarify
   PLAN architecture            → plan          → /speckit.plan
   CREATE tasks                 → tasks         → /speckit.tasks
   IMPLEMENT solution           → implement     → /speckit.implement
   CHECK quality                → checklist     → /speckit.checklist
   ANALYZE results              → analyze       → /speckit.analyze
   ```
   
   **🎯 Adaptation Principle**: Use spec-kit's 8-phase workflow as a base, then customize:
   - Keep core phases (constitution, specify, plan, implement)
   - Adapt command names to your domain terminology
   - Add/remove phases based on domain requirements
   - Example: Marketing domain might add "research" or "campaign" phases
   
   **⚠️ Anti-Pattern to Avoid**:
   ```
   ❌ WRONG: Deriving from domain entities
   Domain has: Project, Campaign, Channel
   → Generating: /domain.project, /domain.campaign, /domain.channel
   This creates a data-access tool, not a workflow-guidance tool!
   
   ✅ RIGHT: Deriving from workflow phases (adapt spec-kit pattern)
   Base workflow: constitution → specify → clarify → plan → tasks → implement
   Adapt to domain: Add domain-specific phases as needed
   → Generating: /domainspec.constitution, /domainspec.specify, /domainspec.clarify, etc.
   This creates a workflow-guidance tool (Speckit standard)!
   ```
   
   **Note**: MetaSpec itself was built this way - we eat our own dog food.

5. **Examples & Templates**
   - [ ] Does the specification include examples or templates?
   - [ ] Will AI need to reference these?
   - **If YES** → Need commands to retrieve examples

---

**STEP 1 Checklist** ✅

**Complete this analysis before moving to STEP 2**:

**Specification Understanding**:
- [ ] Identified all specification entities (Server, Tool, Resource, etc.)
- [ ] Listed all specification operations (initialize, list, call, etc.)
- [ ] Documented validation rules (schemas, constraints)

**Workflow Analysis** (CRITICAL):
- [ ] Determined workflow type:
  - [ ] Type A (State Machine): Abstract states → navigation commands
  - [ ] Type B (Action Sequence): Concrete actions/phases → action commands
  - [ ] Type C (Composed): Both patterns
  
**If Type B detected**:
- [ ] Listed all workflow phases/actions
- [ ] Confirmed phases are "verb-able" (can become command verbs)
- [ ] Prepared phase-to-command mapping

**Mapping Example** (for Type B):
```
Specification Phase     → Command Verb → Command Name         → With Namespace
──────────────────────────────────────────────────────────────────────────
SPECIFY feature    → specify      → specify              → sdd.specify
CLARIFY ambiguity  → clarify      → clarify              → sdd.clarify
PLAN architecture  → plan         → plan                 → sdd.plan
IMPLEMENT code     → implement    → implement            → sdd.implement
```

**Why This Matters**:
- ❌ Skipping this analysis → Generic commands without domain context
- ✅ Complete analysis → Simple, memorable commands derived from specification phases
- 💡 Use simple verbs; add namespace if needed; context goes in help text

---

### ⚠️ ANTI-PATTERNS TO AVOID ⭐ NEW (v0.7.2+)

**Before proceeding to command naming**, review these common mistakes:

#### Anti-Pattern 1: Entity-Based Commands (For Type B Toolkits)

**❌ WRONG**:
```bash
# Deriving commands from domain entities
Domain spec defines: Project, Product, Plan, Campaign, Channel
→ Commands: /domain.project, /domain.product, /domain.plan
```

**Why wrong**: This creates a "data-access" tool, not a "workflow-guidance" tool.

**✅ RIGHT**:
```bash
# Deriving commands from workflow phases (adapt spec-kit pattern)
Base pattern: constitution → specify → clarify → plan → tasks → implement
Your domain workflow: (analyze domain workflow phases)
→ Commands: /domainspec.constitution, /domainspec.specify, /domainspec.clarify, etc.
(Customize phase names based on domain terminology)
```

**Key difference**:
- Entity commands = Access/manipulate data objects
- Workflow commands = Guide users through specification creation

#### Anti-Pattern 2: Forgetting MetaSpec's Own Pattern

**MetaSpec itself uses workflow commands**:
- ✅ `/metaspec.sds.specify` (workflow action)
- ❌ NOT `/metaspec.specification.create` (entity operation)

**Your toolkit should follow the same pattern**.

#### Anti-Pattern 3: Missing Workflow Analysis

**If you skipped** the "Workflows & Phases" analysis:
- ⚠️ STOP and go back
- Workflow is the CORE of Type B toolkits
- Without workflow analysis, you'll default to entity commands

---

**🎯 Golden Rule for Type B Toolkits**:

1. **Start with spec-kit pattern** (proven workflow: 8 phases)
2. **Adapt to your domain** (rename phases, add domain-specific steps)
3. **Never derive from entities** (entities are specification structures, not commands)
4. **Always derive from workflow** (phases/actions → commands)

**Example Adaptation**:
```
spec-kit base:      /speckit.constitution → specify → clarify → plan → tasks → implement → checklist → analyze
Marketing domain:   /marketspec.constitution → discover → strategy → design → content → execute → measure → optimize
API Testing domain: /apispec.constitution → define → schema → test → mock → validate → document → deploy
```

**Key insight**: spec-kit's workflow is a template, not a requirement. Customize freely!

---

**STEP 2: Derive Command Names from Specification**

**CRITICAL**: ❌ **DON'T use generic names** (get-spec, get-template, validate)  
            ✅ **DO extract domain-specific names** from specification terminology

**Why This Matters**:
- Generic names lose domain meaning
- Real projects use domain-specific terminology
- Better developer experience with familiar terms

---

**Command Naming Process**:

1. **Read Specification Content**
   - Workflow phases: "Define Server", "Configure Endpoints"
   - Entity names: "Server", "Tool", "Resource"
   - Operations: "Initialize", "Validate", "Deploy"

2. **Extract Verb + Noun Pairs**
   - "Define Server" → verb: define, noun: server
   - "Configure Endpoints" → verb: configure, noun: endpoints
   - "Validate Configuration" → verb: validate, noun: configuration

3. **Form Simple Command Names**
   - Single verbs: `specify`, `plan`, `validate`
   - Or use specification's exact terminology (keep simple)

---

**Real Project Command Naming Patterns**:

| Project | Pattern | Examples | Use Case | Insight |
|---------|---------|----------|----------|---------|
| **MetaSpec** | Namespaced Verbs | `sdd.specify`<br>`sdd.clarify`<br>`sdd.plan`<br>`sdd.implement`<br>`sdd.analyze` | Multi-layer systems | **Simple verbs + namespace** (dogfooding) |
| **OpenSpec** | Domain Verbs | `proposal`<br>`apply`<br>`archive` | Single-domain tools | **Domain-specific single verbs** |

**Key Insights**: 
- ✅ **Two proven patterns**: Use namespaces for multi-layer systems, domain verbs for focused tools
- ✅ **Keep verbs simple**: `specify` not `specify-feature`, `plan` not `plan-implementation`
- ✅ **Context in help text** - not in command names (e.g., `specify --help` shows detailed context)

---

**Command Purpose Categories** (for guidance, NOT fixed names):

| Specification Contains | Command Purpose | Naming Examples | When to Include |
|------------------|----------------|-----------------|-----------------|
| **Workflow phases** | Execute phase actions | MetaSpec: `specify`, `clarify`, `plan`<br>Generic: `design`, `build`, `test` | Always (if workflow exists) |
| **Validation** | Validate outputs | MetaSpec: `analyze`, `checklist`<br>Generic: `validate`, `verify`, `lint` | If validation rules exist |
| **Multi-step process** | Navigate process | Generic: `next`, `status`, `rollback`<br>Lifecycle: `init`, `deploy`, `cleanup` | If state machine workflow |
| **Reference docs** | Access knowledge | Generic: `docs`, `show`, `reference`<br>Query: `list`, `search`, `info` | If complex docs (20+ pages) |

**Key Principle**: Use specification's own vocabulary, don't impose generic names

---

**Quick Reference**:
```markdown
Specification workflow: "Specify Feature" → Command: `specify` (simple verb)
Specification phases: "Plan Architecture" → Command: `plan` (phase becomes command)
Specification validation: "Check Quality" → Command: `checklist` (domain-specific verb)

Key principle: Extract simple verbs from specification phases/actions
```

---

**STEP 3: Classify Commands (Slash + CLI/Script Support)**

**CRITICAL**: Slash Commands are for AI execution. CLI/Scripts provide optional support.

**Command Types** (based on real projects: Spec-Kit, OpenSpec, MetaSpec):

| Type | AI Role | Support | Slash? | CLI? | Script? | Example |
|------|---------|---------|--------|------|---------|---------|
| **Pure-Execution** | Produces content | None | ✅ Yes | ❌ No | ❌ No | `define-requirements` |
| **Script-Assisted** | Produces content | Shell scripts | ✅ Yes | ❌ No | ✅ Yes | Spec-Kit's `specify` |
| **CLI-Referenced** | Produces + validates | Independent CLI | ✅ Yes | ✅ Yes | ❌ No | OpenSpec's `proposal` |

**Classification Decision Tree**:

```
For each derived command, ask:

1. Does AI need to produce structured content?
   ✅ YES → Continue to Q2
   ❌ NO → This is likely a pure CLI tool (skip Slash)

2. Does it need file system setup (directories, skeleton)?
   ✅ YES → Script-Assisted (create helper script)
   ❌ NO → Continue to Q3

3. Should output be validated independently?
   ✅ YES → CLI-Referenced (create validate CLI)
   ❌ NO → Pure-Execution (Slash only)
```

**Key Insights from Real Projects**:

- **Spec-Kit**: Uses shell scripts for setup, AI for content
  ```bash
  /speckit.specify → calls create-new-feature.sh → AI fills content
  ```

- **OpenSpec**: AI produces, CLI validates independently
  ```bash
  /openspec.proposal → AI creates → User runs: openspec validate <id>
  ```

- **MetaSpec**: Pure AI execution, CLI for other purposes
  ```bash
  /metaspec.sdd.specify → AI produces spec.md (no CLI needed)
  metaspec init → Separate CLI for generation
  ```

**Classification Result**:

```markdown
For each derived command, classify as:

- **Pure-Execution**: AI produces content → Slash only
  - Example: specify, plan, design (most common)
  
- **Script-Assisted**: Need structure setup → Script + Slash
  - Example: init-project (if creating directories)
  
- **CLI-Referenced**: Need independent validation → CLI + Slash
  - Example: validate command (See **Component 3, STEP 2: Derive CLI Commands from Toolkit Purpose** for CLI design)

**Typical Counts**:
- Slash Commands: 4-8
- Helper Scripts: 1-2 (if Script-Assisted)
- CLI Commands: 3-5 (if CLI-Referenced, defined in Component 3)
```

---

**STEP 4: Implement Support Tools (CLI + Scripts)**

**IMPORTANT**: CLI commands should be fully defined in **Component 3: CLI Commands** first.  
This section covers implementation of support tools specifically for Slash Commands.

**Cross-Reference**: See **Component 3: CLI Commands** for complete CLI command specification.

**This section covers**:
- 4a. CLI Commands (CLI-Referenced Pattern only - subset of Component 3)
- 4b. Helper Scripts (Script-Assisted Pattern only)

---

**Implement based on command classification**:

**4a. CLI Commands (CLI-Referenced Pattern)**

**Cross-Reference**: This is a subset of CLI commands defined in **Component 3: CLI Commands**.

**Context**: When STEP 3 identifies "CLI-Referenced Pattern" commands, implement the associated CLI tools here.

**From Component 3**: Follow the **CLI Command Derivation Process** (Component 3, STEP 1-4) to fully define these CLI commands before implementing.

**Purpose**: Independent tools for validation, querying, display

```markdown
### CLI Implementation Checklist

**Independent CLI Tools** (user calls directly):

Based on your toolkit functions (from **Component 3, STEP 1: Define Toolkit Type**), implement:

- [ ] **Validation**: validate <file>, check, lint
  - Validate against specification schema
  - Independent verification tool

- [ ] **Information Display**: show [section], docs <topic>, help
  - Display specification documentation
  - Provide reference information

- [ ] **Query**: list {type}, info
  - List available entities/examples
  - Show specification information

**Naming Reminder**:
- ❌ Don't hardcode: get-spec, get-template, get-example
- ✅ Choose intuitive: show, docs, list, help
- ✅ Or domain-specific: show-spec, list-entities

**Implementation Guidelines**:
- These are **standalone tools**, not called by Slash Commands
- Focus on validation, querying, displaying
- Should work without AI involvement
- Users call them directly after AI produces content
```

**4b. Helper Scripts (Script-Assisted Only)**

**Purpose**: Set up file structure, create skeletons

```markdown
### Script Implementation Checklist

**Helper Scripts** (called by Slash Commands):
- [ ] scripts/setup-project.sh: Create project structure
- [ ] scripts/init-entity.sh <entity>: Create entity skeleton
- [ ] scripts/check-prerequisites.sh: Verify environment

**Script Guidelines**:
- Keep scripts simple (directory creation, file copying)
- AI does content production, scripts do structure
- Example from Spec-Kit:
  ```bash
  # scripts/setup-project.sh
  mkdir -p specs/ templates/ docs/
  cp templates/spec-template.md specs/
  echo "Structure ready for AI to fill"
  ```
```

**Key Principle**: **Slash Commands don't "call" CLI**. CLI and Scripts are separate support tools.

---

**STEP 5: Create Spec-Driven Slash Commands (All Types)**

**Based on classification in STEP 3**, create appropriate Slash Command templates for each type.

**Reference**: See **STEP 3: Classify Commands** above for command type definitions (Pure-Execution, Script-Assisted, CLI-Referenced).

---

##### Template 1: Pure-Execution Slash Commands (Most Common)

```markdown
---
description: Brief description of what this command does
argument-hint: [arg1] [arg2]  # Optional: show expected arguments
allowed-tools: Bash(git:*), FileEdit(specs/*)  # Optional: restrict tools
model: claude-3-5-sonnet-20241022  # Optional: specify model
---

# /{toolkit-name}.{command}

## User Input

\```text
$ARGUMENTS
\```

You **MUST** consider the user input before proceeding (if not empty).

**Argument Access**: `$ARGUMENTS`, `$1`, `$2`, `$3` (see [Frontmatter Fields](#frontmatter-fields-yaml-metadata) above)

## Purpose
{What specification-compliant output to produce}

## Domain Specification (EMBEDDED)
**From**: specs/domain/{XXX}/spec.md

### Entity Structure
[Copy entity definition from specification]
- field1: type (required) - description
- field2: type (optional) - description
- Constraints: [Specification constraints]

### Validation Rules
- VR001: {Rule from specification}
- VR002: {Rule from specification}

### Examples
[Specification examples]

## AI Execution Steps
1. **Understand User Intent**
   - Extract key information
   - Map to specification entity

2. **Apply Specification Rules**
   - Check constraint 1
   - Ensure constraint 2

3. **Structure Output**
   - Follow entity schema
   - Include required fields

4. **Self-Validate**
   - Verify against specification rules
   - Check all constraints met

## Output Template
\```json
{
  "field1": "...",  // From specification
  "field2": "..."   // Validated against VR001
}
\```

## Validation (Optional)
User can validate output independently:
\```bash
{toolkit-name} validate output.json
\```

## Related Commands
- /{toolkit}.get-spec - Reference full specification (if exists)
```

**Example**: MetaSpec's `/metaspec.sdd.specify`, OpenSpec's `/openspec.proposal`

---

##### Template 2: Script-Assisted Slash Commands (Spec-Kit Pattern)

```markdown
---
description: Brief description of what this command does
argument-hint: [arg1] [arg2]  # Optional: show expected arguments
scripts:
  sh: scripts/bash/{script-name}.sh --json "{ARGS}"
  ps: scripts/powershell/{script-name}.ps1 -Json "{ARGS}"
allowed-tools: Bash(*), FileEdit(*)  # Scripts need broader permissions
model: claude-3-5-sonnet-20241022  # Optional: specify model
---

# /{toolkit-name}.{command}

## User Input

\```text
$ARGUMENTS
\```

You **MUST** consider the user input before proceeding (if not empty).

**Argument Access**: `$ARGUMENTS`, `$1`, `$2`, `$3`, `{ARGS}` (see [Frontmatter Fields](#frontmatter-fields-yaml-metadata) above)

## Purpose
{What to produce, with script handling setup}

## Helper Script

**Cross-platform execution**:
\```bash
# Linux/Mac
scripts/bash/{script-name}.sh --json "$ARGUMENTS"

# Windows
scripts/powershell/{script-name}.ps1 -Json "$ARGUMENTS"
\```

**Script Purpose**: Set up file structure, create skeleton

## Domain Specification (EMBEDDED)
**From**: specs/domain/{XXX}/spec.md

[Copy relevant specification sections like Pure-Execution template]

## Execution Flow
1. **Call Helper Script**
   \```bash
   scripts/setup-{entity}.sh --name {entity-name}
   \```
   - Script creates: Directory structure, skeleton files
   - Script outputs: Paths to files AI should fill

2. **AI Produces Content**
   - Read script output (file paths)
   - Load domain specification
   - Fill skeleton with specification-compliant content

3. **Verify Structure**
   - Check all required files created
   - Validate against specification

## Output
- Structure: Created by script
- Content: Produced by AI

## Related Commands
- /{toolkit}.validate - Validate final output
```

**Example**: Spec-Kit's `/speckit.specify` (calls `create-new-feature.sh`)

---

##### Template 3: CLI-Referenced Slash Commands (Validation Reminder)

**Purpose**: Remind AI to suggest CLI validation after production

```markdown
---
description: Validate output against domain specifications
argument-hint: [file-to-validate]  # Optional: show expected arguments
allowed-tools: Bash({toolkit-name}:validate:*)  # Only allow validation tools
model: claude-3-5-haiku-20241022  # Can use lighter model for simple reminders
---

# /{toolkit-name}.validate

## User Input

\```text
$ARGUMENTS
\```

**Argument Access**: `$ARGUMENTS`, `$1` (see [Frontmatter Fields](#frontmatter-fields-yaml-metadata) above)

## Purpose
Remind AI to suggest validation after producing content

## When to Use
After AI has produced output via Pure-Execution commands

## What AI Should Do
1. Acknowledge content production complete
2. Suggest validation to user:
   \```
   "Content created successfully!
   
   To validate against {specification-name} schema, run:
     {toolkit-name} validate <file>
   "
   \```

## Available CLI Commands
- `{toolkit-name} validate <file>` - Validate against schema
- `{toolkit-name} get-spec` - View specification details
- `{toolkit-name} list` - List available entities

## Note
This Slash Command doesn't "call" CLI directly.
It teaches AI to suggest appropriate CLI commands to users.
```

**Example**: After `/speckit.define-requirements`, AI suggests `speckit validate requirements.json`

---

**STEP 6: Workflow-Specific Commands (Type B Only)**

**If specification defines Type B Workflow (Action Sequence)**, these workflow actions become **Pure-Execution Slash Commands**:

```markdown
Specification Workflow Example:
  phases:
    - Requirements:
        actions:
          - define_requirements   ← Action (verb)
          - clarify_requirements  ← Action (verb)
    - Design:
        actions:
          - create_design         ← Action (verb)
          - review_design         ← Action (verb)

Command Classification:
  - define-requirements → Pure-Execution (AI produces)
  - clarify-requirements → Pure-Execution (AI refines)
  - create-design → Pure-Execution (AI produces)
  - review-design → Pure-Execution (AI reviews)

Each Slash Command contains:
  - Specification knowledge for that phase
  - Entity structure for that artifact
  - Spec-driven execution steps
  - Validation rules for outputs
  - No CLI needed (AI produces directly)
```

**Judgment Rule**: 
- Workflow step is a **verb/action** → Pure-Execution Slash Command
- Workflow step is a **noun/state** → CLI-Backed navigation commands (`get-workflow`, `next-phase`)

---

**STEP 7: Final Command Inventory**

**Summarize all derived and classified commands**:

```markdown
## Command Inventory

### CLI Commands (Total: X)

**CLI-Backed** (Y commands):
- [ ] get-spec: Read specification files
- [ ] get-template: Read entity templates
- [ ] validate: Execute validation logic
- [ ] get-workflow: Query workflow state
- [ ] get-example: Read examples

**Hybrid** (Z commands):
- [ ] init: Create project structure

**Total CLI**: X = Y + Z

### Slash Commands (Total: X+N)

**CLI-Backed** (Y commands - matches CLI):
- [ ] /{toolkit}.get-spec.md
- [ ] /{toolkit}.get-template.md
- [ ] /{toolkit}.validate.md
- [ ] /{toolkit}.get-workflow.md
- [ ] /{toolkit}.get-example.md

**Hybrid** (Z commands - matches CLI):
- [ ] /{toolkit}.init.md

**Pure-Execution** (N commands - NO CLI):
- [ ] /{toolkit}.define-requirements.md
- [ ] /{toolkit}.clarify-requirements.md
- [ ] /{toolkit}.create-design.md
- [ ] /{toolkit}.generate-code.md
- ... (from workflow actions)

**Total Slash**: X + N
```

**Key Ratios**:
- CLI commands: 5-10 typical
- Slash commands: 10-20 typical
- Slash > CLI (this is expected!)

**Priority Guide**:
- P0 (Critical): get-spec, get-template, validate, workflow actions
- P1 (Important): get-workflow, get-example, init
- P2 (Skip): info, version (use CLI --help instead)

---

**Design Principles: Spec-Driven Execution**

1. **Embed Specification Knowledge**
   - ✅ Include entity definitions from specification
   - ✅ Copy validation rules into commands
   - ✅ Provide specification examples
   - ❌ Don't just say "call this CLI"

2. **Guide Spec-Compliant Production**
   - ✅ Show how to structure outputs per specification
   - ✅ Explain how to apply validation rules
   - ✅ Provide output templates from specification
   - ❌ Don't just describe CLI parameters

3. **Validate Against Specification**
   - ✅ Include validation checklists from specification
   - ✅ Self-check steps for AI
   - ✅ Clear compliance criteria
   - ❌ Don't rely on external validation only

**Quality Checklist**:
- [ ] Embeds specification knowledge (entities, rules, constraints)
- [ ] Guides spec-compliant output production
- [ ] Includes validation rules from specification
- [ ] Provides specification-based templates
- [ ] AI can produce compliant output without external reference

**Summary**: Source 1 provides a 7-STEP process to derive custom Slash Commands from your domain specification, ensuring domain-specific terminology and spec-driven execution.

---

#### Source 2: Library-Selected Commands (Reusable)

**Overview**: Select and adapt pre-built specification systems from MetaSpec's template library.

**Alternative/Complement to Specification-Derived**: Use pre-built specification systems from MetaSpec library.

**Why Simpler Process?**  
Unlike Source 1 (derive from scratch), Source 2 reuses proven commands. The process is:
1. **Select** appropriate library (based on domain/workflow)
2. **Adapt** variables to your domain
3. **Integrate** into your speckit

This is intentionally simpler than Source 1's 7-STEP derivation process.

---

**Discover Available Libraries**

**Library Location**: MetaSpec GitHub repository

**To explore available specification systems**:

1. **Browse library catalog online**:
   ```
   https://github.com/ACNet-AI/MetaSpec/tree/main/src/metaspec/templates/library
   ```

2. **Read library README**:
   ```
   https://github.com/ACNet-AI/MetaSpec/blob/main/src/metaspec/templates/library/README.md
   ```

3. **View specific library**:
   ```
   https://github.com/ACNet-AI/MetaSpec/tree/main/src/metaspec/templates/library/{library-name}
   ```

**Each library provides**:
- Pre-built Slash Commands
- Proven workflow patterns
- Domain-specific or universal abstractions
- Adaptation guidelines

**Selection Principles**

**Choose library based on**:

1. **Domain Match**
   - Software development → Look for SDD libraries
   - Design/Testing/Documentation → Look for generic/universal libraries
   - Specific specifications → Look for specification-specific libraries

2. **Abstraction Level**
   - Need pure abstraction → Choose generic/universal
   - Need domain concepts → Choose specialized (e.g., sdd/*)
   - Need specification-specific → Choose specification libraries

3. **Workflow Type**
   - Greenfield (from scratch) → Greenfield workflows
   - Brownfield (evolution) → Evolution/change management workflows
   - Both → Compose multiple libraries

4. **Complexity**
   - Simple toolkit → Start with generic
   - Complex domain → Use specialized library
   - Uncertain → Start generic, specialize later

**Quick Reference (Current Libraries)**

**See [library/README.md](https://github.com/ACNet-AI/MetaSpec/blob/main/src/metaspec/templates/library/README.md) for complete catalog.**

**Common libraries include**:

- [`generic/`](https://github.com/ACNet-AI/MetaSpec/tree/main/src/metaspec/templates/library/generic) - Universal SD-X (domain-agnostic)
- [`sdd/spec-kit/`](https://github.com/ACNet-AI/MetaSpec/tree/main/src/metaspec/templates/library/sdd/spec-kit) - Software development (greenfield)
- [`sdd/openspec/`](https://github.com/ACNet-AI/MetaSpec/tree/main/src/metaspec/templates/library/sdd/openspec) - Specification evolution (brownfield)

**As library grows, refer to [online catalog](https://github.com/ACNet-AI/MetaSpec/tree/main/src/metaspec/templates/library) for full list.**

---

**Adaptation Process**

**When using library commands**:

1. **Variable Mapping**
   - Map library variables to your domain terms
   - Example: `{{ entity_type }}` → "API Endpoint"
   - Example: `{{ deliverable }}` → "OpenAPI Schema"
   - See library's README.md on GitHub for all variables

2. **Terminology Adjustment**
   - Replace generic terms with domain-specific ones
   - Maintain command structure and workflow logic
   - Preserve spec-driven execution principles

3. **Add Specification Context** (if composing)
   - Enhance library commands with specification knowledge
   - Embed entity definitions and validation rules
   - Result: Library structure + Specification specifics

**See selected library's README.md on [MetaSpec GitHub](https://github.com/ACNet-AI/MetaSpec/tree/main/src/metaspec/templates/library) for detailed adaptation guidelines.**

---

**Composition Examples**

**Composition Pattern 1: Library + Specification**

```
Base: Select library (e.g., generic/)
  → Provides workflow commands
  
Extension: Derive from specification
  → Add entity-specific commands (get-template)
  → Add specification commands (get-spec, validate)

Result: Combined command set
```

**Composition Pattern 2: Specification Only**

```
Derive all commands from specification
  → No library dependency
  → Fully custom to domain
  
Result: Tailored command set
```

**Composition Pattern 3: Library Only**

```
Use library as-is
  → Quick start
  → Adapt variables only
  
Result: Proven workflow pattern
```

---

**Integration with Generator**

**In toolkit specification**, document:

```markdown
### Slash Commands Strategy

**Source**: [Specification | Library | Composed]

**If Library**: 
- Selected: {library-name} (from MetaSpec library)
- Reference: https://github.com/ACNet-AI/MetaSpec/tree/main/src/metaspec/templates/library/{library-name}
- Rationale: {Why this library}

**If Specification-Derived**:
- Based on: specs/domain/{number}-{name}
- Commands needed: {List and rationale}

**If Composed**:
- Base: {library-name} (from MetaSpec)
- Extensions: {Specification-derived commands}
- Composition rationale: {Why compose}
```

**Generator expectations**:
- Copy selected library from MetaSpec to `templates/{source}/commands/`
- Apply variable mappings (cli_name, entity_type, etc.)
- Add specification-derived commands if specified
- Source isolation prevents naming conflicts

---

**Quality Checklist (Library-Selected)**

- [ ] Selected appropriate library for domain
- [ ] Mapped all library variables to domain terms
- [ ] Adapted terminology to match domain
- [ ] Added specification knowledge where applicable
- [ ] No naming conflicts between library and specification commands
- [ ] All commands properly prefixed (/{toolkit}.*)

---

**Integration with Generated Speckit**

These Slash Commands (from library and/or specification) will:
1. Be generated into `templates/{source}/commands/` directory (organized by source)
2. Embed specification knowledge where applicable
3. Provide reusable workflow patterns from library
4. Enable spec-driven development by AI agents
5. Support composition of multiple specification systems

**This demonstrates MetaSpec's Composability**: Specification systems can be selected, adapted, and composed.

**Summary**: Source 2 enables rapid adoption by selecting pre-built specification systems from MetaSpec's library, adapting variables to your domain, and composing with custom commands.

\```

##### **Component 5: Generator (Optional)**

If applicable:

```markdown
### Generator Component

**Purpose**: Generate code/artifacts from validated specs

**Generation Targets**:
- {Target 1}: {Description}
- {Target 2}: {Description}

**Templates**:
- Location: `templates/`
- Format: Jinja2
- Customization: User-overridable

**API**:
```python
from {toolkit_name}.generator import generate

# Generate from spec
generate(spec, output_dir="./output", template="default")
```
\```

#### **Architecture Design**

```markdown
## Architecture

### Module Structure
```
{toolkit_name}/
├── __init__.py
├── parser.py          # Parser component
├── validator.py       # Validator component
├── generator.py       # Generator component (optional)
├── cli.py             # CLI entry point
├── models.py          # Data models
├── exceptions.py      # Custom exceptions
└── templates/         # Templates (if generator exists)
```

### Data Flow
```
Input File
    ↓
  Parser  ───→ Parsed Spec Object
    ↓
Validator ───→ Validation Result
    ↓
Generator ───→ Output Artifacts
```

### Key Classes
- `{Toolkit}Spec`: Main specification object
- `{Toolkit}Parser`: Parser implementation
- `{Toolkit}Validator`: Validator implementation
- `{Toolkit}Generator`: Generator implementation (optional)
\```

#### **Dependencies and Requirements**

```markdown
## Technical Requirements

### Language
- Python 3.9+

### Core Dependencies
- `pydantic`: Data validation and settings management
- `typer`: CLI framework
- `pyyaml` or `ruamel.yaml`: YAML parsing
- `jinja2`: Template engine (if generator)
- `rich`: Terminal formatting

### Development Dependencies
- `pytest`: Testing framework
- `mypy`: Type checking
- `ruff`: Linting and formatting
- `coverage`: Code coverage

### Optional Dependencies
- {Additional deps based on specific needs}
```

#### **Validation Strategy**

```markdown
## Validation Strategy

### Unit Tests
- Test each component independently
- Mock external dependencies
- Aim for 80%+ coverage

### Integration Tests
- Test component interactions
- Test CLI commands end-to-end
- Test with real specification files

### Validation Cases
1. **Parser Tests**:
   - Valid YAML/JSON parsing
   - Invalid syntax handling
   - Edge cases (empty files, large files)

2. **Validator Tests**:
   - Each validation rule from specification spec
   - Error message quality
   - Multiple errors handling

3. **CLI Tests**:
   - Each command with various options
   - Error handling
   - Help messages

4. **Generator Tests** (if applicable):
   - Template rendering
   - Output file creation
   - Custom template handling

### Validation Data
- Sample valid specifications
- Sample invalid specifications
- Edge cases

**Validation Location**: `tests/` directory
```

#### **Success Criteria**

```markdown
## Success Criteria

### MVP Features
- ✅ {Feature 1}
- ✅ {Feature 2}
- ✅ {Feature 3}

### Quality Metrics
- All tests pass
- 80%+ code coverage
- No critical linting errors
- Type hints complete (mypy passes)

### Documentation
- README with quickstart
- API documentation
- CLI help messages complete
- Example specifications

### User Experience
- Clear error messages
- Fast execution (< 1s for typical specs)
- Good CLI UX (progress bars, colors)
```

### 4. Write Specification File

**Location**: `specs/toolkit/{number}-{name}/spec.md`

**Structure**:
```markdown
# {Toolkit Name}

**Version**: {version}
**Status**: Draft | In Development | Stable
**Created**: {date}

## Dependencies

{Dependencies from Section 3: Generate Toolkit Specification Content}

## Overview

{Overview from Section 3: Generate Toolkit Specification Content}

## Components

{Component specifications from Section 3: Generate Toolkit Specification Content}

## Architecture

{Architecture design from Section 3: Generate Toolkit Specification Content}

## Technical Requirements

{Requirements from Section 3: Generate Toolkit Specification Content}

## Validation Strategy

{Validation strategy from Section 3: Generate Toolkit Specification Content}

## Success Criteria

{Success criteria from Section 3: Generate Toolkit Specification Content}

## Implementation Plan

See `plan.md` (created via `/metaspec.sdd.plan`)

## Tasks

See `tasks.md` (created via `/metaspec.sdd.tasks`)
```

### 5. Generate Detailed Impact Report (NEW)

**Purpose**: Create comprehensive change tracking and impact analysis for toolkit specifications.

**Step 5a: Prepare Report Content**

Collect information for the report:

```markdown
Report Data:
- Toolkit ID: {spec_id}
- Version: {version} (1.0.0 for new, increment for updates)
- Date: {today}
- Type: New | Update
- Language: {Primary language}
- Components: {List of components}
- Dependencies: {List of domain specs}
```

**Step 5b: Generate HTML Comment**

Create compact report and **prepend** to spec.md:

```html
<!--
Toolkit Specification Report
============================
Toolkit: {spec_id} v{version} | {New | Update}
Date: {ISO_DATE}

Summary:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Language: {Python | TypeScript | Go | Rust}
Components: {count} ({Parser, Validator, CLI, etc.})
Domain Dependencies: {count}
Status: {Draft | In Development | Stable}

Impact:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Created: specs/toolkit/{spec_id}/spec.md
Review: README.md, AGENTS.md{IF dependencies}, domain specs{END}

Constitution: {✅ Compliant | ⚠️ Check: {issues}}

Next: Plan architecture, Break down tasks, Verify dependencies

Generated by: /metaspec.sdd.specify
-->
```

**Step 5c: Write Order**

When writing spec.md:
1. **First**: Prepend HTML comment (Impact Report)
2. **Then**: Write toolkit specification content

### 6. Consistency Propagation and Impact Analysis (NEW)

**Purpose**: Identify affected files and verify dependencies.

After writing spec.md, systematically check related files:

#### A. Domain Specification Dependencies (CRITICAL)

**Verify all dependencies exist**:

```bash
# Extract dependencies from spec.md
grep -A 10 "^## Dependencies" specs/toolkit/{spec_id}/spec.md

# For each domain spec dependency:
# 1. Verify it exists
# 2. Check if entities are correctly referenced
# 3. Verify validation rules are consistent
```

**Actions**:
- **Read**: Each dependent domain spec
- **Verify**: Entity names and structures match
- **Check**: Validation rules are aligned
- **Note**: Any mismatches or missing references
- **Mark**: Dependencies needing updates

**Example Check**:
```markdown
Checking dependency: domain/001-mcp-core-spec...
- Status: ✅ Exists
- Entities referenced by toolkit: Server, Tool, Resource
- Verification: ✅ All entities exist in domain spec
- Validation rules: ✅ Toolkit enforces domain rules

Checking dependency: domain/002-auth-spec...
- Status: ❌ NOT FOUND
- ⚠️  CRITICAL: Toolkit declares dependency but spec doesn't exist
- → Action: Create domain/002-auth-spec first, or remove dependency
```

#### B. Other Toolkit Specifications

**Check for overlaps or conflicts**:

```bash
# List all other toolkit specifications
ls specs/toolkit/ | grep -E '^[0-9]{3}-' | grep -v {current_spec_id}

# For each existing toolkit:
# 1. Component overlap (do toolkits do similar things?)
# 2. Naming conflicts
# 3. Dependency relationships
```

**Actions**:
- **Read**: Each toolkit's purpose and components
- **Compare**: Against new toolkit's functionality
- **Note**: Any functional overlaps
- **Mark**: Potential consolidation opportunities

**Example Check**:
```markdown
Checking specs/toolkit/001-mcp-parser/spec.md...
- Purpose: Parse MCP server definitions
- Components: Parser, Validator
- ⚠️  OVERLAP: New toolkit also has Parser component
- → Review: Consider reusing vs separate implementation

Checking specs/toolkit/002-mcp-generator/spec.md...
- Purpose: Generate MCP client code
- Components: Generator, Templates
- ✅ No overlap with new toolkit
```

#### C. MetaSpec Commands (Slash Commands)

**Check if toolkit commands need generation**:

```bash
# If toolkit defined slash commands in Component 4
# Check if command files should be generated

# For each slash command specified:
# - Should .metaspec/commands/ be created?
# - Are there library commands to copy?
# - Are custom commands needed?
```

**Actions**:
- **Read**: Component 4 (Slash Commands) from spec.md
- **Check**: Command derivation strategy (specification vs library)
- **Note**: Commands to be generated
- **Mark**: For generation in /metaspec.sdd.implement

**Example**:
```markdown
Slash Commands Strategy: Composed (Library + Specification-derived)
- Base Library: library/sdd/spec-kit
- Custom Commands: get-spec, validate, show-template
- → Action: Copy library commands + generate custom commands
```

#### D. Source Code Structure (If Exists)

**Check existing source code**:

```bash
# If src/{toolkit_name}/ already exists
ls src/{toolkit_name}/

# For each component in specification:
# - Does corresponding source file exist?
# - Does it need updates?
# - Are new files needed?
```

**Actions**:
- **Read**: Existing source files
- **Compare**: Against specified components
- **Note**: Missing implementations
- **Mark**: Files needing updates or creation

**Example Check**:
```markdown
Checking src/mcp-parser/...
- parser.py: ✅ Exists (may need updates)
- validator.py: ✅ Exists (may need updates)
- models.py: ❌ NOT FOUND (needs creation)
- cli.py: ✅ Exists (may need updates)
- generator.py: ❌ NOT PLANNED (new component, needs creation)

→ Impact: 2 new files, 3 files needing review
```

#### E. Project Documentation

**Check documentation files**:

```bash
# Files to review
- README.md: Toolkit list and usage
- AGENTS.md: Toolkit documentation for AI
- CHANGELOG.md: Record toolkit addition
- docs/*.md: Any toolkit guides
```

**Actions**:
- **Read**: Current documentation
- **Check**: If toolkit is documented
- **Note**: Missing documentation sections
- **Update**: Add to Impact Report

**Example**:
```markdown
Checking README.md...
- ⚠️  New toolkit not listed
- → Action: Add to "Toolkits" section with purpose

Checking AGENTS.md...
- ⚠️  Toolkit commands not documented
- → Action: Add toolkit slash commands section
```

#### F. Test Files (If Tests Directory Exists)

**Check test coverage**:

```bash
# If tests/ directory exists
ls tests/

# For each component in specification:
# - Do corresponding tests exist?
# - What tests need to be created?
# - Are existing tests still valid?
```

**Actions**:
- **Read**: Existing test files
- **Check**: Coverage for specified components
- **Note**: Missing test files
- **Mark**: Tests to create or update

**Example**:
```markdown
Checking tests/unit/...
- test_parser.py: ✅ Exists
- test_validator.py: ✅ Exists
- test_models.py: ❌ NOT FOUND (needs creation)
- test_cli.py: ✅ Exists

Checking tests/integration/...
- test_end_to_end.py: ⚠️  May need updates for new generator component

→ Test Impact: 1 new test file, 1 file needing review
```

### 7. Validation Checklist (NEW)

**Purpose**: Ensure toolkit specification quality before finalizing.

Run these critical validation checks:

- [ ] **Structure**: Required sections present (Dependencies, Overview, Implementation, Components, Success Criteria)
- [ ] **Dependencies**: At least one domain spec referenced, all dependencies exist
- [ ] **Implementation**: Language specified with rationale, architecture type defined
- [ ] **Components**: Core components listed (Parser/Validator/CLI/etc.) with clear purposes
- [ ] **Constitution Compliance**: Entity-First Design, Spec-First Development, AI-Agent Friendly, Progressive Enhancement
- [ ] **Validation Strategy**: Test plan defined (unit/integration tests)
- [ ] **Impact Report**: Prepended at top of spec.md
- [ ] **File Path**: specs/toolkit/{spec_id}/spec.md

### 8. Generate Validation Report

**Output validation results**:

```markdown
Validation Report
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Structure Validation: ✅ PASSED (3/3 checks)
- Header section: ✅
- Required sections: ✅ (All present)
- File organization: ✅

Content Validation: ✅ PASSED (6/6 checks)
- Dependencies: ✅ (Depends on domain/001-mcp-spec)
- Implementation details: ✅ (Python 3.10+, Modular)
- Component specifications: ✅ (4 components defined)
- Architecture design: ✅ (Clear module structure)
- Validation strategy: ✅ (Unit + Integration tests)
- Success criteria: ✅ (MVP features listed)

Constitution Compliance: ✅ PASSED (6/6 principles)
- Entity-First Design: ✅
- Validator Extensibility: ✅
- Spec-First Development: ✅
- AI-Agent Friendly: ✅
- Progressive Enhancement: ✅
- Automated Quality: ✅

Dependency Validation: ✅ PASSED (4/4 checks)
- All dependencies exist: ✅ (domain/001-mcp-spec verified)
- No circular dependencies: ✅
- Consistent references: ✅ (Entity names match)
- Version compatibility: ✅

Implementation Validation: ✅ PASSED (5/5 checks)
- Language choice: ✅ (Python justified for ecosystem)
- Dependencies: ✅ (Pydantic, Typer available)
- Architecture: ✅ (Modular is feasible)
- Components: ✅ (All implementable)
- Performance targets: ✅ (< 100ms is realistic)

Overall Score: 24/24 (100%) ✅

{IF any warnings}:
⚠️  Warnings:
- {Warning 1}
- {Warning 2}

{IF any suggestions}:
💡 Suggestions:
- {Suggestion 1}: {Rationale}
- {Suggestion 2}: {Rationale}
```

### 9. Success Output (Enhanced)

**Provide comprehensive summary with validation and impact results**:

```
✅ Toolkit specification created/updated successfully

📁 Location:
   specs/toolkit/{number}-{name}/spec.md

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

📋 Toolkit Summary:
   Name: {Toolkit Name}
   Version: {version}
   Status: {Draft | In Development | Stable}
   Primary Language: {Python | TypeScript | Go | Rust}
   Architecture: {Monolithic | Modular | Plugin-based}

📦 Dependencies:
   Domain Specifications:
   - domain/{dependency-1}: {What it provides}
   - domain/{dependency-2}: {What it provides}
   ...

   Key Libraries:
   - {library-1}: {Purpose}
   - {library-2}: {Purpose}
   ...

🔧 Components ({count}):
   - {Component 1}: {brief description}
   - {Component 2}: {brief description}
   ...

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

✅ Validation Results: PASSED ({score}/24 checks)

   Structure: ✅ {3/3 checks passed}
   Content: ✅ {6/6 checks passed}
   Constitution: ✅ {6/6 principles compliant}
   Dependencies: ✅ {4/4 checks passed}
   Implementation: ✅ {5/5 checks passed}

{IF any warnings}:
   ⚠️  Warnings:
   - {Warning 1}
   - {Warning 2}

{IF any suggestions}:
   💡 Suggestions:
   - {Suggestion 1}
   - {Suggestion 2}

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

📋 Impact Analysis:

   ✅ Files Created/Updated:
   - specs/toolkit/{spec_id}/spec.md

   ⚠️  Files Requiring Manual Review:
   - README.md (add toolkit to list)
   - AGENTS.md (document toolkit commands)
   {IF domain specs dependencies}:
   - Domain specs verified: {list of checked specs}
   {IF source code exists}:
   - Source files needing review: {count} files
   {IF tests exist}:
   - Test files needing update: {count} files

   📊 Consistency Check:
   - Domain specifications verified: {count}
   - Toolkit specifications reviewed: {count}
   - Source files analyzed: {count}
   - Test files checked: {count}
   - Documentation needing updates: {count} files

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

🔄 Next Steps:

   Immediate:
   1. Review toolkit specification completeness
   2. Verify domain specification dependencies
   3. Update README.md with toolkit information
   4. Update AGENTS.md with commands documentation
   {IF conflicts}:
   5. ⚠️  Resolve component overlaps with other toolkits
   {IF source impact}:
   6. ⚠️  Review and update {count} source files

   Recommended:
   - Run /metaspec.sdd.plan to create architecture plan
   - Run /metaspec.sdd.tasks to break down implementation
   - Run /metaspec.sdd.implement to start building
   {IF slash commands needed}:
   - Generate slash commands during implementation

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

💡 Suggested commit message:
   {IF new}:
   feat(toolkit): add {spec_id} toolkit specification
   
   - Primary language: {language}
   - Components: {count} ({component list})
   - Depends on: {domain spec list}
   {IF slash commands}:
   - Slash commands: {count} planned
   
   {IF update}:
   feat(toolkit): update {spec_id} toolkit specification
   
   - {summary of changes}
```

## Best Practices

### Toolkit Specification Focus

✅ **DO**:
- Define HOW to implement the toolkit
- Specify Parser, Validator, CLI, Generator
- Reference specification specs explicitly
- Include architecture and validation strategy
- Focus on user experience

❌ **DON'T**:
- Redefine the specification (belongs in specification specs)
- Skip dependency declarations
- Mix specification and toolkit concerns
- Over-specify implementation details

### Dependency Management

- **Always** declare specification dependencies at the top
- Reference specific specification/XXX- specs
- Document which specification features are supported
- Note version compatibility if relevant

### Component Design

- Keep components modular and testable
- Clear interfaces between components
- Minimal coupling
- Support both CLI and programmatic usage

### Progressive Enhancement

Start with MVP:
1. Parser (basic)
2. Validator (core rules)
3. CLI (init + validate)

Add later:
4. Generator
5. Advanced CLI features
6. SDK/Library enhancements

## Constitution Check

Before finalizing, verify against `memory/constitution.md`:

```bash
# Check toolkit spec against constitution
grep -A 5 "Minimal Viable Abstraction" memory/constitution.md
grep -A 5 "AI-First Design" memory/constitution.md
```

**Ensure**:
- Start with minimal viable toolkit
- Components are clearly defined
- Architecture supports extension
- Testing is built-in from start

## Troubleshooting

**If no specification specs exist**:
→ Prompt user to create specification spec first with `/metaspec.sds.specify`

**If toolkit seems too complex**:
→ Break into multiple toolkit specs (e.g., parser-only, validator-only)

**If unclear architecture**:
→ Use `/metaspec.sdd.clarify` to resolve design questions

**If components overlap**:
→ Review separation of concerns, consider merging or splitting

**If validation strategy unclear**:
→ Focus on contract testing at component boundaries
