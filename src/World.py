import math
from src.PointLight import PointLight
from src.VectorAndMatrix import point, Vec3
from src.Color import Color
from src.Shapes.Sphere import Sphere
from src.VectorAndMatrix import Matrix
from src.Ray import Ray
from src.Precomputed import Precomputed
from src.GroupIntersections import GroupIntersections


class World(object):

    def __init__(self):
        self.objects = []
        self.light = None

    def intersect_world(self, ray: Ray) -> GroupIntersections:
        """Iterates through the list of objects in the world. Each object will check if the given
        ray will intersect.

        :param ray: A point with direction moving across the world.
        :return: An Intersection container object with a list of Intersect that the ray encountered.
        """
        object_intersections = []
        for obj in self.objects:
            intersections = obj.intersect(ray)
            object_intersections.extend(intersections.intersects)
        all_intersections = GroupIntersections(*object_intersections)
        return all_intersections

    # To make this work with multiple light sources,
    # You would needs to iterates a list of light sources
    # and repeatedly call the lighting function for each source
    # and sum the all the color results.
    def shade_hit(self, comps: Precomputed, remaining: int=5) -> Color:
        in_shadow = self.is_shadowed(comps.over_point)
        surface = comps.object.material.lighting(
                        comps.object,
                        self.light,
                        comps.point, comps.eyev, comps.normalv, in_shadow)

        # If the surface is reflected,
        # then it will return a portion of it's color
        reflected = self.reflected_color(comps, remaining)

        # TODO: WTF is wrong here
        refracted = self.refracted_color(comps, remaining)

        return surface + reflected + refracted

    def is_shadowed(self, point: Vec3) -> bool:
        point_to_light = (self.light.position - point)
        distance = point_to_light.magnitude()
        direction = point_to_light.normalize()

        ray = Ray(point, direction)
        intersections = self.intersect_world(ray)

        h = intersections.hit()
        return h is not None and h.t < distance

    def reflected_color(self, comps: Precomputed, remaining: int=5) -> Color:
        if remaining <= 0:
            return Color(0, 0, 0)
        if comps.object.material.reflective == 0.0:
            return Color(0, 0, 0)

        reflect_ray = Ray(comps.over_point, comps.reflectv)
        color = self.color_at(reflect_ray, remaining - 1)

        return color * comps.object.material.reflective

    def refracted_color(self, comps: Precomputed, remaining: int=5) -> Color:
        if remaining <= 0:
            return Color(0, 0, 0)

        if comps.object.material.transparency == 0:
            return Color(0, 0, 0)

        # Find the ratio of the first index of refraction to the second.
        # (Yup, this is inverted from the definition of Snell's Law.)
        n_ratio = comps.n1 / comps.n2

        # cos(theta_i) is the same as the dot product of the two vectors
        cos_i = Vec3.dot(comps.eyev, comps.normalv)

        # Find sin(theta_t)^2 via trigonometric identity
        sin2_t = n_ratio ** 2 * (1 - cos_i ** 2)

        if sin2_t > 1:
            return Color(0, 0, 0)

        # Find cos(theta_t) via trigonometric identity
        cos_t = math.sqrt(1.0 - sin2_t)

        # Compute the direction of the refracted ray
        direction = comps.normalv * (n_ratio * cos_i - cos_t) - comps.eyev * n_ratio

        # Create the refracted ray
        refract_ray = Ray(comps.under_point, direction)

        # Find the color of the refracted ray, making sure to multiply
        # by the transparency value to account for any opacity
        result = self.color_at(refract_ray, remaining - 1) *\
               comps.object.material.transparency
        return result

    def color_at(self, ray: Ray, remaining: int=5) -> Color:
        intersections = self.intersect_world(ray)
        intersect = intersections.hit()
        if intersect is None:
            return Color(0, 0, 0)
        precomputed = intersect.prepare_computations(ray)
        return self.shade_hit(precomputed, remaining)


def default_world():
    world = World()
    world.light = PointLight(point(-10, 10, -10), Color(1, 1, 1))

    s1 = Sphere()
    s1.material.color = Color(0.8, 1.0, 0.6)
    s1.material.diffuse = 0.7
    s1.material.specular = 0.2
    world.objects.append(s1)

    s2 = Sphere()
    s2.transform = Matrix.scaling(0.5, 0.5, 0.5)
    world.objects.append(s2)

    return world
