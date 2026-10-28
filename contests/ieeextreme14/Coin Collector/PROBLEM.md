# Coin Collector

**IEEEXtreme 14.0** · Time limit: 1000 ms · Memory limit: 256 MB

**CS Academy:** <https://csacademy.com/ieeextreme-practice/task/coin-collector/>

Zapray has been playing the game World of Warcraft Classic. In the game, he needs to collect coins to exchange for rewards from a tribe. There are $9$ kinds of coins he could collect. He can turn in the following combinations of coins for rewards, as many times as he likes.

- Set I: `Zulian` Coin $\times 1$, `Razzashi` Coin $\times 1$, and `Hakkari` Coin $\times 1$
- Set II: `Sandfury` Coin $\times 1$, `Skullsplitter` Coin $\times 1$, and `Bloodscalp` Coin $\times 1$
- Set III: `Gurubashi` Coin $\times 1$, `Vilebranch` Coin $\times 1$, and `Witherbark` Coin $\times 1$

Each completed set gives the same rewards. Zapray has figured out he wants $N$ sets of coins for the rewards, thus he is going to buy the coins from other players via the Auction House. Each of the listings on the Auction House always consists a number of the same kind of coins with a buyout price.

Now Zapray needs your help to find out the minimum amount of money to complete $N$ sets of coins.

## Standard input

The first line of input consists two integers $N$ and $M$.

Each of the next $M$ lines describes a listing of coins on the Auction House with the name of the coin, quantity $K$ as an integer and price $P$ as an integer, separated by spaces. For example, `Zulian 3 100` means $3$ Zulian Coins are listed at a price of $100$.

Zapray cannot partially buy a listing.

## Standard output

If it is impossible, output a single line `impossible`. Otherwise, output the minimum amount of money Zapray has to spend on completing $N$ sets of coins.

## Constraints and notes

- $0 \leq N \leq 1000$
- $0 \leq M \leq 5000$
- $0 < K \leq 250$
- $0 < P \leq 10^{6}$
- Coin names in the input are case-sensitive, and each coin name is exactly one of the $9$ coin names as in the statement.
- World of Warcraft Classic is developed and released by Blizzard Entertainment. Blizzard Entertainment does not endorse and has no involvement with IEEEXtreme 14.0 contest.

## Examples

### Example 1

Input:
```
10 8
Zulian 3 100
Sandfury 5 500
Skullsplitter 6 900
Bloodscalp 5 400
Razzashi 5 125
Hakkari 7 375
Witherbark 7 60
Zulian 4 800
```

Output:
```
3200
```

Explanation:

Zapray needs to buy all listings except for Witherbark Coins to complete $10$ sets.

### Example 2

Input:
```
10 3
Zulian 100 100
Sandfury 100 100
Gurubashi 100 100
```

Output:
```
impossible
```

Explanation:

There is no possible ways to complete enough sets.
