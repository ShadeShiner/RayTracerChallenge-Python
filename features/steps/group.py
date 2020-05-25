from behave import given, then, when

from src.Shapes.Group import Group


@given('{attribute} = group()')
def step_impl(context, attribute):
    setattr(context, attribute, Group())


@then('g is empty')
def step_impl(context):
    assert len(context.g.children) == 0, 'The group instance has objects.'


@when('add_child({group}, {shape})')
@given('add_child({group}, {shape})')
def step_impl(context, group, shape):
    g = getattr(context, group)
    s = getattr(context, shape)
    g.add_child(s)


@then('g is not empty')
def step_impl(context):
    assert context.g.child_count() != 0, 'g is empty'


@then('g includes s')
def step_impl(context):
    assert context.g.has_child(context.s), 'g does not include s'


@then('s.parent = g')
def step_impl(context):
    assert context.s.parent == context.g, 's.parent != g'


@given('g = group() of {shapes}')
def step_impl(context, shapes):
    context.g = Group()
    for shape in eval(shapes):
        context.g.add_child(shape)


@when('(left, right) = partition_children(g)')
def step_impl(context):
    context.left, context.right = context.g.partition_children()


@then('g is a group of {expected}')
def step_impl(context, expected):
    expected = eval(expected)
    value = context.g.children
    result = expected == value
    assert result, f'g is not a group of {result} == {expected}'


@then('left = {expected}')
def step_impl(context, expected):
    expected = eval(expected)
    value = context.left
    result = expected == value
    assert result, f'left({value}) != {expected}'


@then('right = {expected}')
def step_impl(context, expected):
    expected = eval(expected)
    value = context.right
    result = expected == value
    assert result, f'right({value}) != {expected}'


@when('make_subgroup(g, {value})')
def step_impl(context, value):
    context.g.make_subgroup(eval(value))


@then('g.count = {expected:d}')
def step_impl(context, expected):
    value = context.g.child_count()
    result = expected == value
    assert result, f'g.count({value}) != {expected}'


@then('g[{index:d}] is a group of {expected}')
def step_impl(context, index, expected):
    expected = eval(expected)
    value = context.g.children[index].children
    result = value == expected
    assert result, f'g[{index}] is not a group of ({value}) != {expected}'


@then('g[{index:d}] = {obj}')
def step_impl(context, index, obj):
    expected = getattr(context, obj)
    value = context.g.children[index]
    result = expected == value
    assert result, f'g[{index}]({value}) != {expected}'


@then('{attribute} = g[{index:d}]')
def step_impl(context, attribute, index):
    setattr(context, attribute, context.g.children[index])


@then('{attribute} is a group')
def step_impl(context, attribute):
    shape = getattr(context, attribute)
    assert isinstance(shape, Group), f'{attribute} is not a group.'


@then('subgroup.count = {expected:d}')
def step_impl(context, expected):
    value = context.subgroup.child_count()
    result = expected == value
    assert result, f'subgroup.count({result}) != {expected}'


@then('subgroup[{index:d}] is a group of {expected}')
def step_impl(context, index, expected):
    expected = eval(expected)
    value = context.subgroup.children[index].children
    result = value == expected
    assert result, f'subgroup[{index}] is not a group of ({value}) != {expected}'


@given('subgroup = group() of {shapes}')
def step_impl(context, shapes):
    context.subgroup = Group()
    for shape in eval(shapes):
        context.subgroup.add_child(shape)
