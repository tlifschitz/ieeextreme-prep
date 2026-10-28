DIRS4 = ((0, -1), (-1, 0), (0, 1), (1, 0))  # left, up, right, down


def neighbors4(i, j, n, m):
    """In-bounds 4-neighbors of (i, j) in an n x m grid, in DIRS4 order."""
    for di, dj in DIRS4:
        a, b = i + di, j + dj
        if 0 <= a < n and 0 <= b < m:
            yield a, b


def neighbors4_wrap(i, j, n, m):
    """4-neighbors of (i, j) on a torus (edges wrap around), in DIRS4 order."""
    for di, dj in DIRS4:
        yield (i + di) % n, (j + dj) % m
