from src.VectorAndMatrix import Matrix
from src.Canvas import Canvas
from src.VectorAndMatrix import Vec3, point
from src.Color import Color


# Can probably have this done internally in the Canvas class, but left
# it here for simplicity and it doesn't hide how the conversion is done.
def convert_position_to_canvas(canvas: Canvas, world_position: Vec3):
    """Converts the position from world to canvas. This is done by subtracting
    the z world position from the canvas height, the other positions are left alone."""
    return point(round(world_position.x + (canvas.width / 2)),
                 round(world_position.y),
                 round((canvas.height - (canvas.height / 2) - world_position.z)))


if __name__ == '__main__':
    width = 400
    height = 400
    canvas = Canvas(width, height)

    hour_rotation = 360 / 12
    hour_rotation_matrix = Matrix.rotation_y(hour_rotation)

    radius = (3 / 8) * canvas.width
    print(f'Radius: {radius}')
    position = point(0, 0, 1) * radius

    for i in range(12):
        canvas_point = convert_position_to_canvas(canvas, position)
        print(f'Position:{position}\nCanvas:{canvas_point}')
        canvas.write_pixel(canvas_point.x, canvas_point.z, Color(1, 1, 1))
        position = hour_rotation_matrix * position

    with open('clock2.ppm', 'w') as fp:
        fp.write(canvas.to_ppm())
