from behave import given, then

from src.Shapes.Cylinder import Cylinder
from src.Shapes.Cone import Cone


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


@given('shape = cone()')
def step_impl(context):
    context.shape = Cone()


@given('shape.minimum = {value:g}')
def step_impl(context, value):
    context.shape.minimum = value


@given('shape.maximum = {value:g}')
def step_impl(context, value):
    context.shape.maximum = value


@given('shape.closed = true')
def step_impl(context):
    context.shape.closed = True
