from behave import given, then, when

import sys, os
sys.path.append(os.path.abspath(os.path.join(__file__, os.pardir, os.pardir, os.pardir)))
from src.Intersection import Intersections, Intersect, prepare_computations
from src.Vector import point, vector
from src.utils import EPSILON


@given('i = intersection({t:g}, shape)')
def step_impl(context, t):
    context.i = Intersect(t, context.shape)


@when('comps = prepare_computations(i, r)')
def step_impl(context):
    context.comps = prepare_computations(context.i, context.r)


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


@given('i = intersection({t:g}, s2)')
def step_impl(context, t):
    context.i = Intersect(t, context.s2)


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
    context.xs = Intersections(
        Intersect(2.0, context.A),
        Intersect(2.75, context.B),
        Intersect(3.25, context.C),
        Intersect(4.75, context.B),
        Intersect(5.25, context.C),
        Intersect(6.0, context.A)
    )


@when('comps = prepare_computations(xs["{index}"], r, xs)')
def step_impl(context, index):
    context.comps = prepare_computations(
        context.xs[int(index)],
        context.r,
        context.xs)


@when('comps = prepare_computations(i, r, xs)')
def step_impl(context):
    context.comps = prepare_computations(context.i, context.r, context.xs)


@then('comps.n1 = "{n1}"')
def step_impl(context, n1):
    assert context.comps.n1 == float(n1), f'{context.comps.n1} != {n1}'


@then('comps.n2 = "{n2}"')
def step_impl(context, n2):
    assert context.comps.n2 == float(n2), f'{context.comps.n2} != {n2}'


@given('xs = intersections(i)')
def step_impl(context):
    context.xs = Intersections(context.i)


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
    context.xs = Intersections(Intersect(4, context.shape),
                               Intersect(6, context.shape))


@when('comps = prepare_computations(xs[{index:d}], r, xs)')
def step_impl(context, index):
    context.comps = prepare_computations(context.xs[index], context.r, context.xs)


@given('xs = intersection(-0.7071067811865476:shape, 0.7071067811865476:shape)')
def step_impl(context):
    context.xs = Intersections(Intersect(-0.7071067811865476, context.shape),
                               Intersect(0.7071067811865476, context.shape))


@given('xs = intersection(-0.9899:A, -0.4899:B, 0.4899:B, 0.9899:A)')
def step_impl(context):
    context.xs = Intersections(Intersect(-0.9899, context.A),
                               Intersect(-0.4899, context.B),
                               Intersect(0.4899, context.B),
                               Intersect(0.9899, context.A))


@given('xs = intersections(1.4142135623730951:floor)')
def step_impl(context):
    context.xs = Intersections(Intersect(1.4142135623730951, context.floor))
