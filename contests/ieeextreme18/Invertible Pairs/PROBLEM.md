# Invertible Pairs

**IEEEXtreme 18.0** · Time limit: 750 ms · Memory limit: 512 MB

**CS Academy:** <https://csacademy.com/ieeextreme-practice/task/invertible-pairs/>

Given an integer array $A$ ($1$-indexed) with even length $n$. You can do the following operation as many times as you want:

- Choose a pair of positions $2k - 1$ and $2k$ and multiply both $A_{2k - 1}$ and $A_{2k}$ by $-1$.

After finishing your operations, you must compute the maximum subarray sum of the resulting array. Maximize this value.

## Standard input

The first line contains an integer $T$, the number of test cases.

The following lines describe $t$ test cases. The first line of each test case contains an even integer $N_{i}$, the length of the array. The second line contains $N_{i}$ integers $A_{j}$, the $j$-th integer is the $j$-th element of the array.

## Standard output

Print $t$ lines, the $i$-th line must contain the answer to the $i$-th test case.

## Constraints and notes

- $1 \leq T \leq 10^{5}$.
- $1 \leq \sum\limits_{i = 1}^{T}N_{i} \leq 4 * 10^{5}$.
- $2 \leq N_{i} \leq 2 * 10^{5}$ for every $i = 1, \ldots, T$.
- $N_{i}$ is even for every $i = 1, \ldots, T$.
- $|A_{j}| \leq 10^{4}$ for every valid $j$.

## Examples

### Example 1

Input:
```
3
4
5 -10 7 -2
2
7 -8
2
5 4
```

Output:
```
17
8
9
```

Explanation:

For the first test case, it's possible to apply the operation on position $2$, which gives the array $(-5, 10, 7, -2)$ and its maximum subarray sum is $10 + 7 = 17$.

For the second test case, it's possible to apply the operation on position $2$, which gives the array $(-7, 8)$ and its maximum subarray sum is $8$.

For the third test case, there is no need to apply the operation since all the values are positive, so the maximum subarray sum is $5 + 4 = 9$.

### Example 2

Input:
```
2
6
-8 -6 9 5 -6 -10
2
-1 -8
```

Output:
```
44
9
```

Explanation:

For the first test case, it's possible to apply the operation on positions $2$ and $6$, which gives the array $(8, 6, 9, 5, 6, 10)$ and its maximum subarray sum is $8 + 6 + 9 + 5 + 6 + 10 = 44$.

For the second test case, it's possible to apply the operation on position $2$, which gives the array $(1, 8)$ and its maximum subarray sum is $1 + 8 = 9$ .

### Example 3

Input:
```
2
6
9 -5 -3 8 0 -6
2
-8 0
```

Output:
```
16
8
```

Explanation:

For the first test case, it's possible to apply the operation on positions $2$ and $6$, which gives the array $(-9, 5, -3, 8, 0, 6)$ and its maximum subarray sum is $5 + (-3) + 8 + 0 + 6 = 16$.

For the second test case, it's possible to apply the operation on position $2$, which gives the array $(8, 0)$ and its maximum subarray sum is $8 + 0 = 8$ .

### Example 4

Input:
```
3
2
-9 0
2
-2 1
6
-6 3 7 1 -4 -6
```

Output:
```
9
2
21
```

Explanation:

For the first test case, it's possible to apply the operation on position $2$, which gives the array $(9, 0)$ and its maximum subarray sum is $9 + 0 = 9$ .

For the second test case, it's possible to apply the operation on position $2$, which gives the array $(2, -1)$ and its maximum subarray sum is $2$ .

For the third test case, it's possible to apply the operation on position $6$, which gives the array $(-6, 3, 7, 1, 4, 6)$ and its maximum subarray sum is $3 + 7 + 1 + 4 + 6 = 21$.
