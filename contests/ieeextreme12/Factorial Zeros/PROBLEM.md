**CS Academy:** <https://csacademy.com/ieeextreme-practice/task/factorial-zeros/>

# Factorial Zeros

**IEEEXtreme 12.0** · Time limit: 1000 ms · Memory limit: 256 MB

Dahsser studies business administration in Lima but he is also an amateur programer. During a particularly boring class he realized that the factorial of a number in a base $B$ would end with a certain number of zeros, but that not all exact number of zeros was possible for a given base. He then tried to find an algorithm to print the minimum number whose factorial in base $B$ ends with exactly $N$ zeros.

## Standard input

The first line contains an integer $T$, denoting the number of cases. The next $T$ lines contain two separated integers $B$ and $N$.

## Standard output

For each case $T$, print the minimum number whose factorial in base $B$ ends with exactly $N$ zeros. In case there is no solution, print $-1$.

## Constraints and notes

- $1 \leq T \leq 20$
- $2 \leq B \leq 100$
- $1 \leq N \leq 10^{12}$

## Examples

### Example 1

Input:
```
2
3 2 
10 5
```

Output:
```
6
-1
```

Explanation:

In the first case, 6 is the minimum number whose factorial in base 3 ends with exactly 2 zeros.

$6! = 720$ (base 10), $222200$ (base 3)

In the second case there is no solution. There is no factorial in base 10 that ends with exactly 5 zeros.
