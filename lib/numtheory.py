from math import gcd


def sieve(n):
    """is_prime as a bytearray for 0..n."""
    s = bytearray([1]) * (n + 1)
    s[0:2] = b"\0\0"[: min(2, n + 1)]
    for i in range(2, int(n**0.5) + 1):
        if s[i]:
            s[i * i :: i] = bytes(len(range(i * i, n + 1, i)))
    return s


def primes_upto(n):
    return [i for i, f in enumerate(sieve(n)) if f]


def multiple_sums(c, primes=None):
    """In place on a numpy int array: c[d] = sum of c[d t] over t >= 1 (c[0] untouched).
    primes: up to len(c) - 1. O(M log log M) vectorized."""
    M = len(c) - 1
    for p in primes_upto(M) if primes is None else primes:
        hi = M // p
        while hi:  # d in (lo, hi] reads d p > hi, already final
            lo = hi // p
            c[lo + 1 : hi + 1] += c[(lo + 1) * p : hi * p + 1 : p]
            hi = lo


def multiple_mobius(f, primes=None):
    """Inverse of multiple_sums, in place: f[d] = sum of mu(t) f[d t]
    (e.g. count with gcd exactly d from counts with gcd divisible by d)."""
    M = len(f) - 1
    for p in primes_upto(M) if primes is None else primes:
        f[1 : M // p + 1] -= f[p::p]


def spf_sieve(n):
    """Smallest prime factor of every 0..n (spf[0] = 0, spf[1] = 1)."""
    spf = list(range(n + 1))
    for i in range(2, int(n**0.5) + 1):
        if spf[i] == i:
            for j in range(i * i, n + 1, i):
                if spf[j] == j:
                    spf[j] = i
    return spf


def is_prime(n):
    """Deterministic Miller-Rabin for n < 3.3e24 (all 64-bit n)."""
    if n < 2:
        return False
    small = (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41)
    for p in small:
        if n % p == 0:
            return n == p
    d, s = n - 1, 0
    while d % 2 == 0:
        d //= 2
        s += 1
    for a in small:
        x = pow(a, d, n)
        if x in (1, n - 1):
            continue
        for _ in range(s - 1):
            x = x * x % n
            if x == n - 1:
                break
        else:
            return False
    return True


def factorize(n):
    """{prime: exponent} of n >= 1 by trial division, O(sqrt n)."""
    f = {}
    d = 2
    while d * d <= n:
        while n % d == 0:
            f[d] = f.get(d, 0) + 1
            n //= d
        d += 1 if d == 2 else 2
    if n > 1:
        f[n] = f.get(n, 0) + 1
    return f


def ext_gcd(a, b):
    """(g, x, y) with a x + b y = g = gcd(a, b)."""
    x0, y0, x1, y1 = 1, 0, 0, 1
    while b:
        q = a // b
        a, b = b, a - q * b
        x0, x1 = x1, x0 - q * x1
        y0, y1 = y1, y0 - q * y1
    return a, x0, y0


def crt(r1, m1, r2, m2):
    """x with x = r1 (mod m1) and x = r2 (mod m2), as (x, lcm); None if impossible.
    Moduli need not be coprime."""
    g, p, _ = ext_gcd(m1, m2)
    if (r2 - r1) % g:
        return None
    l = m1 // g * m2
    return (r1 + (r2 - r1) // g * p % (m2 // g) * m1) % l, l


def mat_mul(A, B, mod):
    Bt = list(zip(*B))
    return [[sum(a * b for a, b in zip(row, col)) % mod for col in Bt] for row in A]


def mat_pow(A, e, mod):
    """A^e mod mod for a square matrix (list of lists), O(n^3 log e)."""
    n = len(A)
    R = [[int(i == j) % mod for j in range(n)] for i in range(n)]
    while e:
        if e & 1:
            R = mat_mul(R, A, mod)
        A = mat_mul(A, A, mod)
        e >>= 1
    return R


class XorBasis:
    """Linear basis of non-negative ints over GF(2); b[i] is the vector with highest bit i."""

    def __init__(self, bits=64):
        self.b = [0] * bits
        self.rank = 0

    def insert(self, x):
        """Add x; False if it was already in the span."""
        b = self.b
        while x:
            i = x.bit_length() - 1
            if not b[i]:
                b[i] = x
                self.rank += 1
                return True
            x ^= b[i]
        return False

    def reduce(self, x):
        """Smallest value of x xor (any span element); 0 iff x is in the span."""
        for i in range(len(self.b) - 1, -1, -1):
            if self.b[i] and x >> i & 1:
                x ^= self.b[i]
        return x

    def max_xor(self, x=0):
        for i in range(len(self.b) - 1, -1, -1):
            if self.b[i] and not x >> i & 1:
                x ^= self.b[i]
        return x

    def span(self):
        """Every element of the span (2^rank values; keep rank small)."""
        vals = [0]
        for v in self.b:
            if v:
                vals += [u ^ v for u in vals]
        return vals


def gauss(M, m, p):
    """Gauss-Jordan mod prime p on rows M in place, pivots in columns < m. Returns (rank,
    det of M[:, :m] if square, x with M[:, :m] x = M[:, m] or None). O(n^2 len(M[0]))."""
    n, r, d, piv = len(M), 0, 1, []
    for c in range(m):
        k = next((i for i in range(r, n) if M[i][c] % p), -1)
        if k < 0:
            continue
        M[r], M[k] = M[k], M[r]
        v = M[r][c]
        d *= v if k == r else -v
        iv = pow(v, p - 2, p)
        M[r] = R = [w * iv % p for w in M[r]]
        for i in range(n):
            f = M[i][c]
            if i != r and f % p:
                M[i] = [(a - f * b) % p for a, b in zip(M[i], R)]
        piv.append(c)
        r += 1
    x = [0] * m
    for i, c in enumerate(piv):
        x[c] = M[i][m]
    return r, d * (r == m) % p, None if any(M[i][m] % p for i in range(r, n)) else x
