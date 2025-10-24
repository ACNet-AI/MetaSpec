# MetaSpec Quick Start

> Get started with MetaSpec in 5 minutes - from zero to a complete spec-driven toolkit

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

  MetaSpec - Meta-specification framework for generating Spec-Driven X (SD-X) toolkits

Commands:
  init     Create spec-driven toolkit
  spec     Manage and use spec toolkits
  version  Show version information
```

---

## 🎯 Step 2: Create Your First Toolkit

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
MetaSpec - Create Spec-Driven Toolkit

Step 1/5: Basic Information
────────────────────────────────────────

Available domains:
  1. generic - Generic toolkit for any domain
  2. mcp - MCP server development
  3. web - Web development
  4. ai - AI agent development

Select domain [1]: 1
Toolkit name (lowercase-with-dashes) [spec-kit]: my-spec-kit
Brief description [Spec-driven toolkit]: My first spec toolkit

Step 2/5: Entity Design
────────────────────────────────────────

Main entity name [Entity]: Task
...
```

### Option B: Quick Start with Template

```bash
# Generic toolkit
metaspec init my-spec-kit --template generic

# MCP server toolkit
metaspec init mcp-server --template mcp

# Web component toolkit
metaspec init web-toolkit --template web

# AI agent toolkit
metaspec init ai-toolkit --template ai
```

### Option C: Preview Before Creating

```bash
metaspec init my-spec-kit --template generic --dry-run
```

---

## 🔍 Step 3: Explore Generated Toolkit

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

## 🛠️ Step 4: Initialize Toolkit

```bash
# Install dependencies
pip install -e .
```

---

## 🎮 Step 5: Use Generated Toolkit

Your toolkit is now ready:

```bash
# View help
my-spec-kit --help

# Initialize a new spec
my-spec-kit init my-spec.yaml

# Validate spec
my-spec-kit validate my-spec.yaml

# Generate output from spec
my-spec-kit generate my-spec.yaml
```

---

## 🌟 Step 6: Add Spec-Driven Development (Optional)

Want to use spec-driven methodology to develop your toolkit?

```bash
# Create with spec-kit integration
metaspec init my-spec-kit --spec-kit

cd my-spec-kit

# Now you have specs/ directory for requirements
ls specs/
# spec.md  plan.md  tasks.md
```

---

## 🔧 Step 7: Use Unified Spec Interface

MetaSpec provides a unified interface for all spec toolkits:

```bash
# List available spec toolkits
metaspec spec --list

# Use spec-kit (if installed)
metaspec spec spec-kit spec

# Use OpenSpec (if installed)
metaspec spec openspec analyze

# Use your custom toolkit
metaspec spec my-spec-kit init
```

---

## 🎯 Examples

### Create API Testing Toolkit

```bash
metaspec init api-test-kit --template generic
cd api-test-kit
pip install -e .
api-test-kit --help
```

### Create with Spec-Kit for Development

```bash
# Create toolkit with spec-kit
metaspec init my-project --spec-kit

cd my-project

# Use spec-kit for development
metaspec spec spec-kit spec    # Generate spec.md
metaspec spec spec-kit plan    # Generate plan.md
metaspec spec spec-kit tasks   # Generate tasks.md
```

### Update Existing Toolkit with OpenSpec

```bash
cd my-spec-kit

# Initialize OpenSpec
metaspec spec openspec init

# Analyze and update
metaspec spec openspec analyze
metaspec spec openspec plan
metaspec spec openspec implement
```

---

## 🎨 Customize Your Toolkit

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

Install it first:

```bash
pip install git+https://github.com/github/spec-kit.git
```

**Q: OpenSpec not found?**

Install it first:

```bash
pip install git+https://github.com/Fission-AI/OpenSpec.git
```

---

## 🎉 What's Next?

### Learn More

- 📖 [Main README](../README.md) - Complete feature overview
- 🤖 [AGENTS.md](../AGENTS.md) - AI agent workflow guide
- 📚 [Examples](../examples/) - Example toolkit definitions
- 🔧 [Spec Toolkit Protocol](./SPEC_TOOLKIT_PROTOCOL.md) - Build custom spec toolkits

### Advanced Usage

- Use templates for quick start
- Integrate spec-kit for development
- Use OpenSpec for maintenance
- Create custom spec toolkits

---

## 🎊 Congratulations!

You have successfully:

- ✅ Installed MetaSpec
- ✅ Created your first spec-driven toolkit
- ✅ Explored the unified spec interface
- ✅ Learned about spec-kit and OpenSpec integration

Now you can create spec-driven toolkits for any domain!

---

**Version**: v0.1.0 | **Last Updated**: 2025-10-24
