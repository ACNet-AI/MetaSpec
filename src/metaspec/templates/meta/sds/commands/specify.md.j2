---
description: Define domain specification (SDS - Spec-Driven Specification)
---

## User Input

```text
$ARGUMENTS
```

You **MUST** consider the user input before proceeding (if not empty).

## Outline

The text the user typed after `/metaspec.sds.specify` is the **domain specification description**. 

**PURPOSE: Domain Specification (SDS)** 🎯

This command is for defining **domain specifications, rules, and standards**:
- Focus: WHAT the domain specification is
- Output: `specs/domain/001-{name}/spec.md`
- Independent of any implementation
- Pure domain specification

**NOT for toolkit implementation** - Use `/metaspec.sdd.specify` for that.

---

### 📖 Navigation Guide (Quick Reference with Line Numbers)

**🎯 AI Token Optimization**: Use `read_file` with `offset` and `limit` to read only needed sections.

**Core Flow** (Read sequentially):

| Step | Lines | Size | read_file Usage |
|------|-------|------|-----------------|
| 0. Check Context | 54-104 | 50 lines | `read_file(target_file, offset=54, limit=50)` |
| 1. Determine Spec | 105-134 | 29 lines | `read_file(target_file, offset=105, limit=29)` |
| 2. Gather Content | 135-165 | 30 lines | `read_file(target_file, offset=135, limit=30)` |
| 3. Generate Sections | 166-457 | 291 lines | See templates below ⬇️ |
| 4. Write File | 458-542 | 84 lines | `read_file(target_file, offset=458, limit=84)` |
| 5-11. Validate & Report | 543-973 | 430 lines | `read_file(target_file, offset=543, limit=430)` |

**📋 Key Templates in Step 3** (Jump to specific templates):

| Template | Lines | Size | Usage |
|----------|-------|------|-------|
| Overview & Glossary | 170-203 | 33 lines | `read_file(target_file, offset=170, limit=33)` |
| Use Cases | 204-245 | 41 lines | `read_file(target_file, offset=204, limit=41)` |
| **Entity Template** ⭐ | 252-283 | 31 lines | `read_file(target_file, offset=252, limit=31)` |
| Workflow & State | 284-359 | 75 lines | `read_file(target_file, offset=284, limit=75)` |
| **Operations** ⭐ | 366-395 | 29 lines | `read_file(target_file, offset=366, limit=29)` |
| Validation Rules | 396-415 | 19 lines | `read_file(target_file, offset=396, limit=19)` |
| Error Handling | 416-435 | 19 lines | `read_file(target_file, offset=416, limit=19)` |
| Examples | 436-457 | 21 lines | `read_file(target_file, offset=436, limit=21)` |

**💡 Typical Usage Patterns**:
```python
# Quick start: Read only Steps 0-2 (109 lines)
read_file(target_file, offset=54, limit=111)

# Just templates: Read Step 3 only (291 lines)
read_file(target_file, offset=166, limit=291)

# Just Entity template: Read specific template (31 lines)
read_file(target_file, offset=252, limit=31)
```

**Token Savings**: Reading specific sections saves 70-90% tokens vs reading full file (1039 lines).

---

Follow this execution flow:

### 0. Check Invocation Context (NEW - Critical for Recursive Structure)

**Determine if this is**:
- **Direct invocation**: User called `/metaspec.sds.specify` directly
- **From implement**: Called by `/metaspec.sds.implement` internally

**How to detect**:

Check for environment variables or context passed by implement:
- `$PARENT_SPEC_ID` - Parent specification ID (if called by implement)
- `$ROOT_SPEC_ID` - Root specification ID (if called by implement)
- `$SPEC_NUMBER` - Assigned specification number (if called by implement)

**Implementation Note for AI**:

When implement calls specify "internally", context is passed through the conversation:
- implement extracts context from task (parent, root, number)
- implement **mentions these values** when invoking specify
- specify reads context from the conversation flow
- No actual environment variables needed in AI context

**If from implement** (has parent context):
```bash
# Context provided by implement
PARENT_SPEC_ID="003-payment-processing"
ROOT_SPEC_ID="001-order-spec"
SPEC_NUMBER="013"

# This means:
# - We're creating a sub-specification of 003
# - The root is 001
# - Use number 013 (don't auto-find)
```

**If direct invocation** (no parent):
```bash
# No context variables set
# This means:
# - We're creating a root or independent specification
# - Need to find next available number
# - parent: null, root: self
```

**Store context for later steps**:
- `is_sub_specification`: true | false
- `parent_id`: {parent-id} or null
- `root_id`: {root-id} or {self-id}
- `assigned_number`: {number} or null

---

### 1. Determine Specification and Load Existing Specification

**Step 1a: Generate Specification Name**

Based on user input, generate:
- Short name: `{domain}-{component}-spec`
- Example: "mcp-core-spec", "graphql-schema", "oauth2-flow"
- Check existing `specs/domain/` directory structure

**Step 1b: Determine Specification Number**

**If `assigned_number` is set** (from implement context):
```bash
# Use the number provided by implement
specification_number=$SPEC_NUMBER  # e.g., "013"
```

**If `assigned_number` is NOT set** (direct invocation):
```bash
# Find next available number
ls specs/domain/ | grep -E '^[0-9]{3}-' | sort -n
# Find next number (e.g., if 001, 002 exist, use 003)
```

**Step 1c: Load Existing or Create New**

- Check for `specs/domain/{number}-{name}/spec.md`
- If exists, load for updating
- If new, create new directory structure

### 2. Gather Domain Specification Content

**Focus**: Define the domain specification, entities, schemas, and validation rules.

**Critical Questions**:

1. **Specification Name**: What is this specification called?
   - Example: "MCP (Model Context Specification)"
   
2. **Specification Purpose**: What problem does this specification solve?
   - Example: "Enable AI models to interact with external tools and resources"
   
3. **Core Entities**: What are the main entities in this specification?
   - Example: Server, Tool, Resource, Prompt
   
4. **Entity Schemas**: What fields/properties does each entity have?
   - Example: Tool has `name`, `description`, `inputSchema`
   
5. **Validation Rules**: What are the constraints and requirements?
   - Example: "Tool name must be unique", "inputSchema must be valid JSON Schema"

6. **Specification Operations**: What operations/interfaces does the specification define?
   - **⚠️ IMPORTANT**: This is for API/Protocol specifications that define interfaces
   - **Example (API Spec)**: `initialize`, `tools/list`, `tools/call` (MCP protocol operations)
   - **Example (REST API)**: `GET /users`, `POST /orders` (HTTP endpoints)
   - **⚠️ NOT for**: Toolkit commands like `/domain.entity` - those belong in SDD!
   
   **When to define Specification Operations**:
   - ✅ Your domain IS an API/Protocol specification (MCP, REST API, GraphQL)
   - ✅ You're defining interfaces that implementers must follow
   - ✅ These are specification-level operations, not toolkit commands
   
   **When NOT to define**:
   - ❌ Your domain is NOT an API specification (Marketing, E-commerce, CRM)
   - ❌ You want to define toolkit commands (use `/metaspec.sdd.specify` instead)
   - ❌ You're confused - if unsure, leave empty and define commands in SDD
   
   **Key distinction**:
   - **Specification Operations** (SDS) = Interfaces the specification defines (e.g., API endpoints)
   - **Toolkit Commands** (SDD) = Commands your toolkit provides (e.g., `/domainspec.discover`)
   - These are completely different! Most domains don't need Specification Operations.

**Important Notes**:
- This is SDS (Spec-Driven Specification) - focus on specification definition only
- Do NOT include implementation details (Parser, Validator, CLI)
- Do NOT define toolkit commands here - use `/metaspec.sdd.specify` for that
- For toolkit development, use `/metaspec.sdd.specify` instead

**If user input is vague**, make informed guesses based on domain standards and document assumptions.

### 3. Generate Domain Specification Content

Generate **Domain Specification** with these sections:

#### **Specification Overview**
- Specification name and version
- Problem it solves
- Core capabilities
- Example: "MCP (Model Context Specification) v1.0 enables standardized communication between AI models and external tools/resources."

#### **Glossary** (Optional but Recommended)

Define key terms used in the specification to help all audiences understand:

**Template**:
```markdown
## Glossary

- **{Term 1}**: {Clear, concise definition}
  - Example: "Tool: A callable function exposed by the server that can be invoked by AI agents"
  
- **{Term 2}**: {Clear, concise definition}
  - Example: "Resource: A data source or file that can be accessed through the specification"
  
- **{Term 3}**: {Clear, concise definition}
```

**When to include**:
- Specification contains domain-specific terminology
- Audience includes non-technical stakeholders
- Terms might be ambiguous or have multiple meanings

**Best practices**:
- Keep definitions concise (1-2 sentences)
- Provide examples where helpful
- Focus on specification-specific meanings
- Avoid overly technical jargon in definitions

#### **Use Cases** (Optional but Recommended)

Describe real-world scenarios where this specification applies:

**Template**:
```markdown
## Use Cases

### Use Case 1: {Scenario Name}

**Scenario**: {Brief description of the situation}

**Actors**: {Who/what is involved}
- Actor 1: {Role}
- Actor 2: {Role}

**Flow**:
1. {Step 1}
2. {Step 2}
3. {Step 3}

**Specification Elements Used**:
- {Entity or Operation 1}
- {Entity or Operation 2}

**Outcome**: {Expected result}

### Use Case 2: {Another Scenario}
...
```

**When to include**:
- Specification purpose might not be immediately clear
- Need to demonstrate practical value
- Want to guide implementation priorities

**Best practices**:
- Provide 2-4 concrete use cases
- Cover common scenarios
- Show how entities and operations work together
- Keep scenarios realistic and relatable

#### **Core Entities**

Define specification entities (NOT toolkit entities):

**Template**:
```markdown
### Entity: {EntityName}

**Purpose**: {What this entity represents in the specification}

**Schema**:
```yaml
entity_name:
  field1:
    type: string
    required: true
    description: {field description}
  field2:
    type: number
    required: false
    description: {field description}
```

**Validation Rules**:
- {Rule 1}
- {Rule 2}

**Example**:
```json
{
  "field1": "example value",
  "field2": 42
}
```
\```

**Repeat for each entity**.

#### **Workflow** (Optional but Recommended for Stateful Specifications)

Define state machines and transition rules for entities with lifecycle:

**When to include**:
- Specification involves state management (e.g., Order, Session, Device)
- Entities have lifecycle or status changes
- Operations have sequential dependencies
- Need to define allowed/forbidden transitions

**Template**:
```markdown
## Workflow

### State Machine: {Entity Name}

**States**:
- `{state_1}`: {State description}
  - Example: `pending`: Order received, awaiting confirmation
- `{state_2}`: {State description}
  - Example: `confirmed`: Order confirmed, preparing for shipment
- `{state_3}`: {State description}

**Initial State**: `{initial_state}`
**Final States**: `{final_state_1}`, `{final_state_2}`

**Allowed Transitions**:

#### `{state_1}` → `{state_2}`
- **Trigger**: {What causes this transition}
- **Precondition**: {What must be true before transition}
- **Action**: {What happens during transition}
- **Postcondition**: {What must be true after transition}

Example:
#### `pending` → `confirmed`
- **Trigger**: Admin confirms order
- **Precondition**: Payment verified, inventory available
- **Action**: Reserve inventory, send confirmation email
- **Postcondition**: Order status is `confirmed`, inventory reserved

**Forbidden Transitions**:
- ❌ `{state_x}` → `{state_y}`: {Reason why this is forbidden}
  - Example: `confirmed` → `pending`: Cannot un-confirm an order
- ❌ `{state_z}` → `{state_w}`: {Reason}

**Validation Rules**:
1. All transitions must follow allowed paths
2. Preconditions must be satisfied before transition
3. State must be explicitly set (no implicit transitions)
4. {Additional validation rules}

**State Diagram** (Optional):
```mermaid
stateDiagram-v2
    [*] --> state_1
    state_1 --> state_2
    state_2 --> state_3
    state_1 --> cancelled
    state_3 --> [*]
```
\```

**Note**: 
- Multiple entities can have their own state machines
- Define one state machine per entity that has lifecycle
- Focus on specification-level states (WHAT), not implementation details (HOW)
\```

**Best practices**:
- Keep states minimal (3-7 states is typical)
- Clearly define preconditions and postconditions
- Document why certain transitions are forbidden
- Use clear, business-meaningful state names
- Consider using state diagrams for complex workflows

#### **Specification Operations**

Define operations/interfaces:

**Template**:
```markdown
### Operation: {operation_name}

**Purpose**: {What this operation does}

**Request Schema**:
```yaml
operation_name_request:
  param1:
    type: string
    required: true
  param2:
    type: object
    required: false
```

**Response Schema**:
```yaml
operation_name_response:
  result:
    type: string
  error:
    type: string
    required: false
```

**Validation Rules**:
- {Rule 1}
- {Rule 2}
\```

#### **Validation Rules Summary**

Comprehensive list of all specification constraints:

```markdown
## Validation Rules

### Entity Validation
1. {Entity 1}: {validation rules}
2. {Entity 2}: {validation rules}

### Operation Validation
1. {Operation 1}: {validation rules}
2. {Operation 2}: {validation rules}

### Cross-Entity Validation
1. {Rule 1}
2. {Rule 2}
```

#### **Error Handling**

Define specification-level error handling:

```markdown
## Error Handling

### Error Codes
- `E001`: {Error description}
- `E002`: {Error description}

### Error Response Format
```yaml
error_response:
  code: string
  message: string
  details: object (optional)
```
\```

#### **Examples**

Provide complete specification examples:

```markdown
## Specification Examples

### Example 1: {Scenario Name}

**Request**:
```json
{specification request example}
```

**Response**:
```json
{specification response example}
```

**Validation**: All rules pass ✅
\```

### 4. Write Specification File

**Location**: `specs/domain/{number}-{name}/spec.md`

**IMPORTANT**: Add YAML frontmatter for recursive structure tracking

**Step 4a: Generate Frontmatter and Header**

Based on context from Step 0, generate spec.md with:

**1. YAML Frontmatter**:

- **If direct invocation** (root specification):
  ```yaml
  ---
  spec_id: {number}-{name}
  parent: null
  root: {number}-{name}
  type: root
  ---
  ```

- **If from implement** (sub-specification):
  ```yaml
  ---
  spec_id: {number}-{name}
  parent: {parent_id}
  root: {root_id}
  type: leaf
  ---
  ```

**2. Header with Parent Chain** (if sub-specification):

- **If direct invocation** (root):
  ```markdown
  # {Specification Name}
  
  **Type**: Root Specification
  **Version**: 1.0.0
  ```

- **If from implement** (sub-specification):
  ```markdown
  # {Specification Name}
  
  **Parent chain**: [{root_name}](../{root_id}/spec.md) > [{parent_name}](../{parent_id}/spec.md) > {current_id}
  
  **Type**: Leaf Specification (complete specification)
  **Version**: 1.0.0
  ```

**Step 4b: Populate Template**

**Use template**: `meta/templates/domain-spec-template.md.j2`

Populate the template with the following variables:

- `metadata`
  - `name`: Specification name (e.g., "MCP Core Specification")
  - `version`: Semantic version (start with `1.0.0`)
  - `status`: Draft | Stable | Deprecated
  - `created`: ISO date (`{{ today }}`)
  - `summary`: 3-5 sentence overview (from Step 3)
- `glossary`: List of `{ term, definition, example }` (optional)
- `use_cases`: List of use case dictionaries (name, scenario, actors, flow, elements, outcome)
- `entities`: For each specification entity collected in Step 3:
  - `name`, `purpose`
  - `fields`: `[{ name, type, required, description, constraints }]`
  - `schema_example`: YAML snippet (optional)
  - `validation`: Bullet list of entity-specific rules
  - `examples`: JSON examples (optional)
- `workflows`: State machines (if applicable) with `states`, `transitions`, `forbidden`, `validation`
- `operations`: Specification operations/interfaces with request/response schemas
- `validation_rules`: Flat list of cross-cutting rules (`id`, `description`, `type`, `target`, `scope`, `details`)
- `error_handling`: `{ codes: [...], format: yaml_snippet }` (optional)
- `examples`: End-to-end examples (request/response pairs)
- `references`: External resources or related specifications

The template automatically renders:
- YAML frontmatter (spec_type, `entities`, `operations`, `validation_rules`, etc.) for machine-readable specs
- Markdown body (Overview, Entities, Workflow, Operations, Validation, Examples) for human-readable docs

✅ Ensure all required sections are populated. Optional sections (Glossary, Use Cases, Workflow, Error Handling) can be omitted if not applicable—the template handles empty lists gracefully.

### 5. Generate Detailed Impact Report (NEW)

**Purpose**: Create comprehensive change tracking and impact analysis.

**Step 5a: Prepare Report Content**

Collect information for the report:

```markdown
Report Data:
- Spec ID: {spec_id}
- Version: {version} (1.0.0 for new, increment for updates)
- Date: {today}
- Type: New | Update
- Entity Count: {count of entities}
- Operation Count: {count of operations}
- Validation Rules: {count of rules}
- Workflow States: {count if workflow exists, else 0}
```

**Step 5b: Generate HTML Comment**

Create compact report and **prepend** to spec.md:

```html
<!--
Domain Specification Report
===========================
Spec: {spec_id} v{version} | {New | Update}
Date: {ISO_DATE}

Summary:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Entities: {count} | Operations: {count} | Rules: {count}
Status: {Draft | Stable}

Impact:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Created: specs/domain/{spec_id}/spec.md
Review: README.md, AGENTS.md{IF dependencies}, related specs{END}

Constitution: {✅ Compliant | ⚠️ Check: {issues}}

Next: {IF complex}Plan sub-specs, {END}{IF toolkit}Create toolkit, {END}Run analyze

Generated by: /metaspec.sds.specify
-->
```

**Step 5c: Write Order**

When writing spec.md:
1. **First**: Prepend HTML comment (Impact Report)
2. **Then**: Write YAML frontmatter
3. **Then**: Write specification content (from template)

### 6. Consistency Propagation and Impact Analysis (NEW)

**Purpose**: Identify affected files and potential conflicts.

After writing spec.md, systematically check related files:

#### A. Other Domain Specifications

**Check for conflicts**:

```bash
# List all other domain specifications
ls specs/domain/ | grep -E '^[0-9]{3}-' | grep -v {current_spec_id}

# For each existing spec, check:
# 1. Entity name conflicts
# 2. Operation name conflicts  
# 3. Validation rule inconsistencies
# 4. Overlapping use cases
```

**Actions**:
- **Read**: Each spec's entity and operation names
- **Compare**: Against new specification's entities/operations
- **Note**: Any naming conflicts or semantic overlaps
- **Mark**: Specifications requiring manual review

**Example Check**:
```markdown
Checking specs/domain/001-mcp-core-spec/spec.md...
- Entities: Server, Tool, Resource
- Operations: initialize, tools/list, tools/call
- ✅ No conflicts with new spec

Checking specs/domain/002-auth-spec/spec.md...
- Entities: User, Token, Session
- ⚠️  WARNING: "Session" entity also exists in new spec
- → Manual review needed: Check if same concept or different
```

#### B. Toolkit Specifications (If Any Exist)

**Check toolkit dependencies**:

```bash
# Find toolkits that depend on this or related specs
grep -r "Depends on.*domain" specs/toolkit/*/spec.md

# For each dependent toolkit:
# - Does it reference entities from this spec?
# - Do validation rules affect toolkit implementation?
# - Should toolkit be updated?
```

**Actions**:
- **Read**: Toolkit Dependencies sections
- **Check**: If toolkit depends on this specification
- **Note**: Toolkits that may need updates
- **Mark**: For manual review after specification stabilizes

**Example Check**:
```markdown
Checking specs/toolkit/001-mcp-parser/spec.md...
- Depends on: domain/001-mcp-core-spec
- ✅ No direct impact (different spec)

Checking specs/toolkit/002-auth-validator/spec.md...
- Depends on: domain/002-auth-spec
- ⚠️  IMPACT: New "Session" entity may require toolkit updates
- → Manual review needed
```

#### C. MetaSpec Commands (If Custom Commands Exist)

**Check custom slash commands**:

```bash
# Check if any custom commands reference this spec
find .metaspec/commands/ -name "*.md" -exec grep -l "{spec_id}" {} \;

# For each command:
# - Does it embed specification knowledge?
# - Does it reference entities or operations?
# - Should command be updated?
```

**Actions**:
- **Read**: Custom command files
- **Check**: Embedded specification references
- **Note**: Commands needing updates
- **Mark**: For regeneration if needed

#### D. Project Documentation

**Check documentation files**:

```bash
# Files to review
- README.md: Specification list
- AGENTS.md: Specification documentation
- CHANGELOG.md: Record specification addition
- docs/*.md: Any specification guides
```

**Actions**:
- **Read**: Current documentation
- **Check**: If specification is listed/documented
- **Note**: Missing documentation
- **Update**: Add to Impact Report

**Example**:
```markdown
Checking README.md...
- ⚠️  New specification not listed
- → Action: Add to "Specifications" section

Checking AGENTS.md...
- ⚠️  Specification purpose not documented
- → Action: Add to "Domain Specifications" section
```

#### E. Example Specifications (If Examples Directory Exists)

**Check example files**:

```bash
# If examples/ directory exists
ls examples/

# For each example:
# - Does it reference similar entities?
# - Should a new example be created?
# - Are existing examples still valid?
```

**Actions**:
- **Read**: Existing examples
- **Check**: Relevance to new specification
- **Note**: Need for new examples
- **Mark**: Examples to update

### 7. Validation Checklist (NEW)

**Purpose**: Ensure specification quality before finalizing.

Run these critical validation checks:

- [ ] **Structure**: YAML frontmatter + required sections (Overview, Entities, Validation, Examples)
- [ ] **Entities**: Complete definitions with types, validation rules, and examples
- [ ] **Operations**: Request/response schemas defined (if applicable)
- [ ] **Validation Rules**: Comprehensive, testable, covering entities and operations
- [ ] **Constitution Compliance**: Entity Clarity, Validation Completeness, Implementation Neutrality, Domain Fidelity
- [ ] **Cross-References**: Dependencies listed, no conflicts with other specs
- [ ] **Impact Report**: Prepended at top of spec.md
- [ ] **File Path**: specs/domain/{spec_id}/spec.md

### 8. Generate Validation Report

**Output validation results**:

```markdown
Validation Report
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Structure Validation: ✅ PASSED (4/4 checks)
- YAML frontmatter: ✅
- Header section: ✅  
- Required sections: ✅
- File organization: ✅

Content Validation: ✅ PASSED (5/5 checks)
- Entity definitions: ✅ (3 entities, all complete)
- Operation definitions: ✅ (5 operations defined)
- Validation rules: ✅ (12 rules specified)
- Examples: ✅ (All entities have examples)
- Optional sections: ✅ (Glossary, Use Cases included)

Constitution Compliance: ✅ PASSED (7/7 principles)
- Entity Clarity: ✅
- Validation Completeness: ✅
- Operation Semantics: ✅
- Implementation Neutrality: ✅
- Extensibility Design: ✅
- Domain Fidelity: ✅
- Minimal Abstraction: ✅

Documentation Quality: ✅ PASSED (5/5 checks)
- Clarity: ✅
- Completeness: ✅
- Consistency: ✅
- Correctness: ✅
- Accessibility: ✅

Cross-Reference Validation: ✅ PASSED (3/3 checks)
- Dependencies: ✅ (All referenced specs exist)
- No conflicts: ✅ (Checked against 2 other specs)
- Consistent terminology: ✅

Overall Score: 24/24 (100%) ✅

{IF any warnings or suggestions}:
⚠️  Warnings:
- {Warning 1}
- {Warning 2}

💡 Suggestions:
- {Suggestion 1}: {Rationale}
- {Suggestion 2}: {Rationale}
```

### 9. Update Success Output

Update the success output to include validation and impact information:

### 10. Create README.md (Optional)

If this is a new specification spec, create `specs/domain/{number}-{name}/README.md`:

```markdown
# {Specification Name}

Brief overview of the specification.

## Files

- `spec.md` - Complete domain specification
- `schema.{format}` - Schema files (if applicable)

## Status

**Current Status**: {Draft | Stable | Deprecated}

## Quick Start

{How to read and use this domain specification}
```

### 6. Update Dependencies (If needed)

If this specification depends on other specifications, document in spec.md:

```markdown
## Dependencies

- **domain/001-base-spec** - Core specification definitions
- **domain/002-auth-spec** - Authentication mechanisms
```

### 11. Success Output (Enhanced)

**Provide comprehensive summary with validation and impact results**:

```
✅ Domain specification created/updated successfully

📁 Location:
   specs/domain/{number}-{name}/spec.md

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

📋 Specification Summary:
   Name: {Specification Name}
   Version: {version}
   Status: {Draft | Stable | Deprecated}
   Type: {Root | Leaf} Specification
   {IF leaf: Parent: {parent_id}}

📊 Content Statistics:
   - Core Entities: {count} entities defined
     * {Entity 1}
     * {Entity 2}
     * ...
   
   - Specification Operations: {count} API/protocol operations defined
     * {Operation 1} (e.g., API endpoint, protocol message)
     * {Operation 2}
     * ...
     ⚠️ Note: Only for API/Protocol specs (MCP, REST API). Most domains leave this empty.
            Toolkit commands should be defined in SDD, not here!
   
   - Validation Rules: {count} rules specified
     * Entity validation: {count} rules
     * Operation validation: {count} rules
     * Cross-entity validation: {count} rules
   
   {IF workflow exists}:
   - Workflow: {count} state machine(s)
     * {Entity 1} State Machine: {state_count} states, {transition_count} transitions
     * ...
   
   {IF glossary included}:
   - Glossary: {count} terms defined
   
   {IF use cases included}:
   - Use Cases: {count} scenarios documented

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

✅ Validation Results: PASSED ({score}/24 checks)

   Structure: ✅ {4/4 checks passed}
   Content: ✅ {5/5 checks passed}
   Constitution: ✅ {7/7 principles compliant}
   Documentation: ✅ {5/5 checks passed}
   Cross-References: ✅ {3/3 checks passed}

{IF any warnings}:
   ⚠️  Warnings:
   - {Warning 1}
   - {Warning 2}

{IF any suggestions}:
   💡 Suggestions:
   - {Suggestion 1}
   - {Suggestion 2}

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

📋 Impact Analysis:

   ✅ Files Created/Updated:
   - specs/domain/{spec_id}/spec.md

   ⚠️  Files Requiring Manual Review:
   - README.md (add specification to list)
   - AGENTS.md (document specification purpose)
   {IF conflicts detected}:
   - specs/domain/{conflicting_spec}/spec.md (naming conflict detected)
   {IF toolkits affected}:
   - specs/toolkit/{affected_toolkit}/spec.md (may need updates)

   📊 Consistency Check:
   - Domain specifications reviewed: {count}
   - Conflicts detected: {count}
   - Toolkits potentially affected: {count}
   - Documentation needing updates: {count} files

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

🔄 Next Steps:

   Immediate:
   1. Review specification completeness
   2. Update README.md with new specification
   3. Update AGENTS.md with specification documentation
   {IF conflicts}:
   4. ⚠️  Resolve naming conflicts with other specs
   {IF toolkits affected}:
   5. ⚠️  Review and update affected toolkits

   Recommended:
   - Run /metaspec.sds.analyze to check full consistency
   {IF complex}:
   - Consider /metaspec.sds.plan for sub-specifications
   {IF needs toolkit}:
   - Create toolkit with /metaspec.sdd.specify

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

💡 Suggested commit message:
   {IF new}:
   docs(spec): add {spec_id} domain specification
   
   - Define {count} core entities
   - Specify {count} operations
   - Include {count} validation rules
   {IF workflow}:
   - Document {count} workflow state machine(s)
   
   {IF update}:
   docs(spec): update {spec_id} domain specification
   
   - {summary of changes}
```

## Best Practices

### Domain Specification Focus

✅ **DO**:
- Define WHAT the specification is
- Specify entities, schemas, validation rules
- Define operations and interfaces
- Keep implementation-agnostic
- Use standard data formats (JSON Schema, YAML)

❌ **DON'T**:
- Include implementation code
- Specify Parser/Validator details
- Define CLI commands
- Mix specification and toolkit concerns

### Naming Conventions

- **Specification names**: `{domain}-{component}-spec`
- **Entity names**: PascalCase (e.g., `ServerInfo`, `ToolDefinition`)
- **Operations**: snake_case (e.g., `tools/list`, `initialize`)
- **Fields**: camelCase (e.g., `userName`, `isActive`)

### Version Control

- Start with v1.0 for new specifications
- Use semantic versioning
- Document breaking changes
- Mark deprecated fields clearly

### Documentation

- Provide clear examples
- Explain validation rules rationale
- Link to related standards
- Include common pitfalls

## Constitution Check

Before finalizing, verify against `memory/constitution.md`:

```bash
# Check specification spec against constitution
grep -A 5 "Entity Clarity" memory/constitution.md
grep -A 5 "Minimal Viable Abstraction" memory/constitution.md
```

**Ensure**:
- Specification entities are minimal and clear
- No over-engineering
- Progressive enhancement is possible
- Domain specificity is maintained

## Troubleshooting

**If specification seems too complex**:
→ Break into multiple specification specs (e.g., core + extensions)

**If overlapping with toolkit**:
→ Move implementation concerns to `specs/toolkit/` using `/metaspec.sdd.specify`

**If unclear validation rules**:
→ Use `/metaspec.sds.clarify` to resolve ambiguities

**If specification dependencies are complex**:
→ Document in `Dependencies` section and consider using `/metaspec.sds.analyze`
