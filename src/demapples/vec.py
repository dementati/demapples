from __future__ import annotations
from dataclasses import dataclass


@dataclass(eq=True, frozen=True, slots=True)
class Vec3:
    x: int
    y: int
    z: int

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
