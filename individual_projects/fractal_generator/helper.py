#BH 2nd fractal_generator helper.py
#function for drawing a triangle in turtle graphics
def draw_triangle(color, depth, turtle):
    turtle.speed(0)
    turtle.tracer(0)
    turtle.hideturtle()
    turtle.screensize(500, 500)
    turtle.color(color)
    turtle.hideturtle()
    turtle.penup()
    turtle.goto(-500, -500)
    turtle.pendown()
    turtle.goto(500, -500)
    turtle.goto(0, 500)
    turtle.goto(-500, -500)
    turtle.penup()