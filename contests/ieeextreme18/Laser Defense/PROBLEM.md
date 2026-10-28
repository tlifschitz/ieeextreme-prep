# Laser Defense

**IEEEXtreme 18.0** · Time limit: 1000 ms · Memory limit: 256 MB

**CS Academy:** <https://csacademy.com/ieeextreme-practice/task/laser-defense/>

A group of thieves has decided to steal the statements of this year's IEEEXtreme. In order to do so, they need to cross a parking lot in front of the IEEE headquarters.

 The parking lot can be viewed as a square having the lower left corner at $(0, 0)$ and the upper right one at $(L, L)$. In the lower left corner and the lower right corner of the parking lot, the scientific committee has installed two lasers that send several beams of light which can detect movement. Check out the image below for a better understanding.

![](images/Screenshot-2024-10-21-at-15.30.10.png)

The two lasers are marked with $A$ and $B$. The left laser sends beams of light that intersect either the upper or the right sides of the square. The right laser sends beams that intersect either the upper or the left sides. In the example above, laser $A$ sends $3$ beams, while laser $B$ sends $2$.

The laser beams divide the parking lot into several areas, in the example above there are $11$ such areas. The thieves have managed to hack into the IEEE servers and know the number and the direction of the laser beams. Your task is to compute the number of resulting areas.

## Standard input

The first line contains three integers $L$, $N$ and $M$, representing the size of the parking lot, the number of beams sent by laser $A$ and the number of beams sent by laser $B$, respectively.

Each of the following $N$ lines describes a laser beam sent by $A$. It contains a character, either `U` or `R`, followed by an integer coordinate $C$. The character `U` specifies that the beam intersects the upper side, and $C$ is the $x$ coordinate of the intersection point. Similarly, the character `R` specifies that the beam intersects the right side, and $C$ is the $y$ coordinate of the intersection point.

Each of the following $M$ lines describes a laser beam sent by $B$. It contains a character, either `U` or `L`, followed by an integer coordinate $C$. The character `U` specifies that the beam intersects the upper side, and $C$ is the $x$ coordinate of the intersection point. Similarly, the character `L` specifies that the beam intersects the left side, and $C$ is the $y$ coordinate of the intersection point.

## Standard output

Print a single integer representing the number of resulting areas.

## Constraints and notes

- $2 \leq L \leq 10^9$
- $0 \leq N, M \leq 10^5$
- $0 < C < L$
- The input does not contain identical laser beams

## Examples

### Example 1

Input:
```
30 3 2
U 10
U 25
R 10
L 15
U 20
```

Output:
```
11
```

Explanation:

This test case corresponds to the image in the statement.

![](images/Screenshot-2024-10-21-at-15.30.10.png)

### Example 2

Input:
```
20 3 3
U 10
U 15
R 10
L 15
U 5
U 15
```

Output:
```
14
```

Explanation:

There are $14$ areas:

![](images/Screenshot-2024-10-24-at-16.56.23.png)
