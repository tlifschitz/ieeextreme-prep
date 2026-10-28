import numpy as np


def conv_mod(a, b, mod):
    """Convolution of int sequences a, b modulo any mod < 2^30, via float
    FFT on 10-bit limbs (exact for lengths up to ~10^6)."""
    n = len(a) + len(b) - 1
    sz = 1 << (n - 1).bit_length()
    a = np.asarray(a, dtype=np.int64) % mod
    b = np.asarray(b, dtype=np.int64) % mod
    fa = [np.fft.rfft((a >> (10 * i)) & 1023, sz) for i in range(3)]
    fb = [np.fft.rfft((b >> (10 * i)) & 1023, sz) for i in range(3)]
    res = np.zeros(n, dtype=np.int64)
    for s in range(5):
        f = sum(fa[i] * fb[s - i] for i in range(3) if 0 <= s - i < 3)
        c = np.rint(np.fft.irfft(f, sz)[:n]).astype(np.int64) % mod
        res = (res + c * pow(2, 10 * s, mod)) % mod
    return res
