# SDD Templates (Spec-Driven Development)

> **Specification-Driven Development Workflows**

This directory contains templates for Spec-Driven Development (SDD) methodologies across different project lifecycles.

---

## 📁 Sub-libraries

### spec-kit/

**Source**: [GitHub spec-kit](https://github.com/github/spec-kit)  
**Lifecycle**: Greenfield (0→1)  
**Focus**: Creating new features and projects from scratch  
**Status**: ✅ Active (auto-synced)

**Commands (8)**:
- `constitution` - Define design principles
- `specify` - Create feature specifications
- `clarify` - Resolve ambiguities
- `plan` - Plan implementation
- `tasks` - Break down tasks
- `implement` - Execute implementation
- `checklist` - Quality validation
- `analyze` - Consistency checking

**Best for**:
- New feature development
- Project bootstrapping
- 0→1 product creation

### openspec/

**Source**: OpenSpec project (concept)  
**Lifecycle**: Brownfield (1→n)  
**Focus**: Collaborative specification evolution  
**Status**: ⚠️ Planning stage

**Commands (planned)**:
- `propose` - Propose specification changes
- `review` - Collaborative review process
- `merge` - Merge approved changes
- `version` - Version management
- `track` - Track evolution history

**Best for**:
- Evolving existing specifications
- Team collaboration
- Specification versioning
- 1→n continuous improvement

---

## 🎯 Usage

### Use spec-kit for Greenfield development

```yaml
# Generated speckit configuration (internal)
slash_commands:
  - name: "specify"
    description: "Create feature specification"
    source: "sdd/spec-kit"
    
  - name: "plan"
    description: "Plan implementation"
    source: "sdd/spec-kit"
```

### Use openspec for Brownfield evolution

```yaml
# Generated speckit configuration (internal)
slash_commands:
  - name: "propose"
    description: "Propose specification changes"
    source: "sdd/openspec"
    
  - name: "review"
    description: "Review proposed changes"
    source: "sdd/openspec"
```

### Mix both methodologies

```yaml
# Generated speckit configuration (internal)
slash_commands:
  # Greenfield phase
  - name: "specify"
    source: "sdd/spec-kit"
  
  # Brownfield phase  
  - name: "propose"
    source: "sdd/openspec"
```

---

## 🔄 Syncing Templates

### Sync all development templates

```bash
python scripts/sync-dev-templates.py
```

### Sync individually

```bash
# Sync spec-kit only
python scripts/sync-spec-kit-templates.py

# Sync openspec only (when available)
python scripts/sync-openspec-templates.py
```

---

## 📊 Comparison

| Aspect | spec-kit | openspec |
|--------|----------|----------|
| **Lifecycle** | 0→1 (Greenfield) | 1→n (Brownfield) |
| **Focus** | Creation | Evolution |
| **Collaboration** | Single developer | Team collaboration |
| **Versioning** | Feature branches | Specification versions |
| **Use case** | New features | Specification changes |

---

## 🚀 Future Expansion

This directory may expand to include other development methodologies:
- `tdd-spec/` - Test-Driven Development workflows
- `bdd-spec/` - Behavior-Driven Development workflows
- `ddd-spec/` - Domain-Driven Design workflows

---

**Last updated**: 2025-10-30

