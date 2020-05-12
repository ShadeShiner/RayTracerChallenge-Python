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

    @test
    Scenario: The Schlick approximation under total internal reflection
        Given shape = glass_sphere()
          And r = ray(point(0, 0, 0.7071067811865476), vector(0, 1, 0))
          And xs = intersections(-0.7071067811865476:shape, 0.7071067811865476:shape)
         When comps = prepare_computations(xs[1], r, xs)
          And reflectance = schlick(comps)
         Then reflectance = 1.0

    @test
    Scenario: The Schlick approximation with a perpendicular viewing angle
        Given shape = glass_sphere()
          And r = ray(point(0, 0, 0), vector(0, 1, 0))
          And xs = intersection(-1:shape, 1:shape)
         When comps = prepare_computations(xs[1], r, xs)
          And reflectance = schlick(comps)
         Then reflectance = 0.04

    @test
    Scenario: The Schlick approximation with small angle and n2 > n1
        Given shape = glass_sphere()
          And r = ray(point(0, 0.99, -2), vector(0, 0, 1))
          And xs = intersections(1.8589:shape)
         When comps = prepare_computations(xs[0], r, xs)
          And reflectance = schlick(comps)
         Then reflectance = 0.48873

    Scenario: shade_hit() with a reflective, transparent material
        Given w = default_world()
          And r = ray(point(0, 0, -3), vector(0, -0.7071067811865476, 0.7071067811865476))
          And floor = plane() with:
            | attribute | value |
            | transform | Matrix.translation(0, -1, 0) |
            | material.reflective | 0.5 |
            | material.transparency | 0.5 |
            | material.refractive_index | 1.5 |
          And floor is added to w
          And ball = sphere() with:
            | attribute | value |
            | material.color | Color(1, 0, 0) |
            | material.ambient | 0.5 |
            | transform | Matrix.translation(0, -3.5, -0.5) |
          And ball is added to w
          And xs = intersections(1.4142135623730951:floor)
         When comps = prepare_computations(xs[0], r, xs)
          And color = shade_hit(w, comps, 5)
         Then color = color(0.93391, 0.69643, 0.69243)
