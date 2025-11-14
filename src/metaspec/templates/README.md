# MetaSpec Templates

> **Internal template organization for MetaSpec**

This directory contains all Jinja2 templates used by MetaSpec to generate spec-driven toolkits (speckits).

---

## 📁 Directory Structure

```
templates/
├── base/           # Speckit project base files
├── library/        # Domain-specific template libraries
│   ├── sdd/        # Spec-Driven Development workflow templates
│   │   ├── spec-kit/   # From spec-kit (0→1 Greenfield)
│   │   └── openspec/   # From OpenSpec (1→n Brownfield)
│   └── generic/    # Universal feature specification templates
└── meta/           # MetaSpec three-layer command architecture
    ├── sds/        # Spec-Driven Specification (specification definition)
    ├── sdd/        # Spec-Driven Development (toolkit development)
    └── evolution/  # Shared specification evolution commands
```

---

## 📦 Template Categories

### `base/` - Speckit Project Files

**Purpose**: Core files for every generated speckit

**Files**:
- `AGENTS.md.j2` - AI agent guide for the speckit
- `README.md.j2` - Speckit documentation
- `CHANGELOG.md.j2` - Version history
- `constitution.md.j2` - Development principles
- `pyproject.toml.j2` - Python project configuration
- `.gitignore.j2` - Git ignore patterns
- `specs/README.md.j2` - Specifications directory guide
- `scripts/bash/create-new-feature.sh.j2` - Feature creation script (generalized for all entity types)
- `scripts/bash/check-prerequisites.sh.j2` - Check required files and return paths
- `scripts/bash/setup-plan.sh.j2` - Initialize plan file from template

**Generated to**: Speckit root directory

**Example**:
```
my-speckit/
├── AGENTS.md
├── README.md
├── pyproject.toml
├── memory/constitution.md
├── specs/README.md
└── scripts/bash/
    ├── create-new-feature.sh
    ├── check-prerequisites.sh
    └── setup-plan.sh
```

---

### `library/` - Domain-Specific Template Libraries

**Purpose**: Reusable template collections for different domains

#### `library/sdd/` - Development Workflow Templates

Development methodologies organized by lifecycle:

##### `library/sdd/spec-kit/` - Greenfield Development (0→1)

**Source**: Synchronized from [spec-kit](https://github.com/github/spec-kit)
**Lifecycle**: Creating new features from scratch

**Commands** (8):
- `constitution.md.j2` - Define design principles
- `specify.md.j2` - Create specifications
- `clarify.md.j2` - Resolve ambiguities
- `plan.md.j2` - Plan implementation
- `tasks.md.j2` - Break down tasks
- `implement.md.j2` - Execute implementation
- `checklist.md.j2` - Quality validation
- `analyze.md.j2` - Consistency checking

**Templates** (5):
- `spec-template.md.j2` - Specification format
- `plan-template.md.j2` - Implementation plan format
- `tasks-template.md.j2` - Task breakdown format
- `checklist-template.md.j2` - Quality checklist format
- `agent-file-template.md.j2` - Agent guide format

**Usage**: Specify `source: "sdd/spec-kit"` or `source: "dev"` in meta-spec slash_commands

##### `library/sdd/openspec/` - Brownfield Evolution (1→n)

**Source**: OpenSpec project (planned)  
**Lifecycle**: Evolving existing specifications collaboratively  
**Status**: ⚠️ Planning stage

**Planned Commands**:
- `propose.md.j2` - Propose specification changes
- `review.md.j2` - Collaborative review
- `merge.md.j2` - Merge approved changes
- `version.md.j2` - Version management

**Usage**: Will use `source: "sdd/openspec"` when available

#### `library/generic/` - Universal Feature Templates

**Purpose**: Domain-agnostic feature specification templates

**Templates** (1):
- `feature-spec-template.md.j2` - Universal feature specification format

**Note**: This library has no commands (commands optional, templates required)

**Usage**: Used by `create-new-feature.sh` script, specify `source: "generic"` if needed

---

### `meta/` - MetaSpec Three-Layer Architecture

**Purpose**: AI-assisted workflow for developing the speckit itself using a three-layer command architecture that separates domain specification from toolkit development.

#### Three Layers

##### `meta/sds/commands/` - Spec-Driven Specification (8 commands)

**Purpose**: Define domain specifications

- `constitution.md.j2` - Define specification design principles
- `specify.md.j2` - Define specification entities, operations, validation rules
- `clarify.md.j2` - Resolve specification ambiguities
- `plan.md.j2` - Plan specification architecture and sub-specifications
- `tasks.md.j2` - Break down specification work
- `implement.md.j2` - Write specification documents
- `checklist.md.j2` - Generate quality checklist for specification
- `analyze.md.j2` - Check specification consistency

**Generated to**: `.metaspec/commands/metaspec.sds.*`
**Works with**: `specs/domain/` directory

##### `meta/sdd/commands/` - Spec-Driven Development (8 commands)

**Purpose**: Develop spec-driven toolkits

- `constitution.md.j2` - Define toolkit development principles
- `specify.md.j2` - Define toolkit specifications
- `clarify.md.j2` - Resolve toolkit ambiguities
- `plan.md.j2` - Plan toolkit implementation
- `tasks.md.j2` - Break down implementation work
- `implement.md.j2` - Execute implementation
- `checklist.md.j2` - Validate quality
- `analyze.md.j2` - Check consistency

**Generated to**: `.metaspec/commands/metaspec.sdd.*`
**Works with**: `specs/toolkit/` directory

##### `meta/evolution/commands/` - Shared Evolution (3 commands)

**Purpose**: Manage specification evolution for both SDS and SDD

- `proposal.md.j2` - Propose changes (with `--type sds|sdd` parameter)
- `apply.md.j2` - Apply approved changes
- `archive.md.j2` - Archive completed changes

**Generated to**: `.metaspec/commands/metaspec.*`
**Works with**: `changes/` directory (independent from specs/)

#### `meta/templates/` - MetaSpec Output Formats (5)

- `constitution-template.md.j2` - Constitution format
- `spec-template.md.j2` - Specification format
- `plan-template.md.j2` - Implementation plan format
- `tasks-template.md.j2` - Task breakdown format
- `checklist-template.md.j2` - Quality checklist format

**Generated to**: Speckit `.metaspec/templates/` (development working files)

---

## 🔄 Template Generation Flow

### Step 1: Generate Speckit

```bash
metaspec init my-speckit
```

**Result**:
```
my-speckit/
├── AGENTS.md                          # from base/
├── README.md                          # from base/
├── pyproject.toml                     # from base/
├── memory/constitution.md             # from base/
├── specs/README.md                    # from base/
├── scripts/bash/create-new-feature.sh # from base/
├── templates/
│   └── feature-spec-template.md       # from library/generic/
└── .metaspec/
    ├── commands/
    │   ├── metaspec.sds.constitution.md    # from meta/sds/commands/
    │   ├── metaspec.sds.specify.md         # from meta/sds/commands/
    │   ├── metaspec.sds.plan.md            # from meta/sds/commands/
    │   ├── metaspec.sdd.constitution.md    # from meta/sdd/commands/
    │   ├── metaspec.sdd.plan.md            # from meta/sdd/commands/
    │   ├── metaspec.evolution.proposal.md  # from meta/evolution/commands/
    │   └── ... (19 commands total: 8 SDS + 8 SDD + 3 Evolution)
    └── templates/
        ├── constitution-template.md   # from meta/templates/
        ├── spec-template.md           # from meta/templates/
        └── ... (5 templates total)
```

### Step 2: Develop Speckit

```bash
cd my-speckit

# Phase 1: Define specification (SDS)
/metaspec.sds.constitution  # Define specification design principles
/metaspec.sds.specify       # Create domain specifications
/metaspec.sds.analyze       # Check specification consistency

# Phase 2: Develop toolkit (SDD)
/metaspec.sdd.constitution  # Define toolkit principles
/metaspec.sdd.specify       # Create toolkit specifications
/metaspec.sdd.plan          # Plan toolkit implementation
/metaspec.sdd.tasks         # Break down implementation
/metaspec.sdd.implement     # Execute implementation

# Evolution: Manage changes
/metaspec.proposal "Add feature" --type sds  # or --type sdd
```

### Step 3: Use Library Templates (Optional)

If meta-spec defines `slash_commands` with specific `source`:

```yaml
# MetaSpecDefinition configuration (created via interactive wizard or template)
slash_commands:
  - name: "plan"
    description: "Generate implementation plan"
    source: "dev"  # Use library/sdd/ templates (defaults to dev/spec-kit)
```

**Generated**:
```
my-speckit/
└── templates/
    ├── commands/
    │   └── plan.md                    # from library/sdd/commands/
    └── plan-template.md               # from library/sdd/templates/
```

---

## ✅ Key Design Principles

### 1. Optional Commands, Required Templates

- **Templates** (required): Must exist, used for output formatting
- **Commands** (optional): Can be missing (e.g., `library/generic/commands/`)
- Missing commands are silently skipped during generation

### 2. Source-Based Selection

Templates are selected dynamically based on `slash_commands[].source`:
- `source: "dev"` → `library/sdd/`
- `source: "generic"` → `library/generic/`
- Default: `"generic"`

### 3. Clear Separation of Concerns

| Template Set | Purpose | Target Audience |
|-------------|---------|-----------------|
| `base/` | Speckit structure | All speckits |
| `library/sdd/` | Development workflows | Speckit users (from spec-kit) |
| `library/generic/` | Universal templates | Speckit users |
| `meta/` | Speckit development | Speckit developers |

### 4. Two-Layer Architecture

**Layer 1**: Speckit Development (using MetaSpec commands)
- Developer uses `/metaspec.*` commands
- Works with `.metaspec/` directory
- Defines specifications in `specs/`

**Layer 2**: Speckit Usage (using library templates)
- User uses packaged templates from `library/`
- Works with `templates/` directory
- Develops projects based on specifications

---

## 📚 References

- [Architecture Documentation](../../../docs/architecture.md)
- [Slash Command Specification](../../../docs/slash-cmd-protocol.md)
- [AGENTS.md](../../../AGENTS.md) - AI Agent usage guide

---

**Last Updated**: 2025-10-31

