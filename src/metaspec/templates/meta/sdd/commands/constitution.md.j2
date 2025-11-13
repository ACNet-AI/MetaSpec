---
description: Create or update the speckit constitution defining design principles for spec-driven toolkit development
---

## User Input

```text
$ARGUMENTS
```

You **MUST** consider the user input before proceeding (if not empty).

## Outline

You are updating **Part III: Toolkit Implementation Principles** in `/memory/constitution.md`. This section defines guidelines for building the toolkit (parser, validator, CLI, generator).

Unlike specification design principles (Part II), Part III focuses on **implementation quality** - it guides decisions about entity models, validator architecture, CLI design, and code organization.

Follow this execution flow:

### 1. Load existing constitution

- Read `/memory/constitution.md`
- Locate `## Part III: Toolkit Implementation Principles` section
- Preserve Part I and Part II unchanged

### 2. Understand the toolkit implementation

**Critical**: Before updating principles, understand what this toolkit implements:
- What specifications does it process? (Marketing campaigns, MCP servers, API tests?)
- What components are needed? (Parser, Validator, CLI, Generator?)
- What technology stack? (Python/TypeScript, Pydantic/Zod, Typer/Commander?)
- What workflows? (init → validate → generate → execute?)

**Ask clarifying questions if unclear**:
- "What technology stack is used?"
- "What components does the toolkit have?"
- "What is the typical user workflow?"

### 3. Update Part III principles

Based on user input and implementation understanding, update these **standard toolkit implementation principles** in Part III:

#### **I. Entity-First Design**
- Start with minimal viable entity definition (3-5 core fields)
- All fields must have clear descriptions and types
- Required fields only for truly essential data
- Support progressive enhancement (add fields later)

**Rationale**: Simple entities are easier for AI agents to understand and validate.

#### **II. Validator Extensibility**
- Core validator handles structure validation (JSON Schema, Pydantic)
- Support custom validation rules via plugins or hooks
- Clear error messages with field path and fix suggestions
- Validation must be fast (<100ms for typical specs)

**Rationale**: Different domains need different validation logic; extensibility is key.

#### **III. Spec-First Development**
- Users write specifications first, then toolkit processes them
- Specifications are declarative (what, not how)
- Specifications are human-readable (YAML/JSON/Markdown)
- Specifications are version-controlled

**Rationale**: Spec-first enables AI agents to generate and validate specifications.

#### **IV. AI-Agent Friendly**
- Clear error messages: "Field 'endpoint' is required in APITest entity"
- Examples in documentation and templates
- Consistent naming conventions (snake_case, kebab-case)
- Avoid implicit behavior (explicit is better)

**Rationale**: AI agents need clear feedback to correct mistakes and learn patterns.

#### **V. Progressive Enhancement**
- Ship MVP first (init + validate commands)
- Add features incrementally (generate, execute, report)
- Maintain backward compatibility (semantic versioning)
- Document feature maturity (alpha, beta, stable)

**Rationale**: Start simple, grow based on user feedback.

#### **VI. Domain Specificity**
- Respect domain constraints and conventions
- Research domain standards before designing entities
- Don't over-generalize (toolkit serves one domain well)
- Include domain-specific validation (e.g., HTTP methods for API tests)

**Rationale**: Generic toolkits are weak toolkits; domain focus creates value.

### 4. Prepare implementation-specific examples

For each principle in Part III, provide implementation-specific examples:

- **Entity-First Design**: What models? What libraries? Field count?
- **Validator Extensibility**: Plugin system? Custom rules? Error format?
- **Spec-First Development**: Input formats? Declarative style?
- **AI-Agent Friendly**: Error messages? Naming conventions?
- **Progressive Enhancement**: MVP scope? Feature roadmap?
- **Automated Quality**: Test strategy? CI/CD setup?

**Examples by tech stack**:
- Python: Pydantic models, @validator decorators, Typer CLI
- TypeScript: Zod schemas, Commander CLI, Jest tests
- Go: struct tags, cobra CLI, testify
- Rust: serde, clap CLI, cargo test

### 5. Update Part III section

Update only the `## Part III: Toolkit Implementation Principles` section with implementation-specific content:

```markdown
## Part III: Toolkit Implementation Principles

**Purpose**: Guidelines for building the toolkit (parser, validator, CLI, generator)

### 1. Entity-First Design

[Implementation approach: Pydantic/Zod/struct, field count, validation]

### 2. Validator Extensibility

[Plugin system, custom rules, error format]

### 3. Spec-First Development

[Input formats, declarative style, generation approach]

### 4. AI-Agent Friendly

[Error messages, naming conventions, documentation]

### 5. Progressive Enhancement

[MVP scope, feature roadmap, versioning]

### 6. Automated Quality

[Testing strategy, CI/CD, coverage targets]

<!-- Managed by /metaspec.sdd.constitution -->
```

**CRITICAL**: Only update Part III. Preserve Part I and Part II exactly as they are.

### 6. Consistency propagation and impact analysis

Check and update dependent files to align with updated principles:

#### A. Toolkit Specifications
- **Read** `specs/toolkit/001-*/spec.md` (if exists)
- **Check** tech stack matches Entity-First principle
- **Check** validator design matches Validator Extensibility principle
- **Check** CLI design follows AI-Agent Friendly principle
- **Note** any inconsistencies

#### B. MetaSpec Commands
- **Read** `/.metaspec/commands/sdd.specify.md` (if exists)
- **Check** if principles are referenced in guidance
- **Update** if principle names or descriptions changed
- **Mark** with `<!-- Updated per constitution v{VERSION} -->`

#### C. Toolkit Templates
- **Read** `/src/metaspec/templates/meta/templates/spec-template.md.j2` (if exists)
- **Check** template structure matches required principles
- **Check** mandatory sections align with Entity-First and Spec-First principles
- **Update** if new principles require new sections

#### D. Source Code Structure
- **Read** `src/` directory structure (if exists)
- **Check** if code organization follows Entity-First Design
- **Check** if validation logic follows Validator Extensibility
- **Check** if CLI follows AI-Agent Friendly patterns
- **Note** code that may need refactoring

#### E. Project Documentation
- **Read** `/README.md`
- **Check** "Architecture" or "Implementation" sections
- **Update** if principles changed
- **Read** `/AGENTS.md`
- **Check** Part III references in Constitutional Principles section
- **Update** if principle names changed

#### F. Test Files
- **Read** `tests/` directory (if exists)
- **Check** if tests follow Automated Quality principle
- **Note** test coverage gaps

**Track all changes**:
- ✅ Updated: List files successfully updated
- ⚠️ Needs manual review: List files requiring human attention
- 📝 Recommendations: Suggest code/architecture improvements

### 7. Generate detailed Sync Impact Report

Prepend this as an HTML comment at the top of `/memory/constitution.md`:

```html
<!--
Constitution Part III Update Report
====================================
Version: {OLD_VERSION} → {NEW_VERSION} ({BUMP_TYPE})
Updated: {ISO_DATE}
Rationale: {Brief reason for update}

Key Changes:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
{IF modified}: • Modified: {PRINCIPLE_NAME} - {brief change}
{IF added}: • Added: {NEW_PRINCIPLE_NAME} - {brief description}
{IF removed}: • Removed: {OLD_PRINCIPLE_NAME} - {reason}

Impact:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Updated: {count} files (toolkit-specs/src/docs)
Review: {count} files may need manual updates (code/tests)
Constitution Compliance: {✅ Maintained | ⚠️ Check required}

Follow-up: Review toolkit code, update tests, validate compliance

Generated by: /metaspec.sdd.constitution
-->
```

### 8. Update version and timestamp

Update the version line at the top of `/memory/constitution.md`:

```markdown
> Version {NEW_VERSION} | Ratified: {ORIGINAL_DATE} | Last Updated: {TODAY}
```

**Version bump rules** (CRITICAL):

**MAJOR (X.0.0)** - Part I changes only:
- Core values modified or removed
- Project philosophy fundamentally changed
- Breaking changes to constitutional framework
- Example: 1.0.0 → 2.0.0

**MINOR (X.Y.0)** - Part II or Part III changes:
- New principles added to Part III
- Existing principles significantly expanded
- New mandatory implementation requirements
- Principle renamed (semantic change)
- Tech stack requirements changed
- Example: 1.1.0 → 1.2.0

**PATCH (X.Y.Z)** - Minor refinements:
- Clarifications, wording improvements
- Examples added to existing principles
- Typo corrections
- Non-semantic formatting changes
- Example: 1.1.0 → 1.1.1

**For Part III updates**:
- If principles added/removed: MINOR bump
- If principles substantially changed: MINOR bump
- If only examples/clarifications added: PATCH bump
- If tech stack requirements changed: MINOR bump
- If implementation patterns changed: MINOR bump

**Add update marker in Part III**:
```markdown
<!-- Managed by /metaspec.sdd.constitution -->
<!-- Last updated: {TODAY} v{VERSION} - {Brief description of changes} -->
```

### 9. Validation checklist

Before writing file, verify:

**Critical Checks**:
- [ ] Part I/II unchanged, Part III updated
- [ ] All 6 toolkit implementation principles present in Part III
- [ ] Version bump follows semantic versioning (MAJOR: Part I, MINOR: Part II/III, PATCH: fixes)
- [ ] Impact Report prepended at top
- [ ] Version line updated: `> Version X.Y.Z | Ratified: ... | Last Updated: ...`

**Quality Checks**:
- [ ] Each principle has implementation-specific examples (with tech stack/libraries)
- [ ] Consistency check results documented
- [ ] Affected files listed in Impact Report (specs/src/docs/tests)

### 10. Write updated constitution

**Write order**:
1. **Prepend** HTML comment Sync Impact Report at top
2. **Preserve** Part I exactly (Project Core Values)
3. **Preserve** Part II exactly (Specification Design Principles)
4. **Update** Part III (Toolkit Implementation Principles)
5. **Preserve** Governance section at bottom

**Write to**: `/memory/constitution.md`

**Quality checks**:
- Proper Markdown formatting
- Single blank line between sections
- No trailing whitespace
- Consistent heading levels

### 11. Output summary to user

Provide a comprehensive summary:

```
✅ Constitution Part III (Toolkit Implementation) updated to v{NEW_VERSION}

📊 Version Change: v{OLD_VERSION} → v{NEW_VERSION}
Bump Type: {MAJOR|MINOR|PATCH}
Rationale: {Brief reason for version bump}

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

📋 Changes in Part III:
Modified Principles:
- {PRINCIPLE_NAME}: {What changed}

Added Principles:
- {NEW_PRINCIPLE_NAME}: {Brief description}

Removed Principles:
- [OLD_PRINCIPLE_NAME]: [Reason for removal]

Tech Stack Updates:
- [LANGUAGE/LIBRARY]: {What was added/changed}

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

📁 Files Updated:
✅ Successfully Updated:
- /memory/constitution.md (Part III)
- [List other files auto-updated]

⚠️  Require Manual Review:
- [List files needing human attention]
- [List source code files that may need refactoring]

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

✅ Consistency Check Results:
- Toolkit specifications reviewed: [COUNT]
- Specifications compliant: [COUNT]
- Specifications needing update: [COUNT]
- Source files checked: [COUNT]
- Documentation files checked: [COUNT]

⚠️  Code Impact:
- Source files needing refactoring: [COUNT]
- Tests needing updates: [COUNT]
- Architecture changes required: [Yes/No]

📋 Follow-up TODOs:
- [ ] [TODO item 1]
- [ ] [TODO item 2]
- [ ] [TODO item 3]

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

🔄 Next Steps:
1. Review the Sync Impact Report in /memory/constitution.md (HTML comment at top)
2. Review Part III changes in /memory/constitution.md
3. Address files marked ⚠️  Require Manual Review
4. Refactor code if needed to match updated principles
5. Use /metaspec.sdd.specify to define toolkit specs following updated principles
6. Use /metaspec.sdd.checklist to validate implementation quality
7. Update tests to meet Automated Quality requirements

💡 Suggested Commit Message:
   docs(constitution): update Part III to v{NEW_VERSION} ({brief description})
   
   - {Change 1}
   - {Change 2}
   
   Affects: {list key files}
   Breaking: [Yes/No - if architecture changes required]
```

## Important Notes

1. **Constitution is for the toolkit, not the end-user project**
   - This defines how to BUILD the toolkit
   - It does NOT define how users USE the toolkit
   - Focus on entity design, validator architecture, CLI design

2. **Standard vs Domain-Specific Principles**
   - Always include the 6 standard speckit principles
   - Add domain-specific principles as needed (e.g., "RESTful API Conventions" for API testing)
   - Don't remove standard principles without strong justification

3. **Examples Matter**
   - Each principle should include concrete examples
   - Examples should use the actual entities from this toolkit
   - Bad: "Validators should be extensible"
   - Good: "Validators support custom rules via hooks, e.g., `register_assertion_validator('status_code', validate_http_status)`"

4. **AI-First Language**
   - Write for AI agents reading this document
   - Use imperative language (MUST, SHOULD, MAY)
   - Avoid ambiguity ("usually", "typically" → specify exact rules)
   - Include anti-patterns (what NOT to do)

5. **Version Control**
   - Never decrement version
   - Document reason for every version bump
   - Keep sync report for traceability

## Example Interaction

**User**: `/metaspec:constitution "Design principles for API Test Kit"`

**AI**:
"I'll help create the constitution for your API Test Kit. Let me ask a few clarifying questions:

1. What specifications will users write? (I'm assuming API test specs with endpoint, method, assertions)
2. Should the toolkit support both REST and GraphQL? (impacts Domain Specificity principle)
3. What's the primary workflow? (validate → execute → report?)

I'll draft a constitution with these standard principles:
- Entity-First Design (start with minimal APITest entity)
- Validator Extensibility (support custom assertion types)
- Spec-First Development (users write test.yaml, toolkit executes)
- AI-Agent Friendly (clear error messages, examples)
- Progressive Enhancement (MVP: validate + execute, later: generate, coverage)
- Domain Specificity (REST/GraphQL standards, HTTP semantics)

Shall I proceed?"

**[After user confirms]**

**AI**: 
"✅ Constitution created at /memory/constitution.md (v1.0.0)

📋 Principles defined:
- Entity-First: Start with APITest (endpoint, method, assertions)
- Validator Extensibility: Custom assertion types via plugins
- Spec-First: Declarative YAML specifications
- AI-Agent Friendly: Error messages show fix examples
- Progressive Enhancement: MVP first, then advanced features
- Domain Specificity: HTTP/REST standards, status codes, headers

🔄 Next step:
Use /metaspec:specify to define the APITest entity structure and validation rules, following these principles."

