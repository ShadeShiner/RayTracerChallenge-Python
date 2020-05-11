from behave import given, then, when

from src.World import World, default_world
from src.PointLight import PointLight
from src.VectorAndMatrix import point
from src.Color import Color
from src.Shapes.Sphere import Sphere
from src.VectorAndMatrix import Matrix
from src.TestPattern import TestPattern


@given('w = world()')
def step_impl(context):
    context.w = World()


@then('w contains no objects')
def step_impl(context):
    assert len(context.w.objects) == 0, 'The are objects within the world.'


@then('w has no light source')
def step_impl(context):
    assert context.w.light is None, 'There is a light source within the world.'


@given('s1 = sphere() with')
def step_impl(context):
    context.s1 = Sphere()
    context.s1.material.color = Color(0.8, 1.0, 0.6)
    context.s1.material.diffuse = 0.7
    context.s1.material.specular = 0.2


@given('s2 = sphere() with')
def step_impl(context):
    context.s2 = Sphere()
    context.s2.transform = Matrix.scaling(0.5, 0.5, 0.5)


@when('w = default_world()')
def step_impl(context):
    context.w = default_world()


@then('w.light = light')
def step_impl(context):
    expected = context.light
    result = context.w.light
    assert expected == result, 'w.light != light'


@then('w contains s1')
def step_impl(context):
    for obj in context.w.objects:
        if obj == context.s1:
            break
    else:
        assert False, 'w does not contain s1'


@then('w contains s2')
def step_impl(context):
    for obj in context.w.objects:
        if obj == context.s2:
            break
    else:
        assert False, 'w does not contain s2'


@given('w = default_world()')
def step_impl(context):
    context.w = default_world()


@when('xs = intersect_world(w, r)')
def step_impl(context):
    context.xs = context.w.intersect_world(context.r)


@given('shape = the first object in w')
def step_impl(context):
    context.shape = context.w.objects[0]


@when('c = shade_hit(w, comps)')
def step_impl(context):
    context.c = context.w.shade_hit(context.comps)


@given('w.light = point_light(point({x:g}, {y:g}, {z:g}), color({r:g}, {g:g}, {b:g}))')
def step_impl(context, x, y, z, r, g, b):
    context.w.light = PointLight(point(x, y, z), Color(r, g, b))


@given('shape = the second object in w')
def step_impl(context):
    context.shape = context.w.objects[1]


@when('c = color_at(w, r)')
def step_impl(context):
    context.c = context.w.color_at(context.r)


@given('outer = the first object in w')
def step_impl(context):
    context.outer = context.w.objects[0]


@given('outer.material.ambient = {d:d}')
def step_impl(context, d):
    context.outer.material.ambient = d


@given('inner = the second object in w')
def step_impl(context):
    context.inner = context.w.objects[1]


@given('inner.material.ambient = {d:d}')
def step_impl(context, d):
    context.inner.material.ambient = d


@then('is_shadowed(w, p) is false')
def step_impl(context):
    expected = False
    result = context.w.is_shadowed(context.p)
    assert expected == result, 'Point is in shadow'


@then('is_shadowed(w, p) is true')
def step_impl(context):
    expected = True
    result = context.w.is_shadowed(context.p)
    assert expected == result, 'Point is not in shadow'


@given('s1 is added to w')
def step_impl(context):
    context.w.objects.append(context.s1)


@given('s2 is added to w')
def step_impl(context):
    context.w.objects.append(context.s2)


@when('color = reflected_color(w, comps)')
def step_impl(context):
    context.color = context.w.reflected_color(context.comps)


@given('shape is added to w')
def step_impl(context):
    context.w.objects.append(context.shape)


@when('color = shade_hit(w, comps)')
def step_impl(context):
    context.color = context.w.shade_hit(context.comps)


@given('lower is added to w')
def step_impl(context):
    context.w.objects.append(context.lower)


@given('upper is added to w')
def step_impl(context):
    context.w.objects.append(context.upper)


@then('color_at(w, r) should terminate successfully')
def step_impl(context):
    try:
        context.w.color_at(context.r, 10000)
    except RecursionError:
        pass
    else:
        assert False, 'Recursion depth was not reached'


@when('color = reflected_color(w, comps, {depth:d})')
def step_impl(context, depth):
    context.color = context.w.reflected_color(context.comps, depth)


@when('c = refracted_color(w, comps, {remaining:d})')
def step_impl(context, remaining):
    context.c = context.w.refracted_color(context.comps, remaining)


@given('shape has')
def step_impl(context):
    context.shape.material.transparency = 1.0
    context.shape.material.refractive_index = 1.5


@given('A = the first object in w')
def step_impl(context):
    context.A = context.w.objects[0]


@given('A has')
def step_impl(context):
    context.A.material.ambient = 1.0
    context.A.material.pattern = TestPattern()


@given('B = the second object in w')
def step_impl(context):
    context.B = context.w.objects[1]


@given('B has')
def step_impl(context):
    context.B.material.transparency = 1.0
    context.B.material.refractive_index = 1.5


@given('floor is added to w')
def step_impl(context):
    context.w.objects.append(context.floor)


@given('ball is added to w')
def step_impl(context):
    context.w.objects.append(context.ball)


@when('color = shade_hit(w, comps, {remaining:d})')
def step_impl(context, remaining):
    context.color = context.w.shade_hit(context.comps, remaining)
