"""
This class is used to represent the color for a pixel in a "Canvas". This is done
using the class attributes: red, green, blue. The range is between 0 and 255
inclusive.

The itself can use mathematical operations to interact with other Color
instances such as:
    - Addition
    - Subtraction
    - Multiplication
    - Division
    - Equality Checking

The mathematical operations is done attribute wise. I.E. A red is add with a red,
blue added with a blue, and green added with a green.
"""

import numbers
from src.utils import EPSILON


class Color:

    def __init__(self, red, green, blue):
        self.red = red
        self.green = green
        self.blue = blue

    def __add__(self, other):
        assert isinstance(other, Color), 'The other operand must be an object of type Color.'
        return Color(self.red + other.red, self.green + other.green, self.blue + other.blue)

    def __sub__(self, other):
        assert isinstance(other, Color), 'The other operand must be an object of type Color.'
        return Color(self.red - other.red, self.green - other.green, self.blue - other.blue)

    def __mul__(self, other):
        if isinstance(other, numbers.Real):
            return Color(self.red * other, self.green * other, self.blue * other)
        elif isinstance(other, Color):
            return Color(self.red * other.red, self.green * other. green, self.blue * other.blue)
        else:
            raise Exception('The other operand must be an int, float, or Color.')

    def __eq__(self, other):
        assert isinstance(other, Color), 'The other operand must be an object of type Color.'
        return abs(self.red - other.red) < EPSILON and\
                abs(self.green - other.green) < EPSILON and\
                abs(self.blue - other.blue) < EPSILON

    def __str__(self):
        return f'Color({self.red}, {self.green}, {self.blue})'
