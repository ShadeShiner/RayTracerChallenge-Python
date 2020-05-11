from src.Color import Color
from src.VectorAndMatrix import Vec3, Vec3 as Point, Vec3 as Vector, reflect
from src.PointLight import PointLight

"""
Material represents the color, lighting, reflectiveness,
refractiveness, transparency of a Shape.

Ambient - Background lighting, or light reflected from other objects in the environment. 
Colors all points on the surface equally.

Diffuse - Light reflected from a matte surface.
It depends only on the angle between the light source and the surface normal.

Specular - The reflection from the light source - the bright spot on the curved surface.
It depends on the reflect vector and the eye vector. Controlled by "shininess", meaning
a higher "shininess", a smaller and tighter specular highlight.

Pattern - (Optional) A pattern that will be applied to the surface of the object. If a
pattern is set, it will override the color for the lighting model.

Reflective - How much light reflects from the surface of the object. The higher the
value, the more of the light reflects.

Transparency - How much the surface can be seen through the object. The higher the
value, the less of the surface is visible.

Refractive Index - Indicates how likely an object will bend the light ray once it
collides with the surface of the object.
"""
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
                 point: Point, eyev: Vector, normalv: Vector,
                 in_shadow: bool) -> Color:
        """Calculates the color shaded on the surface of the object using various
        properties from the material.

        :param obj: The Shape object that will be used if a pattern is set.
        :param light: A light source that potentially intersects with the surface.
        :param point: A point in the space.
        :param eyev: A vector representing the direction from the point on the surface to the eye of the view
        :param normalv: The normal of the surface.
        :param in_shadow: Boolean indicating if the point is in shadow between an object and the light source.
        :return:
        """
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
