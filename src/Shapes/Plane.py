from src.GroupIntersections import GroupIntersections, Intersection
from src.Ray import Ray
from src.Shapes.Shape import Shape
from src.VectorAndMatrix import Vec3, vector
from src.utils import EPSILON


class Plane(Shape):

    def __str__(self):
        return Plane.__name__

    def local_intersect(self, shape_ray: Ray) -> GroupIntersections:
        if abs(shape_ray.direction.y) < EPSILON:
            return GroupIntersections()

        t = -shape_ray.origin.y / shape_ray.direction.y
        return GroupIntersections(Intersection(t, self))

    def local_normal_at(self, shape_point) -> Vec3:
        return vector(0, 1, 0)
