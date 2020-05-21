import math
import numbers

from src.utils import EPSILON, equal


class Vec3(object):

    def __init__(self, x, y, z, w):
        self.x = x
        self.y = y
        self.z = z
        self.w = w

    def __add__(self, other):
        assert isinstance(other, Vec3), 'Cannot add to object that is not Vec3.'
        return Vec3(self.x + other.x,
                    self.y + other.y,
                    self.z + other.z,
                    self.w + other.w)

    def __sub__(self, other):
        assert isinstance(other, Vec3), 'Cannot add to object that is not Vec3.'
        return Vec3(self.x - other.x,
                    self.y - other.y,
                    self.z - other.z,
                    self.w - other.w)

    def __neg__(self):
        return Vec3(-self.x, -self.y, -self.z, -self.w)

    def __mul__(self, other):
        assert isinstance(other, numbers.Real), 'The other operand must be a real number.'
        return Vec3(self.x * other, self.y * other, self.z * other, self.w * other)

    def __truediv__(self, other):
        assert isinstance(other, numbers.Real), 'The other operand must be a real number.'
        return Vec3(self.x / other, self.y / other, self.z / other, self.w / other)

    def __eq__(self, other):
        assert isinstance(other, Vec3), 'The other operand must be a Vec3 object as well.'
        if not equal(self.x, other.x) or \
                not equal(self.y, other.y) or \
                not equal(self.z, other.z):
            return False
        return True

    def __str__(self):
        return f'Vec3(x={self.x},y={self.y},z={self.z},w={self.w})'

    def magnitude(self):
        return math.sqrt(self.x ** 2 + self.y ** 2 + self.z ** 2 + self.w ** 2)

    def normalize(self):
        magnitude = self.magnitude()
        return Vec3(self.x / magnitude, self.y / magnitude,
                    self.z / magnitude, self.w / magnitude)

    @staticmethod
    def dot(v1, v2):
        x = v1.x * v2.x
        y = v1.y * v2.y
        z = v1.z * v2.z
        w = v1.w * v2.w
        return x + y + z + w

    @staticmethod
    def cross(v1, v2):
        return Vec3(v1.y * v2.z - v1.z * v2.y,
                    v1.z * v2.x - v1.x * v2.z,
                    v1.x * v2.y - v1.y * v2.x,
                    0.0)


def point(x, y, z):
    return Vec3(x, y, z, 1.0)


def vector(x, y, z):
    return Vec3(x, y, z, 0.0)


def reflect(in_vector: Vec3, normal: Vec3):
    return in_vector - normal * 2 * Vec3.dot(in_vector, normal)


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


def view_transform(from_point: Vec3, to_point: Vec3, up_vector: Vec3):
    """ Creates a camera view transformation matrix that will re-orientate in
    the world to be in the appropriate position relative to the camera.

    :param from_point: src.Vector.Vec3 Point representing where the camera's position.
    :param to_point: src.Vector.Vec3  Point representing where the camera wants to look.
    :param up_vector: src.Vector.Vec3 Vector representing the Up direction in world space.
    :return:
    """
    forward_vector = (to_point - from_point).normalize()
    world_up = up_vector.normalize()
    left_vector = Vec3.cross(forward_vector, world_up)
    view_up = Vec3.cross(left_vector, forward_vector)

    orientation = Matrix.identity_matrix()
    orientation._matrix[0][0] = left_vector.x
    orientation._matrix[0][1] = left_vector.y
    orientation._matrix[0][2] = left_vector.z
    orientation._matrix[1][0] = view_up.x
    orientation._matrix[1][1] = view_up.y
    orientation._matrix[1][2] = view_up.z
    orientation._matrix[2][0] = -forward_vector.x
    orientation._matrix[2][1] = -forward_vector.y
    orientation._matrix[2][2] = -forward_vector.z

    return orientation * Matrix.translation(-from_point.x, -from_point.y, -from_point.z)
