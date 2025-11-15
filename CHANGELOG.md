# Changelog

All notable changes to MetaSpec will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

---

## [0.7.0] - 2025-11-15

### ⭐ Major Feature - Workflow-Driven Design Philosophy

**Introduced Workflow Completeness Principle for Domain Specifications**

MetaSpec now enforces **workflow-first design** for all domain specifications, addressing a fundamental design gap where speckits could pass all quality checks but lack clear user workflows.

**Problem We Solved**:
- Before v0.7.0: Developers created speckits with isolated operations ("tool箱")
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
❌ Don't build: "Tool箱" (isolated operations)
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

**Feedback Source**: Real-world development of `marketing-spec-kit`
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

- **Feedback Document**: `/Users/guyue/marketing-spec-kit/docs/internal/metaspec-feedback.md`
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
- Example: `[Register] marketing-spec-kit`

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
- Bug Report: marketing-spec-kit registration failure
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
- Eliminates "template套用" anti-pattern
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

