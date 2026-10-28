# Dice

**IEEEXtreme 17.0** · Time limit: 1000 ms · Memory limit: 256 MB

**CS Academy:** <https://csacademy.com/ieeextreme-practice/task/dices/>

Let's choose an integer $t$ uniformly randomly from 1 to $k$.

Now let's roll $t$ standard six-sided dice.

What is the probability that the sum of values rolled on those dice is exactly $n$?

## Standard input

The first line contains two integers $n$ and $k$.

## Standard output

It can be proven, that the answer can be represented as a rational number $P/Q$, where $Q \mod 998244353 \neq 0$

Output one value, $P * Q^{-1} \mod 998244353$ .

## Constraints and notes

- $1 \leq n, k \leq 2^{23}$,

## Examples

### Example 1

Input:
```
1 1
```

Output:
```
166374059
```

### Example 2

Input:
```
2 3
```

Output:
```
341991121
```

Explanation:

There are 3 cases:

t = 1: the only way to obtain sum 2 is to roll 2 (with probability $1/6$).

t = 2: the only way to obtain sum 2 is to roll two ones (with probability $1/36$).

t = 3: there is no way to obtain the sum equal 2.

So the probability is equal to $1/3 * (1/6 + 1/36 + 0) = 7/108$
