# Changelog

All notable changes to MetaSpec will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### 🎯 Speckit Metadata Support in pyproject.toml

**Feature**: Enable community discovery of speckit capabilities through standardized metadata  
**Status**: ✅ Implemented

#### Changes

**1. Added [tool.metaspec] Section to Generated Speckits**

New metadata fields in `pyproject.toml`:
```toml
[tool.metaspec]
generated_by = "0.9.5"        # MetaSpec version (required)
domain = "marketing"           # Toolkit domain (required)
lifecycle = "greenfield"       # Optional: omit for non-dev domains
sd_type = "sdd"               # Command system type (updated during impl)

[[tool.metaspec.slash_commands]]
name = "specify"
description = "Create specification"
source = "sdd/spec-kit"
```

**Purpose**: 
- Community tools can discover speckit capabilities
- Enable speckit registry and search
- Support compatibility checking

**2. Two-Phase Implementation Model**

**Phase 1: Initialization** (`metaspec init`)
- `pyproject.toml.j2` provides base framework
- `sd_type = "tbd"` or `"none"` (placeholder)
- `slash_commands` section commented out
- Simplified: No complex Jinja2 auto-detection logic

**Phase 2: Implementation** (`/metaspec.sdd.implement`)
- AI scans `.metaspec/commands/` for deployed commands
- Calculates `sd_type` from command sources (sds/sdd/generic/mixed)
- Populates `slash_commands` array
- Updates metadata based on actual deployment

**3. Enhanced implement.md.j2 Guidance**

Added 92 lines of Python-specific guidance:
- `pyproject.toml` structure with `[tool.metaspec]`
- `sd_type` calculation rules (scan commands → detect source → compute type)
- Auto-detection logic with examples
- Reference to comprehensive documentation

**4. Navigation Guide Corrections**

Fixed all line numbers in `implement.md.j2`:
- Main navigation table: All sections corrected (+65-67 line offset)
- Section 7 subsections: Accurate line ranges
- Token savings: Language-specific reading now 99% savings 🏆

**5. Model & Generator Updates**

- `models.py`: Added `lifecycle` field to `MetaSpecDefinition` (default: "greenfield")
- `generator.py`: Pass `lifecycle` to template context
- `init.py`: Add `lifecycle` to default preset
- `README.md.j2` & `AGENTS.md.j2`: Make `lifecycle` display optional

**6. Comprehensive Documentation**

New file: `docs/metaspec-metadata-examples.md` (255 lines)
- 5 real-world examples (Generic, SDD, Mixed SDS+SDD, SD-Marketing, Mixed sources)
- Auto-detection rules explanation
- Community use cases (registry, search, compatibility check)
- Design principles

#### Files Changed

- `src/metaspec/templates/base/pyproject.toml.j2` (+29, -10)
- `src/metaspec/templates/meta/sdd/commands/implement.md.j2` (+108, -11)
- `src/metaspec/models.py` (+3)
- `src/metaspec/generator.py` (+1)
- `src/metaspec/cli/init.py` (+1)
- `src/metaspec/templates/base/{README,AGENTS}.md.j2` (+6, -2)
- `docs/metaspec-metadata-examples.md` (+255, new)

**Total**: +403 lines, -23 lines

#### Benefits

1. **Community Discovery**: Standardized metadata format for registry tools
2. **Accurate Metadata**: Based on actual deployment, not initial guesses
3. **Flexible**: Works for dev and non-dev domains (lifecycle optional)
4. **Maintainable**: Calculation logic centralized in `implement.md.j2`
5. **Token Efficient**: Enhanced navigation with 99% savings for language-specific reading

---

## [0.9.5] - 2025-11-19

### 🔧 Documentation Optimization & Logical Consistency

**Issue**: After v0.9.4 introduced "Generator vs AI Commands" separation, the documentation still contained logical contradictions and redundancy  
**Severity**: MEDIUM (Documentation quality)  
**Status**: ✅ Resolved

#### 🎯 Changes

**1. Resolved Critical Logical Contradictions in specify.md.j2**

**Contradiction 1**: init Command Standard vs Generator Pattern
- ❌ **Before**: Line 745-746 required creating `{initial-spec-file}` (actual spec template)
- ✅ **After**: Now requires creating `specs/README.md` (workflow guidance only)
- **Impact**: Aligns with v0.9.4's "AI-First" philosophy

**Contradiction 2**: MetaSpec Self-Reference Misleading
- ❌ **Before**: Example showed MetaSpec creating `001-meta-spec/spec.md`
- ✅ **After**: Correctly shows creating `.metaspec/commands/` and `specs/README.md`
- **Impact**: MetaSpec's own behavior now matches documentation

**Contradiction 3**: Use Case Example Misleading
- ❌ **Before**: "AI-Driven Content Generation" implied AI content = Generator's job
- ✅ **After**: "Generate project structure" correctly shows infrastructure setup
- **Impact**: Clear role separation between Generator and AI Commands

**2. Removed 334 Lines of Redundancy (-9.2%)**

Removed duplicate content across documentation:

**specify.md.j2** (295 lines removed):
- init Command Standard details (150+ lines duplicated 3 times)
- Generator Pattern explanations (redundant sections)
- Verification Checklist (192 lines → 25 lines template reference)
- CLI vs Slash Command distinctions (repeated 4+ times)

**README.md** (39 lines removed):
- Duplicate core features (already in Key Features section)
- Duplicate quality metrics (already in badges)
- Historical updates (belong in CHANGELOG)
- Outdated version info

**Token Savings**:
- Verification Checklist: 192 lines → 25 lines = **86.9% savings** 🏆
- README Status: 44 lines → 5 lines = **88.6% savings** 🏆
- Overall: 3618 lines → 3284 lines = **9.2% reduction**
- Updated token savings: 84-98% → **84-99%**

**3. Synchronized Related Documentation**

**plan.md.j2**: Updated project structure example
- ❌ **Before**: Showed `spec-template.yaml` in templates
- ✅ **After**: Shows `specs-readme.md.j2` (correct infrastructure template)

**constitution.md.j2**: Clarified template reference
- Added explicit note: `spec-template.md.j2` is MetaSpec's own toolkit spec template, NOT user project spec template

**4. Updated Navigation Guides**

Updated line numbers and section sizes in:
- `specify.md.j2` (comprehensive update)
- `plan.md.j2` (project structure changes)
- `implement.md.j2` (line number sync)

**5. README Status Section Optimization**

Removed redundant Status section (44 lines → 5 lines):
- ❌ **Removed**: Duplicate core features (already in Key Features section)
- ❌ **Removed**: Duplicate quality metrics (already in badges)
- ❌ **Removed**: Historical updates (belong in CHANGELOG)
- ❌ **Removed**: Outdated version info (v0.9.4 → v0.9.5)
- ✅ **Simplified**: Clean "Release Notes" section with CHANGELOG reference

**Impact**: Improved README readability and maintainability

#### 📊 Summary

| Metric | Before | After | Improvement |
|--------|--------|-------|-------------|
| specify.md.j2 size | 3574 lines | 3279 lines | -295 lines (-8.3%) |
| README Status section | 44 lines | 5 lines | -39 lines (-88.6%) |
| Total optimization | 3618 lines | 3284 lines | -334 lines (-9.2%) |
| Logical contradictions | 3 critical | 0 | ✅ Resolved |
| Token savings (max) | 84-98% | 84-99% | +1% |
| Documentation alignment | Partial | ✅ Complete | Full v0.9.4 alignment |

#### 🎓 Lessons Learned

1. **Incremental fixes need holistic review**: v0.9.4 added "Generator vs AI Commands" but left old contradictory text
2. **External validation is valuable**: marketing-spec-kit analysis revealed critical contradictions
3. **Navigation guides are living documents**: Must update when content changes
4. **Single source of truth**: Status information should live in badges and CHANGELOG, not duplicated in Status sections

---

## [0.9.4] - 2025-11-19

### 🎯 Generator vs AI Commands: Role Separation

**Issue**: Generator Pattern documentation inconsistent with MetaSpec implementation  
**Severity**: MEDIUM-HIGH (Architecture principle)  
**Source**: marketing-spec-kit implementation feedback  
**Status**: ✅ Resolved

#### 🚨 Problem

MetaSpec v0.9.3's `/metaspec.sdd.specify` documentation required `spec-template.{format}.j2`, but MetaSpec's **own implementation** only generates `specs/README.md`. This created a fundamental misunderstanding about Generator's role.

**Core Contradiction**:
- 📄 **Doc claimed**: Generate `spec-template.{format}.j2` (empty template for users to fill)
- 💻 **MetaSpec does**: Only generates `specs/README.md` (guidance document)
- 🤖 **Actual workflow**: Specifications generated by AI + slash commands

**Design Philosophy Conflict**:
- ❌ **Template-First** (doc suggested): Pre-generate empty templates, users fill manually
- ✅ **AI-First** (actual design): AI generates specs through interactive dialogue

#### 🔧 Implemented Fixes

**Fix 1: Added "Generator vs AI Commands: Role Separation" Section** (Line 2220-2316)

New comprehensive explanation clarifying:
- **Generator's Role**: Set up project infrastructure (NOT generate specifications)
- **AI Commands' Role**: Generate specifications through interactive dialogue
- **Why This Separation**: Flexibility, intelligence, quality, true spec-driven
- **Workflow Comparison**: Template-First (wrong) vs AI-First (correct)
- **Real-World Example**: MetaSpec itself uses AI generation, not templates

**Fix 2: Updated Required Templates** (Line 2666-2680)

**Before**:
```markdown
- `spec-template.md.j2` - Specification template
```

**After**:
```markdown
- `specs-readme.md.j2` - specs/ directory guidance template ⭐ CRITICAL
  - Target: specs/README.md (NOT spec-template)
  - Content: Explains how to use slash commands
  - Purpose: Guide users to AI-driven specification generation

- Anti-Pattern - Do NOT Create ❌:
  - ❌ spec-template.{format}.j2
  - ❌ example-spec.{format}.j2
  - Reason: Specs generated by AI, not pre-templated
```

**Fix 3: Updated Generation Targets** (Line 2571-2592)

Changed from "Project files" to "Project infrastructure only":
- ✅ Added: `specs/README.md` (guidance, not template)
- ❌ Removed: Specification files rendering
- ❌ Added anti-pattern section: Don't generate spec templates

**Fix 4: Updated Example Code** (Line 2670-2697)

Added `_select_templates()` method example showing:
- Only 4 infrastructure templates
- `specs/README.md` (guidance, NOT template)
- Explicit note: No spec-template or example-spec

**Fix 5: Added Generator Scope Verification** (Line 2819-2865)

New verification checklist:
- 7 verification checks (infrastructure vs specifications)
- Verification code with assertions
- Common anti-patterns to avoid
- Correct pattern guidance

#### 📊 Impact

**Architecture Clarity**:
- ✅ Clear separation: Generator (infrastructure) vs AI (specifications)
- ✅ Aligned with MetaSpec's own implementation
- ✅ Embraces AI-First design philosophy

**Documentation Quality**:
- ✅ Removed misleading `spec-template` requirement
- ✅ Added comprehensive role separation explanation
- ✅ Real-world example (MetaSpec itself)
- ✅ Explicit anti-patterns

**Implementation Correctness**:
- ✅ Future toolkits won't pre-generate empty templates
- ✅ Users guided to AI-driven spec generation
- ✅ Better UX (dialogue vs form-filling)

#### 🔄 Migration Path

**For existing toolkits** (like marketing-spec-kit):

1. **Remove anti-patterns**:
   - Delete `spec-template.{format}.j2`
   - Delete `example-spec.{format}.j2`

2. **Add guidance**:
   - Create `specs-readme.md.j2` (based on MetaSpec's template)
   - Update Generator to only create infrastructure

3. **Verify**:
   - Run new "Generator Scope Verification" checklist
   - Ensure `specs/` only contains `README.md` after init

**For new toolkits**:
- Follow updated `/metaspec.sdd.specify` guidance
- Generator creates infrastructure only
- Rely on AI + slash commands for spec generation

#### 📚 Related Documentation

- MetaSpec's Generator: `src/metaspec/generator.py` (Line 233)
- MetaSpec's template: `templates/base/specs/README.md.j2`
- Design philosophy: AI-First, not Template-First

---

## [0.9.3] - 2025-11-19

### 📋 Slash Commands Deployment Documentation Fix

**Issue**: Generator Pattern documentation incomplete regarding slash commands deployment  
**Severity**: MEDIUM (Documentation completeness)  
**Source**: marketing-spec-kit implementation feedback  
**Status**: ✅ Resolved

#### 🚨 Problem

MetaSpec v0.9.2's `/metaspec.sdd.specify` command had incomplete documentation on deploying slash commands to user projects. The phrase "Generate custom slash commands (if specified)" was misleading, causing implementers to miss this critical step.

**Consequences**:
- Implementers didn't deploy slash commands to user projects
- User projects lacked `.{toolkit}/commands/` directory
- AI assistants couldn't access operational guides
- Core AI-driven workflow value was lost

#### 🔧 Implemented Fixes

**Fix 1: Updated Generation Targets** (Line 2473-2483)

**Before**:
```markdown
- **Commands**: Generate custom slash commands (if specified)
```

**After**:
```markdown
- **Slash Commands**: Deploy toolkit's slash commands to `.{toolkit}/commands/`
  - ✅ Always deploy all slash command files (*.md)
  - ✅ Target location: `.{toolkit}/commands/` in user projects
  - ✅ Purpose: AI assistant operational guides
  - ✅ Method: Direct file copy (NOT Jinja2 rendering)
  - ⚠️ Not optional - Critical for AI-driven workflows
```

**Fix 2: Added Command Deployment Implementation** (Line 2527-2559)

Added detailed `_deploy_slash_commands()` method with:
- Clear docstring explaining purpose
- Source/target directory specification
- Direct file copy approach (not rendering)
- Graceful handling when no commands exist

**Fix 3: Added Slash Commands Deployment Checklist** (Line 2645-2666)

New verification table checking:
- Commands deployed correctly
- File format preserved
- AI accessibility
- Proper timing (during init)

**Fix 4: Updated Required Templates List** (Line 2565-2576)

Added "Required Command Deployment" section specifying:
- Source/target paths
- Deployment method
- Purpose clarification
- Timing requirements

#### 📊 Impact

**Documentation Quality**:
- ✅ Clear guidance on slash commands deployment
- ✅ Complete code examples with `_deploy_slash_commands()`
- ✅ Verification checklist for implementers
- ✅ Aligned with MetaSpec's own implementation

**Implementation Correctness**:
- ✅ Future toolkits will correctly deploy commands
- ✅ AI-driven workflows will work out-of-the-box
- ✅ Consistent with MetaSpec architecture patterns

#### 🔄 Migration Path

**For existing toolkits** (like marketing-spec-kit):

1. **Add command deployment logic** to Generator:
   ```python
   def _deploy_slash_commands(self, output_dir: Path) -> None:
       # Copy from templates/{source}/commands/ to .{toolkit}/commands/
   ```

2. **Update project structure** description in spec.md
3. **Verify** using new checklist
4. **Re-release** toolkit with fix

**For new toolkits**:
- Follow updated `/metaspec.sdd.specify` guidance
- Run verification checklist
- Commands will deploy automatically

#### 📚 Related Documentation

- Generator implementation: `src/metaspec/generator.py` (Line 310, 328, 342)
- Base AGENTS.md: Documents `.metaspec/commands/` purpose

---

## [0.9.2] - 2025-11-18

### 🎯 Toolkit Type Detection & Simplified Generator Pattern

**Proposal ID**: PROP-2025-11-18-TOOLKIT-TYPE-DETECTION  
**Date**: 2025-11-18  
**Status**: ✅ Implemented  
**Severity**: HIGH (Architecture-level)  
**Source**: Continued Generator pattern misinterpretation analysis  
**Related**: v0.9.1 (complete solution)

#### 🚨 Critical Insight

**MetaSpec only generates Specification Toolkits, not Domain Applications.**

The previous v0.9.1 fix added guidance but did not remove the conceptual confusion introduced by "Domain Application" examples in `specify.md.j2`. This led to continued misunderstandings about Generator's purpose.

**Key realization**:
```
MetaSpec Architecture:
  Layer 1: MetaSpec → Generates Specification Toolkits
  Layer 2: Specification Toolkit → Manages specifications (parse, validate, init)
  Layer 3: Domain Application → Consumes specs, generates domain content (OUTSIDE MetaSpec scope)
```

**Domain Applications** (content generators, doc builders, SDK generators) are **NOT generated by MetaSpec** - they are separate applications built by users that consume specifications.

#### 🔧 Implemented Fixes

**Fix 1: Simplified Step 4.5 - Removed "Domain Application" Concept** (`specify.md.j2`)

**Before** (v0.9.1):
```markdown
### Step 4.5: Determine Toolkit Type (CRITICAL for Generator)

Decision Tree:
  Question 1: MANAGE specifications? → SPECIFICATION TOOLKIT
  Question 2: CONSUME specifications? → DOMAIN APPLICATION

Classification Examples:
  - marketing-spec-kit → SPECIFICATION TOOLKIT
  - api-doc-generator → DOMAIN APPLICATION ❌

Choose template based on classification:
  - Option A: For Specification Toolkits
  - Option B: For Domain Applications
```

**After** (v0.9.2):
```markdown
### Step 4.5: Understand Generator's Purpose in Spec Toolkits

CRITICAL: All toolkits generated by MetaSpec are Specification Toolkits.

Generator should create:
  ✅ Project structure (dirs, constitution, README)
  ✅ Specification templates (.yaml/.json)
  ❌ NOT domain content (posts, docs, code)

Real Example: marketing-spec-kit
  ✅ Generate: Project structure, spec templates
  ❌ Do NOT generate: Marketing posts, blog articles
  (Those belong in separate "marketing-content-generator" app)
```

**Changes**:
- Removed "Domain Application" decision tree (Question 2)
- Removed "Domain Application Indicators" table
- Removed "api-doc-generator" example (not a spec toolkit)
- Removed classification logic (no longer needed)
- Clarified "content generation" means project files, not domain deliverables
- Deleted 190 lines of confusing content
- Replaced with 62 lines of focused guidance

**Fix 2: Unified Generator Template - Removed Option B** (`specify.md.j2`)

**Before** (v0.9.1):
```markdown
### Step 5: Define Generator Component (if CORE)

⚠️ CRITICAL: Choose the correct template based on your toolkit type

#### Option A: For Specification Toolkits
  (Project file generation template)

#### Option B: For Domain Applications
  (Domain content generation template)
```

**After** (v0.9.2):
```markdown
### Step 5: Define Generator Component (if CORE)

Use this template for your Specification Toolkit

(Single unified template for project file generation)
```

**Changes**:
- Removed Option A/B distinction
- Removed entire "Option B: For Domain Applications" section (115 lines)
- Simplified to single template
- All generated toolkits now have consistent Generator architecture

**Fix 3: Added Post-Generation Verification Checklist** (`specify.md.j2`)

**New Section**: Step 5d - Post-Generation Verification

```markdown
#### Step 5d: Post-Generation Verification ⭐ NEW

Verify Generator aligns with MetaSpec standards:

✅ Generator Purpose Checklist:
  - What does Generator create? Project files ✅ / Domain content ❌
  - init command argument? <project-directory> ✅ / <spec-file> ❌
  - init command output? Full project structure ✅ / Single file ❌

📋 Specific Validation Rules:
  Rule 1: Generator Purpose (correct examples / wrong examples)
  Rule 2: Generation Targets (project files / domain content)
  Rule 3: init Command Pattern (directory arg / file arg)
  Rule 4: CLI Integration (init creates project / generate creates content)

🎯 Decision Matrix:
  Does Generator create project directories? YES ✅ / NO ⚠️
  Does Generator create domain content? NO ✅ / YES ❌

🚨 Red Flags:
  - Generation Targets include: "posts", "articles", "emails"
  - CLI example shows: `generate post`, `create content`
  - Templates include: `post.j2`, `article.j2`

✅ Verification Actions:
  1-5. Review checklist items
  6. Run `/metaspec.sdd.analyze` for automated validation
```

**Changes**:
- Added 122 lines of comprehensive verification guidance
- Provides concrete red flags to catch mistakes immediately
- Links to automated validation via `/metaspec.sdd.analyze`

#### 📊 Implementation Results

**File Changes**:
- `src/metaspec/templates/meta/sdd/commands/specify.md.j2`
  - Lines: 3587 → 3461 (-126 lines net)
  - Deleted Domain Application content: ~250 lines
  - Added verification checklist: +122 lines
  - Simplified architecture guidance

**Architecture Impact**:
- ✅ Eliminates conceptual confusion about MetaSpec's scope
- ✅ Single clear pattern: All toolkits are Specification Toolkits
- ✅ Generator always creates project files, never domain content
- ✅ Provides verification checklist to catch mistakes early
- ✅ Links to automated validation via `/metaspec.sdd.analyze`

**Quality Improvements**:
- Specification generation clarity: 📈 Significantly improved
- Generator purpose clarity: 📈 Significantly improved
- Early mistake detection: 📈 New capability (Step 5d checklist)
- Architecture consistency: 📈 Perfect alignment with MetaSpec's own implementation

#### 🧪 Test Coverage

**Not applicable**: These are guidance improvements in template content, not runtime code changes.

**Validation approach**:
- Review generated `spec.md` files from `/metaspec.sdd.specify`
- Verify Generator definitions follow project file pattern
- Confirm no domain content generation examples
- Run `/metaspec.sdd.analyze` to catch violations

#### 🚀 Migration Path

**For existing toolkit specs**:

1. **Review Generator definition** in your `specs/toolkit/001-*/spec.md`
2. **Check Generator Purpose** against Step 5d checklist
3. **If Generator creates domain content**: This is architectural misalignment
   - Option A: Redefine Generator to create project files only
   - Option B: Remove Generator, move domain generation to separate app
4. **Run `/metaspec.sdd.analyze`** to validate compliance

**For new toolkit development**:
- Follow updated `/metaspec.sdd.specify` guidance automatically
- Use Step 5d checklist before finalizing spec
- Run `/metaspec.sdd.analyze` for validation

#### 📝 Notes

**Why this matters**:

The confusion between "Specification Toolkits" and "Domain Applications" is not just semantic - it represents a fundamental misunderstanding of MetaSpec's architecture:

- **MetaSpec generates toolkits** that manage specifications
- **Domain Applications** consume specifications to generate deliverables
- These are **two different layers** in the architecture

By removing "Domain Application" from `specify.md.j2`, we eliminate the false choice and guide users toward the correct pattern: **All MetaSpec-generated toolkits are Specification Toolkits**.

**Related documentation**:
- See `AGENTS.md` Step 3.5 for init command standards
- See v0.9.0 for init command standard definition
- See v0.9.1 for Generator Pattern guidance

---

## [0.9.1] - 2025-11-18

### 🎯 Generator Pattern Clarification (Supplement to v0.9.0)

**Proposal ID**: PROP-2025-11-18-GENERATOR-PATTERN  
**Date**: 2025-11-18  
**Status**: ✅ Implemented  
**Severity**: HIGH (Architecture-level)  
**Source**: marketing-spec-kit development feedback (continued)  
**Related**: v0.9.0 fixes (supplementary fix)

#### 🚨 Critical Issue

The `/metaspec.sdd.specify` command allowed Generator components to be misinterpreted, leading to architectures where Generator creates **domain content** (posts, articles, emails) instead of **project files** (specs, constitution, commands).

**Example from marketing-spec-kit**:
```markdown
### Component: Generator ❌ WRONG
Purpose: Generate marketing content from validated specifications
Features:
- Generate social media posts
- Generate blog articles  
- Generate email campaigns
```

**MetaSpec's own implementation** (generator.py):
```python
"""Generate complete speckit projects from meta-spec definitions."""
# ✅ Generates project files (constitution.md, specs/, README.md)
# ❌ Does NOT generate domain content
```

#### 🎯 Root Cause

**Pattern Confusion**: Toolkit vs Domain Application

```
Specification Toolkit (marketing-spec-kit)
  ├─ Generator → Project files ✅
  └─ Wrong: Domain content ❌

Domain Application (user's marketing app)
  ├─ Generator → Marketing content ✅
  └─ Uses specifications from toolkit
```

**Key Insight**: When Use Case says "AI-Driven Content Generation":
- ❌ Wrong interpretation: Generate domain deliverables (posts, articles)
- ✅ Correct interpretation: Generate project files and specifications

#### ✅ Implemented Fixes

| Fix | Content | Location | Status |
|-----|---------|----------|--------|
| **Fix 1** | Generator Pattern guidance | `/metaspec.sdd.specify` Component 5 | ✅ Done |
| **Fix 2** | Generator Pattern validation | `/metaspec.sdd.analyze` Dimension L | ✅ Done |

#### 📝 Fix 1: Generator Pattern Guidance (`specify.md.j2`)

**Added Section**: "Generator Pattern - Toolkit vs Domain Tool" (line 2196+)

**Key Content**:
- ✅ CORRECT: Generate project files (specs, constitution, commands, templates)
- ❌ FORBIDDEN: Generate domain content (posts, articles, emails, marketing content)
- Visual diagram showing toolkit vs domain application separation
- Reference to MetaSpec's own generator.py implementation
- Correct/incorrect template examples
- Correct/incorrect CLI command examples

**Impact**: Prevents the #1 architectural mistake in toolkit development

#### 🔍 Fix 2: Generator Pattern Validation (`analyze.md.j2`)

**Added Dimension**: L. Generator Pattern Compliance (line 813+)

**Three Validation Checks**:

**L1: Generator Purpose Validation** (CRITICAL)
- Detects domain content keywords (posts, articles, emails, marketing content)
- Verifies toolkit keywords (project files, specification structure)
- Reports CRITICAL error if domain pattern detected

**L2: Template Pattern Validation** (HIGH)
- Detects domain templates (post.j2, article.j2, email.j2)
- Verifies toolkit templates (constitution.j2, spec.yaml.j2)
- Reports HIGH error if domain templates detected

**L3: CLI Command Pattern Validation** (HIGH)
- Detects domain commands (generate post, generate article)
- Verifies toolkit commands (init <project-dir>, generate spec)
- Reports HIGH error if domain commands detected

**Example Report**:
```
❌ CRITICAL: Generator follows domain content pattern [GEN_PATTERN_001]
  Detected: "social media post", "blog article", "email campaign"
  
  Current: "Generate marketing content from specifications"
  Expected: "Generate project structure and specification files"
  
  Fix Strategy:
    1. Update Purpose: FROM "Generate marketing content" 
                       TO "Generate project files"
    2. Update Features: FROM "Generate posts/articles/emails"
                        TO "Generate specs/constitution/commands"
    3. Update Templates: FROM templates/post.j2
                         TO templates/spec.yaml.j2
    4. Update CLI: FROM {toolkit} generate post
                   TO {toolkit} init <project-dir>
```

#### 📊 Implementation Results

**Code Change Statistics**:
- `specify.md.j2`: +87 lines (Generator Pattern guidance)
- `analyze.md.j2`: +290 lines (Dimension L validation)
- Total: +377 lines

**Validation Coverage**:
- ✅ Purpose & Features: Anti-pattern keyword detection
- ✅ Templates: Pattern matching for domain vs toolkit templates
- ✅ CLI Commands: Command pattern validation
- ✅ Comprehensive fix guidance with concrete examples

**Expected Impact**:
- 🎯 Prevents toolkit vs domain application confusion
- ✅ Enforces correct Generator pattern across all speckits
- 📝 Provides actionable fix guidance with error codes
- 🔍 Auto-detects 3 types of pattern violations (purpose, templates, CLI)

#### 🧪 Test Coverage

This enhancement can be validated by:
1. **Regenerate marketing-spec-kit** with v0.10.0
   - Expected: `/metaspec.sdd.specify` provides clear Generator pattern guidance
   - Expected: `/metaspec.sdd.analyze` detects incorrect Generator definition

2. **Run analyze on existing incorrect spec**
   - Create spec.md with domain content Generator
   - Run `/metaspec.sdd.analyze`
   - Expected: CRITICAL error with GEN_PATTERN_001 and fix guidance

#### 🔄 Migration Path

**Existing Users** (with incorrect Generator patterns):
- ⚠️ Run `/metaspec.sdd.analyze` to detect violations
- ⚠️ Follow fix guidance to correct Generator definition
- ⚠️ This is an architectural issue - requires manual fix

**New Users**:
- ✅ Follow new guidance in `/metaspec.sdd.specify`
- ✅ Validation automatically detects mistakes
- ✅ Clear distinction between toolkit and domain application

**For marketing-spec-kit**:
- Manual fix required (separate from MetaSpec release)
- Update spec.md Generator definition
- Rewrite generator.py to generate project files
- Update templates and CLI commands

#### 📚 Related Resources

- **Proposal**: `docs/internal/generator-pattern-clarification-proposal.md`
- **Original Feedback**: `marketing-spec-kit/docs/internal/metaspec-generator-misdefinition-feedback.md`
- **Command Template**: `src/metaspec/templates/meta/sdd/commands/specify.md.j2`
- **Validation Template**: `src/metaspec/templates/meta/sdd/commands/analyze.md.j2`

#### 🙏 Acknowledgments

This enhancement addresses a critical architectural pattern discovered during marketing-spec-kit development. It complements the v0.9.0 fixes by providing explicit guidance and validation for the Generator component pattern.

**Pattern Clarity**: The distinction between "toolkit Generator" (project files) and "domain application Generator" (business content) is now explicitly documented and automatically validated.

---

## [0.9.0] - 2025-11-17

### 🎯 `/metaspec.sdd.specify` Command Enhancement

**Proposal ID**: PROP-2024-11-17-SDD-SPECIFY  
**Date**: 2025-11-17  
**Status**: ✅ Implemented  
**Severity**: High  
**Source**: marketing-spec-kit development practice feedback  
**Migration Guide**: `docs/migration-guide-v0.9.0.md`

#### Core Issues

Based on actual `marketing-spec-kit` development, we identified **5 design flaws** in `/metaspec.sdd.specify` command:

**P0 - Must Fix**:
1. **Missing Use Case → Component logic derivation** - causes incorrect component classification
2. **Missing AGENTS.md consistency check** - init command conflicts with standards
3. **Unclear init command standards** - inconsistent behavior across toolkits

**P1 - Should Fix**:
4. **Missing Generator necessity logic** - generation-focused toolkits lack core components
5. **Missing cross-document consistency validation** - no automatic verification mechanism

#### Real-World Case

**Issues exposed by marketing-spec-kit**:
```bash
# Issue 1: Generator misclassification
Primary Use Case: "AI-Driven Content Generation"
But Generator marked as "Future Enhancement" ❌
Should be: Core Component ✅

# Issue 2: init command non-compliant
Generated definition: marketing_spec_kit init <filename> ❌
AGENTS.md standard: {toolkit} init <project-dir> ✅
```

#### ✅ Implemented Fixes

**Key Insight**: During implementation, we discovered MetaSpec already has complete validation architecture (both SDS/SDD have independent analyze commands). Final solution adopts **separation of concerns**: specify generates, analyze validates.

**Detailed Proposal**: `docs/internal/sdd-specify-enhancement-proposal.md`  
**Final Summary**: `docs/internal/v0.9.0-final-implementation-summary.md`

| Fix | Content | Implementation Location | Status |
|-----|---------|------------------------|--------|
| **Fix 1** | Use Case → Component automatic derivation | `/metaspec.sdd.specify` Step 3 (line 288-348) | ✅ Done |
| **Fix 2** | AGENTS.md consistency check | `/metaspec.sdd.specify` Component 3 (line 504-607) | ✅ Done |
| **Fix 3** | init command standard definition | `/metaspec.sdd.specify` Component 3 + AGENTS.md Step 3.5 | ✅ Done |
| **Fix 4** | Generator necessity logic | `/metaspec.sdd.specify` Component 5 (line 2191-2362) | ✅ Done |
| **Fix 5** | Framework Standards validation | `/metaspec.sdd.analyze` Dimension J ⭐ | ✅ Done |

#### ✅ Documentation Updates

| Document | Update Content | Status |
|----------|---------------|--------|
| **AGENTS.md** | Added STEP 3.5: init command standards | ✅ Done |
| **Constitution** | Part III added Principle 7: Document Consistency | ✅ Done |
| **Migration Guide** | Complete v0.8.x → v0.9.0 migration guide | ✅ Done |
| **Test Plan** | 5 regression test case documents | ✅ Done |

#### 📊 Implementation Results

**Code Change Statistics**:
- `specify.md.j2`: +540 lines (added 4 key enhancements + recommended steps)
- `analyze.md.j2`: +230 lines (added Dimension J: Framework Standards Compliance) ⭐
- `AGENTS.md`: +69 lines (added STEP 3.5: init command standards)
- `constitution.md.j2`: +20 lines (Part III Principle VII: Document Consistency)
- New documents: 5 (proposal + migration guide + test plan + clarification + summary)

**Architectural Advantages**:
- ✅ Separation of concerns: specify generates, analyze validates
- ✅ Aligns with MetaSpec design philosophy (follows SDS/SDD patterns)
- ✅ Optional user validation (not forced, non-blocking)
- ✅ Easy to extend (future validation dimensions can be added easily)

**Expected Impact**:
- 🎯 Prevents 80% of common toolkit development errors
- ✅ Ensures all generated toolkits comply with MetaSpec standards
- 📝 Provides actionable fix guidance (with error codes and specific suggestions)
- 🔍 Auto-detects 3 types of Framework Standards violations (init, components, generator)

#### 🧪 Test Coverage

Regression test plan (see `docs/internal/v0.9.0-regression-test-plan.md`):

1. **TC1**: marketing-spec-kit regeneration (original issue validation)
2. **TC2**: New generation-focused toolkit (Use Case → Component test)
3. **TC3**: New validation-focused toolkit (Generator optionality test)
4. **TC4**: AGENTS.md consistency check (error detection test)
5. **TC5**: Comprehensive consistency report (report completeness test)

**Test Status**: 📋 Test plan ready, pending manual execution

#### 🔄 Migration Path

**Existing Users**:
- ✅ Backward compatible: Existing toolkits need no modification
- ✅ Optional upgrade: Regenerate to get new validation
- ⚠️ Recommendation: New projects should use v0.9.0 immediately

**New Users**:
- ✅ Works out of box: All enhancements automatically active
- ✅ Better guidance: Detailed steps and checklists
- ✅ Error prevention: Consistency validation runs automatically

See: `docs/migration-guide-v0.9.0.md`

#### 📦 Release Checklist

- [x] Phase 1: Command template updates (5 fixes)
- [x] Phase 2: Documentation updates (AGENTS.md, Constitution)
- [x] Phase 3: Test plan preparation (5 test cases)
- [x] Phase 4: Release materials (migration guide, version numbers)
- [ ] Phase 5: Execute regression tests (manual completion needed)
- [ ] Phase 6: PyPI release

#### 📚 Related Resources

- **Proposal Document**: `docs/internal/sdd-specify-enhancement-proposal.md`
- **Original Feedback**: `marketing-spec-kit/docs/internal/metaspec-sdd-specify-feedback.md`
- **Migration Guide**: `docs/migration-guide-v0.9.0.md`
- **Test Plan**: `docs/internal/v0.9.0-regression-test-plan.md`
- **Core File**: `src/metaspec/templates/meta/sdd/commands/specify.md.j2`

#### 🙏 Acknowledgments

This enhancement is based on real feedback from `marketing-spec-kit` development process. Thanks to the issues discovered in practice for providing direction for framework improvement.

---

## [0.8.1] - 2025-11-17

### 🐛 Bugfix - Version Number Consistency

**Fix version number mismatch in v0.8.0 release**

#### Issue
v0.8.0 was uploaded to PyPI with inconsistent version numbers:
- `pyproject.toml`: 0.8.0 ✅
- `__init__.py` `__version__`: 0.7.3 ❌

This caused `import metaspec; metaspec.__version__` to return `"0.7.3"` instead of `"0.8.0"`.

#### Fix
- Updated `__init__.py` to `__version__ = "0.8.1"`
- All version references now consistent

**Note**: v0.8.0 on PyPI should not be used. Please upgrade to v0.8.1.

---

## [0.8.0] - 2025-11-17 ⚠️ DEPRECATED

**⚠️ WARNING**: This version has a bug where `__version__` returns `"0.7.3"`. Please use v0.8.1 instead.

### 🔄 Workflow Completeness Enhancement

**Date**: 2025-11-17  
**Focus**: Clarify two types of workflows and eliminate project-specific examples

#### Context

Based on community feedback, MetaSpec's workflow guidance was incomplete:
- ✅ Type 1 (Entity State Machines) was well-documented
- ❌ Type 2 (Specification Usage Workflow) lacked clear guidance
- ❌ Examples used project-specific terminology (SDM, marketing)

This caused confusion: developers didn't know what granularity of workflow to define, or where Type 2 workflows should be documented.

#### Changes

##### 1. Clarified Two Types of Workflows

**Added clear distinction throughout all documentation**:

**Type 1: Entity State Machines**
- Purpose: Entity lifecycle during business execution
- Example: Order (pending → confirmed → shipped → delivered)
- Used by: Business logic, domain operations
- Defines: Status field transitions, business rules
- Optional: Only for stateful entities

**Type 2: Specification Usage Workflow** ⭐ NEW
- Purpose: End-to-end specification creation process
- Example: SDS Workflow (Constitution → Specify → Clarify → ... → Implement)
- Used by: Users creating specifications, AI agents
- Defines: Action steps, slash commands, quality gates
- **Required**: For all Speckits

##### 2. Updated All Examples to Use MetaSpec Itself

**Before** (v0.7.x):
```yaml
# Used project-specific examples
SDM Workflow: Constitution → Discover → Strategy → Create
Marketing Operations: /marketing.project, /marketing.campaign
```

**After** (v0.8.0):
```yaml
# Uses MetaSpec's own workflows
SDS Workflow: Constitution → Specify → Clarify → Plan → ... → Implement
Specification Entity: draft → review → approved → deprecated
```

**Rationale**: MetaSpec should be self-demonstrating. Every example now uses MetaSpec's own SDS/SDD workflows, making it universally applicable without project-specific bias.

##### 3. Updated Constitution (Part II: Workflow Completeness)

**Added to `memory/constitution.md`**:
- Restructured into three parts (Part I, II, III)
- **Part II, Principle 7: Workflow Completeness**
  - Defines both workflow types clearly
  - Specifies Type 2 as REQUIRED for all speckits
  - Provides MetaSpec's own workflow as example
  - Explains the rationale (pre-v0.7.0 vs post-v0.7.0)

##### 4. Enhanced `/metaspec.sds.specify` Command

**File**: `src/metaspec/templates/meta/sds/commands/specify.md.j2`

**Changes**:
- Lines 464-568: Replaced SDM example with complete MetaSpec SDS Workflow (8 steps)
- Lines 439-445: Updated workflow type examples (SDS, SDD, SD-X instead of SDM)
- Lines 624-638: Updated comparison example using MetaSpec entities

**Example improvement**:
```markdown
# Before
Workflow: Spec-Driven Marketing (SDM)
Step 1: Constitution → Define brand principles
Step 2: Discover → Research market needs
...

# After
Workflow: SDS (Spec-Driven Specification)
Step 1: Constitution → Establish specification design principles
Step 2: Specify → Create initial specification document
Step 3: Clarify → Resolve underspecified areas
...
Step 8: Implement → Write sub-specification documents
```

##### 5. Enhanced `/metaspec.sdd.specify` Command

**File**: `src/metaspec/templates/meta/sdd/commands/specify.md.j2`

**Changes**:
- Lines 929-947: Added explicit guidance to check Domain Spec for Specification Usage Workflow
- Added key question: "What is the recommended workflow for users to create specifications using these entities?"
- Emphasized: If workflow not in Domain Spec → go back and define it first

**New guidance**:
```markdown
**First, check your Domain Specification**:
- [ ] Does it have a "Specification Usage Workflow" section?
- [ ] Does this workflow define the end-to-end process?
- [ ] Are workflow steps defined at action level (8-12 steps)?
- **If YES** → Use this workflow directly to derive commands
- **If NO** → Go back to Domain Spec and define it first
```

##### 6. Updated Domain Spec Template

**File**: `src/metaspec/templates/meta/templates/domain-spec-template.md.j2`

**Changes**:
- Lines 210-214: Updated "Key Distinction" to use MetaSpec examples
  - Type 2: SDS workflow (Constitution → Specify → Clarify → ...)
  - Type 1: Specification entity (draft → review → approved → deprecated)

##### 7. Enhanced AGENTS.md

**File**: `AGENTS.md`

**Changes**:
- Lines 127-169: Added new section "Two Types of Workflows" with clear comparison
- Lines 247-284: Updated examples to use MetaSpec SDS/SDD workflows
- Lines 290-304: Enhanced checklist to distinguish Type 1 vs Type 2 requirements

**Structure**:
```markdown
### Two Types of Workflows ⭐ UPDATED v0.8.0

#### Type 1: Entity State Machines (Business Execution)
[Clear definition and example]

#### Type 2: Specification Usage Workflow (Specification Creation) ⭐ NEW
[Clear definition and example]

**Key Distinction**: ...
**Most speckits need BOTH**: ...
```

#### Impact

**For Speckit Developers**:
- ✅ Clear understanding of two workflow types
- ✅ Know where to define each type (Domain Spec)
- ✅ Can directly map Type 2 workflow to slash commands
- ✅ Universal examples (MetaSpec) applicable to any domain

**For AI Agents**:
- ✅ Consistent examples across all documentation
- ✅ Clear Type 2 workflow → command derivation pattern
- ✅ No confusion from project-specific terminology

**For MetaSpec Itself**:
- ✅ Self-demonstrating: Uses own workflows as examples
- ✅ No maintenance burden of keeping project-specific examples updated
- ✅ Dogfooding: MetaSpec practices what it preaches

#### Files Changed

1. `src/metaspec/templates/meta/sds/commands/specify.md.j2` (+104 lines)
2. `src/metaspec/templates/meta/sdd/commands/specify.md.j2` (+17 lines)
3. `src/metaspec/templates/meta/templates/domain-spec-template.md.j2` (+3 lines)
4. `src/metaspec/templates/meta/sds/commands/constitution.md.j2` (+47 lines) ⭐ **KEY FILE**
5. `memory/constitution.md` (+184 lines, restructured)
6. `AGENTS.md` (+60 lines, restructured)

**⚠️ Note**: File #4 (`constitution.md.j2` command template) is the most critical update, as it defines Part II principles for all generated speckits.

#### Enforcement

The Workflow Completeness principle (Part II, Principle 7) ensures:
- `/metaspec.sds.constitution` includes workflow requirements
- `/metaspec.sds.specify` generates both workflow types
- `/metaspec.sds.checklist` (future) validates workflow completeness
- `/metaspec.sds.analyze` (future) scores workflow quality

#### Migration Guide

**For existing speckits**:
1. Review Domain Spec: Does it have "Specification Usage Workflow"?
2. If NO: Run `/metaspec.sds.specify` again with Type 2 workflow guidance
3. Define 8-12 action steps (Constitution → Specify → ... → Implement pattern)
4. Map each step to a slash command
5. Update Toolkit Spec to reference Domain Spec workflow

**For new speckits**:
- Start with MetaSpec's SDS workflow as template
- Adapt to your domain terminology
- Keep core phases (constitution, specify, plan, implement)
- Add/remove phases based on domain requirements

---

## [0.7.3] - 2025-11-16

### 📝 Documentation Improvement - SDS "Specification Operations" Clarification

**Prevents confusion between Specification Operations and Toolkit Commands in domain specs**

This release completes the command generation fix by clarifying the SDS (Spec-Driven Specification) side, preventing users from defining toolkit commands in domain specifications.

### Context

**Related to v0.7.2**: v0.7.2 fixed SDD (toolkit generation logic), but the root cause was in SDS where "Specification Operations" was being misused as "Toolkit Commands".

**Discovery**: Real-world usage revealed that Domain Spec's "Specification Operations" section was being used to define toolkit commands (e.g., `/marketing.project`, `/marketing.campaign`), when it should only be used for API/Protocol interface definitions.

### The Confusion

#### Two Different "Operations" Were Being Mixed:

**Type 1: Specification Operations** (SDS - Correct Usage) ✅
```yaml
# API/Protocol Specification
Operations:
  - initialize: Server startup (MCP protocol)
  - GET /users: List users (REST API)
  - tools/list: Enumerate tools (MCP operation)
```
- These are **interface definitions** that the specification defines
- Implementers must follow these interfaces
- Only for API/Protocol specifications

**Type 2: Toolkit Commands** (Should be in SDD) ❌
```yaml
# Marketing Spec-Kit (Incorrect - was in Domain Spec)
Operations:
  - /marketing.project: Access project
  - /marketing.campaign: Access campaign
```
- These are **toolkit commands** for operating data
- Should be defined in Toolkit Spec (SDD), not Domain Spec (SDS)
- Most domains don't need Specification Operations at all

### Changed

#### `/metaspec.sds.specify` Command Template

**Added Clear Usage Guidance** (Line 177-196):
- Explicit warning: "This is for API/Protocol specifications that define interfaces"
- Examples: MCP protocol operations, REST API endpoints
- Clear "When to use" vs "When NOT to use" guidance
- Key distinction between Specification Operations (SDS) and Toolkit Commands (SDD)

**Added Output Warnings** (Line 912-917):
```markdown
- Specification Operations: {count} API/protocol operations defined
  ⚠️ Note: Only for API/Protocol specs (MCP, REST API). Most domains leave this empty.
          Toolkit commands should be defined in SDD, not here!
```

### When to Define Specification Operations

**✅ Use when**:
- Your domain IS an API/Protocol specification (MCP, REST API, GraphQL, gRPC)
- You're defining interfaces that implementers must follow
- These are specification-level operations (WHAT interfaces exist)

**❌ Don't use when**:
- Your domain is NOT an API specification (Marketing, E-commerce, CRM, etc.)
- You want to define toolkit commands (use `/metaspec.sdd.specify` instead)
- You're unsure - if confused, leave empty and define commands in SDD

**Key principle**: Most domains don't need Specification Operations. This is specifically for API/Protocol specifications.

### ⚠️ Important Clarification

**This fix is ONLY about "Specification Operations"**. Domain Specs still MUST include:

✅ **Workflow Specification** (v0.7.0 requirement):
```yaml
user_workflows:
  - name: Marketing Workflow
    phases:
      - Discover: Research market needs
      - Strategy: Plan campaigns
      - Design: Create content
      - Execute: Launch campaigns
      - Analyze: Measure results
```

This describes **how users use the specification**, not API interfaces or toolkit commands.

**Summary**:
- ✅ **Keep**: Workflow Specification (describes user workflow)
- ⚠️ **Conditional**: Specification Operations (only for API specs)
- ❌ **Remove**: Toolkit Commands (belongs in SDD)

### Impact

**Before this fix**:
```
User creates Marketing domain spec
  ↓
Defines "Operations": /marketing.project, /marketing.campaign...
  ↓
SDD inherits these as commands
  ↓
Generates wrong command type ❌
```

**After this fix**:
```
User creates Marketing domain spec
  ↓
Sees: "Only for API/Protocol specs, most domains leave empty"
  ↓
Leaves Operations empty
  ↓
SDD independently designs workflow commands ✅
```

### Migration Guide

**For existing speckits with misused Specification Operations**:

1. **Check your domain type**:
   ```bash
   # Is your domain an API/Protocol spec?
   - MCP, REST API, GraphQL → Keep Specification Operations
   - Marketing, E-commerce, CRM → Remove/leave empty
   ```

2. **If NOT an API spec, clean domain spec**:
   ```bash
   # Edit: specs/domain/001-{domain}-spec/spec.md
   # Remove or set to empty:
   operations: []
   ```

3. **Verify toolkit spec has workflow commands**:
   ```bash
   # specs/toolkit/001-{name}/spec.md should have:
   Commands:
     - /domainspec.constitution
     - /domainspec.specify
     - ...workflow commands (not entity commands)
   ```

### Why This Matters

This fix completes the command generation problem by addressing both sides:
- **v0.7.2**: Fixed SDD (toolkit generation logic) - prevents generating entity commands
- **v0.7.3**: Fixed SDS (specification guidance) - prevents defining wrong operations

Together, these ensure speckits follow the correct workflow-guidance pattern from specification to implementation.

### References

- **Fix Document**: `docs/internal/sds-operations-clarification-fix.md`
- **Related Version**: v0.7.2 (fixed SDD side)
- **Discovery Source**: Real-world speckit development feedback

---

## [0.7.2] - 2025-11-16

### 🔧 Critical Bug Fix - SDD Specify Command Generation Logic

**Fixes MetaSpec generating entity commands instead of workflow commands for speckits**

This release addresses a fundamental design flaw in `/metaspec.sdd.specify` that caused it to generate entity operation commands (e.g., `/marketing.project`, `/marketing.campaign`) instead of workflow commands (e.g., `/marketingspec.discover`, `/marketingspec.strategy`) when creating new speckits.

### Context

**Issue discovered**: When using MetaSpec to generate a new speckit, the toolkit spec could incorrectly define entity operation commands (e.g., 22 entity commands), contradicting the design pattern used by both spec-kit and MetaSpec itself (which only use workflow commands).

**Root cause**: The SDD specify template contained misleading prompts that suggested generating commands from domain entities, rather than from workflow phases.

### Changed

#### `/metaspec.sdd.specify` Command Template

**Fix 1: Added "Determine Toolkit Type" Section** (NEW)
- Introduces explicit distinction between:
  - **Type A: Data-Access Toolkit** (Rare) - API clients with entity operations
  - **Type B: Workflow-Guidance Toolkit** (Speckit Standard) - Speckits with workflow commands
- Includes checkpoint to confirm Type B selection before proceeding
- Provides clear examples of both patterns
- Default: Type B (Workflow-Guidance) for speckits

**Fix 2: Modified "Entities & Structures" Prompt**
- Changed from: "Need commands to work with entities" ❌
- Changed to: "Entities are specification structures, not data objects" ✅
- Added explicit warning: "Do NOT generate entity operation commands"
- Provides anti-pattern example:
  ```
  ❌ Wrong: Domain has Project, Campaign → Generate /marketing.project
  ✅ Right: Workflow has Discover, Strategy → Generate /marketingspec.discover
  ```

**Fix 3: Strengthened "Workflows & Phases" Guidance**
- Marked as "⭐ CRITICAL FOR TYPE B"
- Added detailed workflow-to-command derivation examples using MetaSpec's own pattern
- Added domain-specific speckit example showing correct workflow command derivation
- Emphasized: "Derive workflow commands from phases, not entity commands from entities"

**Fix 4: Added "Anti-Patterns to Avoid" Section** (NEW)
- Lists 3 common mistakes:
  1. Entity-Based Commands (for Type B toolkits)
  2. Forgetting MetaSpec's Own Pattern
  3. Missing Workflow Analysis
- Includes before/after examples for each anti-pattern

### Impact

**Before this fix**:
```
/metaspec.sdd.specify
  ↓
AI sees: "Domain has 9 entities"
  ↓
AI generates: 22 entity operation commands ❌
  ↓
Result: /marketing.project, /marketing.campaign, etc.
```

**After this fix**:
```
/metaspec.sdd.specify
  ↓
AI confirms: Type B - Workflow-Guidance ✅
  ↓
AI analyzes: Workflow phases (not entities)
  ↓
AI generates: 10 workflow commands ✅
  ↓
Result: /marketingspec.discover, /marketingspec.strategy, etc.
```

### Migration Guide

**For existing speckits generated with older MetaSpec**:

If your toolkit spec contains entity operation commands instead of workflow commands:

1. **Check your current commands**:
   ```bash
   cat specs/toolkit/001-*/spec.md | grep "Component 4"
   ```

2. **If you see entity commands** (e.g., `/domain.entity`):
   - ❌ This is the old, incorrect pattern

3. **Regenerate toolkit spec**:
   ```bash
   # Backup current spec
   mv specs/toolkit/001-*/ specs/toolkit/001-*.backup/
   
   # Regenerate with fixed command
   /metaspec.sdd.specify
   
   # Verify you now have workflow commands
   cat specs/toolkit/001-*/spec.md | grep "Component 4"
   ```

4. **Expected result**: Workflow commands (e.g., `/domainspec.discover`)

**No action needed if**:
- Your toolkit already uses workflow commands
- Your toolkit was hand-crafted (not auto-generated)

### References

- **Fix Proposal**: `docs/internal/sdd-specify-fix-proposal.md`
- **Pattern Source**: MetaSpec's own command structure (dogfooding)
- **Precedent**: spec-kit uses only workflow commands

### Why This Matters

This fix ensures MetaSpec's SDD workflow correctly generates workflow-guidance toolkits (Type B) by default, aligning with its own design pattern and the broader speckit ecosystem. Without this fix, generated speckits would contradict the core philosophy of spec-driven development.

---

## [0.7.1] - 2025-11-15

### ✨ Quality Gates Enhancement - Workflow Validation

**Implemented Phase 2 of Workflow-Driven Design Philosophy**

v0.7.0 introduced Workflow Completeness principle. v0.7.1 adds automated validation to enforce it.

### Added

#### Checklist (SDS) - Category 8: Workflow Design Quality
- **Added 10 new checklist items** (CHK027-CHK036) for workflow validation
- Validates workflow specification completeness per Constitution Part II Principle 7
- Checks:
  - "Workflow Specification" section exists
  - At least 2 distinct workflow phases defined
  - Operations mapped to workflow phases
  - Entry/exit criteria specified
  - Phase transitions and dependencies documented
  - Decision points and branching logic explained
  - End-to-end workflow example provided
  - All operations referenced in at least one phase

**Location**: `/metaspec.sds.checklist` command template

**Purpose**: Catch workflow gaps during specification review phase

#### Analyze (SDS) - Dimension L: Workflow Completeness
- **Added 12th analysis dimension** (L) with 15% weight
- Severity rules:
  - **CRITICAL**: No "Workflow Specification" section (Constitution violation)
  - **HIGH**: <2 phases OR operations not mapped to phases
  - **MEDIUM**: Missing entry/exit criteria or examples
  - **LOW**: Workflow exists but could be clearer
- Score calculation: `(Checks Passed / 9) * 15%`
- Focused mode support: `/metaspec.sds.analyze workflow`

**Location**: `/metaspec.sds.analyze` command template

**Why it matters**: Prevents "high-score but no workflow" problem discovered in real-world usage

### Changed

- **Full Analysis Mode**: Now checks 12 dimensions (A-L) instead of 11
- **Focused Mode**: Added `workflow`, `workflows`, `user-journey` keywords
- **Checklist Categories**: 8 categories (was 7)
- **Total Checklist Items**: 36 items (was 26)

### Quality Impact

**Before v0.7.1**:
```
Specification passes all checks → ✅ 100%
But missing workflow definition → ❌ Users confused
```

**After v0.7.1**:
```
Specification without workflow → ❌ CRITICAL in analyze
                               → ❌ 10 failed in checklist
                               → 📉 Score < 70%
→ Forces workflow definition before high scores
```

### Backward Compatibility

✅ Fully compatible with v0.7.0
- Existing specifications with workflows: no impact
- Existing specifications without workflows: will now fail new checks (as intended)
- All other dimensions unchanged

### Migration Guide

**For existing projects**:
1. Run `/metaspec.sds.analyze workflow` to check current status
2. If missing workflow section, add via `/metaspec.sds.specify`
3. Re-run `/metaspec.sds.checklist` (update mode) to verify
4. Re-run `/metaspec.sds.analyze` for full score

**For new projects**: Workflow validation automatic with v0.7.1 templates

### Rationale

**Feedback-driven improvement**: A real-world speckit passed all quality checks (98/100) but lacked workflow definition. v0.7.1 ensures this can't happen again.

**Three-layer enforcement**:
1. **v0.7.0**: Constitution requires workflows (principle)
2. **v0.7.1**: Checklist validates workflows (quality gate)
3. **v0.7.1**: Analyze scores workflows (quantitative measure)

### References

- **Related Version**: v0.7.0 (introduced Workflow Completeness principle)
- **Philosophy**: Enforcement through automated quality gates

---

## [0.7.0] - 2025-11-15

### ⭐ Major Feature - Workflow-Driven Design Philosophy

**Introduced Workflow Completeness Principle for Domain Specifications**

MetaSpec now enforces **workflow-first design** for all domain specifications, addressing a fundamental design gap where speckits could pass all quality checks but lack clear user workflows.

**Problem We Solved**:
- Before v0.7.0: Developers created speckits with isolated operations ("toolbox")
- Users received collections of commands without knowing usage order or relationships
- High quality scores but poor usability - no end-to-end guidance
- Example: "13 commands" but unclear which to use first, how they connect

**Solution**:
- Added **Part II Principle 7: Workflow Completeness** to Constitution
- All domain specifications MUST now define complete user workflows
- Workflows include phases, operation mapping, sequencing, and examples
- MetaSpec itself demonstrates this principle with SDS/SDD workflows

### ✨ Added

#### Constitution Template Updates
- **Added Part II Principle 7**: "Workflow Completeness"
  - Requires complete user workflows from start to finish
  - Distinct phases/stages with clear purposes
  - Operation ordering and dependencies
  - Decision points and branching logic
  - End-to-end workflow examples
  - Operations mapped to workflow phases
- Example workflow structure in constitution template
- Domain-specific workflow examples (Marketing, MCP, API Testing)

#### Domain Specification Template
- **Added "Workflow Specification" section** to `domain-spec-template.md.j2`
  - `user_workflows` in frontmatter YAML
  - Workflow phases with purpose, entry/exit criteria
  - Operation-to-phase mapping
  - Workflow example usage
  - Design rationale emphasizing integrated workflows
- Positioned after "Use Cases", before "Core Entities"

#### Documentation Updates
- **AGENTS.md**: New "Workflow-Driven Design Philosophy" section
  - Explains why workflow matters (systems vs toolboxes)
  - Shows MetaSpec's own workflows as examples
  - Required workflow elements checklist
  - Good vs bad design examples
  - Enforcement mechanisms
- **Constitution Structure**: Updated to show Workflow Completeness as 7th principle

### 🎯 Philosophy

**Core Principle**:
```
❌ Don't build: "Toolbox" (isolated operations)
✅ Do build: "Workflow Systems" (integrated user journeys)
```

**MetaSpec as Example**:
```
SDS Workflow:
  Phase 1: Constitution → /metaspec.sds.constitution
  Phase 2: Specification → /metaspec.sds.specify
  Phase 3: Quality Gates → /metaspec.sds.clarify, /metaspec.sds.checklist
  Phase 4: Implementation → /metaspec.sds.plan, /metaspec.sds.tasks, /metaspec.sds.implement
  Phase 5: Validation → /metaspec.sds.analyze
```

**Required Elements**:
1. **Workflow Phases** - Distinct stages in user journey
2. **Phase Purposes** - Why each phase exists
3. **Operation Mapping** - Which operations belong to which phase
4. **Sequencing** - Entry/exit criteria, dependencies, ordering
5. **End-to-End Examples** - Complete workflow demonstrations

### 🔄 Impact on Existing Projects

**Backward Compatibility**: ✅ Fully compatible
- Existing speckits continue to work
- No breaking changes to APIs or commands
- Templates add new sections but don't remove existing content

**Migration Path**:
- New projects automatically get workflow-focused templates
- Existing projects can add workflow sections via `/metaspec.sds.specify`
- Constitution updates guide workflow definition
- Future: `/metaspec.sds.checklist` and `/metaspec.sds.analyze` will validate workflow completeness

### 📊 Quality Enforcement

**Current (v0.7.0)**:
- ✅ Constitution template includes Workflow Completeness principle
- ✅ Domain spec template includes Workflow Specification section
- ✅ AGENTS.md documents workflow requirements

**Future (v0.7.x)**:
- 🔜 `/metaspec.sds.checklist` validates workflow completeness
- 🔜 `/metaspec.sds.analyze` scores workflow quality (Dimension 7: 15% weight)
- 🔜 Low scores (<70%) if workflow missing or incomplete

### 💡 Rationale

**Feedback Source**: Real-world speckit development
- Followed complete SDS + SDD workflow
- All quality checks passed (50/50, 98/100)
- Final result: 13 isolated commands without clear workflow
- Discovery: MetaSpec showed perfect workflows but didn't require them

**Design Philosophy Alignment**:
- MetaSpec demonstrates workflow-first design
- New principle ensures generated speckits follow same pattern
- "Practice what you preach" - consistency across framework

**User Experience**:
- Users need guidance on operation sequencing
- Isolated operations less valuable than integrated workflows
- Workflow definition enables better AI assistance and automation

### 🎉 Benefits

1. **Clearer User Guidance**: Users know which operations to use when
2. **Better AI Support**: AI agents understand operation context and sequencing
3. **Improved Usability**: Speckits are systems, not just tool collections
4. **Design Consistency**: All speckits follow MetaSpec's workflow pattern
5. **Quality Assurance**: Future validation catches workflow gaps early

### 📚 References

- **Related Issue**: Design gap identified through real-world usage
- **Philosophy**: Workflow Systems vs Tool Boxes

---

## [0.6.8] - 2025-11-15

### 🐛 Bug Fixes - Critical

**Fixed Documentation Inconsistency in `metaspec sync`**

Fixed a critical bug where `metaspec sync` updated command files but not `.metaspec/README.md`, causing documentation to reference old command names.

**Problem**:
- `metaspec sync` only synchronized `.metaspec/commands/` directory
- Did NOT sync `.metaspec/README.md`
- After sync: commands use new naming (`metaspec.evolution.*.md`)
- But README still referenced old naming (`/metaspec.proposal`, etc.)
- **Result**: Documentation contradicted actual files

**Impact**: 🔴 Critical
- Severity: High - Documentation misleads users
- Affected: All speckits using `metaspec sync` from v0.6.2+
- Confusion: Users follow README but commands don't exist

**Fix**:
- Added `.metaspec/README.md` to sync process (Step 7.6)
- Extracts speckit name from `pyproject.toml`
- Renders template with current version
- Updates Evolution command references in template:
  - `/metaspec.proposal` → `/metaspec.evolution.proposal`
  - `/metaspec.apply` → `/metaspec.evolution.apply`
  - `/metaspec.archive` → `/metaspec.evolution.archive`

**Before (v0.6.7)**:
```
metaspec sync
→ Updates .metaspec/commands/metaspec.evolution.*.md
→ .metaspec/README.md still shows: /metaspec.proposal
→ User runs /metaspec.proposal → File not found!
```

**After (v0.6.8)**:
```
metaspec sync
→ Updates .metaspec/commands/metaspec.evolution.*.md
→ Updates .metaspec/README.md → /metaspec.evolution.proposal
→ Documentation and files consistent!
```

**Implementation**:
- Modified `src/metaspec/cli/sync.py`:
  - Added Step 7.6: Sync `.metaspec/README.md`
  - Renders template with speckit name and version
  - Increments updated files count
- Updated template `src/metaspec/templates/base/.metaspec/README.md.j2`:
  - All Evolution command references now use unified naming
  - Examples updated to show correct commands

**All 156 tests passing.**

**Credit**: Bug discovered by user reviewing documentation consistency.

---

## [0.6.7] - 2025-11-15

### ✨ Improvements

**Added Clear Reminder for Required Checkboxes**

Improved user experience by adding prominent reminder about GitHub Issue's required checkboxes.

**Context**:
- GitHub Issue Forms have 5 required checkboxes
- GitHub security design: required checkboxes cannot be pre-checked via URL
- Users need to manually check them before submitting

**What we added**:
- Prominent yellow panel with "Action Required" title
- Lists all 5 required checkboxes users need to check
- Explains why they can't be pre-checked
- Updates "What happens next" flow to include checkbox step

**User experience improvement**:
```
Before (v0.6.6):
→ User opens browser
→ Sees empty checkboxes
→ Might be confused: "Why aren't these checked?"
→ Has to figure out what to do

After (v0.6.7):
→ Clear warning before browser opens
→ Lists all 5 checkboxes to check
→ Explains GitHub's limitation
→ User knows exactly what to expect
```

**Design philosophy**:
- Simple > Complex: Accept GitHub's constraint, communicate clearly
- Clear > Perfect: Explicit reminder > Attempting workarounds
- User-friendly: Set expectations upfront, minimize confusion

**All 156 tests passing.**

---

## [0.6.6] - 2025-11-15

### 🐛 Bug Fixes

**Added Missing Issue Title in Registration URL**

Fixed Issue title only showing `[Register]` prefix without speckit name.

**Problem**:
- v0.6.5 fixed template name but removed `title` parameter
- Resulted in generic Issue titles: just `[Register]`
- Less informative for maintainers reviewing registrations

**Fix**:
- Added `title` URL parameter back with speckit name
- Title format: `[Register] {speckit-name}`
- Example: `[Register] my-speckit`

**Before (v0.6.5)**:
```
https://.../issues/new?template=register-speckit.yml&repository=...
→ Title: "[Register]" (generic)
```

**After (v0.6.6)**:
```
https://.../issues/new?template=register-speckit.yml&title=%5BRegister%5D+my-speckit&repository=...
→ Title: "[Register] my-speckit" (descriptive)
```

**Implementation**:
- Extract speckit name from `pyproject.toml` (with fallback to directory name)
- Pass to `_generate_issue_url()` function
- Include in URL parameters for pre-filled title

**All 156 tests passing.**

---

## [0.6.5] - 2025-11-15

### 🐛 Bug Fixes - Critical

**Fixed `metaspec contribute` Registration Failure**

Fixed a critical bug that completely broke the speckit registration workflow.

**Problem**:
- Used incorrect GitHub Issue template name: `register.yml`
- Correct template name is: `register-speckit.yml`
- Resulted in empty Issue body, bot couldn't process registration
- All registration attempts failed

**Impact**: 🔴 Critical
- Severity: High - Broke entire registration workflow
- Affected: All users attempting to register speckits
- Duration: Since v0.6.4 release

**Fix**:
- Updated template name: `register.yml` → `register-speckit.yml`
- Removed `title` URL parameter (handled by GitHub Issue Forms)
- Updated URL generation to match GitHub Issue Forms API
- Updated tests to verify correct template name

**Verification**:
```bash
# Before (v0.6.4) - BROKEN
https://github.com/.../issues/new?template=register.yml&...
# → Empty Issue body, bot couldn't process

# After (v0.6.5) - FIXED
https://github.com/.../issues/new?template=register-speckit.yml&repository=...
# → Repository field pre-filled, bot processes automatically
```

**References**:
- Issue: Speckit registration failure discovered in testing
- Broken Example: awesome-spec-kits#6 (empty body)
- Working Template: `.github/ISSUE_TEMPLATE/register-speckit.yml`

**All 156 tests passing.**

---

## [0.6.4] - 2025-11-15

### 🎉 Changed - Major UX Improvement

**`metaspec contribute` - Redesigned for Simplicity**

Completely redesigned `metaspec contribute` to focus on its true value: validation + one-click submission.

**Why**: awesome-spec-kits bot already extracts all metadata automatically, making manual JSON generation unnecessary. The new design aligns with the actual workflow.

**New behavior**:
```bash
# Validate only
metaspec contribute --check-only

# Default: Show pre-filled issue URL  
metaspec contribute
# → Validates + displays GitHub issue URL

# One-click: Open browser automatically
metaspec contribute --open
# → Validates + opens pre-filled issue in browser (done in ~30 seconds!)

# Optional: Preview metadata
metaspec contribute --save-json
# → Saves JSON file for preview (not required)
```

**Key improvements**:
- ✅ **Simpler**: No interactive prompts
- ✅ **Faster**: 15-30 minutes → 30 seconds
- ✅ **Clearer**: Shows what bot will extract
- ✅ **One-click**: `--open` opens browser
- ✅ **Honest**: JSON is optional, not required

**Breaking Changes**:
- ❌ Removed: `--command` option (auto-detected)
- ❌ Removed: `--interactive` flag
- ❌ Changed: No longer generates JSON by default
- ✅ Added: `--open` flag
- ✅ Added: `--save-json` flag

**Migration**:
```bash
# Old (v0.6.3)
metaspec contribute my-command
# → Interactive prompts

# New (v0.6.4+)
metaspec contribute --open
# → One command, done!
```

**Implementation**:
- Auto-extract repository URL from pyproject.toml or git remote
- Auto-extract metadata from pyproject.toml
- Generate pre-filled GitHub issue URL
- Display what bot will extract
- Optional JSON preview with `--save-json`

**Philosophy**: The best automation is invisible automation. Users shouldn't manually enter data that bots can extract automatically.

---

## [0.6.3] - 2025-11-15

### ✨ Features

**metaspec contribute - Validation Enhancement (Phase 1)**
- Added pre-flight validation for speckit requirements
- New `--check-only` flag to validate without generating metadata
- Validates: pyproject.toml, README.md, LICENSE, CLI entry points, GitHub repository
- Actionable error messages with fix suggestions
- Beautiful validation results table with pass/fail status

**Usage**:
```bash
metaspec contribute --check-only  # Validate only
metaspec contribute               # Validate + generate metadata
```

**Benefits**:
- ✅ Catch issues before contribution
- ✅ Clear guidance on what's missing
- ✅ Improved community submission quality
- ✅ Better user experience

---

## [0.6.2] - 2025-11-15

### 🐛 Bug Fixes

**Unified Command Naming Pattern (Fixes Duplicate Files)**
- Implemented consistent naming across all command groups: `metaspec.{group}.{command}.md`
- Evolution commands now: `metaspec.evolution.apply.md` (not `metaspec.apply.md`)
- Generator (`metaspec init`) now uses unified naming from the start
- Sync command automatically migrates v0.5.x projects (removes old naming)
- Updated documentation to reflect unified naming pattern

**Why unified naming?**
- ✅ Consistent pattern across SDS, SDD, Evolution
- ✅ Better extensibility for future command groups
- ✅ Easier automation and tooling
- ✅ Clearer logical grouping

**Migration**: Run `metaspec sync` to migrate from v0.5.x or v0.6.0/0.6.1

**Fixes**: Duplicate Evolution command files bug (reported in METASPEC-SYNC-BUG-REPORT.md)

---

## [0.6.1] - 2025-11-14

### 🐛 Bug Fixes

**sync Command - PackageLoader Support**
- Fixed `metaspec sync` failing with "Unexpected loader type" error
- Now supports both `FileSystemLoader` (pip install) and `PackageLoader` (editable installs)
- Added template directory existence validation
- Improved error messages for troubleshooting

**Impact**: 
- ✅ Works with: `pip install metaspec`
- ✅ Works with: `pip install -e .` (development mode)
- ✅ Works with: `uv pip install -e .`

**Root Cause**: Code only checked for `FileSystemLoader`, but Generator uses `PackageLoader` in editable installs

---

## [0.6.0] - 2025-11-14

### ✨ Features

**metaspec sync Command**
- Added `metaspec sync` command to update MetaSpec commands in generated speckits
- Automatically backs up existing commands before updating (timestamped backups)
- Detects version differences and shows changelog
- Safe and reversible operations with Git-friendly workflow

**Version Tracking**
- Generated speckits now record the MetaSpec version used to create them
- Stored in `pyproject.toml` under `[tool.metaspec]` section
- Enables intelligent version detection and sync recommendations

**Usage**:
```bash
cd my-speckit
metaspec sync              # Update to latest version
metaspec sync --check-only # Check version without updating
metaspec sync --force      # Force update even if versions match
```

**Benefits**:
- Easily get workflow fixes (like v0.5.8 workflow order correction)
- No need to regenerate entire speckit
- Review changes with `git diff .metaspec/`
- Rollback if needed (automatic backups)

**Implementation**:
- New file: `src/metaspec/cli/sync.py`
- Updated: Command registration, template generation
- ~200 lines of code for complete sync functionality

---

## [0.5.8] - 2025-11-14

### 🐛 Bug Fixes

**Workflow Order Correction**
- Fixed SDS/SDD workflow command order to align with [GitHub spec-kit](https://github.com/github/spec-kit) official pattern
- Corrected quality gate positions: clarify (before plan) → checklist (after plan) → analyze (after tasks, before implement)
- Previous order was: `specify → plan → tasks → implement → checklist → analyze` ❌
- Correct order is: `specify → clarify → plan → checklist → tasks → analyze → implement` ✅

### 📝 Documentation

**SDS vs SDD Clarification**
- Distinguished SDS (two paths: Simple 4-5 commands | Complex 7-8 commands) from SDD (one complete path: 7-8 commands)
- Clarified SDD always follows complete spec-kit workflow (toolkit development is always complex)
- Completed SDD workflow examples in AGENTS.md with all 8 commands
- Fixed command count descriptions (was 2-4/5-7, now correctly 4-5/7-8)

**Quality Gate Explanation**
- Clarified why checklist and analyze don't overlap:
  - checklist: validates WHAT (requirements completeness in single document)
  - analyze: validates HOW (cross-artifact consistency and coverage)
  - Different check layers: unit test (checklist) vs integration test (analyze)

**Updated files**:
- `README.md`: Workflow order corrections and SDD clarification
- `AGENTS.md`: SDS/SDD distinction, workflow examples, typical workflow section
- `src/metaspec/templates/base/.metaspec/README.md.j2`: Template for generated speckits
- `CHANGELOG.md`: Command count corrections

**Impact**:
- Users will follow correct workflow order aligned with spec-kit best practices
- Clear guidance preventing confusion about command sequence
- Proper quality gate positioning ensures validation at right stages

---

## [0.5.7] - 2025-11-14

### 📝 Documentation

**Workflow Alignment with spec-kit**
- Corrected SDS/SDD command order based on [GitHub spec-kit](https://github.com/github/spec-kit) official guidance
- **SDS**: Two paths (Simple: 2-4 commands | Complex: 5-8 commands, follows spec-kit when splitting)
- **SDD**: One complete path (always 5-8 commands, follows spec-kit workflow)
- **Quality gates**: clarify (before plan) → checklist (after plan) → analyze (after tasks, before implement)

**Key fixes**:
1. Corrected command order: `specify → clarify → plan → checklist → tasks → analyze → implement`
2. Clarified `/metaspec.sds.implement` creates specification documents, NOT code
3. Explained why checklist and analyze don't overlap (WHAT vs HOW validation)
4. SDD always uses complete workflow (toolkit development is always complex)

**Updated files**:
- `README.md`: Command listings with workflow annotations and quality gate positions
- `AGENTS.md`: SDS/SDD workflows, examples, and typical workflow section
- `src/metaspec/templates/base/.metaspec/README.md.j2`: Template for generated speckits

**Impact**:
- Aligns MetaSpec with spec-kit best practices
- Clear quality gate positioning (input → plan → execution checkpoints)
- Reduces confusion about command overlapping and order
- Distinguishes simple spec definition from complex toolkit development

---

## [0.5.6] - 2025-11-14

### 🐛 Bug Fixes

**Documentation Command Count Fix**
- Fixed SDS command count: was showing 5, now correctly shows 8 commands
- Fixed total command count: was showing 16, now correctly shows 19 commands (8 SDS + 8 SDD + 3 Evolution)
- Added missing SDS commands in documentation: `plan`, `tasks`, `implement`

**Files Updated**:
- `README.md`: Quick start example now shows all 8 SDS and 8 SDD commands
- `src/metaspec/templates/base/.metaspec/README.md.j2`: Updated command counts and added missing commands
- `src/metaspec/templates/base/AGENTS.md.j2`: Fixed command count in developer section
- `docs/quickstart.md`: Updated command count from 16 to 19
- `docs/architecture.md`: Fixed SDS command count from 5 to 8

**Impact**:
- All newly generated speckits will show correct command counts
- Documentation now matches actual implementation (8 SDS + 8 SDD + 3 Evolution = 19 commands)

---

## [0.5.5] - 2025-11-13

### 🐛 Bug Fixes

**Version Sync**
- Fixed version number inconsistency in `src/metaspec/__init__.py` (was 0.5.0, now 0.5.5)
- Ensures all version indicators are synchronized across the codebase

---

## [0.5.4] - 2025-11-13

### 🚀 Features

**Precision-Guided Navigation with Line Numbers**

Added precision-guided navigation to 6 major MetaSpec commands, enabling massive token savings (84-98%) through targeted reading with `read_file(offset, limit)`.

**Commands Enhanced**:
- `specify` (SDS: 1060 lines, SDD: 2378 lines)
- `implement` (SDS: 1271 lines, SDD: 998 lines)
- `tasks` (SDS: 1054 lines)
- `plan` (SDD: 854 lines)

**Key Features**:
- 📋 Precise line numbers for each section (e.g., Lines 390-663)
- 🎯 Language-specific navigation (Python/TS/Go/Rust)
- 📊 Token savings calculation for each usage pattern
- 💡 Typical usage examples with concrete code

**Impact**:
- Total coverage: 8615 lines across 6 commands
- Token savings: 84-98% in typical usage scenarios
- Special achievement: 97-98% savings for language-specific sections

**analyze Command Enhancement**

Added three analysis modes for flexible validation workflows:
- **Quick Mode**: Fast structural integrity checks (<2 min)
- **Focused Mode**: Deep dive into specific dimension
- **Full Mode**: Comprehensive 11-dimension analysis (default)

**Impact**:
- Expected token reduction: 70% average
- Faster validation cycles for iterative development
- Better separation of concerns

### 🐛 Bug Fixes

**Template Syntax Errors**

Fixed 6 Jinja2 syntax errors in command templates:
- Replace `{%}` with `{percent}` to avoid control structure conflicts
- Files: sds/tasks.md.j2, sds/implement.md.j2, sdd/tasks.md.j2, sdd/implement.md.j2
- All 19 command templates now pass validation

### 📚 Documentation

**Internal Audit Reports**

Created comprehensive audit documentation (stored locally in `docs/internal/`):
- COMMAND_AUDIT_REPORT.md: Complete analysis of all 19 MetaSpec commands
- VERSION_COMPARISON_AUDIT.md: Comparison with GitHub published version

### 🧹 Chore

**Version Control Cleanup**

Removed internal documentation from Git tracking to respect `.gitignore` rules:
- Cleaned up `docs/internal/` directory
- Files remain available locally for development use

---

## [0.5.3] - 2025-11-11

### ✅ Testing

**Test Coverage Enhancement**

Significantly improved test coverage for CLI modules, enhancing code quality and reliability.

**Coverage Improvements**:
- **Overall Coverage**: 74.00% → 90.99% (+16.99%)
- **cli/init.py**: 35.12% → 88.02% (+52.90%)
- **cli/contribute.py**: 21.62% → 90.54% (+68.92%)

**New Test Cases** (15 new tests):

*cli/init.py* (8 new tests):
- `test_init_interactive_minimal_path` - Minimal user interaction flow
- `test_init_interactive_full_path` - Full customization flow
- `test_init_generation_flow` - Complete generation process
- `test_init_force_overwrites_existing` - Force overwrite functionality
- `test_init_fails_without_force_on_existing` - Directory conflict handling
- `test_init_interactive_user_cancels` - User cancellation handling
- `test_init_interactive_keyboard_interrupt` - Keyboard interrupt handling
- Full mock coverage for interactive prompts and generators

*cli/contribute.py* (7 new tests):
- `test_contribute_interactive_full_flow` - Complete contribution workflow
- `test_contribute_with_detected_commands` - Auto-detection of CLI commands
- `test_contribute_command_not_in_path_continue` - Missing command handling
- `test_contribute_custom_commands` - Custom command definition
- `test_contribute_non_interactive_fails` - Non-interactive mode validation
- `test_contribute_no_command_interactive_prompt` - Missing command prompt
- Full mock coverage for registry, prompts, and file operations

**Test Results**:
- ✅ 151/151 tests passing
- ✅ 90.99% coverage (exceeds 69% requirement by 21.99%)
- ✅ All critical user interaction paths covered

---

## [0.5.2] - 2025-11-11

### 🐛 Bug Fixes

**Technical Debt Cleanup**

Resolved 2 TODO items in the generator module:

1. **Dynamic Version Retrieval**: Now automatically gets MetaSpec version from package metadata using `importlib.metadata.version()`
   - Previously hardcoded as "0.1.0"
   - Now reflects the actual installed version (0.5.2)
   - Includes fallback to "0.0.0" if metadata unavailable

2. **Command Options Handling**: Properly generates CLI command parameters from options
   - Supports both required and optional parameters
   - Correctly handles parameter types
   - Generates appropriate default values for optional parameters
   - Adds display output for each option

**Changes**:
- `generator.py`: Added `_get_metaspec_version()` method
- `generator.py`: Enhanced command generation to properly handle options with types and requirements
- Fixed linter warnings (removed unused variables, cleaned blank lines)

---

## [0.5.1] - 2025-11-11

### 🔄 Refactoring

**Terminology Unification: Protocol → Specification**

Complete codebase-wide terminology standardization for better clarity and consistency.

**BREAKING CHANGES**:
- **Directory**: `specs/protocol/` renamed to `specs/domain/`
- **Variables**: `protocol_id` → `spec_id`, `PROTOCOL_NUMBER` → `SPEC_NUMBER`, etc.
- **Commands**: `show-protocol` → `show-spec`
- **Files**: `protocol-spec-template.md.j2` → `domain-spec-template.md.j2`
- **YAML**: `protocol:` → `specification:` (frontmatter field)

**Statistics**:
- ✅ Processed: **362 occurrences** (97.6%)
- ✅ Reserved: **9 occurrences** (proper nouns: Model Context Protocol, Protocol Buffers, MCP Protocol)
- ✅ Files affected: 100+
- ✅ Templates updated: SDS (8), SDD (3), Base templates

**Impact**:
- All MetaSpec commands and templates now use consistent "specification" terminology
- Domain specifications located in `specs/domain/` (previously `specs/protocol/`)
- All variable names, commands, and documentation updated accordingly
- Preserved technical terms where "protocol" is part of a proper noun

**Migration Guide**:
- Update any custom scripts referencing `specs/protocol/` to `specs/domain/`
- Replace `protocol_id` with `spec_id` in custom specifications
- Update command references from `show-protocol` to `show-spec`

---

## [0.5.0] - 2025-11-09

### ✨ Features

**Recursive Tree Structure for SDS Specifications**

SDS now supports hierarchical domain specifications with unlimited depth:

- **Physical Structure**: Flat directory layout under `specs/domain/`
  - All specifications are sibling directories (e.g., `001-root/`, `002-child/`, `013-grandchild/`)
  - Simple paths, FEATURE independence, Git branch friendly
  
- **Logical Structure**: Tree hierarchy via YAML frontmatter
  - Parent-child relationships declared in `spec.md` frontmatter
  - Context tracking: `spec_id`, `parent`, `root`, `type` (leaf/parent/root)
  - Parent → Child: Listed in "Sub-Specifications" table
  - Child → Parent: Shown in "Parent chain" breadcrumb

- **Numbering Strategy**:
  - Root: 001
  - First-level children: 002-009
  - Second-level children: 010-099
  - Third-level children: 100-999
  - Benefits: Clear hierarchy, flexible expansion, easy identification

**New SDS Commands** (8 total, up from 5)

Added 3 new commands for complex specification definition:

1. `/metaspec.sds.plan` - Plan specification architecture and sub-specifications
   - Assess complexity score (line count, entities, operations)
   - Decide: Keep single specification vs Split into sub-specifications
   - Design sub-specification structure if complex
   
2. `/metaspec.sds.tasks` - Break down specification work
   - Generate actionable task list organized by sub-specification
   - Track dependencies between sub-specifications
   - Include parent/root context for recursive structure
   
3. `/metaspec.sds.implement` - Write specification documents
   - Create new specification FEATUREs (independent `00X-` directories)
   - Call `/metaspec.sds.specify` internally with context
   - Update parent specification's "Sub-Specifications" section
   - Support recursive splitting at any depth

**Command Total**: 19 commands (8 SDS + 8 SDD + 3 Evolution)

### 📚 Documentation

**Clarity and Consistency Improvements**

- **Removed redundancy**: Eliminated duplicate "Specification relationships" section in AGENTS.md
- **Fixed anchor links**: Updated 3 broken references from "Two-Feature Architecture" to "SDS + SDD Separation"
- **Added numbering strategy**: Explained specification numbering logic (001, 002-009, 010-099, 100-999)
- **Updated command counts**: Synchronized across all files (README.md, CHANGELOG.md, architecture.md, templates)
- **Clarified design decision**: Emphasized flat physical structure with tree logical structure

**Files Updated**:
- `AGENTS.md` - Recursive tree structure section, fixed redundancy and links
- `README.md` - Updated command counts and examples
- `CHANGELOG.md` - Version history consistency
- `docs/architecture.md` - Command count updates
- `src/metaspec/templates/README.md` - SDS command list
- `src/metaspec/templates/meta/sds/commands/*.md.j2` - New command templates
- `src/metaspec/templates/meta/sdd/commands/specify.md.j2` - Command count reference

### 🎯 Design Principles

**Why Flat Physical + Tree Logical?**

1. **Simple paths**: `specs/domain/013-credit-card-payment/` (not deeply nested)
2. **FEATURE independence**: Each specification is a standalone FEATURE with its own lifecycle
3. **Flexible numbering**: Sub-specifications can use any available numbers (skip ranges)
4. **Git branch friendly**: Branch name = directory name = spec_id
5. **Easy reorganization**: Change relationships via frontmatter, no file moves
6. **Unlimited depth**: Any specification can be a parent with its own sub-specifications

---

## [0.4.0] - 2025-11-08

### ✨ Features

**Added templates/README.md for user guidance**

Generated speckits now include a comprehensive README in the `templates/` directory that explains:
- ✅ New directory structure organized by source
- ✅ Available templates and slash commands
- ✅ How to use templates (AI agents, CLI, manual)
- ✅ How to add custom templates
- ✅ Why organize by source (provenance, namespace isolation, composability)

**Example content**:
```markdown
# Templates Directory
> Organized by Specification System Source

templates/
├── generic/              # From MetaSpec library/generic
│   ├── commands/         # Slash Commands
│   └── templates/        # Template files
└── spec-kit/             # From MetaSpec library/sdd/spec-kit
    ├── commands/
    └── templates/
```

**Benefits**:
- ✅ Reduces user confusion about new structure
- ✅ Self-documenting directory
- ✅ Onboarding guide for new users
- ✅ Reference for adding custom templates

**Files Changed**:
- `src/metaspec/templates/base/templates/README.md.j2` - New template file
- `src/metaspec/generator.py` (Line 220) - Add to base templates list
- `src/metaspec/templates/meta/templates/spec-template.md.j2` - Updated structure examples and checklist

---

### 💥 BREAKING CHANGES

**Templates directory structure now organized by specification system source**

**Issue**: Generator implementation did not match documented design  
- ❌ Documentation promised: `templates/{source}/commands/` (organized by source)
- ❌ Implementation generated: `templates/commands/` (flat structure)
- ❌ Result: Naming conflicts, unclear provenance, violated "specification composability" principle

**Fix**: Restructured templates directory to preserve source hierarchy

**Before** (0.3.0):
```
my-speckit/
└── templates/
    ├── specify-template.md      # ❌ Flat, no source info
    ├── plan-template.md
    └── commands/                # ❌ All commands mixed
        ├── specify.md           # From generic?
        └── plan.md              # From spec-kit?
```

**After** (0.4.0):
```
my-speckit/
└── templates/
    ├── generic/                 # ✅ Clear source
    │   ├── commands/
    │   │   └── specify.md
    │   └── templates/
    │       └── specify-template.md
    └── spec-kit/                # ✅ Clear source
        ├── commands/
        │   └── plan.md
        └── templates/
            └── plan-template.md
```

**Benefits**:
- ✅ **Clear provenance**: Users know which specification system each command comes from
- ✅ **Namespace isolation**: Different sources can have same-named commands without conflict
- ✅ **Specification composability**: Embodies MetaSpec's core design principle
- ✅ **Matches documentation**: Implementation now aligns with spec-template.md.j2

**Migration Guide**:

For existing speckits generated with 0.x.x:

1. **Restructure templates directory**:
   ```bash
   cd my-speckit/templates
   
   # Create source directories
   mkdir -p generic/commands generic/templates
   mkdir -p spec-kit/commands spec-kit/templates
   
   # Move files based on their source
   # (Check your meta-spec.yaml to identify which commands came from which source)
   mv specify-template.md generic/templates/
   mv commands/specify.md generic/commands/
   
   mv plan-template.md spec-kit/templates/
   mv commands/plan.md spec-kit/commands/
   
   # Remove old flat directories
   rmdir commands/
   ```

2. **Update any hardcoded paths in scripts** (if applicable)

**Impact**:
- ⚠️ **Existing speckits**: Need manual restructuring (see migration guide above)
- ⚠️ **New speckits**: Automatically use new structure via `metaspec init`
- ⚠️ **Breaking change in 0.x**: MINOR version bump (0.3.0 → 0.4.0)

**Files Changed**:
- `src/metaspec/generator.py` (Line 261, 268) - Preserve source in output paths
- `src/metaspec/templates/meta/sdd/commands/specify.md.j2` (3 locations) - Updated documentation
- `docs/architecture.md` (Line 266-268) - Updated examples

**References**:
- Detailed analysis: `ANALYSIS-templates-structure-diff.md`
- Original specification: `spec-template.md.j2` Line 409-455

---

## [0.3.0] - 2025-11-07

### ✨ Features

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
- ✅ Preserved dual-source architecture (Specification-Derived + Library-Selected)

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

**Impact**: 
- ✅ **Framework neutral**: No external specification dependencies
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

### ♻️ Refactoring

**Removed redundant Argument Access descriptions**

**Issue**:
- "Argument Access" section repeated 4 times in slash command templates
- Full descriptions duplicated in Template 1, Template 2, and Template 3
- ~10 lines of redundant content

**Fix**: Simplified to single-line references in templates:
- ✅ Kept comprehensive description in Frontmatter Fields section (single source of truth)
- ✅ Template 1: 3 lines → 1 line reference
- ✅ Template 2: 4 lines → 1 line reference
- ✅ Template 3: 3 lines → 1 line reference

**After**: `**Argument Access**: $ARGUMENTS, $1, $2, $3 (see Frontmatter Fields above)`

**Impact**: 
- ✅ Removed 9 lines of redundancy
- ✅ Easier to maintain (single source of truth)
- ✅ Users still see relevant variables in templates

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
1. AI generates MCP server → needs: show-spec, get-template
2. Developer validates manually → needs: init, validate, docs
3. AI debugs errors → needs: validate, explain-error

### Derived Features (P0)
- Specification reference system (Scenarios 1, 3)
- Template system (Scenarios 1, 2)
- Validation CLI (All scenarios)

### Command Design Rationale
- `show-spec`: AI needs rules before generating (Scenario 1)
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
   └── {custom}/               # Custom (from domain specification)
       ├── commands/           # Specification-specific Slash Commands
       └── templates/          # Specification entity templates
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
   └── mcp/                   # Custom (from domain/001-mcp-spec)
       ├── commands/
       └── templates/
   ```

4. **Implementation Guide**:
   - **Library Specifications**: Copy from MetaSpec library → `templates/{library-name}/`
   - **Custom Specification**: Derive from domain specification → `templates/{domain}/`
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
- [ ] Entity templates match specification entities
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
| **❌ P0-1: Missing User Journey** | ✅ **Resolved** | Step 2.5 added with 5-step analysis |
| **❌ P0-3: Insufficient Template Guidance** | ✅ **Resolved** | Component 6 added with complete structure |
| **🟡 P0-1: Derive CLI from Requirements** | ✅ **Improved** | Commands now derived from scenarios (Step 2.5 STEP 4) |
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
4. **Entity Templates**: Specification entities → template files
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
└── mcp/                   # Custom (from domain specification)
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
   - Before: "Toolkit specs explicitly depend on specifications and define HOW to implement"
   - After: "Toolkit specs explicitly depend on specifications, **derive features from user scenarios**, and define HOW to implement"

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
- Slash Commands = "Spec-driven execution guides with embedded specification knowledge"
- AI reads Slash Command (with specification knowledge) → produces spec-compliant output
- Commands derived from domain specification

#### Key Improvements

1. **Specification-Driven Command Derivation**
   - Added STEP 1: Analyze domain specification
   - Added STEP 2: Derive commands from specification content
   - Mapping rules: entities → get-template, validation_rules → validate, workflows → commands
   
2. **Workflow-Aware Command Generation**
   - Type A (State Machine): Use navigation commands (get-workflow, next-phase)
   - Type B (Action Sequence): Each action becomes a command (like MetaSpec's specify → clarify → plan)
   - Judgment rule: verb/action → command, noun/state → navigation

3. **Embedded Specification Knowledge**
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
   - Slash Commands = Specification-Driven (workflow actions)
   - CLI Commands = Purpose-Driven (toolkit functions)
   - Clear separation of concerns

2. **Toolkit Type Classification**
   - 6 toolkit types identified: Generator, Environment Checker, Validator, Query Tool, State Manager, Community Platform
   - Each type derives specific CLI commands
   - Real project examples: Specify, OpenSpec, MetaSpec

3. **4-Step CLI Derivation Process**
   - STEP 1: Define Toolkit Type (Generator? Validator? Query Tool?)
   - STEP 2: Derive CLI Commands from Type (type → commands mapping)
   - STEP 3: Specification-Influenced CLI Parameters (specification affects parameters, not commands)
   - STEP 4: Define CLI Implementation (detailed specs for each command)

4. **Real-World Validation**
   - Analyzed 4 projects: Spec-Kit (shell scripts), OpenSpec (validator+query), MetaSpec (generator+community), Specify (generator+checker)
   - Confirmed: CLI commands come from toolkit purpose, not specification workflow
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
   - ❌ Removed: Hardcoded mapping table (Specification Content → Fixed Command Names)
   - ✅ Added: Command naming process (3 steps: Read specification → Extract verbs/nouns → Form domain names)
   - ✅ Added: Real project patterns (Spec-Kit, OpenSpec, MetaSpec naming examples)
   - ✅ Added: "Command Purpose Categories" (guidance, NOT fixed names)
   - ✅ Example: MCP specification → `define-server`, `configure-tools` (NOT get-template)

2. **CLI Commands - STEP 2 (Complete Rewrite)**
   - ❌ Removed: Hardcoded command table (Toolkit Type → Fixed CLI Commands)
   - ✅ Added: CLI command derivation process (Identify functions → Match purposes → Choose names)
   - ✅ Added: Real project CLI commands (actual implementations from Specify, OpenSpec, MetaSpec)
   - ✅ Added: "Command Purpose Guidelines" (NOT fixed names)
   - ✅ Example: MCP-Speckit → `show`, `docs`, `list` (NOT get-spec, get-template)

3. **Updated All Examples**
   - STEP 3: Specification parameters (removed get-template, get-spec examples)
   - Classification Example: Now uses domain-specific names
   - CLI Implementation Checklist: Removed hardcoded commands, added naming guidance

**Key Principle Now Enforced**:
```
❌ DON'T: Use generic/hardcoded names (get-spec, get-template, validate)
✅ DO: Extract domain-specific names from specification terminology
```

**Real Project Alignment**:
- Spec-Kit: `specify`, `plan`, `implement` ✅
- OpenSpec: `proposal`, `apply`, `archive` ✅
- MetaSpec: `specify`, `clarify`, `plan` ✅
- No project uses: `get-template`, `get-spec` ✅

**Impact**: 
- Eliminates "template copying" anti-pattern
- Ensures domain-appropriate naming
- Aligns with all real-world projects
- Better developer experience with familiar domain terms

#### Combined Impact - Complete Command Architecture

**Slash Commands** (Specification-Driven) + **CLI Commands** (Purpose-Driven) = Complete toolkit architecture

**Before** ❌:
- Generic templates (init, validate, generate)
- No methodology for command derivation
- Confusion between CLI and Slash Commands

**After** ✅:
- Specification-derived Slash Commands (from workflow, entities, validation rules)
- Purpose-derived CLI Commands (from toolkit type)
- Clear separation and derivation methodology

**Example - MCP-Speckit**:
```
Slash Commands (from MCP specification):
  /mcpspeckit.define-requirements  ← From specification workflow
  /mcpspeckit.create-design        ← From specification entities
  /mcpspeckit.generate-code        ← From specification operations

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
  - `/metaspec.sds.checklist` - Specification quality validation with iteration tracking
  - `/metaspec.sds.analyze` - Specification consistency analysis with progress comparison
  - `/metaspec.sds.clarify` - Specification ambiguity resolution with resolved item tracking
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
- **SDS Commands**: Added `/metaspec.sds.checklist` command for specification quality validation
  - Generates systematic quality checklists for domain specifications
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
- **SDS/SDD Symmetry**: Better alignment between specification and toolkit workflows
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
- MetaSpec workflow commands (19 commands: 8 SDS + 8 SDD + 3 Evolution)
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

