"""
Shape represents the parent class that contains all common functions
all children class will have and/or needs to implement.
"""

from src.Material import Material
from src.Ray import Ray
from src.GroupIntersections import GroupIntersections
from src.VectorAndMatrix import Matrix, Vec3


class Shape(object):

    def __init__(self):
        # Converts itself from shape -> world space
        self.transform = Matrix.identity_matrix()
        self.material = Material()

    def intersect(self, world_ray: Ray) -> GroupIntersections:
        """ Calculates the intersections that occur with the shape
        according to the given ray that is in world space.

        :param world_ray: A Ray object in world space, that will be converted to shape space.
        :return: A GroupIntersections object that contains all intersections on the shape by the ray.
        """
        # Converting the ray from world space to shape space
        local_ray = world_ray.transform(self.transform.inverse())
        return self.local_intersect(local_ray)

    def local_intersect(self, shape_ray: Ray) -> GroupIntersections:
        """ Abstract method that will need to be implemented by the children classes.

        Will calculate the intersections that occur with the shape
        according to the given ray that is in object space.

        :param shape_ray: A Ray object in shape space. Will be used to find intersects.
        :return: A GroupIntersections object that contains all intersection on the shape
        by the ray in shape space.
        """
        raise NotImplementedError(f'Method "{self.local_intersect.__name__}" needs to be implemented')

    def normal_at(self, world_point: Vec3) -> Vec3:
        """Calculates a normal that occurs on the given world point.

        :param world_point: A point object in world space. Will be converted to shape space.
        :return: A vector object representing a normal in world space.
        """
        # Convert the world point and normal to shape space
        local_point = self.transform.inverse() * world_point
        local_normal = self.local_normal_at(local_point)

        # Convert the local normal vector back to world space
        world_normal = self.transform.inverse().transpose() * local_normal
        world_normal.w = 0
        return world_normal.normalize()

    def local_normal_at(self, shape_point: Vec3) -> Vec3:
        """ Abstract method that will need to be implemented by the children classes.

        Will calculate the normal at the given point, that is in shape space,
        in relation the shape.

        :param shape_point: A point object that is in shape space.
        :return: A vector object representing the normal in shape space.
        """
        raise NotImplementedError(f'Method "{self.local_intersect.__name__}" needs to be implemented')
