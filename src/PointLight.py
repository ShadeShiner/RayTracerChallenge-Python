from src.VectorAndMatrix import Vec3
from src.Color import Color

"""
A simple data structure representing a light source in the world.
"""
class PointLight(object):

    def __init__(self, position: Vec3, intensity: Color):
        self.position = position
        self.intensity = intensity

    def __eq__(self, other):
        assert isinstance(other, PointLight), 'The other operand must be of type PointLight.'
        return self.position == other.position and self.intensity == other.intensity
