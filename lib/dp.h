#pragma once
// Needs the includes and typedefs of lib/template.cpp (ll, vl, vi, pii, sz).

// ============================================================================
// Longest increasing subsequence: indices of one, O(n log n)
// ============================================================================

template <class T>
vi lis(const vector<T> &a, bool strict = true) {  // strict=false: non-decreasing
    vector<T> tails;
    vi idx, prev(sz(a), -1);
    for (int i = 0; i < sz(a); i++) {
        int k = (strict ? lower_bound(tails.begin(), tails.end(), a[i]) : upper_bound(tails.begin(), tails.end(), a[i])) - tails.begin();
        if (k == sz(tails)) tails.push_back(a[i]), idx.push_back(i);
        else tails[k] = a[i], idx[k] = i;
        prev[i] = k ? idx[k - 1] : -1;
    }
    vi out;
    for (int i = idx.empty() ? -1 : idx.back(); i != -1; i = prev[i]) out.push_back(i);
    reverse(out.begin(), out.end());
    return out;
}

// ============================================================================
// Monotonic stack: left[i] = last j < i with a[j] < a[i] (else -1),
// right[i] = first j > i with a[j] < a[i] (else n). strict=false uses <=.
// For greater, pass negated values.
// ============================================================================

template <class T>
pair<vi, vi> nearest_smaller(const vector<T> &a, bool strict = true) {
    int n = sz(a);
    vi left(n), right(n), st;
    auto worse = [&](int j, int i) { return strict ? a[j] >= a[i] : a[j] > a[i]; };
    for (int i = 0; i < n; i++) {
        while (!st.empty() && worse(st.back(), i)) st.pop_back();
        left[i] = st.empty() ? -1 : st.back();
        st.push_back(i);
    }
    st.clear();
    for (int i = n - 1; i >= 0; i--) {
        while (!st.empty() && worse(st.back(), i)) st.pop_back();
        right[i] = st.empty() ? n : st.back();
        st.push_back(i);
    }
    return {left, right};
}

// ============================================================================
// Sliding window minimum (fixed k) and a FIFO queue with min (monotonic deque)
// ============================================================================

template <class T>
vector<T> window_min(const vector<T> &a, int k) {  // n-k+1 values; for max, negate
    deque<int> q;
    vector<T> out;
    for (int i = 0; i < sz(a); i++) {
        while (!q.empty() && a[q.back()] >= a[i]) q.pop_back();
        q.push_back(i);
        if (q.front() <= i - k) q.pop_front();
        if (i >= k - 1) out.push_back(a[q.front()]);
    }
    return out;
}

template <class T>
struct MinQueue {  // push, pop (oldest), min; for max push negated values
    deque<T> q, d;
    void push(T x) {
        q.push_back(x);
        while (!d.empty() && d.back() > x) d.pop_back();
        d.push_back(x);
    }
    T pop() {
        T x = q.front();
        q.pop_front();
        if (d.front() == x) d.pop_front();
        return x;
    }
    T min() const { return d.front(); }
    int size() const { return sz(q); }
};

// ============================================================================
// Li Chao tree (convex hull trick): add y = a*x + b, min at a query x.
// xs = every x that will be queried. For max, add (-a, -b) and negate.
// Values a*x + b must fit in ll.
// ============================================================================

struct LiChao {
    static constexpr ll INF = LLONG_MAX;
    int size = 1;
    vl xs, A, B;
    LiChao(vl x) : xs(x) {
        sort(xs.begin(), xs.end());
        xs.erase(unique(xs.begin(), xs.end()), xs.end());
        while (size < sz(xs)) size *= 2;
        xs.resize(size, xs.empty() ? 0 : xs.back());
        A.assign(2 * size, 0), B.assign(2 * size, INF);
    }
    static ll eval(ll a, ll b, ll x) { return b == INF ? INF : a * x + b; }
    void add(ll a, ll b) {
        for (int node = 1, lo = 0, hi = size;;) {
            int mid = (lo + hi) / 2;
            if (eval(a, b, xs[mid]) < eval(A[node], B[node], xs[mid])) swap(a, A[node]), swap(b, B[node]);
            if (hi - lo == 1 || b == INF) return;
            if (eval(a, b, xs[lo]) < eval(A[node], B[node], xs[lo])) node = 2 * node, hi = mid;
            else node = 2 * node + 1, lo = mid;
        }
    }
    ll query(ll x) {
        int k = lower_bound(xs.begin(), xs.begin() + size, x) - xs.begin() + size;
        ll best = INF;
        for (; k; k >>= 1) best = min(best, eval(A[k], B[k], x));
        return best;
    }
};

// ============================================================================
// Monotone convex hull trick: add y = a*x + b with non-increasing a, min at an
// integer x by binary search, O(log n); query_inc for non-decreasing x, O(1)
// amortized. Increasing a: add (-a, b), query -x. Max: add (-a, -b), negate.
// Integer-exact (floor division, no products); a*x + b must fit in ll.
// ============================================================================

struct MonoHull {
    vl A, B, T;  // line k is the min on [T[k], T[k+1])
    int p = 0;
    void add(ll a, ll b) {
        if (!A.empty() && A.back() == a) {
            if (b >= B.back()) return;
            A.pop_back(), B.pop_back(), T.pop_back();
        }
        ll t = LLONG_MIN;
        while (!A.empty()) {
            ll n = b - B.back(), d = A.back() - a;  // new line <= last from x >= ceil(n / d)
            t = n / d + (n % d > 0);
            if (t > T.back()) break;
            A.pop_back(), B.pop_back(), T.pop_back();
        }
        A.pb(a), B.pb(b), T.pb(t);
    }
    ll query(ll x) {
        int k = upper_bound(T.begin(), T.end(), x) - T.begin() - 1;
        return A[k] * x + B[k];
    }
    ll query_inc(ll x) {
        p = min(p, sz(A) - 1);
        while (p + 1 < sz(A) && T[p + 1] <= x) p++;
        return A[p] * x + B[p];
    }
};

// ============================================================================
// Slope trick: min sum |a_i - b_i| over non-decreasing b, O(n log n).
// Strictly increasing b: pass a_i - i.
// ============================================================================

ll slope_trick(const vl &a) {
    priority_queue<ll> q;
    ll cost = 0;
    for (ll x : a) {
        q.push(x);
        if (q.top() > x) cost += q.top() - x, q.pop(), q.push(x);
    }
    return cost;
}
