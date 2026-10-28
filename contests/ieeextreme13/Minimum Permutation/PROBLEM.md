# Minimum Permutation

**IEEEXtreme 13.0** · Time limit: 1000 ms · Memory limit: 256 MB

**CS Academy:** <https://csacademy.com/ieeextreme-practice/task/minimum-permutation/>

You are given an array $A$ of size $N$ and a set $S$ with $M$ elements. Each number from $1$ to $N + M$ occurs exactly once in either $A$ or $S$.

You need to insert the elements from the set $S$  into the array $A$ in order to obtain the lexicographically smallest permutation.

Note: A Sequence $X_{1..n}$, of the same length as a sequence $Y_{1..n}$, is considered lexicographically smaller than $Y_{1..n}$ if, and only if, there exists an index $j$ for which $X_{i}$ = $Y_{i}$ for $1 \le i \lt j$, and $X_{j} \lt Y_{j}$.

## Standard input

The first line contains the numbers $N$ and $M$. The second line contains $N$ integers corresponding to the elements of $A$. The third line contains $M$ integers corresponding to the elements of $S$.

## Standard output

The output should contain the elements of the lexicographically smallest permutation, separated by single spaces.

## Constraints and notes

- $1 \leq N \leq 10^5$
- $1 \leq M \leq 10^5$
- $2 \leq N + M \leq 10^5$
- All the elements are unique and between $1$ and $N + M$

## Examples

### Example 1

Input:
```
3 2
3 1 5
4 2
```

Output:
```
2 3 1 4 5 
```

Explanation:

The array is $[3, 1, 5]$ and the set is $\{4, 2\}$.

The first operation is to insert $2$ at the beginning of the array, obtaining $[2, 3, 1, 5]$.

The second operation is to insert $4$ right after $1$, obtaining $[2, 3, 1, 4, 5]$.
