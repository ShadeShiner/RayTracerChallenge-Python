from behave import given, then, when

from src.Color import Color
from src.VectorAndMatrix import point


@then('{attribute:S} = color({r:g}, {g:g}, {b:g})')
def step_impl(context, attribute, r, g, b):
    expected = Color(r, g, b)
    result = context
    for prop in attribute.split('.'):
        result = getattr(result, prop)
    assert expected == result, f'c != {expected}'


@then('c = inner.material.color')
def step_impl(context):
    expected = context.inner.material.color
    result = context.c
    assert expected == result, 'c != inner.material.color'


@given('{attribute:S} = color({r:g}, {g:g}, {b:g})')
def step_impl(context, attribute, r, g, b):
    setattr(context, attribute, Color(r, g, b))


@when('c = stripe_at_object(pattern, object, point({x:g}, {y:g}, {z:g}))')
def step_impl(context, x, y, z):
    context.c = context.pattern.pattern_at_shape(context.object, point(x, y, z))


@then('c = white')
def step_impl(context):
    expected = context.white
    result = context.c
    assert expected == result, 'c != white'
