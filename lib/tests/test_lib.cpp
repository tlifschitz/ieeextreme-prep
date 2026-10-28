// Randomized tests of the C++ lib (lib/*.h) against brute force.
// Run: g++-14 -std=c++17 -O2 -I. lib/tests/test_lib.cpp -o /tmp/t && /tmp/t   (from the repo root)
#include <bits/stdc++.h>
using namespace std;
#define sz(x) ((int)(x).size())
#define pb push_back
using ll = long long;
using pii = pair<int, int>;
using pll = pair<ll, ll>;
using vi = vector<int>;
using vl = vector<ll>;

#include "lib/modular.h"
#include "lib/ntt.h"
#include "lib/tree.h"
#include "lib/segtree.h"
#include "lib/ds.h"
#include "lib/graphs.h"
#include "lib/strings.h"
#include "lib/numtheory.h"
#include "lib/geometry.h"
#include "lib/dp.h"

mt19937_64 R(12345);
ll rnd(ll lo, ll hi) { return uniform_int_distribution<ll>(lo, hi)(R); }
const int ITER = 300;

vl naive_mul(const vl &a, const vl &b) {
    vl c(sz(a) + sz(b) - 1, 0);
    for (int i = 0; i < sz(a); i++)
        for (int j = 0; j < sz(b); j++) c[i + j] = (c[i + j] + a[i] * b[j]) % NTT_MOD;
    return c;
}

vl rand_poly(int n) {
    vl a(n);
    for (ll &x : a) x = rnd(0, NTT_MOD - 1);
    return a;
}

void test_modular() {
    for (int it = 0; it < ITER; it++) {
        ll m = rnd(1, 2e9), b = rnd(0, 4e18), e = rnd(0, 60);
        ll exp = 1 % m;
        for (int i = 0; i < e; i++) exp = (__int128)exp * (b % m) % m;
        assert(power(b, e, m) == exp);
    }
    for (ll m : {7LL, 1000000007LL, NTT_MOD}) {
        vl inv = inverses(min<ll>(m - 1, 5000), m);
        for (int i = 1; i < sz(inv); i++) assert((__int128)inv[i] * i % m == 1);
    }
}

void test_multiply() {
    for (int it = 0; it < ITER; it++) {
        vl a = rand_poly(rnd(1, 120)), b = rand_poly(rnd(1, 120));
        assert(multiply(a, b) == naive_mul(a, b));
    }
    assert(multiply({}, {1, 2}).empty());
}

void test_poly_inv() {
    for (int it = 0; it < ITER; it++) {
        int n = rnd(1, 300);
        vl f = rand_poly(rnd(1, 300));
        if (f[0] == 0) f[0] = 1;
        vl g = poly_inv(f, n), p = multiply(f, g);
        assert(sz(g) == n);
        for (int i = 0; i < n; i++) assert(p[i] == (i == 0));
    }
}

void test_online_convolution() {
    for (int it = 0; it < ITER; it++) {
        int n = rnd(1, 200);
        vl g = rand_poly(rnd(1, 250)), f(n, 0), exp(n, 0);
        f[0] = exp[0] = rnd(0, NTT_MOD - 1);
        ll mul = rnd(1, NTT_MOD - 1);
        for (int i = 1; i < n; i++) {
            for (int j = 1; j <= i && j < sz(g); j++) exp[i] = (exp[i] + g[j] * exp[i - j]) % NTT_MOD;
            exp[i] = (exp[i] * mul + i) % NTT_MOD;  // finish() rewrites f[i]
        }
        online_convolution(f, g, [&](int i) { f[i] = (f[i] * mul + i) % NTT_MOD; });
        assert(f == exp);
    }
}

void test_centroid() {
    for (int it = 0; it < ITER; it++) {
        int n = rnd(1, 60);
        vector<vi> adj(n);
        for (int v = 1; v < n; v++)
            if (rnd(0, 9)) {  // sometimes a forest
                int p = rnd(0, v - 1);
                adj[p].pb(v), adj[v].pb(p);
            }
        auto anc = centroid_ancestors(adj);
        auto bfs = [&](int s) {
            vi d(n, -1);
            queue<int> q;
            q.push(s), d[s] = 0;
            while (!q.empty()) {
                int v = q.front();
                q.pop();
                for (int u : adj[v])
                    if (d[u] < 0) d[u] = d[v] + 1, q.push(u);
            }
            return d;
        };
        for (int v = 0; v < n; v++) {
            assert(!anc[v].empty() && anc[v].back() == pii(v, 0));  // v is its own last centroid
            assert((1 << (sz(anc[v]) - 1)) <= n);                    // depth <= log2 n + 1
            vi d = bfs(v);
            for (auto [c, dc] : anc[v]) assert(d[c] == dc);
        }
        // Every u-v path passes through their deepest common centroid.
        for (int u = 0; u < n; u++) {
            vi du = bfs(u);
            for (int v = 0; v < n; v++) {
                if (du[v] < 0) continue;
                int k = 0;
                while (k < min(sz(anc[u]), sz(anc[v])) && anc[u][k].first == anc[v][k].first) k++;
                assert(k > 0 && anc[u][k - 1].second + anc[v][k - 1].second == du[v]);
            }
        }
    }
}

void test_beats() {
    for (int it = 0; it < ITER; it++) {
        int n = rnd(1, 40);
        vl a(n);
        for (ll &x : a) x = rnd(0, 20);
        Beats t(a);
        for (int q = 0; q < 200; q++) {
            int l = rnd(0, n - 1), r = rnd(l, n - 1), op = rnd(0, 2);
            ll c = rnd(0, 25);
            if (op == 0) {
                t.assign(l, r, c);
                for (int i = l; i <= r; i++) a[i] = c;
            } else if (op == 1) {
                t.chmax(l, r, c);
                for (int i = l; i <= r; i++) a[i] = max(a[i], c);
            } else {
                assert(t.sum_of(l, r) == accumulate(a.begin() + l, a.begin() + r + 1, 0LL));
                assert(t.min_of(l, r) == *min_element(a.begin() + l, a.begin() + r + 1));
            }
        }
    }
}

void test_ds() {
    for (int it = 0; it < ITER; it++) {
        int n = rnd(1, 30);
        DSU d(n);
        vi comp(n);
        iota(comp.begin(), comp.end(), 0);
        vl a(n);
        for (ll &x : a) x = rnd(-50, 50);
        Fenwick f(n);
        for (int i = 0; i < n; i++) f.add(i, a[i]);
        SegTree<ll> mn(a, [](ll x, ll y) { return min(x, y); }, LLONG_MAX);
        vector<string> s(n);
        for (int i = 0; i < n; i++) s[i] = to_string(a[i]);
        SegTree<string> cat(s, [](string x, string y) { return x + y; }, "");
        LazySegTree lz(a);
        for (int q = 0; q < 60; q++) {
            int x = rnd(0, n - 1), y = rnd(0, n - 1);
            bool merged = comp[x] != comp[y];
            assert(d.unite(x, y) == merged);
            if (merged) {
                int old = comp[y];
                for (int &c : comp) if (c == old) c = comp[x];
            }
            int u = rnd(0, n - 1), v = rnd(0, n - 1);
            assert((d.find(u) == d.find(v)) == (comp[u] == comp[v]));
            assert(d.size[d.find(u)] == count(comp.begin(), comp.end(), comp[u]));
            assert(d.count == (int)set<int>(comp.begin(), comp.end()).size());
            int i = rnd(0, n - 1);
            ll val = rnd(-50, 50);
            int l = rnd(0, n), r = rnd(l, n);
            if (rnd(0, 1)) {
                f.add(i, val - a[i]);
                mn.set(i, val), cat.set(i, to_string(val));
                ll delta = val - a[i];
                lz.add(i, i, delta);
                a[i] = val;
            } else if (l < r) {
                ll add = rnd(-5, 5);
                lz.add(l, r - 1, add);
                for (int j = l; j < r; j++) {
                    f.add(j, add), a[j] += add;
                    mn.set(j, a[j]), cat.set(j, to_string(a[j]));
                }
            }
            ll sum = 0, m = LLONG_MAX;
            string c;
            for (int j = l; j < r; j++) sum += a[j], m = min(m, a[j]), c += to_string(a[j]);
            assert(f.range_sum(l, r) == sum && mn.query(l, r) == m && cat.query(l, r) == c);
            if (l < r) assert(lz.sum_of(l, r - 1) == sum && lz.min_of(l, r - 1) == m);
        }
        SparseTable<ll, Max> sp(a);
        SparseTable<ll> sq(a);
        for (int l = 0; l < n; l++)
            for (int r = l + 1; r <= n; r++) {
                assert(sp.query(l, r) == *max_element(a.begin() + l, a.begin() + r));
                assert(sq.query(l, r) == *min_element(a.begin() + l, a.begin() + r));
            }
    }
}

void test_graphs() {
    for (int it = 0; it < ITER; it++) {
        int n = rnd(1, 8), m = rnd(0, 16);
        vector<array<ll, 3>> ed(m);
        vector<vector<pair<int, ll>>> adj(n);
        vector<vi> uadj(n);
        vector<vl> d(n, vl(n, INF_DIST)), h(n, vl(n, INF_DIST));
        for (int i = 0; i < n; i++) d[i][i] = h[i][i] = 0;
        for (auto &[u, v, w] : ed) {
            u = rnd(0, n - 1), v = rnd(0, n - 1), w = rnd(0, 9);
            adj[u].pb({(int)v, w}), uadj[u].pb(v);
            d[u][v] = min(d[u][v], w), h[u][v] = min(h[u][v], 1LL);
        }
        for (int k = 0; k < n; k++)
            for (int i = 0; i < n; i++)
                for (int j = 0; j < n; j++)
                    if (d[i][k] < INF_DIST && d[k][j] < INF_DIST) d[i][j] = min(d[i][j], d[i][k] + d[k][j]),
                                                        h[i][j] = min(h[i][j], h[i][k] + h[k][j]);
        int s = rnd(0, n - 1);
        auto [dist, par] = dijkstra(adj, {s});
        vi bd = bfs(uadj, {s});
        for (int v = 0; v < n; v++) {
            assert(dist[v] == d[s][v]);
            assert(bd[v] == (h[s][v] < INF_DIST ? h[s][v] : -1));
        }
        // max flow vs brute-force min cut; matching vs flow
        if (n >= 2) {
            int t = (s + rnd(1, n - 1)) % n;
            MaxFlow f(n);
            for (auto [u, v, w] : ed) f.add_edge(u, v, w);
            ll best = LLONG_MAX;
            for (int mask = 0; mask < (1 << n); mask++) {
                if (!(mask >> s & 1) || (mask >> t & 1)) continue;
                ll c = 0;
                for (auto [u, v, w] : ed) if ((mask >> u & 1) && !(mask >> v & 1)) c += w;
                best = min(best, c);
            }
            assert(f.flow(s, t) == best);
        }
        int nl = rnd(1, 6), nr = rnd(1, 6);
        BipartiteMatching bm(nl, nr);
        MaxFlow g(nl + nr + 2);
        for (int l = 0; l < nl; l++) {
            g.add_edge(nl + nr, l, 1);
            set<int> rs;
            for (int k = rnd(0, 3); k--;) rs.insert(rnd(0, nr - 1));
            for (int r : rs) bm.add_edge(l, r), g.add_edge(l, nl + r, 1);
        }
        for (int r = 0; r < nr; r++) g.add_edge(nl + r, nl + nr + 1, 1);
        assert(bm.solve() == g.flow(nl + nr, nl + nr + 1));
        // LCA vs naive on a random tree
        int tn = rnd(1, 30), root = rnd(0, tn - 1);
        vector<vi> tadj(tn);
        vi par0(tn, -1);
        for (int v = 1; v < tn; v++) {
            int p = rnd(0, v - 1);
            tadj[p].pb(v), tadj[v].pb(p);
        }
        LCA lc(tadj, root);
        vi pr(tn, -1), dp(tn, 0), order = {root};
        vector<char> vis(tn, 0);
        vis[root] = 1;
        for (int i = 0; i < sz(order); i++)
            for (int u : tadj[order[i]])
                if (!vis[u]) vis[u] = 1, pr[u] = order[i], dp[u] = dp[order[i]] + 1, order.pb(u);
        for (int q = 0; q < 20; q++) {
            int a = rnd(0, tn - 1), b = rnd(0, tn - 1), x = a, y = b;
            while (dp[x] > dp[y]) x = pr[x];
            while (dp[y] > dp[x]) y = pr[y];
            while (x != y) x = pr[x], y = pr[y];
            assert(lc.lca(a, b) == x && lc.dist(a, b) == dp[a] + dp[b] - 2 * dp[x]);
        }
    }
}

void test_tree_dfs_weighted_centroid() {
    for (int it = 0; it < ITER; it++) {
        int n = rnd(1, 40), root = rnd(0, n - 1);
        vector<vi> adj(n);
        vector<vector<pair<int, ll>>> wadj(n);
        for (int v = 1; v < n; v++) {
            int p = rnd(0, v - 1);
            ll w = rnd(-5, 20);
            adj[p].pb(v), adj[v].pb(p);
            wadj[p].pb({v, w}), wadj[v].pb({p, w});
        }
        TreeDFS t(adj, root);
        assert(sz(t.order) == n && t.order[0] == root && t.par[root] == -1);
        for (int v = 0; v < n; v++) {
            assert(t.order[t.tin[v]] == v);
            if (v != root) assert(t.tin[t.par[v]] < t.tin[v] && t.dep[v] == t.dep[t.par[v]] + 1);
            int size = 0;  // subtree = order[tin, tout)
            for (int u = 0; u < n; u++) {
                int x = u;
                while (x != -1 && x != v) x = t.par[x];
                if (x == v) size++, assert(t.is_ancestor(v, u));
                else assert(!t.is_ancestor(v, u));
            }
            assert(t.tout[v] - t.tin[v] == size);
        }
        auto anc = centroid_ancestors(wadj);
        for (int v = 0; v < n; v++) {  // weighted distances by DFS from v
            vl d(n, LLONG_MIN);
            vi st = {v};
            d[v] = 0;
            while (!st.empty()) {
                int x = st.back();
                st.pop_back();
                for (auto [u, w] : wadj[x]) if (d[u] == LLONG_MIN) d[u] = d[x] + w, st.pb(u);
            }
            assert(anc[v].back().first == v);
            for (auto [c, dc] : anc[v]) assert(d[c] == dc);
        }
    }
}

void test_strings_nt_geo() {
    for (int it = 0; it < ITER; it++) {
        string s;
        for (int i = rnd(0, 30); i--;) s += char('a' + rnd(0, 1));
        string pat;
        for (int i = rnd(1, 4); i--;) pat += char('a' + rnd(0, 1));
        vi exp;
        for (int i = 0; i + sz(pat) <= sz(s); i++) if (s.compare(i, sz(pat), pat) == 0) exp.pb(i);
        assert(find_all(s, pat) == exp);
        vi z = z_function(s), pi = prefix_function(s);
        for (int i = 0; i < sz(s); i++) {
            int k = 0;
            while (i + k < sz(s) && s[k] == s[i + k]) k++;
            assert(z[i] == k);
            int b = 0;
            for (int L = 1; L <= i; L++) if (s.compare(0, L, s, i + 1 - L, L) == 0) b = L;
            assert(pi[i] == b);
        }
        Hash h(s);
        for (int q = 0; q < 20 && sz(s); q++) {
            int a = rnd(0, sz(s)), b = rnd(a, sz(s)), c = rnd(0, sz(s) - (b - a));
            assert((h.get(a, b) == h.get(c, c + b - a)) == (s.compare(a, b - a, s, c, b - a) == 0));
        }
        // number theory
        ll m1 = rnd(1, 30), m2 = rnd(1, 30), r1 = rnd(0, m1 - 1), r2 = rnd(0, m2 - 1);
        ll sol = -1;
        for (ll x = 0; x < m1 * m2 && sol < 0; x++) if (x % m1 == r1 && x % m2 == r2) sol = x;
        pll c = crt(r1, m1, r2, m2);
        assert(c.first == sol && (sol < 0 || c.second == m1 / __gcd(m1, m2) * m2));
        ll x = rnd(1, 1e12);
        ll prod = 1;
        for (auto [p, e] : factorize(x)) { assert(is_prime(p)); while (e--) prod *= p; }
        assert(prod == x);
        int k = rnd(1, 3);
        ll mod = rnd(2, 2e9), e = rnd(0, 20);
        Mat A(k, vl(k)), E(k, vl(k, 0));
        for (auto &r : A) for (ll &v : r) v = rnd(0, mod - 1);
        for (int i = 0; i < k; i++) E[i][i] = 1 % mod;
        for (int i = 0; i < e; i++) E = mat_mul(E, A, mod);
        assert(mat_pow(A, e, mod) == E);
        // geometry
        vector<Pt> pts(rnd(1, 12));
        for (auto &q : pts) q = {rnd(-5, 5), rnd(-5, 5)};
        auto hl = convex_hull(pts);
        if (sz(hl) >= 3) {
            for (int i = 0; i < sz(hl); i++) assert(cross(hl[(i + sz(hl) - 1) % sz(hl)], hl[i], hl[(i + 1) % sz(hl)]) > 0);
            for (auto &q : pts) assert(point_in_polygon(q, hl) >= 0);
            assert(area2(hl) > 0);
        }
        Pt a{rnd(-4, 4), rnd(-4, 4)}, b{rnd(-4, 4), rnd(-4, 4)}, cc{rnd(-4, 4), rnd(-4, 4)}, d{rnd(-4, 4), rnd(-4, 4)};
        ll den = (b.x - a.x) * (d.y - cc.y) - (b.y - a.y) * (d.x - cc.x);
        if (den) {  // exact parametric check: t = tn / den, u = un / den in [0, 1]
            ll tn = (cc.x - a.x) * (d.y - cc.y) - (cc.y - a.y) * (d.x - cc.x);
            ll un = (cc.x - a.x) * (b.y - a.y) - (cc.y - a.y) * (b.x - a.x);
            if (den < 0) den = -den, tn = -tn, un = -un;
            assert(segments_intersect(a, b, cc, d) == (0 <= tn && tn <= den && 0 <= un && un <= den));
        }
    }
    Sieve sv(3000);
    for (int i = 2; i <= 3000; i++) {
        int sp = 2;
        while (i % sp) sp++;
        assert(sv.spf[i] == sp && is_prime(i) == (sp == i));
    }
    assert(is_prime((1LL << 61) - 1) && !is_prime(3215031751LL) && powmod(2, 62, (1LL << 61) - 1) == 2);
}

void test_xor_hilbert() {
    for (int it = 0; it < ITER; it++) {
        XorBasis xb;
        set<ll> span = {0};
        for (int k = rnd(0, 8); k--;) {
            ll v = rnd(0, 63);
            assert(xb.insert(v) == !span.count(v));
            set<ll> ns = span;
            for (ll u : span) ns.insert(u ^ v);
            span = ns;
        }
        assert((1LL << xb.rank) == sz(span));
        ll q = rnd(0, 63), best = 0;
        for (ll u : span) best = max(best, q ^ u);
        assert((xb.reduce(q) == 0) == (span.count(q) > 0) && xb.max_xor(q) == best);
    }
    // range trick: span of a[l..r] = {bas : pos >= l}
    for (int it = 0; it < ITER; it++) {
        int n = rnd(1, 12);
        vl a(n);
        for (ll &x : a) x = rnd(0, 31);
        XorBasis xb;
        for (int r = 0; r < n; r++) {
            xb.insert(a[r], r);
            for (int l = 0; l <= r; l++) {
                set<ll> span = {0};
                for (int i = l; i <= r; i++) { set<ll> ns = span; for (ll u : span) ns.insert(u ^ a[i]); span = ns; }
                int k = 0;
                for (int b = 0; b < XorBasis::B; b++) if (xb.bas[b] && xb.pos[b] >= l) k++;
                assert((1LL << k) == sz(span));
            }
        }
    }
    vector<pair<ll, pll>> pts;
    for (ll x = 0; x < 16; x++) for (ll y = 0; y < 16; y++) pts.pb({hilbert(x, y, 4), {x, y}});
    sort(pts.begin(), pts.end());
    for (int i = 0; i + 1 < sz(pts); i++) {
        assert(pts[i].first == i);
        assert(llabs(pts[i + 1].second.first - pts[i].second.first) + llabs(pts[i + 1].second.second - pts[i].second.second) == 1);
    }
}

void test_dp() {
    for (int it = 0; it < ITER; it++) {
        int n = rnd(0, 9);
        vl a(n);
        for (ll &x : a) x = rnd(0, 4);
        for (bool strict : {true, false}) {
            auto ok = [&](ll x, ll y) { return strict ? x < y : x <= y; };
            int best = 0;
            for (int mask = 0; mask < (1 << n); mask++) {
                vl s;
                for (int i = 0; i < n; i++) if (mask >> i & 1) s.pb(a[i]);
                bool good = true;
                for (int i = 0; i + 1 < sz(s); i++) good &= ok(s[i], s[i + 1]);
                if (good) best = max(best, sz(s));
            }
            vi got = lis(a, strict);
            assert(sz(got) == best);
            for (int i = 0; i + 1 < sz(got); i++) assert(got[i] < got[i + 1] && ok(a[got[i]], a[got[i + 1]]));
            auto [L, Rt] = nearest_smaller(a, strict);
            for (int i = 0; i < n; i++) {
                int l = -1, r = n;
                for (int j = 0; j < i; j++) if (ok(a[j], a[i])) l = j;
                for (int j = n - 1; j > i; j--) if (ok(a[j], a[i])) r = j;
                assert(L[i] == l && Rt[i] == r);
            }
        }
        if (n) {
            int k = rnd(1, n);
            vl w = window_min(a, k);
            for (int i = 0; i + k <= n; i++) assert(w[i] == *min_element(a.begin() + i, a.begin() + i + k));
        }
        MinQueue<ll> q;
        deque<ll> ref;
        for (int s = 0; s < 20; s++) {
            if (!ref.empty() && rnd(0, 9) < 4) assert(q.pop() == ref.front()), ref.pop_front();
            else { ll x = rnd(-3, 3); q.push(x), ref.pb(x); }
            if (!ref.empty()) assert(q.min() == *min_element(ref.begin(), ref.end()) && q.size() == sz(ref));
        }
        vl xs(rnd(1, 8));
        for (ll &x : xs) x = rnd(-10, 10);
        LiChao lc(xs);
        vector<pll> lines;
        for (int s = rnd(1, 10); s--;) {
            ll p = rnd(-5, 5), c = rnd(-20, 20);
            lc.add(p, c), lines.pb({p, c});
            ll x = xs[rnd(0, sz(xs) - 1)], m = LLONG_MAX;
            for (auto [u, v] : lines) m = min(m, u * x + v);
            assert(lc.query(x) == m);
        }
    }
}

void test_hungarian() {
    for (int it = 0; it < 3 * ITER; it++) {
        int n = rnd(0, 6), m = rnd(max(n, 1), 7);
        ll lim = it % 3 == 0 ? 3 : it % 3 == 1 ? 1000 : (ll)1e12;
        vector<vl> a(n, vl(m));
        for (auto &r : a) for (ll &x : r) x = rnd(-lim, lim) + (it % 7 == 0 ? lim : 0);
        vi perm(m);
        iota(perm.begin(), perm.end(), 0);
        ll best = LLONG_MAX;
        do {
            ll s = 0;
            for (int i = 0; i < n; i++) s += a[i][perm[i]];
            best = min(best, s);
        } while (next_permutation(perm.begin(), perm.end()));
        auto [cost, col] = hungarian(a);
        assert(cost == best && sz(col) == n);
        set<int> used(col.begin(), col.end());
        assert(sz(used) == n);
        ll s = 0;
        for (int i = 0; i < n; i++) assert(0 <= col[i] && col[i] < m), s += a[i][col[i]];
        assert(s == cost);
        vector<vector<double>> d(n, vector<double>(m));
        for (int i = 0; i < n; i++) for (int j = 0; j < m; j++) d[i][j] = a[i][j];
        if (lim <= 1000) assert(fabs(hungarian(d).first - best) < 1e-6);
    }
    for (int it = 0; it < ITER; it++) {  // larger: DP over column subsets
        int n = rnd(1, 9), m = rnd(n, 12);
        vector<vl> a(n, vl(m));
        for (auto &r : a) for (ll &x : r) x = rnd(-1e6, it % 2 ? 1e6 : 3);
        vl dp(1 << m, LLONG_MAX);
        dp[0] = 0;
        ll best = LLONG_MAX;
        for (int mask = 0; mask < (1 << m); mask++) {
            if (dp[mask] == LLONG_MAX) continue;
            int i = __builtin_popcount(mask);
            if (i == n) { best = min(best, dp[mask]); continue; }
            for (int j = 0; j < m; j++)
                if (!(mask >> j & 1)) dp[mask | 1 << j] = min(dp[mask | 1 << j], dp[mask] + a[i][j]);
        }
        assert(hungarian(a).first == best);
    }
    vector<vl> empty;
    assert(hungarian(empty).first == 0);
}

void test_kruskal_tree() {
    for (int it = 0; it < ITER; it++) {
        int n = rnd(1, 12), m = rnd(0, 20);
        vector<tuple<ll, int, int>> edges;
        const ll INF = LLONG_MAX;
        vector<vl> b(n, vl(n, INF));
        for (int i = 0; i < m; i++) {
            int u = rnd(0, n - 1), v = rnd(0, n - 1);
            ll w = rnd(-5, 5);
            edges.pb({w, u, v});
            b[u][v] = min(b[u][v], w), b[v][u] = min(b[v][u], w);
        }
        for (int k = 0; k < n; k++)
            for (int i = 0; i < n; i++)
                for (int j = 0; j < n; j++) b[i][j] = min(b[i][j], max(b[i][k], b[k][j]));
        KruskalTree kt(n, edges);
        LCA lca(kt.adj, kt.root);
        assert(sz(kt.adj) <= 2 * n);
        for (int i = 0; i < n; i++)
            for (int j = 0; j < n; j++)
                if (i != j) assert(kt.w[lca.lca(i, j)] == b[i][j]);
    }
}

string canon(const vector<vi> &adj, int v, int p) {
    vector<string> ch;
    for (int u : adj[v]) if (u != p) ch.pb(canon(adj, u, v));
    sort(ch.begin(), ch.end());
    string s = "(";
    for (auto &c : ch) s += c;
    return s + ")";
}

void test_rooted_iso() {
    for (int it = 0; it < ITER; it++) {
        int k = rnd(1, 3);
        vector<vi> adj;
        vi roots, rootof;
        for (int t = 0; t < k; t++) {
            int n = rnd(1, 9), off = sz(adj);
            adj.resize(off + n);
            for (int v = 1; v < n; v++) {
                int p = rnd(0, v - 1) + off, c = v + off;
                adj[p].pb(c), adj[c].pb(p);
            }
            int r = off + rnd(0, n - 1);
            roots.pb(r);
            // a relabeled copy, rooted at the image of r
            vi perm(n);
            iota(perm.begin(), perm.end(), sz(adj));
            shuffle(perm.begin(), perm.end(), R);
            int off2 = sz(adj);
            adj.resize(off2 + n);
            for (int v = 0; v < n; v++)
                for (int u : adj[off + v]) adj[perm[v]].pb(perm[u - off]);
            for (auto &l : adj) shuffle(l.begin(), l.end(), R);
            roots.pb(perm[r - off]);
        }
        int N = sz(adj);
        vi id = rooted_iso_ids(adj, roots);
        vi par(N, -2);  // parent under the given roots
        for (int r : roots) {
            par[r] = -1;
            vi st = {r};
            while (!st.empty()) {
                int v = st.back();
                st.pop_back();
                for (int u : adj[v]) if (par[u] == -2) par[u] = v, st.pb(u);
            }
        }
        vector<string> c(N);
        for (int v = 0; v < N; v++) c[v] = canon(adj, v, par[v]);
        for (int i = 0; i + 1 < sz(roots); i += 2) assert(id[roots[i]] == id[roots[i + 1]]);
        for (int u = 0; u < N; u++)
            for (int v = 0; v < N; v++) assert((id[u] == id[v]) == (c[u] == c[v]));
    }
    assert(rooted_iso_ids({{}}, {0}) == vi{0});
}

void test_mono_hull() {
    for (int it = 0; it < ITER; it++) {
        ll L = it % 2 ? 5 : (ll)1e9, X = it % 2 ? 10 : (ll)1e9;
        MonoHull h, hi;
        vector<pll> lines;
        ll a = rnd(-L, L), x = -X;
        for (int s = rnd(1, 40); s--;) {
            if (lines.empty() || rnd(0, 2)) {
                a -= rnd(0, 2) ? rnd(0, 2) : rnd(0, L);
                ll b = rnd(-L * X, L * X);
                h.add(a, b), hi.add(a, b), lines.pb({a, b});
            }
            ll q = rnd(-X, X), m = LLONG_MAX, mi = LLONG_MAX;
            x = min(X, x + rnd(0, X / 3 + 1));
            for (auto [p, c] : lines) m = min(m, p * q + c), mi = min(mi, p * x + c);
            assert(h.query(q) == m);
            assert(hi.query_inc(x) == mi);
        }
    }
}

template <class F>
void timed(const char *name, F f) {
    auto t0 = chrono::steady_clock::now();
    f();
    printf("    %s: %.3f s\n", name, chrono::duration<double>(chrono::steady_clock::now() - t0).count());
}

void speed() {
    timed("hungarian 500x500 ll, a[i][j] = -i*j - noise", [] {
        vector<vl> a(500, vl(500));
        for (int i = 0; i < 500; i++) for (int j = 0; j < 500; j++) a[i][j] = -(ll)i * j - rnd(0, 3);
        auto [c, col] = hungarian(a);
        ll s = 0;
        for (int i = 0; i < 500; i++) s += a[i][col[i]];
        assert(s == c && c < 0);
    });
    timed("hungarian 300x2000 ll", [] {
        vector<vl> a(300, vl(2000));
        for (auto &r : a) for (ll &x : r) x = rnd(0, 1e9);
        assert(hungarian(a).first >= 0);
    });
    timed("kruskal tree n=2e5 m=4e5 + LCA + 2e5 queries", [] {
        int n = 200000;
        vector<tuple<ll, int, int>> e;
        for (int i = 0; i < 2 * n; i++) e.pb({rnd(0, 1e9), (int)rnd(0, n - 1), (int)rnd(0, n - 1)});
        KruskalTree kt(n, e);
        LCA lca(kt.adj, kt.root);
        ll s = 0;
        for (int i = 0; i < n; i++) s += kt.w[lca.lca(rnd(0, n - 1), rnd(0, n - 1))];
        assert(s);
    });
    int n = 1000000;
    for (int shape = 0; shape < 4; shape++) {
        vector<vi> adj(n);
        for (int v = 1; v < n; v++) {
            int p = shape == 0 ? rnd(0, v - 1) : shape == 1 ? v - 1 : shape == 2 ? 0 : (v - 1) / 2;
            adj[p].pb(v), adj[v].pb(p);
        }
        const char *names[] = {"random", "path", "star", "binary"};
        string label = string("rooted_iso_ids n=1e6 ") + names[shape];
        timed(label.c_str(), [&] { rooted_iso_ids(adj, {0}); });
    }
    timed("MonoHull 1e6 adds + 1e6 query + 1e6 query_inc", [] {
        MonoHull h;
        ll a = 1e9, s = 0;
        for (int i = 0; i < 1000000; i++) h.add(a -= rnd(0, 1000), rnd(-1e12, 1e12)), s += h.query(rnd(-1e6, 1e6));
        for (int i = 0; i < 1000000; i++) s += h.query_inc(i - 500000);
        assert(s);
    });
}

void test_partitions() {
    int n = 300;
    for (ll m : {1000000007LL, 1000LL, 2LL}) {
        vl p(n + 1, 0);  // brute: coin DP over parts 1..n
        p[0] = 1;
        for (int k = 1; k <= n; k++)
            for (int i = k; i <= n; i++) p[i] = (p[i] + p[i - k]) % m;
        assert(partitions(n, m) == p);
    }
    for (int it = 0; it < 50; it++) {
        ll m = rnd(0, 1) ? 998244353 : 13;
        int n = rnd(1, 60);
        vl a(n);
        for (ll &x : a) x = rnd(0, m - 1);
        vl h = div_euler(a, m), e(n, 0);
        e[0] = 1;  // prod (1 - x^k), then check h * e == a
        for (int k = 1; k < n; k++)
            for (int i = n - 1; i >= k; i--) e[i] = (e[i] - e[i - k] + m) % m;
        for (int i = 0; i < n; i++) {
            ll v = 0;
            for (int j = 0; j <= i; j++) v = (v + h[j] * e[i - j]) % m;
            assert(v == a[i]);
        }
    }
}


void test_scc() {
    for (int it = 0; it < ITER; it++) {
        int n = rnd(1, 12);
        vector<vi> adj(n);
        for (auto &a : adj)
            for (int j = rnd(0, 3); j--;) a.pb(rnd(0, n - 1));
        vector<vector<char>> r(n, vector<char>(n, 0));
        for (int s = 0; s < n; s++) {
            vi st = {s};
            r[s][s] = 1;
            while (!st.empty()) {
                int v = st.back();
                st.pop_back();
                for (int u : adj[v])
                    if (!r[s][u]) r[s][u] = 1, st.pb(u);
            }
        }
        auto [k, comp] = scc(adj);
        set<int> ids(comp.begin(), comp.end());
        assert(sz(ids) == k && *ids.begin() == 0 && *ids.rbegin() == k - 1);
        for (int a = 0; a < n; a++) {
            for (int b = 0; b < n; b++) assert((comp[a] == comp[b]) == (r[a][b] && r[b][a]));
            for (int b : adj[a]) assert(comp[a] <= comp[b]);
        }
    }
}

void test_two_sat() {
    int nsat = 0;
    for (int it = 0; it < ITER; it++) {
        int n = rnd(1, 8);
        vector<pii> cl(rnd(0, 3 * n));
        for (auto &[a, b] : cl) a = rnd(0, 2 * n - 1), b = rnd(0, 2 * n - 1);
        auto sat = [&](const vector<bool> &x) {
            for (auto [a, b] : cl)
                if (x[a >> 1] == (a & 1) && x[b >> 1] == (b & 1)) return false;
            return true;
        };
        bool exists = false;
        for (int m = 0; m < (1 << n) && !exists; m++) {
            vector<bool> x(n);
            for (int i = 0; i < n; i++) x[i] = m >> i & 1;
            exists = sat(x);
        }
        auto res = two_sat(n, cl);
        assert(!res.empty() == exists);
        if (exists) assert(sz(res) == n && sat(res)), nsat++;
    }
    assert(nsat > 30 && nsat < ITER - 30);
}

// brute min cost of each flow value: enumerate integer flows on every edge
void test_mcmf() {
    for (int it = 0; it < ITER; it++) {
        int n = rnd(2, 5), m = rnd(1, 7), s = 0, t = n - 1;
        bool dag = rnd(0, 1);  // DAG: negative costs allowed
        vector<array<ll, 4>> es(m);
        for (auto &[u, v, cap, cost] : es) {
            do u = rnd(0, n - 1), v = rnd(0, n - 1); while (u == v || (dag && u > v));
            cap = rnd(0, 2), cost = dag ? rnd(-5, 9) : rnd(0, 9);
        }
        map<ll, ll> best;  // flow value -> min cost
        vl fl(m, 0);
        while (true) {
            vl bal(n, 0);
            ll c = 0;
            for (int i = 0; i < m; i++) bal[es[i][0]] -= fl[i], bal[es[i][1]] += fl[i], c += fl[i] * es[i][3];
            bool ok = true;
            for (int v = 0; v < n; v++) if (v != s && v != t && bal[v]) ok = false;
            if (ok && !best.count(bal[t]) || ok && best[bal[t]] > c) best[bal[t]] = c;
            int i = 0;
            while (i < m && fl[i] == es[i][2]) fl[i++] = 0;
            if (i == m) break;
            fl[i]++;
        }
        MaxFlow mf(n);
        for (auto [u, v, cap, cost] : es) mf.add_edge(u, v, cap);
        ll F = mf.flow(s, t);
        assert(best.rbegin()->first == F);
        ll lim = rnd(0, 1) ? LLONG_MAX : rnd(0, F + 1);
        MCMF mc(n);
        vi ids;
        for (auto [u, v, cap, cost] : es) ids.pb(mc.add_edge(u, v, cap, cost));
        auto [f, c] = mc.flow(s, t, lim);
        assert(f == min(F, lim) && c == best[f]);
        ll f2 = 0, c2 = 0;  // edge flows consistent with the answer
        for (int i = 0; i < m; i++) {
            ll x = mc.e[ids[i] ^ 1].cap;
            assert(0 <= x && x <= es[i][2]);
            c2 += x * es[i][3];
            if (es[i][0] == s) f2 += x;
            if (es[i][1] == s) f2 -= x;
        }
        assert(f2 == f && c2 == c);
    }
    for (int it = 0; it < 100; it++) {  // assignment vs hungarian
        int n = rnd(1, 8), m = rnd(n, 9);
        vector<vl> a(n, vl(m));
        MCMF mc(n + m + 2);
        for (int i = 0; i < n; i++) mc.add_edge(n + m, i, 1, 0);
        for (int j = 0; j < m; j++) mc.add_edge(n + j, n + m + 1, 1, 0);
        for (int i = 0; i < n; i++)
            for (int j = 0; j < m; j++) a[i][j] = rnd(-50, 50), mc.add_edge(i, n + j, 1, a[i][j]);
        auto [f, c] = mc.flow(n + m, n + m + 1);
        assert(f == n && c == hungarian(a).first);
    }
}


template <class S> void check_sa(const S &s) {
    int n = sz(s);
    auto [sa, lcp] = suffix_array(s);
    vi e(n);
    iota(begin(e), end(e), 0);
    sort(begin(e), end(e), [&](int a, int b) { return lexicographical_compare(begin(s) + a, end(s), begin(s) + b, end(s)); });
    assert(sa == e && sz(lcp) == max(n - 1, 0));
    for (int i = 0; i + 1 < n; i++) {
        int h = 0;
        while (max(sa[i], sa[i + 1]) + h < n && s[sa[i] + h] == s[sa[i + 1] + h]) h++;
        assert(lcp[i] == h);
    }
}

void test_suffix_array() {
    for (int it = 0; it < 3000; it++) {
        int n = rnd(0, 40), a = rnd(1, 4);
        string s;
        vi v;
        for (int i = 0; i < n; i++) s += (char)(it % 3 ? 'a' + rnd(0, a - 1) : rnd(-128, 127)), v.pb(rnd(-a, a) * 1000000000);
        check_sa(s), check_sa(v);
    }
}

ll det_brute(const vector<vl> &A, ll p) {
    int n = sz(A);
    vi perm(n);
    iota(begin(perm), end(perm), 0);
    ll tot = 0;
    do {
        int inv = 0;
        for (int i = 0; i < n; i++) for (int j = i + 1; j < n; j++) inv += perm[i] > perm[j];
        ll t = inv % 2 ? p - 1 : 1;
        for (int i = 0; i < n; i++) t = (__int128)t * A[i][perm[i]] % p;
        tot = (tot + t) % p;
    } while (next_permutation(begin(perm), end(perm)));
    return tot;
}

int rank_brute(const vector<vl> &A, int m, ll p) {  // largest k with a nonzero k x k minor (first m columns)
    int n = sz(A), best = 0;
    for (int rs = 1; rs < 1 << n; rs++)
        for (int cs = 1; cs < 1 << m; cs++) {
            int k = __builtin_popcount(rs);
            if (k != __builtin_popcount(cs) || k <= best) continue;
            vector<vl> B;
            for (int i = 0; i < n; i++) if (rs >> i & 1) {
                B.pb({});
                for (int j = 0; j < m; j++) if (cs >> j & 1) B.back().pb(A[i][j]);
            }
            if (det_brute(B, p)) best = k;
        }
    return best;
}

void test_gauss() {
    for (int it = 0; it < ITER * 3; it++) {
        ll p = vl{2, 3, 5, 7, 998244353, 2999999929LL}[rnd(0, 5)];
        int n = rnd(1, 5), m = rnd(1, 5);
        vector<vl> A(n, vl(m + 1));
        for (auto &row : A) for (ll &v : row) v = rnd(0, 2) ? rnd(0, p - 1) : 0;
        if (n > 1 && rnd(0, 2) == 0) for (int j = 0; j <= m; j++) A[n - 1][j] = (A[0][j] * 2 + A[1][j]) % p;
        auto M = A;
        ll det;
        vl x;
        int rk = gauss(M, m, p, det, x);
        assert(rk == rank_brute(A, m, p));
        if (n == m) assert(det == det_brute(A, p));
        if (x.empty()) assert(rank_brute(A, m + 1, p) > rk);
        else for (auto &row : A) {
            ll s = 0;
            for (int j = 0; j < m; j++) s = (s + (__int128)row[j] * x[j]) % p;
            assert(s == row[m]);
        }
    }
}


void test_slope_trick() {
    for (int it = 0; it < 500; it++) {
        int n = rnd(0, 8);
        vl a(n);
        for (ll &x : a) x = rnd(-6, 6);
        vl dp(13, 0);
        for (ll x : a) {
            ll best = LLONG_MAX;
            for (int j = 0; j < 13; j++) best = min(best, dp[j]), dp[j] = best + llabs(x - (j - 6));
        }
        assert(slope_trick(a) == (n ? *min_element(dp.begin(), dp.end()) : 0));
    }
}

void test_fenwick_lower_bound() {
    for (int it = 0; it < 300; it++) {
        int n = rnd(1, 40);
        vl a(n, 0);
        Fenwick f(n);
        for (int s = 0; s < 60; s++) {
            int i = rnd(0, n - 1);
            ll v = (a[i] && rnd(0, 2) == 0) ? -1 : rnd(0, 3);
            f.add(i, v), a[i] += v;
            ll tot = accumulate(a.begin(), a.end(), 0LL);
            for (ll k = 0; k <= tot + 1; k++) {
                ll p = 0;
                int want = n;
                for (int j = 0; j < n; j++)
                    if ((p += a[j]) >= k) { want = j; break; }
                assert(f.lower_bound(k) == want);
            }
        }
    }
}

int main() {
    pair<const char *, void (*)()> tests[] = {
        {"modular", test_modular},     {"multiply", test_multiply}, {"poly_inv", test_poly_inv},
        {"online_convolution", test_online_convolution}, {"centroid", test_centroid}, {"beats", test_beats}, {"ds", test_ds}, {"graphs", test_graphs}, {"tree_dfs_weighted_centroid", test_tree_dfs_weighted_centroid}, {"strings_nt_geo", test_strings_nt_geo}, {"xor_hilbert", test_xor_hilbert}, {"dp", test_dp}, {"hungarian", test_hungarian}, {"kruskal_tree", test_kruskal_tree}, {"rooted_iso", test_rooted_iso}, {"mono_hull", test_mono_hull}, {"partitions", test_partitions}, {"scc", test_scc}, {"two_sat", test_two_sat}, {"mcmf", test_mcmf}, {"suffix_array", test_suffix_array}, {"gauss", test_gauss}, {"slope_trick", test_slope_trick}, {"fenwick_lower_bound", test_fenwick_lower_bound},
    };
    for (auto [name, fn] : tests) {
        fn();
        printf("ok  test_%s\n", name);
    }
    printf("%d tests passed\n", (int)size(tests));
}
