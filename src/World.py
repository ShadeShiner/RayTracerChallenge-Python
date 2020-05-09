from src.PointLight import PointLight
from src.Vector import point, Vec3
from src.Color import Color
from src.Sphere import sphere
from src.Matrix import Matrix
from src.Ray import Ray
from src.Intersection import Intersections, Precomputed, hit, prepare_computations
from src.Material import lighting


class World(object):

    def __init__(self):
        self.objects = []
        self.light = None

    def intersect_world(self, ray: Ray) -> Intersections:
        """Iterates through the list of objects in the world. Each object will check if the given
        ray will intersect.

        :param ray: A point with direction moving across the world
        :return: Intersection object with a list of Intersect that the ray encountered.
        """
        object_intersections = []
        for obj in self.objects:
            intersections = obj.intersect(ray)
            object_intersections.extend(intersections.intersects)
        all_intersections = Intersections(*object_intersections)
        return all_intersections

    # To make this work with multiple light sources,
    # You would needs to iterates a list of light sources
    # and repeatedly call the lighting function for each source
    # and sum the all the color results.
    def shade_hit(self, comps: Precomputed) -> Color:
        in_shadow = self.is_shadowed(comps.over_point)
        return lighting(comps.object.material,
                        comps.object,
                        self.light,
                        comps.point, comps.eyev, comps.normalv, in_shadow)

    def is_shadowed(self, point: Vec3) -> bool:
        point_to_light = (self.light.position - point)
        distance = point_to_light.magnitude()
        direction = point_to_light.normalize()

        ray = Ray(point, direction)
        intersections = self.intersect_world(ray)

        h = hit(intersections)
        return h is not None and h.t < distance

    def color_at(self, ray: Ray) -> Color:
        intersections = self.intersect_world(ray)
        intersect = hit(intersections)
        if intersect is None:
            return Color(0, 0, 0)
        precomputed = prepare_computations(intersect, ray)
        return self.shade_hit(precomputed)


def default_world():
    world = World()
    world.light = PointLight(point(-10, 10, -10), Color(1, 1, 1))

    s1 = sphere()
    s1.material.color = Color(0.8, 1.0, 0.6)
    s1.material.diffuse = 0.7
    s1.material.specular = 0.2
    world.objects.append(s1)

    s2 = sphere()
    s2.transform = Matrix.scaling(0.5, 0.5, 0.5)
    world.objects.append(s2)

    return world


def view_transform(from_point: Vec3, to_point: Vec3, up_vector: Vec3):
    forward_vector = (to_point - from_point).normalize()
    world_up = up_vector.normalize()
    left_vector = Vec3.cross(forward_vector, world_up)
    view_up = Vec3.cross(left_vector, forward_vector)

    orientation = Matrix.identity_matrix()
    orientation._matrix[0][0] = left_vector.x
    orientation._matrix[0][1] = left_vector.y
    orientation._matrix[0][2] = left_vector.z
    orientation._matrix[1][0] = view_up.x
    orientation._matrix[1][1] = view_up.y
    orientation._matrix[1][2] = view_up.z
    orientation._matrix[2][0] = -forward_vector.x
    orientation._matrix[2][1] = -forward_vector.y
    orientation._matrix[2][2] = -forward_vector.z

    return orientation * Matrix.translation(-from_point.x, -from_point.y, -from_point.z)


from src.Vector import  vector
if __name__ == '__main__':
    w = default_world()
    r = Ray(point(0, 0, -5), vector(0, 1, 0))
