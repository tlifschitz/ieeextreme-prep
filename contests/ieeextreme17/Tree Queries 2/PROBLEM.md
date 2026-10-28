# Tree Queries 2

**IEEEXtreme 17.0** · Time limit: 4000 ms · Memory limit: 256 MB

**CS Academy:** <https://csacademy.com/ieeextreme-practice/task/tree-queries-2/>

You are given a tree with $N$ vertices and $N - 1$ edges. Vertex $i$ has value $w_i$ and edge $i$ has a multiplier $m_i$. Your task is to process $Q$ operations of the following types:

- Type 1: Change the value of vertex $x_i$ to $a_i$,
- Type 2: Change the multiplier of edge $e_i$ to $b_i$.

A /directed/ path from vertex $u$ to vertex $v$ is considered correct if the values $w_i$ of consecutive vertices of this path are non-decreasing. In particular, the path from vertex $v$ to $v$ is also considered correct. The score of a path is defined as a product of multipliers of its edges. In particular, the path from vertex $v$ to $v$ has a score of $1$. After every operation, your task is to print the sum of scores of all correct paths between every pair of vertices in the tree. Paths from vertex $u$ to $v$ and from $v$ to $u$ are considered different, and if they are both correct, they should be counted separately. Since the sum may be large, output it modulo $998244353$.

## Standard input

The first line contains two integers $N$ and $Q$. The next line contains $N$ integers, where the $i$-th of them is $w_i$. The next $N - 1$ lines describe the edges of the tree, where the $i$-th of them contains three integers $u_i$, $v_i$ and $m_i$ representing an edge between vertices $u_i$ and $v_i$ with the multiplier of $m_i$. The next $Q$ lines contain descriptions of the operations. Each description starts with one number $t_i$ representing the type of operation. If $t_i = 1$, then two numbers $x_i$ and $a_i$ follow. If $t_i = 2$, then two numbers $e_i$ and $b_i$ follow. Both cases were described above.

## Standard output

Output $Q$ lines, where the $i$-th of these lines contains the sum of scores of all correct paths after the first $i$ operations, modulo $998244353$.

## Constraints and notes

- $1 \leq N \leq 500\,000$,
- $1 \leq Q \leq 100\,000$,
- $1 \leq u_i, v_i, x_i, w_i, a_i \leq N$,
- $1 \leq e_i \leq N - 1$,
- $0 \leq m_i, b_i \leq 10^6$,
- $1 \leq t_i \leq 2$

The given graph is a tree.

In some of the testcases, the tree is a path.

## Examples

### Example 1

Input:
```
4 3
2 2 1 3
1 2 2
1 3 3
1 4 4
1 1 3
1 2 4
2 3 1
```

Output:
```
37
43
22
```
