# Alfa Pool

**IEEEXtreme 13.0** · Time limit: 1000 ms · Memory limit: 362 MB

**CS Academy:** <https://csacademy.com/ieeextreme-practice/task/alfa-pool/>

In an online pool tournament, players play against each other in pairs, in the order dictated by the system. For each game, the winner earns a given number of points and the loser earns no points.

To make the tournament more interesting, the organizers decided on the following set of rules:

- The points awarded are doubled for every successive win. The first win earns 1 point, the second successive win earns 2 points, the third successive win earns 4 points, and so on.
- In case of a loss, the successive win streak resets. A subsequent win earns again 1 point.
- If a player loses twice in a row, they are eliminated from the tournament.

Find out in how many different ways a player can earn $B$ points, before being eliminated. For example, let $B = 5$.  A player can earn 5 points in 8 different ways, where a number $K$ denotes a win earning $K$ points and *X* denotes a loss.

```
1 X 1 X 1 X 1 X 1 X X
X 1 X 1 X 1 X 1 X 1 X X
1 2 X 1 X 1 X X
X 1 2 X 1 X 1 X X
1 X 1 2 X 1 X X
X 1 X 1 2 X 1 X X
1 X 1 X 1 2 X X
X 1 X 1 X 1 2 X X
```
In all the 8 scenarios above, the player exited the tournament with a total of 5 points.

## Standard input

Your program must read from the standard input. The first line contains the number of queries $N$ that you have to answer. Each of the following $N$ lines contains one query, consisting of one non-negative integer $B_i$.

## Standard output

Your program must print to the standard output exactly $N$ lines, each containing exactly one integer number: the number of different ways in which a player can earn $B_i$ points before exiting the tournament. For each query, you have to print the result modulo $10^9 + 7$.

## Constraints and notes

- $1 \leq N \leq 10^4$
- $0 \leq B_i \leq 10^5$

## Examples

### Example 1

Input:
```
1
5
```

Output:
```
8
```

Explanation:

This is the example shown above.
