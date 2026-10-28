def caesar_shift(text, k):
    """Shift letters by k (any sign), keeping case; other chars unchanged."""
    res = []
    for ch in text:
        if "a" <= ch <= "z":
            res.append(chr((ord(ch) - 97 + k) % 26 + 97))
        elif "A" <= ch <= "Z":
            res.append(chr((ord(ch) - 65 + k) % 26 + 65))
        else:
            res.append(ch)
    return "".join(res)


def prefix_function(s):
    """pi[i] = length of the longest proper border of s[:i+1] (KMP)."""
    pi = [0] * len(s)
    k = 0
    for i in range(1, len(s)):
        while k and s[i] != s[k]:
            k = pi[k - 1]
        if s[i] == s[k]:
            k += 1
        pi[i] = k
    return pi


def find_all(text, pat):
    """Start indices of every (overlapping) occurrence of pat in text, O(n + m)."""
    if not pat:
        return list(range(len(text) + 1))
    pi = prefix_function(pat)
    res, k = [], 0
    for i, ch in enumerate(text):
        while k and ch != pat[k]:
            k = pi[k - 1]
        if ch == pat[k]:
            k += 1
        if k == len(pat):
            res.append(i - k + 1)
            k = pi[k - 1]
    return res


def z_function(s):
    """z[i] = length of the longest common prefix of s and s[i:] (z[0] = len(s))."""
    n = len(s)
    z = [0] * n
    if n:
        z[0] = n
    l = r = 0
    for i in range(1, n):
        if i < r:
            z[i] = min(r - i, z[i - l])
        while i + z[i] < n and s[z[i]] == s[i + z[i]]:
            z[i] += 1
        if i + z[i] > r:
            l, r = i, i + z[i]
    return z


HASH_MOD = (1 << 61) - 1
HASH_BASE = 911382323  # fixed: a random base would be safer against anti-hash tests


class Hash:
    """Polynomial prefix hashes mod 2^61-1: get(l, r) hashes s[l:r] in O(1).
    s may be a str or a list of ints (values < HASH_MOD)."""

    def __init__(self, s):
        n = len(s)
        h, p = [0] * (n + 1), [1] * (n + 1)
        M, B = HASH_MOD, HASH_BASE
        vals = map(ord, s) if isinstance(s, str) else s
        for i, c in enumerate(vals):
            h[i + 1] = (h[i] * B + c) % M
            p[i + 1] = p[i] * B % M
        self.h, self.p = h, p

    def get(self, l, r):
        return (self.h[r] - self.h[l] * self.p[r - l]) % HASH_MOD


def aho_corasick(pats, alpha=26, base=97):
    """Aho-Corasick over patterns (str, bytes or int lists; symbols base..base+alpha-1).
    Returns (go, fail, cnt), root 0: go[s][c] full transition table (c = symbol - base),
    fail[s] suffix link, cnt[s] = number of patterns ending at s or at a suffix of it.
    Matches in text: s = 0; for c in text: s = go[s][c - base]; total += cnt[s].
    Also a DP automaton: states = len(go). O(alpha * total length)."""
    go, cnt = [[-1] * alpha], [0]
    for p in pats:
        s = 0
        for c in p.encode() if isinstance(p, str) else p:
            c -= base
            if go[s][c] < 0:
                go[s][c] = len(go)
                go.append([-1] * alpha)
                cnt.append(0)
            s = go[s][c]
        cnt[s] += 1
    fail = [0] * len(go)
    order = []
    for c in range(alpha):
        if go[0][c] < 0:
            go[0][c] = 0
        else:
            order.append(go[0][c])
    for s in order:  # BFS: order grows while iterating
        f = fail[s]
        cnt[s] += cnt[f]
        gs, gf = go[s], go[f]
        for c in range(alpha):
            t = gs[c]
            if t < 0:
                gs[c] = gf[c]
            else:
                fail[t] = gf[c]
                order.append(t)
    return go, fail, cnt


def manacher(s):
    """Palindrome radii, O(n). Returns p of length 2n+1 over t = '#s0#s1#...#':
    odd i is centred on s[i//2], even i on the gap before s[i//2]; the longest
    palindrome there is s[(i - p[i])//2 : (i + p[i])//2], of length p[i].
    s: str or list."""
    n = len(s)
    t = [object()] * (2 * n + 3)  # separators; distinct objects as sentinels at both ends
    t[0], t[-1] = object(), object()
    t[2:2 * n + 1:2] = s
    p = [0] * (2 * n + 3)
    c2 = r = 0  # c2 = 2 * centre of the palindrome reaching furthest right, r = its end
    for i in range(1, 2 * n + 2):
        k = 0
        if i < r:
            k = p[c2 - i]
            if k < r - i:
                p[i] = k
                continue
            k = r - i
        a, b = i - k - 1, i + k + 1
        while t[a] == t[b]:
            a -= 1
            b += 1
        p[i] = b - i - 1
        if b - 1 > r:
            c2, r = 2 * i, b - 1
    return p[1:-1]


def lyndon_factorization(s):
    """Duval, O(n): starts b of the Lyndon factors s = w0 w1 ... (w0 >= w1 >= ...),
    with b[-1] = n so factor j is s[b[j]:b[j+1]]. s: str or list."""
    n, i, b = len(s), 0, [0]
    while i < n:
        j, k = i + 1, i
        while j < n and s[k] <= s[j]:
            k = i if s[k] < s[j] else k + 1
            j += 1
        while i <= k:
            i += j - k
            b.append(i)
    return b


def min_rotation(s):
    """Smallest i such that s[i:] + s[:i] is the least rotation of s, O(n) (Duval on s+s).
    s is a necklace (minimal among its rotations) iff min_rotation(s) == 0."""
    n = len(s)
    s = s + s
    i = ans = 0
    while i < n:
        ans, j, k = i, i + 1, i
        while j < 2 * n and s[k] <= s[j]:
            k = i if s[k] < s[j] else k + 1
            j += 1
        while i <= k:
            i += j - k
    return ans


def suffix_array(s):
    """(sa, lcp) of s (str or list): sorted suffix starts, O(n log^2 n) doubling;
    lcp[i] = LCP of s[sa[i]:] and s[sa[i+1]:] (Kasai)."""
    n, k, h = len(s), 1, 0
    d = {c: i for i, c in enumerate(sorted(set(s)))}
    r = [d[c] for c in s]
    while len(d) < n:
        key = [a * (n + 1) + b for a, b in zip(r, r[k:] + [-1] * k)]
        d = {v: i for i, v in enumerate(sorted(set(key)))}
        r = [d[v] for v in key]
        k *= 2
    sa = sorted(range(n), key=r.__getitem__)
    lcp = [0] * max(n - 1, 0)
    for i in range(n):
        if r[i] < n - 1:
            j = sa[r[i] + 1]
            while max(i, j) + h < n and s[i + h] == s[j + h]:
                h += 1
            lcp[r[i]] = h
            h -= h > 0
        else:
            h = 0
    return sa, lcp
