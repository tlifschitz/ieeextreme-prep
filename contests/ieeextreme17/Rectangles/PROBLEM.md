**CS Academy:** <https://csacademy.com/ieeextreme-practice/task/rectangles/>

# Rectangles

**IEEEXtreme 17.0** · Time limit: 2000 ms · Memory limit: 512 MB

Alice has a collection of square blocks that she likes to arrange in groups. She has constraints on her groups:

1) Each group must have at least $p$ and no more than $q$ blocks.

2) Suppose that the ith group has $n_i$ blocks. She will arrange the blocks in a rectangle, with dimensions $w_i$ and $h_i$, such that $w_i \times h_i = n_i$.

3) Each group size must be unique, and we should guarantee that, for the chosen group sizes, any possible set of rectangles will have dimensions that are relatively prime. In other words, given the group sizes, all of the following must hold for any set of possible rectangles:

For all $i \neq j$, $gcd(w_i, w_j) = 1$, $gcd(h_i, h_j) = 1$, and $gcd(h_i,w_j) = 1$, where $gcd$ is the greatest common divisor.

## Standard Input

The input consists of two-space separated integers, $p$ followed by $q$.

## Standard Output

The maximum number of blocks that Alice could have in her collection, subject to the constraints listed above.

## Constraints and notes

- $1 \le p \le q \le 10^9$
- $q - p \le 100$

## Examples

### Example 1

Input:
```
1 12
```

Output:
```
41
```

Explanation:

Alice could have divide 41 blocks into the following group sizes: {1, 5, 7, 8, 9, 11}.  These groups could be arranged into the following rectangles:

* Group of 1: 1x1
* Group of 5: 1x5 or 5x1
* Group of 7: 1x7 or 7x1
* Group of 8: 1x8, 2x4, 4x2, or 8x1
* Group of 9: 1x9, 3x3, or 9x1
* Group of 11: 1x11 or 11x1

No matter how we arrange the rectangles, the dimensions of different rectangles will be relatively prime.

Consider the group of 8. The possible widths and heights of rectangles for this group include 1, 2, 4, and 8. The possible widths and heights of the rectangles for the other groups are 1, 3, 5, 7, 9, and 11. Note that the 1 is the greatest common divisor of any dimension for this rectangle and any dimension for a rectangle in another group.
