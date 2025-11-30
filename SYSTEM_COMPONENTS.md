# Bromcom - System Components & Configuration

## Part 1: Key System Components

### 1.1 Frontend Components Architecture

#### Authentication Components
```
LoginComponent
├── Email Input Field
├── Password Input Field
├── Remember Me Checkbox
├── Forgot Password Link
├── Login Button
└── Sign Up Link

RegistrationComponent
├── Email Field
├── Password Field
├── Confirm Password Field
├── Full Name Field
├── Role Selection
├── School Selection
└── Submit Button
```

#### Attendance Components
```
AttendanceFormComponent
├── Class Selection Dropdown
├── Date Picker
├── Student List Table
│   ├── Student Name Column
│   ├── Status Radio Buttons (P/A/L/E)
│   ├── Time Input
│   └── Notes Text Area
├── Bulk Mark Present Button
├── Submit Button
└── Save as Draft Button

AttendanceListComponent
├── Filter Section
│   ├── Date Range Filter
│   ├── Class Filter
│   └── Status Filter
├── Attendance Table
│   ├── Student Name
│   ├── Date
│   ├── Status
│   ├── Time
│   └── Actions (Edit, Delete)
├── Pagination
└── Export to CSV Button
```

#### Behavior Components
```
BehaviorIncidentForm
├── Student Selection
├── Incident Type Dropdown
├── Severity Level Selector
├── Description Text Area
├── Evidence Upload
├── Witnesses Field
├── Location Input
├── Date/Time Picker
└── Submit Button

BehaviorDashboard
├── Student Behavior Card
│   ├── Total Behavior Points
│   ├── Recent Incidents List
│   ├── Incident Timeline
│   └── View Full History Link
├── Class Behavior Stats
│   ├── Total Incidents by Type
│   ├── Severity Distribution
│   └── Top Offenders List
└── Behavior Alerts
    └── Students Needing Intervention
```

#### Detention Components
```
DetentionScheduleComponent
├── Calendar View
├── Detention Session Cards
│   ├── Date and Time
│   ├── Duration
│   ├── Assigned Students
│   ├── Supervisor
│   └── Room Location
├── Add New Detention Button
└── View Detention Details

DetentionFormComponent
├── Student Selection
├── Reason/Incident Link
├── Detention Type Selection
├── Date/Time Picker
├── Duration Selection
├── Supervisor Assignment
├── Room Assignment
├── Special Instructions
└── Submit Button
```

### 1.2 Backend API Endpoints Structure

#### Authentication Endpoints
```
POST   /api/v1/auth/register          - User registration
POST   /api/v1/auth/login             - User login
POST   /api/v1/auth/logout            - User logout
POST   /api/v1/auth/refresh-token     - Refresh JWT token
POST   /api/v1/auth/forgot-password   - Password reset request
POST   /api/v1/auth/reset-password    - Reset password
GET    /api/v1/auth/me                - Get current user info
PUT    /api/v1/auth/profile           - Update user profile
```

#### Attendance Endpoints
```
GET    /api/v1/attendance/            - List attendance records
POST   /api/v1/attendance/            - Create attendance record
GET    /api/v1/attendance/{id}        - Get attendance detail
PUT    /api/v1/attendance/{id}        - Update attendance record
DELETE /api/v1/attendance/{id}        - Delete attendance record
POST   /api/v1/attendance/bulk-import - Bulk import from CSV
GET    /api/v1/attendance/by-student/{student_id} - Student attendance history
GET    /api/v1/attendance/by-class/{class_id}     - Class attendance
GET    /api/v1/attendance/report     - Attendance report
```

#### Behavior Endpoints
```
GET    /api/v1/behavior/incidents     - List behavior incidents
POST   /api/v1/behavior/incidents     - Create incident
GET    /api/v1/behavior/incidents/{id} - Get incident detail
PUT    /api/v1/behavior/incidents/{id} - Update incident
DELETE /api/v1/behavior/incidents/{id} - Delete incident
GET    /api/v1/behavior/student/{id}  - Student behavior profile
POST   /api/v1/behavior/upload-evidence - Upload incident evidence
GET    /api/v1/behavior/report        - Behavior report
GET    /api/v1/behavior/analytics     - Behavior analytics
```

#### Detention Endpoints
```
GET    /api/v1/detention/             - List detentions
POST   /api/v1/detention/             - Create detention
GET    /api/v1/detention/{id}         - Get detention detail
PUT    /api/v1/detention/{id}         - Update detention
DELETE /api/v1/detention/{id}         - Cancel detention
PUT    /api/v1/detention/{id}/mark-complete - Mark detention complete
GET    /api/v1/detention/schedule     - Get detention schedule
GET    /api/v1/detention/student/{id} - Student detention history
POST   /api/v1/detention/bulk-assign  - Bulk assign detentions
```

#### Notification Endpoints
```
GET    /api/v1/notifications/         - Get all notifications
POST   /api/v1/notifications/         - Create notification
PUT    /api/v1/notifications/{id}/read - Mark as read
DELETE /api/v1/notifications/{id}     - Delete notification
GET    /api/v1/notifications/unread   - Get unread count
POST   /api/v1/notifications/preferences - Update preferences
```

#### Reports Endpoints
```
GET    /api/v1/reports/attendance     - Generate attendance report
GET    /api/v1/reports/behavior       - Generate behavior report
GET    /api/v1/reports/detention      - Generate detention report
GET    /api/v1/reports/custom         - Generate custom report
POST   /api/v1/reports/export         - Export report
GET    /api/v1/reports/history        - Previously generated reports
```

#### User Management Endpoints
```
GET    /api/v1/users/                 - List users (admin only)
POST   /api/v1/users/                 - Create user (admin only)
GET    /api/v1/users/{id}             - Get user detail
PUT    /api/v1/users/{id}             - Update user
DELETE /api/v1/users/{id}             - Delete user (admin only)
GET    /api/v1/users/roles            - Get available roles
GET    /api/v1/users/permissions      - Get user permissions
```

#### Student Endpoints
```
GET    /api/v1/students/              - List students
POST   /api/v1/students/              - Create student
GET    /api/v1/students/{id}          - Get student profile
PUT    /api/v1/students/{id}          - Update student info
GET    /api/v1/students/{id}/summary  - Student summary
GET    /api/v1/students/{id}/records  - All student records
```

#### Class Endpoints
```
GET    /api/v1/classes/               - List classes
POST   /api/v1/classes/               - Create class
GET    /api/v1/classes/{id}           - Get class detail
PUT    /api/v1/classes/{id}           - Update class
GET    /api/v1/classes/{id}/students  - Get class students
GET    /api/v1/classes/{id}/stats     - Class statistics
```

### 1.3 Database Models

#### User Model
```python
class User(models.Model):
    id = UUID (Primary Key)
    username = CharField (unique)
    email = EmailField (unique)
    password = CharField (hashed)
    first_name = CharField
    last_name = CharField
    role = ChoiceField (admin, teacher, parent, student)
    school = ForeignKey (School)
    is_active = BooleanField
    is_email_verified = BooleanField
    is_phone_verified = BooleanField
    phone_number = CharField (optional)
    profile_picture = ImageField (optional)
    last_login = DateTimeField
    created_at = DateTimeField
    updated_at = DateTimeField
```

#### Student Model
```python
class Student(models.Model):
    id = UUID (Primary Key)
    user = OneToOneField (User)
    student_id = CharField (unique)
    class_assignment = ForeignKey (Class)
    parent = ForeignKey (User, role='parent')
    admission_date = DateField
    enrollment_status = ChoiceField (active, inactive, graduated)
    date_of_birth = DateField
    gender = ChoiceField (M, F, Other)
    address = TextField
    emergency_contact = CharField
    medical_conditions = TextField
    created_at = DateTimeField
    updated_at = DateTimeField
```

#### Class Model
```python
class Class(models.Model):
    id = UUID (Primary Key)
    class_name = CharField
    school = ForeignKey (School)
    teacher = ForeignKey (User, role='teacher')
    academic_year = CharField
    max_students = IntegerField
    grade_level = CharField
    created_at = DateTimeField
    updated_at = DateTimeField
```

#### Attendance Model
```python
class Attendance(models.Model):
    id = UUID (Primary Key)
    student = ForeignKey (Student)
    class_assignment = ForeignKey (Class)
    date = DateField
    status = ChoiceField (Present, Absent, Late, Excused)
    time_in = TimeField (optional)
    time_out = TimeField (optional)
    notes = TextField
    marked_by = ForeignKey (User, role='teacher')
    created_at = DateTimeField
    updated_at = DateTimeField
    
    Unique Constraint: (student, date)
```

#### BehaviorIncident Model
```python
class BehaviorIncident(models.Model):
    id = UUID (Primary Key)
    student = ForeignKey (Student)
    incident_type = CharField (Disruption, Disrespect, Bullying, etc.)
    severity = IntegerField (1-4)
    points = IntegerField (calculated from severity)
    description = TextField
    reported_by = ForeignKey (User)
    incident_date = DateTimeField
    location = CharField
    witnesses = ManyToMany (User, optional)
    evidence = FileField (optional, multiple)
    resolution = TextField (optional)
    is_resolved = BooleanField
    created_at = DateTimeField
    updated_at = DateTimeField
```

#### Detention Model
```python
class Detention(models.Model):
    id = UUID (Primary Key)
    student = ForeignKey (Student)
    reason = CharField
    incident = ForeignKey (BehaviorIncident, optional)
    detention_type = ChoiceField (In-school, After-school, Weekend, Saturday)
    scheduled_date = DateField
    scheduled_time = TimeField
    duration = IntegerField (minutes)
    supervisor = ForeignKey (User, role='teacher')
    room_location = CharField
    status = ChoiceField (Scheduled, Completed, Cancelled, No-show)
    notes = TextField
    completion_time = DateTimeField (optional)
    supervisor_notes = TextField (optional)
    created_at = DateTimeField
    updated_at = DateTimeField
```

#### Notification Model
```python
class Notification(models.Model):
    id = UUID (Primary Key)
    user = ForeignKey (User)
    notification_type = ChoiceField (Attendance, Behavior, Detention, System)
    subject = CharField
    message = TextField
    is_read = BooleanField
    recipient = CharField (email, sms, in-app)
    related_model = CharField (Student, Class, etc.)
    related_id = UUID
    created_at = DateTimeField
    expires_at = DateTimeField
    read_at = DateTimeField (optional)
```

#### Report Model
```python
class Report(models.Model):
    id = UUID (Primary Key)
    report_type = ChoiceField (Attendance, Behavior, Detention, Custom)
    title = CharField
    generated_by = ForeignKey (User)
    description = TextField
    filters = JSONField (date_range, class_id, etc.)
    file_type = ChoiceField (PDF, CSV, Excel, JSON)
    file_path = CharField
    generated_at = DateTimeField
    expires_at = DateTimeField
    is_public = BooleanField
    view_count = IntegerField
```

---

## Part 2: Configuration Files

### 2.1 Django Settings (settings.py)

```python
# Core Configuration
SECRET_KEY = os.environ.get('SECRET_KEY')
DEBUG = os.environ.get('DEBUG', False)
ALLOWED_HOSTS = os.environ.get('ALLOWED_HOSTS', '').split(',')
CSRF_TRUSTED_ORIGINS = [...]

# Installed Apps
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    
    # Third-party
    'rest_framework',
    'django_filters',
    'corsheaders',
    'django_celery_beat',
    'django_celery_results',
    'channels',
    'drf_spectacular',  # API documentation
    
    # Local apps
    'apps.users',
    'apps.attendance',
    'apps.behavior',
    'apps.detention',
    'apps.notifications',
    'apps.reports',
    'apps.api',
]

# Database Configuration
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.environ.get('DB_NAME'),
        'USER': os.environ.get('DB_USER'),
        'PASSWORD': os.environ.get('DB_PASSWORD'),
        'HOST': os.environ.get('DB_HOST'),
        'PORT': os.environ.get('DB_PORT', 5432),
    }
}

# Cache Configuration
CACHES = {
    'default': {
        'BACKEND': 'django_redis.cache.RedisCache',
        'LOCATION': os.environ.get('REDIS_URL', 'redis://127.0.0.1:6379/1'),
        'OPTIONS': {
            'CLIENT_CLASS': 'django_redis.client.DefaultClient',
            'SOCKET_CONNECT_TIMEOUT': 5,
            'SOCKET_TIMEOUT': 5,
            'COMPRESSOR': 'django_redis.compressors.zlib.ZlibCompressor',
        }
    }
}

# Email Configuration
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = os.environ.get('EMAIL_HOST')
EMAIL_PORT = os.environ.get('EMAIL_PORT', 587)
EMAIL_USE_TLS = True
EMAIL_HOST_USER = os.environ.get('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = os.environ.get('EMAIL_HOST_PASSWORD')
DEFAULT_FROM_EMAIL = 'noreply@bromcom.school'

# Celery Configuration
CELERY_BROKER_URL = os.environ.get('CELERY_BROKER_URL', 'redis://localhost:6379/0')
CELERY_RESULT_BACKEND = os.environ.get('CELERY_RESULT_BACKEND', 'redis://localhost:6379/0')
CELERY_ACCEPT_CONTENT = ['json']
CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'
CELERY_TIMEZONE = 'UTC'

# REST Framework Configuration
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ],
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticated',
    ],
    'DEFAULT_FILTER_BACKENDS': [
        'django_filters.rest_framework.DjangoFilterBackend',
        'rest_framework.filters.SearchFilter',
        'rest_framework.filters.OrderingFilter',
    ],
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 20,
    'DEFAULT_SCHEMA_CLASS': 'drf_spectacular.openapi.AutoSchema',
}

# JWT Configuration
SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(hours=1),
    'REFRESH_TOKEN_LIFETIME': timedelta(days=1),
    'ALGORITHM': 'HS256',
}

# CORS Configuration
CORS_ALLOWED_ORIGINS = os.environ.get('CORS_ALLOWED_ORIGINS', '').split(',')

# Logging Configuration
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': '{levelname} {asctime} {module} {process:d} {thread:d} {message}',
            'style': '{',
        },
    },
    'handlers': {
        'file': {
            'level': 'INFO',
            'class': 'logging.FileHandler',
            'filename': '/var/log/bromcom/debug.log',
            'formatter': 'verbose',
        },
        'console': {
            'class': 'logging.StreamHandler',
            'formatter': 'verbose',
        },
    },
    'root': {
        'handlers': ['file', 'console'],
        'level': 'INFO',
    },
}

# Security Settings
SECURE_SSL_REDIRECT = True
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
SECURE_HSTS_SECONDS = 31536000
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_HSTS_PRELOAD = True
```

### 2.2 Docker Compose Configuration

```yaml
version: '3.8'

services:
  # Database Service
  db:
    image: postgres:15-alpine
    environment:
      POSTGRES_DB: ${DB_NAME}
      POSTGRES_USER: ${DB_USER}
      POSTGRES_PASSWORD: ${DB_PASSWORD}
    volumes:
      - postgres_data:/var/lib/postgresql/data
    ports:
      - "5432:5432"
    healthcheck:
      test: ["CMD-SHELL", "pg_isready -U ${DB_USER}"]
      interval: 10s
      timeout: 5s
      retries: 5

  # Redis Cache Service
  redis:
    image: redis:7-alpine
    ports:
      - "6379:6379"
    volumes:
      - redis_data:/data
    healthcheck:
      test: ["CMD", "redis-cli", "ping"]
      interval: 10s
      timeout: 5s
      retries: 5

  # Backend Service
  backend:
    build:
      context: ./backend
      dockerfile: Dockerfile
    command: gunicorn bromcom.wsgi:application --bind 0.0.0.0:8000
    environment:
      - DEBUG=${DEBUG}
      - SECRET_KEY=${SECRET_KEY}
      - DATABASE_URL=postgresql://${DB_USER}:${DB_PASSWORD}@db:5432/${DB_NAME}
      - REDIS_URL=redis://redis:6379/0
    ports:
      - "8000:8000"
    depends_on:
      db:
        condition: service_healthy
      redis:
        condition: service_healthy
    volumes:
      - ./backend:/app
      - static_volume:/app/staticfiles
      - media_volume:/app/media

  # Celery Worker Service
  celery:
    build:
      context: ./backend
      dockerfile: Dockerfile
    command: celery -A bromcom worker --loglevel=info
    environment:
      - DEBUG=${DEBUG}
      - SECRET_KEY=${SECRET_KEY}
      - DATABASE_URL=postgresql://${DB_USER}:${DB_PASSWORD}@db:5432/${DB_NAME}
      - REDIS_URL=redis://redis:6379/0
    depends_on:
      - db
      - redis
      - backend
    volumes:
      - ./backend:/app

  # Celery Beat Service
  celery-beat:
    build:
      context: ./backend
      dockerfile: Dockerfile
    command: celery -A bromcom beat --loglevel=info
    environment:
      - DEBUG=${DEBUG}
      - SECRET_KEY=${SECRET_KEY}
      - DATABASE_URL=postgresql://${DB_USER}:${DB_PASSWORD}@db:5432/${DB_NAME}
      - REDIS_URL=redis://redis:6379/0
    depends_on:
      - db
      - redis
      - backend

  # Frontend Service
  frontend:
    build:
      context: ./frontend
      dockerfile: Dockerfile
    ports:
      - "3000:3000"
    depends_on:
      - backend
    volumes:
      - ./frontend:/app
      - node_modules:/app/node_modules

  # Nginx Reverse Proxy
  nginx:
    image: nginx:alpine
    ports:
      - "80:80"
      - "443:443"
    volumes:
      - ./config/nginx.conf:/etc/nginx/nginx.conf:ro
      - static_volume:/app/staticfiles:ro
      - media_volume:/app/media:ro
      - ./ssl:/etc/nginx/ssl:ro
    depends_on:
      - backend
      - frontend

volumes:
  postgres_data:
  redis_data:
  static_volume:
  media_volume:
  node_modules:
```

### 2.3 Environment Configuration (.env)

```env
# Server Configuration
DEBUG=False
SECRET_KEY=your-secret-key-here
ALLOWED_HOSTS=localhost,127.0.0.1,bromcom.local,api.bromcom.local

# Database Configuration
DB_ENGINE=django.db.backends.postgresql
DB_NAME=bromcom_db
DB_USER=bromcom_user
DB_PASSWORD=secure_password_here
DB_HOST=localhost
DB_PORT=5432

# Redis Configuration
REDIS_URL=redis://localhost:6379/0
CACHE_TIMEOUT=300

# Email Configuration
EMAIL_BACKEND=django.core.mail.backends.smtp.EmailBackend
EMAIL_HOST=smtp.sendgrid.net
EMAIL_PORT=587
EMAIL_USE_TLS=True
EMAIL_HOST_USER=apikey
EMAIL_HOST_PASSWORD=your-sendgrid-api-key
DEFAULT_FROM_EMAIL=noreply@bromcom.school

# SMS Configuration
SMS_PROVIDER=twilio
TWILIO_ACCOUNT_SID=your-twilio-sid
TWILIO_AUTH_TOKEN=your-twilio-token
TWILIO_PHONE_NUMBER=+1234567890

# AWS Configuration
AWS_ACCESS_KEY_ID=your-aws-key
AWS_SECRET_ACCESS_KEY=your-aws-secret
AWS_STORAGE_BUCKET_NAME=bromcom-storage
AWS_S3_REGION_NAME=us-east-1

# Celery Configuration
CELERY_BROKER_URL=redis://localhost:6379/0
CELERY_RESULT_BACKEND=redis://localhost:6379/0

# JWT Configuration
JWT_SECRET_KEY=your-jwt-secret-key
JWT_ALGORITHM=HS256

# CORS Configuration
CORS_ALLOWED_ORIGINS=http://localhost:3000,https://bromcom.local

# Application Configuration
APP_NAME=Bromcom
SCHOOL_NAME=Your School Name
ACADEMIC_YEAR=2024-2025
```

---

## Part 3: System Requirements

### 3.1 System Requirements

#### Minimum (Small Deployment)
- CPU: 2 cores
- RAM: 4 GB
- Storage: 20 GB SSD
- Network: 1 Mbps

#### Recommended (Medium Deployment)
- CPU: 4 cores
- RAM: 8 GB
- Storage: 100 GB SSD
- Network: 10 Mbps

#### Production (Large Deployment)
- CPU: 8+ cores
- RAM: 16+ GB
- Storage: 500+ GB SSD
- Network: 100 Mbps
- Load Balancer
- Database Replication
- Backup Storage

### 3.2 Software Requirements

#### Core Requirements
- Python 3.9+
- Node.js 16+
- PostgreSQL 12+
- Redis 6+
- Docker & Docker Compose

#### Development Tools
- Git
- Visual Studio Code / PyCharm
- Postman (for API testing)
- DBeaver (for database management)

---

## Version & Support

- **Created**: 2024
- **Last Updated**: December 2024
- **Version**: 1.0
- **Status**: Active

