#include <bits/stdc++.h>  // if the judge says "Compilation stopped: Time limit exceeded", use instead:
// #include <algorithm>
// #include <array>
// #include <chrono>
// #include <climits>
// #include <cmath>
// #include <cstring>
// #include <functional>
// #include <iomanip>
// #include <iostream>
// #include <map>
// #include <numeric>
// #include <queue>
// #include <set>
// #include <string>
// #include <unordered_map>
// #include <vector>
using namespace std;

#define all(x) begin(x), end(x)
#define rall(x) rbegin(x), rend(x)
#define sz(x) ((int)(x).size())
#define rep(i, n) for (int i = 0; i < (int)(n); ++i)
#define each(x, a) for (auto &x : a)
#define pb push_back

using ll = long long;
using ull = unsigned long long;
using pii = pair<int, int>;
using pll = pair<ll, ll>;
using vi = vector<int>;
using vl = vector<ll>;

#ifdef LOCAL  // g++ -DLOCAL: dbg(x, y) prints [x, y] = 1 2 to stderr
#define dbg(...) cerr << "[" << #__VA_ARGS__ << "] =", [](auto &&...a) { ((cerr << ' ' << a), ...); cerr << endl; }(__VA_ARGS__)
#else
#define dbg(...)
#endif

// Time budget for heuristics: if (elapsed() > 0.8) stop searching. Seconds since start.
auto T0 = chrono::steady_clock::now();
double elapsed() { return chrono::duration<double>(chrono::steady_clock::now() - T0).count(); }

// #include "lib/<topic>.h" lines go here (modular, ntt, tree, segtree, ds, graphs, io)

void solve() {
    int n;
    cin >> n;
    vl a(n);
    each(x, a) cin >> x;
    sort(all(a));
    rep(i, n) cout << a[i] << " \n"[i == n - 1];
}

int main() {
    ios::sync_with_stdio(false);  // cin/cout only from here on: no scanf/printf
    cin.tie(nullptr);
    int T = 1;
    // cin >> T;
    while (T--) solve();
}
