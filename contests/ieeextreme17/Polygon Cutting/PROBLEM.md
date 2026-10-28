# Polygon Cutting

**IEEEXtreme 17.0** · Time limit: 2000 ms · Memory limit: 256 MB

**CS Academy:** <https://csacademy.com/ieeextreme-practice/task/polygon-cutting/>

You are given a strictly convex polygon with $N$ vertices and $M$ diagonals of this polygon. These diagonals don't intersect in the interior of the polygon and cut the polygon into $M + 1$ pieces. Your task is to choose some set of pieces $S$ so that the total area of pieces in $S$ is maximized and no two pieces inside $S$ share an edge. Output double the total area of that set.

## Standard input

The first line contains two integers $N$ and $M$. The next $N$ lines contain descriptions of vertices of the polygon in clockwise order. The $i$-th of these lines contains two numbers $x_i$, $y_i$ that are the coordinates of the $i$-th vertex. The next $M$ lines contain descriptions of the diagonals. The $i$-th of these lines contains two integers $u_i$, $v_i$ which represent a diagonal between vertices $u_i$ and $v_i$.

## Standard output

Output one line with double the total area of the bigger set in an optimal split of the polygon pieces.

## Constraints and notes

- $3 \leq N \leq 1\,000\,000$,
- $1 \leq M \leq 1\,000\,000$,
- $|x_i|, |y_i| \leq 10^9$

## Examples

### Example 1

Input:
```
4 1
-9 4
4 9
9 4
10 0
2 4
```

Output:
```
147
```

### Example 2

Input:
```
4 1
4 9
4 -9
-8 -6
-10 0
2 4
```

Output:
```
252
```

### Example 3

Input:
```
4 1
3 4
5 0
4 -3
-5 0
2 4
```

Output:
```
40
```
