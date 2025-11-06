# Changelog

All notable changes to MetaSpec will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

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

#### Updated `/metaspec.sdd.specify`

**New Section**: Component 4 - Slash Commands - Spec-Driven Execution
- 4-step process: Analyze → Derive → Create → Workflow-specific
- Protocol content → command mapping rules
- Spec-driven template structure with embedded knowledge
- Design principles for spec-compliant production

#### Impact

This addresses the core feedback: **commands are no longer套用模板, but derived from protocol specifications**.

**Example**:
```
Before: init, validate, generate (generic)
After: get-spec, get-template, validate (derived from MCP protocol)
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

