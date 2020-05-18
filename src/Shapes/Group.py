from src.GroupIntersections import GroupIntersections
from src.Ray import Ray
from src.Shapes.Shape import Shape


class Group(Shape):

    def __init__(self, *args, **kwargs):
        super(Group, self).__init__(*args, **kwargs)
        self.children: [Shape] = []

    def add_child(self, child: Shape):
        self.children.append(child)
        child.parent = self

    def local_intersect(self, shape_ray: Ray) -> GroupIntersections:
        all_intersections = GroupIntersections()
        for child in self.children:
            all_intersections += child.intersect(shape_ray)
        return all_intersections

    def child_count(self) -> int:
        return len(self.children)

    def has_child(self, child: Shape) -> bool:
        return child in self.children
