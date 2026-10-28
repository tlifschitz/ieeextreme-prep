# Pair Swap Teams

**IEEEXtreme 13.0** · Time limit: 1000 ms · Memory limit: 256 MB

**CS Academy:** <https://csacademy.com/ieeextreme-practice/task/pair-swap-teams/>

In a parallel universe, Sara also invented a new board game, and she has invited all her friends to play at her house. Everyone is already sitting at a big circular table. Sara randomly attributes a team, represented by a letter from `A` to `D`, to each friend. In order to group teams around the table, a subset of players should get up and change their places.

Contrary to the other universe, they have to swap places in pairs.

What is the minimum number of swaps such that all the players in any team occupy a contiguous sequence of chairs?

## Standard input

The first line of the input contains the number of times, $T$, that you need to solve the challenge.

Each of the following $T$ lines contains a string $S_i$ of length $L_i$.

## Standard output

For each test, output a line containing a single integer representing the minimum number of seat swaps.

## Constraints and notes

- $1 \le T \leq 10$
- $1 \leq L_i \leq 10^5$
- Teams are represented by characters (`A`, `B`, `C` or `D`)
- The same player can be involved in multiple seat swaps

## Examples

### Example 1

Input:
```
5
CBBACC
DBCA
CCACACC
ABCABCABC
ABCDABCDABCDABCD
```

Output:
```
0
0
1
3
6
```
