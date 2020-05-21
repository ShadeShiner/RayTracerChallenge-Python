from behave import given, then, when

from src.GroupIntersections import GroupIntersections, Intersection
from src.VectorAndMatrix import point, vector
from src.utils import EPSILON, equal


@given('i = intersection({t:g}, {attribute:S})')
def step_impl(context, t, attribute):
    instance = getattr(context, attribute)
    context.i = Intersection(t, instance)


@when('comps = prepare_computations(i, r)')
def step_impl(context):
    context.comps = context.i.prepare_computations(context.r)


@then('comps.t = i.t')
def step_impl(context):
    expected = context.i.t
    result = context.comps.t
    assert expected == result, 'comps.t != i.t'


@then('comps.object = i.object')
def step_impl(context):
    expected = context.i.obj
    result = context.comps.object
    assert expected == result, 'comps.object != i.object'


@then('comps.point = point({x:g}, {y:g}, {z:g})')
def step_impl(context, x, y, z):
    expected = point(x, y, z)
    result = context.comps.point
    assert expected == result, f'comps.point != {expected}'


@then('comps.eyev = vector({x:g}, {y:g}, {z:g})')
def step_impl(context, x, y, z):
    expected = vector(x, y, z)
    result = context.comps.eyev
    assert expected == result, f'comps.eyev != {expected}'


@then('comps.normalv = vector({x:g}, {y:g}, {z:g})')
def step_impl(context, x, y, z):
    expected = vector(x, y, z)
    result = context.comps.normalv
    assert expected == result, f'comps.normalv != {expected}'


@then('comps.inside = false')
def step_impl(context):
    assert context.comps.inside is False, 'comps.inside = true'


@then('comps.inside = true')
def step_impl(context):
    assert context.comps.inside is True, 'comps.inside = false'


@then('comps.over_point.z < -EPSILON/2')
def step_impl(context):
    expected = -EPSILON / 2
    result = context.comps.over_point.z
    assert result < expected, 'comps.over_point.z >= -EPSILON/2'


@then('comps.point.z > comps.over_point.z')
def step_impl(context):
    expected = context.comps.over_point.z
    result = context.comps.point.z
    assert result > expected, 'comps.point.z <= comps.over_point.z'


@then('comps.reflectv = vector({x:g}, {y:g}, {z:g})')
def step_impl(context, x, y, z):
    expected = vector(x, y, z)
    result = context.comps.reflectv
    assert expected == result, f'{result} != {expected}'


@given('xs = intersections(2:A, 2.75:B, 3.25:C, 4.75:B, 5.25:C, 6:A)')
def step_impl(context):
    context.xs = GroupIntersections(
        Intersection(2.0, context.A),
        Intersection(2.75, context.B),
        Intersection(3.25, context.C),
        Intersection(4.75, context.B),
        Intersection(5.25, context.C),
        Intersection(6.0, context.A)
    )


@when('comps = prepare_computations(i, r, xs)')
def step_impl(context):
    context.comps = context.i.prepare_computations(context.r, context.xs)


@then('comps.n1 = "{n1}"')
def step_impl(context, n1):
    assert context.comps.n1 == float(n1), f'{context.comps.n1} != {n1}'


@then('comps.n2 = "{n2}"')
def step_impl(context, n2):
    assert context.comps.n2 == float(n2), f'{context.comps.n2} != {n2}'


@given('xs = intersections(i)')
def step_impl(context):
    context.xs = GroupIntersections(context.i)


@then('comps.under_point.z > EPSILON/2')
def step_impl(context):
    expected = EPSILON/2
    result = context.comps.under_point.z
    assert result > expected, 'comps.under_point.z <= EPSILON/2'


@then('comps.point.z < comps.under_point.z')
def step_impl(context):
    assert context.comps.point.z < context.comps.under_point.z, 'comps.point.z >= comps.under_point.z'


@given('xs = intersections(4:shape, 6:shape)')
def step_impl(context):
    context.xs = GroupIntersections(Intersection(4, context.shape),
                                    Intersection(6, context.shape))


@when('comps = prepare_computations(xs[{index:d}], r, xs)')
def step_impl(context, index):
    intersect = context.xs[index]
    ray = context.r
    intersections = context.xs
    context.comps = intersect.prepare_computations(ray, intersections)


@given('xs = intersection(-0.7071067811865476:shape, 0.7071067811865476:shape)')
def step_impl(context):
    context.xs = GroupIntersections(Intersection(-0.7071067811865476, context.shape),
                                    Intersection(0.7071067811865476, context.shape))


@given('xs = intersection(-0.9899:A, -0.4899:B, 0.4899:B, 0.9899:A)')
def step_impl(context):
    context.xs = GroupIntersections(Intersection(-0.9899, context.A),
                                    Intersection(-0.4899, context.B),
                                    Intersection(0.4899, context.B),
                                    Intersection(0.9899, context.A))


@given('xs = intersections(1.4142135623730951:floor)')
def step_impl(context):
    context.xs = GroupIntersections(Intersection(1.4142135623730951, context.floor))


@given('xs = intersections(-0.7071067811865476:shape, 0.7071067811865476:shape)')
def step_impl(context):
    context.xs = GroupIntersections(Intersection(-0.7071067811865476, context.shape),
                                    Intersection(0.7071067811865476, context.shape))


@given('xs = intersection(-1:shape, 1:shape)')
def step_impl(context):
    context.xs = GroupIntersections(Intersection(-1, context.shape),
                                    Intersection(1, context.shape))


@given('xs = intersections(1.8589:shape)')
def step_impl(context):
    context.xs = GroupIntersections(Intersection(1.8589, context.shape))


@when('reflectance = schlick(comps)')
def step_impl(context):
    context.reflectance = context.comps.schlick()


@then('reflectance = {expected:g}')
def step_impl(context, expected):
    result = context.reflectance
    assert equal(expected, result), f'{result} != {expected}'

@then('xs.count = {n:d}')
def step_impl(context, n):
    expected = n
    result = len(context.xs.intersects)
    assert equal(expected, result), f'xs.count:{result} != {n}'

@then('xs[{i:d}].t = {expected:g}')
def step_impl(context, i, expected):
    result = context.xs.intersects[i].t
    assert equal(expected, result), f'xs[{i}]:{result} != {expected}'
