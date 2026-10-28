# Concentration Game

**IEEEXtreme 13.0** · Time limit: 1000 ms · Memory limit: 256 MB

**CS Academy:** <https://csacademy.com/ieeextreme-practice/task/concentration-game/>

Concentration is a card game in which a set of cards are laid face down on a surface and two cards are flipped face up over each turn. The objective of the game is to turn over pairs of matching cards.

There will be $2N$ cards of $N$ different types labelled with integers from $1$ to $N$.

## Interaction

You should read an integer $N$.

A move consists in choosing two distinct card indices $i_1$ and $i_2$ and revealing them. To make a move, print a line with both indices separated by a space between them (and don't forget to flush the output!). If these cards have the same value written on them, the interactor will reply with `MATCH` and eliminate the cards from the surface. Otherwise, it will reply with two integers, the first representing the value of $i_1$ and the second representing the value of $i_2$.

If at any point in time the interactor decides you've made an invalid move, it will print `-1` and exit. You must read this value and exit right away, otherwise you might get a verdict which does not properly reflect your invalid move.

You must print `-1` after you have decided to not make any more moves.

## Constraints and notes

- $1 \leq N \leq 10^3$
- You are allowed at most $2N$ moves
- You may not ask to make a move with a card that has already been removed from the surface
- The card indices *DO NOT* change after other cards are removed from the surface

## Examples

### Example 1

Input:
```
5
3 4 3 4 1 2 5 5 1 2
```

Output:
```

```

Explanation:

The initial order for the cards is $[3, 4, 3, 4, 1, 2, 5, 5, 1, 2]$.
