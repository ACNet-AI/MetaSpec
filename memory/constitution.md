# Meta-Spec Development Constitution

> **Core Principles**: This document defines the fundamental rules and principles that govern Meta-Spec development and usage.

---

## 🎯 Mission Statement

**Meta-Spec exists to democratize the creation of spec-driven tools for AI agents.**

We believe that:
- Specification-driven development improves software quality
- AI agents can effectively use structured specifications
- Meta-programming reduces repetitive framework creation
- Domain expertise should be easily encoded into tools

---

## ✅ Core Principles

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

**This constitution is a living document. It evolves with the project, but core principles remain stable.**

**Last Updated**: 2025-01-20  
**Version**: 1.0  
**Status**: Active

