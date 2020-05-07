"""
This file tests to see that the Canvas, Vector/Position, and Tuples work correctly in order to
correctly draw pixels and store them into a .ppm image. Can use software like GIMP to see the image.
"""
from Vector import point, vector, Vec3
from Canvas import Canvas
from Color import Color


class Projectile(object):

    def __init__(self, position, velocity):
        self.position = position
        self.velocity = velocity


class Environment(object):

    def __init__(self, gravity, wind):
        self.gravity = gravity
        self.wind = wind


def tick(env, proj):
    proj.position = proj.position + proj.velocity
    proj.velocity = proj.velocity + env.gravity + env.wind
    return Projectile(proj.position, proj.velocity)


# Can probably have this done internally in the Canvas class, but left
# it here for simplicity and it doesn't hide how the conversion is done.
def convert_position_to_canvas(canvas: Canvas, world_position: Vec3):
    """Converts the position from world to canvas. This is done by subtracting
    the y world position from the canvas height, the other positions are left alone."""
    return point(round(world_position.x),
                 round(canvas.height - world_position.y),
                 round(world_position.z))


if __name__ == '__main__':
    start = point(0, 1, 0)  # The starting position can be set anywhere different
    velocity = vector(1, 1.8, 0).normalize() * 11.25  # This can be changed to any value to change the trajectory

    p = Projectile(start, velocity)

    gravity = vector(0, -0.1, 0)  # This can be changed to force the projectile down faster/slower
    wind = vector(-0.01, 0, 0)  # This can changed to force the projectile forward less or more
    e = Environment(gravity, wind)

    screen_width = 900  # You can play around with the width of the canvas
    screen_height = 550  # You can play around with the height of the canvas
    c = Canvas(screen_width, screen_height)

    # It's ok if the y position is above the canvas as it can come down into it still.
    # But with the x-axis, it's not worth it since, once it's off screen, the wind is
    # is too strong in the beginning or the it will not return on-screen on the right end
    while p.position.y > 0 and 0 <= p.position.x < c.width:
        canvas_position = convert_position_to_canvas(c, p.position)
        c.write_pixel(canvas_position.x, canvas_position.y, Color(1, 0, 0))
        p = tick(e, p)

    # The final process of storing the canvas to a .ppm file.
    # You can change the name of the file to whatever you like
    with open('ch1and2.ppm', 'w') as fp:
        fp.write(c.to_ppm())
