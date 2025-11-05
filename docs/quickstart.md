# MetaSpec Quick Start

> Get started with MetaSpec in 5 minutes - from zero to a complete speckit

---

## 📋 Prerequisites

- Python 3.11+
- pip or uv

---

## 🚀 Step 1: Install MetaSpec

```bash
# Recommended: Use uv (10-100x faster) ⚡
uv pip install git+https://github.com/ACNet-AI/MetaSpec.git

# Or use pip
pip install git+https://github.com/ACNet-AI/MetaSpec.git

# Verify installation
metaspec --version
```

<details>
<summary>💡 First time using uv? Install in one line</summary>

```bash
# macOS/Linux
curl -LsSf https://astral.sh/uv/install.sh | sh

# Windows
powershell -c "irm https://astral.sh/uv/install.ps1 | iex"
```
</details>

<details>
<summary>🔧 Development mode installation</summary>

```bash
git clone https://github.com/ACNet-AI/MetaSpec.git && cd MetaSpec
uv pip install -e .
```
</details>

---

## 🎯 Step 2: Create Your First Speckit

```bash
# Interactive mode (recommended)
metaspec init

# Or quick start with template
metaspec init my-spec-kit --template generic

# Preview (dry-run)
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

## 🛠️ Step 4: Install and Use

```bash
# Enter generated project
cd my-spec-kit

# Install
uv pip install -e .

# Use 16 built-in MetaSpec commands (in AI editor)
# SDS: /metaspec.sds.* (5 commands) - Define protocol
# SDD: /metaspec.sdd.* (8 commands) - Develop toolkit
# Evolution: /metaspec.* (3 commands) - Manage changes
```

---

## 🎯 Complete Example

```bash
# 1. Create speckit
metaspec init api-kit --template generic && cd api-kit

# 2. Install
uv pip install -e .

# 3. Develop with built-in commands (in AI editor)
# /metaspec.sds.specify  - Define API protocol
# /metaspec.sdd.plan     - Design toolkit architecture
# /metaspec.sdd.implement - Implement toolkit code
```

---

## 🐛 FAQ

```bash
# Force overwrite existing directory
metaspec init my-kit --template generic --force

# Preview (dry-run)
metaspec init my-kit --template generic --dry-run
```

**Q: Do I need to install spec-kit or openspec?**  
**A**: No! Generated speckit includes 15 built-in MetaSpec commands for complete workflow.

---

## 📚 Learn More

- 📖 [README](../README.md) - Complete feature overview
- 🤖 [AGENTS.md](../AGENTS.md) - AI workflow guide
- 📚 [Examples](../examples/) - Example projects

---

**Congratulations!** You've mastered MetaSpec basics and can now create speckits for any domain! 🎉
