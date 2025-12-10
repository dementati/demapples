import heapq
from typing import Callable, TypeVar

T = TypeVar("T")
Number = int | float


def _reconstruct_path(came_from: dict[T, T], current: T) -> list[T]:
    """
    >>> _reconstruct_path({'B': 'A', 'C': 'B', 'D': 'C'}, 'D')
    ['A', 'B', 'C', 'D']
    """
    total_path = [current]
    while current in came_from:
        current = came_from[current]
        total_path.append(current)
    total_path.reverse()
    return total_path


def find_path(
    start: T,
    end: T,
    dist: Callable[[T, T], Number],
    get_neighbours: Callable[[T], list[T]],
    heuristic: Callable[[T], Number],
) -> tuple[Number, list[T]] | None:
    """
    >>> def dist(a: str, b: str) -> int:
    ...     return 1
    >>> def get_neighbours(s: str) -> list[str]:
    ...     neighbors = {
    ...         'A': ['B', 'C'],
    ...         'B': ['D'],
    ...         'C': ['D'],
    ...         'D': ['e'],
    ...         'e': [],
    ...     }
    ...     return neighbors.get(s, [])
    >>> def heuristic(s: str) -> int:
    ...     return 0
    >>> find_path('A', 'e', dist, get_neighbours, heuristic)
    (3, ['A', 'B', 'D', 'e'])
    """

    open_set: set[T] = {start}
    open_heap: list[tuple[Number, T]] = []
    g_score: dict[T, Number] = {start: 0}
    f_score: dict[T, Number] = {}
    came_from: dict[T, T] = {}

    def update_f_score(key: T, value: Number) -> None:
        f_score[key] = value
        heapq.heappush(open_heap, (value, key))

    update_f_score(start, heuristic(start))

    while open_set:
        _, current = heapq.heappop(open_heap)
        open_set.remove(current)

        if current == end:
            return g_score[current], _reconstruct_path(came_from, current)

        for neighbor in get_neighbours(current):
            tentative_g = g_score[current] + dist(current, neighbor)
            if neighbor not in g_score or tentative_g < g_score[neighbor]:
                g_score[neighbor] = tentative_g
                update_f_score(neighbor, tentative_g + heuristic(neighbor))
                came_from[neighbor] = current
                open_set.add(neighbor)

    raise AssertionError("No path")
