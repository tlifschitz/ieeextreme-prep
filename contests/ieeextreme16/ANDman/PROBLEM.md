**CS Academy:** <https://csacademy.com/ieeextreme-practice/task/andman/>

# ANDman

**IEEEXtreme 16.0** · Time limit: 1500 ms · Memory limit: 256 MB

And-man is found in a tree with $N$ nodes numbered $1$ to $N$ represented by apples. Each apple has a specific weight $W_i$. Steve Rangers wants to see how reliable And-man is at completing missions, so he gives him various operations to calculate the multiplication of the weights of the apples associated with nodes in a simple path from $u$ to $v$. But to see if he is really working on each mission, at certain times he will take an apple associated with node $u$ and exchange it for another with the same or different weight. In short, there will be $Q$ operations given by Steve Rangers. Each operation is one of the two following types:

- Type 1: $u$, $v$: We change the apple of node $u$ for another one with a weight $v$.
- Type 2: $u$, $v$: Calculate the multiplication of all the weights of the apples associated with nodes in unique single path from u to v, print this number modulo $1000000007$ $(10^9+7)$.

## Standard input

The first line is $T$, the number of testcases. Then $T$ testcases follow.

Each test consists of several lines.

- The first line contains a single integer $N$ - the number of nodes in tree.
- The second line contains $N$ integers $W_1, W_2, .., W_N$ where $W_i$ is the weight of the apple associated with node $i$.
- Then $N - 1$ lines, each line contains two integers $u$ and $v$ $(1 <= u, v <= N)$ denoting there is a direct edge between node $u$ and node $v$. It is guaranteed that these edges form a tree.
- Then $Q$ on a single line - the number of operations.
- $Q$ lines follow, each line contains $3$ integers $t, u, v$ in which $t$ is $1$ or $2$ denoting type of this operation described in the statement. If $t = 1$ then $1 <= u <= N, 1 <= v <= 10^9$. If $t = 2$ then $1 <= u, v <= N$.

## Standard output

For each operation of type 2, print the answer on a single line.

## Constraints and notes

- $1 <= T <= 10$
- $1 <= N <= 10^5$
- $1 <= Wi <= 10^9$
- $1 <= Q <= 10^5$

## Examples

### Example 1

Input:
```
1
5
9 11 11 13 13
1 2
1 3
2 4
2 5
6
2 4 5
1 1 15
2 1 4
2 3 5
1 2 10
2 4 3
```

Output:
```
1859
2145
23595
21450
```

Explanation:

The list of operations is:

- operation 1: Calculate from node 4 to node 5, 13*11*13 = 1859
- operation 2: Change the apple in node 1 for other with weight 15
- operation 3: Calculate from node 1 to node 4, 15*11*13 = 2145
- operation 4: Calculate from node 3 to node 5, 11*15*11*13 = 23595
- operation 5: Change the apple in node 2 for other with weight 10
- operation 6: Calculate from node 4 to node 3, 13*10*15*11 = 21450

### Example 2

Input:
```
1
6
500000 6 5 7 300000 400000
3 1
2 5
3 6
4 3
4 2
5
2 3 4
2 1 6
2 1 5
1 4 100000
2 6 5
```

Output:
```
35
999993007
999779507
480000021
```

Explanation:

The list of operations is:

- operation 1: Calculate from node 3 to node 4, 5*7 = 35
- operation 2: Calculate from node 1 to node 6, (500000*5*400000)%1000000007 = 999993007
- operation 3: Calculate from node 1 to node 5, (500000*5*7*6*300000)%1000000007 = 999779507
- operation 4: Change the apple in node 4 for other with weight 100000
- operation 5: Calculate from node 6 to node 5, (400000*5*100000*6*300000)%1000000007 = 480000021
