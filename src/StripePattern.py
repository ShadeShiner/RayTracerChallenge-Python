import math
from src.Pattern import Pattern
from src.Color import Color
from src.VectorAndMatrix import Vec3
from src.Shape import Shape


class StripePattern(Pattern):

    def __init__(self, a: Color, b: Color):
        super(StripePattern, self).__init__()
        self.a = a
        self.b = b

    def pattern_at(self, point: Vec3) -> Color:
        return self.a if math.floor(point.x) % 2 == 0 else self.b
