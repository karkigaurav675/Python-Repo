from file_handling.manage_data import load_data
from file_handling.manage_data import save_data

def get_student_data():
    student = {
        "id": int(input("Enter student ID: ")),
        "Name": input("Enter student Name: "),
        "Address": input("Enter student Address: "),
        "Age": int(input("Enter student Age: ")),
        "Number": int(input("Enter student Mobile Number: ")),
        "EducationalQualification": [
            {
                "qualificationName": input("Enter First educational qualification name: "),
                "passingyear": int(input("Enter year of passing: ")),
                "percentage": int(input("Enter percentage: "))
            },
            {
                "qualificationName": input("Enter Second educational qualification name: "),
                "passingyear": int(input("Enter year of passing: ")),
                "percentage": int(input("Enter percentage: "))
            }
        ]
    }
    return student

def register_student():
    students = load_data()
    students.append(get_student_data())
    save_data(students)