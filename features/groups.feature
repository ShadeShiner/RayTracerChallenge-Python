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

    Scenario: A group has a bounding box that contains its children
        Given s = sphere()
          And set_transform(s, Matrix.translation(2, 5, -3) * Matrix.scaling(2, 2, 2))
          And c = cylinder()
          And c.minimum = -2
          And c.maximum = 2
          And set_transform(c, Matrix.translation(-4, -1, 4) * Matrix.scaling(0.5, 1, 0.5))
          And shape = group()
          And add_child(shape, s)
          And add_child(shape, c)
         When box = bounds_of(shape)
         Then box.min = point(-4.5, -3, -5)
          And box.max = point(4, 7, 4.5)

    Scenario: Intersecting ray+group doesn't test children if box is missed
        Given child = test_shape()
          And shape = group()
          And add_child(shape, child)
          And r = ray(point(0, 0, -5), vector(0, 1, 0))
         When xs = intersect(shape, r)
         Then child.saved_ray is unset

    Scenario: Intersecting ray+group tests children if box is hit
        Given child = test_shape()
          And shape = group()
          And add_child(shape, child)
          And r = ray(point(0, 0, -5), vector(0, 0, 1))
         When xs = intersect(shape, r)
         Then child.saved_ray is set

    Scenario: Partitioning a group's children
        Given s1 = sphere() with:
            | variable  | value                        |
            | transform | Matrix.translation(-2, 0, 0) |
          And s2 = sphere() with:
            | variable  | value                       |
            | transform | Matrix.translation(2, 0, 0) |
          And s3 = sphere()
          And g = group() of [context.s1, context.s2, context.s3]
         When (left, right) = partition_children(g)
         Then g is a group of [context.s3]
           And left = [context.s1]
           And right = [context.s2]

    Scenario: Creating a sub-group from a list of children
        Given s1 = sphere()
          And s2 = sphere()
          And g = group()
         When make_subgroup(g, [context.s1, context.s2])
         Then g.count = 1
          And g[0] is a group of [context.s1, context.s2]

    Scenario: Subdividing a group partitions its children
        Given s1 = sphere() with:
          | variable  | value                         |
          | transform | Matrix.translation(-2, -2, 0) |
          And s2 = sphere() with:
            | variable  | value                        |
            | transform | Matrix.translation(-2, 2, 0) |
          And s3 = sphere() with:
            | variable  | value |
            | transform | Matrix.scaling(4, 4, 4) |
          And g = group() of [context.s1, context.s2, context.s3]
         When divide(g, 1)
         Then g[0] = s3
          And subgroup = g[1]
          And subgroup is a group
          And subgroup.count = 2
          And subgroup[0] is a group of [context.s1]
          And subgroup[1] is a group of [context.s2]

    Scenario: Subdividing a group with too few children
        Given s1 = sphere() with:
          | variable  | value                        |
          | transform | Matrix.translation(-2, 0, 0) |
          And s2 = sphere() with:
            | variable  | value                       |
            | transform | Matrix.translation(2, 1, 0) |
          And s3 = sphere() with:
            | variable  | value                        |
            | transform | Matrix.translation(2, -1, 0) |
          And subgroup = group() of [context.s1, context.s2, context.s3]
          And s4 = sphere()
          And g = group() of [context.subgroup, context.s4]
          When divide(g, 3)
          Then g[0] = subgroup
           And g[1] = s4
           And subgroup.count = 2
           And subgroup[0] is a group of [context.s1]
           And subgroup[1] is a group of [context.s2, context.s3]
