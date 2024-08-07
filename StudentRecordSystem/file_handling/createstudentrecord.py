from file_handling.manage_data import load_data
from file_handling.manage_data import save_data

def get_student_data():
    student = {
        "id": int(input("Enter student ID: ")),
        "Name": input("Enter student Name: "),
        "Address": input("Enter student Address: "),
        "Age": int(input("Enter student Age: ")),
        "Number": int(input("Enter student Mobile Number: "))
    }
    return student

def register_student():
    students = load_data()
    students.append(get_student_data())
    save_data(students)