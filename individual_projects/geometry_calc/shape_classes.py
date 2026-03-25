#BH 2nd shape_classes.py
# imports
from abc import ABC, abstractmethod
import math
#Install a shape class that other shapes can use as a base.
class Shape(ABC):
    def has_larger_area(self, other_shape):
        return self.calculate_area() > other_shape.calculate_area()
    def has_longer_perimeter(self, other_shape):
        return self.calculate_perimeter() > other_shape.calculate_perimeter()
    @abstractmethod
    def calculate_area(self):
        pass
    @abstractmethod
    def calculate_perimeter(self):
        pass
#The following classes represent the different shapes that the user can create.
class Circle(Shape):
    @staticmethod
    def explain_formulas():
        return "area = π * radius^2\nperimeter = 2π * radius"
    def __init__(self, radius):
        self.radius = radius
    def __str__(self):
        return f"| Shape: Circle\n| Radius: {round(self.radius, 2)}"
    def calculate_area(self):
        area = math.pi * self.radius ** 2
        return area
    def calculate_perimeter(self):
        perimeter = 2 * math.pi * self.radius
        return perimeter
class Triangle(Shape):
    @staticmethod
    def explain_formulas():
        return "area = 0.5 * base * height\nperimeter = base + side2 + side3"
    def __init__(self, base, side2, side3, height):
        self.base = base
        self.side2 = side2
        self.side3 = side3
        self.height = height
    def __str__(self):
        return f"| Shape: Triangle\n| Base: {round(self.base, 2)}\n| Side 2: {round(self.side2, 2)}\n| Side 3: {round(self.side3, 2)}\n| Height: {round(self.height, 2)}"
    def calculate_area(self):
        area = 0.5 * self.base * self.height
        return area
    def calculate_perimeter(self):
        perimeter = self.base + self.side2 + self.side3
        return perimeter
class Rectangle(Shape):
    @staticmethod
    def explain_formulas():
        return "area = length * width\nperimeter = 2 * (length + width)"
    def __init__(self, length, width):
        self.length = length
        self.width = width
    def __str__(self):
        return f"| Shape: Rectangle\n| Length: {round(self.length, 2)}\n| Width: {round(self.width, 2)}"
    def calculate_area(self):
        area = self.length * self.width
        return area
    def calculate_perimeter(self):
        perimeter = 2 * (self.length + self.width)
        return perimeter
class Square(Rectangle):
    @staticmethod
    def explain_formulas():
        return "area = side^2\nperimeter = 4 * side"
    def __init__(self, side):
        super().__init__(side, side)
    def __str__(self):
        return f"| Shape: Square\n| Side: {round(self.length, 2)}"