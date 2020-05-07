import math
from src.Vector import Vec3, point
from src.Matrix import Matrix
from src.Intersection import Intersect, Intersections
from src.Material import Material
from src.Ray import Ray


class Sphere(object):
    SPHERE_ID = 0

    def __init__(self):
        self._id = self.SPHERE_ID
        self.SPHERE_ID += 1
        self.radius = 1
        # Converts itself from object -> world space
        self.transform = Matrix.identity_matrix()
        self.material = Material()

    def __eq__(self, other):
        assert isinstance(other, Sphere), 'The other operand must be a Sphere.'
        return self.radius == other.radius and \
               self.transform == other.transform and \
               self.material == other.material

    @property
    def id(self):
        return self._id

    def intersect(self, ray: Ray) -> Intersections:
        # Converting the ray from world space to object space
        object_ray = ray.transform(self.transform.inverse())

        # the vector from the sphere's center, to the ray origin
        # remember: the sphere is centered at the world origin
        sphere_to_ray = object_ray.origin - point(0, 0, 0)

        a = Vec3.dot(object_ray.direction, object_ray.direction)
        b = 2 * Vec3.dot(object_ray.direction, sphere_to_ray)
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

    def normal_at(self, world_point: Vec3) -> Vec3:
        # Convert world space to object space
        object_point = self.transform.inverse() * world_point
        # Calculate the object normal
        object_normal = (object_point - point(0, 0, 0)).normalize()
        # Convert object space to world space
        world_normal = self.transform.inverse().transpose() * object_normal
        world_normal.w = 0
        return world_normal.normalize()


def sphere():
    return Sphere()


if __name__ == '__main__':
    from src.Vector import vector
    from src.Ray import Ray
    from src.Matrix import Matrix

    s = sphere()
    m = Matrix.scaling(1, 0.5, 1) * Matrix.rotation_z(36)
    s.transform = m
    print(s.normal_at(point(0, 0.7071067811865, -0.7071067811865)))
