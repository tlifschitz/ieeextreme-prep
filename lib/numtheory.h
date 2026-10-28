#pragma once
// Needs the includes and typedefs of lib/template.cpp (ll, vl, vi, sz).

// ============================================================================
// Sieve: smallest prime factor and primes up to n
// ============================================================================

struct Sieve {
    vi spf, primes;  // spf[x] = smallest prime factor of x (x >= 2)
    Sieve(int n) : spf(n + 1, 0) {
        for (int i = 2; i <= n; i++) {
            if (!spf[i]) spf[i] = i, primes.pb(i);
            for (int p : primes) {
                if (p > spf[i] || (ll)i * p > n) break;
                spf[i * p] = p;
            }
        }
    }
    vector<pii> factor(int x) {  // (prime, exponent), x <= n
        vector<pii> f;
        while (x > 1) {
            int p = spf[x], e = 0;
            while (x % p == 0) x /= p, e++;
            f.pb({p, e});
        }
        return f;
    }
};

// ============================================================================
// 64-bit modular arithmetic, Miller-Rabin, trial factorization
// ============================================================================

ll mulmod(ll a, ll b, ll m) { return (__int128)a * b % m; }

ll powmod(ll b, ll e, ll m) {  // works for m up to 2^63
    ll r = 1 % m;
    for (b %= m; e; e >>= 1, b = mulmod(b, b, m))
        if (e & 1) r = mulmod(r, b, m);
    return r;
}

bool is_prime(ll n) {  // deterministic for all 64-bit n
    if (n < 2) return false;
    for (ll p : {2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37})
        if (n % p == 0) return n == p;
    ll d = n - 1;
    int s = 0;
    while (d % 2 == 0) d /= 2, s++;
    for (ll a : {2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37}) {
        ll x = powmod(a, d, n);
        if (x == 1 || x == n - 1) continue;
        bool comp = true;
        for (int i = 1; i < s && comp; i++) {
            x = mulmod(x, x, n);
            if (x == n - 1) comp = false;
        }
        if (comp) return false;
    }
    return true;
}

vector<pair<ll, int>> factorize(ll n) {  // trial division, O(sqrt n)
    vector<pair<ll, int>> f;
    for (ll d = 2; d * d <= n; d += d == 2 ? 1 : 2)
        if (n % d == 0) {
            int e = 0;
            while (n % d == 0) n /= d, e++;
            f.pb({d, e});
        }
    if (n > 1) f.pb({n, 1});
    return f;
}

// ============================================================================
// Extended gcd and CRT
// ============================================================================

ll ext_gcd(ll a, ll b, ll &x, ll &y) {  // a x + b y = g
    if (!b) return x = 1, y = 0, a;
    ll g = ext_gcd(b, a % b, y, x);
    y -= a / b * x;
    return g;
}

// x = r1 (mod m1), x = r2 (mod m2) -> (x, lcm), or (-1, -1) if impossible. Moduli need not be coprime.
pll crt(ll r1, ll m1, ll r2, ll m2) {
    ll p, q, g = ext_gcd(m1, m2, p, q);
    if ((r2 - r1) % g) return {-1, -1};
    ll l = m1 / g * m2, k = (__int128)((r2 - r1) / g % (m2 / g)) * p % (m2 / g);
    ll x = ((r1 + (__int128)k * m1) % l + l) % l;
    return {x, l};
}

// ============================================================================
// Matrix power mod m and Gauss-Jordan elimination
// ============================================================================

typedef vector<vl> Mat;

Mat mat_mul(const Mat &A, const Mat &B, ll m) {
    int n = sz(A), k = sz(B), p = sz(B[0]);
    Mat C(n, vl(p, 0));
    for (int i = 0; i < n; i++)
        for (int t = 0; t < k; t++) {
            if (!A[i][t]) continue;
            for (int j = 0; j < p; j++) C[i][j] = (C[i][j] + A[i][t] * B[t][j]) % m;
        }
    return C;
}

Mat mat_pow(Mat A, ll e, ll m) {  // entries < m, m < 3e9 so products fit in ll
    int n = sz(A);
    Mat R(n, vl(n, 0));
    for (int i = 0; i < n; i++) R[i][i] = 1 % m;
    for (; e; e >>= 1, A = mat_mul(A, A, m))
        if (e & 1) R = mat_mul(R, A, m);
    return R;
}

// Gauss-Jordan mod prime p < 3e9 on rows M (entries in [0, p)), pivots in columns < m. Returns rank;
// det of M[:, :m] if square; x: M[:, :m] x = M[:, m] (free vars 0), empty if inconsistent.
int gauss(vector<vl> &M, int m, ll p, ll &det, vl &x) {
    int n = sz(M), r = 0;
    vi piv;
    det = 1;
    for (int c = 0; c < m && r < n; c++) {
        int k = r;
        while (k < n && !M[k][c]) k++;
        if (k == n) continue;
        swap(M[k], M[r]);
        ll v = M[r][c], iv = powmod(v, p - 2, p);
        det = det * (k == r ? v : p - v) % p;
        for (ll &w : M[r]) w = w * iv % p;
        for (int i = 0; i < n; i++)
            if (ll f = p - M[i][c]; i != r && f < p)
                for (int j = 0; j < sz(M[i]); j++) M[i][j] = (M[i][j] + f * M[r][j]) % p;
        piv.pb(c), r++;
    }
    if (r < m) det = 0;
    x.assign(m, 0);
    for (int i = 0; i < r; i++) x[piv[i]] = M[i][m];
    for (int i = r; i < n; i++) if (M[i][m]) x.clear();
    return r;
}

// ============================================================================
// XOR basis over GF(2) (optionally keeping the latest position per vector)
// ============================================================================

// insert(x, p): with increasing positions p, the span of the elements at positions >= l is
// {bas[b] : pos[b] >= l} (prefix-basis trick for range queries). Without positions it is a plain basis.
struct XorBasis {
    static const int B = 62;
    ll bas[B] = {}, pos[B] = {};
    int rank = 0;
    bool insert(ll x, ll p = 0) {
        for (int b = B - 1; b >= 0 && x; b--) {
            if (!(x >> b & 1)) continue;
            if (!bas[b]) { bas[b] = x, pos[b] = p, rank++; return true; }
            if (pos[b] < p) swap(bas[b], x), swap(pos[b], p);
            x ^= bas[b];
        }
        return false;
    }
    ll reduce(ll x) {  // 0 iff x is in the span
        for (int b = B - 1; b >= 0; b--) if (bas[b] && (x >> b & 1)) x ^= bas[b];
        return x;
    }
    ll max_xor(ll x = 0) {
        for (int b = B - 1; b >= 0; b--) if (bas[b] && !(x >> b & 1)) x ^= bas[b];
        return x;
    }
};
