# Reshuffle Teams

**IEEEXtreme 13.0** · Time limit: 1000 ms · Memory limit: 256 MB

**CS Academy:** <https://csacademy.com/ieeextreme-practice/task/reshuffle-teams/>

Recently Sara invented a new board game, and she has invited all her friends to play at her house. Everyone is already sitting at a big circular table. Sara randomly attributes a team, represented by a letter from `A` to `D`, to each friend. In order to group teams around the table, a subset of players should get up and change their places.

What is the minimum number of people that need to change their seat such that all the players in any team occupy a contiguous sequence of chairs?

## Standard input

The first line of the input contains the number of times, $T$, that you need to solve the challenge.

Each of the following $T$ lines contains a string $S_i$ of length $L_i$.

## Standard output

For each test, output a line containing a single integer representing the minimum number of people that have to change their seat.

## Constraints and notes

- $1 \le T \leq 10$
- $1 \leq L_i \leq 10^5$
- Teams are represented by characters (`A`, `B`, `C` or `D`)

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
2
6
12
```

Explanation:

CBBACC -> 0 (Teams are already sitting beside each other.)

DBCA -> 0 (Teams are already sitting beside each other.)

CCACACC -> CCCAACC: 2 letters out of place

ABCABCABC -> AAABBBCCC: 6 letters out of place

ABCDABCDABCDABCD -> AAAABBBBCCCCDDDD: 12 letters out of place
