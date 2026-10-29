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

// ============================================================================
// Fast output: buffered fwrite writer (call flush_out() before returning from main)
// ============================================================================

static char obuf[1 << 16];
int opos = 0;

void flush_out() { fwrite(obuf, 1, opos, stdout), opos = 0; }

void put_char(char c) {
    if (opos == sizeof obuf) flush_out();
    obuf[opos++] = c;
}

void write_int(ll x, char end = '\n') {
    if (x < 0) put_char('-'), x = -x;
    char s[20];
    int n = 0;
    do s[n++] = char('0' + x % 10), x /= 10; while (x);
    while (n) put_char(s[--n]);
    if (end) put_char(end);
}
