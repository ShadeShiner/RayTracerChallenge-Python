import bisect
import operator
from typing import Optional

from src.Precomputed import Precomputed
from src.Ray import Ray
from src.VectorAndMatrix import Vec3, reflect
from src.utils import EPSILON

"""
Intersection is a simple data structure representing a collision
that occurs with a Ray object and a Shape. The 't' value is a float
indicating how long in "time" units a ray will take to intersect with
the shape. The shape in which the collision occurred is stored in "obj".
"""
class Intersection(object):

    def __init__(self, t: float, obj):
        self.t = t
        self.obj = obj

    def __lt__(self, other):
        return self.t < other.t

    def __eq__(self, other):
        return self.t == other.t and self.obj.id == other.obj.id

    def __str__(self):
        return f'Intersect(t={self.t}, obj={self.obj})'

    def prepare_computations(self, ray: Ray, xs = None) -> Precomputed:
        """ Generate a data structure with useful mathematical properties related
        to lighting, reflection, and refraction.

        :param ray: A ray object that collided with an object in this intersect.
        :param xs: (Optional) A GroupIntersection objects used to determine the
        "refractiveness" of when the intersect "entered" and "exited" the object

        :return: The PreComputed data structure with calculated information.
        """
        # instantiate a data structure for storing some precomputed values
        comps = Precomputed()

        # copy the intersection's properties, for convenience
        comps.t = self.t
        comps.object = self.obj

        # Calculate values needed for the Lighting model
        comps.point = ray.position(comps.t)
        comps.eyev = -ray.direction
        comps.normalv = comps.object.normal_at(comps.point)

        # Determine if the ray hit from inside the object.
        # Used to avoid darkening the surface too much.
        if Vec3.dot(comps.normalv, comps.eyev) < 0:
            comps.inside = True
            comps.normalv = -comps.normalv
        else:
            comps.inside = False

        # after negating the normal, if necessary
        comps.reflectv = reflect(ray.direction, comps.normalv)

        # This is used for generating shadows, avoids graphical "acne"
        comps.over_point = comps.point + comps.normalv * EPSILON
        # This is used for generating refraction, where light is bended
        comps.under_point = comps.point - comps.normalv * EPSILON

        # Calculating Refractive Indices
        if xs is None:
            xs = GroupIntersections()

        # TODO: Might need a unique id for the shapes. The container seems to be remove when it shouldn't.
        containers = []
        for intersect in xs:
            if intersect == self:
                if containers:
                    comps.n1 = containers[-1].material.refractive_index

            for shape in containers:
                if shape.id == intersect.obj.id:
                    containers.remove(intersect.obj)
                    break
            else:
                containers.append(intersect.obj)

            if intersect == self:
                if containers:
                    comps.n2 = containers[-1].material.refractive_index
                break

        return comps

"""
This class is a container of all Intersection that has occurred from a
Ray intersect Shape operation. The Intersections are sorted by their
't' values from negative to positive.
"""
class GroupIntersections(object):

    def __init__(self, *args: Intersection):
        self.intersects = [intersect for intersect in args]
        self.intersects.sort(key=operator.attrgetter('t'))

    def __getitem__(self, index):
        return self.intersects[index]

    def __len__(self):
        return len(self.intersects)

    def __add__(self, other):
        assert isinstance(other, GroupIntersections), f'The other operand must be of type: {GroupIntersections.__name__}'
        all_intersections = []
        for intersect in self:
            all_intersections.append(intersect)
        for intersect in other:
            all_intersections.append(intersect)
        return GroupIntersections(*all_intersections)

    def add_intersection(self, intersect: Intersection) -> None:
        bisect.insort(self.intersects, intersect)

    def hit(self) -> Optional[Intersection]:
        """ Find the closest intersection with a positive value. A positive value
        represents an intersection that occur in the forward direction.

        :return: The closest Intersection that occurs in the Group of Intersections.
        Can be "None", representing no intersection that occurred.
        """
        for intersect in self.intersects:
            if intersect.t < 0:
                continue
            return intersect
        return None
