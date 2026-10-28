# Doubled Sequence

**IEEEXtreme 18.0** · Time limit: 1000 ms · Memory limit: 512 MB

**CS Academy:** <https://csacademy.com/ieeextreme-practice/task/doubled-sequence/>

A *doubled sequence* $S_{N}$ is a sequence that holds the following conditions:

- It contains each value in $\{1, 2, \ldots, N\}$ exactly twice.
- Let $L_{i}$ and $R_{i}$ be the leftmost and rightmost occurrence of $i$ in $S_{N}$, then $R_{i} - L_{i} = i$.

Given $N$, find any doubled sequence $S_{N}$ or determine that none exists.

## Standard input

The first line of input contains an integer $T$, the number of test cases.

The following $t$ lines contain an integer $N_{i}$ , the $i$-th line contains the $N$ corresponding to the $i$-th query.

## Standard output

Print $T$ lines, the $i$-th line must contain a doubled sequence $S_{N_{i}}$ or $-1$ if there are no doubled sequences.

## Constraints and notes

- $1 \leq T \leq 10^{5}$.

- $1 \leq N_{i} \leq 10^{6}$ for each $i = 1, \ldots, T$.

- $1 \leq \sum\limits_{i = 1}^{t}N_{i} \leq 10^{6}$.

## Examples

### Example 1

Input:
```
4
1
2
3
4
```

Output:
```
1 1
-1
-1
2 3 2 4 3 1 1 4
```

Explanation:

For the case $N = 4$, these are all the valid answers:

- 1 1 3 4 2 3 2 4
- 1 1 4 2 3 2 4 3
- 2 3 2 4 3 1 1 4
- 3 4 2 3 2 4 1 1
- 4 1 1 3 4 2 3 2
- 4 2 3 2 4 3 1 1
