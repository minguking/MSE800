student1 = {
    "name": "Alex",
    "age": 42,
    "course": "Data Analytics",
    "city": "Auckland",
    "status": "Lecturer"
}

student2 = {
    "name": "Sophia",
    "age": 29,
    "course": "Software Engineering",
    "city": "Wellington",
    "status": "Student"
}

student3 = {
    "name": "Michael",
    "age": 35,
    "course": "Cyber Security",
    "city": "Christchurch",
    "status": "Researcher"
}

all_students = [student1, student2, student3]

filtered = [s for s in all_students if "ex" in s["name"].lower()]

merged = {}
for student in filtered:
    merged = {**merged, **student}

print("Dictionaries with 'ex' in name:")
for s in filtered:
    print(f"  {s}")

print("\nMerged result:")
print(merged)
