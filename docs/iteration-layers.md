# MetaSpec Iteration Layers - Visual Guide

> **Quick Reference**: When to use which layer and how they work together

---

## 🎯 Two Layers of Iteration

```
┌─────────────────────────────────────────────────────────────────┐
│                    MetaSpec Iteration System                    │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│  Layer 1: Evolution (Formal Change Management)                 │
│  ┌───────────────────────────────────────────────────────────┐ │
│  │ Purpose: Modify specification with controlled process     │ │
│  │ Commands: /metaspec.proposal → apply → archive            │ │
│  │ Output: changes/[id]/proposal.md, spec-delta.md          │ │
│  │ Modifies: spec.md (after approval)                        │ │
│  └───────────────────────────────────────────────────────────┘ │
│                                                                 │
│  Layer 2: Command Iteration (Daily Quality Checks)             │
│  ┌───────────────────────────────────────────────────────────┐ │
│  │ Purpose: Validate specification quality                   │ │
│  │ Commands: /metaspec.sds.checklist (update mode)           │ │
│  │ Output: checklists/comprehensive-quality.md               │ │
│  │ Modifies: NEVER modifies spec.md                          │ │
│  └───────────────────────────────────────────────────────────┘ │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

---

## 🔄 Complete Workflow Diagram

```
┌─────────────────────────────────────────────────────────────────┐
│                     User wants to change spec                   │
└───────────────────────────┬─────────────────────────────────────┘
                            │
                            ▼
                ┌───────────────────────────┐
                │ Is toolkit released?      │
                │ (v1.x.x or published)     │
                └───────────┬───────────────┘
                            │
              ┌─────────────┼─────────────┐
              │ YES                       │ NO
              ▼                           ▼
    ┌──────────────────────┐    ┌──────────────────────┐
    │ Use Evolution Layer  │    │ Check change type    │
    │                      │    └──────────┬───────────┘
    │ /metaspec.proposal   │               │
    └──────────────────────┘     ┌─────────┼─────────┐
              │                  │ Breaking/Major    │ Minor
              │                  ▼                   ▼
              │         ┌──────────────────┐  ┌────────────────┐
              │         │ Use Evolution    │  │ Direct Edit    │
              │         │                  │  │                │
              │         │ /metaspec.       │  │ vim spec.md    │
              │         │   proposal       │  │                │
              │         └──────────────────┘  └────────┬───────┘
              │                  │                     │
              └──────────────────┼─────────────────────┘
                                 │
                                 ▼
                    ┌──────────────────────┐
                    │ Execute change       │
                    │                      │
                    │ Evolution: apply     │
                    │ Direct: edit done    │
                    └──────────┬───────────┘
                               │
                               ▼
                    ┌──────────────────────┐
                    │ Validate Quality     │
                    │                      │
                    │ /metaspec.sds.       │
                    │   checklist          │
                    │   (update mode)      │
                    └──────────┬───────────┘
                               │
                               ▼
                    ┌──────────────────────┐
                    │ Quality OK?          │
                    └──────────┬───────────┘
                               │
                    ┌──────────┼──────────┐
                    │ YES               │ NO
                    ▼                   ▼
            ┌──────────────┐    ┌──────────────────┐
            │ Evolution:   │    │ Fix issues and   │
            │ archive      │    │ repeat           │
            │              │    └──────────────────┘
            │ Direct: Done │
            └──────────────┘
```

---

## 📊 Layer Comparison Table

| Aspect | Evolution Layer | Command Layer |
|--------|----------------|---------------|
| **Purpose** | Modify spec.md | Validate spec.md |
| **Modifies Spec** | ✅ YES (after approval) | ❌ NO (read-only) |
| **When** | Released OR Breaking/Major | Anytime (quality check) |
| **Workflow** | Proposal → Apply → Archive | Generate → Update → Update |
| **Output** | changes/[id]/proposal.md | checklists/quality.md |
| **Overhead** | Heavy (formal process) | Light (immediate feedback) |
| **Version Control** | ✅ Required | ❌ Not needed |
| **Impact Analysis** | ✅ Required | ❌ Not needed |
| **Approval** | ✅ Required | ❌ Not needed |

---

## 🎮 Usage Scenarios

### Scenario 1: Draft Toolkit - Add Example (Minor)

```bash
# Toolkit: v0.2.0 (draft)
# Change: Add usage example

1. vim specs/domain/001-mcp/spec.md
   # Add example section

2. /metaspec.sds.checklist
   # AI detects existing checklist
   → Mode: update (default)
   → CHK010: ❌ → ✅ (Examples added)

3. Done! ✅
```

**Layer used**: Command Layer only (no Evolution needed)

---

### Scenario 2: Draft Toolkit - Add New Entity (Major)

```bash
# Toolkit: v0.2.0 (draft)
# Change: Add new "Notification" entity

1. /metaspec.proposal "Add Notification entity" --type sds
   → Creates changes/2025-11-05-add-notification/

2. Review proposal.md and approve

3. /metaspec.apply 2025-11-05-add-notification
   → Executes tasks, modifies spec.md

4. /metaspec.sds.checklist
   → Validates new entity quality
   → CHK001-CHK010: Check Notification entity

5. /metaspec.archive 2025-11-05-add-notification
   → Moves to archive, updates CHANGELOG

Done! ✅
```

**Layers used**: Evolution Layer + Command Layer (validation)

---

### Scenario 3: Released Toolkit - Fix Typo (Minor but Released)

```bash
# Toolkit: v1.0.0 (released)
# Change: Fix typo in description

1. /metaspec.proposal "Fix typo in entity description" --type sds
   → Even minor changes need Evolution for released toolkit

2. Review and approve

3. /metaspec.apply 2025-11-05-fix-typo
   → Version: v1.0.0 → v1.0.1 (PATCH)

4. /metaspec.sds.checklist
   → Validates fix

5. /metaspec.archive 2025-11-05-fix-typo

Done! ✅
```

**Layers used**: Evolution Layer (required for released) + Command Layer

---

### Scenario 4: Quality Check Only (No Changes)

```bash
# Toolkit: any version
# Purpose: Check spec quality

1. /metaspec.sds.checklist
   → Generates quality report
   → Identifies issues: CHK003 ❌, CHK007 ⚠️

2. User reviews issues

3. If fixes needed:
   → Draft: Direct edit → Re-run checklist
   → Released: /metaspec.proposal

Done! ✅
```

**Layer used**: Command Layer only

---

## 🚦 Decision Matrix

| Toolkit Status | Change Type | Method | Example |
|----------------|-------------|--------|---------|
| **Draft (v0.x.x)** | Fix typo | Direct edit | `vim spec.md` |
| **Draft (v0.x.x)** | Add example | Direct edit | `vim spec.md` |
| **Draft (v0.x.x)** | Add optional field | Direct edit | `vim spec.md` |
| **Draft (v0.x.x)** | Add required field | Evolution or Direct* | Breaking → Evolution preferred |
| **Draft (v0.x.x)** | Add new entity | Evolution | Major change → Evolution |
| **Released (v1.x.x)** | Any change | Evolution | ALWAYS Evolution |

*Note: For draft toolkit, if near release (v0.9.x), use Evolution for breaking changes too.

---

## 🔑 Key Principles

### Principle 1: Command Layer Never Modifies

```yaml
✅ Checklist reads:
  - specs/domain/XXX/spec.md
  
✅ Checklist writes:
  - checklists/comprehensive-quality.md
  
❌ Checklist NEVER modifies:
  - spec.md
```

---

### Principle 2: Evolution for Formal Changes

```yaml
Use Evolution when:
  - Toolkit is released (v1.x.x)
  - Breaking changes
  - Major features
  - Need version control and impact analysis
```

---

### Principle 3: Direct Edit for Fast Iteration

```yaml
Use Direct Edit when:
  - Toolkit is draft (v0.x.x)
  - Minor, non-breaking changes
  - Fast iteration needed
  - THEN validate with checklist
```

---

## 🎯 No Conflict Between Layers

**Q: Can they conflict?**  
**A: No, they serve different purposes.**

- **Evolution**: MODIFY spec.md (formal process)
- **Command**: VALIDATE spec.md (read-only)

**They complement each other**:
```
Evolution modifies → Command validates → Evolution archives
```

---

## 📚 Reference

For detailed decision guide, see:
- `docs/evolution-guide.md` - Complete decision tree
- `memory/constitution.md` - Principle #6: Iteration-Aware Design
- `src/metaspec/templates/meta/sds/commands/checklist.md.j2` - Command Layer
- `src/metaspec/templates/meta/evolution/commands/proposal.md.j2` - Evolution Layer

---

## 🚀 Best Practices

1. **Always validate after modifying**
   ```bash
   # After ANY modification (Evolution or direct)
   $ /metaspec.sds.checklist
   ```

2. **Use Evolution for released toolkits**
   ```bash
   # If v1.x.x, ALWAYS use Evolution
   $ /metaspec.proposal "..."
   ```

3. **Fast iterate in draft phase**
   ```bash
   # If v0.x.x, iterate quickly
   $ vim spec.md
   $ /metaspec.sds.checklist  # validate
   $ vim spec.md              # fix issues
   $ /metaspec.sds.checklist  # validate again
   ```

4. **Track iterations with checklist**
   ```bash
   # Checklist automatically tracks:
   ## Iteration 1: [2025-11-03]
   ## Iteration 2: [2025-11-05]
   ```

---

## ✅ Summary

**Two layers, zero conflict, perfect synergy:**

```
Evolution Layer (Modify) + Command Layer (Validate) = Robust Iteration
```

**When to use what:**

```
Released?
  YES → Evolution
  NO → Breaking/Major?
    YES → Evolution
    NO → Direct Edit + Checklist
```

**Always validate:**

```
After ANY change → /metaspec.sds.checklist (update mode)
```

