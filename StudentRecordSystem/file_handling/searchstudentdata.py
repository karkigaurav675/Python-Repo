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

def find_by_qualification():
    qualification_name = input("Enter qualification name for search (press 0 to skip): ")
    passing_year = int(input("Enter year of passing for search (press 0 to skip): "))
    percentage = int(input("Enter percentage for search (press 0 to skip): "))
    students = load_data()
    for student in students:
        this = student.get('EducationalQualification')
        for search in this:
            qualification_matches = (
                qualification_name == 0 or 
                qualification_name in search.get('qualificationName', '')
            )
            passing_year_matches = (
                passing_year == 0 or 
                search.get('passingyear') == passing_year
            )
            percentage_matches = (
                percentage == 0 or 
                search.get('percentage') >= percentage
            )
            if qualification_matches and passing_year_matches and percentage_matches:
                print("Student found:")
                print(json.dumps(student, indent=4))
                found = True
                break
    if not found:
        print("No student found.")

def top_3_student_percentage_sum():
    students = load_data()
    if not students:
        print("No data available.")
        return
    for student in students:
        qualifications = student.get("EducationalQualification")
        total_percentage = 0
        for this in qualifications:
            total_percentage += this.get("percentage")
        student["TotalPercentage"] = total_percentage
    sorted_students = sorted(students, key=lambda student: student["TotalPercentage"], reverse=True)
    top_students = sorted_students[:3]
    if top_students:
        print("Top 3 Students based on percentage: ")
        for student in top_students:
            print(f"Student ID: {student['id']}, Total Percentage: {student['TotalPercentage']}%")
            print(json.dumps(student, indent=4))