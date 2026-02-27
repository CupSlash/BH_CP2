#BH 2nd fractal_generator main.py
#imports
from helper import *
import turtle
#define menu function
def menu():
    #introduce the user
    print("Welcome to the Sierpinski Triangle Generator! This program creates a Sierpinski Triangle fractal using recursion.")
    #get valid user input for depth and color
    while True:
        depth = int(input("\nEnter recursion depth (1-10): "))
        if depth not in range(1, 11):
            print("Invalid input. Please enter a number between 1 and 10.")
        else:
            break
    while True:
        color = input("Enter triangle color, can be one of: red, blue, green, yellow, purple, orange, pink, brown, black, white: ")
        if color not in ["red", "blue", "green", "yellow", "purple", "orange", "pink", "brown", "black", "white"]:
            print("Invalid input. Please enter a valid color.")
        else:
            break
    #tell user what they entered
    print("Generating Sierpinski Triangle with depth", depth, "and color", color)
    #draw the triangle
    draw_triangle(color, depth, turtle)
menu()