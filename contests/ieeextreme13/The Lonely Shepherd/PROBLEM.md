# The Lonely Shepherd

**IEEEXtreme 13.0** · Time limit: 1000 ms · Memory limit: 256 MB

**CS Academy:** <https://csacademy.com/ieeextreme-practice/task/lonely-shepherd/>

Bogdan the Lonely Shepherd is standing under a special <Definition term="tree"/> with $N$ nodes, out of which $K$ are blue and the rest are red. Bogdan really wants a unicorn, being tired of so many sheep and he thinks that if he could do some magic with this tree, a unicorn will show up. What kind of magic, you ask? He has to toggle a set of nodes from blue to red or red to blue (doing this twice cancels any change) and then cut an edge of the tree, resulting in two trees. Bogdan thinks that a pair of trees is unicornish (magic) if the trees have the same number of blue nodes. You need to output a set of toggle operations, and the edge to be cut, such that at the end the resulting two trees have the same number of blue nodes.

![](images/unicorn-3824876_960_720.png)

**AHA!** You thought this was gonna be an easy task, but there's a catch! Bogdan is colorblind!  So he doesn't know the initial coloring of the tree, except for the fact that there are $K$ blue nodes. So he asks you to find a set of toggle operations and a cut such that for any possible initial colouring of the tree, the resulting pair of two trees is unicornish! In case this is not possible, you must tell him so, because pointless hope is a dangerous thing.

## Standard input

The first line will contain two integers, $N$ and $K$.

The following $N-1$ lines will each contain two numbers $x$ and $y$ meaning there's an edge between nodes $x$ and $y$ in our tree.

## Standard output

In case there is no way of obtaining the unicornish pair, output `-1`, otherwise, output at most $10^6$ lines, each line denoting a toggle operation or the final cut.

A toggle operation will be represented by a line starting with the string `flip` followed by a number $x$, denoting the node to be toggled, both separated by a space.

The cut operation will be represented by a line starting with the string `cut` followed by two numbers $x$ and $y$ denoting the endpoints of the edge to be cut, all separated by spaces. There can be at most one cut operation in the output.

## Constraints and notes

- $2 \le N\le 10^5$
- $1 \le K < N$
- Big thanks to the actual Bogdan Ciobanu for being a true superman in the making of this contest

## Examples

### Example 1

Input:
```
3 1
1 2
2 3
```

Output:
```
flip 1
cut 2 1
```

Explanation:

For every valid coloring of the tree (with only one blue node), changing the color of the first and then cutting the $(1, 2)$ edge will leave us with two trees with the same number of blue nodes

### Example 2

Input:
```
5 2
1 2
1 3
1 4
1 5
```

Output:
```
-1
```

Explanation:

There is no way to apply the operations such that for any initial valid coloring (with only two blue nodes), in the end we'll end up with two trees with the same number of blue nodes.
