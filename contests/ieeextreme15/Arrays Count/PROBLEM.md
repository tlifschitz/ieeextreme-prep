# Arrays Count

**IEEEXtreme 15.0** · Time limit: 2000 ms · Memory limit: 256 MB

**CS Academy:** <https://csacademy.com/ieeextreme-practice/task/arrays-count/>

Makoto has just learned about the [bitwise OR](https://en.wikipedia.org/wiki/Bitwise_operation#OR) operation, so he thought of an array $A$ of integers and then wrote down the binary representation of its elements separated by the $|$ operator, *without leading zeros*. As a result, he got an OR expression from $A$. Interestingly, when counting the total digits he wrote down he found that there are exactly $K$ digits (excluding the $|$ operators).

For $K = 10$, Makoto could have written down $10 | 111|1001|1$ ($A$ has $4$ numbers), or just $1010101010$ ($A$ has a single number). Notice that each integer's binary representation starts with $1$.

When Makoto wasn't paying attention, his little brother, Akio, erased a prefix (possibly empty) of the symbols written down by Makoto, such that the resulting array of symbols starts with $1$. In other words, the numbers in the new expression still contain no leading zeros, and the new expression cannot start with an operator.

So, if Makoto's intial expression was $10 | 111|1001|1$, after Akio's actions he could've been left with any of the following:

-  $111|1001|1$
-  $1|1001|1$
- $10 | 111|1001|1$
- $1$

Note that these are not all possible outcomes, they are just a few examples.

Later that day, Makoto returned to his array, and unaware of Akio's actions, he computed the bitwise OR of the numbers that were still written down and got the result $2^N-1$ (or in binary form, $111...1$ , where there are exactly $N$ ones).

You are given the two integers $N$ and $K$, and are asked to count the number of distinct possible initial array $A$, *modulo* $4$. Two arrays are considered distinct if their string representation is different.

## Standard input

The first input line contains the number of cases $T$. Each test case contains a single line with two integers $N$ and $K$.

## Standard output

For each test case, output a single integer, the answer modulo $4$.

## Constraints and notes

- $1 \le T \le 10$
- $2 \le N \le 10^{12}$
- $N+2 \le K \le 2 \cdot 10^{12}$
- For $20\%$ of the test files, $K \le 10$.
- For $40\%$ of the test files, $K \le 100$.
- For $60\%$ of the test files, $K \le 1000$.
- For $80\%$ of the test files, $K \le 10^6$.

## Examples

### Example 1

Input:
```
4
2 4
5 15
147 10000
60 150
```

Output:
```
2
0
1
3
```

Explanation:

In the first test case, there are $14$ possible initial arrays $A$:

1. $1111$
1. $1011$
1. $1|111$
1. $111|1$
1. $110|1$
1. $11|11$
1. $10|11$
1. $11|10$
1. $10|1|1$
1. $11|1|1$
1. $1|10|1$
1. $1|11|1$
1. $1|1|10$
1. $1|1|11$
