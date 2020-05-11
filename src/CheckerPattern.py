import math
from src.Pattern import Pattern
from src.VectorAndMatrix import Vec3
from src.Color import Color


class CheckerPattern(Pattern):

    def __init__(self, a, b):
        super(CheckerPattern, self).__init__()
        self.a = a
        self.b = b

    def pattern_at(self, point: Vec3) -> Color:
        result = math.floor(point.x) + math.floor(point.y) + math.floor(point.z)
        return self.a if result % 2 == 0 else self.b
