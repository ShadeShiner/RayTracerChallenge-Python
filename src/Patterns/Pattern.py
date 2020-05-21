from src.VectorAndMatrix import Matrix, Vec3
from src.Color import Color
from src.Shapes.Shape import Shape


class Pattern(object):

    def __init__(self):
        self.transform = Matrix.identity_matrix()

    def pattern_at(self, point: Vec3) -> Color:
        raise NotImplementedError(f'{Pattern.__name__}.pattern_at is not implemented')

    def pattern_at_shape(self, shape: Shape, world_point: Vec3):
        # Convert point from world space to object space
        local_point = shape.world_to_object(world_point)

        # Convert point from object space to pattern space
        pattern_point = self.transform.inverse() * local_point

        # Calculate the color for the point in pattern space
        return self.pattern_at(pattern_point)
