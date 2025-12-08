class DisjointSetUnion:
    """
    >>> dsu = DisjointSetUnion(5)
    >>> dsu.find(0)
    0
    >>> dsu.get_size(0)
    1
    >>> dsu.union(0, 1)
    >>> dsu.find(1)
    0
    >>> dsu.union(1, 2)
    >>> dsu.find(2)
    0
    >>> dsu.get_size(0)
    3
    """

    def __init__(self, size: int):
        self.parent = list(range(size))
        self.rank = [1] * size
        self.size = [1] * size

    def find(self, u: int) -> int:
        if self.parent[u] != u:
            self.parent[u] = self.find(self.parent[u])
        return self.parent[u]

    def union(self, u: int, v: int) -> None:
        root_u = self.find(u)
        root_v = self.find(v)

        if root_u != root_v:
            if self.rank[root_u] > self.rank[root_v]:
                self.parent[root_v] = root_u
                self.size[root_u] += self.size[root_v]
            elif self.rank[root_u] < self.rank[root_v]:
                self.parent[root_u] = root_v
                self.size[root_v] += self.size[root_u]
            else:
                self.parent[root_v] = root_u
                self.size[root_u] += self.size[root_v]
                self.rank[root_u] += 1

    def get_size(self, u: int) -> int:
        return self.size[self.find(u)]
