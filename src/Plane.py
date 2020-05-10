from src.Intersection import Intersections, Intersect
from src.Ray import Ray
from src.Shape import Shape
from src.Vector import Vec3, vector
from src.utils import EPSILON


class Plane(Shape):

    def __str__(self):
        return Plane.__name__

    def local_intersect(self, local_ray: Ray) -> Intersections:
        if abs(local_ray.direction.y) < EPSILON:
            return Intersections()

        t = -local_ray.origin.y / local_ray.direction.y
        return Intersections(Intersect(t, self))

    def local_normal_at(self, local_point) -> Vec3:
        return vector(0, 1, 0)


def plane():
    return Plane()
