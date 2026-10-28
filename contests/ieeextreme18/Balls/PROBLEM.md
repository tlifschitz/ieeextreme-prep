# Balls

**IEEEXtreme 18.0** · Time limit: 1000 ms · Memory limit: 256 MB

**CS Academy:** <https://csacademy.com/ieeextreme-practice/task/balls/>

Josh has $N$ tiles arranged in a row and he has numbered them from $1$ to $N$. He also has $K$ balls, and for each of the balls he knows a special property called elasticity. Josh denotes the elasticity of the $i$-th ball by $E_i$. When he throws a ball of elasticity $E_i$, it will hit the $E_i$-th tile, $2*E_i$-th tile, $3*E_i$-th tile, and so on.

Josh decides to throw all the $K$ balls at once. How many tiles will he hit at least once?

## Standard input

The first line contains two integers $N$ and $K$.

The second line contains $K$ integers, the elasticities of the balls.

## Standard output

Print one integer representing the number of tiles that will be hit at least once.

## Constraints and notes

- $1 \leq N \leq 10^{14}$
- $1 \leq K \leq 100$
- $1 \leq E_i \leq 1000$
- The greatest common divisor of any two elasticities is $1$ (also expressed as $\text{gcd}(E_i, E_j) = 1$ for all $i \neq j$)

## Examples

### Example 1

Input:
```
17 3
2 3 7
```

Output:
```
12
```

Explanation:

The first ball will hit the tiles ${2, 4, 6, 8, 10, 12, 14, 16}$.

The second ball will hit the tiles ${3, 6, 9, 12, 15}$.

The third ball will hit the tiles ${7, 14}$.

In total there are 12 tiles hit by at least one ball: ${2, 3, 4, 6, 7, 8, 9, 10, 12, 14, 15, 16}$.
