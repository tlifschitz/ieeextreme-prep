#pragma once
// Needs the includes and typedefs of lib/template.cpp (ll, sz). Integer coordinates (exact).

// ============================================================================
// Points, cross product, convex hull, polygon area, segment intersection
// ============================================================================

struct Pt {
    ll x, y;
    Pt operator-(const Pt &o) const { return {x - o.x, y - o.y}; }
    bool operator<(const Pt &o) const { return x != o.x ? x < o.x : y < o.y; }
    bool operator==(const Pt &o) const { return x == o.x && y == o.y; }
};

ll cross(const Pt &a, const Pt &b) { return a.x * b.y - a.y * b.x; }
ll cross(const Pt &o, const Pt &a, const Pt &b) { return cross(a - o, b - o); }  // > 0: counter-clockwise

vector<Pt> convex_hull(vector<Pt> pts) {  // counter-clockwise, no collinear points (monotone chain)
    sort(pts.begin(), pts.end());
    pts.erase(unique(pts.begin(), pts.end()), pts.end());
    if (sz(pts) <= 2) return pts;
    vector<Pt> h(2 * sz(pts));
    int k = 0;
    for (int i = 0; i < sz(pts); i++) {
        while (k >= 2 && cross(h[k - 2], h[k - 1], pts[i]) <= 0) k--;
        h[k++] = pts[i];
    }
    for (int i = sz(pts) - 2, t = k + 1; i >= 0; i--) {
        while (k >= t && cross(h[k - 2], h[k - 1], pts[i]) <= 0) k--;
        h[k++] = pts[i];
    }
    h.resize(k - 1);
    return h;
}

ll area2(const vector<Pt> &poly) {  // twice the signed area (> 0 if counter-clockwise)
    ll s = 0;
    for (int i = 0, n = sz(poly); i < n; i++) s += cross(poly[i], poly[(i + 1) % n]);
    return s;
}

bool on_segment(const Pt &p, const Pt &a, const Pt &b) {
    return cross(a, b, p) == 0 && min(a.x, b.x) <= p.x && p.x <= max(a.x, b.x) && min(a.y, b.y) <= p.y && p.y <= max(a.y, b.y);
}

bool segments_intersect(const Pt &a, const Pt &b, const Pt &c, const Pt &d) {  // closed segments
    ll d1 = cross(c, d, a), d2 = cross(c, d, b), d3 = cross(a, b, c), d4 = cross(a, b, d);
    if (((d1 > 0 && d2 < 0) || (d1 < 0 && d2 > 0)) && ((d3 > 0 && d4 < 0) || (d3 < 0 && d4 > 0))) return true;
    return on_segment(a, c, d) || on_segment(b, c, d) || on_segment(c, a, b) || on_segment(d, a, b);
}

int point_in_polygon(const Pt &p, const vector<Pt> &poly) {  // 1 inside, 0 boundary, -1 outside
    bool in = false;
    for (int i = 0, n = sz(poly); i < n; i++) {
        Pt a = poly[i], b = poly[(i + 1) % n];
        if (on_segment(p, a, b)) return 0;
        if ((a.y > p.y) != (b.y > p.y) && (cross(a, b, p) > 0) == (b.y > a.y)) in = !in;
    }
    return in ? 1 : -1;
}

// ============================================================================
// Hilbert curve index (visiting order for local search over points)
// ============================================================================

ll hilbert(ll x, ll y, int bits = 20) {  // 0 <= x, y < 2^bits
    ll d = 0;
    for (ll s = 1LL << (bits - 1); s; s >>= 1) {
        int rx = (x & s) > 0, ry = (y & s) > 0;
        d += s * s * ((3 * rx) ^ ry);
        if (!ry) {
            if (rx) x = s - 1 - x, y = s - 1 - y;
            swap(x, y);
        }
    }
    return d;
}
