**CS Academy:** <https://csacademy.com/ieeextreme-practice/task/the-tortoise-and-the-hare/>

# The Tortoise and The Hare  

**IEEEXtreme 15.0** · Time limit: 2000 ms · Memory limit: 256 MB

In the TH-kingdom, there are $N$ cities numbered from $1$ to $N$, connected by $M$ bidirectional roads of various lengths. Tortoise Tim and Hare Hank want to race starting from city $S$ to city $T$. However, the race is unfair due to their enormous speed gap. To make the race fair, Tim can choose a city $X$, and forbid Hank to visit city $X$ during the race. Nevertheless, there must be a path from $S$ to $T$ that doesn't visit $X$, otherwise the race cannot be held. Both Tim and Hank will follow the shortest path from $S$ to $T$, i.e. a path with a minimum sum of its road lengths.

Help Tim decide which city $X$ he should choose, so that Hank's shortest path from city $S$ to city $T$ is maximized.

## Standard input

The first line contains 4 integers $N, M, S, T$. Each of the following $M$ lines contains 3 integers. The $i$th line has $a_i, b_i, d_i$, describing a bidirectional road of length $d_i$ connecting city $a_i$ with city $b_i$.

## Standard output

Print a number $X$, the city that Tim should choose. If there is no valid city, print $-1$ instead. If there are multiple solutions, you can output any of them.

## Constraints and notes

- $3 \leq N \leq 3 \times 10^5$
- $N-1 \leq M \leq 3 \times 10^5$
- $1 \leq S, T \leq N, S \neq T$
- $1 \leq a_i, b_i \leq N$
- $1 \leq d_i \leq 10^9$
- For $30\%$ of the test cases, $1 \leq N, M \leq 1000$.

## Examples

### Example 1

Input:
```
9 10 1 5
1 2 2
2 3 4
2 6 3
2 7 5
3 4 8
6 8 9
4 8 20
7 9 10
4 9 100
4 5 16
```

Output:
```
3
```

Explanation:

<Graph indexType="custom" height="400" width="400" nodes={[{label:1,center:{x:133.3,y:173.9}},{label:2,center:{x:154.4,y:218.4}},{label:3,center:{x:203.6,y:217.8}},{label:4,center:{x:252.7,y:218.5}},{label:5,center:{x:273.9,y:174.1}},{label:"6",center:{x:178.8,y:260.8}},{label:"7",center:{x:180,y:174.7}},{label:"8",center:{x:228.2,y:260.9}},{label:"9",center:{x:227.2,y:174.7}}]} edges={[{label:"2",source:0,target:1},{label:"4",source:1,target:2},{label:"3",source:1,target:5},{label:"5",source:1,target:6},{label:"8",source:2,target:3},{label:"9",source:5,target:7},{label:"20",source:3,target:7},{label:"10",source:6,target:8},{label:"100",source:3,target:8},{label:"16",source:3,target:4}]} />

If visiting city $3, 6, 7, 8, 9$ is forbidden, the length of the shortest path between $S$ and $T$ is $50, 30, 30, 30, 30$ respectively.

Choosing any other city will result in Hank not being able to get to city $T$.

### Example 2

Input:
```
7 9 1 5
1 2 10
2 7 20
2 3 10
3 7 2
3 6 5
6 7 3
3 4 10
4 6 16
4 5 10
```

Output:
```
3
```

Explanation:

The cities and roads are illustrated below:

<Graph indexType="custom" height="200" width="400" nodes={[{label:"1",center:{x:137.2,y:187.8}},{label:"2",center:{x:158.7,y:233.2}},{label:"3",center:{x:206.9,y:233.3}},{label:"6",center:{x:230.1,y:188.3}},{label:"7",center:{x:183.4,y:188.5}},{label:"4",center:{x:255.2,y:232.7}},{label:"5",center:{x:276.3,y:187.2}}]} edges={[{label:"10",source:0,target:1},{label:"20",source:1,target:4},{label:"10",source:1,target:2},{label:"2",source:2,target:4},{label:"5",source:2,target:3},{label:"3",source:3,target:4},{label:"10",source:2,target:5},{label:"16",source:5,target:3},{label:"10",source:5,target:6}]} />

If visiting city $3, 6, 7$ is forbidden, the length of the shortest path between $S$ and $T$ is $59, 40, 40$ respectively.

Choosing any other city will result in Hank not being able to get to city $T$.
