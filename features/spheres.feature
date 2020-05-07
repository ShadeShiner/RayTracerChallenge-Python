Feature: Spheres

    Scenario: The normal on a sphere at a point on the x axis
        Given s = sphere()
         When n = normal_at(s, point(1, 0, 0))
         Then n = vector(1, 0, 0)

    Scenario: The normal on a sphere at a point on the y axis
        Given s = sphere()
         When n = normal_at(s, point(0, 1, 0))
         Then n = vector(0, 1, 0)

    Scenario: The normal on a sphere at a point on the z axis
        Given s = sphere()
         When n = normal_at(s, point(0, 0, 1))
         Then n = vector(0, 0, 1)

    Scenario: The normal on a sphere at a nonaxial point
        Given s = sphere()
         When n = normal_at(s, point(0.577350269189, 0.577350269189, 0.577350269189))
         Then n = vector(0.577350269189, 0.577350269189, 0.577350269189)

    Scenario: The normal is a normalized vector
        Given s = sphere()
         When n = normal_at(s, point(0.577350269189, 0.577350269189, 0.577350269189))
         Then n = normalize(n)

    Scenario: Computing the normal on a translated sphere
        Given s = sphere()
          And set_transform(s, translation(0, 1, 0))
         When n = normal_at(s, point(0, 1.70711, -0.70711))
         Then n = vector(0, 0.70711, -0.70711)

    Scenario: Computing the normal on a transformed sphere
        Given s = sphere()
          And m = scaling(1, 0.5, 1) * rotation_z(36)
          And set_transform(s, m)
         When n = normal_at(s, point(0, 0.7071067811865, -0.7071067811865))
         Then n = vector(0, 0.97014, -0.24254)

    Scenario: Reflecting a vector approaching at 45 degrees
        Given v = vector(1, -1, 0)
          And n = vector(0, 1, 0)
         When r = reflect(v, n)
         Then r = vector(1, 1, 0)

    Scenario: Reflecting a vector off a slanted surface
        Given v = vector(0, -1, 0)
          And n = vector(0.7071067811865, 0.7071067811865, 0)
         When r = reflect(v, n)
         Then r = vector(1, 0, 0)

    Scenario: A point light has a position and intensity
        Given intensity = color(1, 1, 1)
          And position = point(0, 0, 0)
         When light = point_light(position, intensity)
         Then light.position = position
          And light.intensity = intensity

    Scenario: The default material
        Given m = material()
         Then m.color = color(1, 1, 1)
          And m.ambient = 0.1
          And m.diffuse = 0.9
          And m.specular = 0.9
          And m.shininess = 200.0

    Scenario: A sphere has a default material
        Given s = sphere()
         When m = s.material
         Then m = material()

    Scenario: A sphere may be assigned a material
        Given s = sphere()
          And m = material()
          And m.ambient = 1
         When s.material = m
         Then s.material = m
