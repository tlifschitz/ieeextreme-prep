**CS Academy:** <https://csacademy.com/ieeextreme-practice/task/war_games/>

# War Games

**IEEEXtreme 17.0** · Time limit: 1000 ms · Memory limit: 256 MB

In one variant of the game of war, two players are dealt a pile of playing cards.  At each turn, both players turn over their top card, and the player with the higher card adds the lower card to the bottom of their deck.  The higher card is then discarded.  If the cards that are turned over have the same value, both players return their card to the bottom of their pile.

The player that runs out of cards loses the game. If no player will run out of cards, the game ends in a draw.

Your challenge is to determine which player will win a game, given the cards in each player's pile.

## Standard Input

Input begins with an integer $n$ on a line by itself that indicates how many games are in the input.

The next $2 n$ lines describe the $n$ games, with the first line in a pair giving player 1's cards and the second line giving player 2's cards.  The cards are listed from the top of the pile to the bottom of the pile, and are described by a single character chosen from the list `<2,3,4,5,6,7,8,9,T,J,Q,K,A>`. Note that this list gives the cards' values sorted in ascending order.

## Standard Output

For each game, output:

`player 1` if player 1 will win the game

`player 2` if player 2 will win the game

`draw` if the game will end in a draw

## Constraints and notes

- $1 \leq n \leq 25$

Each player will have between 1 and 51 cards, inclusive.

The players may start with a different number of cards.

The total number of cards for both players will be less than or equal to 52.

There is no restriction on the number of cards of a particular value that may appear.  For example, the game may include 52 cards with the value of `A`.

## Examples

### Example 1

Input:
```
2
K T 3
2 J 5 J
T A T
T T J
```

Output:
```
player 2
draw
```

Explanation:

In the first game, after the `K` and the `2` are turned over, player 1 adds the `2` to the end of their pile, so players have: `T 3 2` and `J 5 J`.

After the `T` and the `J` are played, the players will have `3 2` and `5 J T`.

After the `3` and the `5` are played, the players will have `2` and `J T 3`.

After the `2` and the `J` are played, player 1  will run out of cards and lose.

In the second game, the two `T` cards will be played first. Since these are tied, they will be moved to the end of the piles giving `A T T` and `T J T` as the piles.  The `A` beats the `T` so the hands become `T T T` and `J T`. After the next card, the hands become: `T T` and `T T`. Since these hands would repeat forever, and the game ends in a draw.
