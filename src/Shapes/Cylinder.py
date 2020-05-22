import math

from src.Shapes.Shape import Shape
from src.GroupIntersections import GroupIntersections, Intersection
from src.Ray import Ray
from src.VectorAndMatrix import Vec3 as Point, Vec3 as Vector, vector, point
from src.BoundingBox import BoundingBox
from src.utils import EPSILON, check_cap


class Cylinder(Shape):

    def __init__(self):
        super(Cylinder, self).__init__()
        self.minimum = float('-inf')
        self.maximum = float('inf')
        self.closed = False

    def local_intersect(self, shape_ray: Ray) -> GroupIntersections:
        a = shape_ray.direction.x ** 2 + shape_ray.direction.z ** 2

        # ray is parallel to the y axis
        if a < EPSILON:
            xs = GroupIntersections()
            self.intersect_caps(shape_ray, xs)
            return xs

        b = 2 * shape_ray.origin.x * shape_ray.direction.x +\
            2 * shape_ray.origin.z * shape_ray.direction.z
        c = shape_ray.origin.x ** 2 + shape_ray.origin.z ** 2 - 1
        discriminant = b ** 2 - 4 * a * c

        # ray does not intersect the cylinder
        if discriminant < 0:
            return GroupIntersections()

        t0 = (-b - math.sqrt(discriminant)) / (2 * a)
        t1 = (-b + math.sqrt(discriminant)) / (2 * a)

        if t0 > t1:
            t0, t1 = t1, t0

        xs = GroupIntersections()

        y0 = shape_ray.origin.y + t0 * shape_ray.direction.y
        if self.minimum < y0 < self.maximum:
            xs.add_intersection(Intersection(t0, self))

        y1 = shape_ray.origin.y + t1 * shape_ray.direction.y
        if self.minimum < y1 < self.maximum:
            xs.add_intersection(Intersection(t1, self))

        self.intersect_caps(shape_ray, xs)

        return xs

    def intersect_caps(self, shape_ray: Ray, xs: GroupIntersections):
        # caps only matter if the cylinder is closed, and might possibly be
        # intersected by the ray.
        if not self.closed or abs(shape_ray.direction.y) < EPSILON:
            return

        # check for an intersection with the lower end cap by intersecting
        # the ray with the plane at y=cyl.minimum
        t = (self.minimum - shape_ray.origin.y) / shape_ray.direction.y
        if check_cap(shape_ray, t):
            xs.add_intersection(Intersection(t, self))

        # check for an intersection with the upper end by intersecting
        # the ray with the plane at y=cyl.maximum
        t = (self.maximum - shape_ray.origin.y) / shape_ray.direction.y
        if check_cap(shape_ray, t):
            xs.add_intersection(Intersection(t, self))

    def local_normal_at(self, shape_point: Point) -> Vector:
        # compute the square of teh distance from the y axis
        distance = shape_point.x ** 2 + shape_point.z ** 2

        # Calculating the normal at the top cap
        if distance < 1 and shape_point.y >= self.maximum - EPSILON:
            return vector(0, 1, 0)

        # Calculating the normal at the bottom cap
        elif distance < 1 and shape_point.y <= self.minimum + EPSILON:
            return vector(0, -1, 0)

        # The normal is at the side of the cylinders
        else:
            return vector(shape_point.x, 0, shape_point.z)

    def bounds_of(self) -> BoundingBox:
        return BoundingBox(point(-1, self.minimum, -1),
                           point(1, self.maximum, 1))
