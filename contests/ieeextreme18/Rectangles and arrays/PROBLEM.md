# Rectangles and arrays

**IEEEXtreme 18.0** · Time limit: 500 ms · Memory limit: 256 MB

**CS Academy:** <https://csacademy.com/ieeextreme-practice/task/rectangles-and-arrays-ieeextreme-18/>

In the final hours of IEEExtreme, you're tasked with a challenge involving arrays and rectangles. You are given an array $A$ of $N$ integers representing heights. Your objective is to determine the largest possible area of a rectangle that can be formed using a contiguous subarray of $A$.

A rectangle is defined by selecting two indices $l$ and $r$ (with $1 \leq  l \leq r \leq N$), and choosing a height $h$ such that $h$ is *not greater than* any of the elements between $l$ and $r$, inclusive. The area of the rectangle is then calculated as $(r - l + 1) \times h$.

Additionally, you have a special ability: *you can modify the value of any element in the array once* to any positive integer between $1$ and $X$. After making this one modification, you need to determine the maximum possible area of any rectangle that can be formed.

## Standard input

The first line contains two integers $N$  and $X$, the number of elements in the array and the maximum value that you can set on an element of the array.

The second line contains $N$ integers representing the heights of the elements $A_{i}$ in the array.

## Standard output

Output a single integer representing the maximum area of a rectangle that can be formed after modifying at most one element of the array.

## Constraints and notes

- $1 \leq N \leq 10^{6}$.
- $1 \leq X \leq 10^{6}$.
- $1 \leq A_{i} \leq 10^{6}$ for every $i = 1, \ldots, N$.

## Examples

### Example 1

Input:
```
5 2
3 4 2 4 3
```

Output:
```
10
```

Explanation:

It's possible not to modify the array and then choose $h = 2$ for the whole array, which gives $2 \times 5 = 10$ as the maximum area.

### Example 2

Input:
```
5 5
3 4 1 4 3
```

Output:
```
15
```

Explanation:

It's possible to modify the third position of array to $3$ and then choose $h = 3$ for the whole array, which gives $3 \times 5 = 15$ as the maximum area.
