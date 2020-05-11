from src.Color import Color
from src.Pattern import Pattern
from src.VectorAndMatrix import Vec3


class TestPattern(Pattern):

    def pattern_at(self, point: Vec3) -> Color:
        return Color(point.x, point.y, point.z)

