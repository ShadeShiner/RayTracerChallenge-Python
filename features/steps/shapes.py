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
    for row in context.table:
        attributes = row['attribute'].split('.')
        if len(attributes) > 1:
            setattr(floor.material, attributes[1], eval(row['value']))
        else:
            setattr(floor, attributes[0], eval(row['value']))
    context.floor = floor


@then('normal = {normal}')
def step_impl(context, normal):
    expected = eval(normal)
    result = context.normal
    assert expected == result, f'normal:{result} != {expected}'


@when('xs = local_intersect({shape:S}, r)')
def step_impl(context, shape):
    obj = getattr(context, shape)
    context.xs = obj.local_intersect(context.r)


@when('n = local_normal_at({attribute:S}, {position})')
def step_impl(context, attribute, position):
    obj = getattr(context, attribute)
    context.n = obj.local_normal_at(eval(position))


@then('s.parent is nothing')
def step_impl(context):
    assert context.s.parent is None, 'The shape instance has a parent.'


@given('set_transform({shape}, {transform})')
def step_impl(context, shape, transform):
    obj = getattr(context, shape)
    transform = eval(transform)
    obj.transform = transform
