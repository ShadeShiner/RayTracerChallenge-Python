from src.VectorAndMatrix import Matrix


# 1. What happens when you invert the identity matrix?
def question_one():
    print('1. What happens when you invert the identity matrix?')
    print('You get this:')

    m = Matrix.identity_matrix().submatrix(3, 3)
    m = m.inverse()
    for row in m.matrix:
        print(row)
    print('The Identity matrix again :)\n')


# 2. What do you get when you multiply a matrix by its inverse?
def question_two():
    print('2. What do you get when you multiply a matrix by its inverse?')
    m = Matrix(3, 3)
    m._matrix = [[1, 2, 3],
                [20, 5, 6],
                [7, 8, 11]]
    print('We have the following matrix:')
    for row in m.matrix:
        print(row)

    print('\nThe inverse matrix is the following:')
    i = m.inverse()
    for row in i.matrix:
        print(row)

    print('\nThe product of the matrix with it\'s inverse is the following:')
    p = i * m
    for row in p.matrix:
        print(row)


if __name__ == '__main__':
    question_one()
    question_two()
