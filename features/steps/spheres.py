from behave import given, then, when

from src.VectorAndMatrix import Matrix, point, vector, reflect
from src.Color import Color
from src.PointLight import PointLight
from src.Material import Material
from src.Sphere import Sphere, glass_sphere


@when('n = normal_at(s, point({x:g}, {y:g}, {z:g}))')
def step_impl(context, x, y, z):
    p = point(x, y, z)
    context.n = context.s.normal_at(p)


@then('n = vector({x:g}, {y:g}, {z:g})')
def step_impl(context, x, y, z):
    expected = vector(x, y, z)
    result = context.n
    assert expected == result, f'{result} != {expected}'


@then('n = normalize(n)')
def step_impl(context):
    expected = context.n.normalize()
    result = context.n
    assert expected == result, f'{result} != {expected}'


@given('set_transform(s, translation({x:d}, {y:d}, {z:d}))')
def step_impl(context, x, y, z):
    context.s.transform = Matrix.translation(x, y, z)


@given('m = scaling({x:g}, {y:g}, {z:g}) * rotation_z({degrees:g})')
def step_impl(context, x, y, z, degrees):
    context.m = Matrix.scaling(x, y, z) * Matrix.rotation_z(degrees)


@given('set_transform(s, m)')
def step_impl(context):
    context.s.transform = context.m


@given('n = vector({x:g}, {y:g}, {z:g})')
def step_impl(context, x, y, z):
    context.n = vector(x, y, z)


@when('r = reflect(v, n)')
def step_impl(context):
    context.r = reflect(context.v, context.n)


@then('r = vector({x:g}, {y:g}, {z:g})')
def step_impl(context, x, y, z):
    expected = vector(x, y, z)
    result = context.r
    assert expected == result, f'{result} != {expected}'


@given('intensity = color({r:d}, {g:d}, {b:d})')
def step_impl(context, r, g, b):
    context.intensity = Color(r, g, b)


@given('position = point({x:d}, {y:d}, {z:d})')
def step_impl(context, x, y, z):
    context.position = point(x, y, z)


@when('light = point_light(position, intensity)')
def step_impl(context):
    context.light = PointLight(context.position, context.intensity)


@then('light.position = position')
def step_impl(context):
    expected = context.position
    result = context.light.position
    assert expected == result, f'{result} != {expected}'


@then('light.intensity = intensity')
def step_impl(context):
    expected = context.intensity
    result = context.light.intensity
    assert expected == result, f'{result} != {expected}'


@given('m = material()')
def step_impl(context):
    context.m = Material()


@then('m.color = color({r:d}, {g:d}, {b:d})')
def step_impl(context, r, g, b):
    expected = Color(r, g, b)
    result = context.m.color
    assert expected == result, f'{result} != {expected}'


@then('m.ambient = {expected:g}')
def step_impl(context, expected):
    result = context.m.ambient
    assert expected == result, f'{result} != {expected}'


@then('m.diffuse = {expected:g}')
def step_impl(context, expected):
    result = context.m.diffuse
    assert expected == result, f'{result} != {expected}'


@then('m.specular = {expected:g}')
def step_impl(context, expected):
    result = context.m.specular
    assert expected == result, f'{result} != {expected}'


@then('m.shininess = {expected:g}')
def step_impl(context, expected):
    result = context.m.shininess
    assert expected == result, f'{result} != {expected}'


@given('m = s.material')
def step_impl(context):
    context.m = context.s.material


@when('m = s.material')
def step_impl(context):
    context.m = context.s.material


@then('m = material()')
def step_impl(context):
    expected = Material()
    result = context.m
    assert expected == result, f'{result} != {expected}'


@given('m.ambient = {value:d}')
def step_impl(context, value):
    context.m.ambient = value


@when('s.material = m')
def step_impl(context):
    context.s.material = context.m


@then('s.material = m')
def step_impl(context):
    expected = context.m
    result = context.s.material
    assert expected == result, f'{result} != {expected}'


@given('shape = sphere()')
def step_impl(context):
    context.shape = Sphere()


@given('s1 = sphere()')
def step_impl(context):
    context.s1 = Sphere()


@given('shape = sphere() with translation({x:g}, {y:g}, {z:g})')
def step_impl(context, x, y, z):
    s = Sphere()
    s.transform = Matrix.translation(x, y, z)
    context.shape = s


@given('s2 = sphere() with translation({x:g}, {y:g}, {z:g})')
def step_impl(context, x, y, z):
    s = Sphere()
    s.transform = Matrix.translation(x, y, z)
    context.s2 = s


@given('object = sphere()')
def step_impl(context):
    context.object = Sphere()


@given('set_transform(object, scaling({x:g}, {y:g}, {z:g}))')
def step_impl(context, x, y, z):
    context.object.transform = Matrix.scaling(x, y, z)


@given('set_transform(shape, scaling({x:g}, {y:g}, {z:g}))')
def step_impl(context, x, y, z):
    context.shape.transform = Matrix.scaling(x, y, z)


@given('s = glass_sphere()')
def step_impl(context):
    context.s = glass_sphere()


@then('s.material.transparency = {expected:g}')
def step_impl(context, expected):
    result = context.s.material.transparency
    assert expected == result, f'{result} != {expected}'


@then('s.material.refractive_index = {expected:g}')
def step_impl(context, expected):
    result = context.s.material.refractive_index
    assert expected == result, f'{result} != {expected}'


@given('A = glass_sphere() with')
def step_impl(context):
    s = glass_sphere()
    s.transform = Matrix.scaling(2, 2, 2)
    s.material.refractive_index = 1.5
    context.A = s


@given('B = glass_sphere() with')
def step_impl(context):
    s = glass_sphere()
    s.transform = Matrix.translation(0, 0, -0.25)
    s.material.refractive_index = 2.0
    context.B = s


@given('C = glass_sphere() with')
def step_impl(context):
    s = glass_sphere()
    s.transform = Matrix.translation(0, 0, 0.25)
    s.material.refractive_index = 2.5
    context.C = s


@given('shape = glass_sphere() with')
def step_impl(context):
    s = glass_sphere()
    s.transform = Matrix.translation(0, 0, 1)
    context.shape = s


@given('ball = sphere() with')
def step_impl(context):
    ball = Sphere()
    ball.material.color = Color(1, 0, 0)
    ball.material.ambient = 0.5
    ball.transform = Matrix.translation(0, -3.5, -0.5)
    context.ball = ball
