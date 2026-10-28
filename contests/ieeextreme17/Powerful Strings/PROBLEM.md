# Powerful Strings

**IEEEXtreme 17.0** · Time limit: 4000 ms · Memory limit: 256 MB

**CS Academy:** <https://csacademy.com/ieeextreme-practice/task/powerful-strings/>

You are given an integer $N$ and $M$ strings $S_i$ with lowercase, English letters. Consider a string of length $N$ with lowercase, English letters. The power of that string is computed as $2^k$ where $k$ is the total number of occurrences of strings from $S$. For example let $M = 2$, $S_1 = ab$ and $S_2 = c$. The power of $ababccca$ is equal $2 ^ 5 = 32$ because $S_1$ occurs twice and $S_2$ occurs three times. Your task is to calculate the sum of powers of all strings of length $N$ modulo $998244353$.

## Standard input

The first line contains two integers $N$ and $M$. Then $M$ lines follow. The $i$-th of these lines contains the string $S_i$.

## Standard output

Output one line with the sum of powers of all strings of length $N$ modulo $998244353$.

## Constraints and notes

- $1 \leq N \leq 10^{18}$,
- $1 \leq M \leq 100$,
- for all $1 \leq i \leq M$, the length of $S_i$ is not greater than $20$

## Examples

### Example 1

Input:
```
3 2
ab
ba
```

Output:
```
17682
```

In the first example there are two strings $aba$ and $bab$ with power $4$, exactly $100$ strings with power $2$ and $17474$ strings with power $1.$
