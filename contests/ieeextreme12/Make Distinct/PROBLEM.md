# Make Distinct

**IEEEXtreme 12.0** · Time limit: 1000 ms · Memory limit: 256 MB

**CS Academy:** <https://csacademy.com/ieeextreme-practice/task/make-distinct/>

You are given an array of $N$ integers, $A$. An operation involves taking a number from the array and either adding or subtracting $1$ from it. What is the minimum number of operations to make $A$ have only distinct elements.

## Standard input

The first line contains an integer $N$.

The second line contains $N$ elements, representing $A$.

## Standard output

Print the answer on the first line.

## Constraints and notes

- $1 \leq N \leq 2 \cdot 10^5$
- $1 \leq A_i \leq N$ for all valid $i$

## Examples

### Example 1

Input:
```
7
2 3 4 2 2 1 3
```

Output:
```
7
```

Explanation:

Transform into `2 4 5 -1 1 0 3` with a cost equal to `(0 + 1 + 1 + 3 + 1 + 1)`.

### Example 2

Input:
```
4
3 3 3 3
```

Output:
```
4
```

Explanation:

Transform into `5 4 3 2`.

### Example 3

Input:
```
5
5 4 4 5 4
```

Output:
```
4
```

Explanation:

Transform into `6 3 4 5 2`.
