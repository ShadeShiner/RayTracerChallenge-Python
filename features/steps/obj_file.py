import os

from behave import given, when, then

from src.ObjParser import parse_obj_file
from src.VectorAndMatrix import point


@given('{file_name} = a file containing')
def step_impl(context, file_name):
    file_path = os.path.join(os.curdir, 'files', f'{file_name}.obj')
    with open(file_path, 'w', newline='') as out_fp:
        out_fp.write(context.text)


@given('file = the file "{file_name}"')
def step_impl(context, file_name):
    file_path = os.path.join(os.curdir, 'files', file_name)
    assert os.path.isfile(file_path), f'The file "{file_name}" does not exists in the files directory'


@when('{group} = "{group_name}" from parser')
def step_impl(context, group, group_name):
    parser_group = context.parser.get_group(group_name)
    setattr(context, group, parser_group)


@when('parser = parse_obj_file({file_name})')
def step_impl(context, file_name):
    file_path = os.path.join(os.curdir, 'files', f'{file_name}.obj')
    context.parser = parse_obj_file(file_path)


@when('g = parser.default_group')
def step_impl(context):
    context.g = context.parser.default_group


@when('t2 = second child of g')
def step_impl(context):
    context.t2 = context.g[1]


@when('t3 = third child of g')
def step_impl(context):
    context.t3 = context.g[2]


@when('{triangle} = first child of {group}')
def step_impl(context, triangle, group):
    obj_group = getattr(context, group)
    setattr(context, triangle, obj_group[0])


@then('parser should have ignored 5 lines')
def step_impl(context):
    assert len(context.parser.vertices) == 0, 'There should be no vertices found in the parser'
    assert len(context.parser.faces) == 0, 'There should be no faces found in the parser'


@then('parser.vertices[{index:d}] = point({x:g}, {y:g}, {z:g})')
def step_impl(context, index, x, y, z):
    result = context.parser.vertices[index-1]
    expected = point(x, y, z)
    assert expected == result, f'parser.vertices[{index}] != point({x}, {y}, {z})'


@then('{triangle}.{attribute} = parser.vertices[{index:d}]')
def step_impl(context, triangle, attribute, index):
    obj_triangle = getattr(context, triangle)
    point = getattr(obj_triangle, attribute)
    assert point == context.parser.vertices[index-1], f'{triangle}.{attribute} != parser.vertices[{index}]'
