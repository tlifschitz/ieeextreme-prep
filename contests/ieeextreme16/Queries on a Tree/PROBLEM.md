# Queries on a Tree

**IEEEXtreme 16.0** · Time limit: 1500 ms · Memory limit: 256 MB

**CS Academy:** <https://csacademy.com/ieeextreme-practice/task/queries-on-a-tree/>

Anton has a tree of $N$ vertices numbered from $1$ to $N$. Vertex $i$ initially has value $A_i$. Anton has a brother that likes to come around and remove some edges from the tree. After such removal $value$ of the graph is a sum of $values$ of all connected components. A $value$ of a connected component is a square of the sum of values of all vertices in it.

Anton is going to perform $Q$ changes to his tree. In the $i$-th one he is going to change the value of $A_{x_i}$ to $C_i$. After every change Anton wants you to calculate the sum of $values$ of all graphs obtainable via removing any number of edges from the original tree. Since this value may be very large, he would like it modulo $998244353$.

## Standard input

The first line contains two numbers $N$ and $Q$. The next line contains $N$ integers, $i$-th one representing $A_i$. The next $N-1$ lines describe edges in the tree. The $i$-th of these lines contains two numbers $u_i$, $v_i$ representing and edge between vertices $u_i$ and $v_i$. Then, $Q$ lines follow, each one represents consecutive changes made to the tree. The $i$-th one of these lines contains two numbers $x_i$ and $C_i$ meaning that $A_{x_i}$ is being set to $C_i$.

## Standard output

The $i$-th line of output should contain one number - the sum of $values$ of all graphs obtainable from the tree, after the $i$-th change, by removing any number of edges from it, printed modulo $998244353$.

## Constraints and notes

- $1 \leq N, Q \leq 10^5$,
- $1 \leq A_i\leq 10^5$ for all $i$ from $1$ to $N$,
- $1 \leq u_i, v_i \leq N$ and the edges represent a tree,
- $1 \leq x_i \leq N$ and $1 \leq C_i \leq 10^5$ for all $i$ from $1$ to $Q$

## Examples

### Example 1

Input:
```
3 3
1 1 1 
1 2
2 3
1 1
1 2
2 3
```

Output:
```
22
40
96
```
