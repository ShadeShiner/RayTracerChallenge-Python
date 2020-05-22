"""
Shape represents the parent class that contains all common functions
all children class will have and/or needs to implement.
"""

from src.Material import Material
from src.Ray import Ray
from src.GroupIntersections import GroupIntersections
from src.VectorAndMatrix import Matrix, Vec3 as Point, Vec3 as Vector
from src.BoundingBox import BoundingBox


class Shape(object):

    def __init__(self, parent=None):
        # Converts itself from shape -> world space
        self.transform = Matrix.identity_matrix()
        self.material = Material()
        self.parent = parent
        self.id = id(self)

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

    def normal_at(self, world_point: Point) -> Vector:
        """Calculates a normal that occurs on the given world point.

        :param world_point: A point object in world space. Will be converted to shape space.
        :return: A vector object representing a normal in world space.
        """
        # Convert the world point and normal to shape space
        local_point = self.world_to_object(world_point)
        # Calculate the normal in shape space
        local_normal = self.local_normal_at(local_point)
        # Convert the local normal vector back to world space
        return self.normal_to_world(local_normal)

    def local_normal_at(self, shape_point: Point) -> Vector:
        """ Abstract method that will need to be implemented by the children classes.

        Will calculate the normal at the given point, that is in shape space,
        in relation the shape.

        :param shape_point: A point object that is in shape space.
        :return: A vector object representing the normal in shape space.
        """
        raise NotImplementedError(f'Method "{self.local_intersect.__name__}" needs to be implemented')

    def world_to_object(self, point: Point) -> Point:
        """ Recursively converts the point from world space to object space within
        nested groups.

        :param point: A point in world or group space that will be converted.
        :return: A matrix of the transformation from world to object space
        """
        if self.parent:
            point = self.parent.world_to_object(point)
        result = self.transform.inverse() * point
        return result

    def normal_to_world(self, local_normal: Vector) -> Vector:
        """ Converts a normal in local space to world space.

        :param local_normal: A vector in object space.
        :return: A vector in world space.
        """
        # This will convert to one group space up if there is a parent group.
        normal = self.transform.inverse().transpose() * local_normal
        normal.w = 0
        normal = normal.normalize()

        if self.parent:
            normal = self.parent.normal_to_world(normal)
        return normal

    def bounds_of(self) -> BoundingBox:
        raise NotImplementedError(f'Method "{self.local_intersect.__name__}" needs to be implemented')

    def parent_space_bounds_of(self) -> BoundingBox:
        return self.bounds_of().transform(self.transform)
