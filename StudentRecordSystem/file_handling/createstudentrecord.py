from file_handling.manage_data import load_data, save_data

def get_student_data():
    student = {
        "id": int(input("Enter student ID: ")),
        "Name": input("Enter student Name: "),
        "Address": input("Enter student Address: "),
        "Age": int(input("Enter student Age: ")),
        "Number": int(input("Enter student Mobile Number: ")),
        "EducationalQualification": []
    }
    while True:
        qualification_name = input("Enter educational qualification name (0 to skip): ")
        if qualification_name == '0':
            break
        passing_year = int(input("Enter year of passing: "))
        percentage = int(input("Enter percentage: "))
        student["EducationalQualification"].append({
            "qualificationName": qualification_name,
            "passingyear": passing_year,
            "percentage": percentage
        })  
    return student

def register_student():
    students = load_data()
    students.append(get_student_data())
    save_data(students)