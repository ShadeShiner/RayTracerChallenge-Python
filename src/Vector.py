import math
import numbers
from src.utils import EPSILON


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
		if abs(self.x - other.x > EPSILON) or\
			abs(self.y - other.y > EPSILON) or\
			abs(self.z - other.z > EPSILON):
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


if __name__ == '__main__':
	result = 0.19033232037953468 - 0.19032
	print(result)
	print(EPSILON)
	print(result <= EPSILON)
