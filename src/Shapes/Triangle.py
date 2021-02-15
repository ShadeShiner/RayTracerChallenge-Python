from src.Shapes.Shape import Shape
from src.VectorAndMatrix import Vec3
from src.Ray import Ray
from src.GroupIntersections import GroupIntersections, Intersection
from src.utils import EPSILON


class Triangle(Shape):

    def __init__(self, p1: Vec3, p2: Vec3, p3: Vec3):
        super(Triangle, self).__init__()
        self.p1 = p1
        self.p2 = p2
        self.p3 = p3

        self.e1 = self.p2 - self.p1
        self.e2 = self.p3 - self.p1

        self.normal = Vec3.cross(self.e2, self.e1).normalize()

    def local_normal_at(self, shape_point: Vec3) -> Vec3:
        return self.normal

    def local_intersect(self, shape_ray: Ray) -> GroupIntersections:
        result = GroupIntersections()

        dir_cross_e2 = Vec3.cross(shape_ray.direction, self.e2)
        det = Vec3.dot(self.e1, dir_cross_e2)
        if abs(det) < EPSILON:
            return result

        f = 1.0 / det

        p1_to_origin = shape_ray.origin - self.p1
        u = f * Vec3.dot(p1_to_origin, dir_cross_e2)
        if u < 0 or u > 1:
            return result


        origin_cross_e1 = Vec3.cross(p1_to_origin, self.e1)
        v = f * Vec3.dot(shape_ray.direction, origin_cross_e1)
        if v < 0 or (u + v) > 1:
            return result

        t = f * Vec3.dot(self.e2, origin_cross_e1)
        return GroupIntersections(Intersection(t, self))
