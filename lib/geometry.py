def cross(o, a, b):
    """(a - o) x (b - o): > 0 if o, a, b turn counter-clockwise."""
    return (a[0] - o[0]) * (b[1] - o[1]) - (a[1] - o[1]) * (b[0] - o[0])


def convex_hull(points):
    """Hull in counter-clockwise order without collinear points (monotone chain).
    Points are tuples; duplicates allowed. Fewer than 3 distinct points are returned as is."""
    pts = sorted(set(points))
    if len(pts) <= 2:
        return pts
    lower, upper = [], []
    for p in pts:
        while len(lower) >= 2 and cross(lower[-2], lower[-1], p) <= 0:
            lower.pop()
        lower.append(p)
    for p in reversed(pts):
        while len(upper) >= 2 and cross(upper[-2], upper[-1], p) <= 0:
            upper.pop()
        upper.append(p)
    return lower[:-1] + upper[:-1]


def area2(poly):
    """Twice the signed area of a polygon (positive if counter-clockwise)."""
    return sum(poly[i - 1][0] * poly[i][1] - poly[i][0] * poly[i - 1][1] for i in range(len(poly)))


def on_segment(p, a, b):
    return cross(a, b, p) == 0 and min(a[0], b[0]) <= p[0] <= max(a[0], b[0]) and min(a[1], b[1]) <= p[1] <= max(a[1], b[1])


def segments_intersect(a, b, c, d):
    """True if closed segments ab and cd share a point (exact for integer coordinates)."""
    d1, d2, d3, d4 = cross(c, d, a), cross(c, d, b), cross(a, b, c), cross(a, b, d)
    if ((d1 > 0) != (d2 > 0)) and d1 and d2 and ((d3 > 0) != (d4 > 0)) and d3 and d4:
        return True
    return on_segment(a, c, d) or on_segment(b, c, d) or on_segment(c, a, b) or on_segment(d, a, b)


def point_in_polygon(p, poly):
    """1 inside, 0 on the boundary, -1 outside (any simple polygon, integer coordinates)."""
    inside = False
    n = len(poly)
    for i in range(n):
        a, b = poly[i], poly[(i + 1) % n]
        if on_segment(p, a, b):
            return 0
        if (a[1] > p[1]) != (b[1] > p[1]):
            if (cross(a, b, p) > 0) == (b[1] > a[1]):
                inside = not inside
    return 1 if inside else -1


def hilbert_order(x, y, bits=20):
    """Indices sorting points along a Hilbert curve (x, y numpy ints in [0, 2^bits)).
    A good visiting order for local-search heuristics on points; scale with hilbert_grid first."""
    import numpy as np

    x, y = np.asarray(x, dtype=np.int64), np.asarray(y, dtype=np.int64)
    d = np.zeros(x.size, dtype=np.int64)
    s = 1 << (bits - 1)
    while s:
        rx = (x & s) > 0
        ry = (y & s) > 0
        d += s * s * ((3 * rx) ^ ry)
        flip = ~ry & rx
        x = np.where(flip, s - 1 - x, x)
        y = np.where(flip, s - 1 - y, y)
        sw = ~ry
        x, y = np.where(sw, y, x), np.where(sw, x, y)
        s >>= 1
    return np.argsort(d, kind="stable")


def hilbert_grid(x, y, bits=20):
    """Shift and scale numpy int coordinates into [0, 2^bits) for hilbert_order."""
    x = x - x.min()
    y = y - y.min()
    span = max(int(x.max()), int(y.max()), 1)
    sh = max(0, span.bit_length() - bits)
    return x >> sh, y >> sh
