#pragma once
// Needs the includes and typedefs of lib/template.cpp (ll, vl, vi, pii, sz).

// ============================================================================
// Disjoint sets (union by size, path halving)
// ============================================================================

// Next free slot >= x: when x is used set parent[x] = x + 1 (size n + 1), then find(x).
struct DSU {
    vi parent, size;
    int count;  // number of sets
    DSU(int n) : parent(n), size(n, 1), count(n) { iota(parent.begin(), parent.end(), 0); }
    int find(int x) {
        while (parent[x] != x) x = parent[x] = parent[parent[x]];
        return x;
    }
    bool unite(int a, int b) {  // false if already together
        a = find(a), b = find(b);
        if (a == b) return false;
        if (size[a] < size[b]) swap(a, b);
        parent[b] = a, size[a] += size[b], count--;
        return true;
    }
};

// ============================================================================
// Fenwick tree: point add, prefix sum (0-indexed)
// ============================================================================

struct Fenwick {
    int n;
    vl t;
    Fenwick(int n) : n(n), t(n + 1, 0) {}
    void add(int i, ll v) {
        for (i++; i <= n; i += i & -i) t[i] += v;
    }
    ll prefix(int i) {  // a[0..i-1]
        ll s = 0;
        for (; i > 0; i -= i & -i) s += t[i];
        return s;
    }
    ll range_sum(int l, int r) { return prefix(r) - prefix(l); }  // a[l..r-1]
    int lower_bound(ll k) {  // smallest i with prefix(i + 1) >= k, n if none (a >= 0): k-th smallest
        int p = 0;
        for (int s = 1 << __lg(n | 1); s; s >>= 1)
            if (p + s <= n && t[p + s] < k) k -= t[p += s];
        return p;
    }
};

// ============================================================================
// Segment tree: point set, fold over a[l..r-1] (iterative)
// ============================================================================

// Op: associative, e its identity. Example: SegTree<ll> t(a, [](ll x, ll y) { return min(x, y); }, LLONG_MAX);
template <class T>
struct SegTree {
    int n;
    vector<T> t;
    function<T(T, T)> op;
    T e;
    SegTree(const vector<T> &a, function<T(T, T)> op, T e) : n(sz(a)), t(2 * sz(a), e), op(op), e(e) {
        for (int i = 0; i < n; i++) t[n + i] = a[i];
        for (int i = n - 1; i > 0; i--) t[i] = op(t[2 * i], t[2 * i + 1]);
    }
    void set(int i, T v) {
        for (t[i += n] = v; i > 1; i >>= 1) t[i >> 1] = op(t[i & ~1], t[i | 1]);
    }
    T query(int l, int r) {  // keeps left-to-right order; e if l >= r
        T left = e, right = e;
        for (l += n, r += n; l < r; l >>= 1, r >>= 1) {
            if (l & 1) left = op(left, t[l++]);
            if (r & 1) right = op(t[--r], right);
        }
        return op(left, right);
    }
};

// ============================================================================
// Lazy segment tree: range add, range sum and min
// ============================================================================

struct LazySegTree {
    int n;
    vl sum, mn, lz;
    LazySegTree(const vl &a) : n(sz(a)), sum(4 * n), mn(4 * n), lz(4 * n, 0) { build(1, 0, n - 1, a); }
    void build(int o, int l, int r, const vl &a) {
        if (l == r) {
            sum[o] = mn[o] = a[l];
            return;
        }
        int m = (l + r) / 2;
        build(2 * o, l, m, a), build(2 * o + 1, m + 1, r, a);
        sum[o] = sum[2 * o] + sum[2 * o + 1], mn[o] = min(mn[2 * o], mn[2 * o + 1]);
    }
    void apply(int o, int len, ll v) { sum[o] += v * len, mn[o] += v, lz[o] += v; }
    void push(int o, int l, int r) {
        if (!lz[o]) return;
        int m = (l + r) / 2;
        apply(2 * o, m - l + 1, lz[o]), apply(2 * o + 1, r - m, lz[o]);
        lz[o] = 0;
    }
    void add(int o, int l, int r, int ql, int qr, ll v) {
        if (qr < l || r < ql) return;
        if (ql <= l && r <= qr) return apply(o, r - l + 1, v);
        push(o, l, r);
        int m = (l + r) / 2;
        add(2 * o, l, m, ql, qr, v), add(2 * o + 1, m + 1, r, ql, qr, v);
        sum[o] = sum[2 * o] + sum[2 * o + 1], mn[o] = min(mn[2 * o], mn[2 * o + 1]);
    }
    pll query(int o, int l, int r, int ql, int qr) {  // (sum, min)
        if (qr < l || r < ql) return {0, LLONG_MAX};
        if (ql <= l && r <= qr) return {sum[o], mn[o]};
        push(o, l, r);
        int m = (l + r) / 2;
        pll a = query(2 * o, l, m, ql, qr), b = query(2 * o + 1, m + 1, r, ql, qr);
        return {a.first + b.first, min(a.second, b.second)};
    }
    void add(int l, int r, ll v) { add(1, 0, n - 1, l, r, v); }  // inclusive, 0-indexed
    ll sum_of(int l, int r) { return query(1, 0, n - 1, l, r).first; }
    ll min_of(int l, int r) { return query(1, 0, n - 1, l, r).second; }
};

// ============================================================================
// Sparse table: O(1) static fold for idempotent op (min, max, gcd) over a[l..r-1]
// ============================================================================

struct Min {
    template <class T> T operator()(const T &a, const T &b) const { return min(a, b); }
};
struct Max {
    template <class T> T operator()(const T &a, const T &b) const { return max(a, b); }
};

// SparseTable<ll> t(a) folds with min, SparseTable<ll, Max> with max (a functor, so it inlines).
template <class T, class Op = Min>
struct SparseTable {
    vector<vector<T>> t;
    Op op;
    SparseTable(const vector<T> &a) : t(1, a) {
        for (int j = 1; 2 * j <= sz(a); j *= 2) {
            auto &p = t.back();
            vector<T> row(sz(p) - j);
            for (int i = 0; i < sz(row); i++) row[i] = op(p[i], p[i + j]);
            t.push_back(row);
        }
    }
    T query(int l, int r) {  // l < r
        int k = 31 - __builtin_clz(r - l);
        return op(t[k][l], t[k][r - (1 << k)]);
    }
};
