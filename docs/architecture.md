# Template Architecture

> **MetaSpec's Three-Layer Template Architecture Design**

---

## 🎯 Overview

MetaSpec uses a three-layer architecture to organize templates:

1. **MetaSpec Internal** - Source and organization of templates
2. **Speckit** - Generated spec-driven speckit
3. **End Project** - Projects developed using the speckit

**Recursive Pattern**: Each layer (MetaSpec, Speckit, User Project) follows the same structure with `memory/` (principles), `specs/` (specifications), and `changes/` (evolution). This consistency enables AI-assisted development at every level.

---

## 📁 Three-Layer Architecture

### Layer 1: MetaSpec Internal Templates

```
src/metaspec/templates/
│
├── base/                    # Speckit project base files
│   ├── AGENTS.md.j2
│   ├── README.md.j2
│   ├── constitution.md.j2
│   └── pyproject.toml.j2
│
├── library/                 # Common template pool (three-layer generalization)
│   ├── sdd/                 # First layer: SDD-specific templates
│   │   ├── spec-kit/        # Greenfield (0→1) from spec-kit
│   │   │   ├── commands/
│   │   │   └── templates/
│   │   └── openspec/        # Brownfield (1→n) from OpenSpec
│   │       ├── commands/
│   │       └── templates/
│   └── generic/             # Second layer: Universal SD-X templates
│
└── meta/                     # Third layer: MetaSpec self-development (SDS + SDD)
    ├── sds/                 # Protocol specification commands
    │   └── commands/        # /metaspec.sds.* (4 commands)
    └── sdd/                 # Speckit development commands
        └── commands/        # /metaspec.sdd.* (8 commands)
```

**Note**: `library/` is only an internal organization method in MetaSpec; it's flattened during generation.

---

### Layer 2: Generated Speckit

```
api-test-kit/                       # Generated speckit
│
├── .metaspec/
│   ├── commands/                   # MetaSpec development commands (15 commands)
│   │   ├── metaspec.sds.*.md      # Protocol specification (4 commands)
│   │   ├── metaspec.sdd.*.md      # Speckit development (8 commands)
│   │   └── metaspec.*.md          # Evolution management (3 commands)
│   └── templates/                  # MetaSpec shared output templates (5 files)
│       ├── constitution-template.md.j2
│       ├── spec-template.md.j2
│       ├── plan-template.md.j2
│       ├── tasks-template.md.j2
│       └── checklist-template.md.j2
│
├── templates/                      # 📚 Reference templates (flat structure, for development)
│   ├── commands/                  # Slash command templates (optional)
│   ├── spec-template.md           # From library/sdd/spec-kit/templates/
│   ├── plan-template.md
│   ├── tasks-template.md
│   ├── checklist-template.md
│   └── agent-file-template.md
│
├── specs/                          # Development workspace (.gitignore)
│   ├── protocol/                  # SDS: Protocol specifications
│   └── toolkit/                   # SDD: Toolkit specifications
│
├── changes/                        # Evolution: Change proposals (parallel to specs/)
│   ├── add-websocket/
│   └── improve-parser/
│
├── src/api_test_kit/
│   ├── __init__.py
│   ├── cli.py
│   ├── parser.py
│   └── validator.py
│
├── scripts/
│   ├── init.sh
│   └── bash/
│       ├── create-new-feature.sh
│       ├── check-prerequisites.sh
│       └── setup-plan.sh
│
├── memory/
│   └── constitution.md
│
├── README.md
├── AGENTS.md
├── CHANGELOG.md
├── pyproject.toml
├── .gitignore
└── examples/
```

**Key Points**:
- ✅ `.metaspec/commands/` contains 15 MetaSpec development commands
- ✅ `.metaspec/templates/` contains 5 shared output templates
- ✅ `templates/` (root) contains development reference templates (flat structure)
- ✅ `specs/` has 2 subdirectories: `protocol/` (SDS), `toolkit/` (SDD)
- ✅ `changes/` is **parallel to specs/** - temporary workspace for evolution proposals
- ✅ `src/{package}/` contains CLI, parser, validator stubs

---

### Layer 3: End User Project

When users use a speckit to develop their projects, they should follow the same pattern:

```
my-api-project/                     # User project using api-test-kit
│
├── .apitestkit/                   # Speckit's workspace (not .cursor!)
│   ├── commands/                  # Commands provided by speckit
│   │   ├── apitestkit.plan.md    # Domain-specific commands
│   │   ├── apitestkit.validate.md
│   │   ├── apitestkit.generate.md
│   │   ├── apitestkit.proposal.md # Evolution commands (if speckit provides)
│   │   ├── apitestkit.apply.md
│   │   └── apitestkit.archive.md
│   └── templates/                 # Output templates (if needed)
│
├── memory/
│   └── constitution.md            # THIS project's development principles
│
├── specs/                          # THIS project's specifications
│   └── my-api-spec.yaml
│
├── changes/                        # (Optional) Change proposals for THIS project's specs
│   ├── add-new-endpoint/
│   └── improve-validation/
│
├── templates/                      # Output format templates (optional)
│   └── custom-template.md
│
└── README.md
```

**Key Points**:
- ✅ **Same structure as MetaSpec and speckit projects** - Recursive consistency
- ✅ `.{speckit-name}/` is the speckit's workspace (not `.cursor/` - AI editor agnostic!)
- ✅ `memory/constitution.md` defines **this project's** development principles
- ✅ `specs/` contains **this project's** specification documents
- ✅ `changes/` (optional) manages evolution of **this project's** specs

**Philosophy - Recursive Consistency**: 
- MetaSpec uses spec-kit → has `.specify/` + `memory/` + `specs/` + `changes/`
- Speckit uses MetaSpec → has `.metaspec/` + `memory/` + `specs/` + `changes/`
- User project uses speckit → has `.{speckit-name}/` + `memory/` + `specs/` + `changes/`

**Every layer has the same structure!**

**Design Principle**: Use `.{speckit-name}/` instead of `.cursor/` to be AI-editor agnostic. Not all users use Cursor - some use Claude, other AI editors, or no AI at all.

---

## 🔄 Complete Workflow

### Scenario 1: Generate Speckit

```bash
$ metaspec init api-test-kit

Execution:
1. Copy base/* → api-test-kit/ (README, AGENTS.md, etc.)
2. Copy meta/commands/* → api-test-kit/.metaspec/commands/
3. Copy library/sdd/spec-kit/templates/* → api-test-kit/templates/ (flattened)
4. Generate src/api_test_kit/ (cli.py, parser.py, etc.)
```

### Scenario 2: Develop Speckit

```bash
$ cd api-test-kit

# Use MetaSpec SDD command to specify speckit
$ /metaspec.sdd.specify "Define APITest entity and validator"
→ Read .metaspec/commands/metaspec.sdd.specify.md
→ Reference metaspec template protocol
→ Generate specs/toolkit/001-api-test-kit/spec.md

# Plan implementation
$ /metaspec.sdd.plan "Plan parser and validator architecture"
→ Generate specs/toolkit/001-api-test-kit/plan.md

# Break down tasks
$ /metaspec.sdd.tasks "Create implementation tasks"
→ Generate specs/toolkit/001-api-test-kit/tasks.md
```

### Scenario 3: Package Speckit

```bash
# After speckit development is complete
$ pip install -e .

Structure:
src/api_test_kit/
└── templates/              # Packaged templates
    ├── commands/           # Selected commands
    │   ├── plan.md.j2     # From library
    │   ├── tasks.md.j2    # From library
    │   └── design-endpoint.md.j2  # Custom
    └── templates/          # Selected output formats
        ├── plan-template.md.j2
        └── endpoint-design-template.md.j2

Cleanup (for distribution):
rm -rf .metaspec/           # MetaSpec development commands (optional)
rm -rf specs/               # Development work files (optional)
```

### Scenario 4: Use Packaged Speckit

```bash
# After speckit is published and installed
pip install api-test-kit

# Use as a library or CLI tool
api-test-kit validate my-api-spec.yaml
api-test-kit generate my-api-spec.yaml
```

**Note**: How end users use the speckit depends on the speckit's implementation. MetaSpec generates the speckit itself, not the end-user workflow.

---

## 🎨 Template Selection Decision Tree

```
When speckit developer designs workflow:

1. Check templates/ directory
   ✅ plan-template.md exists
   ✅ tasks-template.md exists
   ✅ checklist-template.md exists
   ❌ endpoint-design-template.md doesn't exist

2. Decision
   ✅ Use existing plan, tasks, checklist
   ✅ Create custom endpoint-design

3. Configure in MetaSpecDefinition
   slash_commands:
     - name: "plan"
       template: "templates/plan-template.md.j2"
     
     - name: "design-endpoint"
       template: "templates/endpoint-design-template.md.j2"

4. Implement custom template
   → Create endpoint-design-template.md in templates/ (development reference)
   → Create .j2 file in src/*/templates/templates/ (for packaging)
   → Create command instruction in src/*/templates/commands/ (for packaging)
```

---

## ✅ Key Principles

### 1. Flatten Output

**❌ Don't do this**:
```
api-test-kit/
└── templates/
    └── library/                # Don't expose internal organization
        ├── plan-template.md
        └── tasks-template.md
```

**✅ Do this**:
```
api-test-kit/
└── templates/                  # Flat structure
    ├── plan-template.md
    ├── tasks-template.md
    └── custom-template.md      # Custom and library templates at same level
```

### 2. Unified Protocol

All templates (whether from library or custom) follow:
- Slash Command Template Protocol
- Same file structure
- Same variable naming
- Same usage pattern

### 3. Clear Responsibilities

| Template Source | Purpose | Location |
|----------------|---------|----------|
| `base/` | Speckit project files | Speckit root directory |
| `library/sdd/spec-kit/` | Greenfield development (0→1) | Speckit `templates/` |
| `library/sdd/openspec/` | Brownfield evolution (1→n) | Speckit `templates/` |
| `library/generic/` | Universal templates | Speckit `templates/` |
| `meta/` | MetaSpec speckit development support | Speckit `.metaspec/commands/` |
| Custom | Domain-specific functionality | Speckit `templates/` + `src/*/templates/` |

---

## 📚 References

- [Slash Command Template Protocol](./slash-cmd-protocol.md)
- [AGENTS.md Guide](../AGENTS.md)
- [MetaSpec README](../README.md)

---

**Last Updated**: 2025-10-31
