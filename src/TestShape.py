from src.Ray import Ray
from src.Shape import Shape
from src.Vector import Vec3
from src.Vector import point, vector


class TestShape(Shape):

    def __init__(self):
        super(TestShape, self).__init__()

    def local_intersect(self, local_ray: Ray):
        self.saved_ray = local_ray

    def local_normal_at(self, local_point: Vec3) -> Vec3:
        return vector(local_point.x, local_point.y, local_point.z)


def test_shape():
    return TestShape()