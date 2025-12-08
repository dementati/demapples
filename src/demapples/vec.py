from __future__ import annotations
from dataclasses import dataclass
from functools import cache
from itertools import product


@dataclass(eq=True, frozen=True, slots=True)
class Vec2:
    x: int
    y: int

    def __add__(self, other: Vec2) -> Vec2:
        return Vec2(self.x + other.x, self.y + other.y)

    def __sub__(self, other: Vec2) -> Vec2:
        return Vec2(self.x - other.x, self.y - other.y)

    @cache
    def neighbours(self) -> set[Vec2]:
        """
        >>> Vec2(0, 0).neighbours()
        {Vec2(x=0, y=1), Vec2(x=-1, y=-1), Vec2(x=-1, y=1), Vec2(x=1, y=1), Vec2(x=1, y=-1), Vec2(x=-1, y=0), Vec2(x=1, y=0), Vec2(x=0, y=-1)}
        >>> Vec2(1, 1).neighbours()
        {Vec2(x=0, y=1), Vec2(x=1, y=2), Vec2(x=2, y=1), Vec2(x=0, y=0), Vec2(x=2, y=0), Vec2(x=0, y=2), Vec2(x=2, y=2), Vec2(x=1, y=0)}
        """
        neighbours = set()
        for dx, dy in product((-1, 0, 1), repeat=2):
            if dx == 0 and dy == 0:
                continue
            neighbours.add(Vec2(self.x + dx, self.y + dy))
        return neighbours

    def euclidean_distance(self, other: Vec2) -> float:
        """
        >>> Vec2(1, 2).euclidean_distance(Vec2(4, 6))
        5.0
        >>> Vec2(0, 0).euclidean_distance(Vec2(3, 4))
        5.0
        """
        return ((self.x - other.x) ** 2 + (self.y - other.y) ** 2) ** 0.5


@dataclass(eq=True, frozen=True, slots=True)
class Vec3:
    x: int
    y: int
    z: int

    def __add__(self, other: Vec3) -> Vec3:
        return Vec3(self.x + other.x, self.y + other.y, self.z + other.z)

    def __sub__(self, other: Vec3) -> Vec3:
        return Vec3(self.x - other.x, self.y - other.y, self.z - other.z)

    @cache
    def neighbours(self) -> set[Vec3]:
        """
        >>> Vec3(0, 0, 0).neighbours()
        {Vec3(x=0, y=-1, z=-1), Vec3(x=-1, y=1, z=-1), Vec3(x=0, y=-1, z=1), Vec3(x=0, y=1, z=0), Vec3(x=-1, y=1, z=1), Vec3(x=1, y=-1, z=1), Vec3(x=1, y=-1, z=-1), Vec3(x=0, y=0, z=-1), Vec3(x=0, y=0, z=1), Vec3(x=1, y=0, z=1), Vec3(x=1, y=1, z=0), Vec3(x=1, y=0, z=-1), Vec3(x=-1, y=-1, z=-1), Vec3(x=0, y=-1, z=0), Vec3(x=-1, y=-1, z=1), Vec3(x=-1, y=1, z=0), Vec3(x=1, y=-1, z=0), Vec3(x=-1, y=0, z=1), Vec3(x=-1, y=0, z=-1), Vec3(x=1, y=0, z=0), Vec3(x=-1, y=-1, z=0), Vec3(x=0, y=1, z=-1), Vec3(x=0, y=1, z=1), Vec3(x=-1, y=0, z=0), Vec3(x=1, y=1, z=-1), Vec3(x=1, y=1, z=1)}
        >>> Vec3(1, 1, 1).neighbours()
        {Vec3(x=2, y=0, z=2), Vec3(x=0, y=1, z=0), Vec3(x=2, y=2, z=2), Vec3(x=2, y=1, z=0), Vec3(x=1, y=2, z=2), Vec3(x=0, y=0, z=1), Vec3(x=0, y=2, z=1), Vec3(x=1, y=0, z=1), Vec3(x=1, y=1, z=0), Vec3(x=2, y=0, z=1), Vec3(x=2, y=1, z=2), Vec3(x=2, y=2, z=1), Vec3(x=0, y=1, z=2), Vec3(x=1, y=2, z=1), Vec3(x=0, y=2, z=0), Vec3(x=0, y=0, z=0), Vec3(x=1, y=1, z=2), Vec3(x=1, y=0, z=0), Vec3(x=2, y=0, z=0), Vec3(x=2, y=2, z=0), Vec3(x=0, y=1, z=1), Vec3(x=2, y=1, z=1), Vec3(x=1, y=2, z=0), Vec3(x=0, y=0, z=2), Vec3(x=0, y=2, z=2), Vec3(x=1, y=0, z=2)}
        """
        neighbours = set()
        for dx, dy, dz in product((-1, 0, 1), repeat=3):
            if dx == 0 and dy == 0 and dz == 0:
                continue
            neighbours.add(Vec3(self.x + dx, self.y + dy, self.z + dz))
        return neighbours

    def euclidean_distance(self, other: Vec3) -> float:
        """
        >>> Vec3(1, 2, 3).euclidean_distance(Vec3(4, 5, 6))
        5.196152422706632
        >>> Vec3(0, 0, 0).euclidean_distance(Vec3(1, 1, 1))
        1.7320508075688772
        """
        return (
            (self.x - other.x) ** 2 + (self.y - other.y) ** 2 + (self.z - other.z) ** 2
        ) ** 0.5
