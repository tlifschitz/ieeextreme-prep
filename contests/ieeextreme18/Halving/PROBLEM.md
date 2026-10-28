# Halving

**IEEEXtreme 18.0** · Time limit: 1000 ms · Memory limit: 64 MB

**CS Academy:** <https://csacademy.com/ieeextreme-practice/task/halving/>

Alice and Bob are playing a secret communication game. Initially, Alice writes down on a piece of paper a permutation $A$ of size $2*N$ (each number from $1$ to $2*N$ appears in $A$ exactly once). Then Bob chooses a binary array $R$ of size $N$ which he calls "the ruleset".

Alice uses $A$ and $R$ to create another array $B$ of size $N$, which she communicates to Bob. The rules for building $B$ are the following:

- if $R_i = 0$ then $B_i = \text{min}(A_{2*i - 1}, A_{2*i})$;
- if $R_i = 1$ then $B_i = \text{max}(A_{2*i - 1}, A_{2*i})$.

For each $i, 1 \leq i \leq N$.

Unfortunately, Alice has spilled some water on the piece of paper containing $A$, and now some of the numbers are impossible to read. You are given an array $C$ of size $2*N$, where:

- $C_i = A_i$ if the $i$-th number from $A$ is still readable
- $C_i = -1$ otherwise

You also know the ruleset array $R$ and Bob's array $B$. Calculate the total number of possible initial arrays $A$. Output the result modulo $998244353$.

### Standard Input

The first line contains a single integer $N$.

The second line contains $2*N$ integers $C_1, C_2, \dots, C_{2*N}$.

The third line contains $N$ integers $R_1,R_2, \dots, R_N$.

The fourth line contains $N$ integers $B_1, B_2, \dots, B_N$.

### Standard Output

Output a single integer — the number of permutations $A$ consistent with the given data, modulo $998244353$.

### Constraints and Notes

- $1 \leq N \leq 300$
- $C_i = -1$ or $1 \leq C_i \leq 2*N$
- the positive elements of $C$ are pairwise distinct
- $R_i \in \{0, 1\}$
- $1 \leq B_i \leq 2*N$
- the elements of $B$ are pairwise distinct

## Examples

### Example 1

Input:
```
3
-1 2 3 -1 -1 -1
0 0 1
2 3 6
```

Output:
```
4
```

Explanation:

The possible permutations $A$ are:

- $5, 2, 3, 4, 6, 1$
- $4, 2, 3, 5, 1, 6$
- $5, 2, 3, 4, 1, 6$
- $4, 2, 3, 5, 6, 1$

### Example 2

Input:
```
1
1 -1
0
2
```

Output:
```
0
```

Explanation:

There are no matching permutations.
