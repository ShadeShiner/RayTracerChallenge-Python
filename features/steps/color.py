from behave import given, then, when

import sys, os
sys.path.append(os.path.abspath(os.path.join(__file__, os.pardir, os.pardir, os.pardir)))
from src.Color import Color


@then('c = color({r:g}, {g:g}, {b:g})')
def step_impl(context, r, g, b):
    expected = Color(r, g, b)
    result = context.c
    assert expected == result, f'c != {expected}'


@then('c = inner.material.color')
def step_impl(context):
    expected = context.inner.material.color
    result = context.c
    assert expected == result, 'c != inner.material.color'
