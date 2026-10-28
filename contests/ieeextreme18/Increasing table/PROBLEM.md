# Increasing table

**IEEEXtreme 18.0** · Time limit: 1000 ms · Memory limit: 256 MB

**CS Academy:** <https://csacademy.com/ieeextreme-practice/task/increasing-table/>

Alice has a number $N$ and she wants to build a table $T$ with $2$ rows and $N$ columns. The table $T$ should respect the following constraints:

- Each number from $1$ to $2*N$ appears in $T$ exactly once
- The numbers from each row should be in increasing order: $T_{i, j} < T_{i, j + 1}$ for all $1 \leq i \leq 2$, $1 \leq j < N$
- The numbers from each column should also be in increasing order: $T_{1, j} < T_{2, j}$ for all $1 \leq j \leq N$

Additionally, for each number from $1$ to $2*N$ Alice knows whether she wants to use that particular number on the first row of $T$, on the second row of $T$, or both. Alice has two disjoint arrays $A$ and $B$, where:

- The numbers from $A$ should only be used on the first row
- The numbers from $B$ should only be used on the second row
- The numbers that don't appear in either $A$ or $B$ have no restrictions

Print the number of valid ways to fill the table $T$ modulo $998244353$.

### Standard Input

The first line of input contains an integer $N$.

The second line contains an integer $X$ and then $X$ distinct integers representing the elements of $A$.

The third line contains an integer $Y$ and then $Y$ distinct integers representing the elements of $B$.

### Standard Output

Output one integer — the number of valid ways to fill the $2 \times N$ table modulo $998244353$.

### Constraints and Notes

- $1 \leq N \leq 2000$
- $0 \leq X, Y \leq N$
- Sets $A$ and $B$ are disjoint and contain distinct integers from $1$ to $2*N$

## Examples

### Example 1

Input:
```
4
2 5 2
3 6 4 8
```

Output:
```
2
```

Explanation:

The two possible arrangements are:

<Latex value="\begin{array}{cc}

   1 & 2 & 3 & 5 \\

   4 & 6 & 7 & 8

\end{array}"/>

and

<Latex value="\begin{array}{cc}

   1 & 2 & 5 & 7 \\

   3 & 4 & 6 & 8

\end{array}"/>
