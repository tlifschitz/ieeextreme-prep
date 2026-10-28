# Big Matrix Small Determinant

**IEEEXtreme 15.0** · Time limit: 1000 ms · Memory limit: 256 MB

**CS Academy:** <https://csacademy.com/ieeextreme-practice/task/big-matrix-small-determinant/>

Construct a square matrix with $N$ rows and $N$ columns consisting of nonnegative integers from $0$ to $10^{18}$, such that its [determinant](https://en.wikipedia.org/wiki/Determinant) is equal to $1$, and there are exactly $A_i$ odd numbers in the $i$-th row for each $i$ from $1$ to $N$, or report there isn't such a matrix.

## Standard input

The first line contains a single integer $N$. Each of the next $N$ lines contains a single integer $A_i$.

## Standard output

If there is no solution, output $\text{-}1$.

Otherwise, print $N$ lines, each consisting of $N$ integers, representing the values of the constructed matrix. If there are multiple solutions, print any.

## Constraints and notes

- $2 \le N \le 50$
- $1 \leq A_i \leq N$
- For $40\%$ of the test files, $N \le 17$.

## Examples

### Example 1

Input:
```
2
1
1
```

Output:
```
1 0
0 1
```

### Example 2

Input:
```
2
2
1
```

Output:
```
1 1 
0 1 
```

### Example 3

Input:
```
4
3
3
3
3
```

Output:
```
1 1 1 0 
1 1 2 1 
1 0 1 1 
2 1 3 3 
```

### Example 4

Input:
```
3
2
2
2
```

Output:
```
-1
```

### Example 5

Input:
```
3
3
1
3
```

Output:
```
-1
```
