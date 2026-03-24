#BH 2nd Geometry Calc
#Imports
from helper import *
from calc import *
from shape_classes import *

library = []

#define menu function
def main():
#while loop so code repeats
    while True:
    #Design a text-based menu for interacting with the calculator
        choice = input("What would you like to do?\n 1. Create a shape\n 2. View all shapes\n 3. Select a shape\n 4. Compare Shapes\n 5. Sort Shapes\n 6. Formula guide\n 7. Quit\n")
        #Creating a shape!!!
        if choice == "1":
            new_shape_type = input("What shape would you like to create?\n 1. Circle\n 2. Triangle\n 3. Rectangle\n 4. Square\n")
            if new_shape_type == "1":
                r = input("What is the radius of the circle?\n")
                r = float_check(r)
                new_circle = Circle(r)
                library.append(new_circle)
                print("Circle created!")
                print(new_circle)
            elif new_shape_type == "2":
                b = input("What is the length of the base?\n")
                b = float_check(b)
                side2 = input("What is the length of the triangle's left side?\n")
                side2 = float_check(side2)
                side3 = input("What is the length of the triangle's right side?\n")
                side3 = float_check(side3)
                h = input("What is the triangle's height?\n")
                h = float_check(h)
                new_triangle = Triangle(b, side2, side3, h)
                library.append(new_triangle)
                print("Triangle created!")
                print(new_triangle)
            elif new_shape_type == "3":
                l = input("What is the length of the rectangle?\n")
                l = float_check(l)
                w = input("What is the rectangle's width?\n")
                w = float_check(w)
                new_rectangle = Rectangle(l, w)
                library.append(new_rectangle)
                print("Rectangle created!")
                print(new_rectangle)
            elif new_shape_type == "4":
                s = input("What is the length of the square's side?\n")
                s = float_check(s)
                new_square = Square(s)
                library.append(new_square)
                print("Square created!")
                print(new_square)
        #View all shapes
        elif choice == "2":
            for shape in library:
                print(f"{shape}\n")
        #Select a shape
        elif choice == "3":
            list_text = ""
            for i, shape in enumerate(library, start=1):
                list_text += f"{i}.\n{shape}\n"
            selection = input(f"Select a shape from the list below.\n{list_text}")
            if (selection.isdigit() and 1 <= int(selection) <= len(library)):
                selected_shape = library[int(selection) - 1]
                print(f"You selected:\n{selected_shape}")
                selected_action = input("What would you like to do with this shape?\n 1. Calculate area\n 2. Calculate perimeter\n")
                if selected_action == "1":
                    print(f"The area of the shape is: {round(selected_shape.calculate_area(), 2)}")
                elif selected_action == "2":
                    print(f"The perimeter of the shape is: {round(selected_shape.calculate_perimeter(), 2)}")
                else:
                    print("That is not an option.")
        #Formula guide
        elif choice == "6":
            formula = input("Would you like to see the formulas for a circle (c), triangle (t), rectangle (r), or a square (s)?
                if formula == "c":
                elif formula == "t":
                elif formula == "r":
                elif formula == "s":
                else:
                    print("That is not an option, please try again.")
        #Quit app
        elif choice == "7":
            print("Please come again soon.")
            break
        #incorrect input
        else:
            print("That is not an option.")
main()
