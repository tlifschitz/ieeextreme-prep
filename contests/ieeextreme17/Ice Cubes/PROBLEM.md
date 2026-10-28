# Ice Cubes

**IEEEXtreme 17.0** · Time limit: 2000 ms · Memory limit: 512 MB

**CS Academy:** <https://csacademy.com/ieeextreme-practice/task/icecubes/>

Vincent lives in a town where coffee is very popular. The town's map is a grid consisting of $N \times M$ blocks and there's a coffee shop in each block. In the summer, all coffee shops sell ice coffee and Vincent, who's especially fond of ice-cold drinks, knows the exact number of icecubes that each coffee shop serves their ice coffee with. Let's say that the shop located at coordinates $(i, j)$ serves coffee with $G_{i, j}$ icecubes.

Vincent likes the coffee when the number of icecubes is at least $B$. If it's less than $B$, he says it's "bad" coffee and he'll try to avoid it.

On a particularly hot day, Vincent is up for an ice coffee Marathon. He will go from his home, at the upper-left corner of the map, to his work, at the lower-right corner of the map, moving either to the right or downwards in the map and buying coffee in each and every coffee shop that he will visit on the way. Vincent wants to maximize the total number of icecubes that he will get in all the coffees that he will buy. He is willing to buy a few "bad" coffees to achieve the maximum, as long as the number of consecutive "bad" coffees that he buys is always less than $K$.

Help Vincent determine the maximum number of icecubes he can obtain in this way!

## Standard Input

The first line will contain the number $T$ of tests that will be performed. Then, the descriptions of the $T$ tests will follow.

For each test, the first line will contain four space-separated integers: $N$, $M$, $K$, $B$.

This will be followed by $N$ lines, corresponding to the grid's rows. Each will contain $M$ space-separated integers.

## Standard Output

The output must consist of exactly $T$ lines, each corresponding to one test, in order of appearance. The line corresponding to test $n$ (where $1 \le n \le T$) must contain:

`Case`$\ n$`:` $\mathit{result}_n$

where $\mathit{result}_n$ is the answer corresponding to the $n$-th test: an integer number (the maximum number of icecubes that can be obtained) or the word "IMPOSSIBLE" (if there's no path that meets Vincent's restrictions).

## Constraints and notes

- $1 \le T \le 10$
- $1 \le N \le 1000$
- $1 \le M \le 1000$
- $1 \le K \le 20$
- $1 \le B \le 1000$
- $0 \le G_{i,j} \le 1000$ for all grid cells $(i, j)$

## Examples

### Example 1

Input:
```
3
2 3 2 5
6 6 1
1 1 5
3 4 3 7
5 5 6 5
3 6 3 5
7 1 8 4
4 4 3 6
9 5 3 3
9 1 1 5
3 1 3 5
1 1 3 2
```

Output:
```
Case 1: 18
Case 2: 28
Case 3: IMPOSSIBLE
```

Explanation:

In the first test, the optimal path is **6+6+1+5**, giving a total of 18 icecubes. In fact, there are two such paths. Notice that, along this path, there are no $K=2$ or more consecutive values that are less than $B=5$ (there is just one such value).

In the second test, the optimal path is $5+3+7+1+8+4$, giving a total of 28 icecubes. There are no $K=3$ or more consecutive values that are less than $B=7$. Notice also that the path $5+5+6+5+5+4$ gives a total of 30 icecubes but violates the restriction about consecutive small values.

In the third test, there is no way to get to the bottom-right corner without passing from at least $K=3$ consecutive values that are less than $B=6$.
