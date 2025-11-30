# Bromcom - School Management System

## 📌 Project Overview

**Bromcom** is a comprehensive **Attendance, Behavior & Detention Management System** designed for schools to track and manage:

- ✅ **Student Attendance** - Daily roll call, late marking, absence tracking
- ⚠️ **Behavioral Records** - Incident logging, severity tracking, analytics
- 📌 **Detention Management** - Assignment, scheduling, supervision, completion tracking
- 📊 **Reporting & Analytics** - Comprehensive reports, trends, insights
- 🔔 **Notifications** - Automated alerts to parents, teachers, and administrators

---

## 🚀 Quick Start

### View the Website Interface

1. **Option 1: Open in Browser**
   ```bash
   open index.html
   ```

2. **Option 2: Using Python's Built-in Server**
   ```bash
   python3 -m http.server 8000
   ```

---

## 📂 Project Structure

```
bromcom-2-mis-school-syterm/
├── index.html                      # Website interface
├── FEATURES.md                     # Feature documentation
├── DATA_ENTRY_GUIDE.md            # Data entry guide
├── TECHNOLOGY_STACK.md            # Tech stack and architecture
├── SYSTEM_COMPONENTS.md           # System components
├── attendance_entry_tool.py       # Interactive attendance entry
├── attendance_spreadsheet.py      # Spreadsheet-style entry
├── attendance_input_template.txt  # Manual entry template
└── README.md                      # This file
```

---

## 🎯 Key Features

### Dashboard
- Overview metrics and statistics
- Real-time key performance indicators
- Quick navigation to all sections

### Attendance Management
- Mark daily attendance with status (Present/Absent/Late/Excused)
- View attendance records with filtering
- Generate attendance reports
- **Data Entry Methods:**
  - Interactive tool: `python3 attendance_entry_tool.py`
  - Spreadsheet format: `python3 attendance_spreadsheet.py`
  - Manual template: Edit `attendance_input_template.txt`

### Behavioral Management
- Log behavioral incidents with type and severity
- View incident history with analytics
- Track behavior points and escalations

### Detention Management
- Assign detentions linked to incidents
- Schedule detention sessions
- Track supervision and completion

### Reports & Analytics
- Attendance reports (daily, weekly, monthly, yearly)
- Behavioral analytics and trend analysis
- Detention summaries
- Export to PDF, CSV, JSON

---

## 🔧 Data Entry Methods

### Method 1: Interactive Tool
```bash
python3 attendance_entry_tool.py
```
- Guided prompts for easy data entry
- Automatic formatting with proper spacing
- Auto-export to CSV
- Perfect for daily attendance marking

### Method 2: Spreadsheet-Style
```bash
python3 attendance_spreadsheet.py
```
- Creates TSV templates for bulk entry
- Fast batch processing
- Support for CSV/JSON export

### Method 3: Manual Template
Edit `attendance_input_template.txt` with proper spacing and formatting

---

## 📋 Data Reference

### Attendance Codes
| Code | Meaning |
|------|---------|
| P    | Present |
| A    | Absent  |
| L    | Late    |
| E    | Excused |

### Behavior Severity
- Level 1: Minor (5 points)
- Level 2: Moderate (10 points)
- Level 3: Serious (15 points)
- Level 4: Critical (20 points)

---

## 🎓 User Roles

- **Administrator**: Full system access, user management, configuration
- **Teacher**: Mark attendance, log incidents, assign detentions
- **Parent**: View child's records, receive notifications
- **Student**: View personal records and attendance

---

## 📊 Report Types

- **Attendance Reports**: Daily registers, summaries, absence tracking
- **Behavioral Reports**: Incident analysis, student profiles, trends
- **Detention Reports**: Assignments, completion rates, staff load
- **Export Formats**: PDF, CSV, JSON

---

## 🔐 Security

- User authentication with role-based access control
- Data encryption for secure transmission
- Audit trails for all system changes
- GDPR/FERPA compliant

---

## 🛠️ Technologies

### Frontend
- HTML5, CSS3, Vanilla JavaScript
- Responsive design for all devices

### Backend (Recommended)
- Python (Django/Flask)
- PostgreSQL database
- Redis caching
- Celery for background tasks

### External Services
- SendGrid (Email notifications)
- Twilio (SMS notifications)
- AWS S3 (File storage)

---

## 📱 Browser Support

✅ Chrome, Firefox, Safari, Edge, Mobile browsers (all latest versions)

---

## 📚 Documentation

- **FEATURES.md** - Complete feature list (10+ features)
- **DATA_ENTRY_GUIDE.md** - How to use data entry tools
- **TECHNOLOGY_STACK.md** - Architecture and tech choices
- **SYSTEM_COMPONENTS.md** - API endpoints and database models

---

## 🚀 Getting Started

1. **View Interface**: Open `index.html` in your browser
2. **Enter Data**: Run `python3 attendance_entry_tool.py`
3. **Read Docs**: Check individual documentation files
4. **Deploy**: Use Docker or cloud deployment options

---

**Questions?** Check the relevant documentation file for detailed information. 
