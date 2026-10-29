class DSU:
    """Disjoint sets on 0..n-1: union by size, path halving.
    Next free slot >= x: when x is used set parent[x] = x + 1 (n + 1 slots), then find(x)."""

    def __init__(self, n):
        self.parent = list(range(n))
        self.size = [1] * n
        self.count = n  # number of sets

    def find(self, x):
        parent = self.parent
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x

    def union(self, a, b):
        """Merge the sets of a and b; False if they were already together."""
        a, b = self.find(a), self.find(b)
        if a == b:
            return False
        if self.size[a] < self.size[b]:
            a, b = b, a
        self.parent[b] = a
        self.size[a] += self.size[b]
        self.count -= 1
        return True


class PotentialDSU:
    """Disjoint sets with a potential per element in an abelian group (op, inv, e):
    pot[x] is x relative to its root. union(a, b, d) records a = d (op) b.
    E.g. xor parity: op=xor, inv=identity, e=0; ratios mod p: op=mul, inv=pow(x, -1, p), e=1."""

    def __init__(self, n, op, inv, e):
        self.parent = list(range(n))
        self.size = [1] * n
        self.pot = [e] * n
        self.op, self.inv = op, inv

    def find(self, x):
        parent, pot, op = self.parent, self.pot, self.op
        path = []
        while parent[x] != x:
            path.append(x)
            x = parent[x]
        for y in reversed(path):  # closest to the root first
            p = parent[y]
            if p != x:
                pot[y] = op(pot[y], pot[p])
            parent[y] = x
        return x

    def union(self, a, b, d):
        """Record a = d op b. False if already together (then check with diff)."""
        ra, rb = self.find(a), self.find(b)
        if ra == rb:
            return False
        pot, op, inv = self.pot, self.op, self.inv
        if self.size[ra] < self.size[rb]:
            a, b, ra, rb, d = b, a, rb, ra, inv(d)
        # a = pa ra, b = pb rb, a = d b  =>  rb = pa / (d pb) ra
        pot[rb] = op(pot[a], inv(op(d, pot[b])))
        self.parent[rb] = ra
        self.size[ra] += self.size[rb]
        return True

    def diff(self, a, b):
        """d with a = d op b, or None if not connected."""
        if self.find(a) != self.find(b):
            return None
        return self.op(self.pot[a], self.inv(self.pot[b]))


class Fenwick:
    """Point add, prefix sum on 0..n-1."""

    def __init__(self, n):
        self.n = n
        self.t = [0] * (n + 1)

    def add(self, i, v):
        i += 1
        while i <= self.n:
            self.t[i] += v
            i += i & -i

    def prefix(self, i):
        """Sum of a[0..i-1]."""
        s = 0
        while i > 0:
            s += self.t[i]
            i -= i & -i
        return s

    def range_sum(self, l, r):
        """Sum of a[l..r-1]."""
        return self.prefix(r) - self.prefix(l)

    def lower_bound(self, k):
        """Smallest i with prefix(i + 1) >= k, n if none (a >= 0). On value counts:
        the k-th smallest (k >= 1)."""
        t, n, pos = self.t, self.n, 0
        step = 1 << n.bit_length()
        while step:
            if pos + step <= n and t[pos + step] < k:
                pos += step
                k -= t[pos]
            step >>= 1
        return pos


class SegTree:
    """Iterative segment tree: point set, fold of op over a[l..r-1].
    op must be associative with identity e (e.g. min / inf, max / -inf, add / 0)."""

    def __init__(self, a, op, e):
        self.n = n = len(a)
        self.op, self.e = op, e
        self.t = [e] * n + list(a)
        for i in range(n - 1, 0, -1):
            self.t[i] = op(self.t[2 * i], self.t[2 * i + 1])

    def set(self, i, v):
        t, op = self.t, self.op
        i += self.n
        t[i] = v
        while i > 1:
            i >>= 1
            t[i] = op(t[2 * i], t[2 * i + 1])

    def get(self, i):
        return self.t[i + self.n]

    def query(self, l, r):
        """op(a[l], ..., a[r-1]); e if l >= r. Keeps the left-to-right order."""
        t, op = self.t, self.op
        left = right = self.e
        l += self.n
        r += self.n
        while l < r:
            if l & 1:
                left = op(left, t[l])
                l += 1
            if r & 1:
                r -= 1
                right = op(t[r], right)
            l >>= 1
            r >>= 1
        return op(left, right)


class SparseTable:
    """Static range fold in O(1) for idempotent op (min, max, gcd) over a[l..r-1], l < r."""

    def __init__(self, a, op=min):
        self.op = op
        self.t = [list(a)]
        j = 1
        while 2 * j <= len(a):
            prev = self.t[-1]
            self.t.append(list(map(op, prev[: len(prev) - j], prev[j:])))
            j *= 2

    def query(self, l, r):
        k = (r - l).bit_length() - 1
        row = self.t[k]
        return self.op(row[l], row[r - (1 << k)])
