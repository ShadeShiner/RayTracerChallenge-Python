Feature: Intersections

    Scenario: Precomputing the state of an intersection
        Given r = ray(point(0, 0, -5), vector(0, 0, 1))
          And shape = sphere()
          And i = intersection(4, shape)
         When comps = prepare_computations(i, r)
         Then comps.t = i.t
          And comps.object = i.object
          And comps.point = point(0, 0, -1)
          And comps.eyev = vector(0, 0, -1)
          And comps.normalv = vector(0, 0, -1)

    Scenario: The hit, when an intersection occurs on the outside
        Given r = ray(point(0, 0, -5), vector(0, 0, 1))
          And shape = sphere()
          And i = intersection(4, shape)
         When comps = prepare_computations(i, r)
         Then comps.inside = false

    Scenario: The hit, when an intersection occurs on the inside
        Given r = ray(point(0, 0, 0), vector(0, 0, 1))
          And shape = sphere()
          And i = intersection(1, shape)
         When comps = prepare_computations(i, r)
         Then comps.point = point(0, 0, 1)
          And comps.eyev = vector(0, 0, -1)
          And comps.inside = true
          And comps.normalv = vector(0, 0, -1)

    Scenario: The hit should offset the point
        Given r = ray(point(0, 0, -5), vector(0, 0, 1))
          And shape = sphere() with translation(0, 0, 1)
          And i = intersection(5, shape)
         When comps = prepare_computations(i, r)
         Then comps.over_point.z < -EPSILON/2
          And comps.point.z > comps.over_point.z
