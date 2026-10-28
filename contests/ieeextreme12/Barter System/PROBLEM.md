# Barter System

**IEEEXtreme 12.0** · Time limit: 1000 ms · Memory limit: 256 MB

**CS Academy:** <https://csacademy.com/ieeextreme-practice/task/barter-system/>

In a world where currency is not available, people fulfill their necessities by exchanging commodities among them. However, not all commodities are equal.

Exchange rate of commodities $A$ to $B$ is defined as the number of units of $B$ one can get with one unit of $A$.

Given exchange rates of a set of pairs of commodities as input, answer a set of queries by finding the exchange rate of a specific pair.

## Standard input

The first line of the input is an integer $N$ which indicates the number of given exchange rates to follow. The next $N$ lines consists of $A, B, r$ triplets where $A$ and $B$ are the commodities and $r$ is the exchange rate such that $A = r \cdot B \ (\text{mod} \ 998244353)$.

The next line contains another integer $Q$ which represents the number of queries. The following $Q$ lines consists of a pair of commodities $K$ and $L$.

## Standard output

For each of the $Q$ queries you need to find $r$ such that $K = r \cdot L$.

It can be shown that $r$ can be represented as $\frac{X}{Y}$, where $X$ and $Y$ are coprime integers and $X  \ne 0 \ (\text{mod} \ 998244353)$. For each query print $X \cdot Y^{-1} \ (\text{mod} \ 998244353)$.

If the exchange rate can not be computed using the given information, print `-1`.

## Constraints and notes

- $1 \leq N, Q \leq 2 \cdot 10^4$
- $1 \leq |A|, |B| \leq 50$
- $1 \leq r < 998244353$
- All exchange rates are consistent

## Examples

### Example 1

Input:
```
3
Rice Bean 399297742
Bean Beef 598946612
Banana Apple 698771048
3
Rice Beef
Beef Banana
Rice Rice
```

Output:
```
279508419
-1
1
```

Explanation:

Rice = $399297742\cdot598946612$ Beef, which is $279508419$.

There is not enough information to convert from Beef to Banana, so `-1` is printed.
