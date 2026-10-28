# Star Road

**IEEEXtreme 18.0** · Time limit: 1000 ms · Memory limit: 256 MB

**CS Academy:** <https://csacademy.com/ieeextreme-practice/task/star-road/>

You are a food critic that just finished competing in the IEEExtreme, and you started traveling through a country with $N$ cities. Each city has a restaurant which is rated by a number of stars, indicating how good it is. The country has $N - 1$ roads, such that there is a unique simple path between any two cities.

As a very strict food critic, you only eat at a new restaurant if it has strictly more stars than the one where you last dined. However, you also love to eat, so you want to visit the maximum number of restaurants possible while following these rules.

You are tasked with planning a journey that starts at some city $A$ and ends at some city $B$, ensuring that:

- You can eat in as many restaurants as possible during the journey.
- You never go back through the same road once you've passed it.

Note that you don't have to eat in every single city you visit, but can simply pass through it.

Can you help the critic maximize their dining experience?

## Standard input

The first line contains an integer $N$,  the number of cities.

The second line contains $N$ integers, where the $i$-th integer represents the number of stars of the restaurant in city $i$.

The following $N - 1$ lines each contain two integers $u$ and $v$, indicating a road between cities $u$ and $v$.

## Standard output

Print the maximum number of restaurants the critic can dine at, under the given constraints.

## Constraints and notes

- $2 \leq N \leq 10^{5}$
-  $1 \leq S_i \leq 10^{5}$ where by  $S_i$ we understand the number of stars for the restaurant in city $i$.
- $1 \leq u \not = v \leq N$ for every road.

## Examples

### Example 1

Input:
```
6
4 1 3 2 5 3
1 2
1 3
1 4
4 5
4 6
```

Output:
```
3
```

Explanation:

The city network can be seen in the drawing below, where each city's label also has the number of stars of it's restaurant in brackets.

<Graph indexType="custom" height="360" width="250" nodes={[{options:{circleAttr:{radius:25}},label:"4 (2*)",center:{x:192.4,y:240.3}},{options:{circleAttr:{radius:25}},label:"5 (5*)",center:{x:168.1,y:173.2}},{options:{circleAttr:{radius:25}},label:"1 (4*)",center:{x:258.9,y:251}},{options:{circleAttr:{radius:25}},label:"2 (1*)",center:{x:297,y:193.2}},{options:{circleAttr:{radius:25}},label:"3 (3*)",center:{x:232.2,y:185.1}},{options:{circleAttr:{radius:25}},label:"6 (3*)",center:{x:126.6,y:227}}]} edges={[{source:0,target:1},{source:2,target:0},{source:2,target:3},{source:2,target:4},{source:0,target:5}]} />

A solution of size 3 is one where you go through cities $2$, $1$, $4$ and $5$, and in which you eat at:

- restaurant  $2$, which has $1$ star
- restaurant $1$, which has $4$ stars
- restaurant $5$, which has $5$ stars

### Example 2

Input:
```
7
4 1 3 2 5 3 6
1 2
1 3
1 4
4 5
4 6
5 7
```

Output:
```
4
```

### Example 3

Input:
```
6
1 1 1 1 1 1
1 2
1 3
1 4
4 5
4 6
```

Output:
```
1
```
