# MetaSpec Community Registry

A lightweight, decentralized system for discovering and sharing specification toolkits (speckits).

## 🌟 Core Philosophy

```
Create → Publish → Discover → Use
```

MetaSpec Community enables anyone to:
- Create custom speckits  
- Publish to community registry
- Discover and install others' speckits
- Build a thriving ecosystem

---

## 📦 Architecture

### Decentralized Model

```
Developer                Community Registry           PyPI                User
   ↓                           ↓                        ↓                  ↓
Create Speckit  →  Publish Metadata  →  Install Package  →  Use Directly
metaspec init      metaspec contribute  pip install         my-speckit cmd
```

**Key Features**:
- **Community Discovery**: GitHub-hosted JSON registry
- **Standard Distribution**: PyPI for package management
- **Auto Caching**: 24h cache, works offline
- **No Central Control**: Anyone can contribute

---

## 🚀 Usage Guide

### For Users: Discover and Install

#### 1. Search Community Speckits

```bash
metaspec search "api validation"
```

Output example:
```
Found 3 speckit(s)
┏━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━┳━━━━━━━━━━━━┓
┃ Name         ┃ Description        ┃ Author   ┃ Tags       ┃
┡━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━╇━━━━━━━━━━━━┩
│ api-speckit  │ REST API validator │ John Doe │ api, rest  │
│ mcp-speckit  │ MCP protocol kit   │ Jane     │ mcp, ai    │
└──────────────┴────────────────────┴──────────┴────────────┘
```

#### 2. Install Speckit

```bash
metaspec install api-speckit
```

This command:
1. Finds `api-speckit` in community registry
2. Installs from PyPI: `pip install api-speckit`
3. Verifies installation

#### 3. Use Installed Speckit

```bash
# Direct usage (no metaspec prefix!)
api-speckit --help
api-speckit validate my-api.json
```

#### 4. List Installed Speckits

```bash
metaspec list
```

Output:
```
Installed Speckits (3)
┏━━━━━━━━━━━━━━┳━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━┓
┃ Command      ┃ Version ┃ Location             ┃
┡━━━━━━━━━━━━━━╇━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━┩
│ api-speckit  │ 1.0.0   │ /usr/local/bin/...   │
└──────────────┴─────────┴──────────────────────┘
```

#### 5. Get Detailed Information

```bash
metaspec info api-speckit
```

Output:
```
Speckit Information: api-speckit

Command: api-speckit
Location: /usr/local/bin/api-speckit
Version: 1.0.0

Available Commands:
  • init
  • validate
  • generate

✓ Found in community registry
Name: api-speckit
Description: REST API validation toolkit
Author: John Doe
Repository: https://github.com/johndoe/api-speckit
```

---

### For Developers: Publish Your Speckit

#### 1. Create Your Speckit

```bash
metaspec init my-awesome-speckit
cd my-awesome-speckit

# Develop using MetaSpec commands
# /metaspec.specify, /metaspec.implement, etc.
```

#### 2. Publish to PyPI

```bash
# Build package
uv build

# Upload to PyPI
uv publish
```

#### 3. Generate Community Metadata

```bash
metaspec contribute my-awesome-speckit
```

This generates `my-awesome-speckit.json`:

```json
{
  "name": "my-awesome-speckit",
  "command": "my-awesome-speckit",
  "description": "My awesome specification toolkit",
  "version": "1.0.0",
  "pypi_package": "my-awesome-speckit",
  "repository": "https://github.com/username/my-awesome-speckit",
  "author": "Your Name",
  "tags": ["api", "validation"],
  "cli_commands": ["init", "validate", "generate"]
}
```

#### 4. Submit to Community Registry

1. Fork: https://github.com/ACNet-AI/awesome-spec-kits
2. Add file: `speckits/my-awesome-speckit.json`
3. Submit Pull Request

**PR Guidelines**:
- One speckit per PR
- Include README with usage examples
- Test installation before submitting

---

## 📋 Registry Structure

### Community Registry Repository

```
awesome-spec-kits/
├── README.md                  # Overview and listing
├── CONTRIBUTING.md            # Contribution guide
├── speckits.json             # Master registry file
├── speckits/                 # Individual speckit files
│   ├── api-speckit.json
│   ├── mcp-speckit.json
│   └── ...
├── examples/
│   └── example-speckit.json  # Template
└── scripts/
    └── validate.py           # Validation script
```

### Speckit Metadata Schema

```json
{
  "name": "string (required)",
  "command": "string (required)",
  "description": "string (required)",
  "version": "string (optional)",
  "pypi_package": "string (optional but recommended)",
  "repository": "string (optional but recommended)",
  "author": "string (optional)",
  "tags": ["array of strings"],
  "cli_commands": ["array of command names"]
}
```

---

## 🔍 Discovery Workflow

### How Users Find Speckits

```
1. User searches: metaspec search "api"
        ↓
2. MetaSpec fetches: awesome-spec-kits/speckits.json
        ↓
3. Caches locally: ~/.metaspec/cache/community_speckits.json (24h TTL)
        ↓
4. Displays matches
        ↓
5. User installs: metaspec install api-speckit
        ↓
6. Installs from PyPI: pip install api-speckit
        ↓
7. Verifies installation: api-speckit --version
        ↓
8. Ready to use: api-speckit validate
```

---

## 🎯 Best Practices

### For Developers

**Do**:
- ✅ Use clear, descriptive names
- ✅ Provide comprehensive README
- ✅ Add usage examples
- ✅ Tag appropriately
- ✅ Keep PyPI package updated
- ✅ Maintain repository

**Don't**:
- ❌ Use generic names
- ❌ Skip documentation
- ❌ Abandon projects without notice
- ❌ Spam tags

### For Users

**Do**:
- ✅ Check repository and author
- ✅ Read documentation
- ✅ Report issues
- ✅ Contribute improvements

**Don't**:
- ❌ Install untrusted speckits
- ❌ Ignore security warnings

---

## 🔒 Security

### For Users

1. **Review Before Installing**
   - Check repository
   - Read source code
   - Verify author

2. **Use Virtual Environments**
   ```bash
   python -m venv .venv
   source .venv/bin/activate
   metaspec install <speckit>
   ```

3. **Report Security Issues**
   - Email: security@acnet.ai
   - GitHub Issues (for non-critical issues)

### For Developers

1. **Code Review** - All PRs reviewed before merge
2. **No Malicious Code** - Automatic scanning
3. **Clear Licensing** - MIT license preferred

---

## 📊 Statistics

View registry statistics at:
https://github.com/ACNet-AI/awesome-spec-kits

**Current**:
- Total Speckits: Check repository
- Categories: API, Testing, Design, Data, AI, etc.
- Total Downloads: PyPI stats

---

## 💡 FAQ

### How is this different from PyPI?

MetaSpec Community Registry is for **discovery**, PyPI is for **distribution**.

- **Registry**: Curated list with metadata (tags, descriptions)
- **PyPI**: Package hosting and version management

### Can I publish without PyPI?

Not recommended. Users expect standard Python packaging.

### What if my PR is rejected?

Common reasons:
- Missing documentation
- Unclear purpose
- Quality issues
- Duplicate functionality

Address feedback and resubmit.

### How long does approval take?

Usually 1-3 days. Maintainers review:
- Code quality
- Documentation
- Security
- Usefulness

---

## 🤝 Contributing

See [CONTRIBUTING.md](https://github.com/ACNet-AI/awesome-spec-kits/blob/main/CONTRIBUTING.md) for detailed guidelines.

**Quick Start**:
1. Create your speckit
2. Publish to PyPI
3. Generate metadata: `metaspec contribute <name>`
4. Submit PR to awesome-spec-kits

---

## 📚 Resources

- **Registry**: https://github.com/ACNet-AI/awesome-spec-kits
- **MetaSpec Docs**: https://github.com/ACNet-AI/MetaSpec
- **PyPI**: https://pypi.org
- **Community**: https://github.com/ACNet-AI/MetaSpec/discussions

---

**Built with ❤️ by the MetaSpec Community**
