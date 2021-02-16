from src.VectorAndMatrix import Vec3, point
from src.Shapes.Group import Group
from src.Shapes.Triangle import Triangle


class ObjParser(object):
    def __init__(self):
        self.vertices: [Vec3] = []
        self.faces: [Triangle] = []
        self.default_group = Group()
        self.groups = {}

    def get_group(self, key: str):
        return self.groups[key]

    def add_vertex(self, x: float, y: float, z: float):
        self.vertices.append(point(x, y, z))

    def add_face(self, vertex_index_one: int, vertex_index_two: int, vertex_index_three: int):
        triangle = Triangle(self.vertices[vertex_index_one] - 1,
                            self.vertices[vertex_index_two] - 1,
                            self.vertices[vertex_index_three] - 1)
        self.faces.append(triangle)
        self.default_group.add_child(Triangle)

    def add_triangle(self, triangle: Triangle, group_name:str = None):
        self.faces.append(triangle)
        if group_name is None:
            self.default_group.add_child(triangle)
        else:
            if group_name not in self.groups:
                self.groups[group_name] = [triangle]
            else:
                self.groups[group_name].append(triangle)

    def fan_triangulation(self, vertices: [int]):
        triangles = []

        for index in range(1, len(vertices) - 1):
            tri = Triangle(self.vertices[vertices[0]],
                           self.vertices[vertices[index]],
                           self.vertices[vertices[index+1]])
            triangles.append(tri)

        return triangles


def parse_obj_file(file_name: str) -> ObjParser:
    parser = ObjParser()
    current_group = None

    for line in open(file_name, 'r'):
        if line[0] == 'v':
            x, y, z = line[1:].strip().split()
            parser.add_vertex(float(x), float(y), float(z))
        elif line[0] == 'f':
            vertices = [int(num)-1 for num in line[1:].strip().split()]
            for triangle in parser.fan_triangulation(vertices):
                parser.add_triangle(triangle, current_group)
        elif line[0] == 'g':
            _, current_group = line.split()

    for triangle in parser.faces:
        print(triangle.p1, triangle.p2, triangle.p3)
    return parser


if __name__ == '__main__':
    file_path = r'C:\Users\Adrian\PycharmProjects\RayTracerChallenge\polygon.obj'
    parser = parse_obj_file(file_path)
    '''
    for vertix in parser.vertices:
        print(vertix)

    for face in parser.faces:
        print(face.p1, face.p2, face.p3)
    '''
