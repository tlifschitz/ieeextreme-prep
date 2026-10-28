# Increasing-decreasing permutations

**IEEEXtreme 18.0** · Time limit: 1000 ms · Memory limit: 256 MB

**CS Academy:** <https://csacademy.com/ieeextreme-practice/task/increasing-decreasing-permutation/>

There is a permutation of odd length $N$ called $P$ $(P_{1},P_{2},\ldots,P_{N})$. The goal is to change the permutation in the smallest number of $\textbf{adjacent}$ swaps so that the first $\frac{N+1}{2}$ items of the permutation are sorted in ascending order and the last $\frac{N+1}{2}$ items are sorted in descending order. For example the permutation $(1, 2, 3, 4, 5)$ can be changed into $(1, 2, 5, 4, 3)$ in $3$ swaps.

For each permutation of length $N$, let's find the minimum number of swaps needed to organise it in increasing-decreasing order. What is the sum of all those values for all permutations? Now, the sum can be very big, please answer it modulo a prime number $M$.

## Standard input

The first line of input contains two integers $N$ and $M$.

## Standard output

Print the sum of the minimum number of swaps needed to reach the desired order for each permutation of length $N$ modulo $M$.

## Constraints and notes

- $3 \leq N \leq 23$.
- $2 \leq M \leq 2^{30}$.
- $M$ is prime.

## Examples

### Example 1

Input:
```
3 107
```

Output:
```
4
```

Explanation:

The permutations are the following:

- $(1,2,3) \rightarrow (1,3,2)$ requires 1 swap.
- $(1,3,2) \rightarrow (1,3,2)$ requires 0 swaps.
- $(2,1,3) \rightarrow (2,3,1)$ requires 1 swap.
- $(2,3,1) \rightarrow (2,3,1)$ requires 0 swaps.
- $(3,1,2) \rightarrow (1,3,2)$ requires 1 swap.
- $(3,2,1) \rightarrow (2,3,1)$ requires 1 swap.
