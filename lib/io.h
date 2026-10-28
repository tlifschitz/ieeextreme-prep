#pragma once
// Needs the includes and typedefs of lib/template.cpp (ll).

// ============================================================================
// Fast input: streaming fread reader (do not mix with cin / scanf)
// ============================================================================

static char ibuf[1 << 16];
int ipos = 0, ilen = 0;

int gc() {  // next char, -1 at EOF
    if (ipos == ilen) {
        ilen = fread(ibuf, 1, sizeof ibuf, stdin), ipos = 0;
        if (ilen <= 0) return -1;
    }
    return ibuf[ipos++];
}

ll read_int() {  // next integer, sign allowed; 0 at EOF
    int c = gc();
    while (c != '-' && (c < '0' || c > '9')) {
        if (c < 0) return 0;
        c = gc();
    }
    bool neg = c == '-';
    if (neg) c = gc();
    ll x = 0;
    for (; c >= '0' && c <= '9'; c = gc()) x = x * 10 + (c - '0');
    return neg ? -x : x;
}

string read_token() {  // next whitespace-separated word, "" at EOF
    int c = gc();
    while (c >= 0 && c <= ' ') c = gc();
    string s;
    for (; c > ' '; c = gc()) s += char(c);
    return s;
}
