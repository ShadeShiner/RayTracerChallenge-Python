from src.Shapes.Plane import Plane
from src.Shapes.Sphere import Sphere
from src.VectorAndMatrix import Matrix, view_transform
from src.Material import Material
from src.Color import Color
from src.World import World
from src.PointLight import PointLight
from src.VectorAndMatrix import point, vector
from src.Camera import Camera
from src.StripePattern import StripePattern


def ch9():
    # Step 1
    floor = Plane()
    floor.transform = Matrix.scaling(10, 0.01, 10)
    floor.material = Material()
    floor.material.color = Color(1, 0.9, 0.9)
    floor.material.specular = 0
    floor.material.pattern = StripePattern(Color(1, 0, 0), Color(0, 0, 1))

    # Middle biggest sphere
    middle = Sphere()
    middle.transform = Matrix.translation(-0.5, 1, 0.5)
    middle.material = Material()
    middle.material.color = Color(0.1, 1, 0.5)
    middle.material.diffuse = 0.7
    middle.material.specular = 0.3

    # Smaller right sphere
    right = Sphere()
    right.transform = Matrix.translation(1.5, 0.5, -0.5) * Matrix.scaling(0.5, 0.5, 0.5)
    right.material = Material()
    right.material.color = Color(0.5, 1, 0.1)
    right.material.diffuse = 0.7
    right.material.specular = 0.3
    right.material.reflective = 1.0

    # Left yellow sphere
    left = Sphere()
    left.transform = Matrix.translation(-1.5, 0.33, -0.75) * Matrix.scaling(0.33, 0.33, 0.33)
    left.material = Material()
    left.material.color = Color(1, 0.8, 0.1)
    left.material.diffuse = 0.7
    left.material.specular = 0.3

    world = World()
    world.light = PointLight(point(-10, 10, -10), Color(1, 1, 1))
    world.objects.extend([floor, middle, right, left])

    camera = Camera(100, 50, 60)
    # camera = Camera(500, 250, 60)
    camera.transform = view_transform(point(0, 1.5, -5),
                                      point(0, 1, 0),
                                      vector(0, 1, 0))

    canvas = camera.render(world)

    with open('ch9.ppm', 'w') as fp:
        fp.write(canvas.to_ppm())


if __name__ == '__main__':
    ch9()
