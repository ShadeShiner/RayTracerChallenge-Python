from src.Shapes.Sphere import Sphere
from src.Shapes.Cylinder import Cylinder
from src.Shapes.Group import Group
from src.VectorAndMatrix import Matrix, view_transform
from src.World import World
from src.PointLight import PointLight
from src.VectorAndMatrix import point, vector
from src.Color import Color
from src.Camera import Camera



def hexagon_corner():
    corner = Sphere()
    corner.transform = Matrix.translation(0, 0, -1) * \
                       Matrix.scaling(0.25, 0.25, 0.25)
    return corner



def hexagon_edge():
    edge = Cylinder()
    edge.minimum = 0
    edge.maximum = 1
    edge.transform = Matrix.translation(0, 0, -1) * \
                     Matrix.rotation_y(-30) * \
                     Matrix.rotation_z(-90) * \
                     Matrix.scaling(0.25, 1, 0.25)
    return edge



def hexagon_side():
    side = Group()

    side.add_child(hexagon_corner())
    side.add_child(hexagon_edge())

    return side



def hexagon():
    hex = Group()

    for n in range(6):
        side = hexagon_side()
        side.transform = Matrix.rotation_y(n * 60)
        hex.add_child(side)

    return hex



def ch14():
    world = World()
    world.light = PointLight(point(-10, 10, -10), Color(1, 1, 1))

    hex = hexagon()
    world.objects.append(hex)

    camera = Camera(100, 50, 60)
    camera.transform = view_transform(point(0, 2, -1),
                                      point(0, 0, 0),
                                      vector(0, 1, 0))
    canvas = camera.render(world)

    with open('ch14.ppm', 'w') as fp:
        fp.write(canvas.to_ppm())



if __name__ == '__main__':
    ch14()
