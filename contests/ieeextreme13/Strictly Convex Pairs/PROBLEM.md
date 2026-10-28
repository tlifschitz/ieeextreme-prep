# Strictly Convex Pairs

**IEEEXtreme 13.0** · Time limit: 3000 ms · Memory limit: 256 MB

**CS Academy:** <https://csacademy.com/ieeextreme-practice/task/strictly-convex-pairs/>

There is a polygon with $N$ vertices in standard 2-D Cartesian coordinates. The polygon is *strictly convex*. That is, the polygon is convex, and there are no three collinear vertices (i.e. lying in the same straight line).

There are $M$ other distinct points which are located strictly inside or outside the polygon (not on polygon edges). Andy wants to pick two different points $a$ and $b$ from those $M$ points so that he can connect $a$ and $b$ with a straight *line segment* without intersecting or touching the polygon. Andy is curious about how many different unordered pairs of points $a$ and $b$ he can pick. Can you help Andy to count that?

Note: An unordered pair $(a, b)$ is the same as the pair $(b, a)$.

## Standard input

The first line of the input contains two integers, $N$ and $M$.

The next $N$ lines describe the convex polygon. Each line contains two integers indicating $x$-coordinate and $y$-coordinate of one vertex. The vertices are given in counter-clockwise order.

The next $M$ lines describe points that Andy can pick. Each line contains two integers indicating $x$-coordinate and $y$-coordinate of one point.

## Standard output

Print one integer representing the number of pairs.

## Constraints and notes

- $3 \leq N \leq 2 \times 10^{5}$
- $2 \leq M \leq 2 \times 10^{5}$
- $-10^{9} \leq x$-coordinate, $y$-coordinate $\leq 10^{9}$
- The polygon is strictly convex.
- All $M$ points are distinct and not located on any polygon edges.

## Examples

### Example 1

Input:
```
4 6
4 0
0 4
-4 0
0 -4
5 0
1 0
-1 0
3 3
4 -2
4 4
```

Output:
```
5
```

Explanation:

<Geometry xDomain={[-5, 11]} yDomain={[-5, 5]} circles={[]} points={[{x:5,y:0,label:'(5,0)'}, {x:1,y:0,label:'(1,0)'}, {x:-1,y:0,label:'(-1,0)'}, {x:3,y:3,label:'(3,3)'}, {x:4,y:-2,label:'(4,-2)'}, {x:4,y:4,label:'(4,4)'}]} lines={[]} polygons={[[{x:4,y:0}, {x:0,y:4}, {x:-4,y:0}, {x:0,y:-4}]]}/>

The five pairs that can be picked are:

- point $(5, 0)$ and point $(3, 3)$
- point $(5, 0)$ and point $(4, -2)$
- point $(5, 0)$ and point $(4, 4)$
- point $(1, 0)$ and point $(-1, 0)$
- point $(3, 3)$ and point $(4, 4)$
