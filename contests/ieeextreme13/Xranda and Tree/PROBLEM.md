# Xranda and Tree

**IEEEXtreme 13.0** · Time limit: 1000 ms · Memory limit: 256 MB

**CS Academy:** <https://csacademy.com/ieeextreme-practice/task/xranda-and-tree/>

Xranda and her boyfriend, a man who does not chew are living in an <Definition term="tree"/> with $N$ nodes, with numerical labels on the edges. Their passion for treeology determined them to answer some seemingly impossible problems like "how many labeled trees lie in the isomorphism class of a given tree?" or "what is the generalised rotation distance from their tree and some arbitrary other one?". Exhausted by these tasks, they ask you to solve an easier one.

We define the distance $d(u, v)$ between two nodes $u$ and $v$ as the largest label of an edge which belongs to the unique path between them. Compute the sum of the distances across each possible pair of nodes, that is:

$\sum_{a=1}^{n} \sum_{b=1}^{a - 1} d(a, b)$

Given that this number can be quite large, we are only interested of its remainder when divided by $10^9+7$.

## Standard input

The first line will contain the number of nodes of the tree, $N$.

The next $N-1$ lines will contain the description of the edges of the tree, that is, the line $i+1$ will contain (in order) numbers $A_i$, $B_i$ and $W_i$, meaning that there is an edge between nodes $A_i$ and $B_i$ with the label $W_i$ between them.

## Standard output

The output will only contain the desired sum.

## Constraints and notes

- $2 \le N \le 10^5$
- $1 \le W_i \le 10^9$

## Examples

### Example 1

Input:
```
5
1 2 1
1 3 2
2 4 3
2 5 4
```

Output:
```
30
```

Explanation:

<Graph indexType="custom" height="300" width="300" forcePaused="true" nodes={

[

   {

      label:1,

      center:{

         x:150,

         y:50,

      }

   },

   {

      label:2,

      center:{

         x:100,

         y:150

      }

   },

   {

      label:3,

      center:{

         x:200,

         y:150

      }

   },

   {

      label:4,

      center:{

         x:50,

         y:250

      }

   },

   {

      label:5,

      center:{

         x:150,

         y:250

      }

   }

]}

edges={

[

      {

         label:"1",

         source:0,

         target:1

      },

      {

         label:"2",

         source:0,

         target:2

      },

      {

         label:"3",

         source:1,

         target:3

      },

      {

         label:"4",

         source:1,

         target:4

      }

   ]

} />

We have the following distances:

$d(1, 2) = 1$; $d(1, 3) = 2$; $d(1, 4) = 3$; $d(1, 5) = 4$; $d(2, 3) = 2$; $d(2, 4) = 3$; $d(2, 5) = 4$; $d(3, 4) = 3$; $d(3, 5) = 4$; $d(4, 5) = 4$

The total sum is $30$.
