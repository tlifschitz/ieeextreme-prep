# Product Rectangle

**IEEEXtreme 12.0** · Time limit: 1000 ms · Memory limit: 256 MB

**CS Academy:** <https://csacademy.com/ieeextreme-practice/task/product-rectangle/>

You are given an array $A$ of $N$ integers and an array $B$ of $M$ integers. Consider a matrix $C$ of size $N \times M$ where $C_{i, j} = A_i \cdot B_j$. Find the maximum sum of a  rectangle which contains at least one cell.

More formally, find $\text{max}(\sum\limits_{i=r_1}^{r_2} \sum\limits_{j=c_1}^{c_2} C_{i, j} \ |\ 1 \leq r_1 \leq r_2 \leq N, 1 \leq c_1 \leq c_2 \leq M).$

## Standard input

The first line contains two integers $N$ and $M$.

The second line contains $N$ integers, representing $A$.

The third line contains $M$ integers, representing $B$.

## Standard output

Print the value of the sum on the first line.

## Constraints and notes

- $1 \leq N, M \leq 2\cdot10^3$
- $-10^6 \leq A_i, B_j \leq 10^6$ for all valid $i$ and $j$

## Examples

### Example 1

Input:
```
3 3
-1 3 5
-10 -3 20
```

Output:
```
160
```

Explanation:

$C = \begin{pmatrix}10 & 3 & -20 \\-30 & -9 & 60 \\ -50 & -15 & 100\end{pmatrix}$

We will choose $r_1 = 2, r_2 = 3, c_1 = 3, c_2 = 3$, which sums up to $160$.
