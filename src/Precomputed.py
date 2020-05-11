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
