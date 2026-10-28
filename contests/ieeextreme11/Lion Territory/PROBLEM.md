# Lion Territory

**IEEEXtreme 11.0** · Time limit: 1000 ms · Memory limit: 128 MB

**CS Academy:** <https://csacademy.com/ieeextreme-practice/task/15443fc9f89feb90bc30096f43b308af/>

In your last trip to Africa, you had the luck to encounter $k$ lions. The savanna can be encoded as an $n \times m$ ($1 \leq n, m \leq 10^3$) matrix, and the $i^{th}$ lion was located at cell $(r_i, c_i)$.

The (claimed) territory of the $i^{th}$ lion spans over all the cells at Manhattan distance at most $d_i$ from its location. It is possible that territories overlap.

Your task it to identify the lion that is located on most of other lions’ territories.

## Standard input

The first line contains three integers $n$, $m$ and $k$.

The next $k$ lines contain $r_i$, $c_i$ and $d_i$, representing the row, column and distance for the $i^{th}$ lion.

## Standard output

Print two integers representing the smallest index of the lion that is situated on most of other lion’ territories and the number of territories.

## Constraints and notes

- $1 \leq n, m \leq 10^3$
- $1 \leq k \leq n*m$
- $1 \leq r_i \leq n$
- $1 \leq c_i \leq m$
- $0 \leq d_i \leq 10^3$
- It is possible that $2$ or more lions are located in the same cell

## Examples

### Example 1

Input:
```
5 4 4
2 1 3
3 1 2
3 4 2
2 4 2
```

Output:
```
4 2
```

Explanation:

Lion $4$ is situated on the territory of lions $1$ and $3$.
