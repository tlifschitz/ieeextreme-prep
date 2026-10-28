# The Fast and the Curious

**IEEEXtreme 11.0** · Time limit: 2000 ms · Memory limit: 256 MB

**CS Academy:** <https://csacademy.com/ieeextreme-practice/task/e1e444f71a2a7a69baf4c61ed756aa55/>

Jason Bourne is driving his car through the countryside, desperately trying to escape the black ops group «Operation Treadstone», that is on his tail. He is navigating through a map of the area and he can spot $n$ ($1 \leq n \leq 10^5$) cities in the vicinity, numbered from $1$ to $n$, connected by $m$ two-way roads between them. There is at most one road between any two cities.

Jason must avoid «looping routes» at all costs because if he ends up in one, he can get trapped and caught. A «looping route» is a route of at least three cities, where each city is connected to the previous city with a road, the last city is also connected to the first city with a road and no city appears twice in the route. Jason knows that the only way to escape Treadstone, is by avoiding all cities that form «looping routes». Help Jason escape by finding the remaining cities on the map.

## Standard input

The first line of the input consists of two space-separated integers, $n$ and $m$. $n$ is the number of cities on the map and $m$ is the roads that connect them.

The next $m$ lines each contain two integers <Latex value="a_{i}" /> and <Latex value="b_{i}" />, indicating that there is a road between city <Latex value="a_{i}" /> and city <Latex value="b_{i}" />.

## Standard output

Print the numbers of the cities which are not on any looping route, one per line, in ascending order. If no such city exists, do not print anything.

## Constraints and notes

- $1 \leq n \leq 10^5$
- $0 \leq m \leq 3 * 10^5$
- $1 \leq a_{i}, b_{i} \leq n, a_{i} \neq b_{i}$
- There is at most one road between any two cities.

## Examples

### Example 1

Input:
```
5 5
4 5
5 2
2 4
1 3
3 2
```

Output:
```
1
3
```

Explanation:

In the map below, there are $5$ cities. Cities $2$, $4$ and $5$ form a looping route, but cities $1$ and $3$ are not on any looping routes.

<Graph indexType="custom" height="220" width="220"

nodes={[

  {options:{fixed:true},label:1,center:{x:160,y:190}},

  {options:{fixed:true},label:2,center:{x:25,y:90}},

  {options:{fixed:true},label:3,center:{x:60,y:190}},

  {options:{fixed:true},label:4,center:{x:190,y:90}},

  {options:{fixed:true},label:5,center:{x:100,y:25}}]}

edges={[{source:1,target:3},{source:0,target:2},{source:2,target:1},{source:1,target:4},{source:3,target:4}]} />
