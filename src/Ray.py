from src.VectorAndMatrix import Vec3 as Point
from src.VectorAndMatrix import Vec3 as Vector

class Ray(object):

    def __init__(self, origin: Point, direction: Vector):
        self.origin = origin
        self.direction = direction

    def position(self, t):
        return self.origin + self.direction * t

    def transform(self, matrix):
        return Ray(
            matrix * self.origin,
            matrix * self.direction
        )
