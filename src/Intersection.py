import operator
from src.Ray import Ray
from src.Vector import Vec3, reflect
from src.utils import EPSILON


class Intersect(object):

    def __init__(self, t, obj):
        self.t = t
        self.obj = obj

    def __lt__(self, other):
        return self.t < other.t

    def __eq__(self, other):
        return self.t == other.t and self.obj == other.obj

    def __str__(self):
        return f'Intersect(t={self.t}, obj={self.obj})'


class Intersections(object):

    def __init__(self, *args: Intersect):
        self.intersects = [intersect for intersect in args]
        self.intersects.sort(key=operator.attrgetter('t'))


class Precomputed(object):

    def __init__(self):
        self.t = None
        self.object = None
        self.point = None
        self.eyev = None
        self.normalv = None
        self.over_point = None
        self.reflectv = None


def hit(intersections: Intersections) -> Intersect:
    # If intersects are sorted, can instead return
    # the first non-negative t value intersect
    closest_hit = None
    for intersect in intersections.intersects:
        if intersect.t < 0:
            continue
        elif closest_hit is None:
            closest_hit = intersect
        elif intersect.t < closest_hit.t:
            closest_hit = intersect
    return closest_hit


def prepare_computations(intersection: Intersect, ray: Ray) -> Precomputed:
    # instantiate a data structure for storing some precomputed values
    comps = Precomputed()

    # copy the intersection's properties, for convenience
    comps.t = intersection.t
    comps.object = intersection.obj

    # precompute some useful values
    comps.point = ray.position(comps.t)
    comps.eyev = -ray.direction
    comps.normalv = comps.object.normal_at(comps.point)

    if Vec3.dot(comps.normalv, comps.eyev) < 0:
        comps.inside = True
        comps.normalv = -comps.normalv
    else:
        comps.inside = False

    # after negating the normal, if necessary
    comps.reflectv = reflect(ray.direction, comps.normalv)

    comps.over_point = comps.point + comps.normalv * EPSILON
    return comps
