# MetaSpec Quick Start

> Get started with MetaSpec in 5 minutes - from zero to a complete speckit

---

## 📋 Prerequisites

- Python 3.11+
- pip or uv

---

## 🚀 Step 1: Install MetaSpec

### Using uv (Recommended)

```bash
# Clone the repository
git clone https://github.com/ACNet-AI/MetaSpec.git
cd MetaSpec

# Install
uv pip install -e .
```

### Using pip

```bash
pip install -e .
```

### Verify Installation

```bash
metaspec --help
```

You should see:

```
Usage: metaspec [OPTIONS] COMMAND [ARGS]...

  MetaSpec - Meta-specification framework for generating Spec-Driven X (SD-X) speckits

Commands:
  init     Create spec-driven speckit
  spec     Manage and use speckits
  version  Show version information
```

---

## 🎯 Step 2: Create Your First Speckit

### Option A: Interactive Mode (Recommended for first time)

```bash
metaspec init
```

The interactive wizard will guide you through:

1. **Domain Selection** - Choose from generic, mcp, web, ai
2. **Basic Information** - Name, description
3. **Entity Design** - Define your main entity and fields
4. **Commands** - Specify CLI commands
5. **Dependencies** - Select Python packages

Example session:

```
MetaSpec - Create Spec-Driven Speckit

Step 1/5: Basic Information
────────────────────────────────────────

Available domains:
  1. generic - Generic speckit for any domain
  2. mcp - MCP server development
  3. web - Web development
  4. ai - AI agent development

Select domain [1]: 1
Speckit name (lowercase-with-dashes) [spec-kit]: my-spec-kit
Brief description [Spec-driven speckit]: My first speckit

Step 2/5: Entity Design
────────────────────────────────────────

Main entity name [Entity]: Task
...
```

### Option B: Quick Start with Template

```bash
# Generic speckit (recommended)
metaspec init my-spec-kit --template generic
```

### Option C: Preview Before Creating

```bash
metaspec init my-spec-kit --template generic --dry-run
```

---

## 🔍 Step 3: Explore Generated Speckit

```bash
cd my-spec-kit
ls -la
```

You'll see the complete project structure:

```
my-spec-kit/
├── README.md              # Project documentation
├── AGENTS.md              # AI Agent operation guide
├── pyproject.toml         # Python project configuration
├── .gitignore             # Git configuration
├── memory/
│   └── constitution.md    # Development principles
├── scripts/
│   ├── init.sh           # Initialization script ⚡
│   └── validate.sh       # Validation script ⚡
├── templates/
│   └── spec-template.md  # Spec template
└── src/
    └── my_spec_kit/
        ├── __init__.py
        ├── cli.py        # CLI entry point
        ├── parser.py     # Spec parser
        └── validator.py  # Spec validator
```

---

## 🛠️ Step 4: Install and Develop

```bash
# Install dependencies
pip install -e .

# Use built-in MetaSpec commands to develop your speckit (in Cursor/AI editor)
# /metaspec.constitution  - Define design principles
# /metaspec.specify       - Define specifications
# /metaspec.plan          - Plan implementation
# /metaspec.implement     - Implement features
```

---

## 🔧 Step 5: Unified Spec Interface

MetaSpec provides a unified interface for all speckits:

```bash
# List available speckits
metaspec spec --list

# Generated speckits include built-in MetaSpec commands (11 total):
# Definition Commands (8) - Active development
# /metaspec.constitution, /metaspec.specify, /metaspec.clarify, /metaspec.plan,
# /metaspec.tasks, /metaspec.implement, /metaspec.checklist, /metaspec.analyze
# Evolution Commands (3) - Controlled changes
# /metaspec.proposal, /metaspec.apply, /metaspec.archive

# Optional: Use external tools (install separately)
metaspec spec spec-kit init        # Alternative workflow
metaspec spec openspec analyze     # Alternative evolution

# Use your custom speckit
metaspec spec my-spec-kit <command>
```

---

## 🎯 Examples

### Create API Testing Speckit

```bash
metaspec init api-test-kit --template generic
cd api-test-kit
pip install -e .
```

### Develop Speckit with Built-in MetaSpec Commands

```bash
# Create speckit
metaspec init my-project --template generic
cd my-project

# Use built-in MetaSpec slash commands in your editor (no installation needed):

# Definition Commands (8) - Active development
# /metaspec.constitution - Define project principles
# /metaspec.specify      - Define specifications
# /metaspec.clarify      - Clarify ambiguities
# /metaspec.plan         - Plan implementation
# /metaspec.tasks        - Break down tasks
# /metaspec.implement    - Execute implementation
# /metaspec.checklist    - Validate quality
# /metaspec.analyze      - Check consistency

# Evolution Commands (3) - Controlled changes
# /metaspec.proposal     - Propose specification changes
# /metaspec.apply        - Apply approved changes
# /metaspec.archive      - Archive completed changes
```

### Optional: Use External Spec Tools

```bash
cd my-project

# If you prefer external spec tools (install separately):
# metaspec spec spec-kit <command>    # Alternative workflow
# metaspec spec openspec <command>    # Alternative evolution
```

---

## 🎨 Customize Your Speckit

After generation, you can:

1. **Edit Entity Fields** - Modify entity definition in generated code
2. **Add Commands** - Extend CLI commands in cli.py
3. **Customize Templates** - Edit templates for spec file format
4. **Add Dependencies** - Update pyproject.toml

---

## 🐛 Troubleshooting

### Common Issues

**Q: How to overwrite an existing directory?**

```bash
metaspec init my-spec-kit --template generic --force
```

**Q: How to preview before creating?**

```bash
metaspec init my-spec-kit --template generic --dry-run
```

**Q: Spec-kit not found?**

Spec-kit is an optional integrated toolkit. Install it:

```bash
pip install git+https://github.com/github/spec-kit.git
```

**Q: Do I need to install spec-kit/openspec?**

No! Generated toolkits include built-in MetaSpec commands (15 commands: 4 SDS + 8 SDD + 3 Evolution) for complete spec-driven workflows. External tools (spec-kit, OpenSpec) are optional alternatives.

**Q: What's the difference between MetaSpec commands and external tools?**

- **MetaSpec commands**: Built-in, no installation, unified workflow (recommended)
- **External tools**: Alternative workflows, require separate installation

---

## 🎉 What's Next?

### Learn More

- 📖 [Main README](../README.md) - Complete feature overview
- 🤖 [AGENTS.md](../AGENTS.md) - AI agent workflow guide
- 📚 [Examples](../examples/) - Example speckit definitions
- 🔧 [Speckit Protocol](./speckit-protocol.md) - Build custom speckits

### Advanced Usage

- Use templates for quick start
- Use built-in MetaSpec commands for development
- Create custom speckits
- Optional: Integrate external spec tools

---

## 🎊 Congratulations!

You have successfully:

- ✅ Installed MetaSpec
- ✅ Created your first speckit
- ✅ Explored built-in MetaSpec commands (15 commands: 4 SDS + 8 SDD + 3 Evolution)
- ✅ Learned about the unified spec interface

Now you can create speckits for any domain!

---

**Version**: v0.1.0 | **Last Updated**: 2025-10-31
