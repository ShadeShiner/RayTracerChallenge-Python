from src.Canvas import Canvas
from src.Shapes.Sphere import Sphere
from src.Color import Color
from src.VectorAndMatrix import Matrix, view_transform
from src.Ray import Ray
from src.VectorAndMatrix import point, vector
from src.PointLight import PointLight
from src.Material import Material
from src.World import World
from src.Camera import Camera


def ch5and6():
    # start the ray at z = -5
    ray_origin = point(0, 0, -5)

    # put the wall at z = 10
    wall_z = 10
    wall_size = 7

    canvas_pixels = 100
    pixel_size = wall_size / canvas_pixels
    half = wall_size / 2

    canvas = Canvas(canvas_pixels, canvas_pixels)
    shape = Sphere()

    # Optional sphere transformations - uncomment to see the sphere changes
    # shape.transform = Matrix.rotation_z(45) * Matrix.scaling(0.5, 1, 1)
    # shape.transform = Matrix.scaling(1, 0.5, 1)
    # shape.transform = Matrix.shearing(1, 0, 0, 0, 0, 0) * Matrix.scaling(0.5, 1, 1)

    # CH 6
    # CH 6.1
    shape.material.color = Color(1, 0.2, 1)

    # CH 6.2
    light_position = point(-10, 10, -10)
    light_color = Color(1, 1, 1)
    light = PointLight(light_position, light_color)

    # for each row of pixels in the canvas
    for y in range(canvas_pixels):

        # compute the world y coordinate (top = +half, bottom = -half)
        # canvas -> world coordinate conversion
        # (0, 0) -> (-3.5, 3.5)
        # (99, 99) -> (3.43, -3.43)
        world_y = half - pixel_size * y

        # for each pixel in the row
        for x in range(canvas_pixels):

            # compute the world x coordinate (left = -half, right = half)
            world_x = -half + pixel_size * x

            # describe the point on the wall that the ray will target
            position = point(world_x, world_y, wall_z)

            r = Ray(ray_origin, (position - ray_origin).normalize())
            xs = shape.intersect(r)

            intersection = xs.hit()
            if intersection is not None:
                # World position of the intersection
                intersect_point = r.position(intersection.t)
                # World position of the normal at the point
                intersect_normal = intersection.obj.normal_at(intersect_point)
                # Reverse ray direction to get vector from intersection to eye
                eye = -r.direction

                # Color is calculate by the material of the sphere, ambient, diffuse, specular, and the light sources
                color = intersection.obj.material.lighting(light, intersect_point, eye, intersect_normal)
                canvas.write_pixel(x, y, color)

    with open('ch6.ppm', 'w') as fp:
        fp.write(canvas.to_ppm())


def ch7():
    # Step 1
    floor = Sphere()
    floor.transform = Matrix.scaling(10, 0.01, 10)
    floor.material = Material()
    floor.material.color = Color(1, 0.9, 0.9)
    floor.material.specular = 0

    # Step 2
    left_wall = Sphere()
    left_wall.transform = Matrix.translation(0, 0, 5) * Matrix.rotation_y(-45) * \
                          Matrix.rotation_x(90) * Matrix.scaling(10, 0.01, 10)
    left_wall.material = floor.material

    # Step 3
    right_wall = Sphere()
    right_wall.transform = Matrix.translation(0, 0, 5) * Matrix.rotation_y(45) * \
                           Matrix.rotation_x(90) * Matrix.scaling(10, 0.01, 10)
    right_wall.material = floor.material

    # Step 4
    middle = Sphere()
    middle.transform = Matrix.translation(-0.5, 1, 0.5)
    middle.material = Material()
    middle.material.color = Color(0.1, 1, 0.5)
    middle.material.diffuse = 0.7
    middle.material.specular = 0.3

    # Step 5
    right = Sphere()
    right.transform = Matrix.translation(1.5, 0.5, -0.5) * Matrix.scaling(0.5, 0.5, 0.5)
    right.material = Material()
    right.material.color = Color(0.5, 1, 0.1)
    right.material.diffuse = 0.7
    right.material.specular = 0.3

    # Step 6
    left = Sphere()
    left.transform = Matrix.translation(-1.5, 0.33, -0.75) * Matrix.scaling(0.33, 0.33, 0.33)
    left.material = Material()
    left.material.color = Color(1, 0.8, 0.1)
    left.material.diffuse = 0.7
    left.material.specular = 0.3

    world = World()
    world.light = PointLight(point(-10, 10, -10), Color(1, 1, 1))
    world.objects.extend([floor, left_wall, right_wall, middle, right, left])

    camera = Camera(100, 50, 60)
    # camera = Camera(500, 250, 60)
    camera.transform = view_transform(point(0, 1.5, -5),
                                      point(0, 1, 0),
                                      vector(0, 1, 0))

    canvas = camera.render(world)

    with open('ch8.ppm', 'w') as fp:
        fp.write(canvas.to_ppm())


if __name__ == '__main__':
    ch7()
