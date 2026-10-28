# Queries

**IEEEXtreme 18.0** · Time limit: 600 ms · Memory limit: 256 MB

**CS Academy:** <https://csacademy.com/ieeextreme-practice/task/queries/>

You are given an array $A$ of length $N$ with all the elements initially equal to $0$ and a permutation $P = p_1, p_2, \ldots, p_N$ of the same length, along with $Q$ queries/updates.

There are two types of updates:

- Type 0: Given $l, r, c$, add $c$ to $A_l, A_{l+1}, \ldots, A_r$.
- Type 1: Given $l, r, c$, add $c$ to $A_{p_l}, A_{p_{l+1}}, \ldots, A_{p_r}$.

And two types of queries:

- Type 2: Given $l, r$, calculate the sum $A_l + A_{l+1} + \ldots + A_r$.
- Type 3: Given $l, r$, calculate the sum $A_{p_l} + A_{p_{l+1}} + \ldots + A_{p_r}$.

## Standard input

The first line contains two integers $N$ and $Q$.

The next line contains $N$ integers representing the permutation $P$.

The following $Q$ lines describe consecutive events. Each event starts with a number $T_i$ denoting the type of the event. If $T_i = 0$ or $T_i = 1$, it is followed by three numbers $l, r, c$. Otherwise, it is followed by two numbers $l, r$.

## Standard output

For each query of type 2 or type 3, output the result of the corresponding sum.

## Constraints and notes

- $1 \leq N, Q \leq 10^5$
- $0 \leq T_i \leq 3$
- $1 \leq l \leq r \leq N$
- $0 \leq c \leq 10^6$

## Examples

### Example 1

Input:
```
5 6
3 1 5 4 2
0 2 4 2
1 2 4 3
2 3 4
0 2 5 1
3 2 4
3 1 3
```

Output:
```
7
13
10
```
