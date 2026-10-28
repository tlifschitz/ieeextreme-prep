# Knin

**IEEEXtreme 11.0** · Time limit: 2000 ms · Memory limit: 4 MB

**CS Academy:** <https://csacademy.com/ieeextreme-practice/task/a8030fdc5d7b32664ec5b9addc418f83/>

Ariadne likes strategy board games like Chess and Go. One day she thought of her own two player strategy board game which goes as follows.

The game is played on an $w \times h$ ($w$ for width, $h$ for height) board which is cut into $1 \times 1$ squares. Players, starting from player $1$, place in turn a piece in one square. Player pieces are *distinguishable*. More specifically player $1$ pieces are labelled with a $1$ and player $2$ pieces are labelled with a $2$.

In every $n \times n$ square (for $n > 2$) there can be at most $n-1$ pieces (counting both players' pieces). Note that when applying this rule, the $n \times n$ square must be contained within the board and be aligned to the board grid.

The player that can't place a piece on the board on his turn loses.

Given the width $w$ and height $h$ of a board and the state of the board can you tell if the position is valid or not? A valid position is a position that can be reached from an empty board following the rules of the game.

## Standard input

The first line of the input will contain an integer $t$ ($1 \leq t \leq 100$), , which is the number of test cases to follow.

Each case begins with a line containing two numbers $h$ and $w$ ($1 \leq h, w \leq 2\,500$), the size of the board.

Each of the following $h$ lines contains $w$ characters each denoting the piece at each square.

- `.` symbolises an empty square
- `1` symbolises a player $1$ piece
- `2` symbolises a player $2$ piece

## Standard output

For each test case print `YES` or `NO` depending if the input state if the board is valid or not.

## Constraints and notes

- $1 \leq t \leq 100$
- $1 \leq h, w \leq 2\,500$
- The sum of $h*w$ for all the tests in a file is $\leq 2\,500^2$

## Examples

### Example 1

Input:
```
3
3 3
1.1
.2.
212
4 4
...1
1...
.2..
....
1 2
..
```

Output:
```
NO
YES
YES
```

Explanation:

- In the first example the $3 \times 3$ the square starting at $(0,0)$ and finishing at $(2,2)$ has $6$ pieces which are more than the $2$ pieces which are allowed for any $3 \times 3$ square.
- In the second example the state is valid.
- In the third example the state is valid.
