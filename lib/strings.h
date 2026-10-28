#pragma once
// Needs the includes and typedefs of lib/template.cpp (ll, vi, sz).

// ============================================================================
// KMP prefix function, Z function, suffix array
// ============================================================================

vi prefix_function(const string &s) {  // pi[i] = longest proper border of s[0..i]
    vi pi(sz(s), 0);
    for (int i = 1, k = 0; i < sz(s); i++) {
        while (k && s[i] != s[k]) k = pi[k - 1];
        if (s[i] == s[k]) k++;
        pi[i] = k;
    }
    return pi;
}

vi find_all(const string &text, const string &pat) {  // starts of every occurrence (pat non-empty)
    vi pi = prefix_function(pat), res;
    for (int i = 0, k = 0; i < sz(text); i++) {
        while (k && text[i] != pat[k]) k = pi[k - 1];
        if (text[i] == pat[k]) k++;
        if (k == sz(pat)) res.pb(i - k + 1), k = pi[k - 1];
    }
    return res;
}

vi z_function(const string &s) {  // z[i] = LCP of s and s[i..], z[0] = n
    int n = sz(s);
    vi z(n, 0);
    if (n) z[0] = n;
    for (int i = 1, l = 0, r = 0; i < n; i++) {
        if (i < r) z[i] = min(r - i, z[i - l]);
        while (i + z[i] < n && s[z[i]] == s[i + z[i]]) z[i]++;
        if (i + z[i] > r) l = i, r = i + z[i];
    }
    return z;
}

// O(n log^2 n) doubling; s: string or vi. {sa, lcp}: sorted suffix starts, lcp[i] = LCP of sa[i], sa[i+1].
template <class S> pair<vi, vi> suffix_array(const S &s) {
    int n = sz(s), k = 0;
    vi sa(n), r(begin(s), end(s)), t(n), lcp(max(n - 1, 0));
    iota(begin(sa), end(sa), 0);
    for (int h = 1; n; h *= 2) {
        auto cmp = [&](int a, int b) {
            return pii(r[a], a + h < n ? r[a + h] : INT_MIN) < pii(r[b], b + h < n ? r[b + h] : INT_MIN);
        };
        sort(begin(sa), end(sa), cmp);
        for (int i = 0; i < n; i++) t[sa[i]] = i ? t[sa[i - 1]] + cmp(sa[i - 1], sa[i]) : 0;
        if ((r = t)[sa[n - 1]] == n - 1) break;
    }
    for (int i = 0; i < n; i++, k -= k > 0)
        if (r[i] < n - 1) {
            int j = sa[r[i] + 1];
            while (max(i, j) + k < n && s[i + k] == s[j + k]) k++;
            lcp[r[i]] = k;
        } else k = 0;
    return {sa, lcp};
}

// ============================================================================
// Polynomial hashing mod 2^61 - 1
// ============================================================================

struct Hash {
    static constexpr unsigned long long M = (1ULL << 61) - 1, B = 911382323;  // fixed base
    vector<unsigned long long> h, p;
    static unsigned long long mul(unsigned long long a, unsigned long long b) {
        unsigned __int128 c = (unsigned __int128)a * b;
        unsigned long long r = (unsigned long long)(c & M) + (unsigned long long)(c >> 61);
        return r >= M ? r - M : r;
    }
    Hash(const string &s) : h(sz(s) + 1, 0), p(sz(s) + 1, 1) {
        for (int i = 0; i < sz(s); i++) {
            h[i + 1] = mul(h[i], B) + (unsigned char)s[i];
            if (h[i + 1] >= M) h[i + 1] -= M;
            p[i + 1] = mul(p[i], B);
        }
    }
    unsigned long long get(int l, int r) {  // hash of s[l..r-1]
        unsigned long long x = h[r] + M - mul(h[l], p[r - l]);
        return x >= M ? x - M : x;
    }
};
