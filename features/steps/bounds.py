from behave import given, when, then

from src.BoundingBox import BoundingBox
from src.VectorAndMatrix import point


@given('box = bounding_box()')
def step_impl(context):
    context.box = BoundingBox()


@given('{attribute} = bounding_box(min=point({min_x:g}, {min_y:g}, {min_z:g}), max=point({max_x:g}, {max_y:g}, {max_z:g}))')
def step_impl(context, attribute, min_x, min_y, min_z, max_x, max_y, max_z):
    setattr(context, attribute, BoundingBox(point(min_x, min_y, min_z), point(max_x, max_y, max_z)))


@then('{attribute}.min = point({x:g}, {y:g}, {z:g})')
def step_impl(context, attribute, x, y, z):
    expected = point(x, y, z)
    obj = getattr(context, attribute)
    result = obj.min
    is_equal = expected == result
    assert is_equal, f'box.min:{result} != {expected}'


@then('{attribute}.max = point({x:g}, {y:g}, {z:g})')
def step_impl(context, attribute, x, y, z):
    expected = point(x, y, z)
    obj = getattr(context, attribute)
    result = obj.max
    is_equal = expected == result
    assert is_equal, f'box.max:{result} != {expected}'


@given('p1 = point({x:g}, {y:g}, {z:g})')
def step_impl(context, x, y, z):
    context.p1 = point(x, y, z)


@given('p2 = point({x:g}, {y:g}, {z:g})')
def step_impl(context, x, y, z):
    context.p2 = point(x, y, z)


@when('{attribute} is added to {box_attribute}')
def step_impl(context, attribute, box_attribute):
    obj = getattr(context, attribute)
    box_obj = getattr(context, box_attribute)
    box_obj.add(obj)


@when('box = bounds_of({shape})')
def step_impl(context, shape):
    shape_obj = getattr(context, shape)
    context.box = shape_obj.bounds_of()


@then('box_contains_point(box, p) is {expected}')
def step_impl(context, expected):
    expected = eval(expected)
    value = context.box.contains_point(context.p)
    result = value == expected
    assert result, f'box_contains_point(box, p)({value}) != {expected}'


@then('box_contains_box(box, box2) is {expected}')
def step_impl(context, expected):
    expected = eval(expected)
    value = context.box.contains_point(context.box2)
    result = value == expected
    assert result, f'box_contains_point(box, box2)({value}) != {expected}'


@when('{attribute} = transform(box, matrix)')
def step_impl(context, attribute):
    setattr(context, attribute, context.box.transform(context.matrix))


@then('intersects(box, r) is {expected}')
def step_impl(context, expected):
    expected = eval(expected)
    value = context.box.intersects(context.r)
    result = expected == value
    assert result, f'intersects(box, r)({result} != {expected}'
