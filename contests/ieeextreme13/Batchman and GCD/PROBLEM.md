# Batchman and GCD

**IEEEXtreme 13.0** · Time limit: 1000 ms · Memory limit: 256 MB

**CS Academy:** <https://csacademy.com/ieeextreme-practice/task/batchman-and-gcd/>

The streets of Gotham have been poisoned by crime and implementation problems again! But rest assured, our hero, Batchman has come to save the day! Today, he has to face the terrible XML parsing monster by countering him with a number theory problem. The issue is that while fighting the terrible creature, he can't think of an efficient solution for the problem, so he asks for your help!

The problem goes like this: you are given an array $A=(a_1, a_2, ..., a_N)$ and a number $K$. Consider all <Definition value="subsequences" term="subsequence"/> of $A$ of size at most $K$. For each subsequence, compute the GCD of the numbers in the subset. How many *distinct* GCDs can you get?

## Standard input

The first line will contain the numbers $N$ and $K$.

The second line will contain $N$ integers corresponding to the elements of $A$.

## Standard output

The output will contain a single number corresponding to the problem's answer.

## Constraints and notes

-  $1 \le N \le 10^5$
-  $1 \le K \le N$
- $1 \le a_i \le 10^5$

## Examples

### Example 1

Input:
```
5 5
4 8 12 16 18
```

Output:
```
7
```

Explanation:

The only GCD values that can be obtained are:

2 = gcd $\{4, 18\}$,

4 = gcd $\{4\}$,

6 = gcd $\{12, 18 \}$,

8 = gcd $\{8, 16\}$,

12 = gcd $\{12\}$,

16 = gcd $\{16\}$,

18 = gcd $\{18\}$
