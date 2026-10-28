#pragma once
// Needs the includes and typedefs of lib/template.cpp (ll, vl, vi, pii, sz).

// ============================================================================
// Modular arithmetic
// ============================================================================

ll power(ll b, ll e, ll m) {
    ll r = 1;
    for (b %= m; e; e >>= 1, b = b * b % m)
        if (e & 1) r = r * b % m;
    return r;
}

// inv[i] = 1/i mod a prime m for i = 1..n (inv[0] = 0), in O(n).
vl inverses(int n, ll m) {
    vl inv(n + 1, 0);
    if (n >= 1) inv[1] = 1;
    for (int i = 2; i <= n; i++) inv[i] = (m - (m / i) * inv[m % i] % m) % m;
    return inv;
}

// ============================================================================
// Division by the Euler product prod_{k>=1} (1 - x^k) (pentagonal recurrence)
// ============================================================================

// First sz(a) coefficients of a / prod (1 - x^k) mod m, O(n sqrt n).
// h[i] = a[i] + sum over generalized pentagonal g = k(3k-1)/2, k(3k+1)/2 of
// (+h[i-g] for odd k, -h[i-g] for even k).
vl div_euler(const vl &a, ll m) {
    int n = sz(a);
    vl h(n);
    for (int i = 0; i < n; i++) {
        ll s = a[i] % m;
        for (ll k = 1;; k++) {
            ll g1 = k * (3 * k - 1) / 2, g2 = g1 + k;
            if (g1 > i) break;
            ll t = h[i - g1] + (g2 <= i ? h[i - g2] : 0);
            s += k & 1 ? t : m - t % m;
        }
        h[i] = s % m;
    }
    return h;
}

// p(0..n) mod m: number of partitions of each integer.
vl partitions(int n, ll m) {
    vl a(n + 1, 0);
    a[0] = 1;
    return div_euler(a, m);
}
