from behave import given, then, when

from src.Camera import Camera
from src.VectorAndMatrix import Matrix, view_transform, point, vector
from src.utils import equal
from src.Color import Color


@given('hsize = {size:d}')
def step_impl(context, size):
    context.hsize = size


@given('vsize = {size:d}')
def step_impl(context, size):
    context.vsize = size


@given('field_of_view = {degrees:d}')
def step_impl(context, degrees):
    context.field_of_view = degrees


@given('c = camera({width:d}, {height:d}, {degrees:d})')
def step_impl(context, width, height, degrees):
    context.c = Camera(width, height, degrees)


@when('c = camera(hsize, vsize, field_of_view)')
def step_impl(context):
    context.c = Camera(context.hsize, context.vsize, context.field_of_view)


@then('c.hsize = {expected:d}')
def step_impl(context, expected):
    result = context.c.hsize
    assert expected == result, f'c.hsize != {expected}'


@then('c.vsize = {expected:d}')
def step_impl(context, expected):
    result = context.c.vsize
    assert expected == result, f'c.vsize != {expected}'


@then('c.field_of_view = {expected:d}')
def step_impl(context, expected):
    result = context.c.field_of_view
    assert expected == result, f'c.field_of_view != {expected}'


@then('c.transform = identity_matrix')
def step_impl(context):
    assert context.c.transform == Matrix.identity_matrix(), 'c.transform != identity_matrix'


@then('c.pixel_size = {expected:g}')
def step_impl(context, expected):
    assert equal(expected, context.c.pixel_size), f'c.pixel_size != {expected}'


@when('r = ray_for_pixel(c, {width:d}, {height:d})')
def step_impl(context, width, height):
    context.r = context.c.ray_for_pixel(width, height)


@then('r.origin = point({x:g}, {y:g}, {z:g})')
def step_impl(context, x, y, z):
    expected = point(x, y, z)
    assert expected == context.r.origin, f'r.origin != {expected}'


@then('r.direction = vector({x:g}, {y:g}, {z:g})')
def step_impl(context, x, y, z):
    expected = vector(x, y, z)
    assert expected == context.r.direction, f'r.origin != {expected}'


@when('c.transform = rotation_y({degrees:d}) * translation({x:g}, {y:g}, {z:g})')
def step_impl(context, degrees, x, y, z):
    context.c.transform = Matrix.rotation_y(degrees) * Matrix.translation(x, y, z)


@given('c.transform = view_transform(from, to, up)')
def step_impl(context):
    context.c.transform = view_transform(context.from_point, context.to_point, context.up_vector)


@when('image = render(c, w)')
def step_impl(context):
    context.image = context.c.render(context.w)


@then('pixel_at(image, {x:d}, {y:d}) = color({r:g}, {g:g}, {b:g})')
def step_impl(context, x, y, r, g, b):
    expected = Color(r, g, b)
    result = context.image.pixel_at(x, y)
    assert expected == result, f'{result} != {expected}'
