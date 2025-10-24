# MetaSpec Examples

> Meta-Spec definition examples for various domains

---

## 📚 Example List

### 1. MCP Server Development

**File**: [`mcp-spec-kit/meta.yaml`](./mcp-spec-kit/meta.yaml)

**Description**: Spec-driven toolkit for MCP (Model Context Protocol) server development

**Domain**: `mcp`

**Features**:
- MCP-specific templates and guides
- Support for tools, resources, and prompts definitions
- Includes MCP development best practices

**Generate**:
```bash
metaspec init examples/mcp-spec-kit/meta.yaml -o ./mcp-toolkit
```

**Use Case**: For AI coding assistants creating MCP servers

---

### 2. API Testing Toolkit

**File**: [`api-testing.yaml`](./api-testing.yaml)

**Description**: Toolkit for API testing spec management and automation

**Domain**: `testing`

**Features**:
- Define REST API test specs
- Support assertions and validation
- Generate test code (pytest, jest, etc.)

**Generate**:
```bash
metaspec init examples/api-testing.yaml -o ./api-test-toolkit
```

**Use Case**: QA teams standardizing API testing processes

**Sample Spec**:
```yaml
# api-test.yaml
name: "user-api-tests"
tests:
  - name: "create_user"
    endpoint: "/api/users"
    method: "POST"
    body:
      username: "testuser"
      email: "test@example.com"
    assertions:
      - status_code: 201
      - response.id: exists
      - response.username: "testuser"
```

---

### 3. Design System Management

**File**: [`design-system.yaml`](./design-system.yaml)

**Description**: Toolkit for design system spec management

**Domain**: `design`

**Features**:
- Define design component specs
- Support variants and state management
- Accessibility (A11y) checks
- Generate React/Vue/Svelte component code

**Generate**:
```bash
metaspec init examples/design-system.yaml -o ./design-toolkit
```

**Use Case**: Design teams managing design system component specs

**Sample Spec**:
```yaml
# button-component.yaml
name: "Button"
category: "atoms"
props:
  variant: ["primary", "secondary", "ghost"]
  size: ["sm", "md", "lg"]
  disabled: boolean
states:
  - hover
  - active
  - disabled
accessibility:
  role: "button"
  keyboard: ["Enter", "Space"]
```

---

### 4. Dogfooding Example

**File**: [`metaspec-dogfooding.yaml`](./metaspec-dogfooding.yaml)

**Description**: MetaSpec generating its own meta-definition (bootstrapping)

**Domain**: `generic`

**Features**:
- Demonstrates MetaSpec's self-descriptive capability
- Used for testing and validating MetaSpec itself

**Generate**:
```bash
metaspec init examples/metaspec-dogfooding.yaml -o ./metaspec-v2
```

**Use Case**: Testing MetaSpec's completeness and consistency

---

## 🎯 How to Use These Examples

### 1. Preview Examples

Before generating, preview what will be created:

```bash
metaspec preview examples/api-testing.yaml
```

### 2. Validate Examples

Ensure example definitions are valid:

```bash
metaspec validate examples/api-testing.yaml
```

### 3. Generate Toolkit

Generate a complete toolkit from an example:

```bash
metaspec init examples/api-testing.yaml -o ./my-spec-kit
```

### 4. Modify and Customize

Copy an example and modify it for your needs:

```bash
cp examples/api-testing.yaml my-custom-testing.yaml
# Edit my-custom-testing.yaml
metaspec validate my-custom-testing.yaml
metaspec init my-custom-testing.yaml -o ./my-custom-toolkit
```

---

## 📖 Example Comparison

| Example | Domain | Complexity | Use Case |
|---------|--------|------------|----------|
| **MCP Server** | mcp | ⭐⭐⭐ | AI agent MCP server development |
| **API Testing** | testing | ⭐⭐ | API automation testing |
| **Design System** | design | ⭐⭐⭐ | Design system management |
| **Dogfooding** | generic | ⭐ | Learning and testing |

---

## 🚀 Getting Started with Examples

### Recommended for Beginners

If you're using MetaSpec for the first time, try them in this order:

1. **Dogfooding Example** (Simplest)
   ```bash
   metaspec preview examples/metaspec-dogfooding.yaml
   metaspec init examples/metaspec-dogfooding.yaml -o test-toolkit
   ```

2. **API Testing** (Moderate complexity)
   ```bash
   metaspec preview examples/api-testing.yaml --verbose
   metaspec init examples/api-testing.yaml -o api-toolkit
   ```

3. **MCP Server** (Domain-specific)
   ```bash
   metaspec preview examples/mcp-spec-kit/meta.yaml --content
   metaspec init examples/mcp-spec-kit/meta.yaml -o mcp-toolkit
   ```

---

## 🛠️ Create Your Own Examples

### Basic Template

```yaml
name: "your-toolkit-name"
version: "0.1.0"
domain: "generic|mcp|design|testing"
lifecycle: "greenfield|brownfield"
description: "Brief description"

entity:
  name: "YourEntity"
  description: "Entity description"
  fields:
    - name: "field_name"
      type: "string|number|boolean|array|object"
      required: true|false
      description: "Field description"

commands:
  - name: "command-name"
    description: "Command description"
    options:
      - name: "--option"
        description: "Option description"
        default: "value"

dependencies:
  - "package>=version"
```

### Validate Your Definition

```bash
metaspec validate your-toolkit.yaml --strict
```

### Contribute Your Examples

If you create useful examples, feel free to submit a PR!

1. Create a new file in the `examples/` directory
2. Add it to this README's list
3. Ensure it passes validation: `metaspec validate examples/your-example.yaml`
4. Submit a PR

---

## 📚 More Resources

- [Quick Start](../docs/QUICKSTART.md) - 5-minute getting started guide
- [User Guide](../docs/USER_GUIDE.md) - Detailed usage documentation
- [Meta-Spec Format](../docs/METASPEC_FORMAT.md) - Definition format specification
- [Best Practices](../docs/BEST_PRACTICES.md) - Design recommendations

---

## 🤝 Contributing

We welcome new examples! Please ensure:

- ✅ Passes `metaspec validate` validation
- ✅ Includes clear description and use case explanation
- ✅ Follows naming conventions
- ✅ Added to this README

---

**Have fun building spec-driven toolkits!** 🎉
