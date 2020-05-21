Feature: Groups

    Scenario: Creating a new group
        Given g = group()
         Then g.transform = identity_matrix
          And g is empty

    Scenario: A shape has a parent attribute
        Given s = test_shape()
         Then s.parent is nothing

    Scenario: Adding a child to a group
        Given g = group()
          And s = test_shape()
         When add_child(g, s)
         Then g is not empty
          And g includes s
          And s.parent = g

    Scenario: Intersecting a ray with an empty group
        Given g = group()
          And r = ray(point(0, 0, 0), vector(0, 0, 1))
         When xs = local_intersect(g, r)
         Then xs is empty

    Scenario: Intersecting a ray with a nonempty group
        Given g = group()
          And s1 = sphere()
          And s2 = sphere()
          And set_transform(s2, Matrix.translation(0, 0, -3))
          And s3 = sphere()
          And set_transform(s3, Matrix.translation(5, 0, 0))
          And add_child(g, s1)
          And add_child(g, s2)
          And add_child(g, s3)
         When r = ray(point(0, 0, -5), vector(0, 0, 1))
          And xs = local_intersect(g, r)
         Then xs.count = 4
          And xs[0].object = s2
          And xs[1].object = s2
          And xs[2].object = s1
          And xs[3].object = s1

    Scenario: Intersecting a transformed group
        Given g = group()
          And set_transform(g, Matrix.scaling(2, 2, 2))
          And s = sphere()
          And set_transform(s, Matrix.translation(5, 0, 0))
          And add_child(g, s)
         When r = ray(point(10, 0, -10), vector(0, 0, 1))
          And xs = intersect(g, r)
         Then xs.count = 2

    Scenario: Converting a point from world to object space
        Given g1 = group()
          And set_transform(g1, Matrix.rotation_y(90))
          And g2 = group()
          And set_transform(g2, Matrix.scaling(2, 2, 2))
          And add_child(g1, g2)
          And s = sphere()
          And set_transform(s, Matrix.translation(5, 0, 0))
          And add_child(g2, s)
         When p = world_to_object(s, point(-2, 0, -10))
         Then p = point(0, 0, -1)

    Scenario: Converting a normal from object to world space
        Given g1 = group()
          And set_transform(g1, Matrix.rotation_y(90))
          And g2 = group()
          And set_transform(g2, Matrix.scaling(1, 2, 3))
          And add_child(g1, g2)
          And s = sphere()
          And set_transform(s, Matrix.translation(5, 0, 0))
          And add_child(g2, s)
          And s = sphere()
          And set_transform(s, Matrix.translation(5, 0, 0))
          And add_child(g2, s)
         When n = normal_to_world(s, vector(0.5773, 0.5773, 0.5773)
         Then n = vector(0.285714, 0.428571, -0.857142)
