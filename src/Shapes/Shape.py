from src.Material import Material
from src.Ray import Ray
from src.GroupIntersections import GroupIntersections
from src.VectorAndMatrix import Matrix, Vec3


class Shape(object):

    def __init__(self):
        # Converts itself from object -> world space
        self.transform = Matrix.identity_matrix()
        self.material = Material()

    def intersect(self, ray: Ray) -> GroupIntersections:
        # Converting the ray from world space to object space
        local_ray = ray.transform(self.transform.inverse())
        return self.local_intersect(local_ray)

    def local_intersect(self, local_ray: Ray) -> GroupIntersections:
        raise NotImplementedError(f'Method "{self.local_intersect.__name__}" needs to be implemented')

    def normal_at(self, world_point: Vec3) -> Vec3:
        # Convert the world point and normal to local space
        local_point = self.transform.inverse() * world_point
        local_normal = self.local_normal_at(local_point)

        # Convert the local normal vector back to world space
        world_normal = self.transform.inverse().transpose() * local_normal
        world_normal.w = 0
        return world_normal.normalize()

    def local_normal_at(self, local_point) -> Vec3:
        raise NotImplementedError(f'Method "{self.local_intersect.__name__}" needs to be implemented')
