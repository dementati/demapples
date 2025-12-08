from __future__ import annotations
from dataclasses import dataclass


@dataclass(eq=True, frozen=True, slots=True)
class Range:
    start: int
    end: int

    def __len__(self) -> int:
        """
        >>> len(Range(3, 7))
        5
        >>> len(Range(1, 1))
        1
        >>> len(Range(1, 4))
        4
        >>> len(Range(6, 8))
        3
        """
        return self.end - self.start + 1

    def __contains__(self, number: int) -> bool:
        """
        >>> 5 in Range(3, 7)
        True
        >>> 3 in Range(3, 7)
        True
        >>> 7 in Range(3, 7)
        True
        >>> 2 in Range(3, 7)
        False
        >>> 8 in Range(3, 7)
        False
        """
        return self.start <= number <= self.end

    def overlaps(self, other: Range) -> bool:
        return not (self.end < other.start or other.end < self.start)

    def merge(self, other: Range) -> Range:
        return Range(start=min(self.start, other.start), end=max(self.end, other.end))

    @classmethod
    def from_str(cls, range_str: str) -> Range:
        start_str, end_str = range_str.split("-")
        return cls(start=int(start_str), end=int(end_str))
