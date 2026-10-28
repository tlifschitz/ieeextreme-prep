MOD = 10**9 + 7  # set by init(); solutions may reuse it
fact = [1]
inv_fact = [1]


def init(n, mod):
    """Precompute factorials and their inverses up to n modulo a prime mod
    (needs n < mod). Call once before C/P."""
    global MOD
    MOD = mod
    fact[:] = [1] * (n + 1)
    for i in range(1, n + 1):
        fact[i] = fact[i - 1] * i % mod
    inv_fact[:] = [1] * (n + 1)
    inv_fact[n] = pow(fact[n], -1, mod)
    for i in range(n, 0, -1):
        inv_fact[i - 1] = inv_fact[i] * i % mod


def C(n, k):
    """n choose k mod MOD; 0 when k < 0 or k > n."""
    if k < 0 or k > n:
        return 0
    return fact[n] * inv_fact[k] % MOD * inv_fact[n - k] % MOD


def P(n, k):
    """Ordered selections of k out of n mod MOD: n! / (n-k)!."""
    if k < 0 or k > n:
        return 0
    return fact[n] * inv_fact[n - k] % MOD


def inv(a, mod):
    """Modular inverse of a; mod need not be prime, only gcd(a, mod) = 1."""
    return pow(a, -1, mod)
