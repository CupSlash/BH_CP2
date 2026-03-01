#BH 2nd fractal_generator drawing.py

#imports
import math
from turtle import *

#function for drawing a triangle in turtle graphics
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

#function for handling the recursive drawing of the triangles
def draw_recursive_triangles(bottom_left_coord, side_length, remaining_depth):
    draw_triangle(bottom_left_coord, side_length)
    if remaining_depth == 0:
        return
    new_remaining_depth = remaining_depth - 1
    triangle_height = math.sqrt(side_length**2 - (side_length/2)**2)
    draw_recursive_triangles(bottom_left_coord, side_length/2, new_remaining_depth)
    draw_recursive_triangles((bottom_left_coord[0] + side_length/4, bottom_left_coord[1] + triangle_height/2), side_length/2, new_remaining_depth)
    draw_recursive_triangles((bottom_left_coord[0] + side_length/2, bottom_left_coord[1]), side_length/2, new_remaining_depth)

#function for turtle mechanics and rendering the triangle(s)
def render(is_instant, depth, pen_color, bg_color):
    pencolor(pen_color)
    bgcolor(bg_color)
    if is_instant == 'n':
        speed(0)
        tracer(0)
    screen_dimension = 400
    screensize(screen_dimension, screen_dimension)
    bottom_left_coord = (screen_dimension/-2, screen_dimension/-2)
    side_length = screen_dimension
    draw_recursive_triangles(bottom_left_coord, side_length, depth)
    if is_instant == 'n':
        hideturtle()
        update()