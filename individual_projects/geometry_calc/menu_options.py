#BH 2nd menu_options.py
# Imports
from input_validators import *
from shape_classes import *
#check to see if there are any shapes in the library. If there aren't, print a message and return False. If there are, return True.
def check_library_length(library):
    if (len(library) == 0):
        print("There are no shapes in the library yet.")
        return False
    return True
#The following functions handle the different menu options. 
def handle_create_shape_option(library):
    new_shape_type = input("What shape would you like to create?\n 1. Circle\n 2. Triangle\n 3. Rectangle\n 4. Square\n")
    if new_shape_type == "1":
        r = input("What is the radius of the circle?\n")
        r = positive_float_check(r)
        new_circle = Circle(r)
        library.append(new_circle)
        print("Circle created!")
        print(new_circle)
    elif new_shape_type == "2":
        b = input("What is the length of the base?\n")
        b = positive_float_check(b)
        side2 = input("What is the length of the triangle's left side?\n")
        side2 = positive_float_check(side2)
        side3 = input("What is the length of the triangle's right side?\n")
        side3 = positive_float_check(side3)
        h = input("What is the triangle's height?\n")
        h = positive_float_check(h)
        new_triangle = Triangle(b, side2, side3, h)
        library.append(new_triangle)
        print("Triangle created!")
        print(new_triangle)
    elif new_shape_type == "3":
        l = input("What is the length of the rectangle?\n")
        l = positive_float_check(l)
        w = input("What is the rectangle's width?\n")
        w = positive_float_check(w)
        new_rectangle = Rectangle(l, w)
        library.append(new_rectangle)
        print("Rectangle created!")
        print(new_rectangle)
    elif new_shape_type == "4":
        s = input("What is the length of the square's side?\n")
        s = positive_float_check(s)
        new_square = Square(s)
        library.append(new_square)
        print("Square created!")
        print(new_square)
def handle_view_shapes_option(library):
    if not check_library_length(library):
        return
    for shape in library:
        print(shape)
def handle_select_shape_option(library):
    if not check_library_length(library):
        return
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
def handle_compare_shapes_option(library):
    if not check_library_length(library):
        return
    list_text = ""
    for i, shape in enumerate(library, start=1):
        list_text += f"{i}.\n{shape}\n"
    first_selection = input(f"Select your first shape from the list below.\n{list_text}")
    second_selection = input(f"Select your second shape from the list below.\n{list_text}")
    if (first_selection.isdigit() and 1 <= int(first_selection) <= len(library)) and (second_selection.isdigit() and 1 <= int(second_selection) <= len(library)):
        shape1 = library[int(first_selection) - 1]
        shape2 = library[int(second_selection) - 1]
        shape1_has_larger_area = shape1.has_larger_area(shape2)
        shape1_has_longer_perimeter = shape1.has_longer_perimeter(shape2)
        area_comparison_word = "larger" if shape1_has_larger_area else "smaller"
        perimeter_comparison_word = "longer" if shape1_has_longer_perimeter else "shorter"
        print(f"Shape 1 has a {area_comparison_word} area than Shape 2.")
        print(f"Shape 1 has a {perimeter_comparison_word} perimeter than Shape 2.")
def handle_sort_shapes_option(library):
    if not check_library_length(library):
        return
    sort_choice = input("How would you like to sort the shapes?\n 1. By area\n 2. By perimeter\n")
    if sort_choice == "1":
        sorted_library = sorted(library, key=lambda shape: shape.calculate_area())
        print("Shapes sorted by area:")
        for shape in sorted_library:
            print(f"{shape}\n")
    elif sort_choice == "2":
        sorted_library = sorted(library, key=lambda shape: shape.calculate_perimeter())
        print("Shapes sorted by perimeter:")
        for shape in sorted_library:
            print(f"{shape}\n")
    else:
        print("That is not an option.")
def handle_show_formula_guide_option():
    formula = input("Would you like to see the formulas for a circle (c), triangle (t), rectangle (r), or a square (s)?")
    ShapeClass = None
    if formula == "c":
        ShapeClass = Circle
    elif formula == "t":
        ShapeClass = Triangle
    elif formula == "r":
        ShapeClass = Rectangle
    elif formula == "s":
        ShapeClass = Square
    else:
        print("That is not an option, please try again.")
    if ShapeClass:
        print(ShapeClass.explain_formulas())