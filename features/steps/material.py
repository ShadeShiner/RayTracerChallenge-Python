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


@when('result = lighting(m, light, position, eyev, normalv, in_shadow)')
def step_impl(context):
    context.result = lighting(context.m, context.light, context.position,
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
