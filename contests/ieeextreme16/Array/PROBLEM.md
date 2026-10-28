**CS Academy:** <https://csacademy.com/ieeextreme-practice/task/array/>

# Array

**IEEEXtreme 16.0** · Time limit: 1000 ms · Memory limit: 256 MB

*This problem was co-authored by Huawei.*

There is an array of $n$ integers $a_1,a_2,a_3,...,a_{n}$. This array follows $m$ rules. In each rule, you are given three integers $l$, $r$, and $k$, indicating that $(\sum^{r}_{i=l}{a_i}) \% p = k$. You need to find an array satisfying all rules.

## Standard Input

The first line contains 3 integers $n$, $m$ and $p$, indicating the length of the array, the number of rules and the modulo.

The next $m$ lines each contain 3 integers $l$, $r$ and $k$, for the rule: $(\sum^{r}_{i=l}{a_i}) \% p = k$.

## Standard Output

Output an array of $n$ integers $a_1,a_2,a_3,...,a_{n}$ satisfying all rules. This array must be the lexicographically smallest array out of all arrays satisfying the previous conditions. If there is no solution, output $None$.

## Constraints and notes

- $1 \leq m \leq 3000$
- $1 \leq l \leq r \leq n \leq 10^5$
- $p \leq 10^9 + 7$
- $0 \leq k \lt p$

## Examples

### Example 1

Input:
```
5 1 7
2 3 3
```

Output:
```
0 0 3 0 0
```

### Example 2

Input:
```
20 5 19
2 7 15
5 19 0
3 6 1
6 9 1
7 19 17
```

Output:
```
0 0 0 18 0 2 14 0 4 0 0 0 0 0 0 0 0 0 18 0
```

### Example 3

Input:
```
20 3 1000000007
2 5 6511
2 15 165151
6 15 134131351
```

Output:
```
None
```
