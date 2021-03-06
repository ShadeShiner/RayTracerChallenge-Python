from behave import given, then, when

from src.VectorAndMatrix import point, vector
from src.Ray import Ray
from src.Shapes.Sphere import Sphere
from src.GroupIntersections import GroupIntersections, Intersection
from src.VectorAndMatrix import Matrix


@given('origin = point({x:d}, {y:d}, {z:d})')
def step_impl(context, x, y, z):
    context.origin = point(x, y, z)


@given('direction = vector({x:g}, {y:g}, {z:g})')
def step_impl(context, x, y, z):
    context.direction = vector(x, y, z)


@when('r = ray(origin, direction)')
def step_impl(context):
    context.r = Ray(context.origin, context.direction)


@then('r.origin = origin')
def step_impl(context):
    assert context.r.origin == context.origin, f'r.origin({context.r.origin}) != origin({context.origin})'


@then('r.direction = direction')
def step_impl(context):
    assert context.r.direction == context.direction, f'r.direction({context.r.direction}) != direction({context.direction})'


@given('r = ray(point({px:g}, {py:g}, {pz:g}), vector({vx:g}, {vy:g}, {vz:g}))')
@when('r = ray(point({px:g}, {py:g}, {pz:g}), vector({vx:g}, {vy:g}, {vz:g}))')
def step_impl(context, px, py, pz, vx, vy, vz):
    context.r = Ray(point(px, py, pz), vector(vx, vy, vz))


@then('position(r, {t:g}) = point({x:g}, {y:g}, {z:g})')
def step_impl(context, t, x, y, z):
    expected = point(x, y, z)
    result = context.r.position(t)
    assert expected == result, f'position(r, 0) - {result} != {expected}'


@given('s = sphere()')
def step_impl(context):
    context.s = Sphere()


@when('xs = intersect({shape}, r)')
def step_impl(context, shape):
    obj = getattr(context, shape)
    context.xs = obj.intersect(context.r)


@then('xs[{i:d}] = {expected:g}')
def step_impl(context, i, expected):
    result = context.xs.intersects[i].t
    assert expected == result, f'xs[{i}] != {expected}'


@when('i = intersection({t:g}, s)')
def step_impl(context, t):
    context.i = Intersection(t, context.s)


@then('i.t = {expected:g}')
def step_impl(context, expected):
    result = context.i.t
    assert expected == result, f'i.t != {expected}'


@then('i.object = s')
def step_impl(context):
    assert context.i.obj == context.s, 'i.object != s'


@given('i1 = intersection({t:d}, s)')
def step_impl(context, t):
    context.i1 = Intersection(t, context.s)


@given('i2 = intersection({t:d}, s)')
def step_impl(context, t):
    context.i2 = Intersection(t, context.s)


@when('xs = intersection(i1, i2)')
def step_impl(context):
    context.xs = GroupIntersections(context.i1, context.i2)


@then('xs[{i:d}].object = s')
def step_impl(context, i):
    expected = context.s
    result = context.xs.intersects[i].obj
    assert expected == result, f'xs[{i:d}].object != s'


@given('xs = intersections(i2, i1)')
def step_impl(context):
    context.xs = GroupIntersections(context.i2, context.i1)


@when('i = hit(xs)')
def step_impl(context):
    context.i = context.xs.hit()


@then('i = i1')
def step_impl(context):
    assert context.i == context.i1, 'i != i1'


@then('i = i2')
def step_impl(context):
    assert context.i == context.i2, 'i != i2'


@then('i is nothing')
def step_impl(context):
    assert context.i is None, 'i return a value'


@given('i3 = intersection({t:d}, s)')
def step_impl(context, t):
    context.i3 = Intersection(t, context.s)


@given('i4 = intersection({t:d}, s)')
def step_impl(context, t):
    context.i4 = Intersection(t, context.s)


@given('xs = intersections(i1, i2, i3, i4)')
def step_impl(context):
    context.xs = GroupIntersections(context.i1, context.i2, context.i3, context.i4)


@then('i = i4')
def step_impl(context):
    assert context.i == context.i4, 'i != i4'


@given('m = translation({x:d}, {y:d}, {z:d})')
def step_impl(context, x, y, z):
    context.m = Matrix.translation(x, y, z)


@when('r2 = transform(r, m)')
def step_impl(context):
    context.r2 = context.r.transform(context.m)


@then('r2.origin = point({x:d}, {y:d}, {z:d})')
def step_impl(context, x, y, z):
    expected = point(x, y, z)
    result = context.r2.origin
    assert expected == result, f'r2.origin != {expected}'


@given('m = scaling({x:d}, {y:d}, {z:d})')
def step_impl(context, x, y, z):
    context.m = Matrix.scaling(x, y, z)


@then('r2.direction = vector({x:g}, {y:g}, {z:g})')
def step_impl(context, x, y, z):
    expected = vector(x, y, z)
    result = context.r2.direction
    assert expected == result, f'r2.direction != {expected}'


@given('t = translation({x:d}, {y:d}, {z:d})')
def step_impl(context, x, y, z):
    context.t = Matrix.translation(x, y, z)


@when('set_transform(s, t)')
def step_impl(context):
    context.s.transform = context.t


@then('s.transform = t')
def step_impl(context):
    assert context.s.transform == context.t, 's.transform != t'


@when('set_transform(s, scaling({x:d}, {y:d}, {z:d}))')
def step_impl(context, x, y, z):
    context.s.transform = Matrix.scaling(x, y, z)


@when('set_transform(translation({x:d}, {y:d}, {z:d}))')
def step_impl(context, x, y, z):
    context.s.transform = Matrix.translation(x, y, z)


@given('r = ray({origin}, {direction>}')
def step_impl(context, origin, direction):
    context.r = Ray(eval(origin), eval(direction))


@given('r = ray({origin}, direction)')
def step_impl(context, origin):
    context.r = Ray(eval(origin), context.direction)


@given('direction = normalize({direction})')
def step_impl(context, direction):
    context.direction = eval(direction).normalize()
