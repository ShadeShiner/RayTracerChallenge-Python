from src.Ray import Ray
from src.Shapes.Shape import Shape
from src.VectorAndMatrix import Vec3, vector, point
from src.GroupIntersections import GroupIntersections
from src.BoundingBox import BoundingBox


class TestShape(Shape):

    def __init__(self):
        super(TestShape, self).__init__()

    def local_intersect(self, shape_ray: Ray) -> GroupIntersections:
        self.saved_ray = shape_ray
        return GroupIntersections()

    def local_normal_at(self, shape_point: Vec3) -> Vec3:
        return vector(shape_point.x, shape_point.y, shape_point.z)

    def bounds_of(self) -> BoundingBox:
        return BoundingBox(point(-1, -1, -1), point(1, 1, 1))
