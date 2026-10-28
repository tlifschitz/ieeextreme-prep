from array import array
from bisect import bisect_right


def knapsack01(items, cap):
    """0/1 knapsack over (weight, value) items. dp[c] = best value with
    total weight <= c."""
    dp = [0] * (cap + 1)
    for w, v in items:
        for c in range(cap, w - 1, -1):
            if dp[c - w] + v > dp[c]:
                dp[c] = dp[c - w] + v
    return dp


def sos_subsets(f, m):
    """f[S] = sum of f[T] over T subset of S (len(f) == 1 << m). Results must
    fit in 16 bits: f is packed into one big int, 16 bits per entry."""
    n = 1 << m
    F = int.from_bytes(array("H", f).tobytes(), "little")
    for i in range(m):
        h = 1 << i
        low = int.from_bytes((b"\xff\xff" * h + b"\0\0" * h) * (n >> i + 1), "little")
        F += (F & low) << 16 * h
    out = array("H")
    out.frombytes(F.to_bytes(2 * n, "little"))
    return out


def lis(a, strict=True):
    """Indices of one longest increasing subsequence of a (non-decreasing if
    strict=False). O(n log n)."""
    from bisect import bisect_left, bisect_right
    find = bisect_left if strict else bisect_right
    tails, idx, prev = [], [], [-1] * len(a)
    for i, x in enumerate(a):
        k = find(tails, x)
        if k == len(tails):
            tails.append(x)
            idx.append(i)
        else:
            tails[k] = x
            idx[k] = i
        prev[i] = idx[k - 1] if k else -1
    out, i = [], idx[-1] if idx else -1
    while i != -1:
        out.append(i)
        i = prev[i]
    return out[::-1]


def nearest_smaller(a, strict=True):
    """Monotonic stack. left[i] = last j < i with a[j] < a[i], else -1;
    right[i] = first j > i with a[j] < a[i], else n. strict=False uses <=.
    For greater, pass the negated values."""
    n = len(a)
    left, right = [-1] * n, [n] * n
    for out, order in ((left, range(n)), (right, range(n - 1, -1, -1))):
        st = []
        for i in order:
            x = a[i]
            if strict:
                while st and a[st[-1]] >= x:
                    st.pop()
            else:
                while st and a[st[-1]] > x:
                    st.pop()
            if st:
                out[i] = st[-1]
            st.append(i)
    return left, right


def window_min(a, k):
    """Minimum of every window a[i:i+k] (n-k+1 values). For max, negate."""
    from collections import deque
    q, out = deque(), []
    for i, x in enumerate(a):
        while q and a[q[-1]] >= x:
            q.pop()
        q.append(i)
        if q[0] <= i - k:
            q.popleft()
        if i >= k - 1:
            out.append(a[q[0]])
    return out


class MinQueue:
    """FIFO queue with O(1) amortized min (monotonic deque): push(x),
    pop() removes the oldest element, min(). For max, push negated values."""

    def __init__(self):
        from collections import deque
        self.q, self.d = deque(), deque()

    def push(self, x):
        self.q.append(x)
        while self.d and self.d[-1] > x:
            self.d.pop()
        self.d.append(x)

    def pop(self):
        x = self.q.popleft()
        if self.d[0] == x:
            self.d.popleft()
        return x

    def min(self):
        return self.d[0]

    def __len__(self):
        return len(self.q)


class LiChao:
    """Convex hull trick: add lines y = a*x + b, query the minimum at x.
    xs: every x that will be queried (any order, duplicates ok).
    O(log n) per operation. For maximum, add (-a, -b) and negate the result."""

    def __init__(self, xs):
        self.xs = sorted(set(xs))
        self.pos = {x: i for i, x in enumerate(self.xs)}
        self.size = 1
        while self.size < len(self.xs):
            self.size *= 2
        self.xs += [self.xs[-1]] * (self.size - len(self.xs))
        self.A = [0] * (2 * self.size)
        self.B = [float("inf")] * (2 * self.size)

    def add(self, a, b):
        xs, A, B = self.xs, self.A, self.B
        node, lo, hi = 1, 0, self.size
        while True:
            mid = (lo + hi) // 2
            xm = xs[mid]
            if a * xm + b < A[node] * xm + B[node]:
                A[node], a = a, A[node]
                B[node], b = b, B[node]
            if hi - lo == 1 or b == float("inf"):
                return
            xl = xs[lo]
            if a * xl + b < A[node] * xl + B[node]:
                node, hi = 2 * node, mid
            else:
                node, lo = 2 * node + 1, mid

    def query(self, x):
        k = self.pos[x] + self.size
        A, B = self.A, self.B
        best = A[k] * x + B[k]
        k >>= 1
        while k:
            v = A[k] * x + B[k]
            if v < best:
                best = v
            k >>= 1
        return best


class MonoHull:
    """Min of lines y = a*x + b added with non-increasing a; query(x) at an
    integer x by binary search, O(log n). Increasing a: add (-a, b), query -x.
    Max: add (-a, -b), negate. Exact (floor division). Hot loops: inline it,
    the method calls cost ~30%."""

    def __init__(self):
        self.A, self.B, self.T = [], [], []  # line k is the min on [T[k], T[k+1])

    def add(self, a, b):
        A, B, T = self.A, self.B, self.T
        if A and A[-1] == a:
            if b >= B[-1]:
                return
            A.pop(); B.pop(); T.pop()
        t = -(1 << 200)
        while A:
            t = -((B[-1] - b) // (A[-1] - a))  # first x where the new line is <=
            if t > T[-1]:
                break
            A.pop(); B.pop(); T.pop()
        A.append(a); B.append(b); T.append(t)

    def query(self, x):
        k = bisect_right(self.T, x) - 1
        return self.A[k] * x + self.B[k]


def slope_trick(a):
    """Min sum |a_i - b_i| over non-decreasing b, and one such b. O(n log n).
    Strictly increasing b: pass a_i - i, add i back to b."""
    from heapq import heappush, heapreplace
    h, b, cost = [], [], 0
    for x in a:
        heappush(h, -x)
        if -h[0] > x:
            cost += -h[0] - x
            heapreplace(h, -x)
        b.append(-h[0])
    for i in range(len(b) - 2, -1, -1):
        b[i] = min(b[i], b[i + 1])
    return cost, b


def bit_count(lims, ok, bits=61):
    """Tuples 0 <= x_i <= lims[i] with ok(b, m) at every bit b (bit i of m = bit b
    of x_i). Digit DP over tight masks, O(bits * 4^k)."""
    s = 1 << len(lims)
    dp = [0] * s
    dp[-1] = 1
    for b in range(bits - 1, -1, -1):
        L = sum((x >> b & 1) << i for i, x in enumerate(lims))
        nd = [0] * s
        for t in range(s):
            if dp[t]:
                for m in range(s):
                    if not m & t & ~L and ok(b, m):
                        nd[t & ~(L & ~m)] += dp[t]
        dp = nd
    return sum(dp)
