# MetaSpec Metadata in pyproject.toml

> **Purpose**: Enable community tools to discover speckit capabilities

生成的 speckit 的 `pyproject.toml` 会包含 `[tool.metaspec]` 部分，记录 speckit 的元数据。

---

## 📋 Metadata Fields

### Core Fields (Always Present)

| Field | Type | Description |
|-------|------|-------------|
| `generated_by` | string | MetaSpec version used to generate this speckit |
| `domain` | string | Domain area (e.g., "mcp", "testing", "marketing") |

### Optional Fields

| Field | Type | Description |
|-------|------|-------------|
| `lifecycle` | string | Development phase: "greenfield" (0→1) \| "brownfield" (1→n) \| custom |
| `sd_type` | string \| array | Command system type(s): "generic" \| "sds" \| "sdd" \| mixed |
| `slash_commands` | array | Deployed AI slash commands |

---

## 📝 Example Outputs

### Example 1: Generic Speckit (No Slash Commands)

```toml
[tool.metaspec]
generated_by = "0.9.5"
domain = "generic"
lifecycle = "greenfield"

# No slash commands deployed
sd_type = "none"
```

**Scenario**: Simple speckit without AI commands (just CLI)

---

### Example 2: SDD Toolkit (Greenfield Development)

```toml
[tool.metaspec]
generated_by = "0.9.5"
domain = "mcp"
lifecycle = "greenfield"

# Command system type (auto-detected)
sd_type = "sdd"

# Deployed slash commands
[[tool.metaspec.slash_commands]]
name = "specify"
description = "Create feature specification"
source = "sdd/spec-kit"

[[tool.metaspec.slash_commands]]
name = "plan"
description = "Plan implementation architecture"
source = "sdd/spec-kit"

[[tool.metaspec.slash_commands]]
name = "implement"
description = "Execute implementation"
source = "sdd/spec-kit"
```

**Scenario**: Toolkit using GitHub spec-kit workflow (0→1 development)

---

### Example 3: Mixed SDS + SDD (MetaSpec Itself)

```toml
[tool.metaspec]
generated_by = "0.9.5"
domain = "meta-specification"
lifecycle = "greenfield"

# Command system type (auto-detected)
sd_type = ["sds", "sdd"]

# Deployed slash commands (19 total)
[[tool.metaspec.slash_commands]]
name = "sds.specify"
description = "Define domain specification"
source = "sds"

[[tool.metaspec.slash_commands]]
name = "sds.plan"
description = "Plan specification architecture"
source = "sds"

[[tool.metaspec.slash_commands]]
name = "sdd.specify"
description = "Define toolkit specification"
source = "sdd"

[[tool.metaspec.slash_commands]]
name = "sdd.implement"
description = "Build toolkit code"
source = "sdd"

# ... (15 more commands)
```

**Scenario**: MetaSpec itself - generates both specifications and toolkits

---

### Example 4: SD-Marketing (Custom Domain, No Lifecycle)

```toml
[tool.metaspec]
generated_by = "0.9.5"
domain = "marketing"

# Command system type (auto-detected)
sd_type = "generic"

# Deployed slash commands
[[tool.metaspec.slash_commands]]
name = "campaign.create"
description = "Create marketing campaign specification"
source = "generic"

[[tool.metaspec.slash_commands]]
name = "campaign.validate"
description = "Validate campaign against rules"
source = "generic"
```

**Scenario**: Marketing toolkit - "lifecycle" doesn't apply to this domain

---

### Example 5: Generic + SDD (Mixed Sources)

```toml
[tool.metaspec]
generated_by = "0.9.5"
domain = "api"
lifecycle = "greenfield"

# Command system type (auto-detected)
sd_type = ["generic", "sdd"]

# Deployed slash commands
[[tool.metaspec.slash_commands]]
name = "discover"
description = "Discover API structure"
source = "generic"

[[tool.metaspec.slash_commands]]
name = "specify"
description = "Define API specification"
source = "sdd/spec-kit"

[[tool.metaspec.slash_commands]]
name = "generate"
description = "Generate API client code"
source = "generic"
```

**Scenario**: API toolkit combining generic discovery with spec-kit workflow

---

## 🔍 Auto-Detection Rules

### `sd_type` Detection

Based on `slash_commands[].source`:

| Source Pattern | Detected Type |
|----------------|---------------|
| `sdd/spec-kit` | `"sdd"` |
| `sdd/openspec` | `"sdd"` |
| `sds/*` | `"sds"` |
| `generic` | `"generic"` |
| Mixed | `["sds", "sdd"]` or `["generic", "sdd"]` etc. |

### `lifecycle` Usage

- ✅ **Applicable**: Software development domains (API, testing, frameworks)
  - `greenfield`: Creating new features/projects (0→1)
  - `brownfield`: Evolving existing systems (1→n)

- ⚠️ **Not Applicable**: Non-development domains (marketing, design, operations)
  - Leave `lifecycle` undefined (optional field)
  - Focus on `sd_type` and `domain` instead

---

## 🎯 Community Use Cases

### Use Case 1: Speckit Registry

```python
# Read speckit metadata
import toml

config = toml.load("pyproject.toml")
metadata = config["tool"]["metaspec"]

print(f"Domain: {metadata['domain']}")
print(f"Command System: {metadata['sd_type']}")
print(f"Slash Commands: {len(metadata.get('slash_commands', []))}")
```

### Use Case 2: Search by Command Type

```bash
# Find all SDD toolkits
rg -A 5 'sd_type = "sdd"' **/pyproject.toml

# Find toolkits with specific commands
rg -A 10 'name = "specify"' **/pyproject.toml
```

### Use Case 3: Compatibility Check

```python
# Check if speckit has required commands
required_commands = {"specify", "plan", "implement"}
deployed = {cmd["name"] for cmd in metadata["slash_commands"]}

if required_commands.issubset(deployed):
    print("✅ Compatible")
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

