from behave import given, then, when

from src.Shapes.Cube import Cube

@given('c = cube()')
def step_impl(context):
    context.c = Cube()


@when('xs = local_intersect(c, r)')
def step_impl(context):
    context.xs = context.c.local_intersect(context.r)


@when('normal = local_normal_at(c, p)')
def step_impl(context):
    context.normal = context.c.local_normal_at(context.p)
