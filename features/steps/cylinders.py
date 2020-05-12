from behave import given, then

from src.Shapes.Cylinder import Cylinder


@given('cyl = cylinder()')
def step_impl(context):
    context.cyl = Cylinder()


@then('cyl.minimum = -infinity')
def step_impl(context):
    result = context.cyl.minimum
    assert result == float('-inf'), f'cyl.minimum:{result} != -infinity'


@then('cyl.maximum = infinity')
def step_impl(context):
    result = context.cyl.maximum
    assert result == float('inf'), f'cyl.maximum:{result} != infinity'


@given('cyl.minimum = {value:g}')
def step_impl(context, value):
    context.cyl.minimum = value


@given('cyl.maximum = {value:g}')
def step_impl(context, value):
    context.cyl.maximum = value


@then('cyl.closed = false')
def step_impl(context):
    assert context.cyl.closed is False, 'cyl.closed != false'


@given('cyl.closed = true')
def step_impl(context):
    context.cyl.closed = True
