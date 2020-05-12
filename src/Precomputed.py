import math
from src.VectorAndMatrix import Vec3

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

    def schlick(self):
        # find the cosine of the angle between the eye and normal vector
        cos = Vec3.dot(self.eyev, self.normalv)

        # total internal reflection can only occur if n1 > n2
        n = self.n1 / self.n2
        sin2_t = n ** 2 * (1.0 - cos ** 2)

        if self.n1 > self.n2:
            if sin2_t > 1.0:
                return 1.0
            # compute cosine of theta_t using trig identity
            cos_t = math.sqrt(1.0 - sin2_t)

            # when n1 > n2, use cos(theta_t) instead
            cos = cos_t

        r0 = ((self.n1 - self.n2) / (self.n1 + self.n2)) ** 2
        return r0 + (1 - r0) * (1 - cos) ** 5


    def __str__(self):
        result = []
        for key in self.__dict__:
            result.append(f'{key}={self.__dict__[key]}')
        return '\n'.join(result)
