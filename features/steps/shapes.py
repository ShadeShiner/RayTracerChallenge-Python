from behave import given, then, when

from src.Shapes.Plane import Plane
from src.Shapes.TestShape import TestShape
from src.VectorAndMatrix import Matrix
from src.VectorAndMatrix import point, vector


@given('s = test_shape()')
def step_impl(context):
    context.s = TestShape()


@when('set_transform(s, translation({x:g}, {y:g}, {z:g}))')
def step_impl(context, x, y, z):
    context.s.transform = Matrix.translation(x, y, z)


@then('s.transform = translation({x:g}, {y:g}, {z:g})')
def step_impl(context, x, y, z):
    expected = Matrix.translation(x, y, z)
    result = context.s.transform
    assert expected == result, f's.transform != {expected}'


@then('s.saved_ray.origin = point({x:g}, {y:g}, {z:g})')
def step_impl(context, x, y, z):
    expected = point(x, y, z)
    result = context.s.saved_ray.origin
    assert expected == result, f's.saved_ray.origin != {expected}'


@then('s.saved_ray.direction = vector({x:g}, {y:g}, {z:g})')
def step_impl(context, x, y, z):
    expected = vector(x, y, z)
    result = context.s.saved_ray.direction
    assert expected == result, f's.saved_ray.direction != {expected}'


@when('set_transform(s, translation({x:g}, {y:g}, {z:g})')
def step_impl(context, x, y, z):
    context.s.transform = Matrix.translation(x, y, z)


@when('set_transform(s, m)')
def step_impl(context):
    context.s.transform = context.m


@given('shape.material.ambient = {value:g}')
def step_impl(context, value):
    context.shape.material.ambient = value


@given('floor = plane() with')
def step_impl(context):
    floor = Plane()
    floor.transform = Matrix.translation(0, -1, 0)
    floor.material.transparency = 0.5
    floor.material.refractive_index = 1.5
    context.floor = floor
