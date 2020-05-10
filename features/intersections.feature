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

    Scenario: Precomputing the reflection vector
        Given shape = plane()
          And r = ray(point(0, 1, -1), vector(0, -0.70710678, 0.70710678))
          And i = intersection(0.70710678, shape)
         When comps = prepare_computations(i, r)
         Then comps.reflectv = vector(0, 0.70710678, 0.70710678)

    Scenario Outline: Finding n1 and n2 at various intersections
        Given A = glass_sphere() with
          And B = glass_sphere() with
          And C = glass_sphere() with
          And r = ray(point(0, 0, -4), vector(0, 0, 1))
          And xs = intersections(2:A, 2.75:B, 3.25:C, 4.75:B, 5.25:C, 6:A)
         When comps = prepare_computations(xs["<index>"], r, xs)
         Then comps.n1 = "<n1>"
          And comps.n2 = "<n2>"

      Examples: Intersections
      | index | n1  | n2  |
      | 0     | 1.0 | 1.5 |
      | 1     | 1.5 | 2.0 |
      | 2     | 2.0 | 2.5 |
      | 3     | 2.5 | 2.5 |
      | 4     | 2.5 | 1.5 |
      | 5     | 1.5 | 1.0 |

    Scenario: The under point is offset below the surface
        Given r = ray(point(0, 0, -5), vector(0, 0, 1))
          And shape = glass_sphere() with
          And i = intersection(5, shape)
          And xs = intersections(i)
         When comps = prepare_computations(i, r, xs)
         Then comps.under_point.z > EPSILON/2
          And comps.point.z < comps.under_point.z
