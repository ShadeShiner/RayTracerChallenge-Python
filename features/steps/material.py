from behave import given, when, then

import sys, os
sys.path.append(os.path.abspath(os.path.join(__file__, os.pardir, os.pardir, os.pardir)))
from src.Vector import point
from src.Color import Color
from src.PointLight import PointLight
from src.Material import lighting


@given('light = point_light(point({x:d}, {y:d}, {z:d}), color({r:d}, {g:d}, {b:d}))')
def step_impl(context, x, y, z, r, g, b):
    context.light = PointLight(point(x, y, z), Color(r, g, b))


@when('result = lighting(m, shape, light, position, eyev, normalv, in_shadow)')
def step_impl(context):
    context.result = lighting(context.m, context.shape, context.light, context.position,
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


@given('m.diffuse = {x:g}')
def step_impl(context, x):
    context.m.diffuse = x


@given('m.specular = {x:g}')
def step_impl(context, x):
    context.m.specular = x


@when('c1 = lighting(m, shape, light, point({x:g}, {y:g}, {z:g}), eyev, normalv, false)')
def step_impl(context, x, y, z):
    context.c1 = lighting(context.m, context.shape, context.light,
                          point(x, y, z), context.eyev, context.normalv, False)


@when('c2 = lighting(m, shape, light, point({x:g}, {y:g}, {z:g}), eyev, normalv, false)')
def step_impl(context, x, y, z):
    context.c2 = lighting(context.m, context.shape, context.light,
                          point(x, y, z), context.eyev, context.normalv, False)


@then('m.reflective = {expected:g}')
def step_impl(context, expected):
    result = context.m.reflective
    assert expected == result, f'{result} != {expected}'


@then('m.transparency = {expected:g}')
def step_impl(context, expected):
    assert expected == context.m.transparency, f'm.transparency != {expected}'


@then('m.refractive_index = {expected:g}')
def step_impl(context, expected):
    assert expected == context.m.refractive_index, f'm.refractive_index != {expected}'
