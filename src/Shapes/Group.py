from src.BoundingBox import BoundingBox
from src.VectorAndMatrix import Vec3 as Point, Vec3 as Vector
from src.GroupIntersections import GroupIntersections
from src.Ray import Ray
from src.Shapes.Shape import Shape


class Group(Shape):

    def __init__(self, *args, **kwargs):
        super(Group, self).__init__(*args, **kwargs)
        self.children: [Shape] = []

    def local_normal_at(self, shape_point: Point) -> Vector:
        raise NotImplementedError(f'Must not class this method for class: {Group.__name__}')

    def bounds_of(self) -> BoundingBox:
        bounding_box = BoundingBox()
        for child in self.children:
            child_boundary = child.parent_space_bounds_of()
            bounding_box.add(child_boundary)
        return bounding_box

    def add_child(self, child: Shape):
        self.children.append(child)
        child.parent = self

    def local_intersect(self, shape_ray: Ray) -> GroupIntersections:
        all_intersections = GroupIntersections()
        if not self.bounds_of().intersects(shape_ray):
            return all_intersections

        for child in self.children:
            all_intersections += child.intersect(shape_ray)
        return all_intersections

    def child_count(self) -> int:
        return len(self.children)

    def has_child(self, child: Shape) -> bool:
        return child in self.children

    def partition_children(self):
        left_parent, right_parent = self.bounds_of().split_bounds()
        left = []
        right = []

        for child in self.children:
            child_bound = child.parent_space_bounds_of()
            if left_parent.contains_point(child_bound.min) and \
                    left_parent.contains_point(child_bound.max):
                left.append(child)
            elif right_parent.contains_point(child_bound.min) and \
                    right_parent.contains_point(child_bound.max):
                right.append(child)

        for shape in left:
            self.children.remove(shape)
        for shape in right:
            self.children.remove(shape)

        return left, right

    def make_subgroup(self, shapes: [Shape]):
        sub_group = Group()
        for shape in shapes:
            sub_group.add_child(shape)
        self.add_child(sub_group)

    def divide(self, threshold: int):
        if threshold <= self.child_count():
            left, right = self.partition_children()
            if left:
                self.make_subgroup(left)
            if right:
                self.make_subgroup(right)

        for child in self.children:
            child.divide(threshold)
