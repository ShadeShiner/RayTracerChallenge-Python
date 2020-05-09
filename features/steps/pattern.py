from behave import given, then, when

import sys, os
sys.path.append(os.path.abspath(os.path.join(__file__, os.pardir, os.pardir, os.pardir)))
from src.StripePattern import StripePattern
from src.GradientPattern import GradientPattern
from src.RingPattern import RingPattern
from src.CheckerPattern import CheckerPattern
from src.TestPattern import TestPattern
from src.Vector import point
from src.Color import Color
from src.Matrix import Matrix


@given('pattern = stripe_pattern(white, black)')
def step_impl(context):
    context.pattern = StripePattern(context.white, context.black)


@then('pattern.a = white')
def step_impl(context):
    assert context.pattern.a == context.white, 'pattern.a != white'


@then('pattern.b = black')
def step_impl(context):
    assert context.pattern.b == context.black, 'pattern.a != black'


@then('stripe_at(pattern, point({x:g}, {y:g}, {z:g})) = white')
def step_impl(context, x, y, z):
    expected = context.white
    result = context.pattern.pattern_at(point(x, y, z))
    assert expected == result, f'{result} != {expected}'


@then('stripe_at(pattern, point({x:g}, {y:g}, {z:g})) = black')
def step_impl(context, x, y, z):
    expected = context.black
    result = context.pattern.pattern_at(point(x, y, z))
    assert expected == result, f'{result} != {expected}'


@given('m.pattern = stripe_pattern(color({r1:g}, {g1:g}, {b1:g}), color({r2:g}, {g2:g}, {b2:g}))')
def step_impl(context, r1, g1, b1, r2, g2, b2):
    context.m.pattern = StripePattern(Color(r1, g1, b1), Color(r2, g2, b2))


@given('set_pattern_transform(pattern, scaling({x:g}, {y:g}, {z:g}))')
def step_impl(context, x, y, z):
    context.pattern.transform = Matrix.scaling(x, y, z)


@given('set_pattern_transform(pattern, translation({x:g}, {y:g}, {z:g}))')
def step_impl(context, x, y, z):
    context.pattern.transform = Matrix.translation(x, y, z)


@when('set_pattern_transform(pattern, translation({x:g}, {y:g}, {z:g}))')
def step_impl(context, x, y, z):
    context.pattern.transform = Matrix.translation(x, y, z)


@given('pattern = test_pattern()')
def step_impl(context):
    context.pattern = TestPattern()


@then('pattern.transform = identity_matrix')
def step_impl(context):
    expected = Matrix.identity_matrix()
    result = context.pattern.transform
    assert expected == result, 'pattern.transform != identity_matrix'


@then('pattern.transform = translation({x:g}, {y:g}, {z:g})')
def step_impl(context, x, y, z):
    expected = Matrix.translation(x, y, z)
    result = context.pattern.transform
    assert expected == result, f'pattern.transform != {expected}'


@when('c = pattern_at_shape(pattern, shape, point({x:g}, {y:g}, {z:g}))')
def step_impl(context, x, y, z):
    context.c = context.pattern.pattern_at_shape(context.shape, point(x, y, z))


@given('pattern = gradient_pattern(white, black)')
def step_impl(context):
    context.pattern = GradientPattern(context.white, context.black)


@then('pattern_at(pattern, point({x:g}, {y:g}, {z:g})) = white')
def step_impl(context, x, y, z):
    expected = Color(1, 1, 1)
    result = context.pattern.pattern_at(point(x, y, z))
    assert expected == result, f'{result} != {expected}'


@then('pattern_at(pattern, point({x:g}, {y:g}, {z:g})) = black')
def step_impl(context, x, y, z):
    expected = Color(0, 0, 0)
    result = context.pattern.pattern_at(point(x, y, z))
    assert expected == result, f'{result} != {expected}'


@then('pattern_at(pattern, point({x:g}, {y:g}, {z:g})) = color({r:g}, {g:g}, {b:g})')
def step_impl(context, x, y, z, r, g, b):
    expected = Color(r, g, b)
    result = context.pattern.pattern_at(point(x, y, z))
    assert expected == result, f'{result} != {expected}'


@given('pattern = ring_pattern(white, black)')
def step_impl(context):
    context.pattern = RingPattern(context.white, context.black)


@given('pattern = checkers_pattern(white, black)')
def step_impl(context):
    context.pattern = CheckerPattern(context.white, context.black)
