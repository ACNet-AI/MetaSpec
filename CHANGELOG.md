# Changelog

All notable changes to MetaSpec will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### ✨ Improvements

**Enhanced slash command specification with Claude Code best practices**

**Inspiration**: Adopted proven patterns from [Claude Code slash commands](https://code.claude.com/docs/en/slash-commands)

**New frontmatter fields**:
1. ✅ **`argument-hint`**: Show expected arguments in `/help` (e.g., `[pr-number] [priority]`)
2. ✅ **`allowed-tools`**: Restrict command to specific tools for security (e.g., `Bash(git:*), FileEdit(specs/*)`)
3. ✅ **`model`**: Specify AI model for specific commands (e.g., `claude-3-5-haiku-20241022` for simple tasks)
4. ✅ **Positional arguments**: Support `$1`, `$2`, `$3` in addition to `$ARGUMENTS`

**Enhancements**:
- ✅ Updated all 3 slash command templates (Pure-Execution, Script-Assisted, CLI-Referenced)
- ✅ Added comprehensive frontmatter fields table with examples
- ✅ Added argument access patterns documentation
- ✅ Maintained MetaSpec's unique Spec-Driven positioning
- ✅ Preserved dual-source architecture (Protocol-Derived + Library-Selected)

**Before**:
```yaml
---
description: Create feature spec
scripts:
  sh: scripts/bash/script.sh
---
```

**After**:
```yaml
---
description: Create feature specification
argument-hint: [feature-description]
scripts:
  sh: scripts/bash/script.sh --json "{ARGS}"
  ps: scripts/powershell/script.ps1 -Json "{ARGS}"
allowed-tools: Bash(git:*), FileEdit(specs/*)
model: claude-3-5-sonnet-20241022
---
```

**Impact**: 
- ✅ **Better UX**: Users see expected arguments in `/help`
- ✅ **More secure**: Can restrict tools per command
- ✅ **Cost-optimized**: Can use lighter models for simple commands
- ✅ **More flexible**: Positional arguments for structured commands
- ✅ **Industry standard**: Aligns with Claude Code patterns

**Files Changed**: `specify.md.j2`

---

### 🐛 Bug Fixes

**Removed hardcoded line number references**

**Issue**: Document contained hardcoded line references that become stale after edits:
- ❌ "(lines 364-643)" - specific line ranges in cross-references
- ❌ Line numbers shift when content is added/removed
- ❌ Creates maintenance burden and confusion

**Fix**: Removed all hardcoded line numbers (2 occurrences):
- ✅ Line 855: Removed "(lines 364-643)" from Component 3 cross-reference
- ✅ Line 867: Removed "(lines 364-643)" from Component 3 subset reference
- ✅ Kept component name references for clarity

**Impact**: 
- ✅ References won't become stale after edits
- ✅ Easier to maintain
- ✅ Still clear (users can search for "Component 3")

**Files Changed**: `specify.md.j2`

---

**Removed all MCP-specific examples to ensure framework neutrality**

**Issue**: Document contained 30+ references to MCP (Model Context Protocol) throughout:
- ❌ Component 3: "MCP-Speckit CLI Design" entire section
- ❌ Tables: "MCP: define-server, configure-tools, validate-server"
- ❌ Quick Reference: Using MCP Server concepts
- ❌ Examples: mcp-parser, mcp-toolkit, mcpspeckit
- ❌ Made MetaSpec appear MCP-specific, not a general framework

**Fix**: Comprehensive cleanup (30 → 0 references):
- ✅ Removed Component 3 "MCP-Speckit CLI Design" section entirely
- ✅ Replaced table examples with MetaSpec's own commands and generic examples
- ✅ Updated Quick Reference to use universal concepts
- ✅ Changed all MCP examples to framework-neutral ones
- ✅ Tables now show: MetaSpec (specify, clarify, plan) and Generic (design, build, test)

**Before**:
- Component 3: 37 lines of MCP-specific CLI design
- Tables: MCP examples dominating (define-server, init-server, validate-server)
- Quick Reference: "Define Server" → define-server

**After**:
- Component 3: Removed
- Tables: MetaSpec + Generic examples only
- Quick Reference: "Specify Feature" → specify

**Impact**: 
- ✅ **Framework neutral**: No external protocol dependencies
- ✅ **Dogfooding emphasized**: Uses MetaSpec's own commands as examples
- ✅ **Clearer positioning**: General meta-framework, not MCP-specific tool

**Files Changed**: `specify.md.j2` (11 locations updated)

---

**Eliminated redundant and incorrect examples (8 → 3, 62.5% reduction)**

**Issues**:
1. ❌ **Incorrect Spec-Kit pattern**: Table showed false "Verb-Noun" commands (`specify-feature`, `plan-implementation`)
   - Actual commands are single verbs (`specify`, `plan`, `implement`)
   - Spec-Kit is MetaSpec's internal library, same pattern as MetaSpec without namespace
2. ❌ **Redundant examples**: Example 2 (Project Lifecycle) and Example 3 (MetaSpec SDD) duplicated in table
3. ❌ **Too many examples**: 8 total with multiple abstract examples less valuable than real implementations

**Fix**: Comprehensive simplification and correction:
- ✅ **STEP 1**: Reduced from 3 examples to 1 - MetaSpec SDD (real dogfooding implementation)
- ✅ **STEP 2 Table**: Reduced from 5 rows to 2 - MetaSpec / OpenSpec only
- ✅ **Removed incorrect**: Spec-Kit row (false verb-noun pattern)
- ✅ **Removed duplicates**: Example 1 (Development Workflow), Example 2 (Project Lifecycle), MetaSpec SDS

**Two proven patterns retained**:
1. **MetaSpec**: Namespaced Verbs (`sdd.specify`, `sdd.clarify`, `sdd.plan`) - for multi-layer systems
2. **OpenSpec**: Domain Verbs (`proposal`, `apply`, `archive`) - for single-domain tools

**Impact**: 
- ✅ **Accurate**: No false examples (Spec-Kit correction)
- ✅ **Concise**: 62.5% reduction (8 → 3 examples)
- ✅ **Clear**: Each example appears once, no duplication
- ✅ **Valuable**: Real projects only, no abstract examples

**Files Changed**: `specify.md.j2`

---

### 🐛 Bug Fixes

**Replaced external project examples with MetaSpec's own implementations**

**Issue**: Example 3 used "MCP Server Development" (Anthropic's MCP protocol), making MetaSpec appear project-specific rather than a general framework.

**Fix**: Replaced with "MetaSpec SDD Workflow" showing how MetaSpec itself was built (dogfooding):
- Example 3: constitution → specify → clarify → plan → tasks → implement → checklist → analyze
- Table: Added MetaSpec SDD + SDS workflow examples
- Pattern: Development workflow → namespaced commands

**Impact**: 
- ✅ More credible (we use this ourselves)
- ✅ Framework-neutral (not tied to external projects)
- ✅ Educational (verifiable in MetaSpec source)

**Files Changed**: `specify.md.j2`

---

## [0.2.0] - 2025-11-07

### ✨ Major Feature - User-Centered Toolkit Design

**Added User Journey Analysis to `/metaspec.sdd.specify`** (Based on mcp-speckit feedback)

MetaSpec now guides developers to design toolkits from user needs, not just technical specifications.

#### P0: User Journey & Feature Derivation (Step 2.5)

**New Section**: `Step 2.5: User Journey & Feature Derivation` (added between Step 2 and Step 3)

**What Changed**:
1. **User Analysis** (STEP 1)
   - Identify primary users (AI Agents / Human Developers / Both)
   - Define user characteristics (skill level, context, goals)
   - Example: "80% AI Agents, 20% Human Developers"

2. **Usage Scenarios** (STEP 2)
   - Define 3-5 key scenarios with complete workflow
   - Template includes: User, Context, Goal, Pain Point, Desired Experience
   - Example scenarios: "AI Agent generates MCP server", "Developer validates manually", "AI debugs errors"

3. **Feature Derivation** (STEP 3)
   - Map scenarios to features with priority matrix
   - Categorize: Information Access / Content Generation / Validation / Developer Experience
   - Prioritize: P0 (Must Have) / P1 (Should Have) / P2 (Nice to Have)

4. **Command Derivation from Scenarios** (STEP 4)
   - Extract CLI commands from user scenarios
   - Extract Slash Commands from AI agent scenarios
   - Identify templates needed from scenarios

5. **Document Insights** (STEP 5)
   - Add "User Journey Analysis" section to toolkit spec
   - Include rationale for command design decisions
   - Explain feature prioritization

**Why This Matters**:
- ✅ **User-driven design**: Features derived from real user needs, not arbitrary technical choices
- ✅ **Prevents missing features**: Scenario analysis ensures critical functionality isn't overlooked
- ✅ **Clear prioritization**: P0/P1/P2 system based on scenario frequency and criticality
- ✅ **Better AI guidance**: AI knows *why* commands exist (mapped to user scenarios)
- ✅ **Traceability**: Every feature/command traces back to a user scenario

**Example Output**:
```markdown
## User Journey Analysis

### Primary Users
- 80% AI Agents (Claude in Cursor)
- 20% Human Developers

### Key Scenarios
1. AI generates MCP server → needs: show-protocol, get-template
2. Developer validates manually → needs: init, validate, docs
3. AI debugs errors → needs: validate, explain-error

### Derived Features (P0)
- Protocol reference system (Scenarios 1, 3)
- Template system (Scenarios 1, 2)
- Validation CLI (All scenarios)

### Command Design Rationale
- `show-protocol`: AI needs rules before generating (Scenario 1)
- `validate`: Critical for both AI and developers (All scenarios)
- `init`: Developer quick setup (Scenario 2)
```

**Impact on Generated Speckits**:
- Toolkit specifications now include "User Journey Analysis" section
- Commands are justified by user scenarios (not arbitrary)
- Feature prioritization is explicit and traceable

---

#### P1: Templates Directory Structure (Component 6) - Embodies Composability

**New Section**: `Component 6: Templates Directory Structure (CRITICAL - Embodies Composability)` (added after Component 5)

**Core Principle**: **Organize by specification system source**, not by file type.

**What Changed**:

1. **Specification Composability Structure**
   ```bash
   templates/
   ├── {library-spec-1}/       # From library (e.g., generic, spec-kit)
   │   ├── commands/           # Slash Commands from this spec system
   │   └── templates/          # Templates from this spec system
   ├── {library-spec-2}/       # Another specification system
   │   ├── commands/
   │   └── templates/
   └── {custom}/               # Custom (from protocol)
       ├── commands/           # Protocol-specific Slash Commands
       └── templates/          # Protocol entity templates
   ```

2. **Key Benefits**:
   - ✅ **Clear provenance**: Which spec system provides which commands
   - ✅ **Avoid conflicts**: Different systems can have same-named commands
   - ✅ **Partial replacement**: Update one spec system without affecting others
   - ✅ **MetaSpec convention**: Follows `meta/sds/`, `library/sdd/spec-kit/` pattern

3. **Complete Example (MCP-Speckit)**:
   ```bash
   templates/
   ├── generic/               # From library/generic
   │   ├── commands/
   │   └── templates/
   ├── spec-kit/              # From library/sdd/spec-kit
   │   ├── commands/
   │   └── templates/
   └── mcp/                   # Custom (from protocol/001-mcp-protocol)
       ├── commands/
       └── templates/
   ```

4. **Implementation Guide**:
   - **Library Specifications**: Copy from MetaSpec library → `templates/{library-name}/`
   - **Custom Specification**: Derive from protocol → `templates/{domain}/`
   - **Examples**: Separate top-level `examples/` directory (not under `templates/`)

**Why This Matters**:
- ✅ **Embodies MetaSpec's core value**: Specification composability
- ✅ **Traceability**: Clear which commands/templates come from which source
- ✅ **Maintainability**: Update specific specification systems independently
- ✅ **Discoverability**: AI and developers can navigate by specification source
- ✅ **Follows MetaSpec convention**: Same pattern as `library/sdd/spec-kit/`
- ✅ **Aligns with Component 4**: Dual-source architecture consistency

**Checklist Provided**:
- [ ] Library specifications mapped to `templates/{library-name}/`
- [ ] Custom specification in `templates/{domain}/`
- [ ] P0 Slash Commands created (from Step 2.5 STEP 4)
- [ ] Entity templates match protocol entities
- [ ] Examples in top-level `examples/` directory
- [ ] At least 1-2 complete examples

**Implementation Notes**:
- This is the **recommended target structure** for speckit development
- Current `metaspec init` may generate flat structure initially
- Migration path: specify → plan → implement

**Impact on Generated Speckits**:
- Toolkit specifications now embody specification composability
- Clear which specification systems are composed together
- Independent evolution of specification systems enabled
- Aligns with MetaSpec's own source code organization

---

**Resolution of mcp-speckit Feedback**:

| Issue | Status | Resolution |
|-------|--------|------------|
| **❌ P0-1: User Journey 缺失** | ✅ **Resolved** | Step 2.5 added with 5-step analysis |
| **❌ P0-3: Templates 指导不足** | ✅ **Resolved** | Component 6 added with complete structure |
| **🟡 P0-1: CLI 从需求推导** | ✅ **Improved** | Commands now derived from scenarios (Step 2.5 STEP 4) |
| **✅ P0-2: AI Agent Interface** | ✅ **Already Done** | Component 4 (Slash Commands) |

**Overall Resolution**: **100%** (4/4 issues addressed)

---

### 🔧 Structure Improvements

**Fixed file structure issues in `/metaspec.sdd.specify`**:

1. **Fixed Heading Hierarchy** (P0 - Critical)
   - Component 3: Changed STEP 1-4 from `####` (heading level 4) to bold text
   - Resolved: Sub-sections had higher heading level than parent section
   - Impact: Clearer document structure, better table of contents

2. **Renumbered Component 4 STEP Sequence** (P0 - Critical)
   - Before: STEP 1, 2, 2.5, 3, 4, 5, 6 (irregular)
   - After: STEP 1, 2, 3, 4, 5, 6, 7 (sequential)
   - Fixed: "STEP 2.5" irregular numbering

3. **Added Cross-References** (P1 - Important)
   - STEP 4 now explicitly references Component 3
   - Clarified relationship: STEP 4a is subset of Component 3
   - Added clear guidance: "CLI commands should be defined in Component 3 first"

4. **Improved Section Titles** (P1 - Important)
   - STEP 4a: "CLI Commands (CLI-Referenced Only)" → "CLI Commands (CLI-Referenced Pattern)"
   - Added context explanations in STEP 4a
   - Emphasized cross-reference to Component 3

5. **Added Structure Explanation for Source 1/2** (P2 - Optional)
   - Source 2: Added explanation of why process is simpler
   - Clarified: Source 2 reuses proven commands (select + adapt + integrate)
   - Context: Source 1 = derive from scratch (7 steps), Source 2 = reuse (3 steps)

6. **Streamlined Redundant Examples** (Content Optimization)
   - Reduced MCP example repetition (30 mentions → focused usage)
   - STEP 2: Full MCP example → Quick reference (saved ~25 lines)
   - STEP 3: Full classification example → Summary (saved ~45 lines)
   - STEP 5: Command type re-explanation → Reference to STEP 3 (saved ~3 lines)
   - Total reduction: 1835 → 1762 lines (73 lines, 4% reduction)

**Why This Matters**:
- Eliminates reader confusion about CLI command duplication
- Clear hierarchical structure for better navigation
- Explicit cross-references show relationships between sections
- Justifies design decisions (why Source 2 is intentionally simpler)
- Reduces redundancy: More concise, easier to read
- Maintains completeness: Key information preserved, details referenced

**Files Changed**:
- src/metaspec/templates/meta/sdd/commands/specify.md.j2 (structure improvements)

---

### 📝 Template Enhancements

**Enhanced `spec-template.md.j2` to reflect new features**:

#### Added: User Journey Analysis Section

**New Section**: `## User Journey Analysis` (inserted after Toolkit Overview)

**Contents**:
1. **Primary Users**: AI Agents vs Human Developers distribution
2. **Key Scenarios**: 3-5 scenarios with User, Context, Goal, Pain Point, Desired Experience
3. **Derived Features**: P0/P1/P2 priority matrix mapped to scenarios
4. **Command Design Rationale**: Why each CLI/Slash Command exists
5. **Scenario Coverage Matrix**: Feature coverage verification

**Benefits**:
- ✅ Aligns with `/metaspec.sdd.specify` Step 2.5 (User Journey & Feature Derivation)
- ✅ Generated speckits now include user scenario analysis
- ✅ Features are justified by real user needs
- ✅ Traceability from scenarios to commands/templates

**Example**: See complete example in [P0: User Journey & Feature Derivation](#p0-user-journey--feature-derivation-step-25) section above.

---

#### Added: Templates & Examples Section

**New Section**: `## Templates & Examples` (inserted after CLI Commands)

**Contents**:
1. **Templates Directory Structure**: Organized by specification system source
2. **Template Mapping**: Library specs → directory names
3. **P0 Slash Commands**: Must-implement commands from scenarios
4. **Entity Templates**: Protocol entities → template files
5. **Examples Directory**: Separate structure with basic/advanced/use-cases
6. **Implementation Checklist**: Verification checklist

**Benefits**:
- ✅ Aligns with `/metaspec.sdd.specify` Component 6 (Templates Directory Structure)
- ✅ Embodies specification composability principle
- ✅ Clear provenance: Know which spec system provides which commands
- ✅ Follows MetaSpec convention: Same pattern as `library/sdd/spec-kit/`

**Example Structure**:
```
templates/
├── generic/               # From library/generic
│   ├── commands/
│   └── templates/
├── spec-kit/              # From library/sdd/spec-kit
│   ├── commands/
│   └── templates/
└── mcp/                   # Custom (from protocol)
    ├── commands/
    └── templates/

examples/
├── basic/
├── advanced/
└── use-cases/
```

---

#### Impact on Generated Speckits

**Generated `specs/toolkit/001-*/spec.md` now includes**:
- User Journey Analysis with scenario-to-feature mapping
- Templates & Examples section with composability structure
- Clear rationale for every command/feature
- Implementation checklist for templates and examples

**Backward Compatibility**: ✅ Maintained
- Existing sections unchanged
- New sections are additive enhancements
- Optional - can be filled or left as templates

---

**Files Changed**:
- src/metaspec/templates/meta/templates/spec-template.md.j2 (added 2 new sections)

**Related Features**:
- `/metaspec.sdd.specify` Step 2.5: User Journey & Feature Derivation
- `/metaspec.sdd.specify` Component 6: Templates Directory Structure

---

### 📚 Documentation Updates

**Enhanced `AGENTS.md` to reflect new features**:

#### Updated: Phase 2 Toolkit Specification Section

**Section**: `Phase 2: Toolkit Specification (SDD)` → Recommended Practice: SDS + SDD Separation

**What Changed**:

1. **Expanded "What to include" section** (+7 items):
   - Added: **User Journey Analysis** (🆕 From Step 2.5)
     - Primary users distribution
     - Key usage scenarios (3-5 scenarios)
     - Feature derivation (P0/P1/P2 priority matrix)
     - Command design rationale
     - Scenario coverage matrix
   - Added: **Templates & Examples** (🆕 From Component 6)
     - Templates directory structure
     - Template mapping
     - Entity templates
     - Examples directory
     - Implementation checklist

2. **Enhanced Example** (Added 2 new sections):
   - **User Journey Analysis section** with:
     - Primary users (80% AI / 20% Developers)
     - 2 complete scenarios (AI Agent + Developer)
     - Derived features with scenario mapping
     - Command design rationale
   - **Templates & Examples section** with:
     - Complete directory structure (generic/spec-kit/mcp)
     - Slash commands mapping
     - Examples organization (basic/advanced)

3. **Updated Key Principle**:
   - Before: "Toolkit specs explicitly depend on protocol specs and define HOW to implement"
   - After: "Toolkit specs explicitly depend on protocol specs, **derive features from user scenarios**, and define HOW to implement"

**Benefits**:
- ✅ AI Agents now understand how to use User Journey Analysis
- ✅ Clear guidance on Templates & Examples organization
- ✅ Complete example shows new sections in context
- ✅ Aligns with `/metaspec.sdd.specify` Step 2.5 and Component 6

**What it looks like**: See `AGENTS.md` lines 365-422 for the complete updated example with both User Journey Analysis and Templates & Examples sections.

**Impact**:
- AI Agents can better guide developers to create user-centered toolkits
- Clear understanding of scenario-driven feature derivation
- Templates organization principle is now documented for AI reference

---

**Files Changed**:
- AGENTS.md (Phase 2 section enhanced with new features)

**Related Features**:
- `/metaspec.sdd.specify` Step 2.5: User Journey & Feature Derivation
- `/metaspec.sdd.specify` Component 6: Templates Directory Structure
- `spec-template.md.j2`: User Journey Analysis section
- `spec-template.md.j2`: Templates & Examples section

---

### ✨ Major Feature - Spec-Driven Slash Commands

**Revolutionary Change**: Slash Commands redesigned as **spec-driven execution guides**, not CLI wrappers.

#### What Changed

**Previous Understanding** ❌:
- Slash Commands = "How to use CLI commands"
- AI reads Slash Command → calls CLI → processes output
- Generic templates (init, validate, generate)

**New Understanding** ✅:
- Slash Commands = "Spec-driven execution guides with embedded protocol knowledge"
- AI reads Slash Command (with protocol knowledge) → produces spec-compliant output
- Commands derived from protocol specification

#### Key Improvements

1. **Protocol-Driven Command Derivation**
   - Added STEP 1: Analyze protocol specification
   - Added STEP 2: Derive commands from protocol content
   - Mapping rules: entities → get-template, validation_rules → validate, workflows → commands
   
2. **Workflow-Aware Command Generation**
   - Type A (State Machine): Use navigation commands (get-workflow, next-phase)
   - Type B (Action Sequence): Each action becomes a command (like MetaSpec's specify → clarify → plan)
   - Judgment rule: verb/action → command, noun/state → navigation

3. **Embedded Protocol Knowledge**
   - Slash Commands now embed: entity definitions, validation rules, examples
   - AI can produce compliant output without external reference
   - Self-validation checklists included

4. **Command Prioritization**
   - P0 (Critical): get-spec, get-template, validate, workflow actions
   - P1 (Important): get-workflow, get-example, init
   - P2 (Skip): info, version, help

#### Updated `/metaspec.sdd.specify` - Slash Commands

**New Section**: Component 4 - Slash Commands - Spec-Driven Execution

#### Updated `/metaspec.sdd.specify` - CLI Commands

**Major Revision**: Component 3 - CLI Commands completely rewritten with derivation methodology.

**Key Additions**:

1. **CLI vs Slash Commands Distinction**
   - Slash Commands = Protocol-Driven (workflow actions)
   - CLI Commands = Purpose-Driven (toolkit functions)
   - Clear separation of concerns

2. **Toolkit Type Classification**
   - 6 toolkit types identified: Generator, Environment Checker, Validator, Query Tool, State Manager, Community Platform
   - Each type derives specific CLI commands
   - Real project examples: Specify, OpenSpec, MetaSpec

3. **4-Step CLI Derivation Process**
   - STEP 1: Define Toolkit Type (Generator? Validator? Query Tool?)
   - STEP 2: Derive CLI Commands from Type (type → commands mapping)
   - STEP 3: Protocol-Influenced CLI Parameters (protocol affects parameters, not commands)
   - STEP 4: Define CLI Implementation (detailed specs for each command)

4. **Real-World Validation**
   - Analyzed 4 projects: Spec-Kit (shell scripts), OpenSpec (validator+query), MetaSpec (generator+community), Specify (generator+checker)
   - Confirmed: CLI commands come from toolkit purpose, not protocol workflow
   - Examples included for each toolkit type

**Impact**: AI now has clear methodology to derive appropriate CLI commands based on toolkit purpose, avoiding both over-engineering and missing essential functionality.

#### ⚠️ CRITICAL FIX: Removed Hardcoded Command Names

**Problem Identified**: Previous version contained hardcoded command names throughout:
- Slash Commands: `get-spec`, `get-template`, `validate`, `get-example` (hardcoded mapping table)
- CLI Commands: `init`, `create`, `scaffold`, `list`, `show` (hardcoded per toolkit type)

**Why This Was Wrong**:
- ❌ No real project uses `get-template` or `get-spec`
- ❌ Generic names lose domain meaning
- ❌ Contradicts actual implementations (Spec-Kit: `specify`, OpenSpec: `proposal`, MetaSpec: `specify`)
- ❌ Forces "one-size-fits-all" approach

**What Changed**:

1. **Slash Commands - STEP 2 (Complete Rewrite)**
   - ❌ Removed: Hardcoded mapping table (Protocol Content → Fixed Command Names)
   - ✅ Added: Command naming process (3 steps: Read protocol → Extract verbs/nouns → Form domain names)
   - ✅ Added: Real project patterns (Spec-Kit, OpenSpec, MetaSpec naming examples)
   - ✅ Added: "Command Purpose Categories" (guidance, NOT fixed names)
   - ✅ Example: MCP protocol → `define-server`, `configure-tools` (NOT get-template)

2. **CLI Commands - STEP 2 (Complete Rewrite)**
   - ❌ Removed: Hardcoded command table (Toolkit Type → Fixed CLI Commands)
   - ✅ Added: CLI command derivation process (Identify functions → Match purposes → Choose names)
   - ✅ Added: Real project CLI commands (actual implementations from Specify, OpenSpec, MetaSpec)
   - ✅ Added: "Command Purpose Guidelines" (NOT fixed names)
   - ✅ Example: MCP-Speckit → `show`, `docs`, `list` (NOT get-spec, get-template)

3. **Updated All Examples**
   - STEP 3: Protocol parameters (removed get-template, get-spec examples)
   - Classification Example: Now uses domain-specific names
   - CLI Implementation Checklist: Removed hardcoded commands, added naming guidance

**Key Principle Now Enforced**:
```
❌ DON'T: Use generic/hardcoded names (get-spec, get-template, validate)
✅ DO: Extract domain-specific names from protocol terminology
```

**Real Project Alignment**:
- Spec-Kit: `specify`, `plan`, `implement` ✅
- OpenSpec: `proposal`, `apply`, `archive` ✅
- MetaSpec: `specify`, `clarify`, `plan` ✅
- No project uses: `get-template`, `get-spec` ✅

**Impact**: 
- Eliminates "template套用" anti-pattern
- Ensures domain-appropriate naming
- Aligns with all real-world projects
- Better developer experience with familiar domain terms

#### Combined Impact - Complete Command Architecture

**Slash Commands** (Protocol-Driven) + **CLI Commands** (Purpose-Driven) = Complete toolkit architecture

**Before** ❌:
- Generic templates (init, validate, generate)
- No methodology for command derivation
- Confusion between CLI and Slash Commands

**After** ✅:
- Protocol-derived Slash Commands (from workflow, entities, validation rules)
- Purpose-derived CLI Commands (from toolkit type)
- Clear separation and derivation methodology

**Example - MCP-Speckit**:
```
Slash Commands (from MCP protocol):
  /mcpspeckit.define-requirements  ← From protocol workflow
  /mcpspeckit.create-design        ← From protocol entities
  /mcpspeckit.generate-code        ← From protocol operations

CLI Commands (from toolkit purpose):
  mcpspeckit validate <file>       ← Toolkit = Validator
  mcpspeckit get-spec [section]    ← Toolkit = Query Tool
  mcpspeckit init [project]        ← Toolkit = Generator
```

### 📚 Documentation
- **Added `.metaspec/README.md`** for generated speckits:
  - Comprehensive developer guide for speckit maintainers
  - Explains 16 MetaSpec commands (SDS, SDD, Evolution layers)
  - Complete development workflow with examples
  - Iteration support documentation
  - Clear audience separation: root docs for users, `.metaspec/` for developers
- **Updated root `AGENTS.md`** template:
  - Added "For Speckit Developers" section
  - Points developers to `.metaspec/README.md` for development guidance

### 🔧 Internal
- Updated generator to include `.metaspec/README.md` in all generated speckits

## [0.1.4] - 2025-11-05

### ✨ New Features - Phase 1: Complete Iteration-Aware Design
- **All Validation/Analysis Commands** now support iterative refinement:
  - `/metaspec.sds.checklist` - Protocol quality validation with iteration tracking
  - `/metaspec.sds.analyze` - Protocol consistency analysis with progress comparison
  - `/metaspec.sds.clarify` - Protocol ambiguity resolution with resolved item tracking
  - `/metaspec.sdd.checklist` - Toolkit quality validation with iteration tracking
  - `/metaspec.sdd.analyze` - Toolkit consistency analysis with progress comparison
  - `/metaspec.sdd.clarify` - Toolkit ambiguity resolution with resolved item tracking

**Unified Iteration Support**:
  - Checks for existing output before generating
  - Three modes: `update` (default), `new`, `append`
  - Preserves history and evidence in update mode
  - Adds iteration tracking: "Iteration N: [Date]"
  - Default interpretation: "re-run" → "update", not "regenerate"
  - Before/after comparison with improvement percentage
  - Progress tracking: issues resolved, still open, newly found

### 📋 Constitution
- **Principle #6: Iteration-Aware Design**: Added new core principle
  - Commands must check if output already exists
  - Support update/append modes, not just create
  - Preserve history and track progress across iterations
  - Rationale: Spec-driven development is iterative, not one-time

### 🔧 Configuration
- **Git Tracking**: Added `memory/constitution.md` to version control
  - Updated `.gitignore` to allow core memory config files
  - Constitution now properly versioned and tracked

### 📚 Documentation
- **Decision Guide**: Added comprehensive guides to clarify layer usage
  - `docs/evolution-guide.md` - Complete decision matrix
  - `docs/iteration-layers.md` - Visual workflow diagrams
  - `docs/iteration-roadmap.md` - Planning for Phase 1 implementation
  - Clarifies when to use Evolution (formal) vs Direct Edit (fast iteration)
  - Explains Command Layer (validation) vs Evolution Layer (modification)
  - Prevents confusion between `/metaspec.proposal` and direct spec editing
- **Command Templates**: Updated with clear scope definitions
  - `checklist.md.j2`: Explicitly states it never modifies spec.md
  - `proposal.md.j2`: Includes decision guide for when to use Evolution
  - Cross-references to decision guide documentation
- **AGENTS.md**: Added comprehensive "Using Commands with Iteration Support" section
  - Iteration modes explained (update/new/append)
  - Default interpretation rules ("re-run" → update mode)
  - Complete workflow example with before/after comparison
  - Best practices for AI agents
  - Evolution Layer vs Command Layer clarification
- **README.md**: Updated with iteration-aware design features
  - Added Iteration-Aware Design to key features
  - Added links to decision guides in Documentation section

## [0.1.3] - 2025-11-05

### ✨ New Features
- **SDS Commands**: Added `/metaspec.sds.checklist` command for protocol quality validation
  - Generates systematic quality checklists for protocol specifications
  - Validates entity definitions, operations, validation rules, error handling
  - Complements `/metaspec.sds.analyze` with human review framework
  - Aligns with GitHub spec-kit best practices

### 📚 Documentation
- **Command Count**: Updated from 15 to 16 commands (5 SDS + 8 SDD + 3 Evolution)
- **Complete Update**: All documentation reflects new command structure
  - README.md, AGENTS.md, quickstart.md, architecture.md
  - Template documentation and examples

### 🐛 Bug Fixes
- **Template Files**: Fixed `.gitignore` to include `src/metaspec/templates/base/specs/`
  - Changed `specs/` to `/specs/` to only ignore root directory
  - Template files now properly included in distribution

### 🎯 Improvements
- **SDS/SDD Symmetry**: Better alignment between protocol and toolkit workflows
- **Quality Assurance**: Comprehensive quality validation for both SDS and SDD layers

## [0.1.2] - 2025-11-04

### 📚 Documentation
- **Package Name Clarification**: Documented the intentional naming convention
  - PyPI package: `meta-spec` (with hyphen, follows Python convention)
  - Import name: `metaspec` (no hyphen, Python identifier)
  - CLI command: `metaspec` (no hyphen, for convenience)
  - This is standard practice in Python ecosystem (e.g., `scikit-learn` → `sklearn`)

### 🐛 Bug Fixes
- Fixed namespace package issue by adding proper `__init__.py`
- Made CLI option tests resilient to output format differences
- Resolved test failures in CI environment

## [0.1.1] - 2025-11-04

### 📚 Documentation

#### Improved
- **Installation Guide**: Simplified installation instructions (reduced by ~70%)
  - Replace `git clone` workflow with direct `pip install git+https://...`
  - Prioritize `uv` for 10-100x faster installation
  - Add collapsible sections for alternative methods
- **Documentation Quality**: Streamlined quickstart guide
  - Cleaner examples and workflows
  - Removed redundant content
  - Better organized sections

#### Changed
- **Installation Recommendation**: `uv pip install` as primary method
- **Documentation Length**: Reduced from ~350 to ~155 lines in quickstart.md
- **User Experience**: Faster time-to-start (5 minutes or less)

### 🧪 Quality & Testing (2025-11-03)

#### Added
- **Test Suite**: Comprehensive unit test coverage (138 tests, 100% passing)
  - `models.py`: 99.13% coverage ✅
  - `generator.py`: 95.88% coverage ✅
  - `registry.py`: 94.51% coverage ✅
  - `cli/search.py`: 98.63% coverage ✅
  - Overall project: 69.22% coverage (core modules >90%)

#### Improved
- **Code Quality**: Fixed all Ruff and MyPy errors
- **Type Safety**: Complete type annotations in all modules
- **Translation**: All Chinese content translated to English
- **Build System**: Migrated to `uv` for faster dependency management
- **Templates**: Synchronized with latest OpenSpec and spec-kit templates

#### Changed
- **Coverage Target**: Set to 69% (pragmatic for CLI-heavy project)
- **Removed**: `py.typed` file (CLI tool, not a library)

### 🎯 Major Refactoring - Minimal Viable Abstraction

This release represents a fundamental architectural simplification, aligning with MetaSpec's core philosophy: **Do One Thing Well**.

### Changed - Breaking Changes ⚠️

#### Removed Local Registration System
- **Removed**: `~/.metaspec/registry.json` local registration database
- **Removed**: `metaspec register <command>` local registration
- **Removed**: `metaspec register --unregister` local unregistration
- **Rationale**: Local registration provided minimal value (only for display in `--list`) and added unnecessary complexity. Users can directly use installed speckits without registration.

#### Removed `metaspec spec` Command
- **Removed**: `metaspec spec <name> <command>` unified interface
- **Removed**: `metaspec spec --list` listing command
- **Rationale**: MetaSpec is a **generator**, not a **runtime**. Generated speckits are independent CLI tools and should be used directly. This eliminates an unnecessary abstraction layer.

**Migration Guide**:
```bash
# Old (v0.1.0)
metaspec register my-speckit
metaspec spec my-speckit validate spec.yaml

# New (v0.2.0)
metaspec install my-speckit  # or: pip install my-speckit
my-speckit validate spec.yaml  # Direct usage!
```

### Added

#### Simplified Community Commands
- **Added**: `metaspec search <query>` - Search community speckits
- **Added**: `metaspec install <name>` - Install from community registry
- **Added**: `metaspec contribute <name>` - Generate metadata for community contribution

#### Information Commands
- **Added**: `metaspec list` - List installed speckits (auto-scans PATH)
- **Added**: `metaspec info <name>` - Show detailed speckit information

### Improved

#### Cleaner Architecture
- **Simplified**: Core module `src/metaspec/community.py` (previously `registry.py`)
- **Removed**: 500+ lines of local registration code
- **Unified**: Community features in dedicated CLI module
- **Clearer**: Separation between generation (`metaspec init`) and discovery (`metaspec search/install`)

#### Better User Experience
- **Intuitive**: Users directly use installed speckits (e.g., `api-speckit validate`)
- **No confusion**: No need to understand "registration" concept
- **Standard workflow**: Follows `pip install` → `use` pattern

#### Documentation Updates
- **Updated**: README.md with new command structure
- **Updated**: AGENTS.md with simplified CLI reference
- **Rewritten**: docs/community-registry.md with clear workflows
- **Clarified**: MetaSpec is a generator, not a runtime

### Technical Details

#### File Changes
- **Deleted**: `src/metaspec/cli/spec.py`
- **Deleted**: `src/metaspec/cli/register.py`
- **Deleted**: `src/metaspec/registry.py`
- **Created**: `src/metaspec/community.py`
- **Created**: `src/metaspec/cli/community_commands.py`
- **Created**: `src/metaspec/cli/info_commands.py`
- **Modified**: `src/metaspec/cli/main.py`

#### New Module Structure
```
src/metaspec/
├── community.py          # Community registry client (social)
├── cli/
│   ├── main.py           # CLI entry point
│   ├── init.py          # Speckit generation
│   ├── community_commands.py   # search/install/publish
│   └── info_commands.py        # list/info
```

### Design Principles

This refactoring embodies MetaSpec's core principles:

1. **Minimal Viable Abstraction** - Remove unnecessary layers
2. **Do One Thing Well** - MetaSpec generates speckits, pip manages packages
3. **Unix Philosophy** - Each tool has a clear purpose
4. **Progressive Enhancement** - Start simple, grow when needed

### Why This Matters

**Before**: Confusing dual-layer system
```
pip install → metaspec register → metaspec spec speckit cmd
```

**After**: Clear, intuitive workflow
```
metaspec search → metaspec install → speckit cmd
# or: pip install → speckit cmd
```

**Key Benefits**:
- ✅ **Simpler**: Fewer commands, clearer purpose
- ✅ **Faster**: No intermediate layer
- ✅ **Standard**: Follows Python packaging conventions
- ✅ **Maintainable**: Less code, fewer bugs

---

## [0.1.0] - 2025-01-XX

### Added
- Initial release
- `metaspec init` command for generating speckits
- `metaspec spec` unified interface (deprecated in 0.2.0)
- `metaspec register` local registration (deprecated in 0.2.0)
- Community registry integration
- MetaSpec workflow commands (16 commands: 5 SDS + 8 SDD + 3 Evolution)
- Generic and dev templates
- AGENTS.md for AI assistant guidance

### Known Issues
- Over-abstraction with local registry
- Confusing command structure
- Fixed in v0.2.0

---

## Links

- **Repository**: https://github.com/ACNet-AI/MetaSpec
- **Community**: https://github.com/ACNet-AI/awesome-spec-kits
- **Discussions**: https://github.com/ACNet-AI/MetaSpec/discussions

