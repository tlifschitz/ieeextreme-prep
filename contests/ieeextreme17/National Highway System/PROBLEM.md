**CS Academy:** <https://csacademy.com/ieeextreme-practice/task/national_highways/>

# National Highway System

**IEEEXtreme 17.0** · Time limit: 5000 ms · Memory limit: 256 MB

The remote country of Xtremeland is planning a highway system that will allow for travel between all its cities. There is a lot of controversy over which cities should be directly connected. As a result, the following system will be used to impartially select these roads.

The costs for roads that could be built between pairs of cities will be estimated. Then, the country will select the roads that make up the cheapest highway network, that could provide routes between any pair of cities.  If there is more than one possible cheapest network, then the roads from all possible cheapest networks will be selected.

## Standard Input

Input begins with an integer $n$ on a line by itself that indicates the number of potential roads with cost estimates.

The next $n$ lines have the following format:

 $n_i$ $n_j$ $c_{ij}$

where $n_i$ is a city name, $n_j$ is a city name, and $c_{ij}$ is an integer representing the cost of a 2-way highway that connects $n_i$ and $n_j$.

## Standard Output

Output the cost of the highway system, that meets the requirements above.  If there is no way to build a highway system that connects all of the cities, then output -1.

## Constraints and notes

- $1 \leq n \leq 400,000$
- $1 \leq c_{ij} \leq 1,000,000$ for all $c_{ij}$

Each city name will consist of between 1 and 5 lowercase letters.

All cities will be listed in at least one of the input lines.

## Examples

### Example 1

Input:
```
5
a b 1
b c 2
a c 2
b d 4
a d 5
```

Output:
```
9
```

Explanation:

There are two road networks that cost 7 units:

a-b, b-c, b-d

and

a-b, a-c, b-d

We must, therefore, build all of the roads in the networks, a-b, a-c, b-c, and b-d, at a cost of 9.

### Example 2

Input:
```
5
a b 1
b c 1
a c 1
b d 1
a d 1
```

Output:
```
5
```

Explanation:

There are a number of road networks that cost 3 and connect all cities, for example:

a-b, b-c, b-d

a-c, b-c, a-d

a-d, b-d, b-c

Since all of the roads appear in at least one of these cheapest networks, we must build all roads at a cost of 5.

### Example 3

Input:
```
5
a b 1
b c 1
a c 1
b d 1
f e 1
```

Output:
```
-1
```

Explanation:

There is no way to build a network that connects city e or city f to cities a, b, c, or d, and therefore, we output -1.
