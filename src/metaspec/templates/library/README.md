# MetaSpec Template Library

This directory contains MetaSpec's template library for generating various Spec-Driven X (SD-X) toolkits.

## 📁 Directory Structure

```
library/
├── generic/           # Universal SD-X templates (pure abstraction)
│   ├── commands/      # 11 universal commands
│   └── templates/     # Universal output templates
│
└── sdd/               # Spec-Driven Development (development-specific)
    ├── spec-kit/      # Greenfield development (0→1)
    └── openspec/      # Brownfield evolution (1→n)
```

## 🎯 Generic vs SDD

### Generalization Chain

```
[Original Projects] spec-kit, OpenSpec
      ↓ First generalization
      ↓ - Generalize CLI name: openspec → {{ cli_name }}
      ↓ - Generalize command prefix: /speckit.* → /{{ cli_prefix }}.*
      ↓
[library/sdd/] ← Development-specific
      ↓ Second generalization
      ↓ - Generalize domain concepts: Feature → {{ entity_type }}
      ↓ - Generalize scenario terms: User Story → Scenario
      ↓ - Generalize deliverables: Code → {{ deliverable }}
      ↓
[library/generic/] ← Pure SD-X universal
```

### Generic: Pure Abstraction (Second Generalization)

**Purpose**: Applicable to any specification-driven scenario, completely domain-agnostic

**Source**: Abstracted from `sdd/`

**Characteristics**:
- No development-specific concepts
- Uses universal variables: `{{ entity_type }}`, `{{ deliverable }}`
- Applicable to any SD-X scenario

**Use Cases**:
- Create design system toolkits (SD-Design)
- Create testing framework toolkits (SD-Testing)
- Create documentation system toolkits (SD-Documentation)
- Create universal specification-driven tools

**Command List** (11 commands):
- Definition commands (8): constitution, specify, clarify, plan, tasks, generate, validate, analyze
- Evolution commands (3): proposal, apply, archive

### SDD: Development Specialization (First Generalization)

**Purpose**: Specifically for software development scenarios

**Source**: Synced from spec-kit and OpenSpec

**Characteristics**:
- Retains development concepts: Feature, User Story, Implementation, Code
- More aligned with developer habits
- Includes development-specific checks and processes

**Subdirectories**:

#### sdd/spec-kit/
- **Source**: GitHub spec-kit project
- **Lifecycle**: Greenfield (0→1)
- **Focus**: New feature development
- **Commands**: 8 definition commands + 5 output templates

#### sdd/openspec/
- **Source**: OpenSpec project
- **Lifecycle**: Brownfield (1→n)
- **Focus**: Specification evolution
- **Commands**: 3 evolution commands

## 📊 Terminology Comparison

| SDD Concept | Generic Concept | Use Case Examples |
|---------|-------------|------------|
| Feature | {{ entity_type }} | Feature/Component/TestCase/Document/Design |
| User Story | Scenario / Use Case | Use cases in any domain |
| Implementation | Realization / Generation | Code/Design/Test/Document generation |
| Code | {{ deliverable }} | Code/Design/TestSuite/Documentation |
| Git Branch | Work Context | Version management context (optional) |

## 🚀 Usage Guide

### Choose Generic or SDD?

| Use Case | Recommendation | Reason |
|---------|------|------|
| Software development toolkit | `sdd/` | Retains development concepts, more natural |
| Design system toolkit | `generic/` | No development concepts, highly universal |
| Testing framework toolkit | `generic/` | Suitable for specification-driven testing |
| Documentation system toolkit | `generic/` | Suitable for documentation specification management |
| Uncertain domain | `generic/` | Highly universal, can be specialized later |

### Usage Examples

Select via interactive wizard when generating speckit:

```yaml
# Universal SD-X toolkit
source: "generic"

# Or software development toolkit
source: "sdd/spec-kit"   # Greenfield
source: "sdd/openspec"   # Brownfield
```

## 🔄 Maintenance Notes

### Sync Strategy

- **sdd/spec-kit**: Synced via `scripts/sync-spec-kit-templates.py`
- **sdd/openspec**: Synced via `scripts/sync-openspec-templates.py`
- **generic**: Manually abstracted from sdd/, evaluate if updates needed

### Extension Rules

1. **Add sdd templates**: Sync scripts handle automatically
2. **Add generic templates**: Ensure completely domain-agnostic
3. **Add domain library**: Specialize by referencing generic/

## 🌟 Future Expansion

```
library/
├── generic/           # SD-X universal foundation
├── sdd/               # SD-Development specialization
├── sd-design/         # SD-Design specialization (future)
├── sd-testing/        # SD-Testing specialization (future)
└── sd-documentation/  # SD-Documentation specialization (future)
```

Each new domain library should:
1. Reference generic/ command structure
2. Specialize based on domain characteristics
3. Maintain correspondence with generic/
4. Provide clear use case descriptions

---

**Maintainer**: MetaSpec Core Team  
**Last Updated**: 2025-10-30

