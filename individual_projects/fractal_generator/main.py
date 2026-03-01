#BH 2nd fractal_generator main.py

#imports
from drawing import *
from saving import *

#define menu function
def menu():
    #introduce the user
    print("Welcome to the Sierpinski Triangle Generator! This program creates a Sierpinski Triangle fractal using recursion.")
    #get valid user input for depth, color, speed, and saving
    while True:
        depth = input("\nEnter recursion depth (1-10): ")
        if not depth.isdigit() or int(depth) not in range(1, 11):
            print("Invalid input. Please enter a number between 1 and 10.")
        else:
            depth = int(depth)
            break
    while True:
        pen_color = input("Enter triangle color, can be one of: red, blue, green, yellow, purple, orange, pink, brown, black: ")
        if pen_color not in ["red", "blue", "green", "yellow", "purple", "orange", "pink", "brown", "black"]:
            print("Invalid input. Please enter a valid color.")
        else:
            break
    while True:
        bg_color = input("Enter background color, can be one of: red, blue, green, yellow, purple, orange, pink, brown, black, white: ")
        if bg_color not in ["red", "blue", "green", "yellow", "purple", "orange", "pink", "brown", "black", "white"]:
            print("Invalid input. Please enter a valid background color.")
        else:
            break
    is_instant = input("Would you like to watch the triangle being drawn? (y/n): ")
    should_save = input("Would you like to save the image? (y/n): ")
    #tell user what they entered
    print(f"Generating Sierpinski Triangle with depth {depth}, color {pen_color}, and background color {bg_color}")
    #draw the triangle
    render(is_instant, depth, pen_color, bg_color)
    #save the triangle if user wants
    if should_save == 'y':
        save_file()
    done()
menu()