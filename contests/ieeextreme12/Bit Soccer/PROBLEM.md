**CS Academy:** <https://csacademy.com/ieeextreme-practice/task/bit-soccer/>

# Bit Soccer

**IEEEXtreme 12.0** · Time limit: 500 ms · Memory limit: 256 MB

Peredo is a computer scientist who loves soccer. His favorite soccer player is Paolo Guerrero, one of the best Peruvian players, and his favorite team is the Brazilian national team.

He has a very large database of players with videos, photos, and many statistics related to their performance in hundreds of games. He uses his database to compute a binary *performance index* that tracks the players' abilities across 40 possible game metrics.

The *performance index* represents all possible soccer abilities of each player with a $0$ for a lack of ability in a given game metric and a $1$ for perfect ability, with no fractions in between $0$ and $1$.

Based on these numbers, Peredo created a simulation game that takes the *performance indices* and combines multiple players to form a *team performance index*.

The *team performance index* is such that if a single player has a $1$ in a given metric then the *team performance index* also has a $1$ in that metric.

You are given a list of players in your *roster* represented by their *performance indices* in decimal format and your tasks is to combine a subset from your *roster* to form your *starting team* and to obtain a specific *team performance index*. There is no limit to the number of players that can form the *starting team*.

As an example, simplifying with just 4 game metrics, if we have two players on our *starting team* with *performance indices* $5$ `(0101)` and $3$ `(0011)` the resulting *team performance index* will be $7$ `(0111)`.

## Standard input

The first line of the input contains an integer $N$ denoting the number of player available in your *roster*. The second line contains $N$ integers $P_i$, denoting the *performance indices* of each player. The third line contains an integer $Q$, denoting the number of queries, and each of the next $Q$ lines contains an integer $G$ that represents the goal *team performance index*.

## Standard output

For each query, print `YES` if it is possible to select a *starting team* from the *roster* and obtain the *team performance index* $G$, otherwise print `NO`.

## Constraints and notes

- $1 \leq N \leq 10^5$
- $1 \leq Q \leq 20$
- $1 \leq P_i, G \leq 2^{40}-1$

## Examples

### Example 1

Input:
```
5
10 3 5 8 6 
2
7
4
```

Output:
```
YES
NO
```

Explanation:

In the first query, we can obtain 7 by selecting the players with *performance indices* 3 and 6.

There is no way to obtain a *team performance index* of 4.
