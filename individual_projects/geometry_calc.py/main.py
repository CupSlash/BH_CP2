#BH 2nd Geometry Calc
#define menu function
def main():
#while loop so code repeats
    while True:
    #   Design a text-based menu for interacting with the calculator
        choice = input("What would you like to do?\n 1. Create a shape\n 2. Select a shape\n 3. View a shape\n 4. Compare Shapes\n 5. Sort Shapes\n 6. Formula guide\n 7. Quit\n")
        #Creating a shape!!!
        if choice == "1":
            new_shape_type = input("What shape would you like to create?\n 1. Circle\n 2. Triangle\n 3. Rectangle\n 4. Square")
            if new_shape_type == "1":
                r = input("What is the radius of the circle?")
            elif new_shape_type == "2":
                b = input("What is the length of the base ")
                side2 = input("What is the length of the triangle's left side?")
                side3 = input("What is the length of the triangle's right side?")
                h = input("What is the triangle's height?")
            elif new_shape_type == "3":
                l = input("What is the length of the rectangle?")
                w = input("What is the rectangle's width?")
            elif new_shape_type == "4":
                l = input("What is the length of the square's side?")
        #Shape selection 
        if choice == "2":
            selection = input("Select a shape from the following list.")
            else:
                print("That is not an option.")
            #incorrect input
        #Shape view
        if choice == "3":
        #Comparing shapes
        if choice == "4":
        #Shape sorting
        if choice == "5":
        #Formula grids
        if choice == "6":
        #Quit
        if choice == "7":
            break
        #incorrect input
main()
