# Infinite String

**IEEEXtreme 13.0** · Time limit: 1000 ms · Memory limit: 256 MB

**CS Academy:** <https://csacademy.com/ieeextreme-practice/task/infinite-string/>

Ivan Likes playing with strings. Today he decided to make the biggest string ever.

Using the first $B$ characters of the Latin alphabet, he wants to write a string that first consists all the words of length $1$, in lexicographical order, then all the words of length $2$, in lexicographical order, etc.

For example, using the first $4$ characters (a, b, c, d), the string will be the following (without spaces):

*a b c d aa ab ac ad ba bb bc bd ca cb cc cd da db dc dd aaa aab aac aad aba ...*

Because the string is infinite and Ivan has to go to the University in the morning, he is interested what character is at index $X$.

## Standard input

The first line contains one integer, $T$, the number of queries.

The next $T$ lines contain two integers, $B$ and $X$, that correspond to the number of characters used in the alphabet and the $0$-based index of the character Ivan wants to know.

## Standard output

Output $T$ lines. The $i$th line has the character for the $i$th query.

## Constraints and notes

- $1 \le T \le 100$
- $1 \le B \le 26$
- $0 \le X \le 10^{18}$

## Examples

### Example 1

Input:
```
6
4 5
4 3
2 32
26 24
26 50
4 27
```

Output:
```
a
d
b
y 
a
d
```

Explanation:

For cases where $B=2$, the $32$th character is the following:

abaaabbabbaaaaababaabbbaababbbab *b* baaaaaaabaabaaabbabaaabab ...

For Cases where $B=4$, the $3$rd, $5$th and $27$th characters are the following:

abc *d* a *a* abacadbabbbcbdcacbccc *d* dadbdcddaaaaabaacaadaba ...

For cases where $B=26$, the $24$th and $50$th characters are the following:

abcdefghijklmnopqrstuvwx *y* zaaabacadaeafagahaiajakal *a* manaoapaqar ...

Note that all indices are $0$-based.
