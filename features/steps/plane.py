from behave import given, then, when

from src.Plane import plane
from src.Vector import point, vector
from src.Matrix import Matrix


@given('p = plane()')
def step_impl(context):
    context.p = plane()


@given('shape = plane()')
def step_impl(context):
    context.shape = plane()


@given('shape = plane() with')
def step_impl(context):
    shape = plane()
    shape.material.reflective = 0.5
    shape.transform = Matrix.translation(0, -1, 0)
    context.shape = shape


@given('lower = plane() with')
def step_impl(context):
    lower = plane()
    lower.material.reflective = 1
    lower.transform = Matrix.translation(0, -1, 0)
    context.lower = lower


@given('upper = plane() with')
def step_impl(context):
    upper = plane()
    upper.material.reflective = 1
    upper.transform = Matrix.translation(0, 1, 0)
    context.upper = upper


@when('n1 = local_normal_at(p, point({x:g}, {y:g}, {z:g}))')
def step_impl(context, x, y, z):
    context.n1 = context.p.local_normal_at(point(x, y, z))


@when('n2 = local_normal_at(p, point({x:g}, {y:g}, {z:g}))')
def step_impl(context, x, y, z):
    context.n2 = context.p.local_normal_at(point(x, y, z))


@when('n3 = local_normal_at(p, point({x:g}, {y:g}, {z:g}))')
def step_impl(context, x, y, z):
    context.n3 = context.p.local_normal_at(point(x, y, z))


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


@then('xs[0].object = p')
def step_impl(context):
    assert context.xs.intersects[0].obj == context.p, 'xs[0].object != p'
