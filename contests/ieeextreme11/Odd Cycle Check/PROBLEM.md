# Odd Cycle Check

**IEEEXtreme 11.0** · Time limit: 1000 ms · Memory limit: 128 MB

**CS Academy:** <https://csacademy.com/ieeextreme-practice/task/e21a405d32da71227e2d5fb313fd19d4/>

In a distant country there are $n$ ($1 \leq n \leq 10^4$) cities, but there aren't any roads connecting them. To make things better, the king of the country has decided to build exactly one road every day, the $i^{th}$ road connecting two distinct cities $a_i$ and $b_i$. Because the country has the technology to build bridges and tunnels, you can assume two roads never intersect.

The system of roads is /special/ if it's possible to start in some city $a$, move along an *odd* number of roads and end up in the starting city $a$.

Your goal is to find the first day when the system of roads becomes special. This problem is interactive, meaning you'll have to communicate with a special program called the /interactor/. More details follow below.

## Interaction

First you should read a single integer $n$.

Each of the following lines contains two integers $a$ and $b$, representing two cities connected by a new road.

After reading every pair of integers $a$ and $b$, you should output $1$ if the graph is not special, or $0$ if it just became special. In case you print $0$, your program should stop.

*Warning:* You should print your answer ($0$ or $1$) *before* reading the next line of input.

*Warning 2:* Don't forget to flush after every output operation!

## Constraints and notes

- $3 \leq n \leq 10^4$
- It is guaranteed the system of roads will become special in the first $2 * 10^4$ days.

## Examples

### Example 1

Input:
```
4 4 4
1 4
2 1
3 2
4 2
```

Output:
```

```

### Example 2

Input:
```
5 4 5
1 2
1 3
4 2
3 4
4 1
```

Output:
```

```

### Example 3

Input:
```
5 5 5
1 2
2 3
3 4
4 5
5 1
```

Output:
```

```

### Example 4

Input:
```
9 6 9
1 3
5 6
4 3
4 6
3 5
6 1
2 1
2 4
3 6
```

Output:
```

```
