ER Diagram Description
This ER diagram represents a one-to-many (1:N) relationship between Student and Course.
Entities:

Student — stores student information (student_id, name, contact, address, emergency_contact)
Course — stores course information (course_id, class_room, professor)

Relationship:

One student can enroll in many courses, but each course belongs to only one student
This is represented as a 1:N relationship
The student_id in the Course table acts as a Foreign Key (FK), referencing the Student table's Primary Key (PK)
