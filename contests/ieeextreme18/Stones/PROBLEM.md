# Stones

**IEEEXtreme 18.0** · Time limit: 1000 ms · Memory limit: 256 MB

**CS Academy:** <https://csacademy.com/ieeextreme-practice/task/stones/>

Alice and Bob play the following game:

- Each of them has some initial amounts of red stones and blue stones (they know each other's amounts).
- The game is played in turns. A turn consists of several steps, as described below. In a turn, Alice and Bob will take on two roles, $A$ and $B$.
- At the first turn, Alice will take on the role of $A$ and Bob will take on the role of $B$. For the next turns, they will start alternating the roles. So at the second turn, Alice will take on the role of $B$ and Bob on the role of $A$.

A turn consist of the following steps:

- Player $A$ chooses a color (red or blue), writes it down on a piece of paper, and puts it on the table in a way that player $B$ can't see what's written.
- Player $B$ then tries to guess the color written down. Let's call the guessed color $X$.
- If $B$ guesses correctly, player $A$ loses one stone of color $X$; otherwise, player $B$ loses one stone of color $X$.

The game ends when one player loses their last stone of any color, as they lose immediately.

Your task is to calculate the probability of Alice winning the game if both players are trying to maximize their probability of winning regardless of their opponent's moves.

## Standard input

The first line contains two integers, $R_1$ and $B_1$, representing the number of red and blue stones for Alice, followed by another two integers, $R_2$ and $B_2$, representing the number of red and blue stones for Bob.

## Standard output

Output one number - the probability of Alice winning the game, represented as a real number. Your answer will be accepted if the relative or absolute error is less or equal to $10^{-6}$.

## Constraints and notes

- $1 \leq R_1, R_2 \leq 40$,
- $1 \leq B_1, B_2 \leq 40$

## Examples

### Example 1

Input:
```
1 1 1 1
```

Output:
```
0.5
```

### Example 2

Input:
```
1 2 3 4
```

Output:
```
0.071428571
```
