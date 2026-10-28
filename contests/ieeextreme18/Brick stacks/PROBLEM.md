# Brick stacks

**IEEEXtreme 18.0** · Time limit: 1000 ms · Memory limit: 256 MB

**CS Academy:** <https://csacademy.com/ieeextreme-practice/task/brick-stacks/>

You are given $N$ bricks of lengths $A_1, A_2, \dots, A_N$ and an integer $x$. You can place brick $i$ on top of brick $j$ (for any $i \neq j$) only if the condition $A_i + x \leq A_j$ is satisfied. Your task is to arrange the bricks into the least number of stacks satisfying the condition.

### Standard Input

The first line contains integers $N$ and $x$.

The second line contains $N$ integers representing the lengths of the bricks $A_1, A_2, \dots, A_N$.

### Standard Output

Output a single integer representing the minimum number of stacks formed.

Then, for each stack output in a separate line a number $M$ denoting the number of bricks in a stack and then $M$ integers denoting the sizes of bricks in the stack from the biggest brick to the smallest.

If there are many valid arrangements minimizing the number of stacks, print any of them.

### Constraints and Notes

- $1 \leq N \leq 10^6$
- $1 \leq x \leq 10^9$
- $1 \leq A_i \leq 10^9$
- This problems has its tests grouped. In order to score any points, you need to pass all the tests in a group.

## Examples

### Example 1

Input:
```
9 3
8 4 2 5 10 8 1 7 4
```

Output:
```
3
4 10 7 4 1
3 8 5 2
2 8 4
```
