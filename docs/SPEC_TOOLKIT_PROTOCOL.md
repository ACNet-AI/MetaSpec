# Spec Toolkit Protocol

> **Version**: 0.1.0  
> **Status**: Draft

## Overview

The **Spec Toolkit Protocol** defines a standard interface that all spec toolkits should implement to integrate with MetaSpec's ecosystem. This enables:

- **Unified discovery** - Users can find available toolkits through `metaspec spec --list`
- **Consistent usage** - All toolkits work through `metaspec spec <toolkit> <command>`
- **Extensibility** - Anyone can create toolkits that integrate with MetaSpec

## Protocol Definition

### Python Protocol (Recommended)

If you're building a toolkit in Python, implement the `SpecToolkitProtocol`:

```python
from typing import Protocol

class SpecToolkitProtocol(Protocol):
    @property
    def name(self) -> str:
        """Toolkit name (e.g., 'api-spec-kit')"""
        ...
    
    @property
    def version(self) -> str:
        """Toolkit version (e.g., '0.1.0')"""
        ...
    
    @property
    def description(self) -> str:
        """Short description of the toolkit"""
        ...
    
    @property
    def commands(self) -> list[str]:
        """Available commands (e.g., ['init', 'validate', 'generate'])"""
        ...
    
    def execute(self, command: str, args: list[str]) -> int:
        """Execute a command, return exit code"""
        ...
```

### CLI Standard (Language-Agnostic)

For toolkits in any language, implement a CLI that follows these conventions:

#### 1. Command Structure

```bash
<toolkit-name> <command> [args...]
```

Example:
```bash
api-spec-kit init my-api.yaml
api-spec-kit validate my-api.yaml
api-spec-kit generate my-api.yaml
```

#### 2. Required Commands

All toolkits should support these commands:

| Command | Purpose | Example |
|---------|---------|---------|
| `init` | Initialize/create a new spec file | `toolkit init spec.yaml` |
| `validate` | Validate a spec file | `toolkit validate spec.yaml` |
| `--help` | Show help information | `toolkit --help` |
| `--version` | Show version | `toolkit --version` |

#### 3. Standard Flags

- `--help, -h` - Show help
- `--version, -v` - Show version
- `--verbose` - Verbose output
- `--quiet, -q` - Quiet mode
- `--dry-run` - Preview without executing

#### 4. Exit Codes

- `0` - Success
- `1` - General error
- `2` - Invalid usage
- `127` - Command not found

#### 5. Output Format

- Use **colored output** for better UX (optional but recommended)
- Prefix errors with `Error:` or `✗`
- Prefix success with `Success:` or `✓`
- Support `--json` flag for machine-readable output (optional)

## Integration with MetaSpec

### Method 1: Auto-Discovery (Recommended)

Install your toolkit as a Python package with entry points:

```toml
# pyproject.toml
[project.entry-points."metaspec.toolkits"]
api-spec-kit = "api_spec_kit:toolkit"
```

MetaSpec will automatically discover and register your toolkit.

### Method 2: Manual Registration (Coming Soon)

```bash
metaspec spec register ./my-spec-kit
```

This will add your toolkit to `~/.metaspec/registry.yaml`.

### Method 3: Use as External Command

If your toolkit provides a CLI following the standard, MetaSpec can invoke it directly:

```bash
metaspec spec api-spec-kit init my-api.yaml
# → Executes: api-spec-kit init my-api.yaml
```

## Example: Creating a Compliant Toolkit

### 1. Generate with MetaSpec

```bash
# Create meta-spec definition
metaspec new

# Generate toolkit
metaspec init api-spec-kit.yaml
```

MetaSpec-generated toolkits are **automatically compliant** with the protocol.

### 2. Implement Protocol

```python
# src/api_spec_kit/__init__.py
from metaspec.spec_protocol import SpecToolkitProtocol

class APISpecKitToolkit:
    @property
    def name(self) -> str:
        return "api-spec-kit"
    
    @property
    def version(self) -> str:
        return "0.1.0"
    
    @property
    def description(self) -> str:
        return "Spec-driven toolkit for API testing"
    
    @property
    def commands(self) -> list[str]:
        return ["init", "validate", "generate", "run"]
    
    def execute(self, command: str, args: list[str]) -> int:
        # Route to appropriate handler
        if command == "init":
            return init_command(*args)
        elif command == "validate":
            return validate_command(*args)
        # ...

# Export toolkit instance
toolkit = APISpecKitToolkit()
```

### 3. Register as Entry Point

```toml
# pyproject.toml
[project.entry-points."metaspec.toolkits"]
api-spec-kit = "api_spec_kit:toolkit"
```

### 4. Install and Use

```bash
pip install ./api-spec-kit

# Now available through MetaSpec
metaspec spec --list
metaspec spec api-spec-kit init my-api.yaml
```

## Built-in Toolkits

MetaSpec provides built-in support for these toolkits:

### spec-kit

**Purpose**: Spec-driven development (greenfield)  
**Install**: `pip install git+https://github.com/github/spec-kit.git`  
**Usage**:
```bash
metaspec spec spec-kit init
metaspec spec spec-kit spec
metaspec spec spec-kit plan
metaspec spec spec-kit tasks
```

### openspec

**Purpose**: Spec-driven updates (brownfield)  
**Install**: `pip install git+https://github.com/Fission-AI/OpenSpec.git`  
**Usage**:
```bash
metaspec spec openspec init
metaspec spec openspec analyze
metaspec spec openspec plan
metaspec spec openspec implement
```

## FAQ

### Q: Do I have to implement the Python protocol?

**A**: No. If your toolkit provides a CLI following the standard conventions, MetaSpec can invoke it directly.

### Q: Can I use a different language?

**A**: Yes! As long as your toolkit provides a CLI that follows the protocol, it will work with MetaSpec.

### Q: How do I test protocol compliance?

**A**: We'll provide a compliance checker tool (coming soon):
```bash
metaspec spec check ./my-spec-kit
```

### Q: What if I want to add custom commands?

**A**: That's fine! The protocol defines minimum requirements. You can add any additional commands.

## Version History

- **0.1.0** (2025-01-24) - Initial draft

## Contributing

The Spec Toolkit Protocol is evolving. We welcome feedback and contributions:

- Open an issue to discuss protocol changes
- Submit PRs for clarifications or improvements
- Share your toolkit implementations as examples

---

**Related Documents**:
- [README.md](../README.md) - MetaSpec overview
- [AGENTS.md](../AGENTS.md) - AI agent guide
- [spec_protocol.py](../src/metaspec/spec_protocol.py) - Python implementation

