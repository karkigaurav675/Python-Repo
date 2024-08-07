import json
from file_handling.manage_data import load_data

def display_students():
    students = load_data()
    if students:
        for student in students:
            print(json.dumps(student, indent=4))
    else:
        print("No student data available.")