import math
from src.Matrix import Matrix
from src.Ray import Ray
from src.Vector import point
from src.World import World
from src.Canvas import Canvas


class Camera(object):

    def __init__(self, hsize, vsize, field_of_view):
        self.hsize = hsize
        self.vsize = vsize
        self.field_of_view = field_of_view
        self.transform = Matrix.identity_matrix()

        # Calculate pixel size, pixel width, pixel height
        self.fov_radians = math.radians(field_of_view)
        half_view = math.tan(self.fov_radians / 2)
        aspect = hsize / vsize
        if aspect >= 1:
            self.half_width = half_view
            self.half_height = half_view / aspect
        else:
            self.half_width = half_view * aspect
            self.half_height = half_view
        self.pixel_size = (self.half_width * 2) / self.hsize

    def ray_for_pixel(self, px: int, py: int) -> Ray:
        # the offset from the edge of the canvas to pixel's center
        xoffset = (px + 0.5) * self.pixel_size
        yoffset = (py + 0.5) * self.pixel_size

        # the untransformed coordinates of the pixel in world space.
        # (remember that the camera looks toward -z, so +x is to the *left*.)
        world_x = self.half_width - xoffset
        world_y = self.half_height - yoffset

        # using the camera matrix, transform the canvas point and the origin,
        # and then compute the ray's direction vector.
        # (remember that the canvas is at z=-1)
        pixel = self.transform.inverse() * point(world_x, world_y, -1)
        origin = self.transform.inverse() * point(0, 0, 0)
        direction = (pixel - origin).normalize()

        return Ray(origin, direction)

    def render(self, world: World):
        image = Canvas(self.hsize, self.vsize)

        for y in range(self.vsize):
            for x in range(self.hsize):
                ray = self.ray_for_pixel(x, y)
                color = world.color_at(ray)
                image.write_pixel(x, y, color)

        return image


if __name__ == '__main__':
    c = Camera(201, 101, 90)
    r = c.ray_for_pixel(100, 50)
    print(r.origin)
    print(r.direction)
