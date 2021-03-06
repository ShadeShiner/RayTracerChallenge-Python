from behave import given, then, when

from src.Shapes.Plane import Plane
from src.VectorAndMatrix import point, vector
from src.VectorAndMatrix import Matrix


@given('p = Plane()')
def step_impl(context):
    context.p = Plane()


@given('shape = Plane()')
def step_impl(context):
    context.shape = Plane()


@given('shape = Plane() with')
def step_impl(context):
    shape = Plane()
    shape.material.reflective = 0.5
    shape.transform = Matrix.translation(0, -1, 0)
    context.shape = shape


@given('lower = Plane() with')
def step_impl(context):
    lower = Plane()
    lower.material.reflective = 1
    lower.transform = Matrix.translation(0, -1, 0)
    context.lower = lower


@given('upper = Plane() with')
def step_impl(context):
    upper = Plane()
    upper.material.reflective = 1
    upper.transform = Matrix.translation(0, 1, 0)
    context.upper = upper


@when('{attribute:S} = local_normal_at(p, point({x:g}, {y:g}, {z:g}))')
def step_impl(context, attribute, x, y, z):
    setattr(context, attribute, context.p.local_normal_at(point(x, y, z)))


@then('n1 = vector({x:g}, {y:g}, {z:g})')
def step_impl(context, x, y, z):
    expected = vector(x, y, z)
    result = context.n1
    assert expected == result, f'n1 != {expected}'


@then('n2 = vector({x:g}, {y:g}, {z:g})')
def step_impl(context, x, y, z):
    expected = vector(x, y, z)
    result = context.n2
    assert expected == result, f'n2 != {expected}'


@then('n3 = vector({x:g}, {y:g}, {z:g})')
def step_impl(context, x, y, z):
    expected = vector(x, y, z)
    result = context.n3
    assert expected == result, f'n3 != {expected}'


@when('xs = local_intersect(p, r)')
def step_impl(context):
    context.xs = context.p.local_intersect(context.r)


@then('xs is empty')
def step_impl(context):
    assert len(context.xs.intersects) == 0, 'xs is not empty'


@then('xs[{index:d}].object = {shape}')
def step_impl(context, index, shape):
    s = getattr(context, shape)
    assert context.xs.intersects[index].obj == s, f'xs[{index}].object != shape'
