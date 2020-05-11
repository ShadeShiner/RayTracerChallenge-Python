import math
from src.Color import Color
from src.Patterns.Pattern import Pattern
from src.VectorAndMatrix import Vec3


class GradientPattern(Pattern):

    def __init__(self, a: Color, b: Color):
        super(GradientPattern, self).__init__()
        self.a = a
        self.b = b

    def pattern_at(self, point: Vec3) -> Color:
        distance = self.b - self.a
        fraction = point.x - math.floor(point.x)
        return self.a + distance * fraction
