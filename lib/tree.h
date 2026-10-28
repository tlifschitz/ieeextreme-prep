#pragma once
// Needs the includes and typedefs of lib/template.cpp (ll, vl, vi, pii, sz).

// ============================================================================
// Centroid decomposition
// ============================================================================

// anc[v] = (c, dist(v, c)) for every centroid ancestor c of v, top centroid first.
// adj: undirected forest on 0..n-1, adj[v] = {(u, w)}; W is the weight type (int, ll, double).
// Iterative, O(n log n). The unweighted overload below counts edges.
template <class W>
vector<vector<pair<int, W>>> centroid_ancestors(const vector<vector<pair<int, W>>> &adj) {
    int n = sz(adj);
    vector<vector<pair<int, W>>> anc(n);
    vector<char> removed(n, 0), seen(n, 0);
    vi par(n), size(n), order, stk;
    vector<W> dist(n);
    for (int start = 0; start < n; start++) {
        if (seen[start]) continue;
        stk.assign(1, start);
        while (!stk.empty()) {
            int r = stk.back();
            stk.pop_back();
            order.assign(1, r);  // component of r in the remaining forest
            par[r] = -1;
            for (int i = 0; i < sz(order); i++)
                for (auto [u, w] : adj[order[i]])
                    if (!removed[u] && u != par[order[i]]) par[u] = order[i], order.pb(u);
            int total = sz(order), c = r;
            for (int i = total - 1; i >= 0; i--) {
                int v = order[i], big = 0;
                size[v] = 1;
                for (auto [u, w] : adj[v])
                    if (!removed[u] && u != par[v]) size[v] += size[u], big = max(big, size[u]);
                if (max(big, total - size[v]) * 2 <= total) c = v;
            }
            order.assign(1, c);
            par[c] = -1, dist[c] = 0;
            for (int i = 0; i < sz(order); i++) {
                int v = order[i];
                anc[v].pb({c, dist[v]});
                seen[v] = 1;
                for (auto [u, w] : adj[v])
                    if (!removed[u] && u != par[v]) par[u] = v, dist[u] = dist[v] + w, order.pb(u);
            }
            removed[c] = 1;
            for (auto [u, w] : adj[c])
                if (!removed[u]) stk.pb(u);
        }
    }
    return anc;
}

vector<vector<pii>> centroid_ancestors(const vector<vi> &adj) {
    vector<vector<pii>> wadj(sz(adj));
    for (int v = 0; v < sz(adj); v++)
        for (int u : adj[v]) wadj[v].pb({u, 1});
    return centroid_ancestors(wadj);
}

// ============================================================================
// Rooted tree isomorphism (AHU): canonical subtree ids
// ============================================================================

// id[v] = id[u] iff the subtrees of v and u (rooted at the given roots) are isomorphic.
// Exact (sorted child-id lists in a map), iterative, O(n log n). Two trees: put both
// in one adj (offset the second) and pass both roots. Unrooted: root at the center(s).
vi rooted_iso_ids(const vector<vi> &adj, const vi &roots) {
    int n = sz(adj);
    vi par(n, -1), order(roots), id(n, -1), key;
    for (int r : roots) par[r] = r;
    for (int i = 0; i < sz(order); i++)
        for (int u : adj[order[i]])
            if (par[u] < 0) par[u] = order[i], order.pb(u);
    map<vi, int> ids;
    for (int i = sz(order) - 1; i >= 0; i--) {
        int v = order[i];
        key.clear();
        for (int u : adj[v])
            if (par[u] == v) key.pb(id[u]);
        sort(key.begin(), key.end());
        id[v] = ids.emplace(key, sz(ids)).first->second;
    }
    return id;
}
