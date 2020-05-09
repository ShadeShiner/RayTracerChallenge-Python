import math
from src.Color import Color
from src.Pattern import Pattern
from src.Vector import Vec3


class RingPattern(Pattern):

    def __init__(self, a, b):
        super(RingPattern, self).__init__()
        self.a = a
        self.b = b

    def pattern_at(self, point: Vec3) -> Color:
        result = math.floor(math.sqrt(point.x ** 2 + point.z ** 2))
        return self.a if result % 2 == 0 else self.b
