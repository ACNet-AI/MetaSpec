# Contributing Guide

Thank you for your interest in Meta-Spec! We welcome contributions of all kinds.

---

## 🤝 How to Contribute

### Report Bugs

1. Check [Issues](https://github.com/your-org/meta-spec/issues) to ensure the issue hasn't been reported
2. Create a new Issue, including:
   - Problem description
   - Steps to reproduce
   - Expected behavior vs actual behavior
   - Environment information (Python version, OS, etc.)
   - Related logs and screenshots

### Suggest Features

1. Start a discussion in [Discussions](https://github.com/your-org/meta-spec/discussions)
2. If approved, create a Feature Request Issue
3. Describe clearly:
   - Use case
   - Suggested implementation
   - Impact on existing features

### Submit Code

1. Fork the project
2. Create a feature branch: `git checkout -b feature/your-feature`
3. Write code and tests
4. Commit: `git commit -m "feat: add your feature"`
5. Push: `git push origin feature/your-feature`
6. Create a Pull Request

---

## 💻 Development Environment Setup

### Prerequisites

- Python 3.11+
- Git
- uv or pip

### Local Development

```bash
# 1. Fork and clone
git clone https://github.com/your-username/meta-spec.git
cd meta-spec

# 2. Install dependencies
uv sync --all-extras

# 3. Install pre-commit hooks
pre-commit install

# 4. Run tests
pytest

# 5. Start in development mode
python -m meta_spec.cli.main --help
```

---

## 📝 Code Standards

### Python Style

- Follow [PEP 8](https://pep8.org/)
- Use [Black](https://black.readthedocs.io/) for formatting
- Use [Ruff](https://docs.astral.sh/ruff/) for linting

```bash
# Format code
black .

# Lint code
ruff check .
```

### Type Annotations

- Use type annotations
- Run mypy checks

```bash
mypy meta_spec/
```

### Docstrings

```python
def function_name(param: str) -> int:
    """
    Brief description (one line)

    Detailed description (optional, multiple lines)

    Args:
        param: Parameter description

    Returns:
        Return value description

    Raises:
        Exception description (if any)

    Example:
        >>> function_name("test")
        42
    """
    pass
```

---

## 🧪 Testing

### Test Requirements

- New features must include tests
- Bug fixes should include regression tests
- Test coverage ≥ 80%

### Run Tests

```bash
# Run all tests
pytest

# Run specific tests
pytest tests/test_parser.py

# View coverage
pytest --cov=meta_spec --cov-report=html
```

### Test Structure

```
tests/
├── unit/           # Unit tests
├── integration/    # Integration tests
└── fixtures/       # Test fixtures
```

---

## 📚 Documentation

### Documentation Types

- **Code Documentation**: Function and class docstrings
- **User Documentation**: Markdown in `docs/` directory
- **Examples**: `examples/` directory

### Documentation Standards

- Clear and concise
- Include examples
- Keep up to date

---

## 🔀 Git Workflow

### Branch Naming

- `feature/xxx` - New features
- `fix/xxx` - Bug fixes
- `docs/xxx` - Documentation updates
- `refactor/xxx` - Refactoring
- `test/xxx` - Test-related

### Commit Messages

Follow [Conventional Commits](https://www.conventionalcommits.org/):

```
<type>(<scope>): <subject>

<body>

<footer>
```

Types:
- `feat`: New feature
- `fix`: Bug fix
- `docs`: Documentation
- `style`: Formatting
- `refactor`: Refactoring
- `test`: Testing
- `chore`: Build/tools

Example:
```
feat(parser): add YAML validation

- Implement JSON Schema validation
- Add error reporting
- Update tests

Closes #123
```

---

## 🎯 Pull Request

### PR Checklist

- [ ] Code follows style guidelines
- [ ] Added necessary tests
- [ ] All tests pass
- [ ] Updated relevant documentation
- [ ] Commit messages follow conventions
- [ ] Resolved all review comments

### PR Template

```markdown
## Description

Brief description of what this PR does

## Type

- [ ] Bug fix
- [ ] New feature
- [ ] Refactoring
- [ ] Documentation

## Testing

Describe how to test these changes

## Screenshots (if applicable)

## Related Issues

Closes #123
```

---

## 👥 Community

### Code of Conduct

We follow the [Contributor Covenant](https://www.contributor-covenant.org/):
- Respect and inclusivity
- Constructive feedback
- Focus on project goals

### Get Help

- **GitHub Issues**: Report problems
- **GitHub Discussions**: Discussions and questions
- **Email**: meta-spec@example.com

---

## 🏆 Contributors

Thanks to all contributors! Your name will appear in [CONTRIBUTORS.md](./CONTRIBUTORS.md)

---

**Thank you for your contribution!** ❤️
