import os
import json

path = "C:/Users/asus/Documents/python(for class)/Python-Repo/Python_Project_DataStoring/student_records.json"

def get_student_data():
    student = {
        "id": int(input("Enter student ID: ")),
        "Name": input("Enter student Name: "),
        "Address": input("Enter student Address: "),
        "Age": int(input("Enter student Age: ")),
        "Number": int(input("Enter student Mobile Number: "))
    }
    return student

def load_data():
    if os.path.isfile(path):
        with open(path, "r") as file:
            return json.load(file)
    return []

def save_data(data):
    with open(path, "w") as file:
        json.dump(data, file, indent=4)
    print("Data saved successfully!")

def register_student():
    students = load_data()
    students.append(get_student_data())
    save_data(students)

def display_students():
    students = load_data()
    if students:
        for student in students:
            print(json.dumps(student, indent=4))
    else:
        print("No student data available.")

def find_student_by_number():
    number = int(input("Enter the mobile number of the student to search: "))
    students = load_data()
    for student in students:
        if student['Number'] == number:
            print("Student found:")
            print(json.dumps(student, indent=4))
            return
    print("No student found with that mobile number.")

def show_menu():
    menu = {
        '1': register_student,
        '2': display_students,
        '3': find_student_by_number,
        '0': exit
    }

    while True:
        print("1. Register Student")
        print("2. View Students")
        print("3. Search Student by Mobile Number")
        print("0. Exit")
        
        choice = input("Choose an option: ")
        action = menu.get(choice)
        if action:
            action()
        else:
            print("Invalid option, please try again.")
show_menu()