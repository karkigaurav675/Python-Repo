import json
from datetime import datetime
path = "C:/Users/asus/Documents/python(for class)/Python-Repo/RecordKeeping/new.json"
with open(path, 'r') as file:
    json_data = file.read()
data = json.loads(json_data)
date = datetime(2024, 8, 16).strftime("%Y-%m-%d")
records = []
for record in data:
    if record["created_time"].startswith(date):
        records.append(record)
count = len(records)
print(f"Number of records for {date}: {count}")
print(json.dumps(records, indent=2))