import math

from src.Shapes.Shape import Shape
from src.VectorAndMatrix import Vec3, point
from src.GroupIntersections import GroupIntersections, Intersection
from src.BoundingBox import BoundingBox
from src.Ray import Ray


class Sphere(Shape):

    def __init__(self):
        super(Sphere, self).__init__()

    def __eq__(self, other):
        assert isinstance(other, Sphere), 'The other operand must be a Sphere.'
        return self.transform == other.transform and \
               self.material == other.material

    def local_intersect(self, shape_ray: Ray) -> GroupIntersections:
        # the vector from the sphere's center, to the ray origin
        # remember: the sphere is centered at the world origin
        sphere_to_ray = shape_ray.origin - point(0, 0, 0)

        a = Vec3.dot(shape_ray.direction, shape_ray.direction)
        b = 2 * Vec3.dot(shape_ray.direction, sphere_to_ray)
        c = Vec3.dot(sphere_to_ray, sphere_to_ray) - 1

        discriminant = (b ** 2) - (4 * a * c)
        if discriminant < 0:
            return GroupIntersections()
        else:
            t1 = Intersection((-b - math.sqrt(discriminant)) / (2 * a), self)
            if discriminant == 0:
                return GroupIntersections(t1, t1)
            t2 = Intersection((-b + math.sqrt(discriminant)) / (2 * a), self)
            return GroupIntersections(t1, t2) if t1 < t2 else GroupIntersections(t2, t1)

    def local_normal_at(self, shape_point: Vec3) -> Vec3:
        # Calculate the object normal
        return (shape_point - point(0, 0, 0)).normalize()

    def bounds_of(self) -> BoundingBox:
        return BoundingBox(point(-1, -1, -1), point(1, 1, 1))


def glass_sphere():
    sphere = Sphere()
    sphere.material.transparency = 1.0
    sphere.material.refractive_index = 1.5
    return sphere
