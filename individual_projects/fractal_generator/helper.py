#BH 2nd fractal_generator helper.py
#imports
import math
from turtle import *
#function for drawing a triangle in turtle graphics
#set turtle mechanics
def draw_triangle(bottom_left_coord, side_length):
    penup()
    goto(bottom_left_coord[0], bottom_left_coord[1])
    pendown()
    forward(side_length)
    left(120)
    forward(side_length)
    left(120)
    forward(side_length)
    left(120)

def draw_recursive_triangles(bottom_left_coord, side_length, remaining_depth):
    draw_triangle(bottom_left_coord, side_length)
    if remaining_depth == 0:
        return
    new_remaining_depth = remaining_depth - 1
    triangle_height = math.sqrt(side_length**2 - (side_length/2)**2)
    draw_recursive_triangles(bottom_left_coord, side_length/2, new_remaining_depth)
    draw_recursive_triangles((bottom_left_coord[0] + side_length/4, bottom_left_coord[1] + triangle_height/2), side_length/2, new_remaining_depth)
    draw_recursive_triangles((bottom_left_coord[0] + side_length/2, bottom_left_coord[1]), side_length/2, new_remaining_depth)
def render():
    screensize(200,200)
    bottom_left_coord = (-100, -100)
    side_length = 200
    draw_recursive_triangles(bottom_left_coord, side_length, 5)
    done()