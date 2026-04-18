
from dataclasses import dataclass
from typing import List

@dataclass
class Student:
    
    def __init__(self, name, age, student_id):
        self.name = name
        self.age = age
        self.student_id = student_id

def collect_students(count: int = 3) -> List[Student]:
    students: List[Student] = []
    for i in range(3):
        print(f"Student #{i+1}")
        name = input("  Name: ").strip()
        while not name:
            name = input("  Name (cannot be empty): ").strip()
        while True:
            try:
                age = int(input("  Age: ").strip())
                break
            except ValueError:
                print("  Enter a valid integer for age.")
        student_id = input("  Student ID: ").strip() or "N/A"
        students.append(Student(name, age, student_id))
    return students

def print_students_sorted_by_age(students: List[Student]) -> None:
    for s in sorted(students, key=lambda x: x.age):
        print(f"{s.name} - Age: {s.age}")

if __name__ == "__main__":
    students = collect_students(3)  # collects 3 students (minimum)
    print_students_sorted_by_age(students)