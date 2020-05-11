import operator

from src.Precomputed import Precomputed
from src.Ray import Ray
from src.VectorAndMatrix import Vec3, reflect
from src.utils import EPSILON


class Intersection(object):

    def __init__(self, t, obj):
        self.t = t
        self.obj = obj

    def __lt__(self, other):
        return self.t < other.t

    def __eq__(self, other):
        return self.t == other.t and self.obj == other.obj

    def __str__(self):
        return f'Intersect(t={self.t}, obj={self.obj})'

    def prepare_computations(self, ray: Ray, xs = None) -> Precomputed:
        # instantiate a data structure for storing some precomputed values
        comps = Precomputed()

        # copy the intersection's properties, for convenience
        comps.t = self.t
        comps.object = self.obj

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
            xs = GroupIntersections()

        containers = []
        for intersect in xs:
            if intersect == self:
                if containers:
                    comps.n1 = containers[-1].material.refractive_index

            if intersect.obj in containers:
                containers.remove(intersect.obj)
            else:
                containers.append(intersect.obj)

            if intersect == self:
                if containers:
                    comps.n2 = containers[-1].material.refractive_index
                break

        return comps


class GroupIntersections(object):

    def __init__(self, *args: Intersection):
        self.intersects = [intersect for intersect in args]
        self.intersects.sort(key=operator.attrgetter('t'))

    def __getitem__(self, index):
        return self.intersects[index]

    def __len__(self):
        return len(self.intersects)

    def hit(self) -> Intersection:
        # If intersects are sorted, can instead return
        # the first non-negative t value intersect
        closest_hit = None
        for intersect in self.intersects:
            if intersect.t < 0:
                continue
            elif closest_hit is None:
                closest_hit = intersect
            elif intersect.t < closest_hit.t:
                closest_hit = intersect
        return closest_hit
