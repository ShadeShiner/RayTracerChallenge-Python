from behave import given, then, when

from src.VectorAndMatrix import Vec3, point, vector, EPSILON
from src.Color import Color


# Tuples

@given('tuple({x:f}, {y:f}, {z:f}, {w:f})')
def step_impl(context, x, y, z, w):
    context.tuple = Vec3(x, y, z, w)


@then('a.x = {x:f}')
def step_impl(context, x):
    assert context.tuple.x == x, 'The given point\'s x value is not equal to the expected value.'


@then('a.y = {y:f}')
def step_impl(context, y):
    assert context.tuple.y == y, 'The given point\'s y value is not equal to the expected value.'


@then('a.z = {z:f}')
def step_impl(context, z):
    assert context.tuple.z == z, 'The given point\'s z value is not equal to the expected value.'


@then('a.w = {w:f}')
def step_impl(context, w):
    assert context.tuple.w == w, 'The given point\'s w value is not equal to the expected value.'


@then('a is a point')
def step_impl(context):
    assert context.tuple.w == 1.0, 'The test object is not a point.'


@then('a is not a vector')
def step_impl(context):
    assert context.tuple.w != 0.0, 'The test object is a vector.'


@then('a is not a point')
def step_impl(context):
    assert context.tuple.w != 1.0, 'The test object is point.'


@then('a is a vector')
def step_impl(context):
    assert context.tuple.w == 0.0, 'The test object is not a vector.'


@given('point({x:f}, {y:f}, {z:f})')
def step_impl(context, x, y, z):
    context.tuple = point(x, y, z)


@then('p = tuple({x:f}, {y:f}, {z:f}, {w:f})')
def step_impl(context, x, y, z, w):
    assert context.tuple.x == x, 'The test x\'s value does not match.'
    assert context.tuple.y == y, 'The test y\'s value does not match.'
    assert context.tuple.z == z, 'The test z\'s value does not match.'
    assert context.tuple.w == w, 'The test w\'s value does not match.'


@given('vector({x:f}, {y:f}, {z:f})')
def step_impl(context, x, y, z):
    context.tuple = vector(x, y, z)


@then('v = tuple({x:f}, {y:f}, {z:f}, {w:f})')
def step_impl(context, x, y, z, w):
    assert context.tuple.x == x, 'The test x\'s value does not match.'
    assert context.tuple.y == y, 'The test y\'s value does not match.'
    assert context.tuple.z == z, 'The test z\'s value does not match.'
    assert context.tuple.w == w, 'The test w\'s value does not match.'


# Operations
@given('a1 = tuple({x:f}, {y:f}, {z:f}, {w:f})')
def step_impl(context, x, y, z, w):
    context.a1 = Vec3(x, y, z, w)


@given('a2 = tuple({x:f}, {y:f}, {z:f}, {w:f})')
def step_impl(context, x, y, z, w):
    context.a2 = Vec3(x, y, z, w)


@then('a1 + a2 = tuple({x:f}, {y:f}, {z:f}, {w:f})')
def step_impl(context, x, y, z, w):
    assert (context.a1 + context.a2) == Vec3(x, y, z, w),\
        'Adding the tuples did not match the expected result.'


@given('{attribute:S} = point({x:f}, {y:f}, {z:f})')
def step_impl(context, attribute, x, y, z):
    setattr(context, attribute, point(x, y, z))


@then('p1 - p2 = vector({x:f}, {y:f}, {z:f})')
def step_impl(context, x, y, z):
    assert (context.p1 - context.p2) == vector(x, y, z),\
        'Subtracting the two points, did not return the expected vector'


@given('{attribute:S} = vector({x:g}, {y:g}, {z:g})')
def step_impl(context, attribute, x, y, z):
    setattr(context, attribute, vector(x, y, z))


@then('p - v = point({x:f}, {y:f}, {z:f})')
def step_impl(context, x, y, z):
    assert (context.p - context.v) == point(x ,y ,z),\
        'The subtraction of a point from a vector did not return the expected vector.'


@then('v1 - v2 = vector({x:f}, {y:f}, {z:f})')
def step_impl(context, x, y, z):
    assert (context.v1 - context.v2) == vector(x, y, z),\
        'The subtraction of the two vectors did not return the expected vector.'


@given('a = tuple({x:f}, {y:f}, {z:f}, {w:f})')
def step_impl(context, x, y, z ,w):
    context.a = Vec3(x, y, z, w)


@then('-a = tuple({x:f}, {y:f}, {z:f}, {w:f})')
def step_impl(context, x, y, z, w):
    assert -context.a == Vec3(x, y, z, w),\
        'The negation of the tuple did not return the expected result.'


@then('a * 3.5 = tuple(3.5, -7, 10.5, -14)')
def step_impl(context):
    assert (context.a * 3.5) == Vec3(3.5, -7, 10.5, -14),\
        'The multiplication of a tuple did not equal an expected tuple.'


@then('a * 0.5 = tuple(0.5, -1.0, 1.5, -2.0)')
def step_impl(context):
    assert (context.a * 0.5) == Vec3(0.5, -1.0, 1.5, -2.0),\
        'The multiplication of a tuple with a fraction did not equal an expected tuple.'


@then('a / 2 = tuple(0.5, -1, 1.5, -2)')
def step_impl(context):
    assert (context.a / 2) == Vec3(0.5, -1.0, 1.5, -2.0),\
        'The division of a tuple with a number did not equal an expected tuple.'


@then('magnitude(v) = {d:g}')
def step_impl(context, d):
    assert abs(context.v.magnitude() - d) < EPSILON, f'The magnitude of the {context.v} is not {d}'


@then(u'magnitude(v) = ‭3.741657386773941‬')
def step_impl(context):
    assert abs(context.v.magnitude() - 3.741657386773941) < EPSILON,\
        f'The magnitude of the {context.v} is not 3.741657386773941'


@then('normalize(v) = vector({x:g}, {y:g}, {z:g})')
def step_impl(context, x, y, z):
    expected = vector(x, y, z)
    assert context.v.normalize() == expected, f'The normalization of vector {context.v} is not {expected}'


@when('norm = normalize(v)')
def step_impl(context):
    context.norm = context.v.normalize()


@then('magnitude(norm) = 1')
def step_impl(context):
    assert context.norm.magnitude() == 1, f'The magnitude of the normalize vector {context.norm} is not 1.'


@then('dot(v1, v2) = {x:g}')
def step_impl(context, x):
    assert Vec3.dot(context.v1, context.v2) == 20,\
        f'The dot product of {context.v1} and {context.v2} is not {x}'


@then('cross(v1, v2) = vector({x:g}, {y:g}, {z:g})')
def step_impl(context, x, y, z):
    expected = vector(x, y, z)
    assert Vec3.cross(context.v1, context.v2) == expected,\
        f'The Cross Product of vector {context.v1} and {context.v2} is not {expected}'


@then('cross(v2, v1) = vector({x:g}, {y:g}, {z:g})')
def step_impl(context, x, y, z):
    expected = vector(x, y, z)
    assert Vec3.cross(context.v2, context.v1) == expected,\
        f'The Cross Product of vector {context.v2} and {context.v1} is not {expected}'


# Colors


@given('c = color({r:g}, {g:g}, {b:g})')
def step_impl(context, r, g, b):
    context.c = Color(r, g, b)


@then('c.red = {v:g}')
def step_impl(context, v):
    assert context.c.red == v, f'The test color {context.c} does not have the expected red value: {v}'


@then('c.green = {v:g}')
def step_impl(context, v):
    assert context.c.green == v, f'The test color {context.c} does not have the expected green value: {v}'


@then('c.blue = {v:g}')
def step_impl(context, v):
    assert context.c.blue == v, f'The test color {context.c} does not have the expected blue value: {v}'


@given('c1 = color({r:g}, {g:g}, {b:g})')
def step_impl(context, r, g, b):
    context.c1 = Color(r, g, b)


@given('c2 = color({r:g}, {g:g}, {b:g})')
def step_impl(context, r, g, b):
    context.c2 = Color(r, g, b)


@then('c1 + c2 = color({r:g}, {g:g}, {b:g})')
def step_impl(context, r, g, b):
    expected = Color(r, g, b)
    result = context.c1 + context.c2
    assert result == expected,\
        f'The sum {result} does not match the expected value {expected}'


@then('c1 - c2 = color({r:g}, {g:g}, {b:g})')
def step_impl(context, r, g, b):
    expected = Color(r, g, b)
    result = context.c1 - context.c2
    assert result == expected,\
        f'The difference {result} does not match the expected value {expected}'


@then('c * {d:g} = color({r:g}, {g:g}, {b:g})')
def step_impl(context, d, r, g, b):
    expected = Color(r, g, b)
    result = context.c * d
    assert result == expected,\
        f'The multiplication of scalar {d} and {context.c} is not {expected}'


@then('c1 * c2 = color({r:g}, {g:g}, {b:g})')
def step_impl(context, r, g, b):
    expected = Color(r, g, b)
    result = context.c1 * context.c2
    assert result == expected,\
        f'The multiplication of {context.c1} and {context.c2} was: {result} != {expected}'
