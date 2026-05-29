# numbers = [1, 2, 3, 4, 5]
# squares = {str(n): n**2 for n in numbers}
# print(squares)

# keys = ['a', 'b', 'c']
# values = [1, 2, 3]
# d = {key: value for key, value in zip(keys, values)}
# print(d)

# dict1 = {'a': 1, 'b': 2, 'c': 3}
# dict2 = {'d': 4, 'e': 5, 'f': 6}

# merged_dict = {**{k: v for k, v in dict1.items() if k in 'aeiou'},
#                **{k: v for k, v in dict2.items() if k in 'aeiou'}}
# print(merged_dict)

# Develop an script to be able to merge following dictionaries with condition of name with "azw":
 
# Dictionary 1
student1 = {
    "name": "Alex",
    "age": 42,
    "course": "Data Analytics",
    "city": "Auckland",
    "status": "Lecturer"
}
 
# Dictionary 2
student2 = {
    "name": "Sophia",
    "age": 29,
    "course": "Software Engineering",
    "city": "Wellington",
    "status": "Student"
}
 
# Dictionary 3
student3 = {
    "name": "Michael",
    "age": 35,
    "course": "Cyber Security",
    "city": "Christchurch",
    "status": "Researcher"
}

merged_students = []

for student in [student1, student2, student3]:
    if any(c in student["name"].lower()[0] for c in 'azw'):
        merged_students.append(student)
print(merged_students)