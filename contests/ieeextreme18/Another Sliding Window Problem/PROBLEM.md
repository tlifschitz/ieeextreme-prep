# Another Sliding Window Problem

**IEEEXtreme 18.0** · Time limit: 500 ms · Memory limit: 64 MB

**CS Academy:** <https://csacademy.com/ieeextreme-practice/task/another-sliding-window-problem/>

Given a sequence $t_1, t_2, \dots, t_k$, we are interested in grouping the elements into $\left\lceil \frac{k}{2} \right\rceil$ groups — each group will contain exactly $2$ elements, and if $k$ is odd there will be exactly one group with just one element. For each group we compute the sum of its elements. We'll call the maximum of these sums the /matching cost/.

Out of all the possible ways of grouping the elements, we are interested in the one that has the smallest /matching cost/. We will call this value the *optimal cost*.

For example, the optimal cost for $(5, 1, 3, 4)$ is $7$, and we can get it by grouping the elements in $\{\{5, 1\}, \{3, 4\}\}$. Any other grouping has a larger /matching cost/.

You are given a *sorted* array $A$ and you have to answer $Q$ queries:

- Each query consists of a single integer $x$.
- For each <Definition term="subarray"/> of $A$ that has an *optimal cost* $\le x$, add the difference between the rightmost and the leftmost elements of the subarray. Formally, calculate $\sum_{\substack{1 \leq l \leq r \leq N \\ \text{optimal cost}(A_l, \dots, A_r) \leq x}} (A_r - A_l)$.

## Standard input

The first line contains the integers $N$ and $Q$, the number of elements in the sequence and the number of queries.

The second line contains the sequence of integers $A_1, A_2, \dots, A_{N}$ separated by spaces.

The next $Q$ lines, the integer $x_{i}$, the value of $x$ for the $i$-th query, is found.

## Standard output

For each query, return the value of the indicated summation.

## Constraints and notes

- $1 \le N \le 10^{5}$.
- $1 \le Q \le 100$.
- $0 \le A_i \le {10}^9$ for $1 \le i \le N$.
- $0 \le x_{i} \le 2\times {10}^9$ for $1 \le i \le Q$.

## Examples

### Example 1

Input:
```
10 5
4 4 5 5 10 10 10 10 14 14
4
24
9
5
12
```

Output:
```
0
200
4
0
15
```

### Example 2

Input:
```
10 4
0 0 0 6 18 18 18 20 20 20
40
19
1
26
```

Output:
```
456
126
0
264
```
