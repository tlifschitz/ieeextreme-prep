# Luck-i-flip

**IEEEXtreme 13.0** · Time limit: 1000 ms · Memory limit: 256 MB

**CS Academy:** <https://csacademy.com/ieeextreme-practice/task/luck-i-flip/>

In Sierra island there is a famous game called *Luck-i-flip*. To place a bet, each participant fills a row of length $n$ with `0`s and `1`s, representing the two sides of a coin. The bets are public to prevent multiple participants from placing the same bet.

On the day of the event, the president of the Sierra Cultural Association flips a coin $n$ times and the winner is the participant with the most correct coin side guesses. In case of a tie, the association keeps the jackpot.

Sara does not like to gamble but she is interested in the fact that this game is not solely reliant on luck. Not every bet offers the same chances of winning. In particular, she wants to know what are the odds of winning for the worst bet on the public ledger.

For that, Sara should count how many different draws will give the prize to the worst bet. Can you help her?

Take, for example, the three bets `001`, `110` and `101`:

- for the bet `001` the winning draws are `000`, `001` and `011`
- for the bet `110` the winning draws are `010` and `110`
- for the bet `101` the only winning draw is `101`

In this case, the worst bet is `101` and the number of different winning draws for the worst bet is $1$.

## Standard input

The first line is the number of bets, $b$ in the public ledger, followed by a bet in each line.

## Standard output

The output is the minimum number, $m$, of winning draws for the worst bet.

## Constraints and notes

- $n \leq 22$
- $b \leq 100$
- $m \leq 20$

## Examples

### Example 1

Input:
```
2
00
11
```

Output:
```
1
```

Explanation:

There are two bets, `00` and `11`. There are four possible draws of length 2: `00`, `01`, `10`, `11`. If the draw is `00`, then the winning bet would be `00`. If the draw is `11` the winning bet would be `11`. But if the draw is `01` or `10` then both bets failed one coin side and lose the jackpot. For each bet, there is only $1$ draw leading it to the prize. So the answer is the minimum which is $1$.

### Example 2

Input:
```
2
00
01
```

Output:
```
2
```

Explanation:

There are two bets, `00` and `01`. There are four possible draws of length 2: `00`, `01`, `10`, `11`. Both draws `00` and `10` would be won by `00`. Conversely, both draws `11` and `01` would be won by `01`. So both bets have $2$ winning draws. The answer is the minimum which is $2$.
