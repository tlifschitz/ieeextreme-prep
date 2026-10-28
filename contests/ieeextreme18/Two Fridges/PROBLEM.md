# Two Fridges

**IEEEXtreme 18.0** · Time limit: 300 ms · Memory limit: 256 MB

**CS Academy:** <https://csacademy.com/ieeextreme-practice/task/two-fridges/>

Dexter is playing again with $N$ substances trying to complete his greatest invention. Because it's running late, Dexter has decided the invention will have to wait until tomorrow. In the meanwhile, he needs to find a way to store the $N$ substances in his two fridges. Each fridge can be set to a certain temperature, an integer value between $-100$ and $100$. For each of the $N$ substances, Dexter knows an interval $[a_i, b_i]$, meaning the storing temperature of the $i$-th substance needs to fall in that specific interval.

Help Dexter decide the temperatures of the two fridges.

## Standard input

The first line contains a single integer $N$.

Each of the following $N$ lines contains two values $a_i$ and $b_i$, representing the storing interval for the $i$-th substance.

## Standard output

If there is no solution, print $-1$.

Otherwise, print two values $T_1$ and $T_2$ ($T_1 \leq T_2$), representing the temperatures of the two fridges.

## Constraints and notes

- $0 \leq N \leq 100$
- $-100 \leq a_i \leq b_i \leq 100$
- $-100 \leq T_1 \leq T_2 \leq 100$
- If there are multiple solutions, print the one where $T_1$ is minimum. If there are still multiple solutions, print the one where $T_2$ is minimum.

## Examples

### Example 1

Input:
```
2
10 12
20 24
```

Output:
```
10 20
```

Explanation:

Each substance will be stored in a separate fridge.

### Example 2

Input:
```
4
-54 -40
-50 -42
36 77
49 100
```

Output:
```
-50 49
```

Explanation:

The first two substances will be stored in the first fridge, while the last two substances will be stored in the second fridge.
