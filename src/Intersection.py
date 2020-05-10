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

    def __getitem__(self, index):
        return self.intersects[index]

    def __len__(self):
        return len(self.intersects)


class Precomputed(object):

    def __init__(self):
        self.t = None
        self.object = None
        self.point = None
        self.eyev = None
        self.normalv = None
        # This refers to the point a little bit above the surface of the object where it intersects
        # This is used for shadows, to make sure it does not self shadow
        self.over_point = None
        # This refers to the point a little bit below the surface of the object where it intersects
        # This is used to calculate where refracted rays will be originated
        self.under_point = None
        self.reflectv = None
        self.n1 = 1.0
        self.n2 = 1.0

    def __str__(self):
        result = []
        for key in self.__dict__:
            result.append(f'{key}={self.__dict__[key]}')
        return '\n'.join(result)


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


def prepare_computations(intersection: Intersect, ray: Ray, xs: Intersections=None) -> Precomputed:
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
    comps.under_point = comps.point - comps.normalv * EPSILON

    # Refractive Indices
    if xs is None:
        xs = Intersections()

    containers = []
    for intersect in xs:
        if intersect == intersection:
            if containers:
                comps.n1 = containers[-1].material.refractive_index

        # If intersect object is contained, it is exiting the intersection
        if intersect.obj in containers:
            containers.remove(intersect.obj)
        # If intersect object is not contained, it is entering the intersection
        else:
            containers.append(intersect.obj)

        if intersect == intersection:
            if containers:
                comps.n2 = containers[-1].material.refractive_index
            break

    return comps
