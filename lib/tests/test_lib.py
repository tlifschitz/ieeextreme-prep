"""Randomized tests of lib/ against brute force. Run: python3 lib/tests/test_lib.py"""
import itertools
import math
import random
import sys
from pathlib import Path

import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))

from lib import combinatorics  # noqa: E402
from lib.combinatorics import C, P, init, inv  # noqa: E402
from lib.dp import LiChao, MinQueue, knapsack01, lis, nearest_smaller, sos_subsets, window_min  # noqa: E402
from lib.npgraphs import components_np  # noqa: E402
from lib.ds import DSU, Fenwick, PotentialDSU, SegTree, SparseTable  # noqa: E402
from lib.fft import conv_mod  # noqa: E402
from lib.graphs import (  # noqa: E402
    LCA, MaxFlow, bfs, bipartite_matching, bridges, dijkstra, subtree_sizes, topo_sort_min, tree_depths,
    tree_orders,
)
from lib.grid import neighbors4, neighbors4_wrap  # noqa: E402
from lib.sequences import floyd_cycle  # noqa: E402
from lib.strings import Hash, caesar_shift, find_all, prefix_function, z_function  # noqa: E402
from lib.numtheory import XorBasis, crt, ext_gcd, factorize, is_prime, mat_pow, primes_upto, sieve, spf_sieve  # noqa: E402
from lib.geometry import hilbert_grid, hilbert_order, area2, convex_hull, cross, point_in_polygon, segments_intersect  # noqa: E402
from fractions import Fraction  # noqa: E402
from lib.sequences import berlekamp_massey, div_euler, linear_rec_nth, poly_mul  # noqa: E402
from lib.strings import aho_corasick, lyndon_factorization, manacher, min_rotation  # noqa: E402
from lib.graphs import biconnected_blocks, block_cut_tree, kruskal_reconstruction, subtree_ids  # noqa: E402
from lib.npgraphs import floyd  # noqa: E402
from lib.numtheory import multiple_mobius, multiple_sums, primes_upto  # noqa: E402
from lib.dp import MonoHull  # noqa: E402
from lib.graphs import scc, two_sat  # noqa: E402
from lib.strings import suffix_array  # noqa: E402
from lib.numtheory import gauss  # noqa: E402
from lib.dp import bit_count, slope_trick  # noqa: E402
from lib.ds import Fenwick  # noqa: E402

R = random.Random(12345)
ITER = 300


def test_caesar_shift():
    for _ in range(ITER):
        s = "".join(R.choice("abcxyzABCXYZ 09,.!é") for _ in range(R.randint(0, 20)))
        k = R.randint(-60, 60)
        out = caesar_shift(s, k)
        assert caesar_shift(out, -k) == s
        for a, b in zip(s, out):
            if a.isascii() and a.isalpha():
                base = ord("a") if a.islower() else ord("A")
                assert ord(b) - base == (ord(a) - base + k) % 26
            else:
                assert a == b


def test_neighbors():
    for _ in range(ITER):
        n, m = R.randint(1, 5), R.randint(1, 5)
        i, j = R.randrange(n), R.randrange(m)
        exp = [(i + a, j + b) for a, b in ((0, -1), (-1, 0), (0, 1), (1, 0)) if 0 <= i + a < n and 0 <= j + b < m]
        assert list(neighbors4(i, j, n, m)) == exp
        wrap = list(neighbors4_wrap(i, j, n, m))
        assert len(wrap) == 4 and all(0 <= a < n and 0 <= b < m for a, b in wrap)
        assert all(abs(a - i) in (0, 1, n - 1) and abs(b - j) in (0, 1, m - 1) for a, b in wrap)


def test_topo_sort_min():
    for _ in range(ITER):
        n = R.randint(1, 6)
        edges = {(a, b) for a in range(n) for b in range(n) if a != b and R.random() < 0.25}
        adj = [[b for (a, b) in sorted(edges) if a == v] for v in range(n)]
        key = [R.randint(0, 2) for _ in range(n)]
        valid = [p for p in itertools.permutations(range(n)) if all(p.index(a) < p.index(b) for a, b in edges)]
        got = topo_sort_min(n, adj, key)
        if not valid:
            assert got is None
            continue
        # Greedy minimum: at each step the smallest available (key, v).
        assert got in [list(p) for p in valid]
        indeg = [sum(1 for a, b in edges if b == v) for v in range(n)]
        done = set()
        for v in got:
            avail = [u for u in range(n) if u not in done and indeg[u] == 0]
            assert (key[v], v) == min((key[u], u) for u in avail)
            done.add(v)
            for a, b in edges:
                if a == v:
                    indeg[b] -= 1


def random_tree(n):
    adj = [[] for _ in range(n)]
    for v in range(1, n):
        p = R.randrange(v)
        adj[p].append(v)
        adj[v].append(p)
    for lst in adj:
        R.shuffle(lst)
    return adj


def test_tree_orders_and_sizes():
    for _ in range(ITER):
        n = R.randint(1, 12)
        adj, root = random_tree(n), R.randrange(n)
        pre, post, par, size = [], [], [-1] * n, [0] * n

        def dfs(v, p):
            pre.append(v)
            par[v] = p
            size[v] = 1
            for u in adj[v]:
                if u != p:
                    dfs(u, v)
                    size[v] += size[u]
            post.append(v)

        dfs(root, -1)
        parent, gpre, gpost = tree_orders(adj, root)
        assert (parent, gpre, gpost) == (par, pre, post)
        assert subtree_sizes(parent, gpost) == size


def test_knapsack01():
    for _ in range(ITER):
        items = [(R.randint(0, 8), R.randint(0, 20)) for _ in range(R.randint(0, 7))]
        cap = R.randint(0, 25)
        dp = knapsack01(items, cap)
        for c in range(cap + 1):
            best = max(
                sum(v for (w, v), t in zip(items, take) if t)
                for take in itertools.product((0, 1), repeat=len(items))
                if sum(w for (w, _), t in zip(items, take) if t) <= c
            )
            assert dp[c] == best


def test_floyd_cycle():
    for _ in range(ITER):
        n = R.randint(1, 15)
        f_table = [R.randrange(n) for _ in range(n)]
        x0 = R.randrange(n)
        first, x, i = {}, x0, 0
        while x not in first:
            first[x] = i
            x, i = f_table[x], i + 1
        assert floyd_cycle(f_table.__getitem__, x0) == (first[x], i - first[x])


def test_combinatorics():
    for mod in (13, 998244353, 10**9 + 7):
        n_max = min(mod - 1, 60)
        init(n_max, mod)
        assert combinatorics.MOD == mod
        for n in range(n_max + 1):
            for k in range(-2, n + 3):
                ok = 0 <= k <= n
                assert C(n, k) == (math.comb(n, k) % mod if ok else 0)
                assert P(n, k) == (math.perm(n, k) % mod if ok else 0)
    for _ in range(ITER):
        mod = R.randint(2, 10**9)
        a = R.randint(1, 10**12)
        if math.gcd(a, mod) == 1:
            assert a * inv(a, mod) % mod == 1 % mod


def test_sos_subsets():
    for _ in range(ITER // 3):
        m = R.randint(0, 6)
        f = [R.randint(0, 900) for _ in range(1 << m)]
        exp = [sum(f[t] for t in range(1 << m) if t & s == t) for s in range(1 << m)]
        assert list(sos_subsets(f, m)) == exp


def test_conv_mod():
    for _ in range(ITER // 3):
        mod = R.choice([2, 998244353, 10**9 + 7, 10**9 + 99999, R.randint(2, 2**30 - 1)])
        a = [R.randrange(mod) for _ in range(R.randint(1, 40))]
        b = [R.randrange(mod) for _ in range(R.randint(1, 40))]
        exp = [0] * (len(a) + len(b) - 1)
        for i, x in enumerate(a):
            for j, y in enumerate(b):
                exp[i + j] = (exp[i + j] + x * y) % mod
        assert conv_mod(a, b, mod).tolist() == exp
    # long inputs near the limit, checked at a random point
    mod, n = 10**9 + 7, 200000
    a = [R.randrange(mod) for _ in range(n)]
    b = [R.randrange(mod) for _ in range(n)]
    x = R.randrange(mod)
    ev = lambda p: sum(c * pow(x, i, mod) for i, c in enumerate(p)) % mod  # noqa: E731
    assert ev(conv_mod(a, b, mod).tolist()) == ev(a) * ev(b) % mod


def test_ds():
    for _ in range(ITER):
        n = R.randint(1, 25)
        d, comp = DSU(n), list(range(n))
        for _ in range(30):
            a, b = R.randrange(n), R.randrange(n)
            merged = comp[a] != comp[b]
            assert d.union(a, b) == merged
            if merged:
                old = comp[b]
                comp = [comp[a] if c == old else c for c in comp]
            x, y = R.randrange(n), R.randrange(n)
            assert (d.find(x) == d.find(y)) == (comp[x] == comp[y])
            assert d.size[d.find(x)] == comp.count(comp[x]) and d.count == len(set(comp))
        a = [R.randint(-50, 50) for _ in range(n)]
        f, st = Fenwick(n), SegTree(a, min, float("inf"))
        cat = SegTree([str(x) for x in a], lambda x, y: x + y, "")  # non-commutative
        for i, x in enumerate(a):
            f.add(i, x)
        for _ in range(30):
            i, v = R.randrange(n), R.randint(-50, 50)
            f.add(i, v - a[i])
            st.set(i, v)
            cat.set(i, str(v))
            a[i] = v
            l = R.randrange(n + 1)
            r = R.randint(l, n)
            assert f.range_sum(l, r) == sum(a[l:r])
            assert st.query(l, r) == min(a[l:r], default=float("inf"))
            assert cat.query(l, r) == "".join(map(str, a[l:r]))
        sp = SparseTable(a, max)
        for l in range(n):
            for r in range(l + 1, n + 1):
                assert sp.query(l, r) == max(a[l:r])


def test_potential_dsu():
    mod = 998244353
    for _ in range(ITER):
        n = R.randint(1, 12)
        hidden = [R.randint(1, mod - 1) for _ in range(n)]  # a consistent assignment
        d = PotentialDSU(n, lambda x, y: x * y % mod, lambda x: pow(x, -1, mod), 1)
        comp = list(range(n))
        for _ in range(20):
            a, b = R.randrange(n), R.randrange(n)
            r = hidden[a] * pow(hidden[b], -1, mod) % mod
            assert d.union(a, b, r) == (comp[a] != comp[b])
            old = comp[b]
            comp = [comp[a] if c == old else c for c in comp]
            x, y = R.randrange(n), R.randrange(n)
            exp = hidden[x] * pow(hidden[y], -1, mod) % mod if comp[x] == comp[y] else None
            assert d.diff(x, y) == exp
        par = [R.randint(0, 1) for _ in range(n)]
        d = PotentialDSU(n, lambda x, y: x ^ y, lambda x: x, 0)
        for _ in range(20):
            a, b = R.randrange(n), R.randrange(n)
            d.union(a, b, par[a] ^ par[b])
            assert d.diff(a, b) == par[a] ^ par[b]


def test_bridges():
    for _ in range(ITER):
        n = R.randint(1, 9)
        m = R.randint(0, 12)
        us = [R.randrange(n) for _ in range(m)]
        vs = [R.randrange(n) for _ in range(m)]

        def comps(skip):
            dd = DSU(n)
            for e in range(m):
                if e != skip:
                    dd.union(us[e], vs[e])
            return dd.count

        base = comps(-1)
        assert sorted(bridges(n, us, vs)) == [e for e in range(m) if comps(e) > base]


def min_cut_brute(n, edges, s, t):
    best = float("inf")
    for mask in range(1 << n):
        if mask >> s & 1 and not mask >> t & 1:
            best = min(best, sum(c for u, v, c in edges if mask >> u & 1 and not mask >> v & 1))
    return best


def test_graph_search():
    for _ in range(ITER):
        n = R.randint(1, 8)
        edges = [(R.randrange(n), R.randrange(n), R.randint(0, 9)) for _ in range(R.randint(0, 15))]
        adj = [[] for _ in range(n)]
        uadj = [[] for _ in range(n)]
        for u, v, w in edges:
            adj[u].append((v, w))
            uadj[u].append(v)
        INF = float("inf")
        d = [[0 if i == j else INF for j in range(n)] for i in range(n)]
        h = [[0 if i == j else INF for j in range(n)] for i in range(n)]
        for u, v, w in edges:
            d[u][v] = min(d[u][v], w)
            h[u][v] = min(h[u][v], 1)
        for k in range(n):
            for i in range(n):
                for j in range(n):
                    d[i][j] = min(d[i][j], d[i][k] + d[k][j])
                    h[i][j] = min(h[i][j], h[i][k] + h[k][j])
        s = R.randrange(n)
        dist, par = dijkstra(adj, s)
        assert dist == d[s]
        for v in range(n):  # parent pointers give a shortest path
            if v != s and dist[v] < INF:
                assert any(u == v and dist[par[v]] + w == dist[v] for p in [par[v]] for u, w in adj[p])
        assert bfs(uadj, s) == [x if x < INF else -1 for x in h[s]]
        srcs = [R.randrange(n) for _ in range(2)]
        assert dijkstra(adj, srcs)[0] == [min(d[a][v] for a in srcs) for v in range(n)]


def test_lca():
    for _ in range(ITER):
        n = R.randint(1, 30)
        adj, root = random_tree(n), R.randrange(n)
        parent, pre, _ = tree_orders(adj, root)
        depth = tree_depths(parent, pre)
        lc = LCA(adj, root)
        def anc(v):
            out = []
            while v >= 0:
                out.append(v)
                v = parent[v]
            return out
        for _ in range(20):
            a, b = R.randrange(n), R.randrange(n)
            sa = set(anc(a))
            exp = next(v for v in anc(b) if v in sa)
            assert lc.lca(a, b) == exp and lc.dist(a, b) == depth[a] + depth[b] - 2 * depth[exp]


def test_flow_matching():
    for _ in range(ITER):
        n = R.randint(2, 8)
        edges = [(R.randrange(n), R.randrange(n), R.randint(0, 9)) for _ in range(R.randint(0, 16))]
        s, t = R.sample(range(n), 2)
        f = MaxFlow(n)
        ids = [f.add_edge(u, v, c) for u, v, c in edges]
        assert f.flow(s, t) == min_cut_brute(n, edges, s, t)
        assert all(0 <= f.edge_flow(e) <= c for e, (_, _, c) in zip(ids, edges))
        nl, nr = R.randint(1, 6), R.randint(1, 6)
        adj = [sorted(set(R.randrange(nr) for _ in range(R.randint(0, 3)))) for _ in range(nl)]
        size, ml = bipartite_matching(nl, nr, adj)
        g = MaxFlow(nl + nr + 2)
        for l in range(nl):
            g.add_edge(nl + nr, l, 1)
            for r in adj[l]:
                g.add_edge(l, nl + r, 1)
        for r in range(nr):
            g.add_edge(nl + r, nl + nr + 1, 1)
        assert size == g.flow(nl + nr, nl + nr + 1)
        used = [r for r in ml if r >= 0]
        assert len(used) == size == len(set(used)) and all(r in adj[l] for l, r in enumerate(ml) if r >= 0)


def test_components_np():
    for _ in range(ITER):
        n = R.randint(1, 30)
        u = [R.randrange(n) for _ in range(R.randint(0, 40))]
        v = [R.randrange(n) for _ in range(len(u))]
        d = DSU(n)
        for a, b in zip(u, v):
            d.union(a, b)
        lab = components_np(n, u, v).tolist()
        for x in range(n):
            assert lab[x] == min(y for y in range(n) if d.find(y) == d.find(x))


def test_strings():
    for _ in range(ITER):
        t = "".join(R.choice("ab") for _ in range(R.randint(0, 30)))
        pat = "".join(R.choice("ab") for _ in range(R.randint(1, 4)))
        assert find_all(t, pat) == [i for i in range(len(t) - len(pat) + 1) if t[i:i + len(pat)] == pat]
        pi = prefix_function(t)
        assert all(pi[i] == max(k for k in range(i + 1) if t[:k] == t[i + 1 - k:i + 1]) for i in range(len(t)))
        z = z_function(t)
        for i in range(len(t)):
            k = 0
            while i + k < len(t) and t[k] == t[i + k]:
                k += 1
            assert z[i] == k
        h = Hash(t)
        for _ in range(20):
            a, b = sorted(R.sample(range(len(t) + 1), 2)) if len(t) >= 1 else (0, 0)
            c = R.randint(0, len(t) - (b - a))
            assert (h.get(a, b) == h.get(c, c + b - a)) == (t[a:b] == t[c:c + b - a])


def test_numtheory():
    n = 3000
    pr = [all(i % d for d in range(2, i)) and i >= 2 for i in range(n + 1)]
    assert list(sieve(n)) == [int(x) for x in pr] and primes_upto(n) == [i for i in range(n + 1) if pr[i]]
    spf = spf_sieve(n)
    assert all(spf[i] == min(d for d in range(2, i + 1) if i % d == 0) for i in range(2, n + 1))
    for i in range(n + 1):
        assert is_prime(i) == pr[i]
    assert is_prime((1 << 61) - 1) and not is_prime(3215031751) and is_prime(1000000007)
    for _ in range(ITER):
        x = R.randint(1, 10**9)
        f = factorize(x)
        prod = 1
        for p_, e in f.items():
            assert is_prime(p_)
            prod *= p_ ** e
        assert prod == x
        a, b = R.randint(0, 10**6), R.randint(0, 10**6)
        g, u, v = ext_gcd(a, b)
        assert g == math.gcd(a, b) and a * u + b * v == g
        m1, m2 = R.randint(1, 30), R.randint(1, 30)
        r1, r2 = R.randrange(m1), R.randrange(m2)
        sol = [x for x in range(m1 * m2) if x % m1 == r1 and x % m2 == r2]
        res = crt(r1, m1, r2, m2)
        assert (res is None) == (not sol) and (res is None or res == (sol[0], m1 * m2 // math.gcd(m1, m2)))
        k, mod, e = R.randint(1, 3), R.randint(2, 10**9), R.randint(0, 20)
        A = [[R.randrange(mod) for _ in range(k)] for _ in range(k)]
        exp = [[int(i == j) % mod for j in range(k)] for i in range(k)]
        for _ in range(e):
            exp = [[sum(exp[i][t] * A[t][j] for t in range(k)) % mod for j in range(k)] for i in range(k)]
        assert mat_pow(A, e, mod) == exp


def test_geometry():
    for _ in range(ITER):
        pts = [(R.randint(-5, 5), R.randint(-5, 5)) for _ in range(R.randint(1, 12))]
        h = convex_hull(pts)
        if len(set(pts)) >= 3 and len(h) >= 3:
            for i in range(len(h)):
                assert cross(h[i - 1], h[i], h[(i + 1) % len(h)]) > 0  # strictly convex, ccw
            assert all(point_in_polygon(p, h) >= 0 for p in pts)
            assert area2(h) > 0
        a, b, c, d = [(R.randint(-4, 4), R.randint(-4, 4)) for _ in range(4)]
        def pt(p, q, t):
            return (p[0] + (q[0] - p[0]) * t, p[1] + (q[1] - p[1]) * t)
        steps = [Fraction(i, 24) for i in range(25)]
        sa = {pt(a, b, t) for t in steps}
        brute = any(pt(c, d, t) in sa for t in steps)  # dense enough on a small grid? use exact check below
        res = segments_intersect(a, b, c, d)
        if brute:
            assert res
        # exact: solve with fractions when not parallel
        den = (b[0] - a[0]) * (d[1] - c[1]) - (b[1] - a[1]) * (d[0] - c[0])
        if den:
            t = Fraction((c[0] - a[0]) * (d[1] - c[1]) - (c[1] - a[1]) * (d[0] - c[0]), den)
            u = Fraction((c[0] - a[0]) * (b[1] - a[1]) - (c[1] - a[1]) * (b[0] - a[0]), den)
            assert res == (0 <= t <= 1 and 0 <= u <= 1)
        q = (R.randint(-6, 6), R.randint(-6, 6))
        if len(h) >= 3:
            inside = all(cross(h[i - 1], h[i], q) > 0 for i in range(len(h)))
            border = any(cross(h[i - 1], h[i], q) == 0 and min(h[i-1][0], h[i][0]) <= q[0] <= max(h[i-1][0], h[i][0]) and min(h[i-1][1], h[i][1]) <= q[1] <= max(h[i-1][1], h[i][1]) for i in range(len(h)))
            assert point_in_polygon(q, h) == (0 if border else 1 if inside else -1)


def test_xor_basis_hilbert():
    for _ in range(ITER):
        vals = [R.randrange(64) for _ in range(R.randint(0, 8))]
        xb = XorBasis(8)
        span = {0}
        for v in vals:
            added = xb.insert(v)
            assert added == (v not in span)
            span |= {u ^ v for u in span}
        assert sorted(xb.span()) == sorted(span) and 2 ** xb.rank == len(span)
        q = R.randrange(64)
        assert (xb.reduce(q) == 0) == (q in span) and xb.max_xor(q) == max(q ^ u for u in span)
    import numpy as np
    n = 16
    xs, ys = np.meshgrid(np.arange(n), np.arange(n))
    o = hilbert_order(xs.ravel(), ys.ravel(), bits=4)
    px, py = xs.ravel()[o], ys.ravel()[o]
    assert sorted(o.tolist()) == list(range(n * n))
    assert all(abs(int(px[i + 1]) - int(px[i])) + abs(int(py[i + 1]) - int(py[i])) == 1 for i in range(n * n - 1))
    gx, gy = hilbert_grid(np.array([-5, 10**9]), np.array([3, 7]))
    assert gx.min() >= 0 and max(int(gx.max()), int(gy.max())) < 2**20


def test_dp_sequences():
    for _ in range(ITER):
        n = R.randint(0, 9)
        a = [R.randint(0, 4) for _ in range(n)]
        for strict in (True, False):
            best = 0
            for mask in range(1 << n):
                sub = [a[i] for i in range(n) if mask >> i & 1]
                if all(x < y if strict else x <= y for x, y in zip(sub, sub[1:])):
                    best = max(best, len(sub))
            got = lis(a, strict)
            vals = [a[i] for i in got]
            assert len(got) == best and got == sorted(set(got))
            assert all(x < y if strict else x <= y for x, y in zip(vals, vals[1:]))
            left, right = nearest_smaller(a, strict)
            lt = (lambda x, y: x < y) if strict else (lambda x, y: x <= y)
            for i in range(n):
                assert left[i] == max([j for j in range(i) if lt(a[j], a[i])], default=-1)
                assert right[i] == min([j for j in range(i + 1, n) if lt(a[j], a[i])], default=n)
        if n:
            k = R.randint(1, n)
            assert window_min(a, k) == [min(a[i:i + k]) for i in range(n - k + 1)]
        q, ref = MinQueue(), []
        for _ in range(20):
            if ref and R.random() < 0.4:
                assert q.pop() == ref.pop(0)
            else:
                x = R.randint(-3, 3)
                q.push(x)
                ref.append(x)
            if ref:
                assert q.min() == min(ref) and len(q) == len(ref)
        xs = [R.randint(-10, 10) for _ in range(R.randint(1, 8))]
        lc, lines = LiChao(xs), []
        for _ in range(R.randint(1, 10)):
            a_, b_ = R.randint(-5, 5), R.randint(-20, 20)
            lc.add(a_, b_)
            lines.append((a_, b_))
            x = R.choice(xs)
            assert lc.query(x) == min(p * x + c for p, c in lines)


def test_aho_corasick():
    for _ in range(ITER):
        pats = ["".join(R.choice("abc") for _ in range(R.randint(1, 4))) for _ in range(R.randint(1, 6))]
        text = "".join(R.choice("abc") for _ in range(R.randint(0, 40)))
        go, fail, cnt = aho_corasick(pats, 3)
        s = tot = 0
        for i, ch in enumerate(text):
            s = go[s][ord(ch) - 97]
            tot += cnt[s]
            assert cnt[s] == sum(text[:i + 1].endswith(p) for p in pats)
        assert tot == sum(text[i:i + len(p)] == p for p in pats for i in range(len(text)))
        # int lists with base 0, and as a DP automaton: count length-n strings avoiding all patterns
        go2, _, cnt2 = aho_corasick([[ord(c) - 97 for c in p] for p in pats], 3, 0)
        assert go2 == go and cnt2 == cnt
        n = R.randint(0, 6)
        dp = [0] * len(go)
        dp[0] = 1
        for _ in range(n):
            nd = [0] * len(go)
            for st, v in enumerate(dp):
                for c in range(3):
                    t = go[st][c]
                    if not cnt[t]:
                        nd[t] += v
            dp = nd
        brute = 0
        for x in range(3 ** n):
            w = "".join("abc"[x // 3 ** j % 3] for j in range(n))
            brute += not any(p in w for p in pats)
        assert sum(dp) == brute


def test_manacher():
    for it in range(ITER):
        s = "".join(R.choice("ab" if it % 2 else "abc") for _ in range(R.randint(0, 30)))
        lst = [ord(c) % 2 for c in s]  # ints 0/1: sentinels must not collide
        for seq in (s, lst):
            p = manacher(seq)
            assert len(p) == 2 * len(s) + 1
            for i in range(2 * len(s) + 1):
                a, b = (i - p[i]) // 2, (i + p[i]) // 2
                assert seq[a:b] == seq[a:b][::-1] and b - a == p[i]
                assert a == 0 or b == len(s) or seq[a - 1] != seq[b]


def test_lyndon():
    for it in range(ITER):
        s = "".join(R.choice("ab" if it % 2 else "abc") for _ in range(R.randint(0, 20)))
        b = lyndon_factorization(s)
        assert b[0] == 0 and b[-1] == len(s)
        ws = [s[b[j]:b[j + 1]] for j in range(len(b) - 1)]
        for w in ws:
            assert w and all(w < w[i:] for i in range(1, len(w)))
        assert all(ws[j] >= ws[j + 1] for j in range(len(ws) - 1))
        rots = [s[i:] + s[:i] for i in range(len(s))]
        r = min_rotation(s)
        assert r == (rots.index(min(rots)) if s else 0)
        assert min_rotation(list(s)) == r


def test_berlekamp_massey():
    for mod in (998244353, 10**9 + 7, 7):
        for _ in range(100):
            L = R.randint(0, 8)
            rec = [R.randrange(mod) for _ in range(L)]
            seq = [R.randrange(mod) for _ in range(L)]
            while len(seq) < 60:
                seq.append(sum(rec[j] * seq[-1 - j] for j in range(L)) % mod)
            C = berlekamp_massey(seq[:2 * L + R.randint(0, 3)], mod)
            assert C[0] == 1 and len(C) - 1 <= L
            for i in range(len(C) - 1, 60):
                assert sum(C[j] * seq[i - j] for j in range(len(C))) % mod == 0
            for n in range(60):
                assert linear_rec_nth(seq, C, n, mod) == seq[n]
            n = R.randint(0, 10**18)
            if L:
                assert linear_rec_nth(seq, C, n, mod) == mat_nth(rec, seq, n, mod)  # companion matrix power
    # minimality: Fibonacci has order 2
    assert berlekamp_massey([0, 1, 1, 2, 3, 5, 8, 13], 101) == [1, 100, 100]
    for _ in range(100):
        a = [R.randrange(10**9 + 7) for _ in range(R.randint(0, 30))]
        b = [R.randrange(10**9 + 7) for _ in range(R.randint(0, 30))]
        ref = [0] * (len(a) + len(b) - 1) if a and b else []
        for i, x in enumerate(a):
            for j, y in enumerate(b):
                ref[i + j] = (ref[i + j] + x * y) % (10**9 + 7)
        assert poly_mul(a, b, 10**9 + 7) == ref


def mat_nth(rec, seq, n, mod):
    L = len(rec)
    if n < L:
        return seq[n]
    M = [rec[:]] + [[int(j == i) for j in range(L)] for i in range(L - 1)]
    def mul(A, B):
        return [[sum(A[i][k] * B[k][j] for k in range(L)) % mod for j in range(L)] for i in range(L)]
    Rm = [[int(i == j) for j in range(L)] for i in range(L)]
    e = n - L + 1
    while e:
        if e & 1:
            Rm = mul(Rm, M)
        M = mul(M, M)
        e >>= 1
    v = seq[L - 1::-1]
    return sum(Rm[0][j] * v[j] for j in range(L)) % mod


def test_partitions():
    n = 200
    p = [1] + [0] * n  # brute: coin DP over parts 1..n
    for k in range(1, n + 1):
        for i in range(k, n + 1):
            p[i] += p[i - k]
    for mod in (10**9 + 7, 1000, 2):
        assert div_euler([1] + [0] * n, mod) == [x % mod for x in p]
    assert div_euler([1], 7) == [1]
    for _ in range(50):
        mod = R.choice((998244353, 13))
        a = [R.randrange(mod) for _ in range(R.randint(1, 60))]
        h = div_euler(a, mod)
        e = [0] * len(a)  # check h * prod(1 - x^k) == a
        euler = [1] + [0] * (len(a) - 1)
        for k in range(1, len(a)):
            for i in range(len(a) - 1, k - 1, -1):
                euler[i] -= euler[i - k]
        for i in range(len(a)):
            e[i] = sum(h[j] * euler[i - j] for j in range(i + 1)) % mod
        assert e == a


def _components(n, adj, alive):
    seen, cnt = set(), 0
    for s in alive:
        if s in seen:
            continue
        cnt += 1
        seen.add(s)
        st = [s]
        while st:
            v = st.pop()
            for w in adj[v]:
                if w in alive and w not in seen:
                    seen.add(w)
                    st.append(w)
    return cnt


def test_biconnected_blocks():
    for _ in range(ITER):
        n = R.randint(1, 7)
        adj = [[] for _ in range(n)]
        pairs = set()
        for _ in range(R.randint(0, 12)):
            a, b = R.randrange(n), R.randrange(n)
            adj[a].append(b)  # multi-edges and self-loops included
            if a != b:
                adj[b].append(a)
                pairs.add(frozenset((a, b)))
        blocks, roots = biconnected_blocks(n, adj)
        assert len(roots) == _components(n, adj, set(range(n)))
        # brute: blocks = maximal vertex sets S, |S| >= 2, with G[S] connected and no cut vertex
        good = []
        for k in range(2, n + 1):
            for S in itertools.combinations(range(n), k):
                S = set(S)
                if k == 2:
                    ok = frozenset(S) in pairs
                else:
                    ok = _components(n, adj, S) == 1 and all(_components(n, adj, S - {x}) == 1 for x in S)
                if ok:
                    good.append(frozenset(S))
        exp = {S for S in good if not any(S < T for T in good)}
        got = [frozenset(b) for b in blocks]
        assert len(got) == len(set(got)) and set(got) == exp and all(len(b) == len(set(b)) for b in blocks)
        tree = block_cut_tree(n, blocks)
        art = {v for v in range(n) if len(tree[v]) > 1}
        base = _components(n, adj, set(range(n)))
        assert art == {x for x in range(n) if _components(n, adj, set(range(n)) - {x}) > base}


def _canon(v, ch):
    return "(" + "".join(sorted(_canon(u, ch) for u in ch[v])) + ")"


def test_subtree_ids():
    for _ in range(ITER):
        n = R.randint(1, 12)
        adj = [[] for _ in range(n)]
        for v in range(1, n):
            p = R.randrange(v)
            adj[p].append(v)
            adj[v].append(p)
        root = R.randrange(n)
        parent, _, post = tree_orders(adj, root)
        ids = subtree_ids(parent, post)
        ch = [[] for _ in range(n)]
        for v in range(n):
            if parent[v] >= 0:
                ch[parent[v]].append(v)
        cs = [_canon(v, ch) for v in range(n)]
        for a in range(n):
            for b in range(n):
                assert (ids[a] == ids[b]) == (cs[a] == cs[b])
        assert sorted(set(ids)) == list(range(len(set(ids))))


def test_kruskal_reconstruction():
    INF = float("inf")
    for _ in range(ITER):
        n = R.randint(1, 8)
        edges = [(R.randint(0, 9), R.randrange(n), R.randrange(n)) for _ in range(R.randint(0, 14))]
        desc = R.random() < 0.5
        edges.sort(reverse=desc)
        par, wt = kruskal_reconstruction(n, edges)
        # brute: minimax (or maximin) path value over all pairs
        sgn = -1 if desc else 1
        B = [[0 if i == j else INF for j in range(n)] for i in range(n)]
        for w, u, v in edges:
            if u != v:
                B[u][v] = B[v][u] = min(B[u][v], sgn * w)
        for k in range(n):
            for i in range(n):
                for j in range(n):
                    B[i][j] = min(B[i][j], max(B[i][k], B[k][j]))
        assert all(par[v] > v or par[v] == -1 for v in range(len(par)))
        for a in range(n):
            anc = set()
            x = a
            while x >= 0:
                anc.add(x)
                x = par[x]
            for b in range(n):
                if a == b:
                    continue
                y = b
                while y >= 0 and y not in anc:
                    y = par[y]
                if y < 0:
                    assert B[a][b] == INF
                else:
                    assert sgn * wt[y] == B[a][b]
        if n > 1 and len(par) == 2 * n - 1:  # connected: the documented LCA usage
            kids = [[] for _ in par]
            for v, p in enumerate(par):
                if p >= 0:
                    kids[p].append(v)
            L = LCA(kids, len(par) - 1)
            a, b = R.sample(range(n), 2)
            assert sgn * wt[L.lca(a, b)] == B[a][b]


def test_floyd():
    for _ in range(ITER):
        n = R.randint(1, 8)
        BIG = 10**9
        D = [[0 if i == j else (R.randint(0, 20) if R.random() < 0.4 else BIG) for j in range(n)] for i in range(n)]
        A = np.array(D, dtype=np.int64)
        floyd(A)
        for k in range(n):
            for i in range(n):
                for j in range(n):
                    D[i][j] = min(D[i][j], D[i][k] + D[k][j])
        assert A.tolist() == D


def test_multiples():
    for _ in range(ITER):
        M = R.randint(0, 60)
        c = [R.randint(-5, 5) for _ in range(M + 1)]
        a = np.array(c, dtype=np.int64)
        primes = primes_upto(M) if R.random() < 0.5 else None
        multiple_sums(a, primes)
        exp = [c[0]] + [sum(c[d * t] for t in range(1, M // d + 1)) for d in range(1, M + 1)]
        assert a.tolist() == exp
        multiple_mobius(a, primes)
        assert a.tolist() == c


def test_mono_hull():
    for it in range(ITER):
        L, X = (5, 10) if it % 2 else (10**9, 10**9)
        h, lines, a = MonoHull(), [], R.randint(-L, L)
        for _ in range(R.randint(1, 40)):
            if not lines or R.randrange(3):
                a -= R.randint(0, 2) if R.randrange(3) else R.randint(0, L)
                b = R.randint(-L * X, L * X)
                h.add(a, b)
                lines.append((a, b))
            x = R.randint(-X, X)
            assert h.query(x) == min(p * x + c for p, c in lines)
    h = MonoHull()  # increasing slopes via (-a, b) at -x
    lines = [(R.randint(-50, 50), R.randint(-99, 99)) for _ in range(30)]
    lines.sort()
    for p, c in lines:
        h.add(-p, c)
    for x in range(-20, 21):
        assert h.query(-x) == min(-p * -x + c for p, c in lines)


def reach(n, adj):
    r = [[False] * n for _ in range(n)]
    for s in range(n):
        st = [s]
        r[s][s] = True
        while st:
            v = st.pop()
            for u in adj[v]:
                if not r[s][u]:
                    r[s][u] = True
                    st.append(u)
    return r


def test_scc():
    for _ in range(ITER):
        n = R.randint(1, 12)
        adj = [[R.randrange(n) for _ in range(R.randint(0, 3))] for _ in range(n)]
        k, comp = scc(adj)
        r = reach(n, adj)
        assert sorted(set(comp)) == list(range(k))
        for a in range(n):
            for b in range(n):
                assert (comp[a] == comp[b]) == (r[a][b] and r[b][a])
            for b in adj[a]:
                assert comp[a] <= comp[b]


def test_two_sat():
    for _ in range(ITER):
        n = R.randint(1, 8)
        cl = [(R.randrange(2 * n), R.randrange(2 * n)) for _ in range(R.randint(0, 3 * n))]
        sat = lambda x: all(x[a >> 1] != (a & 1) or x[b >> 1] != (b & 1) for a, b in cl)  # noqa: E731
        exists = any(sat(x) for x in itertools.product([False, True], repeat=n))
        res = two_sat(n, cl)
        assert (res is not None) == exists
        if res is not None:
            assert len(res) == n and sat(res)


def test_suffix_array():
    for it in range(3000):
        n = R.randint(0, 30)
        a = R.randint(1, 4)
        s = [R.randint(-2, a) * 10**9 for _ in range(n)] if it % 2 else "".join(R.choice("abcd"[:a]) for _ in range(n))
        sa, lcp = suffix_array(s)
        assert sa == sorted(range(n), key=lambda i: s[i:])
        exp = []
        for x, y in zip(sa, sa[1:]):
            h = 0
            while max(x, y) + h < n and s[x + h] == s[y + h]:
                h += 1
            exp.append(h)
        assert lcp == exp


def det_brute(A, p):
    n, tot = len(A), 0
    for perm in itertools.permutations(range(n)):
        inv = sum(perm[i] > perm[j] for i in range(n) for j in range(i + 1, n))
        t = -1 if inv % 2 else 1
        for i in range(n):
            t *= A[i][perm[i]]
        tot += t
    return tot % p if p else tot


def rank_brute(A, p):  # largest k with a nonzero k x k minor
    n, m = len(A), len(A[0]) if A else 0
    for k in range(min(n, m), 0, -1):
        for rs in itertools.combinations(range(n), k):
            for cs in itertools.combinations(range(m), k):
                if det_brute([[A[i][j] for j in cs] for i in rs], p):
                    return k
    return 0


def test_gauss_mod():
    for it in range(ITER * 3):
        p = R.choice([2, 3, 5, 7, 998244353])
        n, m = R.randint(1, 5), R.randint(1, 5)
        lo = 0 if it % 2 else -3 * p
        A = [[R.randint(lo, min(p - 1, 3) if it % 2 else 3 * p) if R.random() < 0.7 else 0 for _ in range(m)] for _ in range(n)]
        if R.random() < 0.3 and n > 1:
            A[-1] = [(x + y) % p for x, y in zip(A[0], A[1 % n])]
        b = [R.randint(lo, p - 1 if it % 2 else 3 * p) for _ in range(n)]
        M = [row + [bi] for row, bi in zip(A, b)]
        rk, det, x = gauss(M, m, p)
        assert rk == rank_brute(A, p)
        if n == m:
            assert det == det_brute(A, p)
        sols = None
        if p <= 3 and m <= 4:  # brute-force existence over GF(p)^m
            sols = any(all(sum(a * v for a, v in zip(row, y)) % p == bi % p for row, bi in zip(A, b))
                       for y in itertools.product(range(p), repeat=m))
        if x is None:
            assert sols in (None, False)
            assert rank_brute([row + [bi] for row, bi in zip(A, b)], p) > rk
        else:
            assert all(sum(a * v for a, v in zip(row, x)) % p == bi % p for row, bi in zip(A, b))


def test_slope_trick():
    for _ in range(500):
        n = R.randint(0, 8)
        a = [R.randint(-6, 6) for _ in range(n)]
        vals = range(-6, 7)
        dp = [0] * len(vals)  # dp[j] = best with b_i = vals[j]
        for x in a:
            best, nd = float("inf"), []
            for j, v in enumerate(vals):
                best = min(best, dp[j])
                nd.append(best + abs(x - v))
            dp = nd
        cost, b = slope_trick(a)
        assert cost == (min(dp) if n else 0), (a, cost)
        assert len(b) == n and all(b[i] <= b[i + 1] for i in range(n - 1))
        assert sum(abs(x - y) for x, y in zip(a, b)) == cost
    # strictly increasing via a_i - i
    for _ in range(300):
        n = R.randint(1, 6)
        a = [R.randint(0, 5) for _ in range(n)]
        cost, b = slope_trick([x - i for i, x in enumerate(a)])
        b = [y + i for i, y in enumerate(b)]
        assert all(b[i] < b[i + 1] for i in range(n - 1))
        best = min(sum(abs(x - y) for x, y in zip(a, c))
                   for c in itertools.combinations(range(-6, 12), n))
        assert cost == best == sum(abs(x - y) for x, y in zip(a, b))


def test_fenwick_lower_bound():
    for _ in range(300):
        n = R.randint(1, 40)
        a = [0] * n
        f = Fenwick(n)
        for _ in range(60):
            i = R.randrange(n)
            if R.random() < 0.3 and a[i]:
                f.add(i, -1)
                a[i] -= 1
            else:
                v = R.randint(0, 3)
                f.add(i, v)
                a[i] += v
            for k in range(0, sum(a) + 2):
                s, want = 0, n
                for j in range(n):
                    s += a[j]
                    if s >= k:
                        want = j
                        break
                assert f.lower_bound(k) == want, (a, k)


def test_bit_count():
    for _ in range(200):
        k = R.randint(1, 3)
        lims = [R.randint(0, 20) for _ in range(k)]
        tgt = R.randint(0, 31)
        kind = R.randrange(3)
        if kind == 0:  # xor == tgt
            ok = lambda b, m: bin(m).count("1") % 2 == tgt >> b & 1  # noqa: E731
            pred = lambda xs: eval("^".join(map(str, xs))) == tgt  # noqa: E731
        elif kind == 1:  # and == 0
            full = (1 << k) - 1
            ok = lambda b, m: m != full  # noqa: E731
            pred = lambda xs: eval("&".join(map(str, xs))) == 0  # noqa: E731
        else:  # or is a submask of tgt
            ok = lambda b, m: m == 0 or tgt >> b & 1  # noqa: E731
            pred = lambda xs: eval("|".join(map(str, xs))) | tgt == tgt  # noqa: E731
        want = sum(pred(xs) for xs in itertools.product(*(range(L + 1) for L in lims)))
        assert bit_count(lims, ok, 6) == want, (lims, kind, tgt)


if __name__ == "__main__":
    tests = [(k, v) for k, v in dict(globals()).items() if k.startswith("test_")]
    for name, fn in tests:
        fn()
        print(f"ok  {name}")
    print(f"{len(tests)} tests passed")
