from __future__ import annotations
from dataclasses import dataclass
from functools import cache
from itertools import product
from typing import overload


@dataclass(eq=True, frozen=True, slots=True)
class Vec2:
    x: int
    y: int

    def __iter__(self):
        """
        >>> list(Vec2(1, 2))
        [1, 2]
        """
        return iter((self.x, self.y))

    @overload
    def __add__(self, other: Vec2) -> Vec2: ...
    @overload
    def __add__(self, other: int) -> Vec2: ...
    def __add__(self, other: Vec2 | int) -> Vec2:
        if isinstance(other, Vec2):
            return Vec2(self.x + other.x, self.y + other.y)
        if isinstance(other, int):
            return Vec2(self.x + other, self.y + other)
        return NotImplemented

    @overload
    def __sub__(self, other: Vec2) -> Vec2: ...
    @overload
    def __sub__(self, other: int) -> Vec2: ...
    def __sub__(self, other: Vec2 | int) -> Vec2:
        if isinstance(other, Vec2):
            return Vec2(self.x - other.x, self.y - other.y)
        if isinstance(other, int):
            return Vec2(self.x - other, self.y - other)
        return NotImplemented

    @overload
    def __mul__(self, other: Vec2) -> Vec2: ...
    @overload
    def __mul__(self, other: int) -> Vec2: ...
    def __mul__(self, other: Vec2 | int) -> Vec2:
        if isinstance(other, Vec2):
            return Vec2(self.x * other.x, self.y * other.y)
        if isinstance(other, int):
            return Vec2(self.x * other, self.y * other)
        return NotImplemented

    @overload
    def __div__(self, other: Vec2) -> Vec2: ...
    @overload
    def __div__(self, other: int) -> Vec2: ...
    def __div__(self, other: Vec2 | int) -> Vec2:
        if isinstance(other, Vec2):
            return Vec2(self.x // other.x, self.y // other.y)
        if isinstance(other, int):
            return Vec2(self.x // other, self.y // other)
        return NotImplemented

    @overload
    def __iadd__(self, other: Vec2) -> Vec2: ...
    @overload
    def __iadd__(self, other: int) -> Vec2: ...
    def __iadd__(self, other: Vec2 | int) -> Vec2:
        if isinstance(other, Vec2):
            return Vec2(self.x + other.x, self.y + other.y)
        if isinstance(other, int):
            return Vec2(self.x + other, self.y + other)
        return NotImplemented

    @overload
    def __isub__(self, other: Vec2) -> Vec2: ...
    @overload
    def __isub__(self, other: int) -> Vec2: ...
    def __isub__(self, other: Vec2 | int) -> Vec2:
        if isinstance(other, Vec2):
            return Vec2(self.x - other.x, self.y - other.y)
        if isinstance(other, int):
            return Vec2(self.x - other, self.y - other)
        return NotImplemented

    @overload
    def __imul__(self, other: Vec2) -> Vec2: ...
    @overload
    def __imul__(self, other: int) -> Vec2: ...
    def __imul__(self, other: Vec2 | int) -> Vec2:
        if isinstance(other, Vec2):
            return Vec2(self.x * other.x, self.y * other.y)
        if isinstance(other, int):
            return Vec2(self.x * other, self.y * other)
        return NotImplemented

    @overload
    def __idiv__(self, other: Vec2) -> Vec2: ...
    @overload
    def __idiv__(self, other: int) -> Vec2: ...
    def __idiv__(self, other: Vec2 | int) -> Vec2:
        if isinstance(other, Vec2):
            return Vec2(self.x // other.x, self.y // other.y)
        if isinstance(other, int):
            return Vec2(self.x // other, self.y // other)
        return NotImplemented

    @cache
    def neighbours(self, diag: bool = True) -> set[Vec2]:
        """
        >>> Vec2(0, 0).neighbours()
        {Vec2(x=0, y=1), Vec2(x=-1, y=-1), Vec2(x=-1, y=1), Vec2(x=1, y=1), Vec2(x=1, y=-1), Vec2(x=-1, y=0), Vec2(x=1, y=0), Vec2(x=0, y=-1)}
        >>> Vec2(1, 1).neighbours()
        {Vec2(x=0, y=1), Vec2(x=1, y=2), Vec2(x=2, y=1), Vec2(x=0, y=0), Vec2(x=2, y=0), Vec2(x=0, y=2), Vec2(x=2, y=2), Vec2(x=1, y=0)}
        >>> Vec2(0, 0).neighbours(diag=False)
        {Vec2(x=-1, y=0), Vec2(x=1, y=0), Vec2(x=0, y=-1), Vec2(x=0, y=1)}
        """
        neighbours = set()
        for dx, dy in product((-1, 0, 1), repeat=2):
            if not diag and dx != 0 and dy != 0:
                continue

            if dx == 0 and dy == 0:
                continue
            neighbours.add(Vec2(self.x + dx, self.y + dy))
        return neighbours

    def manhattan_distance(self, other: Vec2) -> int:
        """
        >>> Vec2(1, 2).manhattan_distance(Vec2(4, 6))
        7
        >>> Vec2(0, 0).manhattan_distance(Vec2(3, 4))
        7
        """
        return abs(self.x - other.x) + abs(self.y - other.y)

    def euclidean_distance(self, other: Vec2) -> float:
        """
        >>> Vec2(1, 2).euclidean_distance(Vec2(4, 6))
        5.0
        >>> Vec2(0, 0).euclidean_distance(Vec2(3, 4))
        5.0
        """
        return ((self.x - other.x) ** 2 + (self.y - other.y) ** 2) ** 0.5

    def squared_distance(self, other: Vec2) -> int:
        """
        >>> Vec2(1, 2).squared_distance(Vec2(4, 6))
        25
        >>> Vec2(0, 0).squared_distance(Vec2(3, 4))
        25
        """
        return (self.x - other.x) ** 2 + (self.y - other.y) ** 2

    def bounded(self, bounds: Vec2) -> Vec2:
        """
        >>> Vec2(5, 7).bounded(Vec2(4, 6))
        Vec2(x=4, y=6)
        >>> Vec2(-1, 3).bounded(Vec2(0, 2))
        Vec2(x=0, y=2)
        """
        return Vec2(
            max(0, min(self.x, bounds.x)),
            max(0, min(self.y, bounds.y)),
        )


@dataclass(eq=True, frozen=True, slots=True)
class Vec3:
    x: int
    y: int
    z: int

    def __iter__(self):
        """
        >>> list(Vec3(1, 2, 3))
        [1, 2, 3]
        """
        return iter((self.x, self.y, self.z))

    @overload
    def __add__(self, other: Vec3) -> Vec3: ...
    @overload
    def __add__(self, other: int) -> Vec3: ...
    def __add__(self, other: Vec3 | int) -> Vec3:
        if isinstance(other, Vec3):
            return Vec3(self.x + other.x, self.y + other.y, self.z + other.z)
        if isinstance(other, int):
            return Vec3(self.x + other, self.y + other, self.z + other)
        return NotImplemented

    @overload
    def __sub__(self, other: Vec3) -> Vec3: ...
    @overload
    def __sub__(self, other: int) -> Vec3: ...
    def __sub__(self, other: Vec3 | int) -> Vec3:
        if isinstance(other, Vec3):
            return Vec3(self.x - other.x, self.y - other.y, self.z - other.z)
        if isinstance(other, int):
            return Vec3(self.x - other, self.y - other, self.z - other)
        return NotImplemented

    @overload
    def __mul__(self, other: Vec3) -> Vec3: ...
    @overload
    def __mul__(self, other: int) -> Vec3: ...
    def __mul__(self, other: Vec3 | int) -> Vec3:
        if isinstance(other, Vec3):
            return Vec3(self.x * other.x, self.y * other.y, self.z * other.z)
        if isinstance(other, int):
            return Vec3(self.x * other, self.y * other, self.z * other)
        return NotImplemented

    @overload
    def __div__(self, other: Vec3) -> Vec3: ...
    @overload
    def __div__(self, other: int) -> Vec3: ...
    def __div__(self, other: Vec3 | int) -> Vec3:
        if isinstance(other, Vec3):
            return Vec3(self.x // other.x, self.y // other.y, self.z // other.z)
        if isinstance(other, int):
            return Vec3(self.x // other, self.y // other, self.z // other)
        return NotImplemented

    @overload
    def __iadd__(self, other: Vec3) -> Vec3: ...
    @overload
    def __iadd__(self, other: int) -> Vec3: ...
    def __iadd__(self, other: Vec3 | int) -> Vec3:
        if isinstance(other, Vec3):
            return Vec3(self.x + other.x, self.y + other.y, self.z + other.z)
        if isinstance(other, int):
            return Vec3(self.x + other, self.y + other, self.z + other)
        return NotImplemented

    @overload
    def __isub__(self, other: Vec3) -> Vec3: ...
    @overload
    def __isub__(self, other: int) -> Vec3: ...
    def __isub__(self, other: Vec3 | int) -> Vec3:
        if isinstance(other, Vec3):
            return Vec3(self.x - other.x, self.y - other.y, self.z - other.z)
        if isinstance(other, int):
            return Vec3(self.x - other, self.y - other, self.z - other)
        return NotImplemented

    @overload
    def __imul__(self, other: Vec3) -> Vec3: ...
    @overload
    def __imul__(self, other: int) -> Vec3: ...
    def __imul__(self, other: Vec3 | int) -> Vec3:
        if isinstance(other, Vec3):
            return Vec3(self.x * other.x, self.y * other.y, self.z * other.z)
        if isinstance(other, int):
            return Vec3(self.x * other, self.y * other, self.z * other)
        return NotImplemented

    @overload
    def __idiv__(self, other: Vec3) -> Vec3: ...
    @overload
    def __idiv__(self, other: int) -> Vec3: ...
    def __idiv__(self, other: Vec3 | int) -> Vec3:
        if isinstance(other, Vec3):
            return Vec3(self.x // other.x, self.y // other.y, self.z // other.z)
        if isinstance(other, int):
            return Vec3(self.x // other, self.y // other, self.z // other)
        return NotImplemented

    @cache
    def neighbours(self, diag: bool = True) -> set[Vec3]:
        """
        >>> Vec3(0, 0, 0).neighbours()
        {Vec3(x=0, y=-1, z=-1), Vec3(x=-1, y=1, z=-1), Vec3(x=0, y=-1, z=1), Vec3(x=0, y=1, z=0), Vec3(x=-1, y=1, z=1), Vec3(x=1, y=-1, z=1), Vec3(x=1, y=-1, z=-1), Vec3(x=0, y=0, z=-1), Vec3(x=0, y=0, z=1), Vec3(x=1, y=0, z=1), Vec3(x=1, y=1, z=0), Vec3(x=1, y=0, z=-1), Vec3(x=-1, y=-1, z=-1), Vec3(x=0, y=-1, z=0), Vec3(x=-1, y=-1, z=1), Vec3(x=-1, y=1, z=0), Vec3(x=1, y=-1, z=0), Vec3(x=-1, y=0, z=1), Vec3(x=-1, y=0, z=-1), Vec3(x=1, y=0, z=0), Vec3(x=-1, y=-1, z=0), Vec3(x=0, y=1, z=-1), Vec3(x=0, y=1, z=1), Vec3(x=-1, y=0, z=0), Vec3(x=1, y=1, z=-1), Vec3(x=1, y=1, z=1)}
        >>> Vec3(1, 1, 1).neighbours()
        {Vec3(x=2, y=0, z=2), Vec3(x=0, y=1, z=0), Vec3(x=2, y=2, z=2), Vec3(x=2, y=1, z=0), Vec3(x=1, y=2, z=2), Vec3(x=0, y=0, z=1), Vec3(x=0, y=2, z=1), Vec3(x=1, y=0, z=1), Vec3(x=1, y=1, z=0), Vec3(x=2, y=0, z=1), Vec3(x=2, y=1, z=2), Vec3(x=2, y=2, z=1), Vec3(x=0, y=1, z=2), Vec3(x=1, y=2, z=1), Vec3(x=0, y=2, z=0), Vec3(x=0, y=0, z=0), Vec3(x=1, y=1, z=2), Vec3(x=1, y=0, z=0), Vec3(x=2, y=0, z=0), Vec3(x=2, y=2, z=0), Vec3(x=0, y=1, z=1), Vec3(x=2, y=1, z=1), Vec3(x=1, y=2, z=0), Vec3(x=0, y=0, z=2), Vec3(x=0, y=2, z=2), Vec3(x=1, y=0, z=2)}
        >>> Vec3(0, 0, 0).neighbours(diag=False)
        {Vec3(x=0, y=-1, z=-1), Vec3(x=1, y=0, z=1), Vec3(x=-1, y=0, z=1), Vec3(x=0, y=-1, z=1), Vec3(x=0, y=1, z=0), Vec3(x=-1, y=0, z=-1), Vec3(x=1, y=0, z=-1), Vec3(x=1, y=1, z=0), Vec3(x=0, y=-1, z=0), Vec3(x=1, y=0, z=0), Vec3(x=-1, y=0, z=0), Vec3(x=-1, y=1, z=0), Vec3(x=0, y=0, z=-1), Vec3(x=1, y=-1, z=0), Vec3(x=-1, y=-1, z=0), Vec3(x=0, y=0, z=1), Vec3(x=0, y=1, z=-1), Vec3(x=0, y=1, z=1)}
        """
        neighbours = set()
        for dx, dy, dz in product((-1, 0, 1), repeat=3):
            if not diag and dx != 0 and dy != 0 and dz != 0:
                continue

            if dx == 0 and dy == 0 and dz == 0:
                continue
            neighbours.add(Vec3(self.x + dx, self.y + dy, self.z + dz))
        return neighbours

    def manhattan_distance(self, other: Vec3) -> int:
        """
        >>> Vec3(1, 2, 3).manhattan_distance(Vec3(4, 5, 6))
        9
        >>> Vec3(0, 0, 0).manhattan_distance(Vec3(1, 1, 1))
        3
        """
        return abs(self.x - other.x) + abs(self.y - other.y) + abs(self.z - other.z)

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

    def squared_distance(self, other: Vec3) -> int:
        """
        >>> Vec3(1, 2, 3).squared_distance(Vec3(4, 5, 6))
        27
        >>> Vec3(0, 0, 0).squared_distance(Vec3(1, 1, 1))
        3
        """
        return (
            (self.x - other.x) ** 2 + (self.y - other.y) ** 2 + (self.z - other.z) ** 2
        )

    def bounded(self, bounds: Vec3) -> Vec3:
        """
        >>> Vec3(5, 7, 9).bounded(Vec3(4, 6, 8))
        Vec3(x=4, y=6, z=8)
        >>> Vec3(-1, 3, 5).bounded(Vec3(0, 2, 4))
        Vec3(x=0, y=2, z=4)
        """
        return Vec3(
            max(0, min(self.x, bounds.x)),
            max(0, min(self.y, bounds.y)),
            max(0, min(self.z, bounds.z)),
        )
