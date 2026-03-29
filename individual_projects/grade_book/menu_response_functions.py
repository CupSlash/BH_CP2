#BH 2nd Menu Response Functions
#imports
from classes import *
from input_validators import *
#GradeBook instance
grade_book = GradeBook()
#define menu response functions below
def add_new_student():
    name = input("Enter student name: ")
    student_id = input("Enter student ID: ")
    grade_level = input("Enter grade level: ")
    new_student = Student(name, student_id, grade_level)
    existing_student = grade_book.search_students_by_id(student_id)
    if existing_student != None:
        print(f"A student with ID {student_id} already exists. Please try again.")
        return
    grade_book.add_student(new_student)    
def add_grade_to_student():
    student_id = input("Enter student ID: ")
    student = grade_book.search_students_by_id(student_id)
    grade = input("Enter grade (0-100): ")
    grade = validate_grade(grade)
    if student:
        student.add_grade(grade)
    else:
        print(f"No student by ID {student_id} found.")
def view_student_record():
    choice = input("Search by 1. ID or 2. name? ")
    if choice == "1":
        student_id = input("Enter student ID: ")
        student = grade_book.search_students_by_id(student_id)
        if student != None:
            students = [student]
        else:
            students = []
    elif choice == "2":
        name = input("Enter student name: ")
        students = grade_book.search_students_by_name(name)
    else:
        print("That is not a valid option. Please try again.")
        return
    if len(students) > 0:
        for student in students:
            print(student)
            print("Grades: ")
            if len(student.grades) == 0:
                print("No grades.")
            else:
                for grade in student.grades:
                    print(grade)
    else:
        print("No students found.")
def view_all_students():
    if len(grade_book.students) == 0:
        print("No students in the class yet.")
    else:
        for student in grade_book.students:
            print(student)
def view_class_summary():
    pass
def view_class_statistics():
    statistics = grade_book.calculate_grades()
    if statistics is None:
        print("No grades available.")
        return
    print(f"Total Students: {statistics['total_students']}")
    print(f"Class Average: {statistics['average']}")
    print(f"Highest Grade: {statistics['highest']}")
    print(f"Lowest Grade: {statistics['lowest']}")

    