# Digits swap

**IEEEXtreme 18.0** · Time limit: 500 ms · Memory limit: 256 MB

**CS Academy:** <https://csacademy.com/ieeextreme-practice/task/digits-swap/>

You are given an integer $N$ and another integer $K$. You are allowed to perform at most $K$ operations of the type:

- Pick two arbitrary digits and swap them.

After each swap, the number must not contain any leading zeroes. Your task is to maximize the value of $N$ after the swaps.

### Standard Input

The first line contains two integers $N$ and $K$.

### Standard Output

Output one integer — the largest possible value of $N$ after performing at most $K$ swaps.

### Constraints and Notes

- $1 \leq N < 10^{15}$
- $1 \leq K \leq 25$
- Swapping two digits should not result in a number with leading zeroes.

## Examples

### Example 1

Input:
```
1854268 3
```

Output:
```
8865241
```

Explanation:

We will perform the following sequence of swaps:

1. $[1]85426[8]$ into $8854261$.
1. $88[5][4]261$ into $8845261$
1. $88[4]52[6]1$ into $8865241$
