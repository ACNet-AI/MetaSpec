# MetaSpec Metadata in pyproject.toml

> **Purpose**: Enable community tools to discover speckit capabilities

生成的 speckit 的 `pyproject.toml` 会包含 `[tool.metaspec]` 部分，记录 **speckit 自己提供的功能和能力**。

---

## 📋 Metadata Fields

### Core Fields (Always Present)

| Field | Type | Description |
|-------|------|-------------|
| `generated_by` | string | MetaSpec version used to generate this speckit |
| `domain` | string | Domain area (e.g., "mcp", "testing", "marketing") |
| `cli_commands` | array | CLI commands this speckit provides to users |

### Optional Fields

| Field | Type | Description |
|-------|------|-------------|
| `lifecycle` | string | Development phase: "greenfield" (0→1) \| "brownfield" (1→n) \| custom |
| `sd_type` | string \| array | Slash command system type: "generic" \| "sds" \| "sdd" \| mixed |
| `slash_commands` | array | Slash commands this speckit provides for AI agents |

---

## 📝 Example Outputs

### Example 1: Domain-Specific Speckit (MCP Spec Kit)

```toml
[tool.metaspec]
generated_by = "0.9.6"
domain = "mcp"

# CLI commands this speckit provides
cli_commands = ["init", "validate", "generate", "info"]

# Custom domain-specific slash commands
sd_type = "generic"

# Slash commands for AI agents
slash_commands = ["show-spec", "get-template"]
```

**Scenario**: Domain-specific speckit with custom AI commands tailored to MCP domain

---

### Example 2: Spec-Kit Pattern Speckit (API Testing Kit)

```toml
[tool.metaspec]
generated_by = "0.9.6"
domain = "api-testing"
lifecycle = "greenfield"

# CLI commands
cli_commands = ["init", "validate", "test"]

# Uses spec-kit workflow pattern
sd_type = "sdd"

# Slash commands from library/sdd/spec-kit
slash_commands = ["specify", "plan", "implement"]
```

**Scenario**: Speckit adopts spec-kit workflow pattern for greenfield API test development

---

### Example 3: Mixed SDS + SDD (MetaSpec Itself)

```toml
[tool.metaspec]
generated_by = "0.9.6"
domain = "meta-specification"
lifecycle = "greenfield"

# CLI commands
cli_commands = ["init", "search", "install", "contribute", "list", "info"]

# Command system type (auto-detected)
sd_type = ["sds", "sdd"]

# Deployed slash commands (19 total)
slash_commands = [
    "sds.specify", "sds.plan", "sds.tasks", "sds.implement",
    "sds.clarify", "sds.analyze", "sds.checklist", "sds.constitution",
    "sdd.specify", "sdd.plan", "sdd.tasks", "sdd.implement",
    "sdd.clarify", "sdd.analyze", "sdd.checklist", "sdd.constitution",
    "proposal", "apply", "archive"
]
```

**Scenario**: MetaSpec itself - generates both specifications and toolkits

---

### Example 4: SD-Marketing (Custom Domain with Custom System)

```toml
[tool.metaspec]
generated_by = "0.9.6"
domain = "marketing"

# CLI commands for marketing operations
cli_commands = ["info", "init", "validate"]

# Custom marketing-specific command system (SDM)
sd_type = "sdm"

# SDM (Spec-Driven Marketing) commands
slash_commands = [
    "marketspec.constitution",
    "marketspec.specify",
    "marketspec.clarify",
    "marketspec.plan",
    "marketspec.tasks",
    "marketspec.implement",
    "marketspec.review",
    "marketspec.optimize",
    "marketspec.analyze",
    "marketspec.checklist",
]
```

**Scenario**: Marketing toolkit with custom SDM command system - first SD-X extension example

---

### Example 5: Mixed Pattern Speckit (API Development Kit)

```toml
[tool.metaspec]
generated_by = "0.9.6"
domain = "api"
lifecycle = "greenfield"

# CLI commands for API development
cli_commands = ["init", "validate", "generate", "test"]

# Mixed command system: custom + spec-kit
sd_type = ["generic", "sdd"]

# Mix of custom and spec-kit commands
slash_commands = ["discover", "specify", "plan", "implement", "generate"]
```

**Scenario**: API speckit combining domain-specific discovery with spec-kit workflow

---

## 🔍 Auto-Detection Rules

### `sd_type` Detection

**Purpose**: Classify the speckit's slash command system type

Based on `slash_commands[].source`:

| Source Pattern | Detected Type | Meaning |
|----------------|---------------|---------|
| `sdd/spec-kit` | `"sdd"` | Uses spec-kit workflow pattern |
| `sdd/openspec` | `"sdd"` | Uses OpenSpec evolution pattern |
| `sds/*` | `"sds"` | Uses SDS (Spec-Driven Specification) pattern |
| `generic` | `"generic"` | Custom domain-specific commands |
| Mixed sources | `["generic", "sdd"]` | Combines multiple patterns |
| No slash commands | `"none"` | No AI command system |

**Detection Logic**:
1. Collect all unique source prefixes from `slash_commands`
2. Map to types: `sdd/*` → sdd, `sds/*` → sds, `generic` → generic
3. If single type: `sd_type = "sdd"`
4. If multiple types: `sd_type = ["generic", "sdd"]`

### `lifecycle` Usage

- ✅ **Applicable**: Software development domains (API, testing, frameworks)
  - `greenfield`: Creating new features/projects (0→1)
  - `brownfield`: Evolving existing systems (1→n)

- ⚠️ **Not Applicable**: Non-development domains (marketing, design, operations)
  - Leave `lifecycle` undefined (optional field)
  - Focus on `sd_type` and `domain` instead

---

## 🎯 Community Use Cases

### Use Case 1: Discover Speckit Capabilities

```python
# Read speckit metadata
import toml

config = toml.load("pyproject.toml")
metadata = config["tool"]["metaspec"]

print(f"Domain: {metadata['domain']}")
print(f"CLI Commands: {', '.join(metadata['cli_commands'])}")
print(f"AI Command System: {metadata['sd_type']}")
print(f"Slash Commands: {len(metadata.get('slash_commands', []))}")

# Check if speckit supports specific functionality
if "validate" in metadata["cli_commands"]:
    print("✅ Supports validation")

if metadata["sd_type"] in ["sdd", ["generic", "sdd"]]:
    print("✅ Uses spec-kit workflow")
```

### Use Case 2: Search by Capabilities

```bash
# Find all speckits with 'generate' CLI command
rg 'cli_commands.*generate' **/pyproject.toml

# Find speckits using spec-kit pattern
rg 'sd_type = "sdd"' **/pyproject.toml

# Find domain-specific speckits
rg 'domain = "api"' **/pyproject.toml
```

### Use Case 3: AI Agent Compatibility Check

```python
# Check if speckit provides required slash commands for AI workflow
required_ai_commands = {"show-spec", "get-template"}
available_commands = {cmd["name"] for cmd in metadata.get("slash_commands", [])}

if required_ai_commands.issubset(available_commands):
    print("✅ Compatible with AI agent")
else:
    missing = required_ai_commands - available_commands
    print(f"⚠️  Missing commands: {missing}")
```

### Use Case 4: Build Speckit Marketplace

```python
# Aggregate speckit capabilities for marketplace display
class SpeckitEntry:
    def __init__(self, metadata):
        self.domain = metadata["domain"]
        self.cli_commands = metadata["cli_commands"]
        self.ai_enabled = metadata.get("sd_type") != "none"
        self.workflow_pattern = metadata.get("sd_type")
    
    def supports_feature(self, feature):
        return feature in self.cli_commands

# Filter speckits by capability
speckits = [SpeckitEntry(m) for m in all_metadata]
validation_kits = [s for s in speckits if s.supports_feature("validate")]
ai_enabled_kits = [s for s in speckits if s.ai_enabled]
```

---

## 📌 Design Principles

1. **Auto-Detection**: `sd_type` automatically inferred from `slash_commands`
2. **Optional Fields**: `lifecycle` only for applicable domains
3. **Community Discovery**: Standardized format for registry tools
4. **Backward Compatibility**: Minimal required fields
5. **Flexibility**: Supports mixed command systems and custom domains

---

## 🔗 Related

- [Slash Commands Library](../src/metaspec/templates/library/README.md)
- [Generator Implementation](../src/metaspec/generator.py)
- [Models Definition](../src/metaspec/models.py)

