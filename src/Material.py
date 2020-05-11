from src.Color import Color
from src.VectorAndMatrix import Vec3, reflect
from src.PointLight import PointLight


class Material(object):

    def __init__(self, color=None, ambient=0.1, diffuse=0.9, specular=0.9, shininess=200.0):
        self.color = Color(1, 1, 1) if color is None else color
        self.ambient = ambient
        self.diffuse = diffuse
        self.specular = specular
        self.shininess = shininess
        self.pattern = None
        self.reflective = 0.0
        self.transparency = 0.0
        self.refractive_index = 1.0

    def __eq__(self, other):
        return self.color == other.color and\
               self.ambient == other.ambient and\
               self.diffuse == other.diffuse and\
               self.specular == other.specular and\
               self.shininess == other.shininess


    def lighting(self,
                 obj,
                 light: PointLight,
                 point: Vec3, eyev: Vec3, normalv: Vec3,
                 in_shadow: bool) -> Color:
        color = self.pattern.pattern_at_shape(obj, point) if self.pattern is not None else self.color

        # combine the surface color with the light's color/intensity
        effective_color = color * light.intensity

        # find the direction to the light source
        lightv = (light.position - point).normalize()

        # compute the ambient contribution
        ambient = effective_color * self.ambient

        # if the point is in shadow, ambient should be the only color factored into
        if in_shadow:
            return ambient

        # light_dot_normal represent the cosine of the angle between the
        # light vector and the normal vector. A negative number means the
        # light is on the other side of the surface.
        light_dot_normal = Vec3.dot(lightv, normalv)
        if light_dot_normal < 0:
            diffuse = Color(0, 0, 0)
            specular = Color(0, 0, 0)
        else:
            # compute the diffuse contribution
            diffuse = effective_color * self.diffuse * light_dot_normal

            # reflect_dot_eye represents the cosine of the angle between the
            # reflection vector and the eye vector. A negative number means the
            # light reflects away from the eye.
            reflectv = reflect(-lightv, normalv)
            reflect_dot_eye = Vec3.dot(reflectv, eyev)

            if reflect_dot_eye <= 0:
                specular = Color(0, 0, 0)
            else:
                # compute the specular contribution
                factor = reflect_dot_eye ** self.shininess
                specular = light.intensity * self.specular * factor
        return ambient + diffuse + specular
