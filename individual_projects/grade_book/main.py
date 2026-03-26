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
            #Create a function to add a new student to the class.
            add_new_student()
        elif menu_response == "2":
            #Create a function to add a grade to a student in the class.
            add_grade_to_student()
        elif menu_response == "3":
            #Create a function to view a student's record.
            view_student_record()
        elif menu_response == "4":
            #Create a function to view all students in the class.
            view_all_students()
        elif menu_response == "5":
            #Create a function to view the class summary.
            class_summary()
        elif menu_response == "6":
            #Add a menu response for quitting the app.
            print("See you again soon!")
            break
        else:
            #Add input validation for the menu response. If the user enters something that isn't a valid option, tell them.
            print("That is not an option. Please try again.")
main()