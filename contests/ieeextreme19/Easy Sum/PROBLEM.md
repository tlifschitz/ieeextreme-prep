# Easy Sum

**IEEEXtreme 19.0** · Time limit: 1000 ms · Memory limit: 256 MB

**CS Academy:** <https://csacademy.com/ieeextreme-practice/task/easy-sum/>

Victor claims he knows everything about range maximums.

To challenge him, his teammate Miguel gives him a problem he might not be able to solve.

You are given a sequence of positive integers $A_1, A_2, \dots, A_N$ and an integer $K$.

For each $k = 1, 2, \dots, K$, compute:

$S_k = \sum_{1 \le l \le r \le N} \lfloor \log_2(\mathrm{max}_k(A_l, A_{l+1}, \dots, A_r)) \rfloor \times (r - l + 1),$

where $\mathrm{max}_k$ denotes the $k$-th largest element in the range $(A_l, A_{l+1}, \dots, A_r)$,

and is defined as $0$ if the range contains fewer than $k$ elements.

Will Victor be able to solve this problem? Can you?

## Standard input

The first line contains an integer $N$ and an integer $K$.

The second line contains $N$ positive integers $A_{i}$ .

## Standard output

Print $K$ integers, the values $S_1, S_2, \dots, S_K$.

## Constraints and notes

- $1 \le N \le 10^{5}$.
- $1 \le K \le 20$.
- $1 \le A_{i} \le 10^{6}$.

## Examples

### Example 1

Input:
```
10 10
10 1 9 2 8 3 7 4 6 5
```

Output:
```
619 522 384 272 202 134 76 36 10 0 
```
