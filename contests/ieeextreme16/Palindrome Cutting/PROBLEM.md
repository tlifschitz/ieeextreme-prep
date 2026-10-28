# Palindrome Cutting

**IEEEXtreme 16.0** · Time limit: 2000 ms · Memory limit: 256 MB

**CS Academy:** <https://csacademy.com/ieeextreme-practice/task/palindrome-cutting/>

Consider an **even** length array $S$ of numbers from $1$ to $M$. We will call this array $good$ if it can be split into any number of contiguous subsequences of **even** length, each one being a palindrome. Given $N$ and $M$, count the number of **good** arrays of length $N$ with numbers from $1$ to $M$ modulo $998244353$.

## Standard input

The first line of input contains two integers $N$ and $M$.

## Standard output

The first line of output should contain one integer $-$ the number of **good** arrays of length $N$ of numbers from $1$ to $M$ modulo $998244353$.

## Constraints and notes

- $N$ is **even**,
- $2 \leq N \leq 5 \cdot 10^5$,
- $1 \leq M < 998244353$

## Examples

### Example 1

Input:
```
4 2
```

Output:
```
6
```

Explanation:

The 6 good arrays are:

$1\ 1\ 2\ 2$: can be split into $(1\ 1)\ (2\ 2)$

$2\ 2\ 1\ 1$: can be split into $(2\ 2)\ (1\ 1)$

$1\ 1\ 1\ 1$: the entire array is a palindrome

$1\ 2\ 2\ 1$: the entire array is a palindrome

$2\ 1\ 1\ 2$: the entire array is a palindrome

$2\ 2\ 2\ 2$: can be split into $(2\ 2)\ (2\ 2)$
