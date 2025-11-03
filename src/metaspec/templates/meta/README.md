# Meta Templates - MetaSpec Development Commands

## Overview

This directory contains **MetaSpec development command templates** that will be generated into each speckit's `.metaspec/commands/` directory to assist AI in developing the speckit itself.

This is MetaSpec's meta-level: using specification-driven methods to develop specification-driven toolkits.

## Design Philosophy

```
MetaSpec (meta-specification framework)
    ↓ Uses its own methodology
Meta Commands (this directory)
    ↓ Generated into speckit
AI Agent uses these commands to develop speckit
    ↓ Final output
Speckit (specification-driven toolkit)
```

**Key Concepts**:
- MetaSpec uses Spec-Driven Development (SDD) to develop itself
- Generated speckits also contain these commands for continued specification-driven development
- Recursive specification-driven architecture

## Three-Layer Architecture

meta/ adopts a clear three-layer architecture, separating commands at different conceptual levels:

```
meta/
├── sds/              # Spec-Driven Specification (4 commands)
│   ├── commands/     # Protocol specification definition commands
│   └── templates/    # (Current commands reference protocol templates under shared templates/)
│
├── sdd/              # Spec-Driven Development (8 commands)
│   ├── commands/     # Toolkit development commands
│   └── templates/    # (currently empty, uses shared templates/)
│
├── evolution/        # Specification Evolution (3 commands)
│   ├── commands/     # Specification evolution commands (shared by SDS + SDD)
│   └── templates/    # (currently empty, uses shared templates/)
│
└── templates/        # Shared output templates (6 templates)
    ├── constitution-template.md.j2
    ├── spec-template.md.j2           # Toolkit specification
    ├── plan-template.md.j2           # Toolkit planning
    ├── tasks-template.md.j2          # Toolkit task breakdown
    ├── checklist-template.md.j2      # Toolkit quality check
    └── protocol-spec-template.md.j2  # Protocol specification (SDS output: YAML frontmatter + Markdown)
```

### Why Three Layers?

1. **SDS (Spec-Driven Specification)** - Define protocol specifications
   - Goal: Define WHAT (what the protocol is)
   - Output: `specs/protocol/` directory
   - Examples: Define MCP protocol, OpenAPI specification
   - **Status**: Primary, core asset

2. **SDD (Spec-Driven Development)** - Develop toolkits
   - Goal: Define HOW (how to implement the toolkit)
   - Output: `specs/toolkit/` directory
   - Examples: Develop Parser, Validator, CLI
   - **Status**: Derived, depends on SDS

3. **Evolution** - Specification evolution (shared)
   - Goal: Controlled evolution of SDS or SDD specifications
   - Output: `changes/` directory (at same level as specs/)
   - Characteristics: SDS and SDD share the same evolution mechanism

### ⚠️ Key Principle: Protocol First, Toolkit Second

**MetaSpec's core value lies in specification management**:

- Protocol (specification) is the **core asset**, exists independently, can be published separately
- Toolkit is a **supporting tool**, must depend on Protocol
- Toolkit without Protocol = ordinary code generator

**Mandatory Requirements**:
- SDD commands check if Protocol exists
- If not exists, **block** and require running SDS commands first
- Toolkit spec.md must have Dependencies section
- analyze marks missing dependencies as CRITICAL

### 🎯 How Toolkit Value is Realized

**Core Understanding**: Toolkit value ≠ Fixed code templates  
**Toolkit value = Specification-driven code generation**

MetaSpec realizes toolkit value through a three-stage process:

**1. Define Protocol (SDS)** → Define WHAT  
**2. Define Toolkit (SDD)** → Define HOW  
**3. Generate Code (SDD)** → Generate implementation

**Why not use fixed templates?**

❌ Fixed template problems:
- Assumes specific language (forces Python)
- Assumes fixed architecture (6 fixed files)
- Violates Spec-Driven principle

✅ Specification-driven advantages:
- **Language-agnostic**: Supports Python/TypeScript/Go/Rust
- **Architecture-flexible**: Dynamic design based on requirements
- **Component-optional**: Generate only needed parts
- **Truly Spec-Driven**: Code generated from specifications

**Actual Usage**:
```bash
/metaspec.sds.specify "MCP protocol"   # Protocol
/metaspec.sdd.specify "TS toolkit"     # Toolkit (select language, components)
/metaspec.sdd.plan                      # Design architecture
/metaspec.sdd.implement                 # Generate code
→ src/*.ts (usable toolkit!)
```

See: `/metaspec.sdd.specify`, `/metaspec.sdd.plan`, `/metaspec.sdd.implement`

## Command List

### SDS Commands (4) - Protocol Specification

Generated command prefix: `/metaspec.sds.*`

| Command | Purpose | Output |
|------|------|------|
| `constitution` | Define protocol design principles | memory/constitution.md |
| `specify` | Define protocol entities and rules | specs/protocol/00X-name/spec.md |
| `clarify` | Resolve protocol ambiguities | Update spec.md |
| `analyze` | Check protocol consistency | Analysis report |

**Use Cases**:
- Define domain protocols (e.g., MCP, GraphQL)
- Define validation rules and constraints
- Implementation-independent specifications

### SDD Commands (8) - Toolkit Development

Generated command prefix: `/metaspec.sdd.*`

| Command | Purpose | Output |
|------|------|------|
| `constitution` | Define toolkit development principles | memory/constitution.md |
| `specify` | Define toolkit specifications | specs/toolkit/00X-name/spec.md |
| `clarify` | Resolve toolkit requirements | Update spec.md |
| `plan` | Plan architecture design | specs/toolkit/00X-name/plan.md |
| `tasks` | Break down implementation tasks | specs/toolkit/00X-name/tasks.md |
| `implement` | Execute implementation | Code in src/ |
| `checklist` | Quality check | Checklist |
| `analyze` | Verify consistency | Analysis report |

**Use Cases**:
- Develop Parser, Validator
- Implement CLI tools
- Build SDKs and libraries

### Evolution Commands (3) - Shared Evolution

Generated command prefix: `/metaspec.*` (no sds/sdd prefix)

| Command | Purpose | Output | Parameters |
|------|------|------|------|
| `proposal` | Create change proposal | changes/xxx/ | `--type sds\|sdd` |
| `apply` | Apply changes | Implement changes | `--type sds\|sdd` |
| `archive` | Archive completed changes | changes/archive/ | `--type sds\|sdd` |

**Use Cases**:
- Protocol specification evolution after stabilization (`--type sds`)
- Toolkit evolution after stabilization (`--type sdd`)
- Team collaboration and change control

## Generated Directory Structure

When generating a speckit, these commands will be generated to:

```
generated-speckit/
├── .metaspec/
│   └── commands/
│       ├── metaspec.sds.constitution.md   ← SDS commands
│       ├── metaspec.sds.specify.md
│       ├── metaspec.sds.clarify.md
│       ├── metaspec.sds.analyze.md
│       │
│       ├── metaspec.sdd.constitution.md   ← SDD commands
│       ├── metaspec.sdd.specify.md
│       ├── metaspec.sdd.clarify.md
│       ├── metaspec.sdd.plan.md
│       ├── metaspec.sdd.tasks.md
│       ├── metaspec.sdd.implement.md
│       ├── metaspec.sdd.checklist.md
│       ├── metaspec.sdd.analyze.md
│       │
│       ├── metaspec.proposal.md           ← Evolution commands
│       ├── metaspec.apply.md
│       └── metaspec.archive.md
│
├── specs/
│   ├── protocol/    ← SDS output (protocol specifications)
│   └── toolkit/     ← SDD output (toolkit specifications)
│
└── changes/         ← Evolution output (change management, at same level as specs/)
```

### Detailed specs/ Directory Structure

#### protocol/ - Protocol Specifications (SDS Output)

```
specs/protocol/
├── 001-mcp-core-protocol/
│   ├── spec.md              # Protocol entity definitions
│   │                        # - Server interface
│   │                        # - Tool interface
│   │                        # - Resource interface
│   │                        # - Data type definitions
│   │                        # - Validation rules
│   └── README.md            # Protocol overview
│
├── 002-graphql-schema/
│   ├── spec.md              # GraphQL protocol definition
│   └── schema.graphql       # Schema file (optional)
│
└── 003-validation-rules/
    └── spec.md              # Protocol validation rules
```

**Characteristics**:
- Numbered directories: 001-, 002-, 003-
- Pure protocol definitions, no implementation details
- Define WHAT (what the protocol is)

#### toolkit/ - Toolkit Specifications (SDD Output)

```
specs/toolkit/
├── 001-mcp-parser/
│   ├── spec.md              # Parser functionality specification
│   │                        # - Dependency: protocol/001-mcp-core-protocol
│   │                        # - Input format
│   │                        # - Output format
│   │                        # - Error handling
│   ├── plan.md              # Implementation plan
│   │                        # - Tech stack selection
│   │                        # - Architecture design
│   │                        # - Module division
│   ├── tasks.md             # Task breakdown
│   │                        # - [ ] Implement Token parser
│   │                        # - [ ] Implement AST builder
│   │                        # - [ ] Implement error recovery
│   └── checklist.md         # Quality checklist
│
├── 002-mcp-validator/
│   ├── spec.md              # Validator functionality specification
│   │                        # - Dependency: protocol/001-mcp-core-protocol
│   │                        # - Dependency: toolkit/001-mcp-parser
│   ├── plan.md
│   ├── tasks.md
│   └── checklist.md
│
└── 003-cli-tool/
    ├── spec.md              # CLI tool specification
    ├── plan.md
    ├── tasks.md
    └── checklist.md
```

**Characteristics**:
- Numbered directories: 001-, 002-, 003-
- Contains implementation plans and tasks
- Explicitly declares dependencies on protocol/
- Define HOW (how to implement the toolkit)

#### changes/ - Change Management (Evolution Output)

```
changes/
├── add-websocket-support/         # Change proposal (for protocol)
│   ├── proposal.md                # Change proposal
│   │                              # - Type: protocol (SDS)
│   │                              # - Target: protocol/001-mcp-core-protocol
│   │                              # - Change reason
│   │                              # - Impact analysis
│   ├── tasks.md                   # Implementation tasks
│   ├── impact.md                  # Impact assessment
│   └── specs/
│       └── protocol/
│           └── mcp-core/
│               └── spec.md        # Spec Delta
│                                  # - ## ADDED
│                                  # - ## MODIFIED
│                                  # - ## REMOVED
│
├── improve-parser-performance/    # Change proposal (for toolkit)
│   ├── proposal.md                # Change proposal
│   │                              # - Type: toolkit (SDD)
│   │                              # - Target: toolkit/001-mcp-parser
│   ├── tasks.md
│   ├── impact.md
│   └── specs/
│       └── toolkit/
│           └── parser/
│               └── spec.md        # Spec Delta
│
└── archive/                       # Completed changes
    ├── add-websocket-support/     # Archived structure
    │   ├── proposal.md
    │   ├── completion-date.txt    # Completion date
    │   └── applied-version.txt    # Applied version
    │
    └── improve-parser-performance/
        ├── proposal.md
        ├── completion-date.txt
        └── applied-version.txt
```

**Characteristics**:
- Directories named by change ID (not numbered)
- Contains proposal, tasks, impact
- specs/ subdirectory contains delta (incremental changes)
- archive/ stores completed change history
- Can target protocol or toolkit

### Relationship Between Three Directories

```
Project root
├── specs/
│   ├── protocol/           (Protocol definition - WHAT)
│   │                       - Pure specification, independently publishable
│   │                       - Define entities, interfaces, validation rules
│   │
│   └── toolkit/            (Tool implementation - HOW)
│       │                   - Implementation specification, references protocol/
│       │                   - Parser, Validator, CLI
│       │
│       └─ depends ────────> protocol/
│
└── changes/                (Evolution control - change history)
    │                       - Can change protocol/
    │                       - Can change toolkit/
    │                       - Version tracking, approval process
    │
    ├─ change ─────────────> specs/protocol/
    └─ change ─────────────> specs/toolkit/
```

**Key Principles**:
1. **specs/protocol/** - Independent protocol specifications, can be published and referenced separately
2. **specs/toolkit/** - Explicitly depends on protocol/, implements specific tools
3. **changes/** - Manages evolution of both, maintains change history (at project root)

**Why is changes/ at the same level as specs/?**
- changes/ is a **temporary workspace** for drafts and approvals
- specs/ is **stable specifications**, the final source of truth
- Separation of concerns: specification storage vs change management

**Example Dependency Relationships**:
```yaml
# specs/toolkit/001-parser/spec.md
dependencies:
  - protocol/001-mcp-core-protocol  # Reference protocol

# changes/add-websocket/proposal.md
type: protocol                      # Change type
target: protocol/001-mcp-core       # Change target (relative to specs/)
```

## Typical Workflow

### Recommended Practice: SDS + SDD Separation

#### Phase 1: Protocol Specification (SDS)

```bash
# Define protocol principles
/metaspec.sds.constitution

# Create protocol specification
/metaspec.sds.specify "MCP Server Protocol"
# Output: specs/protocol/001-mcp-server-protocol/spec.md

# Clarify details
/metaspec.sds.clarify

# Check consistency
/metaspec.sds.analyze
```

**Output**: `specs/protocol/001-xxx/spec.md` - Pure protocol definition

#### Phase 2: Toolkit Specification (SDD)

```bash
# Define toolkit principles
/metaspec.sdd.constitution

# Create toolkit specification (explicitly depends on protocol/001-xxx)
/metaspec.sdd.specify "MCP Parser"
# Output: specs/toolkit/001-mcp-parser/spec.md

# Plan implementation
/metaspec.sdd.plan

# Break down tasks
/metaspec.sdd.tasks

# Execute implementation
/metaspec.sdd.implement

# Quality check
/metaspec.sdd.checklist

# Verify consistency
/metaspec.sdd.analyze
```

**Output**: `specs/toolkit/001-xxx/` - Toolkit implementation specification

#### Phase 3: Evolution (After Specifications Stabilize)

```bash
# Propose protocol changes
/metaspec.proposal "Add WebSocket support" --type sds

# Or propose toolkit changes
/metaspec.proposal "Improve parser performance" --type sdd

# Apply changes
/metaspec.apply add-websocket

# Archive completion
/metaspec.archive add-websocket
```

**Output**: `specs/changes/xxx/` - Change history

## Relationship with library/

```
templates/
├── meta/              # MetaSpec self-development (this directory)
│   ├── sds/           # Protocol specification definition
│   ├── sdd/           # Toolkit development
│   └── evolution/     # Specification evolution
│
└── library/           # User speckit development
    ├── generic/       # Universal specification-driven templates
    │   ├── greenfield/   # New specification creation
    │   └── brownfield/   # Specification evolution
    │
    └── sdd/           # Development specialization
        ├── spec-kit/     # Greenfield original source
        └── openspec/     # Brownfield original source
```

**Differences**:
- **meta/** - For developing speckit itself (meta layer)
- **library/** - For speckit users (application layer)

## Naming Conventions

### Command Prefixes

- SDS: `/metaspec.sds.*` - Clearly indicates protocol definition
- SDD: `/metaspec.sdd.*` - Clearly indicates toolkit development
- Evolution: `/metaspec.*` - Shared commands, distinguished by `--type` parameter

### Why Doesn't Evolution Need a Prefix?

Because Evolution is a **shared** mechanism for SDS and SDD:
- Doesn't belong to a specific layer
- Target specified via `--type sds|sdd` parameter
- Keeps commands concise

## Maintenance Notes

- **Source**: These commands are MetaSpec core, not synced from external sources
- **Updates**: Modifying these commands affects all generated speckits
- **Testing**: After modification, generate test speckit for verification
- **Documentation Sync**: Update AGENTS.md when updating commands

## Example: Using MetaSpec to Develop MCP Speckit

```bash
# Phase 1: Define MCP protocol (SDS)
/metaspec.sds.constitution  # Define protocol principles
/metaspec.sds.specify "MCP Protocol Core"
# → specs/protocol/001-mcp-protocol-core/spec.md

# Phase 2: Develop MCP Parser (SDD)
/metaspec.sdd.specify "MCP Request Parser"
# → specs/toolkit/001-mcp-request-parser/spec.md
# → Explicit reference: depends on protocol/001-mcp-protocol-core

/metaspec.sdd.plan          # Plan implementation
/metaspec.sdd.tasks         # Break down tasks
/metaspec.sdd.implement     # Execute implementation

# Phase 3: Evolution (after stabilization)
/metaspec.proposal "Add GraphQL support" --type sds
/metaspec.apply add-graphql
/metaspec.archive add-graphql
```

## Design Principles

### 1. Meta Templates Don't Inherit Generic Templates

**This is an intentional design decision, not an oversight.**

**Reasons**:
- **meta/** - For **speckit developers** (meta layer)
  * Used to develop speckit itself
  * Audience: Developers developing speckits generated by MetaSpec
  * Output: specs/protocol/, specs/toolkit/
  
- **library/generic/** - For **speckit users** (application layer)
  * Used to develop projects using speckit
  * Audience: End users using generated speckits
  * Output: User project specs/

**Why Not Inherit**:
1. **Completely Different Audiences** - Meta layer development vs application layer development
2. **Different Focuses** - meta focuses on toolkit development, generic focuses on universal specifications
3. **Stronger Independence** - Avoid unnecessary coupling and inheritance complexity
4. **Higher Clarity** - Dedicated templates are easier to understand than inherited templates

**If significant duplication is found in the future**, consider extracting shared base templates, but prioritize independence.

### 2. Clear Conceptual Separation

SDS and SDD are completely different conceptual levels:
- **SDS**: Define protocol (WHAT)
- **SDD**: Implement tools (HOW)

### 3. Explicit Dependencies

SDD specifications should explicitly declare dependencies on SDS specifications:
```yaml
# specs/toolkit/001-parser/spec.md
dependencies:
  - protocol/001-mcp-core
```

### 4. Shared Evolution Mechanism

Evolution commands apply to both SDS and SDD, avoiding duplication.

### 5. AI-Friendly

Command prefixes help AI understand current context:
- See `metaspec.sds.*` → Know defining protocol
- See `metaspec.sdd.*` → Know developing tools

---

**Status**: ✅ Production Ready

**Total Commands**: 15 (SDS: 4 + SDD: 8 + Evolution: 3)

**Last Updated**: 2025-10-31

**Maintainer**: MetaSpec Core Team

