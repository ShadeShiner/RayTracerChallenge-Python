from behave import given, then

from src.VectorAndMatrix import Matrix
from src.VectorAndMatrix import Vec3
from src.utils import equal


@given('the following {rows:d}x{columns:d} matrix M')
def step_impl(context, rows, columns):
    context.M = Matrix(rows, columns)
    for row_index, row in enumerate(context.table):
        for column_index, column in enumerate(row):
            context.M.matrix[row_index][column_index] = float(column)


@then('M[{row:d},{column:d}] = {expected:g}')
def step_impl(context, row, column, expected):
    assert context.M.matrix[row][column] == expected, f'M[{row}][{column}] != {expected}'


@given('the following matrix A')
def step_impl(context):
    context.A = Matrix(4, 4)
    for row in range(4):
        for column in range(4):
            context.A.matrix[row][column] = float(context.table[row][column])


@given('the following matrix B')
def step_impl(context):
    context.B = Matrix(4, 4)
    for row in range(4):
        for column in range(4):
            context.B.matrix[row][column] = float(context.table[row][column])


@then('A == B')
def step_impl(context):
    assert context.A == context.B, f'The two matrices are not equal: {context.A.matrix} != {context.B.matrix}'


@then('A != B')
def step_impl(context):
    assert context.A != context.B, f'The two matrices are equal: {context.A.matrix} == {context.B.matrix}'


@then('A * B is the following 4x4 matrix')
def step_impl(context):
    expected = Matrix(4, 4)
    for row in range(4):
        for column in range(4):
            expected.matrix[row][column] = float(context.table[row][column])
    result = context.A * context.B
    assert expected == result, 'The multiplication of A * B does not match the expected result.'


@given('b = tuple({x:g}, {y:g}, {z:g}, {w:g})')
def step_impl(context, x, y, z, w):
    context.b = Vec3(x, y, z, w)


@then('A * b = tuple({x:g}, {y:g}, {z:g}, {w:g})')
def step_impl(context, x, y, z, w):
    expected = Vec3(x, y, z, w)
    result = context.A * context.b
    assert expected == result, 'The multiplication of Matrix A with tuple B does not match the expected result.'


@then('transpose(A) is the following matrix')
def step_impl(context):
    expected = Matrix(4, 4)
    for row in range(4):
        for column in range(4):
            expected.matrix[row][column] = float(context.table[row][column])
    result = context.A.transpose()
    assert expected == result, 'The transpose of Matrix A does not match the expected result.'


@then('determinant(M) = {expected:g}')
def step_impl(context, expected):
    result = context.M.determinant()
    assert expected == result, f'The determinant calculated {result} != {expected}'


@then('submatrix(M, {row:d}, {column:d}) is the following {rows:d}x{columns:d} matrix')
def step_impl(context, row, column, rows, columns):
    expected = Matrix(rows, columns)
    for e_row in range(rows):
        for e_col in range(columns):
            expected.matrix[e_row][e_col] = float(context.table[e_row][e_col])
    result = context.M.submatrix(row, column)
    assert expected == result, 'The expected submatrix was not found with the calculated result.'


@given('B = submatrix(M, {row:d}, {column:d})')
def step_impl(context, row, column):
    context.B = context.M.submatrix(row, column)


@then('determinant(B) = {expected:d}')
def step_impl(context, expected):
    result = context.B.determinant()
    assert expected == result, f'The determinant does not match the expected. {expected} != {result}'


@then('minor(M, {row:d}, {column:d}) = {expected:d}')
def step_impl(context, row, column, expected):
    result = context.M.minor(row, column)
    assert expected == result, f'The minor does not match the expected. {expected} != {result}'


@then('cofactor(M, {row:d}, {column:d}) = {expected:d}')
def step_impl(context, row, column, expected):
    result = context.M.cofactor(row, column)
    assert expected == result, f'The cofactor calculated does not match the expected. {expected} != {result}'


@then('M is invertible')
def step_impl(context):
    result = context.M.determinant()
    assert result != 0, f'The determinant {result} is 0, meaning is not invertible.'


@then('M is not invertible')
def step_impl(context):
    result = context.M.determinant()
    assert result == 0, f'The determinant {result} is not 0, meaning it is invertible.'


@given('B = inverse(M)')
def step_impl(context):
    context.B = context.M.inverse()


@then('B[{row:d}, {column:d}] = {expected:g}')
def step_impl(context, row, column, expected):
    result = context.B.matrix[row][column]
    assert equal(expected, result), f'The values do not match. {expected} != {result}'


@then('B is the following 4x4 matrix')
def step_impl(context):
    expected = Matrix(4, 4)
    for e_row in range(4):
        for e_col in range(4):
            expected.matrix[e_row][e_col] = float(context.table[e_row][e_col])
    result = context.B
    assert expected == result, 'The expected matrix does not match what was given.'


@then('inverse(M) is the following 4x4 matrix')
def step_impl(context):
    expected = Matrix(4, 4)
    for e_row in range(4):
        for e_col in range(4):
            expected.matrix[e_row][e_col] = float(context.table[e_row][e_col])
    result = context.M.inverse()
    assert expected == result, 'The expected matrix is does not match the given inverse.'


@given('the following 4x4 matrix B')
def step_impl(context):
    context.B = Matrix(4, 4)
    for row in range(4):
        for col in range(4):
            context.B.matrix[row][col] = float(context.table[row][col])


@given('C = M * B')
def step_impl(context):
    context.C = context.M * context.B


@then('C * inverse(B) = M')
def step_impl(context):
    expected = context.M
    result = context.C * context.B.inverse()
    assert expected == result, 'The multiplication of C with the inverse of B did not given the original M.'
