#BH 2nd Menu Response Functions
from classes import *
from input_validators import *

grade_book = GradeBook()

#define menu response functions below
def add_new_student():
    name = input("Enter student name: ")
    student_id = input("Enter student ID: ")
    new_student = Student(name, student_id)
    grade_book.add_student(new_student)    
def add_grade_to_student():
    student_id = input("Enter student ID: ")
    student_id = validate_student_id()
    grade = input("Enter grade (0-100): ")
    grade = check_float_value()
def view_student_record():
    student_id = input("Enter student ID: ")
    student_id = validate_student_id()
    if validate_student_id() == True:
        for student in grade_book.students:
            print(student_id.student)
def view_all_students():
    for student in grade_book.students:
        print(student)
def view_class_summary():
    pass
