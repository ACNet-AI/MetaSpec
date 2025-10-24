# Meta-Spec AI Agent Guide

> **For AI Assistants**: This document provides guidance on using Meta-Spec to generate Spec-Driven X (SD-X) toolkits.

---

## 🎯 Your Role

You are helping a developer create **spec-driven toolkits for AI agents** using MetaSpec. 

MetaSpec is a meta-specification framework that generates complete Spec-Driven X (SD-X) toolkits:
- **SD-Development** - AI-assisted development tools
- **SD-Design** - AI-assisted design systems
- **SD-Testing** - AI-assisted testing frameworks
- **SD-Documentation** - AI-assisted documentation tools
- **SD-Operations** - AI-assisted operations tools
- **SD-X** - Any spec-driven workflow

**Key principle**: MetaSpec generates production-ready toolkits with CLI, parser, validator, templates, and AI agent support

---

## 📋 CLI Commands

MetaSpec provides these commands:

- `metaspec init [name]` - Create toolkit (interactive or template-based)
- `metaspec spec <toolkit> <cmd>` - Use spec toolkits (unified interface)

Use these commands in your workflow to help users create and manage toolkits.

---

## 🔒 Constitutional Principles

**ALWAYS follow** `memory/constitution.md` which defines:
- Core principles for meta-spec definitions
- Quality standards for generated systems
- Prohibited patterns
- Required patterns

**Key principles:**
1. **Minimal Viable Abstraction**: Don't over-abstract
2. **AI-First Design**: Generated systems must be AI-friendly
3. **Progressive Enhancement**: Start with MVP, add features incrementally
4. **Domain Specificity**: Respect domain constraints

---

## 🤝 Integration with Spec-Kit & OpenSpec

Since generated toolkits are also projects, you can use spec-driven methodologies to develop them:

### Option 1: Generate with Spec-Kit (Recommended)

Generate a toolkit with built-in spec-driven development capabilities:

```bash
# 1. Create toolkit (interactive or template)
metaspec init                              # Interactive
# or
metaspec init my-spec-kit --template mcp --spec-kit   # Template + spec-kit

# What this does:
# - Generates complete toolkit structure
# - Calls `specify init` to create specs/ directory
# - Sets up spec.md, plan.md, tasks.md templates
```

**Prerequisites**: Install [spec-kit](https://github.com/github/spec-kit) first:
```bash
pip install git+https://github.com/github/spec-kit.git
```

**Result**: Your toolkit now has `specs/` directory for spec-driven development.

### Option 2: Add Spec-Kit Later

If you generated without `--spec-kit`, you can add it later:

```bash
cd my-spec-kit
specify init  # Manually initialize spec-kit
```

### Option 3: Use OpenSpec for Updates

**When to use**: After your toolkit is created and you need to iterate or add features.

**Important**: OpenSpec is for **brownfield** projects (existing projects), not for initial creation. Use it **inside the toolkit directory**:

```bash
cd my-spec-kit

# First time: Initialize OpenSpec
openspec init

# Then use it for updates:
openspec analyze      # Analyze current state
openspec plan         # Plan improvements
openspec implement    # Apply changes
```

**Why not integrate into `metaspec init`?**
- OpenSpec is designed for existing projects, not new projects
- You may not need OpenSpec initially
- OpenSpec should be used when toolkit needs iteration, not at creation time

### Standalone Use

MetaSpec works perfectly fine without Spec-Kit/OpenSpec for quick toolkit generation.

---

## 📝 Complete Workflow

Creating a spec-driven toolkit is more complex than building an application. Follow these steps carefully.

---

### **STEP 1: Understand Domain Requirements**

**Goal**: Research and deeply understand the target domain before designing anything.

**What AI should do:**

1. **Ask clarifying questions**:
   - What domain are we targeting? (MCP, API testing, Design systems, etc.)
   - What's the primary use case?
   - Who will use this toolkit? (Developers, designers, testers?)
   - What existing tools exist in this domain?

2. **Research the domain**:
   - Use `web_search` to find domain standards, protocols, and best practices
   - Study existing solutions (e.g., for MCP, study the MCP protocol specification)
   - Identify common patterns and workflows

3. **Identify key entities**:
   - What are the main "things" in this domain?
   - What fields/properties do these entities have?
   - What relationships exist between entities?

**Example dialogue:**

```
Human: "I need a toolkit for API testing"

AI: "Let me research API testing best practices first..."

[Performs web search on API testing, REST API testing patterns, common tools]

"Based on my research, API testing typically involves:

Key Entities:
1. APITest - Individual test case (endpoint, method, headers, body, assertions)
2. TestSuite - Collection of related tests
3. Environment - Configuration (base_url, auth credentials, variables)
4. Response - Expected response structure

Common Workflows:
- Define test spec → Validate spec → Generate test code → Execute tests

Does this align with your requirements? Any specific features you need?"
```

**Common pitfalls to avoid:**
- ❌ Skipping research and guessing domain requirements
- ❌ Designing entities before understanding the domain
- ❌ Assuming all domains work like software development

---

### **STEP 2: Design Entity Model**

**Goal**: Define the core entities and their fields based on domain research.

**What AI should do:**

1. **Start minimal** (Minimal Viable Abstraction principle):
   - 1-3 core entities maximum for MVP
   - 3-5 essential fields per entity
   - Can extend later

2. **Choose appropriate field types**:
   - `string` - Text values
   - `number` - Numeric values  
   - `boolean` - True/false flags
   - `array` - Lists of items
   - `object` - Nested structures

3. **Mark required vs optional**:
   - Only mark fields as `required: true` if absolutely necessary
   - Optional fields provide flexibility

4. **Add clear descriptions**:
   - Every field needs a description
   - Helps future developers understand the intent

**Example:**

```yaml
entity:
  name: "APITest"
  fields:
    # Required core fields
    - name: "name"
      type: "string"
      required: true
      description: "Test case name"
    
    - name: "endpoint"
      type: "string"
      required: true
      description: "API endpoint path"
    
    - name: "method"
      type: "string"
      required: true
      description: "HTTP method (GET, POST, etc.)"
    
    # Optional fields
    - name: "headers"
      type: "object"
      required: false
      description: "Custom HTTP headers"
    
    - name: "assertions"
      type: "array"
      required: false
      description: "List of response assertions"
```

**Validation checklist:**
- [ ] Entities match domain research findings
- [ ] Field names are clear and consistent
- [ ] Only essential fields are required
- [ ] Each field has a description
- [ ] No over-engineering (keep it simple)

---

### **STEP 3: Create Meta-Spec YAML**

**Goal**: Write the complete meta-spec definition file.

**What AI should do:**

**Option A: Quick Start with Scaffold (Recommended)** ⚡

Generate a pre-filled template for your domain:

```bash
metaspec scaffold generic -o toolkit.yaml  # Generic toolkit
metaspec scaffold mcp -o mcp-toolkit.yaml  # MCP domain
metaspec scaffold web -o web-toolkit.yaml  # Web development
metaspec scaffold ai -o ai-toolkit.yaml    # AI agent domain
```

Then customize the generated file based on STEP 2 entity design.

**Option B: Manual Creation**

1. **Use the template**:
   ```bash
   # Read the template first
   cat templates/meta-spec-template.yaml
   ```

2. **Fill in all required fields**:
   - `name` - Toolkit name (lowercase-with-dashes)
   - `version` - Start with "0.1.0"
   - `domain` - Choose: generic, mcp, design, testing
   - `lifecycle` - Usually "greenfield" for new toolkits
   - `description` - Clear one-line description

3. **Add entity definition** (from STEP 2)

4. **Define commands** (what the generated toolkit will do):
   ```yaml
   commands:
     - name: "init"
       description: "Initialize new spec file"
     - name: "validate"
       description: "Validate spec file"
     - name: "generate"
       description: "Generate from spec"
   ```

5. **Add dependencies**:
   ```yaml
   dependencies:
     - "pydantic>=2.0.0"    # For data validation
     - "typer>=0.9.0"        # For CLI
     - "ruamel.yaml>=0.18.0" # For YAML parsing
   ```

**Example complete meta-spec:**

```yaml
name: "api-test-kit"
version: "0.1.0"
domain: "testing"
lifecycle: "greenfield"
description: "Spec-driven toolkit for API testing"

entity:
  name: "APITest"
  fields:
    - name: "name"
      type: "string"
      required: true
      description: "Test case name"
    - name: "endpoint"
      type: "string"
      required: true
      description: "API endpoint path"
    - name: "method"
      type: "string"
      required: true
      description: "HTTP method"

commands:
  - name: "init"
    description: "Initialize new API test spec"
  - name: "validate"
    description: "Validate API test spec"
  - name: "run"
    description: "Execute API tests"

dependencies:
  - "pydantic>=2.0.0"
  - "typer>=0.9.0"
  - "requests>=2.31.0"
```

**Save to file**:
```bash
# Save as: {domain}-{name}.yaml
# Example: testing-api-test-kit.yaml
```

---

### **STEP 4: Iterative Validation**

**Goal**: Ensure the meta-spec is correct before generation.

**What AI should do:**

1. **Run validation**:
   ```bash
   metaspec validate api-test-kit.yaml
   ```

2. **Fix any errors**:
   - Read error messages carefully
   - Apply suggested fixes
   - Re-validate until clean

3. **Common validation errors**:
   
   | Error | Cause | Fix |
   |-------|-------|-----|
   | Missing required field | Forgot `name` or `version` | Add the field |
   | Invalid domain | Typo in domain name | Use: generic, mcp, design, testing |
   | Invalid field type | Wrong type specified | Use: string, number, boolean, array, object |

**Example validation session:**

```
AI: Running validation...
$ metaspec validate api-test-kit.yaml

✗ Validation failed: 2 error(s), 0 warning(s)

Error #1: Missing required field: 'version'
Suggestion: Add: version: "0.1.0"

Error #2: Invalid domain: 'api'
Suggestion: Use one of: generic, mcp, design, testing

AI: Let me fix these errors...
[Updates YAML file]

$ metaspec validate api-test-kit.yaml

✅ Validation Passed!

File: api-test-kit.yaml
Name: api-test-kit
Version: 0.1.0
Domain: testing
Entity: APITest (3 fields)
```

**Don't proceed to next step until validation passes!**

---

### **STEP 5: Preview and Review**

**Goal**: See exactly what will be generated before creating files.

**What AI should do:**

1. **Run preview**:
   ```bash
   metaspec preview api-test-kit.yaml
   ```

2. **Review the output**:
   - Check file structure
   - Verify all necessary files are included
   - Confirm entity names are correct
   - Review dependencies

3. **Show detailed preview** (if needed):
   ```bash
   # Show file sizes
   metaspec preview api-test-kit.yaml --verbose
   
   # Show content preview
   metaspec preview api-test-kit.yaml --content
   ```

**Example preview session:**

```
AI: Let me preview what will be generated...
$ metaspec preview api-test-kit.yaml

🔍 Previewing api-test-kit.yaml...

╭────────────────────────────────────────╮
│ Toolkit: api-test-kit                  │
│ Version: 0.1.0                         │
│ Domain: testing                        │
│ Entity: APITest (3 fields)             │
╰────────────────────────────────────────╯

Project Summary:
- Output: ./api-test-kit
- Files: 12
- Directories: 5
- Executable scripts: 2
- Total size: ~14KB

File Structure:
api-test-kit/
├── README.md
├── AGENTS.md
├── pyproject.toml
├── .gitignore
├── memory/
│   └── constitution.md
├── scripts/
│   ├── init.sh ⚡
│   └── validate.sh ⚡
├── templates/
│   └── spec-template.md
└── src/
    └── api_test_kit/
        ├── __init__.py
        ├── cli.py
        ├── parser.py
        └── validator.py

✓ Preview complete!

AI: "The structure looks good. Shall I proceed with generation?"
```

**Review checklist:**
- [ ] All expected files are listed
- [ ] Package name is correct (snake_case)
- [ ] Dependencies are appropriate
- [ ] AGENTS.md will be included
- [ ] Templates directory exists

---

### **STEP 6: Generate Toolkit**

**Goal**: Generate the complete toolkit with all files.

**What AI should do:**

1. **Run generation**:
   ```bash
   metaspec init api-test-kit.yaml -o ./api-test-kit
   ```

2. **Verify generation succeeded**:
   - Check output directory exists
   - Verify all files were created
   - Look for any error messages

3. **Explore generated structure**:
   ```bash
   cd api-test-kit
   ls -la
   cat README.md  # Read the generated README
   cat AGENTS.md  # Check AI instructions
   ```

4. **Initialize the toolkit** (if init script exists):
   ```bash
   ./scripts/init.sh
   # or
   chmod +x scripts/*.sh
   ./scripts/init.sh
   ```

**Example generation session:**

```
AI: Generating toolkit...
$ metaspec init api-test-kit.yaml -o ./api-test-kit

✨ Generating toolkit from api-test-kit.yaml...

Creating directories...
  ✓ api-test-kit/
  ✓ api-test-kit/memory/
  ✓ api-test-kit/scripts/
  ✓ api-test-kit/templates/
  ✓ api-test-kit/src/api_test_kit/

Generating files...
  ✓ README.md
  ✓ AGENTS.md
  ✓ pyproject.toml
  ✓ .gitignore
  ✓ memory/constitution.md
  ✓ scripts/init.sh
  ✓ scripts/validate.sh
  ✓ templates/spec-template.md
  ✓ src/api_test_kit/__init__.py
  ✓ src/api_test_kit/cli.py
  ✓ src/api_test_kit/parser.py
  ✓ src/api_test_kit/validator.py

✅ Toolkit generated successfully!

Next steps:
  cd api-test-kit
  ./scripts/init.sh
  pip install -e .

AI: "Toolkit generated! Let me verify the structure..."
$ cd api-test-kit && ls -la

[Shows directory listing]

AI: "Everything looks good. The toolkit is ready to use!"
```

---

### **STEP 7: Test and Iterate**

**Goal**: Verify the generated toolkit works correctly.

**What AI should do:**

1. **Install the toolkit**:
   ```bash
   cd api-test-kit
   pip install -e .
   # or with uv
   uv pip install -e .
   ```

2. **Test CLI commands**:
   ```bash
   # Check help
   api-test-kit --help
   
   # Try init command
   api-test-kit init test.yaml
   
   # Try validate command
   api-test-kit validate test.yaml
   ```

3. **Read generated documentation**:
   ```bash
   cat README.md
   cat AGENTS.md
   cat memory/constitution.md
   ```

4. **Test with a sample spec**:
   - Create a sample spec file
   - Validate it
   - Ensure error messages are clear

5. **Iterate if needed**:
   - If something is wrong, go back to STEP 3
   - Update meta-spec YAML
   - Re-generate with `--force` flag:
     ```bash
     metaspec init api-test-kit.yaml -o ./api-test-kit --force
     ```

**Example test session:**

```
AI: Testing the generated toolkit...

$ cd api-test-kit
$ pip install -e .
✓ Installed api-test-kit

$ api-test-kit --help
Usage: api-test-kit [OPTIONS] COMMAND [ARGS]...
...

$ api-test-kit init sample.yaml
✓ Created sample.yaml

$ cat sample.yaml
name: "sample-test"
endpoint: "/api/users"
method: "GET"
...

$ api-test-kit validate sample.yaml
✅ Validation passed!

AI: "Toolkit is working correctly! All commands function as expected."
```

**Final checklist:**
- [ ] CLI commands work
- [ ] Help messages are clear
- [ ] Validation provides good error messages
- [ ] Generated files are well-formatted
- [ ] README is helpful
- [ ] AGENTS.md has clear instructions

---

## ⚠️ Common Pitfalls

### 1. Over-Engineering Entity Model
❌ **Wrong**: Define 20+ fields with complex nested structures
```yaml
entity:
  name: "APITest"
  fields:
    - name: "advanced_config"
      type: "object"
      properties:
        retry_policy: ...
        circuit_breaker: ...
        rate_limiting: ...
        # 50 more fields...
```

✅ **Right**: Start minimal, extend later
```yaml
entity:
  name: "APITest"
  fields:
    - name: "name"
      type: "string"
      required: true
    - name: "endpoint"
      type: "string"
      required: true
    - name: "method"
      type: "string"
      required: true
```

### 2. Skipping Domain Research
❌ **Wrong**: "I know what API testing needs" (proceeds without research)

✅ **Right**: Use `web_search` to:
- Study existing API testing tools
- Understand industry standards
- Learn domain-specific patterns
- Identify common pitfalls

### 3. Not Using Preview
❌ **Wrong**: `metaspec init` directly without checking

✅ **Right**: Always preview first
```bash
metaspec preview api-test-kit.yaml
# Review output
# Then generate
metaspec init api-test-kit.yaml -o ./api-test-kit
```

### 4. Ignoring Validation Errors
❌ **Wrong**: "I'll fix it after generation"

✅ **Right**: Fix all validation errors before generation
```bash
metaspec validate api-test-kit.yaml
# Fix errors
# Validate again until clean
```

### 5. Not Testing Generated Toolkit
❌ **Wrong**: Generate and assume it works

✅ **Right**: Test every command
```bash
api-test-kit --help
api-test-kit init test.yaml
api-test-kit validate test.yaml
```

### 6. Forgetting Constitution Principles
❌ **Wrong**: Add features "because they might be useful"

✅ **Right**: Follow `memory/constitution.md`:
- Minimal Viable Abstraction
- AI-First Design
- Progressive Enhancement
- Domain Specificity

---

## 🎯 Success Criteria

A successful toolkit generation should:

- [ ] **Solves a real domain problem** - Not just a generic tool
- [ ] **Has clear entity model** - Entities match domain research
- [ ] **Follows minimal abstraction** - No over-engineering
- [ ] **Passes validation** - Clean `metaspec validate`
- [ ] **Generates cleanly** - No errors during `metaspec init`
- [ ] **CLI works** - All commands functional
- [ ] **Has good docs** - README and AGENTS.md are clear
- [ ] **Includes constitution** - memory/constitution.md exists
- [ ] **Is testable** - Can create and validate sample specs
- [ ] **Follows patterns** - Matches existing spec-driven tools

---

## 📚 Additional Resources

- **Template**: `templates/meta-spec-template.yaml`
- **Examples**: `examples/` directory
- **Constitution**: `memory/constitution.md`
- **Docs**: `docs/` directory
