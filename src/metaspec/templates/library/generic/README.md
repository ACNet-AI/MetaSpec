# Generic SD-X Templates

## Overview

This directory contains **pure SD-X (Specification-Driven eXperience)** universal templates applicable to any specification-driven scenario.

These templates are abstracted from `sdd/spec-kit` and `sdd/openspec`, removing all development-specific concepts (such as Feature, User Story, Implementation, Code) and replacing them with universal variables.

## Design Philosophy

```
library/
├── generic/          # Pure SD-X abstraction (this directory)
│   ├── greenfield/   # New specification creation (0→1)
│   └── brownfield/   # Specification evolution (1→n)
│
└── sdd/              # Development specialization
    ├── spec-kit/     # Retains development concepts like Feature, User Story
    └── openspec/     # Retains development evolution workflows
```

### Relationship Description

- **generic/ is abstraction**: Abstracted from sdd/, applicable to all SD-X scenarios
- **sdd/ is specialization**: Retains development-specific terminology, more aligned with developer habits
- **Future expansion**: sd-design/, sd-testing/, sd-documentation/, etc. can all specialize by referencing generic/

## Architecture: Greenfield vs Brownfield

### Greenfield (0→1) - New Specification Creation

**Goal**: Quickly create new specifications, suitable for project initialization

**Workflow**:
```
/constitution → Define principles
/specify     → Create specification
/clarify     → Clarify details
/plan        → Plan implementation
/tasks       → Break down tasks
/generate    → Generate deliverables
/validate    → Quality check
/analyze     → Consistency verification
```

**Generated Structure**:
```
specs/
├── 001-user-auth/
│   └── spec.md
├── 002-payment/
│   └── spec.md
└── 003-dashboard/
    └── spec.md
```

### Brownfield (1→n) - Specification Evolution

**Goal**: Controlled evolution of existing specifications, suitable after project stabilization

**Workflow**:
```
/proposal → Create change proposal (AI generates delta)
/apply    → Execute changes (AI implements and manually merges)
/archive  → Archive completion (AI moves to archive/)
```

**Generated Structure**:
```
project/
├── specs/              ← Original specifications created by greenfield
│   ├── 001-user-auth/
│   │   └── spec.md
│   └── 002-payment/
│       └── spec.md
│
└── changes/            ← Changes managed by brownfield (at same level as specs/)
    ├── add-oauth/
    │   ├── proposal.md
    │   ├── tasks.md
    │   └── specs/
    │       └── user-auth/
    │           └── spec.md  ← AI manually merges back to specs/001-user-auth/
    └── archive/        ← Completed changes
```

**Integration Mode**:
- Brownfield adopts **AI Agent manual merge mode** (similar to meta/evolution)
- No need to generate additional CLI tools
- AI Agent responsible for reading delta and merging back to main specification

## Directory Structure

```
generic/
├── README.md           # This file
├── greenfield/         # Greenfield (0→1) workflow
│   ├── commands/ (8 commands)
│   │   ├── constitution.md.j2  # Define governance principles
│   │   ├── specify.md.j2       # Define specification entities
│   │   ├── clarify.md.j2       # Resolve specification ambiguities
│   │   ├── plan.md.j2          # Plan implementation approach
│   │   ├── tasks.md.j2         # Break down tasks
│   │   ├── generate.md.j2      # Generate deliverables (generalized from implement)
│   │   ├── validate.md.j2      # Quality check (generalized from checklist)
│   │   └── analyze.md.j2       # Consistency analysis
│   └── templates/
│       ├── spec-template.md.j2
│       ├── plan-template.md.j2
│       ├── tasks-template.md.j2
│       └── validate-template.md.j2
│
└── brownfield/         # Brownfield (1→n) workflow
    ├── commands/ (3 commands)
    │   ├── proposal.md.j2      # Change proposal
    │   ├── apply.md.j2         # Apply changes
    │   └── archive.md.j2       # Archive history
    └── templates/              # (brownfield commands use greenfield templates)
```

## Generalization Comparison Table

| SDD Concept | Generic Concept | Use Case Examples |
|---------|-------------|------------|
| Feature | {{ entity_type }} | Feature/Component/TestCase/Document/Design |
| User Story | Scenario / Use Case | Use cases in any domain |
| Implementation | Realization / Generation | Code/Design/Test/Document generation |
| Code | {{ deliverable }} | Code/Design/TestSuite/Documentation |
| Git Branch | Work Context | Version management context (optional) |

## Usage

When generating a speckit, if you need to create a **universal SD-X toolkit** (not limited to software development), use:

```yaml
# Select via metaspec init interactive wizard
source: "generic"

# Or specify in internal configuration
slash_commands:
  - source: "generic"
    name: "constitution"
  - source: "generic"
    name: "specify"
  - source: "generic"
    name: "proposal"
  # ...
```

**Note**: Users don't need to specify `generic/greenfield` or `generic/evolution`, the generator will automatically route to the correct subdirectory based on command name.

### When to Use generic vs sdd

| Use Case | Recommended Directory | Reason |
|---------|---------|------|
| Create software development toolkit | `sdd/` | Retains Feature, User Story, more aligned with development habits |
| Create design system toolkit | `generic/` | No development concepts, suitable for design specifications |
| Create testing framework toolkit | `generic/` | Universal specification-driven, not bound to development terminology |
| Create documentation system toolkit | `generic/` | Suitable for documentation specification management |
| Uncertain domain | `generic/` | More universal, can specialize later |

## Workflow Selection Guide

### When to Use Greenfield

- ✅ Project initialization, quickly create multiple specifications
- ✅ Need frequent iteration and modification
- ✅ Single developer or small team development
- ✅ No need for strict change control

**Example**:
```bash
# Quickly create multiple specifications
/specify "User Authentication"
/specify "Payment Processing"
/specify "Data Analytics"
```

### When to Use Brownfield

- ✅ Specifications are stable
- ✅ Need controlled change management
- ✅ Team collaboration and review
- ✅ Need to preserve change history

**Example**:
```bash
# Propose changes
/proposal "Add OAuth2 support to authentication"
# Review, approve, implement
/apply add-oauth
# Complete and archive
/archive add-oauth
```

### Transition Timing

```
Initial (Greenfield)              Stable (Brownfield)
─────────────────────────────►
Create 10+ specifications         Change management
Rapid iteration                  Controlled evolution
```

**Recommendations**:
1. Use Greenfield in project initialization to quickly develop 10-20 specifications
2. Switch to Brownfield after specifications stabilize for controlled changes
3. Can mix, but recommend clear boundaries

## Command List

### Greenfield Commands (8)

| Command | Purpose | Output |
|------|------|------|
| `/constitution` | Define governance principles | memory/constitution.md |
| `/specify` | Define specification entities | specs/00X-name/spec.md |
| `/clarify` | Resolve specification ambiguities | Update spec.md |
| `/plan` | Plan implementation approach | specs/00X-name/plan.md |
| `/tasks` | Break down tasks | specs/00X-name/tasks.md |
| `/generate` | Generate deliverables | Code/assets in src/ |
| `/validate` | Quality check | Validation report |
| `/analyze` | Consistency analysis | Analysis report |

### Brownfield Commands (3)

| Command | Purpose | Output |
|------|------|------|
| `/proposal` | Create change proposal | changes/xxx/ |
| `/apply` | Apply approved changes | Implement changes |
| `/archive` | Archive completed changes | changes/archive/ |

## Maintenance Notes

- **Source Traceability**: All generic templates come from `sdd/spec-kit` and `sdd/openspec`
- **Sync Strategy**: When upstream sdd/ updates, manually evaluate if generalization sync is needed
- **Extension Rules**: New commands must ensure complete domain independence
- **Internal Separation**: greenfield and brownfield are separated internally in MetaSpec, but user commands remain flat (no prefix)

## Example: Speckit Using Generic Templates

Assume creating a **design system specification toolkit**:

```bash
metaspec init design-system-kit
```

The generated speckit will include:

**Greenfield Phase**:
- `/constitution` → Define design principles
- `/specify` → Define component specifications (not Feature)
- `/generate` → Generate design assets (not code)

**Brownfield Phase**:
- `/proposal` → Propose design changes
- `/apply` → Implement changes
- `/archive` → Archive completion

When users call `/specify`, they will see:
```markdown
# {{ entity_type }} Specification  # e.g., "Component Specification"
## Scenarios & Validation           # Not "User Story"
## Requirements
## Realization Plan                 # Not "Implementation Details"
```

---

**Status**: ✅ Greenfield/Brownfield separation architecture implemented

**Last Updated**: 2025-10-31

**Maintainer**: MetaSpec Core Team
