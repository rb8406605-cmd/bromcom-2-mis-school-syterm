#!/usr/bin/env python3
"""
BROMCOM Attendance & Behavior Entry Tool
Allows easy input of attendance and behavior records with proper spacing and formatting
"""

import os
import sys
from datetime import datetime
from typing import List, Dict

class AttendanceEntry:
    """Handle attendance and behavior data entry"""
    
    def __init__(self):
        self.attendance_records = []
        self.behavior_records = []
        self.detention_records = []
        self.class_info = {}
    
    def print_section_header(self, title: str, width: int = 80):
        """Print a formatted section header"""
        print("\n" + "="*width)
        print(f"  {title.center(width-4)}")
        print("="*width)
    
    def print_table_header(self, columns: List[str], widths: List[int]):
        """Print table header with proper spacing"""
        header = " | ".join(col.ljust(width) for col, width in zip(columns, widths))
        print(header)
        separator = "-" * len(header)
        print(separator)
    
    def get_class_information(self):
        """Collect class information"""
        self.print_section_header("CLASS INFORMATION")
        
        self.class_info['date'] = input("Date (YYYY-MM-DD) [Today]: ").strip() or str(datetime.today().date())
        self.class_info['class'] = input("Class/Grade: ").strip()
        self.class_info['teacher'] = input("Teacher Name: ").strip()
        self.class_info['subject'] = input("Subject/Period: ").strip()
        
        print("\n✓ Class information saved")
    
    def get_attendance_records(self):
        """Collect attendance records with proper spacing"""
        self.print_section_header("STUDENT ATTENDANCE RECORDS")
        print("\nEnter student information. Press ENTER after each field:")
        print("Status: P=Present, A=Absent, L=Late, E=Excused")
        print("Time format: HH:MM (e.g., 09:30)")
        print("Type 'done' when finished.\n")
        
        columns = ["STUDENT NAME", "STATUS", "TIME", "NOTES"]
        widths = [20, 10, 10, 30]
        self.print_table_header(columns, widths)
        
        record_count = 0
        while True:
            student_name = input(f"\n[{record_count + 1}] Student Name (or 'done'): ").strip()
            if student_name.lower() == 'done':
                break
            
            status = input("  Status (P/A/L/E): ").strip().upper()
            time = input("  Time (HH:MM) [--:--]: ").strip() or "--:--"
            notes = input("  Notes: ").strip()
            
            record = {
                'name': student_name,
                'status': status,
                'time': time,
                'notes': notes
            }
            self.attendance_records.append(record)
            
            # Print formatted record
            formatted_record = f"{student_name.ljust(20)} | {status.ljust(10)} | {time.ljust(10)} | {notes.ljust(30)}"
            print(f"  {formatted_record}")
            record_count += 1
        
        print(f"\n✓ {record_count} attendance records saved")
    
    def get_behavior_records(self):
        """Collect behavioral incident records"""
        self.print_section_header("BEHAVIORAL INCIDENTS (Optional)")
        print("\nEnter behavioral incidents. Type 'done' when finished.\n")
        
        print("Incident Types: Disruption, Disrespect, Aggression, Bullying, Dishonesty, Property Damage")
        print("Severity: Minor(1), Moderate(2), Serious(3), Critical(4)\n")
        
        columns = ["STUDENT NAME", "INCIDENT TYPE", "SEVERITY", "POINTS"]
        widths = [20, 20, 12, 8]
        self.print_table_header(columns, widths)
        
        record_count = 0
        while True:
            student_name = input(f"\n[{record_count + 1}] Student Name (or 'done'): ").strip()
            if student_name.lower() == 'done':
                break
            
            incident_type = input("  Incident Type: ").strip()
            severity = input("  Severity (1-4): ").strip()
            points = input("  Points: ").strip() or str(int(severity) * 5)
            
            record = {
                'name': student_name,
                'incident': incident_type,
                'severity': severity,
                'points': points
            }
            self.behavior_records.append(record)
            
            # Print formatted record
            formatted_record = f"{student_name.ljust(20)} | {incident_type.ljust(20)} | {severity.ljust(12)} | {points.ljust(8)}"
            print(f"  {formatted_record}")
            record_count += 1
        
        if record_count > 0:
            print(f"\n✓ {record_count} behavior records saved")
        else:
            print("\n✓ No behavior incidents recorded")
    
    def get_detention_records(self):
        """Collect detention assignments"""
        self.print_section_header("DETENTION ASSIGNMENTS (Optional)")
        print("\nEnter detention assignments. Type 'done' when finished.\n")
        
        print("Duration options: 30min, 1hr, 2hrs, custom")
        print("Date & Time format: YYYY-MM-DD HH:MM\n")
        
        columns = ["STUDENT NAME", "REASON", "DURATION", "DATE & TIME"]
        widths = [20, 20, 12, 20]
        self.print_table_header(columns, widths)
        
        record_count = 0
        while True:
            student_name = input(f"\n[{record_count + 1}] Student Name (or 'done'): ").strip()
            if student_name.lower() == 'done':
                break
            
            reason = input("  Reason: ").strip()
            duration = input("  Duration: ").strip()
            datetime_str = input("  Date & Time (YYYY-MM-DD HH:MM): ").strip()
            
            record = {
                'name': student_name,
                'reason': reason,
                'duration': duration,
                'datetime': datetime_str
            }
            self.detention_records.append(record)
            
            # Print formatted record
            formatted_record = f"{student_name.ljust(20)} | {reason.ljust(20)} | {duration.ljust(12)} | {datetime_str.ljust(20)}"
            print(f"  {formatted_record}")
            record_count += 1
        
        if record_count > 0:
            print(f"\n✓ {record_count} detention records saved")
        else:
            print("\n✓ No detention assignments")
    
    def print_summary(self):
        """Print summary of all records"""
        self.print_section_header("SUMMARY")
        
        print(f"\nClass Information:")
        print(f"  Date: {self.class_info.get('date', 'N/A')}")
        print(f"  Class: {self.class_info.get('class', 'N/A')}")
        print(f"  Teacher: {self.class_info.get('teacher', 'N/A')}")
        print(f"  Subject: {self.class_info.get('subject', 'N/A')}")
        
        print(f"\nAttendance Summary:")
        print(f"  Total Students: {len(self.attendance_records)}")
        present = sum(1 for r in self.attendance_records if r['status'] == 'P')
        absent = sum(1 for r in self.attendance_records if r['status'] == 'A')
        late = sum(1 for r in self.attendance_records if r['status'] == 'L')
        excused = sum(1 for r in self.attendance_records if r['status'] == 'E')
        
        print(f"  Present: {present}")
        print(f"  Absent: {absent}")
        print(f"  Late: {late}")
        print(f"  Excused: {excused}")
        
        print(f"\nBehavioral Summary:")
        print(f"  Incidents Recorded: {len(self.behavior_records)}")
        
        print(f"\nDETENTION Summary:")
        print(f"  Detentions Assigned: {len(self.detention_records)}")
        
        print("\n" + "="*80)
    
    def export_to_csv(self, filename: str = None):
        """Export records to CSV file"""
        if filename is None:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f"attendance_report_{timestamp}.csv"
        
        try:
            with open(filename, 'w') as f:
                # Write class info
                f.write("CLASS INFORMATION\n")
                f.write(f"Date,Class,Teacher,Subject\n")
                f.write(f"{self.class_info.get('date', '')},{self.class_info.get('class', '')},{self.class_info.get('teacher', '')},{self.class_info.get('subject', '')}\n\n")
                
                # Write attendance
                f.write("ATTENDANCE RECORDS\n")
                f.write("Student Name,Status,Time,Notes\n")
                for record in self.attendance_records:
                    f.write(f"{record['name']},{record['status']},{record['time']},{record['notes']}\n")
                
                f.write("\n")
                
                # Write behavior
                if self.behavior_records:
                    f.write("BEHAVIORAL INCIDENTS\n")
                    f.write("Student Name,Incident Type,Severity,Points\n")
                    for record in self.behavior_records:
                        f.write(f"{record['name']},{record['incident']},{record['severity']},{record['points']}\n")
                    f.write("\n")
                
                # Write detention
                if self.detention_records:
                    f.write("DETENTION ASSIGNMENTS\n")
                    f.write("Student Name,Reason,Duration,Date & Time\n")
                    for record in self.detention_records:
                        f.write(f"{record['name']},{record['reason']},{record['duration']},{record['datetime']}\n")
            
            print(f"\n✓ Data exported to: {filename}")
            return filename
        except Exception as e:
            print(f"\n✗ Error exporting file: {e}")
            return None
    
    def run(self):
        """Run the interactive entry tool"""
        print("\n" + "="*80)
        print("BROMCOM - ATTENDANCE & BEHAVIOR ENTRY TOOL".center(80))
        print("="*80)
        
        try:
            self.get_class_information()
            self.get_attendance_records()
            self.get_behavior_records()
            self.get_detention_records()
            self.print_summary()
            
            # Ask to export
            export = input("\nExport to CSV? (y/n): ").strip().lower()
            if export == 'y':
                self.export_to_csv()
            
            print("\n✓ Data entry completed successfully!")
            
        except KeyboardInterrupt:
            print("\n\n✗ Entry cancelled by user")
            sys.exit(1)
        except Exception as e:
            print(f"\n✗ Error: {e}")
            sys.exit(1)


if __name__ == "__main__":
    tool = AttendanceEntry()
    tool.run()
