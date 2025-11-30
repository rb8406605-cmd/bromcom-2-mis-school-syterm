# Bromcom API Documentation

## Base URL
```
http://localhost:8000/api/v1
```

## Authentication

All API requests require JWT authentication token in the header:

```bash
Authorization: Bearer <your-jwt-token>
```

### Get Token
```bash
POST /api/v1/auth/token/
Content-Type: application/json

{
  "username": "your-username",
  "password": "your-password"
}
```

Response:
```json
{
  "access": "eyJ0eXAiOiJKV1QiLCJhbGc...",
  "refresh": "eyJ0eXAiOiJKV1QiLCJhbGc..."
}
```

### Refresh Token
```bash
POST /api/v1/auth/token/refresh/
Content-Type: application/json

{
  "refresh": "your-refresh-token"
}
```

---

## API Endpoints

### 1. AUTHENTICATION

#### Register New User
```
POST /api/v1/auth/register/
{
  "username": "john_doe",
  "email": "john@example.com",
  "password": "secure_password",
  "password2": "secure_password",
  "first_name": "John",
  "last_name": "Doe",
  "role": "teacher"  // admin, teacher, parent, student
}
```

#### Get Current User
```
GET /api/v1/auth/me/
```

#### Logout
```
POST /api/v1/auth/logout/
```

---

### 2. STUDENTS

#### List All Students
```
GET /api/v1/students/
?class=1A
?search=John
?page=1
?limit=20
```

#### Get Student Details
```
GET /api/v1/students/{id}/
```

#### Create New Student
```
POST /api/v1/students/
{
  "admission_number": "2024001",
  "first_name": "John",
  "last_name": "Doe",
  "date_of_birth": "2010-05-15",
  "gender": "M",  // M or F
  "class": 1,
  "email": "john@school.com",
  "phone": "+1234567890",
  "parent_name": "Jane Doe",
  "parent_email": "jane@example.com",
  "address": "123 Main St"
}
```

#### Update Student
```
PUT /api/v1/students/{id}/
{
  "first_name": "Jonathan",
  "email": "jonathan@school.com"
}
```

#### Delete Student
```
DELETE /api/v1/students/{id}/
```

---

### 3. ATTENDANCE

#### Mark Attendance
```
POST /api/v1/attendance/
{
  "class_id": 1,
  "date": "2024-01-15",
  "records": [
    {
      "student_id": 1,
      "status": "P",  // P=Present, A=Absent, L=Late, E=Excused
      "time_in": "08:00",
      "notes": "Arrived late due to traffic"
    },
    {
      "student_id": 2,
      "status": "A",
      "notes": "Sick leave"
    }
  ]
}
```

#### Get Attendance Records
```
GET /api/v1/attendance/
?student_id=1
?class_id=1
?date=2024-01-15
?from_date=2024-01-01
?to_date=2024-01-31
?status=P
?page=1
?limit=50
```

#### Get Single Attendance Record
```
GET /api/v1/attendance/{id}/
```

#### Update Attendance Record
```
PUT /api/v1/attendance/{id}/
{
  "status": "E",
  "notes": "Updated to Excused"
}
```

#### Delete Attendance Record
```
DELETE /api/v1/attendance/{id}/
```

#### Get Attendance Summary
```
GET /api/v1/attendance/summary/
?student_id=1
?from_date=2024-01-01
?to_date=2024-01-31
```

Response:
```json
{
  "student_id": 1,
  "total_days": 20,
  "present": 18,
  "absent": 1,
  "late": 1,
  "excused": 0,
  "attendance_percentage": 90.0
}
```

---

### 4. BEHAVIOR & INCIDENTS

#### Log Behavior Incident
```
POST /api/v1/incidents/
{
  "student_id": 1,
  "date": "2024-01-15",
  "time": "14:30",
  "incident_type": "DISRUPTION",  // DISRUPTION, DISRESPECT, AGGRESSION, BULLYING, DISHONESTY, PROPERTY_DAMAGE, OTHER
  "severity": 2,  // 1=Minor, 2=Moderate, 3=Serious, 4=Critical
  "description": "Student disrupted class multiple times",
  "location": "Classroom 2A",
  "witness_name": "Mr. Smith",
  "action_taken": "Verbal warning",
  "points": 10
}
```

#### Get Behavior Incidents
```
GET /api/v1/incidents/
?student_id=1
?incident_type=DISRUPTION
?severity=2
?from_date=2024-01-01
?to_date=2024-01-31
?page=1
?limit=50
```

#### Get Incident Details
```
GET /api/v1/incidents/{id}/
```

#### Update Incident
```
PUT /api/v1/incidents/{id}/
{
  "action_taken": "Updated action",
  "severity": 3
}
```

#### Delete Incident
```
DELETE /api/v1/incidents/{id}/
```

#### Get Student Behavior Summary
```
GET /api/v1/incidents/student/{student_id}/summary/
```

Response:
```json
{
  "student_id": 1,
  "total_incidents": 5,
  "total_points": 35,
  "by_type": {
    "DISRUPTION": 2,
    "DISRESPECT": 2,
    "OTHER": 1
  },
  "by_severity": {
    "1": 1,
    "2": 2,
    "3": 2,
    "4": 0
  },
  "last_incident": "2024-01-15"
}
```

---

### 5. DETENTION

#### Assign Detention
```
POST /api/v1/detention/
{
  "student_id": 1,
  "incident_id": 5,
  "date": "2024-01-17",
  "start_time": "15:00",
  "end_time": "16:00",
  "duration_minutes": 60,
  "supervisor_id": 3,
  "reason": "Follow-up to behavior incident",
  "status": "ASSIGNED"  // ASSIGNED, COMPLETED, CANCELLED
}
```

#### Get Detention Records
```
GET /api/v1/detention/
?student_id=1
?status=ASSIGNED
?from_date=2024-01-01
?to_date=2024-01-31
?supervisor_id=3
?page=1
?limit=50
```

#### Get Single Detention Record
```
GET /api/v1/detention/{id}/
```

#### Update Detention Status
```
PUT /api/v1/detention/{id}/
{
  "status": "COMPLETED",
  "completion_time": "16:00",
  "notes": "Student completed detention, good behavior"
}
```

#### Cancel Detention
```
DELETE /api/v1/detention/{id}/
```

#### Get Detention Schedule
```
GET /api/v1/detention/schedule/
?date=2024-01-17
?supervisor_id=3
```

---

### 6. CLASSES

#### List All Classes
```
GET /api/v1/classes/
?grade=9
?section=A
?search=Science
```

#### Get Class Details
```
GET /api/v1/classes/{id}/
```

#### Create Class
```
POST /api/v1/classes/
{
  "name": "9A",
  "grade": 9,
  "section": "A",
  "class_teacher_id": 2,
  "room_number": "201",
  "total_students": 35,
  "shift": "MORNING"  // MORNING, AFTERNOON
}
```

#### Update Class
```
PUT /api/v1/classes/{id}/
{
  "class_teacher_id": 3,
  "total_students": 36
}
```

#### Get Class Attendance Stats
```
GET /api/v1/classes/{id}/attendance-stats/
?from_date=2024-01-01
?to_date=2024-01-31
```

---

### 7. REPORTS

#### Generate Attendance Report
```
GET /api/v1/reports/attendance/
?class_id=1
?from_date=2024-01-01
?to_date=2024-01-31
?format=pdf  // pdf, csv, json, excel
```

#### Generate Behavior Report
```
GET /api/v1/reports/behavior/
?student_id=1
?from_date=2024-01-01
?to_date=2024-01-31
?format=pdf
```

#### Generate Detention Report
```
GET /api/v1/reports/detention/
?class_id=1
?supervisor_id=2
?from_date=2024-01-01
?to_date=2024-01-31
?format=csv
```

#### Generate Class Summary Report
```
GET /api/v1/reports/class-summary/
?class_id=1
?from_date=2024-01-01
?to_date=2024-01-31
```

---

### 8. NOTIFICATIONS

#### Send Notification
```
POST /api/v1/notifications/
{
  "recipient_id": 1,
  "title": "Attendance Alert",
  "message": "Your child has been absent 3 days this week",
  "notification_type": "EMAIL",  // EMAIL, SMS, PUSH, IN_APP
  "priority": "HIGH"
}
```

#### Get Notifications
```
GET /api/v1/notifications/
?user_id=1
?read=false
?type=EMAIL
```

#### Mark Notification as Read
```
PUT /api/v1/notifications/{id}/
{
  "read": true
}
```

---

### 9. USERS & ROLES

#### List Users
```
GET /api/v1/users/
?role=teacher
?search=john
?page=1
```

#### Get User Details
```
GET /api/v1/users/{id}/
```

#### Update User Profile
```
PUT /api/v1/users/{id}/
{
  "first_name": "John",
  "email": "john.new@school.com",
  "phone": "+1234567890"
}
```

#### Change Password
```
POST /api/v1/users/{id}/change-password/
{
  "old_password": "current_password",
  "new_password": "new_password"
}
```

---

### 10. ADMIN ENDPOINTS

#### Dashboard Stats
```
GET /api/v1/admin/dashboard/
```

Response:
```json
{
  "total_students": 1245,
  "total_teachers": 45,
  "total_classes": 35,
  "today_attendance_rate": 94.5,
  "pending_detentions": 12,
  "recent_incidents": 5,
  "total_incidents_this_month": 23
}
```

#### System Health
```
GET /api/v1/admin/health/
```

#### Settings
```
GET /api/v1/admin/settings/
PUT /api/v1/admin/settings/
```

---

## Error Responses

### 400 Bad Request
```json
{
  "error": "Bad Request",
  "details": {
    "field_name": ["Error message"]
  }
}
```

### 401 Unauthorized
```json
{
  "error": "Unauthorized",
  "message": "Invalid or expired token"
}
```

### 403 Forbidden
```json
{
  "error": "Forbidden",
  "message": "You don't have permission to access this resource"
}
```

### 404 Not Found
```json
{
  "error": "Not Found",
  "message": "Resource not found"
}
```

### 500 Server Error
```json
{
  "error": "Server Error",
  "message": "An unexpected error occurred"
}
```

---

## Rate Limiting

- **Default**: 1000 requests per hour per user
- **Headers**:
  - `X-RateLimit-Limit`: Total limit
  - `X-RateLimit-Remaining`: Remaining requests
  - `X-RateLimit-Reset`: Reset timestamp

---

## Pagination

All list endpoints support pagination:

```
GET /api/v1/resource/?page=1&limit=20
```

Response:
```json
{
  "count": 100,
  "total_pages": 5,
  "next": "http://localhost:8000/api/v1/resource/?page=2",
  "previous": null,
  "results": [...]
}
```

---

## Filtering & Searching

Example:
```
GET /api/v1/students/?search=john&class=1A&status=ACTIVE
```

Supported operators:
- `search` - Text search on name, email, etc.
- `date_from` - Filter by start date
- `date_to` - Filter by end date
- `status` - Filter by status
- `ordering` - Sort by field: `?ordering=-date` (descending)

---

## Webhooks (Optional)

Register webhook for events:
```
POST /api/v1/webhooks/
{
  "event_type": "attendance_marked",
  "url": "https://yourapp.com/webhook",
  "active": true
}
```

Events:
- `attendance_marked`
- `incident_logged`
- `detention_assigned`
- `notification_sent`

---

## Rate Limits & Throttling

- **Anonymous users**: 100 requests/hour
- **Authenticated users**: 1000 requests/hour
- **Admin users**: Unlimited

---

## API Versioning

Current version: **v1**

Future versions will be available at:
- `/api/v2/` (planned)

---

## SDK & Client Libraries

### Python
```python
import requests

token = "your-jwt-token"
headers = {"Authorization": f"Bearer {token}"}

response = requests.get(
    "http://localhost:8000/api/v1/students/",
    headers=headers
)
```

### JavaScript
```javascript
const response = await fetch('http://localhost:8000/api/v1/students/', {
  headers: {
    'Authorization': `Bearer ${token}`
  }
});
```

---

**Last Updated**: December 2024  
**Version**: 1.0

For more information, check the [Features Documentation](FEATURES.md) or [System Components](SYSTEM_COMPONENTS.md).
