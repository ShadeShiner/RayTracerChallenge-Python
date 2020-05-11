from src.GroupIntersections import GroupIntersections, Intersection
from src.Ray import Ray
from src.Shapes.Shape import Shape
from src.VectorAndMatrix import Vec3, vector
from src.utils import EPSILON


class Plane(Shape):

    def __str__(self):
        return Plane.__name__

    def local_intersect(self, local_ray: Ray) -> GroupIntersections:
        if abs(local_ray.direction.y) < EPSILON:
            return GroupIntersections()

        t = -local_ray.origin.y / local_ray.direction.y
        return GroupIntersections(Intersection(t, self))

    def local_normal_at(self, local_point) -> Vec3:
        return vector(0, 1, 0)
