# MetaSpec

> 🤖 **Meta-toolkit for generating Spec-Driven X (SD-X) toolkits for AI Agents**

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python: 3.11+](https://img.shields.io/badge/python-3.11+-blue.svg)](https://www.python.org/downloads/)
[![Status: Alpha](https://img.shields.io/badge/status-alpha-green.svg)]()

---

## 🎯 What is Spec-Driven?

**Spec-Driven** is using structured specifications to drive workflows - from requirements to implementation. Define specs first, validate and generate, then execute. This ensures clarity, consistency, and enables AI agents to understand and assist throughout the process.

## 💡 What is MetaSpec?

**MetaSpec** is a meta-specification framework that enables AI Agents to automatically generate production-ready **Spec-Driven X (SD-X)** toolkits.

Define your toolkit once → Get complete development environment with CLI, parser, validator, templates, and AI agent support.

```
What you can generate:
  ✅ SD-Development  - Spec-driven development toolkits
  ✅ SD-Design       - Spec-driven design systems  
  ✅ SD-Testing      - Spec-driven testing frameworks
  ✅ SD-Operations   - Spec-driven operations tools
  ✅ SD-X            - Any spec-driven workflow
```

### 🌟 Key Features

**1. Meta-Level** - A **meta-toolkit** that generates spec-driven toolkits

**2. Any Domain** - Supports **any** spec-driven domain, not limited to development

**3. Full Lifecycle** - Covers **complete lifecycle** (creation, updates, maintenance)

---

## 🚀 Quick Start

### Installation

```bash
git clone https://github.com/ACNet-AI/MetaSpec.git
cd MetaSpec
uv pip install -e .  # or: pip install -e .
```

### Create Your First Toolkit

**Option 1: Interactive (Recommended)**

```bash
metaspec init                       # Interactive wizard - guides you through
```

**Option 2: Quick start with template**

```bash
metaspec init my-spec-kit --template mcp     # One command, done!
```

**Option 3: Preview first**

```bash
metaspec init my-spec-kit --template api --dry-run    # Preview
metaspec init my-spec-kit --template api              # Create
```

**Result**: Complete toolkit with CLI, parser, validator, templates, and AI agent support!

---

## 📦 Features

**Simple, powerful commands:**

| Command | Description |
|---------|-------------|
| `metaspec init [name]` | 🚀 Create spec-driven toolkit (interactive or template-based) |
| `metaspec spec <toolkit> <cmd>` | 🔧 Manage and use spec toolkits (unified interface) |

**Common usage:**
```bash
# Create toolkit (interactive)
metaspec init

# Create with template (fast)
metaspec init my-api-toolkit --template api

# Create with spec-kit
metaspec init my-spec-kit --spec-kit

# Preview before creating
metaspec init my-spec-kit --template mcp --dry-run

# Use spec toolkits
metaspec spec --list                 # List available toolkits
metaspec spec spec-kit spec          # Use spec-kit
metaspec spec openspec analyze       # Use OpenSpec
```

**What you get**: CLI tools, parser, validator, templates, AGENTS.md, constitution, and full Python package structure.

### 🌟 Unified Spec Toolkit Interface

MetaSpec provides a **unified interface** to manage all spec toolkits:

```bash
# Discover available toolkits
metaspec spec --list

# Use any toolkit through MetaSpec
metaspec spec spec-kit spec      # Spec-driven development
metaspec spec openspec analyze   # Spec-driven updates
metaspec spec api-spec-kit init  # Custom toolkits (extensible)
```

**Built-in support**: `spec-kit`, `openspec`  
**Extensible**: Any toolkit created with MetaSpec can be registered and used

---

## 🤖 AI Assistant Ready

MetaSpec is designed for AI agents with strong reasoning capabilities. Toolkit creation requires meta-level system design, entity modeling, and domain research.

👉 **Complete AI workflow guide**: [AGENTS.md](./AGENTS.md)

---

## 🤝 Works Well With

**MetaSpec** generates spec-driven toolkits. Since generated toolkits are also projects, you can use spec-driven methodologies to develop them.

MetaSpec provides a **unified interface** to work with various spec tools through `metaspec spec`:

| Tool | Purpose | Usage Stage | Access Method |
|------|---------|-------------|--------------|
| **[Spec-Kit](https://github.com/github/spec-kit)** | Spec-driven development (greenfield) | Project creation & development | `metaspec init --spec-kit` or `metaspec spec spec-kit` |
| **[OpenSpec](https://github.com/Fission-AI/OpenSpec)** | Spec-driven updates (brownfield) | Project maintenance | `metaspec spec openspec` |

**Complete Workflow**:

```bash
# 1️⃣ CREATE: Generate toolkit with spec-kit
metaspec new                              # Create meta-spec YAML
metaspec init my-spec-kit.yaml --spec-kit # Generate with spec-kit

# 2️⃣ DEVELOP: Use spec-driven methodology (unified interface)
cd my-spec-kit
metaspec spec spec-kit spec               # Generate spec.md
metaspec spec spec-kit plan               # Generate plan.md
metaspec spec spec-kit tasks              # Generate tasks.md
# AI assistance with /speckit.spec, /speckit.plan commands

# 3️⃣ UPDATE: Use OpenSpec when you need to iterate (unified interface)
metaspec spec openspec init               # First time only
metaspec spec openspec analyze            # Analyze current state
metaspec spec openspec plan               # Plan improvements
metaspec spec openspec implement          # Apply changes
```

**Advantages**:
- ✅ **One command to rule them all** - `metaspec` is your single entry point
- ✅ **No tool switching** - Seamless workflow from creation to maintenance
- ✅ **Extensible** - Support for custom spec toolkits

### 🚀 Ecosystem Vision

MetaSpec is not just a generator—it's a **platform for spec-driven toolkits**:

1. **Create** toolkits with `metaspec init`
2. **Register** them to MetaSpec's ecosystem
3. **Discover** and **use** through unified `metaspec spec` interface
4. **Build network effects** - more toolkits = more value

```bash
# Example: Create and register a custom toolkit
metaspec init api-spec-kit.yaml
pip install ./api-spec-kit

# Now anyone can use it through MetaSpec
metaspec spec api-spec-kit init my-api.yaml
metaspec spec api-spec-kit validate my-api.yaml
```

**Future roadmap**: Plugin marketplace, version management, toolkit discovery

**Prerequisites**: Install [spec-kit](https://github.com/github/spec-kit) to use `--spec-kit`:
```bash
pip install git+https://github.com/github/spec-kit.git
```

📖 **Complete guide**: See [AGENTS.md](./AGENTS.md)

---

## 📖 Example

### Create a Spec-Driven Toolkit

```yaml
# domain-spec-kit.yaml
name: "domain-spec-kit"
version: "0.1.0"
domain: "generic"
description: "Spec-driven toolkit for domain modeling and specifications"

entity:
  name: "DomainModel"
  fields:
    - name: "name"
      type: "string"
      required: true
      description: "Domain model name"
    - name: "entities"
      type: "array"
      required: true
      description: "Domain entities"
    - name: "rules"
      type: "array"
      required: false
      description: "Business rules and constraints"

commands:
  - name: "init"
    description: "Initialize new domain spec"
  - name: "validate"
    description: "Validate domain spec"
  - name: "generate"
    description: "Generate domain model code"
```

```bash
metaspec validate domain-spec-kit.yaml
metaspec init domain-spec-kit.yaml -o ./domain-spec-kit
```

📂 **More examples**: See [examples/](./examples/) (MCP, API testing, design systems)

---

## 🎨 Meta-Spec Format

```yaml
name: "toolkit-name"          # Required
version: "0.1.0"              # Required
domain: "generic|mcp|web|ai"  # Required
description: "..."            # Optional

entity:
  name: "EntityName"
  fields:
    - name: "field_name"
      type: "string|number|boolean|array|object"
      required: true|false

commands:
  - name: "command-name"
    description: "..."

dependencies:
  - "package>=1.0.0"
```

📘 **Complete format reference**: Use `metaspec scaffold --help` or see [templates/](./templates/)

---

## 🛠️ Commands

```bash
metaspec new [--from-speckit PATH]     # Create new toolkit (interactive)
metaspec update [--from-openspec PATH] # Update toolkit (interactive)
metaspec scaffold <domain> -o FILE     # Generate template
metaspec validate FILE [--strict]      # Validate meta-spec
metaspec preview FILE [--verbose]      # Preview generation
metaspec init FILE -o DIR [--force]    # Generate toolkit
```

Use `metaspec <command> --help` for detailed options

---

## 🧪 Development

```bash
# Install dev dependencies
uv pip install -e ".[dev]"

# Run tests
pytest

# Code quality
ruff check src/
ruff format src/
```

📖 **Contributing guide**: See [CONTRIBUTING.md](./docs/CONTRIBUTING.md)

---

## 📚 Documentation

- **[QUICKSTART.md](./docs/QUICKSTART.md)** - 5-minute tutorial
- **[AGENTS.md](./AGENTS.md)** - AI workflow guide
- **[CONTRIBUTING.md](./docs/CONTRIBUTING.md)** - Contribution guide
- **[examples/](./examples/)** - Example meta-specs

---

## 🏗️ Status

**v0.1.0** - Alpha Release 🎉

Core features complete: YAML validation, multi-domain generation, CLI tools, AI agent support, Spec-Kit/OpenSpec integration.

---

## 🤝 Contributing

Contributions welcome! See [CONTRIBUTING.md](./docs/CONTRIBUTING.md) for guidelines.

```bash
git clone https://github.com/ACNet-AI/MetaSpec.git
git checkout -b feature/your-feature
# Make changes, test, commit
git push origin feature/your-feature
```

---

## 📄 License

MIT License - see [LICENSE](./LICENSE)

---

## 🙏 Acknowledgments

Inspired by [Spec-Kit](https://github.com/github/spec-kit), [Protocol Buffers](https://protobuf.dev/), and [OpenAPI](https://www.openapis.org/).

---

**Built for the Spec-Driven Development Community**
