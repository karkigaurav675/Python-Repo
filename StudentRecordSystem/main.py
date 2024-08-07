from file_handling.createstudentrecord import register_student
from file_handling.displaystudentrecord import display_students
from file_handling.searchstudentdata import find_student_by_number

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