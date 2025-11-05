# Changelog

All notable changes to MetaSpec will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

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

