def floyd_cycle(f, x0):
    """Floyd's tortoise and hare on x0, f(x0), f(f(x0)), ...
    Returns (mu, lam): the cycle starts at index mu and has length lam.
    f must not mutate its argument."""
    slow, fast = f(x0), f(f(x0))
    while slow != fast:
        slow, fast = f(slow), f(f(fast))
    mu, slow = 0, x0
    while slow != fast:
        slow, fast = f(slow), f(fast)
        mu += 1
    lam, fast = 1, f(slow)
    while slow != fast:
        fast = f(fast)
        lam += 1
    return mu, lam


def berlekamp_massey(s, mod):
    """Shortest C (C[0] = 1) with sum_j C[j] * s[i-j] = 0 (mod p) for all i >= len(C)-1,
    i.e. s[i] = -sum_{j>=1} C[j] s[i-j]. mod prime; give >= 2L terms for order L. O(n^2)."""
    C, B = [1], [1]
    L, m, b = 0, 1, 1
    for i in range(len(s)):
        d = s[i]
        for j in range(1, L + 1):
            d += C[j] * s[i - j]
        d %= mod
        if d == 0:
            m += 1
            continue
        coef = d * pow(b, mod - 2, mod) % mod
        T = C[:]
        C += [0] * (len(B) + m - len(C))
        for j, x in enumerate(B):
            C[j + m] = (C[j + m] - coef * x) % mod
        if 2 * L <= i:
            L, B, b, m = i + 1 - L, T, d, 1
        else:
            m += 1
    return C[:L + 1]


def poly_mul(a, b, mod):
    """Product of polynomials with coefficients in [0, mod), by Kronecker
    substitution (one big-int multiply, fast up to ~10^5 terms)."""
    if not a or not b:
        return []
    w = (2 * mod.bit_length() + min(len(a), len(b)).bit_length() + 7) // 8
    A = int.from_bytes(b"".join(x.to_bytes(w, "little") for x in a), "little")
    B = int.from_bytes(b"".join(x.to_bytes(w, "little") for x in b), "little")
    n = len(a) + len(b) - 1
    P = (A * B).to_bytes(n * w, "little")
    return [int.from_bytes(P[i:i + w], "little") % mod for i in range(0, n * w, w)]


def linear_rec_nth(s, C, n, mod):
    """n-th term (0-indexed) of the sequence with first terms s and recurrence C as
    returned by berlekamp_massey. Bostan-Mori: [x^n] P/Q, Q = C. O(M(L) log n)."""
    L = len(C) - 1
    if L == 0:
        return 0
    Q = [x % mod for x in C]
    P = poly_mul([x % mod for x in s[:L]], Q, mod)[:L]
    while n:
        Qm = [x if j % 2 == 0 else (mod - x) % mod for j, x in enumerate(Q)]
        P = poly_mul(P, Qm, mod)[n & 1::2]
        Q = poly_mul(Q, Qm, mod)[::2]
        n >>= 1
    return P[0] * pow(Q[0], mod - 2, mod) % mod


def div_euler(a, mod):
    """a / prod_{k>=1} (1 - x^k) mod m, first len(a) coefficients (Euler's pentagonal
    recurrence, O(n sqrt n)). Partition numbers: div_euler([1] + [0] * n, mod).
    Slow for big n (3e5 takes ~5 s): use div_euler / partitions in lib/modular.h."""
    n = len(a) - 1
    pos, neg, k = [], [], 1  # generalized pentagonal numbers by sign of their term
    while k * (3 * k - 1) // 2 <= n:
        (pos if k % 2 else neg).extend((k * (3 * k - 1) // 2, k * (3 * k + 1) // 2))
        k += 1
    h, kp, kn = [0] * (n + 1), 0, 0
    for i in range(n + 1):
        while kp < len(pos) and pos[kp] <= i:
            kp += 1
        while kn < len(neg) and neg[kn] <= i:
            kn += 1
        h[i] = (a[i] + sum([h[i - g] for g in pos[:kp]]) - sum([h[i - g] for g in neg[:kn]])) % mod
    return h
