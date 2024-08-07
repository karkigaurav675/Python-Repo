import json
from file_handling.manage_data import load_data

def find_student_by_number():
    number = int(input("Enter the mobile number of the student to search: "))
    students = load_data()
    for student in students:
        if student['Number'] == number:
            print("Student found:")
            print(json.dumps(student, indent=4))
            return
    print("No student found with that mobile number.")