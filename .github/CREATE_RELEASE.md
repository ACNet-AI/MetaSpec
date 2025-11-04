# How to Create GitHub Release for v0.1.1

## 🚀 Quick Steps

### 1. Go to GitHub Releases Page
Visit: https://github.com/ACNet-AI/MetaSpec/releases/new

### 2. Fill in Release Information

**Choose a tag**: `v0.1.1` (existing tag)

**Release title**: 
```
Release v0.1.1: Documentation Improvements
```

**Description**: Copy content from `.github/release-notes-v0.1.1.md`

### 3. Options
- ✅ Set as the latest release
- ⬜ Set as a pre-release (leave unchecked)

### 4. Publish Release
Click "Publish release" button

---

## 📋 Alternative: Using GitHub CLI

If you have `gh` CLI installed:

```bash
gh release create v0.1.1 \
  --title "Release v0.1.1: Documentation Improvements" \
  --notes-file .github/release-notes-v0.1.1.md
```

---

## ✅ Verify Release

After creating:
1. Visit: https://github.com/ACNet-AI/MetaSpec/releases
2. Check v0.1.1 is listed
3. Verify release notes display correctly

---

## 🎉 Done!

Users can now install with:
```bash
pip install git+https://github.com/ACNet-AI/MetaSpec.git@v0.1.1
```
