from behave import given, when, then

from src.VectorAndMatrix import point
from src.Color import Color
from src.PointLight import PointLight


@given('light = point_light(point({x:d}, {y:d}, {z:d}), color({r:d}, {g:d}, {b:d}))')
def step_impl(context, x, y, z, r, g, b):
    context.light = PointLight(point(x, y, z), Color(r, g, b))


@when('result = lighting(m, shape, light, position, eyev, normalv, in_shadow)')
def step_impl(context):
    context.result = context.m.lighting(context.shape, context.light, context.position,
                              context.eyev, context.normalv, context.in_shadow)


@then('result = color({r:g}, {g:g}, {b:g})')
def step_impl(context, r, g, b):
    expected = Color(r, g, b)
    result = context.result
    assert expected == result, f'{result} != {expected}'


@given('in_shadow = true')
def step_impl(context):
    context.in_shadow = True


@given('in_shadow = false')
def step_impl(context):
    context.in_shadow = False


@given('m.{attribute:S} = {x:g}')
def step_impl(context, attribute, x):
    setattr(context.m, attribute, x)


@when('{attribute:S} = lighting(m, shape, light, point({x:g}, {y:g}, {z:g}), eyev, normalv, false)')
def step_impl(context, attribute, x, y, z):
    setattr(context, attribute, context.m.lighting(context.shape, context.light,
                          point(x, y, z), context.eyev, context.normalv, False))


@then('m.{attribute:S} = {expected:g}')
def step_impl(context, attribute, expected):
    result = getattr(context.m, attribute)
    assert expected == result, f'{result} != {expected}'
