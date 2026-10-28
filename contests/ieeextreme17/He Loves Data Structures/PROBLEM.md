# He Loves Data Structures

**IEEEXtreme 17.0** · Time limit: 1000 ms · Memory limit: 256 MB

**CS Academy:** <https://csacademy.com/ieeextreme-practice/task/data_structures/>

Guillermo loves data structures, especially tree data structures. He can solve all the problems he has faced with the data structures he knows. One day he encountered the following problem:

Given a tree with **n** nodes, with nodes numbered from **1** to **n**, rooted at **1** and values assigned to each node, initially all set to **0**, you are required to solve the following queries, which are presented in the following format:

**1** **v** **l** **r**: Within the subtree of v, assign a value to each node u that has a distance no greater than **r-l** from **v**.

    $value(u) = phi(l+dist(v,u))$

    where $phi$ represents [Euler's totient function](https://en.wikipedia.org/wiki/Euler%27s_totient_function).

**2** **v**: Determine the value of specific node **v**.

Guillermo tried for many days to solve the problem, according to the time limit specified, but he failed. Can you help him solve the problem to restore his love for data structures?

## Standard Input

The first line contains the integer **n**, indicating the number of nodes in the tree.

The following n-1 lines each contain integers **a** and **b**, indicating that there is an edge of length 1 between **a** and **b** in the tree.

The following line contains an integer **q**, indicating the number of queries for the problem.

The following **q** lines indicate the queries, one on each line.

## Standard Output

For every query of type **2**, respond with an integer as specified in the problem.

## Constraints and notes

- $1 \le n \le 3 \times {10}^5$
- $1 \le a, b \le n$
- $1 \le q \le 3 \times {10}^5$
- $1 \le v, l \le n$
- $l \le r < 2 n$

## Examples

### Example 1

Input:
```
10
8 10
1 2
8 5
6 4
4 1
5 1
1 3
7 8
9 1
10
2 1
1 1 5 8
1 1 6 8
2 5
2 10
1 8 10 11
2 10
2 8
2 7
2 6
```

Output:
```
0
6
4
10
4
10
4
```
