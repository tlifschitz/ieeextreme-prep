# Mosaic Decoration I

**IEEEXtreme 14.0** · Time limit: 1000 ms · Memory limit: 256 MB

**CS Academy:** <https://csacademy.com/ieeextreme-practice/task/mosaic1/>

Zapray lives in a big mansion that has $N$ bathrooms. He wants to decorate the bathroom walls using mosaic tiles of two colors: black and pink. The $i$th bathroom needs $B_i$ black tiles and $P_i$ pink tiles. Mosaic tiles are sold in piles. Zapray can buy one pile of $10$ black tiles for $C_B$ dollars, and one pile of $10$ pink tiles for $C_P$ dollars. How much money does he need in total to decorate all the $N$ bathrooms?

## Standard input

The input contains three integers $N, C_B, C_P$ on the first line.

The next $N$ lines each have two integers. The $i$th line has $B_i$ and $P_i$.

## Standard output

Output a single integer, the amount of money in dollars that Zapray needs to decorate all his bathrooms.

## Constraints and notes

- $2 \leq N \leq 100$
- $1 \leq C_B, C_P \leq 1\,000$
- $1 \leq B_i, P_i \leq 1\,000$

## Examples

### Example 1

Input:
```
3 5 7
10 10
20 30
30 3
```

Output:
```
65
```

Explanation:

There are $3$ bathrooms to decorate. In total $60$ black tiles and $43$ pink tiles are needed. Zapray needs to purchase $6$ piles of black tiles and $5$ piles of pink tiles. The total cost is $6 \times 5 + 5 \times 7 = 65$ dollars.
