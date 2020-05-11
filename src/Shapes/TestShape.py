from src.Ray import Ray
from src.Shapes.Shape import Shape
from src.VectorAndMatrix import Vec3
from src.VectorAndMatrix import vector


class TestShape(Shape):

    def __init__(self):
        super(TestShape, self).__init__()

    def local_intersect(self, shape_ray: Ray):
        self.saved_ray = shape_ray

    def local_normal_at(self, shape_point: Vec3) -> Vec3:
        return vector(shape_point.x, shape_point.y, shape_point.z)
