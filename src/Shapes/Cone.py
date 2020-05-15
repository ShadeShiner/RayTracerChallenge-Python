import math
from src.Shapes.Shape import Shape
from src.Ray import Ray
from src.GroupIntersections import GroupIntersections, Intersection
from src.VectorAndMatrix import Vec3 as Point, Vec3 as Vector, vector
from src.utils import EPSILON, check_cap


class Cone(Shape):

    def __init__(self):
        super(Shape, self).__init__()
        self.minimum = float('-inf')
        self.maximum = float('inf')
        self.closed = False

    def local_intersect(self, shape_ray: Ray) -> GroupIntersections:
        a = shape_ray.direction.x ** 2 - shape_ray.direction.y ** 2 + shape_ray.direction.z ** 2

        b = 2 * shape_ray.origin.x * shape_ray.direction.x - \
            2 * shape_ray.origin.y * shape_ray.direction.y + \
            2 * shape_ray.origin.z * shape_ray.direction.z

        xs = GroupIntersections()
        # if a == 0 and b == 0:
        if abs(a) < EPSILON and abs(b) < EPSILON:
            self.intersect_caps(shape_ray, xs)
            return xs

        c = (shape_ray.origin.x ** 2) - (shape_ray.origin.y ** 2) + (shape_ray.origin.z ** 2)

        if abs(a) < EPSILON:
            t = -c / (2 * b)
            xs.add_intersection(Intersection(t, self))
            self.intersect_caps(shape_ray, xs)
            return xs
        discriminant = b ** 2 - 4 * a * c

        # ray does not intersect the cylinder
        if discriminant < 0:
            return GroupIntersections()

        t0 = (-b - math.sqrt(discriminant)) / (2 * a)
        t1 = (-b + math.sqrt(discriminant)) / (2 * a)

        if t0 > t1:
            t0, t1 = t1, t0

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
        if check_cap(shape_ray, t, self.minimum):
            xs.add_intersection(Intersection(t, self))

        # check for an intersection with the upper end by intersecting
        # the ray with the plane at y=cyl.maximum
        t = (self.maximum - shape_ray.origin.y) / shape_ray.direction.y
        if check_cap(shape_ray, t, self.maximum):
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

        # The side of the cone
        y = math.sqrt(shape_point.x ** 2 + shape_point.z ** 2)
        if shape_point.y > 0:
            y = -y
        return vector(shape_point.x, y, shape_point.z)
