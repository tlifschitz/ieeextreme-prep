# Unicornosaurus

**IEEEXtreme 13.0** · Time limit: 800 ms · Memory limit: 256 MB

**CS Academy:** <https://csacademy.com/ieeextreme-practice/task/unicornosaurus/>

Tiranca the unicornosaurus broke Sherbot's duckinator*. After close inspection, she realized that there were $N$ intervals $[L_i, R_i]$ of broken planks. In each interval, all of the planks numbered from $L_i$ to $R_i$ were completely destroyed.

Luckily, Tiranca is a unicornosaurus and she possesses $M$ superpower actions to repair the duckinator. Each superpower costs $C_i$ rainbows and can be used to repair all the planks in the interval $[A_i, B_i]$. To fix the duckinator, she has to fix all of the broken planks and, because rainbows are expensive, she should use the smallest possible number of rainbows.

1* /Duckinator/: Long fence made of wide planks used to catch ducks.  The planks are arranged in a line, numbered from $1$ to $S$.

## Standard input

The first line contains three integers, $N, M$ and $S$. The $i$-th following $N$ lines contain two integers, $L_i$ and $R_i$, describing the damage done to the duckinator. The $i$-th following $M$ lines contain three integers $A_i, B_i$ and $C_i$, describing Tiranca's possible superpower actions.

## Standard output

The output should contain the minimum number of rainbows required to repair the duckinator. In case it is impossible to fix, the output should be `-1`.

## Constraints and notes

- $1 \le  S \le10^5$
- $1 \le C_i \le 10^9$
- $1 \le L_i \le R_i \le S$
- $1 \le N, M \le10^5$
- The intervals of broken planks *may overlap*.
- The author made up the term *duckinator*.

## Examples

### Example 1

Input:
```
1 3 15
5 10
3 7 2
6 12 5
2 11 6
```

Output:
```
6
```

Explanation:

There is one broken segment: $[5, 10]$.

We choose $[2, 11]$ with the total cost of $6$ to fix it.

Note that another solution would be choosing $[3, 7]$ and $[6, 12]$, but the total cost of that would be $7$.

### Example 2

Input:
```
2 4 15
3 7
9 10
2 6 10
3 9 15
5 12 13
8 10 30
```

Output:
```
23
```

Explanation:

There are two broken segments: $[3, 7]$ and $[9, 10]$.

We choose $[2, 6]$ and $[5, 12]$ with the total cost of $23$ to fix it.
