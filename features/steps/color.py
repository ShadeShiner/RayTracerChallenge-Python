from behave import given, then, when

from src.Color import Color
from src.Vector import point


@then('c = color({r:g}, {g:g}, {b:g})')
def step_impl(context, r, g, b):
    expected = Color(r, g, b)
    result = context.c
    print(result)
    assert expected == result, f'c != {expected}'


@then('c = inner.material.color')
def step_impl(context):
    expected = context.inner.material.color
    result = context.c
    assert expected == result, 'c != inner.material.color'


@given('black = color({r:g}, {g:g}, {b:g})')
def step_impl(context, r, g, b):
    context.black = Color(r, g, b)


@given('white = color({r:g}, {g:g}, {b:g})')
def step_impl(context, r, g, b):
    context.white = Color(r, g, b)


@then('c1 = color({r:g}, {g:g}, {b:g})')
def step_impl(context, r, g, b):
    expected = Color(r, g, b)
    result = context.c1
    assert expected == result, f'{result} != {expected}'


@then('c2 = color({r:g}, {g:g}, {b:g})')
def step_impl(context, r, g, b):
    expected = Color(r, g, b)
    result = context.c2
    assert expected == result, f'{result} != {expected}'


@when('c = stripe_at_object(pattern, object, point({x:g}, {y:g}, {z:g}))')
def step_impl(context, x, y, z):
    context.c = context.pattern.pattern_at_shape(context.object, point(x, y, z))


@then('c = white')
def step_impl(context):
    expected = context.white
    result = context.c
    assert expected == result, 'c != white'


@then('color = color({r:g}, {g:g}, {b:g})')
def step_impl(context, r, g, b):
    expected = Color(r, g, b)
    result = context.color
    assert expected == result, f'{result} != {expected}'
