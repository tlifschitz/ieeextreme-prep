import numpy as np


def components_np(n, u, v):
    """Component label of each node 0..n-1 for edges u[i]-v[i] (numpy int arrays),
    vectorized: hook the larger root onto the smaller one, then pointer-jump.
    The label is the smallest node of the component; count = (lab == arange(n)).sum()."""
    lab = np.arange(n)
    u, v = np.asarray(u), np.asarray(v)
    while u.size:
        lu, lv = lab[u], lab[v]
        keep = lu != lv
        u, v, lu, lv = u[keep], v[keep], lu[keep], lv[keep]
        if not u.size:
            break
        lab[np.maximum(lu, lv)] = np.minimum(lu, lv)
        while True:
            nxt = lab[lab]
            if np.array_equal(nxt, lab):
                break
            lab = nxt
    return lab


def floyd(D):
    """In-place Floyd-Warshall on a square numpy matrix (D[i][i] = 0, no edge = big, with 2 big
    not overflowing the dtype). O(n^3) vectorized: n = 1000 in about a second."""
    for k in range(D.shape[0]):
        np.minimum(D, D[:, k, None] + D[k], out=D)
