# Ordered Permutations

**IEEEXtreme 17.0** · Time limit: 1000 ms · Memory limit: 256 MB

**CS Academy:** <https://csacademy.com/ieeextreme-practice/task/ordered-permutations/>

Consider a permutation $P$ of length $N$. You are given a list of $N-1$ restrictions $R$ on permutation $P$. The $i$-th restriction states that $P_i < P_{i+1}$ if $R_i$ is of the first type and $P_i > P_{i+1}$ if $R_i$ is of the second type. Your task is to calculate the number of permutations $P$ that meet all $N-1$ restrictions. Since this number may be large, you should output it modulo $10^9+7$.

## Standard input

The first line contains one number $N$. The second line contains a string $R$ of length $N-1$ representing the restrictions. The $i$-th character is either $<$ or $>$ meaning that $R_i$ is of the first or the second type, respectively.

## Standard output

Output one line containing a single integer, the number of permutations $P$ that meet all $N-1$ restrictions, modulo $10^9+7$.

## Constraints and notes

- $1 \leq N \leq 8000$

## Examples

### Example 1

Input:
```
5
<<<>
```

Output:
```
4
```

### Example 2

Input:
```
4
<><
```

Output:
```
5
```

### Example 3

Input:
```
5
<><>
```

Output:
```
16
```

In the first example, the possible permutations $P$ are $(1, 2, 3, 5, 4), (1, 2, 4, 5, 3), (1, 3, 4, 5, 2), (2, 3, 4, 5, 1).$
