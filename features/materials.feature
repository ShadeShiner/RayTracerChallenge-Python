Feature: Materials

    Background:
        Given m = material()
          And position = point(0, 0, 0)

    Scenario: Lighting with eye between the light and the surface
        Given eyev = vector(0, 0, -1)
          And normalv = vector(0, 0, -1)
          And light = point_light(point(0, 0, -10), color(1, 1, 1))
          And in_shadow = false
          And shape = sphere()
         When result = lighting(m, shape, light, position, eyev, normalv, in_shadow)
         Then result = color(1.9, 1.9, 1.9)

    Scenario: Lighting with the eye between the light and the surface
        Given eyev = vector(0, 0.7071067811865, -0.7071067811865)
          And normalv = vector(0, 0, -1)
          And light = point_light(point(0, 0, -10), color(1, 1, 1))
          And in_shadow = false
          And shape = sphere()
         When result = lighting(m, shape, light, position, eyev, normalv, in_shadow)
         Then result = color(1.0, 1.0, 1.0)

    Scenario: Lighting with eye opposite surface, light offset 45 degrees
        Given eyev = vector(0, 0, -1)
          And normalv = vector(0, 0, -1)
          And light = point_light(point(0, 10, -10), color(1, 1, 1))
          And in_shadow = false
          And shape = sphere()
         When result = lighting(m, shape, light, position, eyev, normalv, in_shadow)
         Then result = color(0.7364, 0.7364, 0.7364)

    Scenario: Lighting with eye in the path of the reflection vector
        Given eyev = vector(0, -0.7071067811865, -0.7071067811865)
          And normalv = vector(0, 0, -1)
          And light = point_light(point(0, 10, -10), color(1, 1, 1))
          And in_shadow = false
          And shape = sphere()
         When result = lighting(m, shape, light, position, eyev, normalv, in_shadow)
         Then result = color(1.6364, 1.6364, 1.6364)

    Scenario: Lighting with the light behind the surface
        Given eyev = vector(0, 0, -1)
          And normalv = vector(0, 0, -1)
          And light = point_light(point(0, 0, 10), color(1, 1, 1))
          And in_shadow = false
          And shape = sphere()
         When result = lighting(m, shape, light, position, eyev, normalv, in_shadow)
         Then result = color(0.1, 0.1, 0.1)

    Scenario: Lighting with the surface in shadow
        Given eyev = vector(0, 0, -1)
          And normalv = vector(0, 0, -1)
          And light = point_light(point(0, 0, -10), color(1, 1, 1))
          And in_shadow = true
          And shape = sphere()
         When result = lighting(m, shape, light, position, eyev, normalv, in_shadow)
         Then result = color(0.1, 0.1, 0.1)

    Scenario: Lighting with a pattern applied
        Given m.pattern = stripe_pattern(color(1, 1, 1), color(0, 0, 0))
          And m.ambient = 1
          And m.diffuse = 0
          And m.specular = 0
          And eyev = vector(0, 0, -1)
          And normalv = vector(0, 0, -1)
          And light = point_light(point(0, 0, -10), color(1, 1, 1))
          And shape = sphere()
         When c1 = lighting(m, shape, light, point(0.9, 0, 0), eyev, normalv, false)
          And c2 = lighting(m, shape, light, point(1.1, 0, 0), eyev, normalv, false)
         Then c1 = color(1, 1, 1)
          And c2 = color(0, 0, 0)

    Scenario: Reflectivity for the default material
        Given m = material()
         Then m.reflective = 0.0

    Scenario: Transparency and Refractive Index for the default material
        Given m = material()
         Then m.transparency = 0.0
          And m.refractive_index = 1.0

    Scenario: A helper for producing a sphere with a glassy material
        Given s = glass_sphere()
         Then s.transform = identity_matrix
          And s.material.transparency = 1.0
          And s.material.refractive_index = 1.5
