# This is not an optimization problem

**IEEEXtreme 18.0** · Time limit: 1000 ms · Memory limit: 512 MB

**CS Academy:** <https://csacademy.com/ieeextreme-practice/task/this-is-not-an-optimization-problem/>

The Steiner Tree problem is stated as follows:

Given an undirected graph $G=(V,E)$ with a set of vertices $V$ and edges $E$, and a subset of vertices $S \subseteq V$ called /terminals/, the goal is to find a minimum-weight tree $T$ (a Steiner tree) that spans all the terminals in $S$. This tree may include non-terminal vertices (called /Steiner vertices/) from $V \backslash S$. The weight of the tree is the sum of weights of its edges.

In this case, we will analyze the node-weighted variation in which the nodes contain the weights instead of the edges so the weight of the tree is the sum of weights of its nodes.

In addition, to make things easier, we will consider that the given graph is a tree (connected undirected acyclic graph).

Now, for every subset $S$ with size $k$, you must compute the weight of its Steiner Tree and sum it up. Since this would be too easy for you, let's consider every $k$ from $1$ to $N$. Since this values could be large, compute them modulo $10^{9} + 99999$.

## Standard input

The first line of input contains an integer $N$, the number of nodes in the tree.

The second line of input contains $N$ integers $W_{i}$, the $i$-th integer is the weight of the $i$-th node.

The following $N - 1$ lines contain two integers $U_{i}$ and $V_{i}$, the $i$-th line contains the extreme nodes of the $i$-th edge.

## Standard output

Print $N$ lines. The $i$-th line must contain the sum of all the node-weighted Steiner trees over every subset of nodes with size $i$ modulo $10^{9} + 99999$.

## Constraints and notes

- $2 \leq N \leq 2 * 10^{5}$.
- $1 \leq W_{i} \leq 10^{9}$ for all $i = 1, \ldots, N$.
- $1 \leq U_{i}, V_{i} \leq N, U_{i} \not = V_{i}$ for all $i = 1, \ldots, N - 1$.
- It is guaranteed that the given graph is a tree.

## Examples

### Example 1

Input:
```
3
3 2 1
2 3
1 2
```

Output:
```
6
14
6
```

Explanation:

In this case, we have the following tree:

<Graph indexType="custom" height="200" width="200" nodes={[{label:"2"},{label:"3"},{label:"1"}]} edges={[{source:0,target:1},{source:2,target:0}]} />

It's not hard to notice that the node-weighted Steiner trees of the following subsets are:

- $S = \{1\} \rightarrow T = \{1\}$ with weight $3$.
- $S = \{2\} \rightarrow T = \{2\}$ with weight $2$.
- $S = \{3\} \rightarrow T = \{3\}$ with weight $1$.
- $S = \{1. 2\} \rightarrow T = \{1, 2\}$ with weight $5$.
- $S = \{1. 3\} \rightarrow T = \{1, 2, 3\}$ with weight $6$.
- $S = \{2. 3\} \rightarrow T = \{2, 3\}$ with weight $3$.
- $S = \{1, 2. 3\} \rightarrow T = \{1, 2, 3\}$ with weight $6$.

Summarizing, the sum of all the node-weighted Steiner trees are:

- With size $1$ is $6$.
- With size $2$ is $14$.
- With size $3$ is $6$.

### Example 2

Input:
```
4
10 1 20 40
1 3
2 3
3 4
```

Output:
```
71
273
233
71
```

Explanation:

In this case, we have the following tree:

<Graph indexType="custom" height="250" width="250" nodes={[{label:"2"},{label:"3"},{label:"1"},{label:"4"}]} edges={[{source:0,target:1},{source:2,target:1},{source:1,target:3}]} />

It's not hard to notice that the node-weighted Steiner trees of the following subsets are:

- $S = \{1\} \rightarrow T = \{1\}$ with weight $10$.
- $S = \{2\} \rightarrow T = \{2\}$ with weight $1$.
- $S = \{3\} \rightarrow T = \{3\}$ with weight $20$.
- $S = \{3\} \rightarrow T = \{4\}$ with weight $40$.
- $S = \{1. 2\} \rightarrow T = \{1, 2, 3\}$ with weight $31$.
- $S = \{1. 3\} \rightarrow T = \{1, 3\}$ with weight $30$.
- $S = \{1. 4\} \rightarrow T = \{1, 3, 4\}$ with weight $70$.
- $S = \{2. 3\} \rightarrow T = \{2, 3\}$ with weight $21$.
- $S = \{2. 4\} \rightarrow T = \{2, 3, 4\}$ with weight $61$.
- $S = \{3, 4\} \rightarrow T = \{3, 4\}$ with weight $60$.
- $S = \{1, 2. 3\} \rightarrow T = \{1, 2, 3\}$ with weight $31$.
- $S = \{1, 2. 4\} \rightarrow T = \{1, 2, 3, 4\}$ with weight $71$.
- $S = \{1, 3, 4\} \rightarrow T = \{1, 3, 4\}$ with weight $70$.
- $S = \{2, 3, 4\} \rightarrow T = \{2, 3, 4\}$ with weight $61$.
- $S = \{1, 2. 3, 4\} \rightarrow T = \{1, 2, 3, 4\}$ with weight $71$.

Summarizing, the sum of all the node-weighted Steiner trees are:

- With size $1$ is $71$.
- With size $2$ is $273$.
- With size $3$ is $233$.
- With size $4$ is $71$.
