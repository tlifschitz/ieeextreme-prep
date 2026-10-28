# Cool Sum

**IEEEXtreme 17.0** · Time limit: 200 ms · Memory limit: 256 MB

**CS Academy:** <https://csacademy.com/ieeextreme-practice/task/coolsum/>

You are given two integers: $k$ and $n$.

Let's define sequence $a_t = \sum_{i=0, i \textbf{ mod } 2^k = t}^{n}{n \choose i}$.

Your task is to find $a_0, a_1, ... a_{2^k-1}$.

Since the answer can be very big, all the calculations should be performed modulo 998244353

## Standard input

The first line contains two integers $k$ and $n$.

## Standard output

Output $2^k$ space separated values where the $i$-th of these values is equal to $a_i$ mod 998244353 (0 indexed).

## Constraints and notes

- $1 \leq k \leq 17$,
- $0 \leq n < 998244353$,

## Examples

### Example 1

Input:
```
3 10
```

Output:
```
46 20 46 120 210 252 210 120 
```
