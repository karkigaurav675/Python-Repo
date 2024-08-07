import os
import json

path = "C:/Users/asus/Documents/python(for class)/Python-Repo/StudentRecordSystem/student_records.json"

def load_data():
    if os.path.isfile(path):
        with open(path, "r") as file:
            return json.load(file)
    return []

def save_data(data):
    with open(path, "w") as file:
        json.dump(data, file, indent=4)
    print("Data saved successfully!")