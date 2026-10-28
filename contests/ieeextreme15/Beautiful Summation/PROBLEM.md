# Beautiful Summation

**IEEEXtreme 15.0** · Time limit: 2000 ms · Memory limit: 256 MB

**CS Academy:** <https://csacademy.com/ieeextreme-practice/task/summation/>

Andy loves arithmetic and geometric progressions. He has mastered the summation formulas for arithmetic and geometric progressions. But, he is already bored with those standard formulas. So, he comes up with a more beautiful summation, i.e.

$S_N= \sum_{k = 1}^{N} P^k \times k^Q$

But, he does not know how to calculate the value of $S_N$. Since you are an awesome problem solver, Andy asks your help to calculate the value of $S_N$ modulo $M$ for given numbers $P$, $Q$, $N$, and $M$.

## Standard input

There is only one line in the input containing four integers separated by single spaces, $P$, $Q$, $N$, and $M$ that represent the parameters in Andy's summation.

## Standard output

You should output an integer between $0$ and $M-1$ representing the result of Andy's summation after modulo by $M$.

## Constraints and notes

- $1 \leq P \leq 1\,000$
- $0 \leq Q \leq 1\,000$
- $1 \leq N, M \leq 10^9$

- For $20\%$ of the test files, $N \leq 10^6$.
- For another $40\%$ of the test files (not including the $20\%$ above), $M \leq 10^6$.

## Examples

### Example 1

Input:
```
2 3 4 10
```

Output:
```
4
```

Explanation:

$S_4 = \sum_{k=1}^{4} 2^k \times k^3$

$S_4 = 2^1 \times 1^3 + 2^2 \times 2^3 + 2^3 \times 3^3 + 2^4 \times 4^3$

$S_4 = 2 + 32 + 216 + 1024$

$S_4 = 1274$

So, $S_4 \mod 10 = 4$.

### Example 2

Input:
```
7 0 5 128
```

Output:
```
23
```

Explanation:

$S_5 = \sum_{k=1}^{5} 7^k \times k^0$

$S_5 = 7^1 \times 1^0 + 7^2 \times 2^0 + 7^3 \times 3^0 + 7^4 \times 4^0 + 7^5 \times 5^0$

$S_5 = 7 + 49 + 343 + 2401 + 16807$

$S_5 = 19607$

So, $S_5 \mod 128 = 23$.
