#!/bin/bash
# PyPI Setup and Upload Script for MetaSpec

set -e

echo "🚀 MetaSpec PyPI Upload Setup"
echo "================================"
echo ""

# Check if .pypirc exists
if [ -f ~/.pypirc ]; then
    echo "✅ Found ~/.pypirc configuration"
    echo ""
else
    echo "⚠️  No ~/.pypirc found. Creating template..."
    echo ""
    cat > ~/.pypirc << 'EOF'
[pypi]
username = __token__
password = pypi-REPLACE_WITH_YOUR_TOKEN

[testpypi]
username = __token__
password = pypi-REPLACE_WITH_YOUR_TEST_TOKEN
EOF
    chmod 600 ~/.pypirc
    
    echo "📝 Template created at ~/.pypirc"
    echo ""
    echo "⚠️  IMPORTANT: You need to update the API tokens!"
    echo ""
    echo "Steps to get your PyPI API token:"
    echo "1. Go to https://pypi.org/manage/account/"
    echo "2. Scroll to 'API tokens' section"
    echo "3. Click 'Add API token'"
    echo "4. Name: 'MetaSpec Upload'"
    echo "5. Scope: 'Entire account' (or project-specific later)"
    echo "6. Copy the token (starts with pypi-...)"
    echo "7. Edit ~/.pypirc and replace REPLACE_WITH_YOUR_TOKEN"
    echo ""
    echo "Then run this script again to upload."
    exit 1
fi

# Check if tokens are configured
if grep -q "REPLACE_WITH_YOUR" ~/.pypirc; then
    echo "❌ API tokens not configured in ~/.pypirc"
    echo ""
    echo "Please edit ~/.pypirc and replace placeholder tokens with real ones:"
    echo "  nano ~/.pypirc"
    echo ""
    echo "Get tokens from: https://pypi.org/manage/account/"
    exit 1
fi

echo "📦 Checking package integrity..."
uv run twine check dist/*

if [ $? -eq 0 ]; then
    echo "✅ Package integrity check passed"
    echo ""
else
    echo "❌ Package integrity check failed"
    exit 1
fi

echo "🚀 Ready to upload to PyPI!"
echo ""
echo "Packages to upload:"
ls -lh dist/

echo ""
read -p "Continue with upload? (y/N): " -n 1 -r
echo
if [[ $REPLY =~ ^[Yy]$ ]]; then
    echo ""
    echo "📤 Uploading to PyPI..."
    uv run twine upload dist/*
    
    if [ $? -eq 0 ]; then
        echo ""
        echo "✅ Upload successful!"
        echo ""
        echo "🎉 MetaSpec v0.1.1 is now live on PyPI!"
        echo ""
        echo "View at: https://pypi.org/project/metaspec/0.1.1/"
        echo ""
        echo "Users can now install with:"
        echo "  pip install metaspec"
        echo ""
    else
        echo ""
        echo "❌ Upload failed. Check error messages above."
        exit 1
    fi
else
    echo "Upload cancelled."
    exit 0
fi

