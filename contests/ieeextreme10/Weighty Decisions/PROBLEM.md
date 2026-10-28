# Weighty Decisions

**IEEEXtreme 10.0** · Time limit: 2000 ms · Memory limit: 512 MB

**CS Academy:** <https://csacademy.com/ieeextreme-practice/task/weighty-decisions/>

You have $N$ lead balls weighing respectively $w_1, w_2, ... w_N$ grams each.

The list of weights is given but we do not know which weight corresponds to which ball.

Our objective is, using a two-pan balance, to find the minimum number of comparisons to associate each ball with its corresponding weight.

A weighing is obtained by putting a subset $A$ of balls on one pan and a disjoint subset $B$ of balls on the other pan. Three outcomes are possible: $A$ weighs more than $B$, $B$ weighs more than $A$ or they weigh the same.

## Standard input

The input of the problem is a list of integers, each on a line by itself. These integers correspond to the weights $w_1, w_2, ..., w_n$.

## Standard output

For each test case, output, on a line by itself, the minimum number of sufficient comparisons to identify each ball.

## Constraints and notes

- Each weight is between $1$ and $100$.
- There will never be more than $9$ balls. Moreover, there will never be more then $7$ different weights.  For example, if there are $8$ balls, at least two balls must have the same weight.

## Examples

### Example 1

Input:
```
2
2
2
3
```

Output:
```
2
```
