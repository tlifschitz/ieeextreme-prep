from collections import deque
from heapq import heappush, heappop


def topo_sort_min(n, adj, key):
    """Kahn's algorithm always taking the available node with the smallest
    (key[v], v). Returns the order, or None if there is a cycle."""
    indeg = [0] * n
    for v in range(n):
        for u in adj[v]:
            indeg[u] += 1
    pq = []
    for v in range(n):
        if indeg[v] == 0:
            heappush(pq, (key[v], v))
    order = []
    while pq:
        _, v = heappop(pq)
        order.append(v)
        for u in adj[v]:
            indeg[u] -= 1
            if indeg[u] == 0:
                heappush(pq, (key[u], u))
    return order if len(order) == n else None


def tree_orders(adj, root):
    """Iterative DFS of a tree from root, children in adj order.
    Returns (parent, preorder, postorder); parent[root] = -1, and nodes
    not reachable from root also keep -1."""
    n = len(adj)
    parent = [-1] * n
    it = [0] * n
    pre, post = [root], []
    stack = [root]
    while stack:
        v = stack[-1]
        if it[v] < len(adj[v]):
            u = adj[v][it[v]]
            it[v] += 1
            if u != parent[v]:
                parent[u] = v
                pre.append(u)
                stack.append(u)
        else:
            stack.pop()
            post.append(v)
    return parent, pre, post


def subtree_sizes(parent, post):
    """Subtree sizes from tree_orders' parent and postorder."""
    size = [0] * len(parent)
    for v in post:
        size[v] += 1
        if parent[v] != -1:
            size[parent[v]] += size[v]
    return size


def subtree_ids(parent, post):
    """AHU: ids[u] == ids[v] iff the rooted subtrees of u and v are isomorphic (dense ids 0, 1, ...).
    post lists children before parents (tree_orders' postorder; for a forest, any such order).
    To compare trees, put them in one forest. O(n log n)."""
    kids = [[] for _ in parent]
    ids, res = {}, [0] * len(parent)
    for v in post:
        k = kids[v]
        k.sort()
        res[v] = ids.setdefault(tuple(k), len(ids))
        kids[v] = None
        if parent[v] >= 0:
            kids[parent[v]].append(res[v])
    return res


def bridges(n, us, vs):
    """Indices of the bridges of the multigraph on 0..n-1 with edges (us[i], vs[i]).
    Stack DFS marking on pop (same tree as recursive DFS, so every non-tree
    edge joins an ancestor and a descendant); a tree edge is a bridge iff no
    such edge jumps over it."""
    m = len(us)
    tgt = [0] * (2 * m)  # half-edge h = 2e or 2e+1 of edge e points to tgt[h]
    tgt[0::2] = vs
    tgt[1::2] = us
    adj = [[] for _ in range(n)]
    for h, a, b in zip(range(0, 2 * m, 2), us, vs):
        adj[a].append(h)
        adj[b].append(h + 1)
    tin = [-1] * n
    pe = [-1] * n  # edge to the dfs parent
    order = []
    for s in range(n):
        if tin[s] >= 0:
            continue
        tin[s] = len(order)
        order.append(s)
        stack = adj[s][:]
        while stack:
            h = stack.pop()
            w = tgt[h]
            if tin[w] < 0:
                tin[w] = len(order)
                order.append(w)
                pe[w] = h
                stack += adj[w]
    cover = [0] * n  # +1 at the lower end of each back edge, -1 at the upper end
    tree = [False] * m
    for h in pe:
        if h >= 0:
            tree[h >> 1] = True
    for t, a, b in zip(tree, us, vs):
        if not t:
            if tin[a] < tin[b]:
                a, b = b, a
            cover[a] += 1
            cover[b] -= 1
    res = []
    for w in reversed(order):  # cover[w] becomes the subtree sum
        h = pe[w]
        if h >= 0:
            if cover[w] == 0:
                res.append(h >> 1)
            cover[tgt[h ^ 1]] += cover[w]
    return res


def biconnected_blocks(n, adj):
    """Vertex-biconnected blocks as lists of vertices (a bridge is a block of 2; isolated vertices
    are in no block), and one root vertex per connected component. Iterative Tarjan, O(n + m);
    multi-edges and self-loops are fine."""
    tin = [-1] * n
    low = [0] * n
    it = [iter(a) for a in adj]
    blocks, roots = [], []
    t = 0
    for s in range(n):
        if tin[s] >= 0:
            continue
        roots.append(s)
        tin[s] = low[s] = t
        t += 1
        stk = [s]
        call = [s]
        while call:
            v = call[-1]
            w = next(it[v], -1)
            if w >= 0:
                if tin[w] < 0:
                    tin[w] = low[w] = t
                    t += 1
                    stk.append(w)
                    call.append(w)
                elif tin[w] < low[v]:
                    low[v] = tin[w]
            else:
                call.pop()
                if call:
                    p = call[-1]
                    if low[v] < low[p]:
                        low[p] = low[v]
                    if low[v] >= tin[p]:  # p separates v's subtree: pop a block
                        blk = [p]
                        while True:
                            x = stk.pop()
                            blk.append(x)
                            if x == v:
                                break
                        blocks.append(blk)
    return blocks, roots


def block_cut_tree(n, blocks):
    """Block-cut forest: nodes 0..n-1 are the vertices, n + i is blocks[i], joined to its vertices.
    The articulation points are the v < n with len(tree[v]) > 1."""
    tree = [[] for _ in range(n)]
    for blk in blocks:
        b = len(tree)
        tree.append(blk)
        for x in blk:
            tree[x].append(b)
    return tree


def bfs(adj, src):
    """Unweighted distances from src (or a list of sources); -1 if unreachable."""
    dist = [-1] * len(adj)
    q = list(src) if isinstance(src, list) else [src]
    for s in q:
        dist[s] = 0
    for v in q:  # the list grows while we iterate: a queue without popleft
        d = dist[v] + 1
        for u in adj[v]:
            if dist[u] < 0:
                dist[u] = d
                q.append(u)
    return dist


def dijkstra(adj, src):
    """Shortest distances from src (or a list of sources) over adj[v] = [(u, w), ...],
    w >= 0; INF = float('inf') if unreachable. Returns (dist, parent)."""
    INF = float("inf")
    dist = [INF] * len(adj)
    parent = [-1] * len(adj)
    heap = []
    for s in src if isinstance(src, list) else [src]:
        dist[s] = 0
        heap.append((0, s))
    while heap:
        d, v = heappop(heap)
        if d > dist[v]:
            continue
        for u, w in adj[v]:
            nd = d + w
            if nd < dist[u]:
                dist[u] = nd
                parent[u] = v
                heappush(heap, (nd, u))
    return dist, parent


class LCA:
    """O(1) LCA queries: range minimum of (depth, vertex) over the preorder.
    For tin[a] < tin[b], lca = parent of the shallowest vertex at preorder positions (tin[a], tin[b]]."""

    def __init__(self, adj, root):
        parent, pre, _ = tree_orders(adj, root)
        self.parent, self.pre, self.depth = parent, pre, tree_depths(parent, pre)
        self.tin = tin = [0] * len(adj)
        for i, v in enumerate(pre):
            tin[v] = i
        depth = self.depth
        self.t = t = [[depth[v] << 21 | v for v in pre]]  # sparse table of min, n < 2^21
        j = 1
        while 2 * j <= len(pre):
            prev = t[-1]
            t.append(list(map(min, prev[: len(prev) - j], prev[j:])))
            j *= 2

    def lca(self, a, b):
        if a == b:
            return a
        l, r = self.tin[a], self.tin[b]
        if l > r:
            l, r = r, l
        k = (r - l).bit_length() - 1  # min over preorder positions l+1..r
        row = self.t[k]
        return self.parent[min(row[l + 1], row[r + 1 - (1 << k)]) & 0x1FFFFF]

    def dist(self, a, b):
        return self.depth[a] + self.depth[b] - 2 * self.depth[self.lca(a, b)]


def kruskal_reconstruction(n, edges):
    """Kruskal reconstruction tree of edges (w, u, v) taken in the given order (sort ascending for
    the minimax path, descending for the maximin). Leaves 0..n-1; node n + i is the i-th edge that
    joined two components, with its w. Returns (parent, weight): parent[v] > v, -1 at roots.
    Bottleneck of u..v = weight[lca(u, v)] (connected: LCA(children lists, len(parent) - 1)); the
    leaves under an ancestor of u are what u reaches using edges up to its weight. O(m log n)."""
    par, wt, d = [-1] * n, [0] * n, list(range(n))  # d: DSU over tree nodes, root = topmost node
    for w, u, v in edges:
        while d[u] != u:
            d[u] = u = d[d[u]]
        while d[v] != v:
            d[v] = v = d[d[v]]
        if u != v:
            k = len(par)
            par[u] = par[v] = d[u] = d[v] = k
            par.append(-1)
            wt.append(w)
            d.append(k)
    return par, wt


def tree_depths(parent, pre):
    """depth[v] from parent and a preorder (as returned by tree_orders)."""
    depth = [0] * len(parent)
    for v in pre:
        if parent[v] >= 0:
            depth[v] = depth[parent[v]] + 1
    return depth


class MaxFlow:
    """Dinic. add_edge(u, v, cap) returns the edge id; flow(s, t) the max flow;
    edge_flow(id) the flow on that edge afterwards."""

    def __init__(self, n):
        self.n = n
        self.adj = [[] for _ in range(n)]
        self.to, self.cap = [], []

    def add_edge(self, u, v, cap):
        e = len(self.to)
        self.to += [v, u]
        self.cap += [cap, 0]
        self.adj[u].append(e)
        self.adj[v].append(e + 1)
        return e

    def edge_flow(self, e):
        return self.cap[e + 1]

    def flow(self, s, t):
        adj, to, cap, n = self.adj, self.to, self.cap, self.n
        total = 0
        while True:
            level = [-1] * n
            level[s] = 0
            q = deque([s])
            while q:
                v = q.popleft()
                for e in adj[v]:
                    if cap[e] and level[to[e]] < 0:
                        level[to[e]] = level[v] + 1
                        q.append(to[e])
            if level[t] < 0:
                return total
            it = [0] * n
            while True:  # iterative blocking-flow DFS
                stack, path = [s], []
                pushed = 0
                while stack:
                    v = stack[-1]
                    if v == t:
                        f = min(cap[e] for e in path)
                        for e in path:
                            cap[e] -= f
                            cap[e ^ 1] += f
                        pushed = f
                        break
                    while it[v] < len(adj[v]):
                        e = adj[v][it[v]]
                        if cap[e] and level[to[e]] == level[v] + 1:
                            break
                        it[v] += 1
                    if it[v] == len(adj[v]):
                        level[v] = -1  # dead end
                        stack.pop()
                        if path:
                            path.pop()
                            it[stack[-1]] += 1
                    else:
                        e = adj[v][it[v]]
                        stack.append(to[e])
                        path.append(e)
                if not pushed:
                    break
                total += pushed


def bipartite_matching(n_left, n_right, adj):
    """Maximum matching, adj[l] = right vertices of left l (Hopcroft-Karp).
    Returns (size, match_left) with match_left[l] = right vertex or -1."""
    INF = float("inf")
    ml, mr = [-1] * n_left, [-1] * n_right
    size = 0
    while True:
        dist = [INF] * n_left
        q = deque()
        for l in range(n_left):
            if ml[l] < 0:
                dist[l] = 0
                q.append(l)
        found = False
        while q:
            l = q.popleft()
            for r in adj[l]:
                m = mr[r]
                if m < 0:
                    found = True
                elif dist[m] == INF:
                    dist[m] = dist[l] + 1
                    q.append(m)
        if not found:
            return size, ml
        it = [0] * n_left
        for root in range(n_left):
            if ml[root] >= 0:
                continue
            stack = [root]
            while stack:  # iterative augmenting-path DFS along dist layers
                l = stack[-1]
                if it[l] == len(adj[l]):
                    dist[l] = INF
                    stack.pop()
                    continue
                r = adj[l][it[l]]
                it[l] += 1
                m = mr[r]
                if m < 0:
                    for l2 in reversed(stack):  # flip the path
                        r2 = adj[l2][it[l2] - 1]
                        ml[l2], mr[r2] = r2, l2
                    size += 1
                    break
                if dist[m] == dist[l] + 1:
                    stack.append(m)


def scc(adj):
    """Iterative Tarjan, O(n + m). (k, comp): comp[v] in [0, k), topological order of the
    condensation (u -> v: comp[u] <= comp[v])."""
    n = len(adj)
    tin, low = [-1] * n, [0] * n
    it = [iter(a) for a in adj]
    t = k = 0
    for s in range(n):
        if tin[s] < 0:
            tin[s] = low[s] = t = t + 1
            stk, call = [s], [s]
        while call:
            v = call[-1]
            u = next(it[v], -1)
            if u < 0:
                call.pop()
                if call and low[v] < low[call[-1]]:
                    low[call[-1]] = low[v]
                if low[v] == tin[v]:
                    while u != v:
                        u = stk.pop()
                        low[u] = n + k
                    k += 1
            elif tin[u] < 0:
                tin[u] = low[u] = t = t + 1
                stk.append(u)
                call.append(u)
            elif low[u] < low[v]:
                low[v] = low[u]
    return k, [n + k - 1 - c for c in low]


def two_sat(n, clauses):
    """Literal 2i = x_i, 2i+1 = not x_i (negate: ^ 1); clause (a, b) = (a or b).
    Returns n satisfying bools, or None."""
    g = [[] for _ in range(2 * n)]
    for a, b in clauses:
        g[a ^ 1].append(b)
        g[b ^ 1].append(a)
    c = scc(g)[1]
    x = [c[i] > c[i + 1] for i in range(0, 2 * n, 2)]
    return None if any(c[i] == c[i ^ 1] for i in range(2 * n)) else x
