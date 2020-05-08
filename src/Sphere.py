import math
from src.Shape import Shape
from src.Vector import Vec3, point
from src.Intersection import Intersect, Intersections
from src.Ray import Ray


class Sphere(Shape):

    SPHERE_ID = 0

    def __init__(self):
        super(Sphere, self).__init__()
        self._id = self.SPHERE_ID
        self.SPHERE_ID += 1
        self.radius = 1

    def __eq__(self, other):
        assert isinstance(other, Sphere), 'The other operand must be a Sphere.'
        return self.radius == other.radius and \
               self.transform == other.transform and \
               self.material == other.material

    @property
    def id(self):
        return self._id

    def local_intersect(self, local_ray: Ray) -> Intersections:
        # the vector from the sphere's center, to the ray origin
        # remember: the sphere is centered at the world origin
        sphere_to_ray = local_ray.origin - point(0, 0, 0)

        a = Vec3.dot(local_ray.direction, local_ray.direction)
        b = 2 * Vec3.dot(local_ray.direction, sphere_to_ray)
        c = Vec3.dot(sphere_to_ray, sphere_to_ray) - 1

        discriminant = (b ** 2) - (4 * a * c)
        if discriminant < 0:
            return Intersections()
        else:
            t1 = Intersect((-b - math.sqrt(discriminant)) / (2 * a), self)
            if discriminant == 0:
                return Intersections(t1, t1)
            t2 = Intersect((-b + math.sqrt(discriminant)) / (2 * a), self)
            return Intersections(t1, t2) if t1 < t2 else Intersections(t2, t1)

    def local_normal_at(self, local_point) -> Vec3:
        # Calculate the object normal
        return (local_point - point(0, 0, 0)).normalize()


def sphere():
    return Sphere()
