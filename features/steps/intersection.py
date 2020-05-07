from behave import given, then, when

import sys, os
sys.path.append(os.path.abspath(os.path.join(__file__, os.pardir, os.pardir, os.pardir)))
from src.Intersection import Intersect, prepare_computations
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
