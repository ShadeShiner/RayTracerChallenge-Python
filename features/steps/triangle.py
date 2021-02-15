from behave import given, then, when

from src.Shapes.Triangle import Triangle
from src.VectorAndMatrix import point, vector


@given('t = triangle(p1, p2, p3)')
def step_impl(context):
    context.t = Triangle(context.p1, context.p2, context.p3)


@given('t = triangle(point({x1:g}, {y1:g}, {z1:g}), point({x2:g}, {y2:g}, {z2:g}), point({x3:g}, {y3:g}, {z3:g}))')
def step_impl(context, x1, y1, z1, x2, y2, z2, x3, y3, z3):
    context.t = Triangle(point(x1, y1, z1), point(x2, y2, z2), point(x3, y3, z3))


@when('n1 = local_normal_at(t, point({x:g}, {y:g}, {z:g}))')
def step_impl(context, x, y, z):
    context.n1 = context.t.local_normal_at(point(x, y, z))


@when('n2 = local_normal_at(t, point({x:g}, {y:g}, {z:g}))')
def step_impl(context, x, y, z):
    context.n2 = context.t.local_normal_at(point(x, y, z))


@when('n3 = local_normal_at(t, point({x:g}, {y:g}, {z:g}))')
def step_impl(context, x, y, z):
    context.n3 = context.t.local_normal_at(point(x, y, z))


@then('t.p1 = p1')
def step_impl(context):
    assert context.t.p1 == context.p1, 't.p1 != p1'


@then('t.p2 = p2')
def step_impl(context):
    assert context.t.p2 == context.p2, 't.p2 != p2'


@then('t.p3 = p3')
def step_impl(context):
    assert context.t.p3 == context.p3, 't.p3 != p3'


@then('t.e1 = vector({x:g}, {y:g}, {z:g})')
def step_impl(context, x, y, z):
    expected = vector(x, y, z)
    assert context.t.e1 == expected, f't.e1 != vector({x}, {y}, {z})'


@then('t.e2 = vector({x:g}, {y:g}, {z:g})')
def step_impl(context, x, y, z):
    expected = vector(x, y, z)
    assert context.t.e2 == expected, f't.e2 != vector({x}, {y}, {z})'


@then('t.normal = vector({x:g}, {y:g}, {z:g})')
def step_impl(context, x, y, z):
    expected = vector(x, y, z)
    assert context.t.normal == expected, f't.normal != vector({x}, {y}, {z})'


@then('n1 = t.normal')
def step_impl(context):
    assert context.n1 == context.t.normal, 'n1 != t.normal'


@then('n2 = t.normal')
def step_impl(context):
    assert context.n2 == context.t.normal, 'n2 != t.normal'


@then('n3 = t.normal')
def step_impl(context):
    assert context.n3 == context.t.normal, 'n3 != t.normal'
