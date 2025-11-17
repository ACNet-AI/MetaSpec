# Meta-Spec Development Constitution

> **Core Principles**: This document defines the fundamental rules and principles that govern Meta-Spec development and usage.
>
> **Structure**: This constitution has three parts:
> - **Part I**: Project Core Values (MetaSpec project development)
> - **Part II**: Specification Design Principles (Domain specification design) - managed by `/metaspec.sds.constitution`
> - **Part III**: Toolkit Implementation Principles (Toolkit development) - managed by `/metaspec.sdd.constitution`

---

## 🎯 Mission Statement

**Meta-Spec exists to democratize the creation of spec-driven tools for AI agents.**

We believe that:
- Specification-driven development improves software quality
- AI agents can effectively use structured specifications
- Meta-programming reduces repetitive framework creation
- Domain expertise should be easily encoded into tools

---

## Part I: Project Core Values

These principles govern MetaSpec project development itself.

### ✅ Core Principles

### 1. Minimal Viable Abstraction

**Principle**: Avoid over-abstraction. Keep it as simple as possible.

```yaml
✅ Good: Only abstract what multiple domains need
❌ Bad: Abstract every possible variation
```

**Rules**:
- Start with concrete examples
- Abstract only after seeing 3+ similar patterns
- Each abstraction level must add clear value

### 2. AI-First Design

**Principle**: Generated systems must be optimized for AI agent usage.

```yaml
✅ Required in generated systems:
  - AGENTS.md with clear instructions
  - memory/constitution.md with domain rules
  - Structured templates for AI output
  - Clear command interfaces

❌ Prohibited:
  - Human-only interfaces without AI guidance
  - Unstructured or ambiguous specifications
  - Missing AI instruction files
```

### 3. Progressive Enhancement

**Principle**: Build incrementally, starting with MVP.

```yaml
✅ Development flow:
  MVP (2-4 weeks) → Enhancements (4-8 weeks) → Advanced (3-6 months)

❌ Don't:
  - Build all features at once
  - Add features before validating MVP
  - Skip user feedback loops
```

### 4. Domain Specificity Over Generality

**Principle**: Respect domain constraints. Don't force-fit generic solutions.

```yaml
✅ For MCP domain:
  - Validate MCP specification compliance
  - Check manifest.json schema
  - Verify tool/resource/prompt structure

✅ For Web domain:
  - Validate HTML/CSS/JS standards
  - Check accessibility requirements
  - Verify responsive design

❌ Don't:
  - Create one-size-fits-all validations
  - Ignore domain-specific best practices
```

### 5. Documentation as Code

**Principle**: Documentation and code must evolve together.

```yaml
✅ Required:
  - Every feature has documentation
  - Examples for all major use cases
  - API documentation for all public interfaces

❌ Prohibited:
  - Undocumented features
  - Outdated documentation
  - Missing examples
```

### 6. Iteration-Aware Design

**Principle**: Commands and workflows must support iterative development, not just one-time generation.

```yaml
✅ Required in command design:
  - Check for existing artifacts before generating
  - Support update/append modes, not just create
  - Preserve history and evidence
  - Track progress across iterations
  - Default to "update" when user says "re-run"

❌ Prohibited:
  - Commands that blindly overwrite existing work
  - No distinction between "new" and "update"
  - Loss of historical context
  - Assuming every run is from scratch
```

**Rules**:
- Every generative command MUST check if output already exists
- If exists, MUST ask user: update/new/append
- Update mode MUST preserve existing structure and evidence
- Add iteration tracking (Iteration N: [Date]) for progress visibility
- Default interpretation: "re-run" = "update", not "regenerate"

**Rationale**: Spec-driven development is iterative. Users refine specs progressively. Commands must support continuous improvement, not just initial generation.

---

## 🚫 Prohibited Patterns

### Anti-Pattern 1: Premature Optimization

```yaml
❌ Don't optimize before measuring
❌ Don't add caching before proving it's needed
❌ Don't create complex architectures for simple problems
```

### Anti-Pattern 2: Feature Creep

```yaml
❌ Don't add features not in the spec
❌ Don't solve problems users don't have
❌ Don't build "just in case" functionality
```

### Anti-Pattern 3: Ignoring Domain Constraints

```yaml
❌ Don't violate specification specifications (e.g., MCP specification)
❌ Don't skip validation for "convenience"
❌ Don't assume domain knowledge without research
```

### Anti-Pattern 4: Breaking Self-Hosting

```yaml
❌ Don't create systems Meta-Spec can't generate
❌ Don't use patterns that can't be abstracted
❌ Don't break the meta-spec → spec-system flow
```

---

## ✅ Required Patterns

### Pattern 1: Schema-First Design

```yaml
✅ Always define JSON Schema before implementation
✅ Validate all inputs against schema
✅ Generate code from schema when possible
```

### Pattern 2: Template-Driven Generation

```yaml
✅ Use Jinja2 templates for code generation
✅ Separate logic from templates
✅ Test templates independently
```

### Pattern 3: Adapter Pattern for Domain Extensions

```yaml
✅ Create adapters for domain-specific logic
✅ Keep core engine domain-agnostic
✅ Register adapters through plugin system
```

### Pattern 4: Constitution Inheritance

```yaml
✅ Generated systems inherit meta-spec principles
✅ Add domain-specific rules on top
✅ Never violate parent constitution
```

---

## 📊 Quality Standards

### Code Quality

| Metric | Target | Measurement |
|--------|--------|-------------|
| Test Coverage | ≥ 80% | pytest-cov |
| Type Safety | 100% | mypy |
| Code Style | 100% | black + ruff |
| Documentation | 100% | All public APIs |

### Generated System Quality

| Metric | Target | Validation |
|--------|--------|------------|
| AI Instruction Completeness | 100% | Has AGENTS.md |
| Constitution Inheritance | 100% | Has memory/constitution.md |
| Template Coverage | 100% | All output types |
| Example Completeness | ≥ 2 | Working examples |

### Performance

| Metric | Target | Scenario |
|--------|--------|----------|
| Parse Speed | < 100ms | Medium meta-spec |
| Validate Speed | < 50ms | Schema validation |
| Generate Speed | < 5s | Complete spec system |
| Memory Usage | < 100MB | Peak memory |

---

## 🎯 Decision Framework

When making design decisions, evaluate against these criteria:

### 1. Does it simplify the user's mental model?
```
✅ Yes → Good decision
❌ No → Reconsider
```

### 2. Does it work well with AI agents?
```
✅ Yes → Good decision
❌ No → Reconsider
```

### 3. Does it add essential value?
```
✅ Yes → Good decision
❌ No → YAGNI (You Aren't Gonna Need It)
```

### 4. Can it be implemented incrementally?
```
✅ Yes → Good decision
❌ No → Break it down
```

### 5. Does it respect domain constraints?
```
✅ Yes → Good decision
❌ No → Add domain adapter
```

---

## 🔄 Evolution Rules

### When to Add Features

```yaml
✅ Add when:
  - 3+ users request it
  - Clear use case exists
  - Fits existing architecture
  - Has champion who will maintain it

❌ Don't add when:
  - "Might be useful someday"
  - Breaks existing patterns
  - No clear owner
```

### When to Refactor

```yaml
✅ Refactor when:
  - Code duplication > 3 instances
  - Cognitive complexity too high
  - Tests are brittle
  - Performance issues measured

❌ Don't refactor when:
  - "Just feels wrong" without data
  - Breaking working code without reason
  - Before validating with users
```

### When to Deprecate

```yaml
✅ Deprecate when:
  - Better alternative exists
  - No active users (measured)
  - High maintenance cost
  - Violates core principles

Process:
  1. Mark as deprecated (1 version)
  2. Provide migration guide
  3. Remove (2 versions later)
```

---

## 📝 Contribution Guidelines

### For Core Features

1. **Discuss First**: Create an issue before coding
2. **Design Document**: Write design doc for major features
3. **Test First**: Write tests before implementation
4. **Document**: Update docs before merging
5. **Review**: Two maintainer approvals required

### For Domain Adapters

1. **Example First**: Show real use case
2. **Minimal Interface**: Keep adapter interface small
3. **Self-Contained**: No dependencies on other adapters
4. **Documented**: Include usage guide and examples

### For Templates

1. **Lint**: Templates must pass linting
2. **Test**: Generate and test output
3. **Variables**: Document all template variables
4. **AI-Friendly**: Include comments for AI agents

---

## 🎉 Success Criteria

A Meta-Spec release is successful when:

1. ✅ All tests pass (100%)
2. ✅ Documentation is complete (100%)
3. ✅ At least 2 working examples
4. ✅ Performance targets met (100%)
5. ✅ Can generate itself (self-hosting)
6. ✅ AI agents can use it effectively
7. ✅ User feedback positive (≥ 4.0/5.0)

---

## 🔮 Long-Term Vision

### Phase 1: Foundation (Current)
- Basic meta-spec → spec-system generation
- Support for spec-kit and openspec patterns
- Core domain adapters (MCP, Web, AI)

### Phase 2: Ecosystem (6-12 months)
- Plugin marketplace
- Community templates
- Multi-language support

### Phase 3: Self-Hosting (1-2 years)
- Meta-Spec can define itself completely
- Automatic meta-spec updates
- AI-assisted meta-spec refinement

---

## 📚 References

### Internal Documents
- **[Development Principles](./development-principles.md)** ⭐⭐⭐⭐⭐
  - DRY, YAGNI, KISS, Pareto, MVP
  - Classic software engineering principles
  - Must read! All development decisions must follow these

- **[Spec Design Principles](./spec-design-principles.md)** ⭐⭐⭐
  - Schema-First, Self-Documenting, Validation-Friendly
  - How to design specification formats (meta-spec.yaml, etc.)
  - Inherited from OpenAPI, JSON Schema standards

- **[SS-X Toolkit Principles](./ssx-toolkit-principles.md)** ⭐⭐⭐⭐⭐
  - Distilled from Spec-Kit real-world projects
  - 5 practical principles (AI-First, Command Workflow, Template-Driven, Progressive, Automated)
  - Guides how to develop spec-driven toolkits (project structure)

### External References
- [Spec-Kit](https://github.com/github/spec-kit) - Original inspiration
- [Protocol Buffers](https://protobuf.dev/) - Meta-programming patterns
- [OpenAPI](https://www.openapis.org/) - Specification standards
- [YAGNI Principle](https://martinfowler.com/bliki/Yagni.html)
- [Progressive Enhancement](https://en.wikipedia.org/wiki/Progressive_enhancement)

---

---

## Part II: Specification Design Principles

These principles govern how domain specifications should be designed (managed by `/metaspec.sds.constitution`).

### 1. Entity Clarity

**Principle**: Entities must have clear purpose, well-defined fields, and unambiguous semantics.

**Rules**:
- Each entity has a single, clear responsibility
- Field types must be explicit (no ambiguous types)
- Relationships between entities are documented
- Every field has a description

### 2. Validation Completeness

**Principle**: All validation rules must be explicitly defined and enforceable.

**Rules**:
- Required vs optional fields clearly marked
- Constraints are machine-checkable
- Validation rules reference specific fields
- Error messages are descriptive

### 3. Operation Semantics

**Principle**: Operations have clear inputs, outputs, and side effects.

**Rules**:
- Request/response schemas defined
- Idempotency documented
- Error conditions specified
- Examples provided

### 4. Implementation Neutrality

**Principle**: Specifications describe WHAT, not HOW (implementation-agnostic).

**Rules**:
- No language-specific constructs
- No implementation details in specs
- Focus on interface contracts
- Platform-neutral terminology

### 5. Extensibility Design

**Principle**: Specifications support evolution without breaking changes.

**Rules**:
- Version fields in entities
- Optional fields for new features
- Deprecation process defined
- Backward compatibility considered

### 6. Domain Fidelity

**Principle**: Specifications accurately reflect domain knowledge and constraints.

**Rules**:
- Use domain terminology
- Respect domain rules
- Research existing standards
- Validate with domain experts

### 7. Workflow Completeness ⭐ NEW v0.8.0

**Principle**: Specifications must define complete user workflows, not just isolated operations.

**Two Types of Workflows**:

#### Type 1: Entity State Machines (Optional, for stateful entities)
- Define entity lifecycle during business execution
- Example: Order (pending → confirmed → shipped → delivered)
- Document allowed/forbidden transitions
- Specify preconditions and postconditions

#### Type 2: Specification Usage Workflow (Required for all Speckits)
- Define end-to-end specification creation process
- Example: SDS Workflow (Constitution → Specify → Clarify → ... → Implement)
- 8-12 action steps typical
- Each step maps to a slash command
- Include quality gates and validation checkpoints

**Rules**:
- Type 2 workflow is REQUIRED for all speckits
- Each workflow step has clear goal, inputs, outputs
- Steps are sequential with dependencies
- Each step maps 1:1 to a command (e.g., `/domainspec.action`)
- No "orphan" operations without workflow context
- End-to-end examples demonstrate complete workflow

**Rationale**: 
- Pre-v0.7.0: Users received "13 commands" without knowing sequence
- Post-v0.7.0: Workflow-first design provides clear user journey
- Type 2 is about HOW to use the speckit, Type 1 is about WHAT entities do

**Example Comparison**:
```yaml
# Type 1 (Entity State Machine) - Business execution
Specification Entity:
  states: [draft, review, approved, deprecated]
  transitions: draft → review → approved

# Type 2 (Specification Usage Workflow) - Specification creation
SDS Workflow:
  Step 1: Constitution → Define principles
  Step 2: Specify → Create spec document
  Step 3: Clarify → Resolve ambiguities
  ...
  Step 8: Implement → Write sub-specifications
```

---

## Part III: Toolkit Implementation Principles

These principles govern how speckits (spec-driven toolkits) should be implemented (managed by `/metaspec.sdd.constitution`).

### 1. Entity-First Design

**Principle**: Toolkit architecture mirrors specification entities.

**Rules**:
- Entity classes match specification entities
- Parser produces entity objects
- Validator checks entity constraints
- Clear mapping: spec → code

### 2. Validator Extensibility

**Principle**: Validation system supports custom rules without core changes.

**Rules**:
- Pluggable validator architecture
- Domain-specific validators as plugins
- Base validators for common patterns
- Clear validator registration mechanism

### 3. Spec-First Development

**Principle**: Specification is the source of truth; toolkit enforces it.

**Rules**:
- Code references specification
- Validation rules implement spec constraints
- Generated code includes spec comments
- Toolkit version matches spec version

### 4. AI-Agent Friendly

**Principle**: Toolkit design optimizes for AI agent usage.

**Rules**:
- Slash commands in `.metaspec/commands/`
- AGENTS.md with clear instructions
- Structured output formats (YAML/JSON)
- Examples for each command
- Templates for common patterns

### 5. Progressive Enhancement

**Principle**: Toolkit starts minimal, adds features incrementally.

**Rules**:
- MVP: Parser + Validator + Init
- Phase 2: Generator + Templates
- Phase 3: Advanced features
- Each phase is deployable

### 6. Automated Quality

**Principle**: Quality checks are automated and integrated.

**Rules**:
- Linting integrated in CLI
- Test generation from examples
- CI/CD validation
- Coverage tracking

---

**This constitution is a living document. It evolves with the project, but core principles remain stable.**

**Last Updated**: 2025-11-17  
**Version**: 2.0  
**Status**: Active

