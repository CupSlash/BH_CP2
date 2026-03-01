#BH 2nd fractal_generator saving.py

#imports
from turtle import *

#function for saving the image
def save_file():
    screen = Screen()
    canvas = screen.getcanvas()
    canvas.postscript(file="turtle_output.eps")