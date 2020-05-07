import math
from src.Vector import Vec3
from src.utils import equal


class Matrix(object):

    def __init__(self, rows: int, columns: int):
        self.rows = rows
        self.columns = columns

        self._matrix = []
        for row in range(self.rows):
            row_line = []
            for column in range(self.columns):
                row_line.append(0)
            self._matrix.append(row_line)

    def __eq__(self, other):
        assert isinstance(other, Matrix), 'The other operand must be of type Matrix.'

        if self.rows != other.rows or self.columns != other.columns:
            return False

        for row in range(self.rows):
            for column in range(self.columns):
                if not equal(self._matrix[row][column], other.matrix[row][column]):
                    return False
        return True

    def __mul__(self, other):
        if isinstance(other, Matrix):
            result = Matrix(self.rows, other.columns)
            new_columns = self.columns
            for row in range(result.rows):
                for column in range(result.columns):
                    cell_result = 0
                    for i in range(new_columns):
                        cell_result += self._matrix[row][i] * other.matrix[i][column]
                    result.matrix[row][column] = cell_result
            return result
        elif isinstance(other, Vec3):
            return Vec3(
                self._matrix[0][0] * other.x + self._matrix[0][1] * other.y + self._matrix[0][2] * other.z + self._matrix[0][3] * other.w,
                self._matrix[1][0] * other.x + self._matrix[1][1] * other.y + self._matrix[1][2] * other.z + self._matrix[1][3] * other.w,
                self._matrix[2][0] * other.x + self._matrix[2][1] * other.y + self._matrix[2][2] * other.z + self._matrix[2][3] * other.w,
                self._matrix[3][0] * other.x + self._matrix[3][1] * other.y + self._matrix[3][2] * other.z + self._matrix[3][3] * other.w
            )

    @property
    def matrix(self):
        return self._matrix

    @staticmethod
    def identity_matrix():
        identity_matrix = Matrix(4, 4)
        identity_matrix.matrix[0][0] = 1
        identity_matrix.matrix[1][1] = 1
        identity_matrix.matrix[2][2] = 1
        identity_matrix.matrix[3][3] = 1
        return identity_matrix

    @staticmethod
    def translation(x, y, z):
        translation_matrix = Matrix.identity_matrix()
        translation_matrix._matrix[0][3] = x
        translation_matrix._matrix[1][3] = y
        translation_matrix._matrix[2][3] = z
        return translation_matrix

    @staticmethod
    def scaling(x, y, z):
        scaling_matrix = Matrix.identity_matrix()
        scaling_matrix._matrix[0][0] = x
        scaling_matrix._matrix[1][1] = y
        scaling_matrix._matrix[2][2] = z
        return scaling_matrix

    @staticmethod
    def rotation_x(degrees):
        radians = math.radians(degrees)
        result = Matrix(4, 4)
        result._matrix[0][0] = 1
        result._matrix[1][1] = math.cos(radians)
        result._matrix[1][2] = -math.sin(radians)
        result._matrix[2][1] = math.sin(radians)
        result._matrix[2][2] = math.cos(radians)
        result._matrix[3][3] = 1
        return result

    @staticmethod
    def rotation_y(degrees):
        radians = math.radians(degrees)
        result = Matrix(4, 4)
        result._matrix[0][0] = math.cos(radians)
        result._matrix[0][2] = math.sin(radians)
        result._matrix[1][1] = 1
        result._matrix[2][0] = -math.sin(radians)
        result._matrix[2][2] = math.cos(radians)
        result._matrix[3][3] = 1
        return result

    @staticmethod
    def rotation_z(degrees):
        radians = math.radians(degrees)
        result = Matrix(4, 4)
        result._matrix[0][0] = math.cos(radians)
        result._matrix[0][1] = -math.sin(radians)
        result._matrix[1][0] = math.sin(radians)
        result._matrix[1][1] = math.cos(radians)
        result._matrix[2][2] = 1
        result._matrix[3][3] = 1
        return result

    @staticmethod
    def shearing(xy, xz, yx, yz, zx, zy):
        result = Matrix.identity_matrix()
        result._matrix[0][1] = xy
        result._matrix[0][2] = xz
        result._matrix[1][0] = yx
        result._matrix[1][2] = yz
        result._matrix[2][0] = zx
        result._matrix[2][1] = zy
        return result

    def transpose(self):
        transposed = Matrix(self.rows, self.columns)
        for i in range(self.rows):
            for j in range(self.columns):
                transposed.matrix[i][j] = self._matrix[j][i]
        return transposed

    def determinant(self):
        det = 0
        if self.columns == 2:
            det = self._matrix[1][1] * self._matrix[0][0] - self._matrix[0][1] * self._matrix[1][0]
        else:
            for column in range(self.columns):
                det += self._matrix[0][column] * self.cofactor(0, column)
        return det

    def submatrix(self, row, column):
        result = Matrix(self.rows - 1, self.columns - 1)
        result_row_index = result_col_index = 0
        for i in range(self.rows):
            if i == row:
                continue
            for j in range(self.columns):
                if j == column:
                    continue
                result.matrix[result_row_index][result_col_index] = self._matrix[i][j]
                result_col_index += 1
            result_row_index += 1
            result_col_index = 0
        return result

    def minor(self, row, column):
        return self.submatrix(row, column).determinant()

    def cofactor(self, row, column):
        result = self.minor(row, column)
        return result if (row + column) % 2 == 0 else -result

    def inverse(self):
        det = self.determinant()
        assert det != 0, 'The determinant is 0, meaning it cannot be inverted'

        result = Matrix(self.rows, self.columns)

        for row in range(self.rows):
            for column in range(self.columns):
                c = self.cofactor(row, column)
                result.matrix[column][row] = c / det
        return result

