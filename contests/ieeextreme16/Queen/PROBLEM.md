**CS Academy:** <https://csacademy.com/ieeextreme-practice/task/queen/>

# Queen

**IEEEXtreme 16.0** · Time limit: 1000 ms · Memory limit: 256 MB

Two players are playing on an infinite chess board. In the beginning, a single piece is located at coordinates $(a, b)$.

In a turn, the player must move the piece to new coordinates $(c, d)$ such that:

a) $0 \leq c \leq a$ (no going right),

b) $0 \leq d \leq b$ (no going up), and

c) At least one of the following is satisfied:

- $d = b$ (same row),
- $c = a$ (same column), or
- $|(a − b) − (c − d)| ≤ K$ (almost same diagonal).

The player that cannot make a move loses the game. For starting coordinates $(a, b)$ and the value of $K$, help the first player determine whether or not he has a winning strategy.

## Standard input

The first line of input contains an integer $t$, giving the number of testcases.

The next $t$ lines contain three space separated integers $K$, $a$, and $b$, which are described above.

## Standard output

For each testcase, output a single bit on a line by itself: 1 if the first player can assure his victory, and 0 otherwise.

## Constraints and notes

- $1 \leq t \leq 10^5$
- $0 \leq a, b \leq 10^9$
- $0 \leq K \leq 10^6$

## Examples

### Example 1

Input:
```
10
0 0 0
0 9 8
0 1 1
0 2 1
0 3 5
0 3 6
0 4 7
0 4 1
0 5 5
0 6 10
```

Output:
```
0
1
1
0
0
1
0
1
1
0
```

Explanation:

When $K = 0$, the piece is a regular queen. For $0 \leq a, b \leq 10$, the coordinates such that the first player doesn't have a winning strategy are: $\{(0, 0)$,$(1, 2)$,$(2, 1)$,$(3, 5)$,$(5, 3)$,$(4, 7)$,$(7, 4)$,$(6, 10)$,$(10, 6)\}$.
