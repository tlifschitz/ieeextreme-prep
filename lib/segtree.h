#pragma once
// Needs the includes and typedefs of lib/template.cpp (ll, vl, vi, pii, sz).

// ============================================================================
// Segment tree beats: range assign, range chmax, range sum and min
// ============================================================================

// a[i] = max(a[i], c) on a range in amortized O(log^2 n); all ops 0-indexed, inclusive.
// To keep other data per node (e.g. power sums), change apply_assign, apply_min and pull.
struct Beats {
    static constexpr ll INF = LLONG_MAX;
    int n;
    vl mn, smn, cnt, tg, sum, len;  // min, second min, count of min, assign tag (-1: none)

    Beats(const vl &a) : n(sz(a)), mn(4 * n), smn(4 * n), cnt(4 * n), tg(4 * n, -1), sum(4 * n), len(4 * n) {
        build(1, 0, n - 1, a);
    }

    void apply_assign(int o, ll c) {
        mn[o] = c, smn[o] = INF, cnt[o] = len[o], tg[o] = c, sum[o] = c * len[o];
    }
    void apply_min(int o, ll c) {  // raise the minimum elements to c (mn < c < smn)
        sum[o] += (c - mn[o]) * cnt[o];
        mn[o] = c;
    }
    void pull(int o) {
        int l = 2 * o, r = 2 * o + 1;
        if (mn[l] == mn[r]) mn[o] = mn[l], cnt[o] = cnt[l] + cnt[r], smn[o] = min(smn[l], smn[r]);
        else if (mn[l] < mn[r]) mn[o] = mn[l], cnt[o] = cnt[l], smn[o] = min(smn[l], mn[r]);
        else mn[o] = mn[r], cnt[o] = cnt[r], smn[o] = min(mn[l], smn[r]);
        sum[o] = sum[l] + sum[r];
    }
    void push(int o) {
        for (int c = 2 * o; c <= 2 * o + 1; c++) {
            if (tg[o] >= 0) apply_assign(c, tg[o]);
            if (mn[c] < mn[o]) apply_min(c, mn[o]);
        }
        tg[o] = -1;
    }
    void build(int o, int l, int r, const vl &a) {
        len[o] = r - l + 1;
        if (l == r) {
            apply_assign(o, a[l]);
            tg[o] = -1;
            return;
        }
        int m = (l + r) / 2;
        build(2 * o, l, m, a), build(2 * o + 1, m + 1, r, a);
        pull(o);
    }
    void assign(int o, int l, int r, int ql, int qr, ll c) {
        if (qr < l || r < ql) return;
        if (ql <= l && r <= qr) return apply_assign(o, c);
        push(o);
        int m = (l + r) / 2;
        assign(2 * o, l, m, ql, qr, c), assign(2 * o + 1, m + 1, r, ql, qr, c);
        pull(o);
    }
    void chmax(int o, int l, int r, int ql, int qr, ll c) {
        if (qr < l || r < ql || mn[o] >= c) return;
        if (ql <= l && r <= qr && c < smn[o]) return apply_min(o, c);
        push(o);
        int m = (l + r) / 2;
        chmax(2 * o, l, m, ql, qr, c), chmax(2 * o + 1, m + 1, r, ql, qr, c);
        pull(o);
    }
    pll query(int o, int l, int r, int ql, int qr) {  // (sum, min)
        if (qr < l || r < ql) return {0, INF};
        if (ql <= l && r <= qr) return {sum[o], mn[o]};
        push(o);
        int m = (l + r) / 2;
        pll a = query(2 * o, l, m, ql, qr), b = query(2 * o + 1, m + 1, r, ql, qr);
        return {a.first + b.first, min(a.second, b.second)};
    }

    void assign(int l, int r, ll c) { assign(1, 0, n - 1, l, r, c); }  // values must be >= 0
    void chmax(int l, int r, ll c) { chmax(1, 0, n - 1, l, r, c); }
    ll sum_of(int l, int r) { return query(1, 0, n - 1, l, r).first; }
    ll min_of(int l, int r) { return query(1, 0, n - 1, l, r).second; }
};
