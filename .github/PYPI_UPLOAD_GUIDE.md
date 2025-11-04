# PyPI Upload Guide for MetaSpec v0.1.1

## ✅ Pre-upload Checklist

- [x] Version bumped to 0.1.1 in pyproject.toml
- [x] CHANGELOG.md updated
- [x] Git committed and tagged (v0.1.1)
- [x] GitHub Release created
- [x] Package built successfully
  - [x] meta_spec-0.1.1-py3-none-any.whl (204K)
  - [x] meta_spec-0.1.1.tar.gz (160K)
- [x] Package integrity checked with twine ✅

## 🔑 PyPI Account Setup

### Step 1: Register PyPI Account (if not done)

1. **Main PyPI**: https://pypi.org/account/register/
2. **Test PyPI**: https://test.pypi.org/account/register/

### Step 2: Generate API Token

1. Go to https://pypi.org/manage/account/
2. Scroll to "API tokens"
3. Click "Add API token"
4. Name: "MetaSpec CLI Upload"
5. Scope: "Entire account" (or specific to meta-spec later)
6. Copy the token (starts with `pypi-...`)

### Step 3: Configure Token

```bash
# Create/edit ~/.pypirc
cat > ~/.pypirc << 'EOF'
[pypi]
username = __token__
password = pypi-AgEIc...YOUR_TOKEN_HERE...

[testpypi]
username = __token__
password = pypi-AgENd...YOUR_TEST_TOKEN_HERE...
EOF

chmod 600 ~/.pypirc
```

## 🧪 Option 1: Upload to Test PyPI First (Recommended)

Test PyPI is a separate instance for testing packages before publishing to the main index.

```bash
# Upload to Test PyPI
uv run twine upload --repository testpypi dist/*

# Test installation
pip install --index-url https://test.pypi.org/simple/ --no-deps metaspec

# Verify it works
metaspec --version
```

**Expected output:**
```
Uploading distributions to https://test.pypi.org/legacy/
Uploading meta_spec-0.1.1-py3-none-any.whl
100% ━━━━━━━━━━━━━━━━━━━━━━ 204.0/204.0 kB • 00:00
Uploading meta_spec-0.1.1.tar.gz
100% ━━━━━━━━━━━━━━━━━━━━━━ 160.0/160.0 kB • 00:00

View at:
https://test.pypi.org/project/metaspec/0.1.1/
```

## 🚀 Option 2: Upload to PyPI (Production)

**⚠️ Warning**: This cannot be undone! You cannot re-upload the same version.

```bash
# Upload to PyPI
uv run twine upload dist/*
```

**Expected output:**
```
Uploading distributions to https://upload.pypi.org/legacy/
Uploading meta_spec-0.1.1-py3-none-any.whl
100% ━━━━━━━━━━━━━━━━━━━━━━ 204.0/204.0 kB • 00:00
Uploading meta_spec-0.1.1.tar.gz
100% ━━━━━━━━━━━━━━━━━━━━━━ 160.0/160.0 kB • 00:00

View at:
https://pypi.org/project/metaspec/0.1.1/
```

## ✅ Verify Upload

### After Upload to PyPI

```bash
# Install from PyPI
pip install metaspec

# Verify version
metaspec --version
# Should output: metaspec version 0.1.1

# Test basic functionality
metaspec --help
metaspec init --help
```

### Update Documentation

After successful upload, update README.md:

```markdown
## Installation

```bash
# Recommended
pip install metaspec

# Or with uv (faster)
uv pip install metaspec
```
```

## 📊 Post-Upload Actions

1. **Update README Badge**
   ```markdown
   [![PyPI version](https://badge.fury.io/py/metaspec.svg)](https://badge.fury.io/py/metaspec)
   ```

2. **Announce Release**
   - Update GitHub Release description
   - Post on social media
   - Update documentation links

3. **Monitor**
   - Check PyPI stats: https://pypistats.org/packages/metaspec
   - Watch for issues

## 🐛 Troubleshooting

### Issue: "Invalid or non-existent authentication information"
**Solution**: Check ~/.pypirc token is correct

### Issue: "File already exists"
**Solution**: Version 0.1.1 already uploaded. Bump to 0.1.2 for new upload.

### Issue: "Package name already taken"
**Solution**: Package name "metaspec" might be taken. Check alternatives:
- `meta-spec` (with hyphen, but imports as `metaspec`)
- `metaspec-ai`
- Contact PyPI to claim if abandoned

## 📝 Next Release Workflow

For future releases:

```bash
# 1. Update version in pyproject.toml
# 2. Update CHANGELOG.md
# 3. Commit and tag
git add pyproject.toml CHANGELOG.md
git commit -m "chore: bump version to x.x.x"
git tag vx.x.x
git push origin main --tags

# 4. Build
rm -rf dist/ build/
uv run python -m build

# 5. Check
uv run twine check dist/*

# 6. Upload
uv run twine upload dist/*
```

---

**Ready to upload?** Choose Option 1 (Test PyPI) or Option 2 (Production PyPI)

