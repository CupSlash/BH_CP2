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
    grade = input("Enter grade (0-100): ")
    grade = validate_score_input(grade)

def view_student_record():
    pass
def view_all_students():
    pass
def view_class_summary():
    pass