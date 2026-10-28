# Yin Yang

**IEEEXtreme 13.0** · Time limit: 1000 ms · Memory limit: 256 MB

**CS Academy:** <https://csacademy.com/ieeextreme-practice/task/yin-yang/>

Finding the perfect balance is something sought after by many people and in many ways... sometimes even in strings. We'll call a string unbalanced if it has even length and its two halves are equal. Find a string of length $N$, consisting only of characters `y` and `Y`, such that it has as few distinct unbalanced  <Definition term="substring" value="substrings"> as possible.

Your score per test will be computed as ${(1 + \frac{1}{10})}^{-K}$, where $K$ is $e^{F - O}$, $O$ is the optimal number of distinct unbalanced substrings and $F$ is the number of distinct unbalanced substrings you have obtained.

/Perfectly balanced as all things should be./

## Standard input

The first line contains an integer $N$.

## Standard output

Print the answer on the first line.

## Constraints and notes

- $1 \leq N \leq 300$
- By $e$ we mean [Euler's number](https://en.wikipedia.org/wiki/E_(mathematical_constant)), which is $\approx 2.718282$

## Examples

### Example 1

Input:
```
4
```

Output:
```
yyyY
```
