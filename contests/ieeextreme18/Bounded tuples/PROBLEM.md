# Bounded tuples

**IEEEXtreme 18.0** · Time limit: 3000 ms · Memory limit: 256 MB

**CS Academy:** <https://csacademy.com/ieeextreme-practice/task/bounded-tuples/>

Alice needs to choose $N$ non-negative integer values $V_1, V_2, \dots, V_N$.

Bob gives Alice $M$ constraints of the form: the sum of the elements of a given subset of $V$ should be greater or equal than a given value $\text{low}$ and smaller or equal than another given value $\text{high}$. Formally, the $i$-th constraint is represented by a set of $K_i$ indices $P_1, P_2, \dots, P_{K_i}$, such that:

- $\text{low}_i \leq V_{P_1} + V_{P_2} + \dots + V_{P_{K_i}} \leq \text{high}_i$

Your task is to calculate how many assignments of the variables $V_i$  satisfy all the inequalities. Output the result modulo $998244353$. However, if there are infinitely many valid assignments, print `infinity`.

### Standard Input

The first line contains two integers $N$ and $M$.

The next $M$ lines each contain the integers $\text{low}_i, \text{high}_i$ and $K_i$. Then, on the same line $K_i$ indices $P_1, P_2, \dots, P_{K_i}$ follow.

### Standard Output

Print the answer on the first line.

### Constraints and Notes

- $1 \leq N \leq 8$
- $0 \leq M \leq 4$
- $0 \leq \text{low}_i, \text{high}_i \leq 10^{18}$
- $1 \leq K_i \leq 3$

## Examples

### Example 1

Input:
```
3 2
0 4 2 1 2
3 5 2 2 3
```

Output:
```
44
```

### Example 2

Input:
```
1 0
```

Output:
```
infinity
```

### Example 3

Input:
```
2 3
0 3 1 1
1 2 1 2
6 10 2 2 1
```

Output:
```
0
```
