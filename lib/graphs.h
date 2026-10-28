#pragma once
// Needs the includes and typedefs of lib/template.cpp (ll, vl, vi, pii, sz).

// ============================================================================
// BFS and Dijkstra
// ============================================================================

vi bfs(const vector<vi> &adj, vi src) {  // -1 if unreachable
    vi dist(sz(adj), -1);
    queue<int> q;
    for (int s : src) dist[s] = 0, q.push(s);
    while (!q.empty()) {
        int v = q.front();
        q.pop();
        for (int u : adj[v])
            if (dist[u] < 0) dist[u] = dist[v] + 1, q.push(u);
    }
    return dist;
}

const ll INF_DIST = LLONG_MAX / 4;  // "unreachable" in dijkstra

// adj[v] = {(u, w)}, w >= 0. dist = INF_DIST if unreachable; parent[v] = previous vertex or -1.
pair<vl, vi> dijkstra(const vector<vector<pair<int, ll>>> &adj, vi src) {
    vl dist(sz(adj), INF_DIST);
    vi parent(sz(adj), -1);
    priority_queue<pair<ll, int>, vector<pair<ll, int>>, greater<>> pq;
    for (int s : src) dist[s] = 0, pq.push({0, s});
    while (!pq.empty()) {
        auto [d, v] = pq.top();
        pq.pop();
        if (d > dist[v]) continue;
        for (auto [u, w] : adj[v])
            if (d + w < dist[u]) dist[u] = d + w, parent[u] = v, pq.push({dist[u], u});
    }
    return {dist, parent};
}

// ============================================================================
// Tree DFS: parent, depth, preorder (tin in [0, n)), subtree end (tout)
// ============================================================================

// Iterative. order = preorder (parents before children); the subtree of v is
// order[tin[v] .. tout[v]-1], so tin indexes a Fenwick / segment tree over the tree.
struct TreeDFS {
    vi par, dep, tin, tout, order;
    TreeDFS(const vector<vi> &adj, int root) : par(sz(adj), -1), dep(sz(adj)), tin(sz(adj)), tout(sz(adj)) {
        int n = sz(adj);
        vi it(n, 0), st = {root};
        order.reserve(n);
        tin[root] = 0, order.pb(root);
        while (!st.empty()) {
            int v = st.back();
            if (it[v] < sz(adj[v])) {
                int u = adj[v][it[v]++];
                if (u == par[v]) continue;
                par[u] = v, dep[u] = dep[v] + 1, tin[u] = sz(order), order.pb(u), st.pb(u);
            } else {
                tout[v] = sz(order);
                st.pop_back();
            }
        }
    }
    bool is_ancestor(int a, int b) { return tin[a] <= tin[b] && tin[b] < tout[a]; }  // a above or equal b
};

// ============================================================================
// LCA (binary lifting over TreeDFS)
// needs: Tree DFS
// ============================================================================

struct LCA : TreeDFS {
    int LOG = 1;
    vector<vi> up;  // up[k][v] = 2^k-th ancestor (the root maps to itself)
    LCA(const vector<vi> &adj, int root) : TreeDFS(adj, root) {
        int n = sz(adj);
        while ((1 << LOG) < n) LOG++;
        up.assign(LOG + 1, vi(n, root));
        for (int v = 0; v < n; v++) if (par[v] >= 0) up[0][v] = par[v];
        for (int k = 1; k <= LOG; k++)
            for (int v = 0; v < n; v++) up[k][v] = up[k - 1][up[k - 1][v]];
    }
    int lca(int a, int b) {
        if (is_ancestor(a, b)) return a;
        if (is_ancestor(b, a)) return b;
        for (int k = LOG; k >= 0; k--)
            if (!is_ancestor(up[k][a], b)) a = up[k][a];
        return up[0][a];
    }
    int dist(int a, int b) { return dep[a] + dep[b] - 2 * dep[lca(a, b)]; }
};

// ============================================================================
// Max flow (Dinic) and min-cost flow
// ============================================================================

struct MaxFlow {
    struct E { int to; ll cap; };
    vector<E> e;
    vector<vi> g;
    vi level, it;
    MaxFlow(int n) : g(n), level(n), it(n) {}
    int add_edge(int u, int v, ll cap) {  // returns edge id; flow on it: e[id ^ 1].cap
        g[u].pb(sz(e)), e.pb({v, cap});
        g[v].pb(sz(e)), e.pb({u, 0});
        return sz(e) - 2;
    }
    bool bfs_levels(int s, int t) {
        fill(level.begin(), level.end(), -1);
        queue<int> q;
        level[s] = 0, q.push(s);
        while (!q.empty()) {
            int v = q.front();
            q.pop();
            for (int id : g[v])
                if (e[id].cap > 0 && level[e[id].to] < 0) level[e[id].to] = level[v] + 1, q.push(e[id].to);
        }
        return level[t] >= 0;
    }
    ll dfs(int v, int t, ll f) {
        if (v == t) return f;
        for (int &i = it[v]; i < sz(g[v]); i++) {
            int id = g[v][i], u = e[id].to;
            if (e[id].cap > 0 && level[u] == level[v] + 1) {
                ll d = dfs(u, t, min(f, e[id].cap));
                if (d > 0) {
                    e[id].cap -= d, e[id ^ 1].cap += d;
                    return d;
                }
            }
        }
        return 0;
    }
    ll flow(int s, int t) {
        ll total = 0;
        while (bfs_levels(s, t)) {
            fill(it.begin(), it.end(), 0);
            while (ll f = dfs(s, t, LLONG_MAX)) total += f;
        }
        return total;
    }
};

// SPFA, no negative cycles. flow(s, t, lim): up to lim units at min cost -> (flow, cost).
struct MCMF {
    struct E { int to; ll cap, cost; };
    vector<E> e;
    vector<vi> g;
    MCMF(int n) : g(n) {}
    int add_edge(int u, int v, ll cap, ll cost) {
        g[u].pb(sz(e)), e.pb({v, cap, cost});
        g[v].pb(sz(e)), e.pb({u, 0, -cost});
        return sz(e) - 2;
    }
    pll flow(int s, int t, ll lim = LLONG_MAX) {
        ll f = 0, c = 0;
        while (f < lim) {
            vl d(sz(g), LLONG_MAX), b(sz(g), lim - f);
            vi pe(sz(g)), inq(sz(g));
            deque<int> q = {s};
            for (d[s] = 0; !q.empty(); q.pop_front()) {
                int v = q.front();
                inq[v] = 0;
                for (int id : g[v])
                    if (E &x = e[id]; x.cap && d[v] + x.cost < d[x.to]) {
                        d[x.to] = d[v] + x.cost, pe[x.to] = id, b[x.to] = min(b[v], x.cap);
                        if (!inq[x.to]) inq[x.to] = 1, q.pb(x.to);
                    }
            }
            if (d[t] == LLONG_MAX) break;
            for (int v = t; v != s; v = e[pe[v] ^ 1].to) e[pe[v]].cap -= b[t], e[pe[v] ^ 1].cap += b[t];
            f += b[t], c += b[t] * d[t];
        }
        return {f, c};
    }
};

// ============================================================================
// Bipartite matching (Hopcroft-Karp)
// ============================================================================

struct BipartiteMatching {
    int nl, nr;
    vector<vi> adj;  // adj[l] = right vertices
    vi ml, mr, dist;
    BipartiteMatching(int nl, int nr) : nl(nl), nr(nr), adj(nl), ml(nl, -1), mr(nr, -1), dist(nl) {}
    void add_edge(int l, int r) { adj[l].pb(r); }
    bool bfs() {
        queue<int> q;
        bool found = false;
        for (int l = 0; l < nl; l++) dist[l] = ml[l] < 0 ? 0 : -1;
        for (int l = 0; l < nl; l++) if (ml[l] < 0) q.push(l);
        while (!q.empty()) {
            int l = q.front();
            q.pop();
            for (int r : adj[l]) {
                int m = mr[r];
                if (m < 0) found = true;
                else if (dist[m] < 0) dist[m] = dist[l] + 1, q.push(m);
            }
        }
        return found;
    }
    bool dfs(int l) {
        for (int r : adj[l]) {
            int m = mr[r];
            if (m < 0 || (dist[m] == dist[l] + 1 && dfs(m))) {
                ml[l] = r, mr[r] = l;
                return true;
            }
        }
        dist[l] = -1;
        return false;
    }
    int solve() {  // size of a maximum matching; ml / mr hold it
        int size = 0;
        while (bfs())
            for (int l = 0; l < nl; l++)
                if (ml[l] < 0 && dfs(l)) size++;
        return size;
    }
};

// ============================================================================
// Hungarian algorithm: min-cost assignment, O(n^2 m)
// ============================================================================

// a: n x m cost matrix, n <= m (any sign; T = ll or double). Returns (cost, col):
// row i gets column col[i], columns distinct. For max cost, negate a.
template <class T>
pair<T, vi> hungarian(const vector<vector<T>> &a) {
    int n = sz(a), m = n ? sz(a[0]) : 0;
    const T INF = numeric_limits<T>::max() / 4;
    vector<T> u(n + 1), v(m + 1);
    vi p(m + 1), way(m + 1);  // p[j]: row on column j, 1-based, 0 = free
    for (int i = 1; i <= n; i++) {
        p[0] = i;
        int j0 = 0;
        vector<T> minv(m + 1, INF);
        vector<char> used(m + 1, 0);
        do {
            used[j0] = 1;
            int i0 = p[j0], j1 = 0;
            T delta = INF;
            for (int j = 1; j <= m; j++)
                if (!used[j]) {
                    T cur = a[i0 - 1][j - 1] - u[i0] - v[j];
                    if (cur < minv[j]) minv[j] = cur, way[j] = j0;
                    if (minv[j] < delta) delta = minv[j], j1 = j;
                }
            for (int j = 0; j <= m; j++)
                if (used[j]) u[p[j]] += delta, v[j] -= delta;
                else minv[j] -= delta;
            j0 = j1;
        } while (p[j0]);
        do {
            int j1 = way[j0];
            p[j0] = p[j1];
            j0 = j1;
        } while (j0);
    }
    vi col(n);
    T cost = 0;
    for (int j = 1; j <= m; j++)
        if (p[j]) col[p[j] - 1] = j - 1, cost += a[p[j] - 1][j - 1];
    return {cost, col};
}

// ============================================================================
// Kruskal reconstruction tree
// ============================================================================

// Leaves 0..n-1 are the vertices; Kruskal (ascending w) adds a node per merge with
// w = that edge, so w[lca(a, b)] = min over a-b paths of the max edge (bottleneck),
// and the leaves under a node are a component of the edges with weight <= its w.
// Maximin: negate the weights. Components are joined under a last node with w = LLONG_MAX.
// Use with LCA(kt.adj, kt.root); leaves have w = 0.
struct KruskalTree {
    vector<vi> adj;
    vl w;
    int root;
    KruskalTree(int n, vector<tuple<ll, int, int>> edges) : adj(n), w(n, 0) {  // edges (w, u, v)
        sort(edges.begin(), edges.end());
        vi dsu(n);
        iota(dsu.begin(), dsu.end(), 0);
        auto find = [&](int x) {
            while (dsu[x] != x) x = dsu[x] = dsu[dsu[x]];
            return x;
        };
        auto node = [&](ll c, const vi &kids) {
            int z = sz(adj);
            adj.pb(kids), w.pb(c), dsu.pb(z);
            for (int x : kids) adj[x].pb(z), dsu[x] = z;
            return z;
        };
        for (auto [c, a, b] : edges)
            if ((a = find(a)) != (b = find(b))) node(c, {a, b});
        vi tops;
        for (int x = 0; x < sz(adj); x++) if (dsu[x] == x) tops.pb(x);
        root = sz(tops) == 1 ? tops[0] : node(LLONG_MAX, tops);
    }
};

// ============================================================================
// SCC (iterative Tarjan) and 2-SAT
// ============================================================================

// (k, comp): comp[v] in [0, k), topological order of the condensation (u -> v: comp[u] <= comp[v]).
pair<int, vi> scc(const vector<vi> &g) {
    int n = sz(g), t = 0, k = 0;
    vi tin(n, -1), low(n), it(n), stk, call;
    for (int s = 0; s < n; s++) {
        if (tin[s] < 0) tin[s] = low[s] = t++, stk = call = {s};
        while (!call.empty()) {
            int v = call.back(), u;
            if (it[v] < sz(g[v])) {
                if (tin[u = g[v][it[v]++]] < 0) tin[u] = low[u] = t++, stk.pb(u), call.pb(u);
                else low[v] = min(low[v], low[u]);
                continue;
            }
            call.pop_back();
            if (!call.empty()) low[call.back()] = min(low[call.back()], low[v]);
            if (low[v] == tin[v]) {
                do u = stk.back(), stk.pop_back(), low[u] = n + k; while (u != v);
                k++;
            }
        }
    }
    for (int &c : low) c = n + k - 1 - c;
    return {k, low};
}

// Literal 2i = x_i, 2i+1 = not x_i (negate: ^ 1); clause {a, b} = (a or b). Returns x, or {} if unsat.
vector<bool> two_sat(int n, const vector<pii> &clauses) {
    vector<vi> g(2 * n);
    for (auto [a, b] : clauses) g[a ^ 1].pb(b), g[b ^ 1].pb(a);
    vi c = scc(g).second;
    vector<bool> x;
    for (int i = 0; i < 2 * n; i += 2)
        if (c[i] == c[i + 1]) return {};
        else x.pb(c[i] > c[i + 1]);
    return x;
}
