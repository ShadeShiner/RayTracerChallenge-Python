from src.Shapes.Shape import Shape
from src.GroupIntersections import GroupIntersections, Intersection
from src.Ray import Ray
from src.VectorAndMatrix import Vec3 as Point, Vec3 as Vector, vector, point
from src.BoundingBox import BoundingBox
from src.utils import check_axis


class Cube(Shape):

    def local_intersect(self, shape_ray: Ray) -> GroupIntersections:
        # TODO: Could avoid having to check all six faces?
        xtmin, xtmax = check_axis(shape_ray.origin.x, shape_ray.direction.x)
        ytmin, ytmax = check_axis(shape_ray.origin.y, shape_ray.direction.y)
        ztmin, ztmax = check_axis(shape_ray.origin.z, shape_ray.direction.z)

        tmin = max(xtmin, ytmin, ztmin)
        tmax = min(xtmax, ytmax, ztmax)

        if tmin > tmax:
            return GroupIntersections()

        return GroupIntersections(Intersection(tmin, self), Intersection(tmax, self))

    def local_normal_at(self, shape_point: Point) -> Vector:
        maxc = max(abs(shape_point.x), abs(shape_point.y), abs(shape_point.z))

        if maxc == abs(shape_point.x):
            return vector(shape_point.x, 0, 0)
        elif maxc == abs(shape_point.y):
            return vector(0, shape_point.y, 0)
        else:
            return vector(0, 0, shape_point.z)

    def bounds_of(self) -> BoundingBox:
        return BoundingBox(point(-1, -1, -1), point(1, 1, 1))
