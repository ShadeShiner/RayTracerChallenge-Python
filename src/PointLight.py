class PointLight(object):

    def __init__(self, position, intensity):
        self.position = position
        self.intensity = intensity

    def __eq__(self, other):
        assert isinstance(other, PointLight), 'The other operand must be of type PointLight.'
        return self.position == other.position and self.intensity == other.intensity
