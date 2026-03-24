#BH 2nd shape classes

# imports
import math

# define classes
class Circle:
    @staticmethod
    def explain_formulas():
        return "Area: a = πr^2\nPerimeter: p = 2πr"
    def __init__(self, r):
        self.r = r
    def __str__(self):
        return f"| Shape: Circle\n| Radius: {round(self.r, 2)}"
    def calculate_area(self):
        a = math.pi * self.r ** 2
        return a
    def calculate_perimeter(self):
        p = 2 * math.pi * self.r
        return p
    
class Triangle:
    @staticmethod
    def explain_formulas():
        return "Area: a = 0.5bh\nPerimeter: p = b + side2 + side3"
    def __init__(self, b, side2, side3, h):
        self.b = b
        self.side2 = side2
        self.side3 = side3
        self.h = h
    def __str__(self):
        return f"| Shape: Triangle\n| Base: {round(self.b, 2)}\n| Side 2: {round(self.side2, 2)}\n| Side 3: {round(self.side3, 2)}\n| Height: {round(self.h, 2)}"
    def calculate_area(self):
        a = 0.5 * self.b * self.h
        return a
    def calculate_perimeter(self):
        p = self.b + self.side2 + self.side3
        return p

class Rectangle:
    @staticmethod
    def explain_formulas():
        return "Area: a = lw\nPerimeter: p = 2(l + w)"
    def __init__(self, l, w):
        self.l = l
        self.w = w
    def __str__(self):
        return f"| Shape: Rectangle\n| Length: {round(self.l, 2)}\n| Width: {round(self.w, 2)}"
    def calculate_area(self):
        a = self.l * self.w
        return a
    def calculate_perimeter(self):
        p = 2 * (self.l + self.w)
        return p

class Square(Rectangle):
    @staticmethod
    def explain_formulas():
        return "Area: a = s^2\nPerimeter: p = 4s"
    def __init__(self, s):
        super().__init__(s, s)
    def __str__(self):
        return f"| Shape: Square\n| Side: {round(self.l, 2)}"
