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
