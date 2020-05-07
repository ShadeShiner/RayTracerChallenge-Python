from behave import given, then, when

import sys, os
sys.path.append(os.path.abspath(os.path.join(__file__, os.pardir, os.pardir, os.pardir)))
from src.Matrix import Matrix
from src.Vector import point, vector
from src.World import view_transform

@given('transform = translation({x:g}, {y:g}, {z:g})')
def step_impl(context, x, y, z):
    context.transform = Matrix.translation(x, y, z)


@given('p = point({x:g}, {y:g}, {z:g})')
def step_impl(context, x, y, z):
    context.p = point(x, y, z)


@given('inv = inverse(transform)')
def step_impl(context):
    context.inv = context.transform.inverse()


@given('v = vector({x:g}, {y:g}, {z:g})')
def step_impl(context, x, y, z):
    context.v = vector(x, y, z)


@given('transform = scaling({x:g}, {y:g}, {z:g})')
def step_impl(context, x, y, z):
    context.transform = Matrix.scaling(x, y, z)


@given('half_quarter = rotation_x({degrees:g})')
def step_impl(context, degrees):
    context.half_quarter = Matrix.rotation_x(degrees)


@given('inv = inverse(half_quarter)')
def step_impl(context):
    context.inv = context.half_quarter.inverse()


@given('half_quarter = rotation_y({degrees:d})')
def step_impl(context, degrees):
    context.half_quarter = Matrix.rotation_y(degrees)


@given('full_quarter = rotation_y({degrees:d})')
def step_impl(context, degrees):
    context.full_quarter = Matrix.rotation_y(degrees)


@given('transform = shearing({xy:d}, {xz:d}, {yx:d}, {yz:d}, {zx:d}, {zy:d})')
def step_impl(context, xy, xz, yx, yz, zx, zy):
    context.transform = Matrix.shearing(xy, xz, yx, yz, zx, zy)


@given('A = rotation_x({degrees:d})')
def step_impl(context, degrees):
    context.A = Matrix.rotation_x(degrees)


@given('B = scaling({x:g}, {y:g}, {z:g})')
def step_impl(context, x, y, z):
    context.B = Matrix.scaling(x, y, z)


@given('C = translation({x:g}, {y:g}, {z:g})')
def step_impl(context, x, y, z):
    context.C = Matrix.translation(x, y, z)


@when('p2 = A * p')
def step_impl(context):
    context.p2 = context.A * context.p


@when('p3 = B * p2')
def step_impl(context):
    context.p3 = context.B * context.p2


@when('p4 = C * p3')
def step_impl(context):
    context.p4 = context.C * context.p3


@when('T = C * B * A')
def step_impl(context):
    context.T = context.C * context.B * context.A


@then('transform * p = point({x:g}, {y:g}, {z:g})')
def step_impl(context, x, y, z):
    expected = point(x, y, z)
    result = context.transform * context.p
    assert expected == result, f'transform * p != point({x}, {y}, {z})'


@then('inv * p = point({x:g}, {y:g}, {z:g})')
def step_impl(context, x, y, z):
    expected = point(x, y, z)
    result = context.inv * context.p
    assert expected == result, f'inv * p != point({x}, {y}, {z})'


@then('transform * v = v')
def step_impl(context):
    expected = context.v
    result = context.transform * context.v
    assert expected == result, f'transform * v != {expected}'


@then('transform * v = vector({x:g}, {y:g}, {z:g})')
def step_impl(context, x, y, z):
    expected = vector(x, y, z)
    result = context.transform * context.v
    assert expected == result, f'transform * v != {expected}'


@then('inv * v = vector({x:g}, {y:g}, {z:g})')
def step_impl(context, x, y, z):
    expected = vector(x, y, z)
    result = context.inv * context.v
    assert expected == result, f'inv * v != {expected}'


@then('half_quarter * p = point({x:g}, {y:g}, {z:g})')
def step_impl(context, x, y, z):
    expected = point(x, y, z)
    result = context.half_quarter * context.p
    assert expected == result, f'half_quarter * p != {expected}'


@then('full_quarter * p = point({x:g}, {y:g}, {z:g})')
def step_impl(context, x, y, z):
    expected = point(x, y, z)
    result = context.full_quarter * context.p
    assert expected == result, f'full_quarter * p != {expected}'


@then('p2 = point({x:g}, {y:g}, {z:g})')
def step_impl(context, x, y, z):
    expected = point(x, y, z)
    result = context.p2
    assert expected == result, f'p2 != {expected}'


@then('p3 = point({x:g}, {y:g}, {z:g})')
def step_impl(context, x, y, z):
    expected = point(x, y, z)
    result = context.p3
    assert expected == result, f'p3 != {expected}'


@then('p4 = point({x:g}, {y:g}, {z:g})')
def step_impl(context, x, y, z):
    expected = point(x, y, z)
    result = context.p4
    assert expected == result, f'p4 != {expected}'


@then('T * p = point({x:g}, {y:g}, {z:g})')
def step_impl(context, x, y, z):
    expected = point(x, y, z)
    result = context.T * context.p
    assert expected == result


@given('from = point({x:g}, {y:g}, {z:g})')
def step_impl(context, x, y, z):
    context.from_point = point(x, y, z)


@given('to = point({x:g}, {y:g}, {z:g})')
def step_impl(context, x, y, z):
    context.to_point = point(x, y, z)


@given('up = vector({x:g}, {y:g}, {z:g})')
def step_impl(context, x, y, z):
    context.up_vector = vector(x, y, z)


@when('t = view_transform(from, to, up)')
def step_impl(context):
    context.t = view_transform(context.from_point, context.to_point, context.up_vector)


@then('t = identity_matrix')
def step_impl(context):
    assert context.t == Matrix.identity_matrix(), 't != identity_matrix'


@then('t = scaling({x:g}, {y:g}, {z:g})')
def step_impl(context, x, y, z):
    expected = Matrix.scaling(x, y, z)
    assert expected == context.t, f't != {expected}'


@then('t = translation({x:g}, {y:g}, {z:g})')
def step_impl(context, x, y, z):
    expected = Matrix.translation(x, y, z)
    assert expected == context.t, f't != {expected}'


@then('t is the following {col:d}x{row:d} matrix')
def step_impl(context, col, row):
    expected = Matrix(col, row)
    i = j = 0
    for row in context.table:
        for col in row:
            expected._matrix[i][j] = float(col)
            j += 1
        i += 1
        j = 0
    assert expected == context.t, f't != {expected._matrix}'
