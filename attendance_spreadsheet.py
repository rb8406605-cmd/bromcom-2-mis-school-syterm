#!/usr/bin/env python3
"""
BROMCOM Spreadsheet-Style Entry Tool
Tab-separated input for quick data entry with proper formatting
"""

import csv
import sys
from datetime import datetime
from typing import List, Dict
import json


class SpreadsheetEntry:
    """Handle spreadsheet-style data entry"""
    
    def __init__(self):
        self.data = []
    
    def create_attendance_template(self):
        """Create a spreadsheet template file"""
        template_content = """Student Name	Status (P/A/L/E)	Time (HH:MM)	Notes
John Smith	P	09:00	
Jane Doe	P	09:05	Late arrival
Mike Johnson	A		Absence excuse submitted
Sarah Williams	L	10:30	
Emily Brown	P	09:02	
David Davis	P	09:01	
Rachel Wilson	E		Excused absence

# Instructions:
# - Use TAB to separate columns
# - Status: P=Present, A=Absent, L=Late, E=Excused
# - Copy this format and add your data
# - Save as .tsv (Tab Separated Values) file
# - Use: python3 attendance_spreadsheet.py your_file.tsv
"""
        
        with open('attendance_template.tsv', 'w') as f:
            f.write(template_content)
        print("✓ Created attendance_template.tsv")
    
    def create_behavior_template(self):
        """Create behavior incident template"""
        template_content = """Student Name	Incident Type	Severity	Points	Notes
John Smith	Disruption	2	10	Talked out of turn
Jane Doe	Disrespect	3	15	Argued with teacher
Mike Johnson	Bullying	4	20	Name calling
Sarah Williams	Dishonesty	2	10	Copied homework
Emily Brown	Property Damage	3	15	Broke desk

# Severity: 1=Minor, 2=Moderate, 3=Serious, 4=Critical
# Points auto-calculated as: severity * 5 (unless specified)
# Incident Types: Disruption, Disrespect, Aggression, Bullying, Dishonesty, Property Damage, Other
"""
        
        with open('behavior_template.tsv', 'w') as f:
            f.write(template_content)
        print("✓ Created behavior_template.tsv")
    
    def create_detention_template(self):
        """Create detention template"""
        template_content = """Student Name	Reason	Duration	Date	Time	Room/Location
John Smith	Repeated disruption	1hr	2024-12-01	15:30	Room 201
Jane Doe	Incomplete homework	30min	2024-12-02	14:00	Library
Mike Johnson	Behavioral incident	2hrs	2024-12-03	15:30	Room 201
Sarah Williams	Tardiness	30min	2024-12-04	14:30	Room 101

# Duration: 30min, 1hr, 2hrs, custom
# Date format: YYYY-MM-DD
# Time format: HH:MM
"""
        
        with open('detention_template.tsv', 'w') as f:
            f.write(template_content)
        print("✓ Created detention_template.tsv")
    
    @staticmethod
    def print_formatted_table(data: List[Dict], title: str = "", max_width: int = 100):
        """Print data in formatted table"""
        if not data:
            print(f"{title}: No data")
            return
        
        print(f"\n{title}")
        print("-" * max_width)
        
        # Get column widths
        columns = list(data[0].keys())
        widths = {}
        for col in columns:
            widths[col] = max(len(col), max(len(str(row.get(col, ''))) for row in data))
        
        # Print header
        header = " | ".join(col.ljust(widths[col]) for col in columns)
        print(header)
        print("-" * len(header))
        
        # Print rows
        for row in data:
            row_str = " | ".join(str(row.get(col, '')).ljust(widths[col]) for col in columns)
            print(row_str)
        
        print("-" * len(header))
    
    @staticmethod
    def read_tsv_file(filepath: str) -> List[Dict]:
        """Read tab-separated values file"""
        try:
            data = []
            with open(filepath, 'r', encoding='utf-8') as f:
                reader = csv.DictReader(f, delimiter='\t')
                for row in reader:
                    if any(row.values()):  # Skip empty rows
                        # Filter out comment lines
                        if not any(str(v).startswith('#') for v in row.values() if v):
                            data.append(row)
            return data
        except FileNotFoundError:
            print(f"✗ File not found: {filepath}")
            return []
        except Exception as e:
            print(f"✗ Error reading file: {e}")
            return []
    
    @staticmethod
    def export_to_json(data: List[Dict], output_file: str = None):
        """Export data to JSON format"""
        if output_file is None:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            output_file = f"data_{timestamp}.json"
        
        try:
            with open(output_file, 'w') as f:
                json.dump(data, f, indent=2)
            print(f"✓ Data exported to: {output_file}")
            return output_file
        except Exception as e:
            print(f"✗ Error exporting: {e}")
            return None
    
    @staticmethod
    def export_to_csv(data: List[Dict], output_file: str = None):
        """Export data to CSV format"""
        if not data:
            print("✗ No data to export")
            return None
        
        if output_file is None:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            output_file = f"data_{timestamp}.csv"
        
        try:
            with open(output_file, 'w', newline='') as f:
                fieldnames = list(data[0].keys())
                writer = csv.DictWriter(f, fieldnames=fieldnames)
                writer.writeheader()
                writer.writerows(data)
            print(f"✓ Data exported to: {output_file}")
            return output_file
        except Exception as e:
            print(f"✗ Error exporting: {e}")
            return None


def main():
    """Main function to run spreadsheet entry tool"""
    if len(sys.argv) > 1:
        filepath = sys.argv[1]
        print(f"\nReading data from: {filepath}\n")
        
        data = SpreadsheetEntry.read_tsv_file(filepath)
        
        if data:
            SpreadsheetEntry.print_formatted_table(data, title=f"Loaded {len(data)} records")
            
            # Ask for export format
            print("\nExport options:")
            print("1. Export to CSV")
            print("2. Export to JSON")
            print("3. Skip export")
            
            choice = input("\nSelect option (1-3): ").strip()
            
            if choice == '1':
                SpreadsheetEntry.export_to_csv(data)
            elif choice == '2':
                SpreadsheetEntry.export_to_json(data)
            elif choice == '3':
                print("✓ Skipped export")
    else:
        # Create templates
        print("\nBROMCOM - Spreadsheet Entry Tool\n")
        print("Creating templates...\n")
        
        SpreadsheetEntry.create_attendance_template()
        SpreadsheetEntry.create_behavior_template()
        SpreadsheetEntry.create_detention_template()
        
        print("\nUsage:")
        print("  1. Edit the created .tsv files with your data")
        print("  2. Run: python3 attendance_spreadsheet.py attendance_template.tsv")
        print("  3. Or: python3 attendance_spreadsheet.py behavior_template.tsv")
        print("  4. Or: python3 attendance_spreadsheet.py detention_template.tsv")
        print("\nNote: Use TAB key to separate columns, not spaces!")


if __name__ == "__main__":
    main()
