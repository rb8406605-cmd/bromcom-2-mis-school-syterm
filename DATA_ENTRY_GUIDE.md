# Bromcom Attendance & Behavior Entry Guide

## Overview
This guide explains how to enter attendance and behavior data with proper spacing, sections, and spreadsheet-like formatting.

---

## Method 1: Interactive Entry Tool (Recommended for Beginners)

### What It Is
An interactive Python script that walks you through entering attendance and behavior data with prompts and formatted output.

### How to Use

1. **Start the Tool**
   ```bash
   python3 attendance_entry_tool.py
   ```

2. **Follow the Prompts**
   - Enter class information (date, class, teacher, subject)
   - Enter student attendance records one by one
   - Optionally enter behavioral incidents
   - Optionally enter detention assignments

3. **Features**
   - ✓ Automatic spacing and formatting
   - ✓ Clear section separation
   - ✓ Input validation
   - ✓ Summary display
   - ✓ Auto-export to CSV

### Example Interaction

```
================================================================================
                    BROMCOM ATTENDANCE & BEHAVIOR ENTRY TOOL
================================================================================

CLASS INFORMATION
================================================================================
Date (YYYY-MM-DD) [Today]: 2024-12-01
Class/Grade: 10A
Teacher Name: Mr. Smith
Subject/Period: English

✓ Class information saved

STUDENT ATTENDANCE RECORDS
================================================================================
Enter student information. Press ENTER after each field:
Status: P=Present, A=Absent, L=Late, E=Excused
Time format: HH:MM (e.g., 09:30)
Type 'done' when finished.

[1] Student Name (or 'done'): John Smith
  Status (P/A/L/E): P
  Time (HH:MM) [--:--]: 09:00
  Notes: 
  John Smith          | P          | 09:00      |

[2] Student Name (or 'done'): Jane Doe
  Status (P/A/L/E): P
  Time (HH:MM) [--:--]: 09:05
  Notes: Late arrival
  Jane Doe            | P          | 09:05      | Late arrival

[3] Student Name (or 'done'): done

✓ 2 attendance records saved
```

---

## Method 2: Spreadsheet-Style Entry (Recommended for Quick Data Entry)

### What It Is
Use a tab-separated values (TSV) file - like a spreadsheet but in text format.

### How to Use

1. **Generate Templates**
   ```bash
   python3 attendance_spreadsheet.py
   ```
   
   This creates three template files:
   - `attendance_template.tsv`
   - `behavior_template.tsv`
   - `detention_template.tsv`

2. **Edit Template Files**
   - Open `attendance_template.tsv` in any text editor (Notepad, VS Code, etc.)
   - Copy the format and add your student data
   - **Important**: Use TAB key to separate columns (not spaces)

3. **Example Attendance Template**
   ```
   Student Name    Status (P/A/L/E)    Time (HH:MM)    Notes
   John Smith      P                   09:00           
   Jane Doe        P                   09:05           Late arrival
   Mike Johnson    A                                   Absence excuse submitted
   Sarah Williams  L                   10:30           
   Emily Brown     P                   09:02           
   ```

4. **Process the Data**
   ```bash
   python3 attendance_spreadsheet.py attendance_template.tsv
   ```

5. **Choose Export Format**
   - CSV (for Excel/Spreadsheets)
   - JSON (for web/APIs)
   - View formatted table

---

## Method 3: Manual Text Template

### What It Is
A pre-formatted text template you can fill in manually.

### How to Use

1. **Open Template**
   ```bash
   cat attendance_input_template.txt
   ```

2. **Edit the Template**
   - Print it out or copy it
   - Fill in each section with proper spacing
   - Use underscores as placeholders

3. **Example Usage**
   ```
   STUDENT NAME          | STATUS        | TIME      | NOTES
   John Smith            | P             | 09:00     | 
   Jane Doe              | P             | 09:05     | Late arrival
   Mike Johnson          | A             | --:--     | Excuse submitted
   ```

---

## Data Format Reference

### Status Codes
| Code | Meaning |
|------|---------|
| P    | Present |
| A    | Absent  |
| L    | Late    |
| E    | Excused |

### Incident Types
- Disruption
- Disrespect
- Aggression
- Bullying
- Dishonesty
- Property Damage
- Other

### Severity Levels
| Level | Points | Meaning |
|-------|--------|---------|
| 1     | 5      | Minor   |
| 2     | 10     | Moderate|
| 3     | 15     | Serious |
| 4     | 20     | Critical|

### Duration Options
- 30min
- 1hr
- 2hrs
- custom (specify exact duration)

---

## Tips for Data Entry

### 1. Organize by Section
- ✓ Complete class information first
- ✓ Enter all attendance records
- ✓ Then add behavioral incidents
- ✓ Finally add detention assignments

### 2. Use Consistent Formatting
- ✓ Use YYYY-MM-DD for dates (2024-12-01)
- ✓ Use HH:MM for times (09:30)
- ✓ Keep student names capitalized consistently

### 3. Maximize Data Quality
- ✓ Add notes for unusual entries
- ✓ Record exact arrival/departure times
- ✓ Document incident details thoroughly
- ✓ Link detention to behavior incidents

### 4. Batch Entry
- ✓ Enter all morning attendance at once
- ✓ Enter all afternoon attendance at once
- ✓ Review and correct before saving
- ✓ Export daily for backup

---

## Keyboard Shortcuts

### In Interactive Tool
- **ENTER**: Move to next field
- **TAB**: Auto-complete (if available)
- **Ctrl+C**: Cancel and exit
- **Ctrl+D**: Skip optional sections

### In Text Editors
- **TAB**: Separate columns (in TSV files)
- **Space**: Within columns (not between columns)
- **Enter**: New row

---

## Common Issues & Solutions

### Issue: "Wrong number of columns"
**Solution**: Make sure you're using TAB, not spaces, to separate columns

### Issue: "Date format error"
**Solution**: Use YYYY-MM-DD format (e.g., 2024-12-01)

### Issue: "Time not recognized"
**Solution**: Use HH:MM format (e.g., 09:30, not 9:30 or 0930)

### Issue: "File not found"
**Solution**: Make sure file is in the same directory. Use full path if different:
```bash
python3 attendance_spreadsheet.py /path/to/file.tsv
```

---

## Export Formats

### CSV (Comma-Separated Values)
- ✓ Works with Excel, Google Sheets
- ✓ Easy to share
- ✓ Good for analysis

### JSON (JavaScript Object Notation)
- ✓ Works with web applications
- ✓ Preserves data structure
- ✓ Good for APIs

### Print/PDF
- ✓ Takes the formatted table output
- ✓ Print directly from terminal
- ✓ Good for records and archives

---

## Best Practices

1. **Daily Entry**
   - Enter attendance at the start of each period
   - Record incidents immediately when they occur
   - Assign detentions same day

2. **Accuracy**
   - Double-check student names
   - Verify times are correct
   - Include detailed notes for disputes

3. **Backup**
   - Export to CSV daily
   - Keep copies in multiple locations
   - Archive end-of-month reports

4. **Privacy**
   - Don't share raw data files
   - Use secure file storage
   - Follow GDPR/privacy regulations

---

## Quick Start Examples

### Quick Attendance Entry
```bash
python3 attendance_entry_tool.py
# Fill in prompts
# Export to CSV when done
```

### Batch Spreadsheet Entry
```bash
# Edit attendance_template.tsv with your data
python3 attendance_spreadsheet.py attendance_template.tsv
# Select export format
```

### View Template
```bash
cat attendance_input_template.txt
# Copy and manually fill in
```

---

## Support

For issues or questions:
1. Check the format requirements above
2. Review example data in templates
3. Ensure file is saved in correct location
4. Verify data is properly separated by TAB (not spaces)

---

**Version**: 1.0  
**Last Updated**: 2024-12-01  
**Status**: Active
