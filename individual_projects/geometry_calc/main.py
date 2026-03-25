#BH 2nd Geometry Calc
#Imports
from menu_options import *
#start with an empty library
library = []
#define menu function
def main():
    #while loop so code repeats
    while True:
        #Design a text-based menu for interacting with the calculator
        choice = input("What would you like to do?\n 1. Create a shape\n 2. View all shapes\n 3. Select a shape\n 4. Compare Shapes\n 5. Sort Shapes\n 6. Show formula guide\n 7. Quit\n")
        #Creating a shape!!!
        if choice == "1":
            handle_create_shape_option(library)
        #View all shapes
        elif choice == "2":
            handle_view_shapes_option(library)
        #Select a shape
        elif choice == "3":
            handle_select_shape_option(library)
        #Compare shapes
        elif choice == "4":
            handle_compare_shapes_option(library)
        #Sort shapes
        elif choice == "5":
            handle_sort_shapes_option(library)
        #Formula guide
        elif choice == "6":
            handle_show_formula_guide_option()
        #Quit app
        elif choice == "7":
            print("Please come again soon.")
            break
        #incorrect input
        else:
            print("That is not an option.")
main()
