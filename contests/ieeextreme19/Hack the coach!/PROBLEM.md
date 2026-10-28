**CS Academy:** <https://csacademy.com/ieeextreme-practice/task/hack-the-coach/>

Today your university had a very important contest, which was open for all. That's why even your coach participated on it. When you asked him about the problem D of the contest, he told you his solution but something seems strange.

The problem D goes as follows:

It is an interactive problem where you are lost in a country modeled as a tree with N vertices, rooted at vertex R — your hotel’s location. You can query an app that, given two vertices u and v, returns their lowest common ancestor (LCA) using a function lca(u, v). However, due to low battery, you can make at most 
⌊N/2⌋ queries. Using these limited LCA queries, you must determine the root of the tree — the location of your hotel. After doing the queries, you must print the root of the tree.
During the contest, he wanted to be fast and trusted his instincts, so he told you he sent this solution:

read integer n

for i from 1 to n - 1:
    read integers u, v
    degree[u] += 1
    degree[v] += 1
    add v to adjacency list G[u]
    add u to adjacency list G[v]

initialize empty list leaves
for i from 1 to n:
    if degree[i] == 1:
        append i to leaves

initialize empty list lcas
i = 0
while i + 1 < size(leaves):
    lcas.append (leaves[i], leaves[i + 1], lca(leaves[i], leaves[i + 1]))
    i += 2

if size(leaves) is odd:
    lcas.append (leaves[0], leaves[|leaves| - 1], lca(leaves[0], leaves[|leaves| - 1]))

initialize empty list candidates
for r from 1 to n:
    if check(r, lcas):
        candidates.append(r)

assert that size(candidates) == 1
answer(candidates[0])



Where check(r, lcas) is a boolean function that validates if using node r as the root is valid under the restrictions of the LCA tuples (u,v,lca(u,v)) in 
lcas.


Due to weak tests he got Accepted, but you know that this idea might fail in some case, so you want to hack his solution.


Standard input
There is no input in this problem.

Standard output
Your solution should print a single file describing a tree in which the coach's solution fails.

The first line of output must contain two integers N and R, the number of nodes in the tree and the root of the tree, respectively.

The following 
N−1 lines must contain two integers 
Ai and Bi, the nodes connected by the corresponding edge.

You must ensure that your solution prints a valid tree.

The score obtained will be based on the value of N, the smaller, the better. 