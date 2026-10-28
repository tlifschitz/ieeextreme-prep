# Happy Numbers

**IEEEXtreme 17.0** · Time limit: 500 ms · Memory limit: 256 MB

**CS Academy:** <https://csacademy.com/ieeextreme-practice/task/happy_numbers/>

A happy number $n$ is a positive integer defined by the following process:

- Starting with $n$, replace it with the sum of the squares of its digits.
- Repeat the process until the number reaches 1 (where it will stay in eternal happiness), or repeats in an infinite loop that does not include 1.
- Those numbers for which this process ends in 1 are happy numbers.

For example, 23 is a happy number: 23 -> 13 -> 10 -> 1 -> 1.

However, 89 is not a happy number (cycle in bold): 89 -> 145 -> *42 -> 20 -> 4 -> 16 -> 37 -> 58 -> 89 -> 145* -> 42 -> 20 -> 4

Given two numbers $a, b$ return the number of happy numbers between $a$ and $b$ (inclusive).

## Standard Input

Each test contains two space separated integers $a, b$

## Standard Output

For each test case, output a single integer, the number of happy numbers between $a$ and $b$ (inclusive).

## Constraints and notes

- $1 \leq a \leq b \leq 10^{16}$

## Examples

### Example 1

Input:
```
1 44
```

Output:
```
10
```

Explanation:

There are 10 happy numbers between 1 and 44 (inclusive):

1, 7, 10, 13, 19, 23, 28, 31, 32, 44
