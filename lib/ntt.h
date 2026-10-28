#pragma once
// Needs the includes and typedefs of lib/template.cpp (ll, vl, vi, pii, sz).
#include "lib/modular.h"

// ============================================================================
// NTT: polynomial multiplication mod 998244353
// ============================================================================

const ll NTT_MOD = 998244353;  // 119 * 2^23 + 1, primitive root 3: sizes up to 2^23

void ntt(vl &a, bool invert) {
    int n = sz(a);
    for (int i = 1, j = 0; i < n; i++) {
        int bit = n >> 1;
        for (; j & bit; bit >>= 1) j ^= bit;
        j ^= bit;
        if (i < j) swap(a[i], a[j]);
    }
    for (int len = 2; len <= n; len <<= 1) {
        ll w = power(3, (NTT_MOD - 1) / len, NTT_MOD);
        if (invert) w = power(w, NTT_MOD - 2, NTT_MOD);
        vl ws(len / 2);
        ws[0] = 1;
        for (int i = 1; i < len / 2; i++) ws[i] = ws[i - 1] * w % NTT_MOD;
        for (int i = 0; i < n; i += len)
            for (int j = 0; j < len / 2; j++) {
                ll u = a[i + j], v = a[i + j + len / 2] * ws[j] % NTT_MOD;
                a[i + j] = u + v < NTT_MOD ? u + v : u + v - NTT_MOD;
                a[i + j + len / 2] = u - v >= 0 ? u - v : u - v + NTT_MOD;
            }
    }
    if (invert) {
        ll ni = power(n, NTT_MOD - 2, NTT_MOD);
        for (ll &x : a) x = x * ni % NTT_MOD;
    }
}

// a * b mod NTT_MOD; coefficients must be in [0, NTT_MOD).
vl multiply(vl a, vl b) {
    if (a.empty() || b.empty()) return {};
    int need = sz(a) + sz(b) - 1;
    if (min(sz(a), sz(b)) <= 32) {  // naive is faster for small inputs
        vl c(need, 0);
        for (int i = 0; i < sz(a); i++)
            for (int j = 0; j < sz(b); j++) c[i + j] = (c[i + j] + a[i] * b[j]) % NTT_MOD;
        return c;
    }
    int n = 1;
    while (n < need) n <<= 1;
    a.resize(n);
    b.resize(n);
    ntt(a, false);
    ntt(b, false);
    for (int i = 0; i < n; i++) a[i] = a[i] * b[i] % NTT_MOD;
    ntt(a, true);
    a.resize(need);
    return a;
}

// ============================================================================
// Series inverse: 1/f mod x^n (Newton), needs f[0] != 0
// ============================================================================

vl poly_inv(const vl &f, int n) {
    vl g = {power(f[0], NTT_MOD - 2, NTT_MOD)};
    for (int m = 1; m < n; m <<= 1) {
        int len = 4 * m;
        vl a(f.begin(), f.begin() + min(sz(f), 2 * m));
        a.resize(len);
        vl b = g;
        b.resize(len);
        ntt(a, false);
        ntt(b, false);
        for (int i = 0; i < len; i++) a[i] = b[i] * ((2 - a[i] * b[i] % NTT_MOD + NTT_MOD) % NTT_MOD) % NTT_MOD;
        ntt(a, true);
        a.resize(2 * m);
        g = a;
    }
    g.resize(n);
    return g;
}

// ============================================================================
// Online convolution (CDQ): f[i] depends on f[0..i-1]
// ============================================================================

// For i = 1..sz(f)-1 in order: f[i] += sum_{j=1..i} g[j] * f[i-j], then finish(i)
// may rewrite f[i] (e.g. divide by i) before later terms use it. O(n log^2 n).
void online_convolution(vl &f, const vl &g, const function<void(int)> &finish) {
    function<void(int, int)> go = [&](int l, int r) {
        if (r - l == 1) {
            if (l > 0) finish(l);
            return;
        }
        int mid = (l + r) / 2;
        go(l, mid);
        vl a(f.begin() + l, f.begin() + mid), b(g.begin(), g.begin() + min(sz(g), r - l));
        vl c = multiply(a, b);
        for (int i = mid; i < r && i - l < sz(c); i++) f[i] = (f[i] + c[i - l]) % NTT_MOD;
        go(mid, r);
    };
    if (!f.empty()) go(0, sz(f));
}
