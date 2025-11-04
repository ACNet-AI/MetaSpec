# Release v0.1.1: Documentation Improvements

## 📚 What's New

This release focuses on improving the user experience with streamlined documentation and better installation guidance.

### 🚀 Installation Made Simple

We've dramatically simplified the installation process:

**Before (v0.1.0)**:
```bash
git clone https://github.com/ACNet-AI/MetaSpec.git
cd MetaSpec
pip install -e .
```

**Now (v0.1.1)**:
```bash
# Recommended: Use uv (10-100x faster) ⚡
uv pip install git+https://github.com/ACNet-AI/MetaSpec.git

# Or use pip
pip install git+https://github.com/ACNet-AI/MetaSpec.git
```

### ✨ Key Improvements

- **70% Shorter Documentation** - Reduced quickstart guide from ~350 to ~155 lines
- **uv First** - Prioritize modern, fast Python package manager
- **Cleaner Structure** - Collapsible sections for alternative methods
- **Better Examples** - Streamlined workflows and commands
- **Faster Onboarding** - Get started in 5 minutes or less

## 📝 Documentation Changes

### Installation Guide
- Replace `git clone` workflow with direct pip/uv install
- Add collapsible sections for development mode
- Highlight uv's 10-100x speed advantage

### Quickstart Guide
- Remove redundant content
- Simplify step-by-step instructions
- Focus on essential workflows
- Better organization of sections

## 🔧 Full Changelog

See [CHANGELOG.md](./CHANGELOG.md) for detailed changes.

## 📦 Installation

```bash
# Recommended: Use uv ⚡
uv pip install git+https://github.com/ACNet-AI/MetaSpec.git@v0.1.1

# Or use pip
pip install git+https://github.com/ACNet-AI/MetaSpec.git@v0.1.1

# Development mode
git clone https://github.com/ACNet-AI/MetaSpec.git
cd MetaSpec
uv pip install -e .
```

## 📚 Documentation

- [README](./README.md) - Complete feature overview
- [Quickstart Guide](./docs/quickstart.md) - Get started in 5 minutes
- [AGENTS.md](./AGENTS.md) - AI workflow guide
- [Examples](./examples/) - Example projects

## 🙏 Thank You

Thanks to everyone who provided feedback on the documentation. Your input helped make MetaSpec more accessible!

## 🔜 What's Next?

- PyPI package release (coming soon!)
- More community speckits
- Enhanced templates

---

**Full Changelog**: https://github.com/ACNet-AI/MetaSpec/compare/v0.1.0...v0.1.1

