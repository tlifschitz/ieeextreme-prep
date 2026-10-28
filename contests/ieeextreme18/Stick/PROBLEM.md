# Stick

**IEEEXtreme 18.0** · Time limit: 500 ms · Memory limit: 256 MB

**CS Academy:** <https://csacademy.com/ieeextreme-practice/task/stick/>

There are $N$ squares on a cartesian plane. The $i$-th square has bottom-left corner on $(i \times K-L,i \times K-L)$ and top-right corner on $(i \times K+L,i \times K+L)$. What is the area of the union of the squares?

## Standard input

The input consists of one line containing three integers $N$, $K$, and $L$.

## Standard output

The output should contain one integer representing the area of of the union of the squares.

## Constraints and notes

- $1 \le N, K \le 10^9$
- $1 \le L \le 5 \times 10^4$

## Examples

### Example 1

Input:
```
4 1 2
```

Output:
```
37
```

Explanation:

The corresponding squares are:

- Square $0$: $(-2, -2), (-2, 2), (2, 2), (2, -2)$.
- Square $1$: $(-1, -1), (-1, 3), (3, 3), (3, -1)$.
- Square $2$: $(0, 0), (0, 4), (4, 4), (4, 0)$.
- Square $3$: $(1, 1), (1, 5), (5, 5), (5, 1)$.

<Geometry circles={[]} points={[]} lines={[]} polygons={[[{"x": -2, "y": -2}, {"x": -2, "y": 2}, {"x": 2, "y": 2}, {"x": 2, "y": -2}],[{"x": -1, "y": -1}, {"x": -1, "y": 3}, {"x": 3, "y": 3}, {"x": 3, "y": -1}],[{"x": 0, "y": 0}, {"x": 0, "y": 4}, {"x": 4, "y": 4}, {"x": 4, "y": 0}],[{"x": 1, "y": 1}, {"x": 1, "y": 5}, {"x": 5, "y": 5}, {"x": 5, "y": 1}],]} segments={[]} xDomain={[-3, 14]} yDomain={[-3, 7]} />

It's easy to see the total area is equal to $37$ .

### Example 2

Input:
```
3 3 1
```

Output:
```
12
```

Explanation:

The corresponding squares are:

- Square 0: $(-1, -1), (-1, 1), (1, 1), (1, -1)$.
- Square 1: $(2, 2), (2, 4), (4, 4), (4, 2)$.
- Square 2: $(5, 5), (5, 7), (7, 7), (7, 5)$.

<Geometry circles={[]} points={[]} lines={[]} polygons={[[{"x": -1, "y": -1}, {"x": -1, "y": 1}, {"x": 1, "y": 1}, {"x": 1, "y": -1}],[{"x": 2, "y": 2}, {"x": 2, "y": 4}, {"x": 4, "y": 4}, {"x": 4, "y": 2}],[{"x": 5, "y": 5}, {"x": 5, "y": 7}, {"x": 7, "y": 7}, {"x": 7, "y": 5}]]} segments={[]} xDomain={[-3, 14]} yDomain={[-3, 7]} />

It's easy to see that since they don't intersect, the area of their union will be $3 \times area = 3 \times 4 = 12$.

### Example 3

Input:
```
1 1 50000
```

Output:
```
10000000000
```

Explanation:

The only square consists of the points $(-50000, -50000), (-50000, 50000), (50000, 50000), (50000, -50000)$, and it has area $100000 \times 100000 = 10000000000$
