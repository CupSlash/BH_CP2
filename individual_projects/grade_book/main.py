#BH 2nd Simple Grade Book 
#imports
from classes import *
from menu_response_functions import *
#menu
def main():
    print("Welcome to the Class Grade Book!")
    while True:
        menu_response = input(" 1. Add New Student\n 2. Add Grade to Student\n 3. View Student Record\n 4. View All Students\n 5. Class Summary \n 6. Exit\n")
        if menu_response == "1":
            add_new_student()
        elif menu_response == "2":
            add_grade_to_student()
        elif menu_response == "3":
            view_student_record()
        elif menu_response == "4":
            view_all_students()
        elif menu_response == "5":
            class_summary()
        elif menu_response == "6":
            print("See you again soon!")
            break
        else:
            print("That is not an option. Please try again.")
main()