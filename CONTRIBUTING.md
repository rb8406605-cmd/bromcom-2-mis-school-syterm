# Contributing to Bromcom

Thank you for your interest in contributing to Bromcom! This document provides guidelines and instructions for contributing to the project.

## Code of Conduct

We are committed to providing a welcoming and inclusive environment. Please be respectful and constructive in all interactions.

---

## Getting Started

### 1. Fork the Repository
```bash
# Fork on GitHub, then clone your fork
git clone https://github.com/YOUR_USERNAME/bromcom-2-mis-school-syterm.git
cd bromcom-2-mis-school-syterm
```

### 2. Add Upstream Remote
```bash
git remote add upstream https://github.com/rb8406605-cmd/bromcom-2-mis-school-syterm.git
```

### 3. Create Feature Branch
```bash
git checkout -b feature/your-feature-name
# or for bug fixes
git checkout -b bugfix/bug-description
```

### 4. Setup Development Environment
```bash
# Create virtual environment
python3 -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows

# Install dependencies
pip install -r requirements.txt
pip install -r requirements-dev.txt

# Setup pre-commit hooks (optional)
pre-commit install
```

---

## Development Workflow

### Code Style

We follow PEP 8 for Python and follow modern JavaScript conventions.

#### Python
```bash
# Format code with Black
black src/

# Sort imports with isort
isort src/

# Lint with flake8
flake8 src/
```

#### JavaScript
```bash
# Format with Prettier
prettier --write src/

# Lint with ESLint
eslint src/
```

### Running Tests
```bash
# Run all tests
pytest

# Run with coverage
pytest --cov=bromcom

# Run specific test
pytest tests/test_attendance.py::test_mark_attendance

# Watch mode
pytest --watch
```

### Database Migrations
```bash
# Create migrations
python manage.py makemigrations

# Run migrations
python manage.py migrate

# Show migration status
python manage.py showmigrations
```

---

## Commit Guidelines

### Commit Message Format
```
<type>(<scope>): <subject>

<body>

<footer>
```

### Types
- `feat`: A new feature
- `fix`: A bug fix
- `docs`: Documentation only changes
- `style`: Changes that don't affect code meaning
- `refactor`: Code change that neither fixes a bug nor adds a feature
- `perf`: Code change that improves performance
- `test`: Adding or updating tests
- `chore`: Changes to build process, dependencies, etc.

### Examples
```
feat(attendance): add bulk attendance marking

Allow teachers to mark attendance for entire class at once using
CSV import feature. Includes validation and error handling.

Closes #123
```

```
fix(detention): prevent duplicate detention assignments

Check for existing detention before creating new one.
Added unique constraint at database level.

Fixes #456
```

---

## Pull Request Process

### 1. Before Submitting
- [ ] Code passes all tests: `pytest`
- [ ] Code is properly formatted: `black` and `prettier`
- [ ] No linting issues: `flake8` and `eslint`
- [ ] Documentation is updated
- [ ] Changes are covered by tests
- [ ] Changelog is updated

### 2. Create Pull Request
```bash
# Push your feature branch
git push origin feature/your-feature-name
```

Then create a PR on GitHub with:
- Clear title describing the change
- Detailed description of what changed and why
- Reference to related issues: `Closes #123`
- Screenshots for UI changes

### 3. PR Template
```markdown
## Description
Brief description of changes

## Related Issue
Closes #(issue number)

## Type of Change
- [ ] Bug fix
- [ ] New feature
- [ ] Breaking change

## Testing
- [ ] Unit tests added/updated
- [ ] Integration tests added/updated
- [ ] Manual testing done

## Screenshots (if applicable)
Include screenshots for UI changes

## Checklist
- [ ] Code follows style guidelines
- [ ] Self-review completed
- [ ] Comments added for complex logic
- [ ] Documentation updated
- [ ] No new warnings generated
```

### 4. Code Review
- Address feedback from reviewers
- Make requested changes
- Push updates to the same branch
- Don't force push unless asked

---

## Reporting Issues

### Bug Report Template
```markdown
## Description
Clear description of the bug

## Steps to Reproduce
1. Go to '...'
2. Click on '...'
3. Observe error

## Expected Behavior
What should happen

## Actual Behavior
What actually happens

## Screenshots/Logs
Include error messages, logs, screenshots

## Environment
- OS: Windows 10 / Ubuntu 22.04 / macOS
- Python Version: 3.11
- Browser: Chrome 120
- Deployment: Local / Docker / AWS
```

### Feature Request Template
```markdown
## Description
Clear description of the requested feature

## Use Case
Why is this feature needed?

## Proposed Solution
How should this feature work?

## Alternative Solutions
Other ways to solve this problem

## Additional Context
Any other information
```

---

## Project Structure

```
bromcom-2-mis-school-syterm/
├── bromcom/                    # Main Django project
│   ├── settings.py            # Configuration
│   ├── urls.py               # URL routing
│   ├── wsgi.py               # WSGI config
│   └── celery.py             # Celery configuration
│
├── apps/                      # Django applications
│   ├── attendance/           # Attendance module
│   ├── behavior/             # Behavior management
│   ├── detention/            # Detention management
│   ├── users/                # User management
│   ├── notifications/        # Notifications
│   └── reports/              # Reporting
│
├── tests/                     # Test files
├── static/                    # Static files (CSS, JS, images)
├── media/                     # User uploaded files
├── docs/                      # Documentation
│
├── manage.py                  # Django CLI
├── requirements.txt           # Python dependencies
└── docker-compose.yml         # Docker configuration
```

---

## Adding a New Feature

### 1. Create Django App
```bash
python manage.py startapp feature_name
```

### 2. Create Models
Edit `apps/feature_name/models.py`:
```python
from django.db import models

class MyModel(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['-created_at']
        verbose_name_plural = 'My Models'
    
    def __str__(self):
        return self.name
```

### 3. Create Serializers
Edit `apps/feature_name/serializers.py`:
```python
from rest_framework import serializers
from .models import MyModel

class MyModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = MyModel
        fields = ['id', 'name', 'description', 'created_at']
        read_only_fields = ['created_at']
```

### 4. Create Views
Edit `apps/feature_name/views.py`:
```python
from rest_framework import viewsets, permissions
from .models import MyModel
from .serializers import MyModelSerializer

class MyModelViewSet(viewsets.ModelViewSet):
    queryset = MyModel.objects.all()
    serializer_class = MyModelSerializer
    permission_classes = [permissions.IsAuthenticated]
```

### 5. Add URL Routes
Edit `apps/feature_name/urls.py`:
```python
from django.urls import path
from . import views

urlpatterns = [
    path('', views.MyModelViewSet.as_view({'get': 'list'})),
]
```

### 6. Write Tests
Create `tests/test_feature_name.py`:
```python
from django.test import TestCase
from apps.feature_name.models import MyModel

class MyModelTestCase(TestCase):
    def setUp(self):
        MyModel.objects.create(name='Test', description='Test model')
    
    def test_model_creation(self):
        obj = MyModel.objects.get(name='Test')
        self.assertEqual(obj.description, 'Test model')
```

### 7. Update Documentation
- Add feature to `FEATURES.md`
- Update `API_DOCUMENTATION.md`
- Add to README if major feature

---

## Testing Guidelines

### Write Meaningful Tests
```python
def test_mark_attendance_with_valid_data(self):
    """Test marking attendance with all required fields"""
    response = self.client.post('/api/v1/attendance/', {
        'student_id': self.student.id,
        'date': '2024-01-15',
        'status': 'P'
    })
    self.assertEqual(response.status_code, 201)

def test_mark_attendance_without_required_field(self):
    """Test marking attendance without required date field"""
    response = self.client.post('/api/v1/attendance/', {
        'student_id': self.student.id,
        'status': 'P'
    })
    self.assertEqual(response.status_code, 400)
```

### Coverage Targets
- Aim for 80%+ code coverage
- Test happy path and error cases
- Test edge cases and boundaries
- Test API response codes and formats

---

## Documentation

### Docstring Format
```python
def mark_attendance(request):
    """
    Mark student attendance for a specific date.
    
    Args:
        request: HTTP request with attendance data
        
    Returns:
        JSON response with created attendance record or errors
        
    Raises:
        ValidationError: If required fields are missing or invalid
    """
```

### Comment Guidelines
- Explain WHY, not WHAT
- Keep comments up to date
- Use clear, concise language
- Avoid obvious comments

---

## Performance Considerations

- Use Django ORM efficiently (avoid N+1 queries)
- Add `.select_related()` and `.prefetch_related()`
- Cache database queries when appropriate
- Optimize API responses
- Profile code for bottlenecks

Example:
```python
# BAD - N+1 query problem
students = Student.objects.all()
for student in students:
    print(student.class.name)  # Queries database each iteration

# GOOD - Use select_related
students = Student.objects.select_related('class')
for student in students:
    print(student.class.name)  # No additional queries
```

---

## Security Checklist

Before submitting code:
- [ ] No hardcoded secrets or credentials
- [ ] Input validation on all endpoints
- [ ] SQL injection protection (use ORM)
- [ ] XSS protection enabled
- [ ] CSRF tokens used in forms
- [ ] Proper permission checks
- [ ] Rate limiting on endpoints
- [ ] Sensitive data not logged

---

## Release Process

1. Update version number in `__init__.py`
2. Update `CHANGELOG.md`
3. Create release branch: `git checkout -b release/v1.2.0`
4. Create tag: `git tag -a v1.2.0 -m "Release version 1.2.0"`
5. Push tag: `git push origin v1.2.0`
6. Create GitHub release with changelog

---

## Resources

- [Django Documentation](https://docs.djangoproject.com/)
- [Django REST Framework](https://www.django-rest-framework.org/)
- [Python Style Guide (PEP 8)](https://www.python.org/dev/peps/pep-0008/)
- [Git Guide](https://git-scm.com/doc)
- [Our API Documentation](API_DOCUMENTATION.md)
- [System Components](SYSTEM_COMPONENTS.md)

---

## Questions?

- Check existing [GitHub Issues](https://github.com/rb8406605-cmd/bromcom-2-mis-school-syterm/issues)
- Create a new issue with question label
- Join our community discussions

---

Thank you for contributing! 🎉

Your contributions help make Bromcom better for schools worldwide.
