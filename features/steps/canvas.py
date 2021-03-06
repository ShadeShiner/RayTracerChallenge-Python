from behave import given, then, when

from src.Canvas import Canvas
from src.Color import Color


@given('c = canvas({width:d}, {height:d})')
def step_impl(context, width, height):
    context.c = Canvas(width, height)


@then('c.width = {width:d}')
def step_impl(context, width):
    assert context.c.width == width,\
        f'The canvas\' width {context.c.width} does not match the expected value {width}'


@then('c.height = {height:d}')
def step_impl(context, height):
    assert context.c.height == height,\
        f'The canvas\' height {context.c.height} does not match the expected value {height}'


@then('every pixel of c is color({r:g}, {g:g}, {b:g})')
def step_impl(context, r, g, b):
    for row in range(context.c.height):
        for column in range(context.c.width):
            assert context.c.pixels[row][column] == Color(0, 0, 0),\
                f'The pixel at row {row} and column {column} is not black {context.c.pixels[row][column]}'


@given('{attribute:S} = color({r:g}, {g:g}, {b:g})')
def step_impl(context, attribute, r, g, b):
    setattr(context, attribute, Color(r, g, b))


@when('write_pixel({attribute:S}, {x:d}, {y:d}, {color:S})')
def step_impl(context, attribute, x, y, color):
    canvas_instance = getattr(context, attribute)
    color_instance = getattr(context, color)
    canvas_instance.write_pixel(x, y, color_instance)


@then('pixel_at(c, {x:d}, {y:d}) = red')
def step_impl(context, x, y):
    color = context.c.pixel_at(x, y)
    print(color)
    assert color == context.red, f'The color at coordinates ({x}, {y}) is not red.'


@when('ppm = canvas_to_ppm(c)')
def step_impl(context):
    context.ppm = context.c.to_ppm()


@then('lines {start_index:d}-{end_index:d} of ppm are')
def step_impl(context, start_index, end_index):
    test_text = [line.strip() for line in context.text.split('\r\n')]
    canvas_text = [line for line in context.ppm.split('\n')[start_index-1:end_index]]
    assert test_text == canvas_text, f'The lines between the test data and the canvas do not match.'


@when('every pixel of c is set to color({r:g}, {g:g}, {b:g})')
def step_impl(context, r, g, b):
    for x in range(context.c.width):
        for y in range(context.c.height):
            context.c.write_pixel(x, y, Color(r, g, b))


@then('ppm ends with a newline character')
def step_impl(context):
    assert context.ppm[-1] == '\n', 'The Canvas to PPM conversion does not create a new line at the end'
