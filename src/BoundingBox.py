from src.VectorAndMatrix import point, Vec3 as Point, Matrix
from src.Ray import Ray
from src.utils import check_axis


class BoundingBox:

    def __init__(self, min: Point=None, max: Point=None):
        if min is None:
            self.min = point(float('inf'), float('inf'), float('inf'))
        else:
            self.min = min
        if max is None:
            self.max = point(float('-inf'), float('-inf'), float('-inf'))
        else:
            self.max = max

    def add(self, point: Point):
        if isinstance(point, Point):
            if self.min.x > point.x:
                self.min.x = point.x
            if self.min.y > point.y:
                self.min.y = point.y
            if self.min.z > point.z:
                self.min.z = point.z

            if self.max.x < point.x:
                self.max.x = point.x
            if self.max.y < point.y:
                self.max.y = point.y
            if self.max.z < point.z:
                self.max.z = point.z
        else:
            self.add(point.min)
            self.add(point.max)

    def contains_point(self, point: Point) -> bool:
        if isinstance(point, BoundingBox):
            return self.contains_point(point.min) and \
                   self.contains_point(point.max)
        else:
            return self.min.x <= point.x <= self.max.x and \
                   self.min.y <= point.y <= self.max.y and \
                   self.min.z <= point.z <= self.max.z

    def transform(self, matrix: Matrix):
        p1 = self.min
        p2 = point(self.min.x, self.min.y, self.max.z)
        p3 = point(self.min.x, self.max.y, self.min.z)
        p4 = point(self.min.x, self.max.y, self.max.z)
        p5 = point(self.max.x, self.min.y, self.min.z)
        p6 = point(self.max.x, self.min.y, self.max.z)
        p7 = point(self.max.x, self.max.y, self.min.z)
        p8 = self.max

        new_bounding_box = BoundingBox()
        for p in [p1, p2, p3, p4, p5, p6, p7, p8]:
            new_bounding_box.add(matrix * p)

        return new_bounding_box

    def intersects(self, ray: Ray) -> bool:
        # TODO: Could avoid having to check all six faces?
        xtmin, xtmax = check_axis(ray.origin.x, ray.direction.x, self.min.x, self.max.x)
        ytmin, ytmax = check_axis(ray.origin.y, ray.direction.y, self.min.y, self.max.y)
        ztmin, ztmax = check_axis(ray.origin.z, ray.direction.z, self.min.z, self.max.z)

        tmin = max(xtmin, ytmin, ztmin)
        tmax = min(xtmax, ytmax, ztmax)

        return tmax > tmin
