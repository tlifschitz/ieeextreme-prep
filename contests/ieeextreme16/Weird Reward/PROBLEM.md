# Weird Reward

**IEEEXtreme 16.0** · Time limit: 2000 ms · Memory limit: 256 MB

**CS Academy:** <https://csacademy.com/ieeextreme-practice/task/weird-reward/>

As a reward for second place at the local programming contest, a team of programmers got a string of length $N$ that is a correct arithmetical expression. It consists of decimal numbers (without leading zeros), plus signs (without unary ones), multiplication signs, and round brackets. Formally, in this problem, a correct arithmetic expression follows this grammar:

- `<expression> ::= <multipliers> | <multipliers> '+' <expression>`

- `<multipliers> ::= <multiplier> | <multiplier> '*' <multipliers>`

- `<multiplier> ::= '(' <expression> ')' | <number>`

- `<number> ::= <digit> | <pos_digit> <number_tail>`

- `<number_tail> ::= <digit> | <digit> <number_tail>`

- `<pos_digit> ::= '1' | '2' | '3' | '4' | '5' | '6' | '7' | '8' | '9' `

- `<digit> ::= '0' | <pos_digit>`

For example, $2 \cdot ((3+0))$ is a correct expression, but $2((3+0))$ and $2 \cdot (3+00)$ aren't.

The first member of the team has rewritten the expression on a large sheet of paper, and the second one wants to know: how many are there *substrings* of that expression which are also correct expressions, and *their value is divisible by the given number* $K$? The third member decided to answer this question, help him!

## Standard input

The first line contains two integers $K$ and $N$. The second line contains a correct arithmetical expression.

## Standard output

Output a single number, which is the answer to the problem.

## Constraints and notes

- $1 \le K \le 10$
- $10 \le N \le 10^5$
- The length of the expression is exactly $N$
- For $10\%$ of the tests, $N \le 200$
- For $30\%$ of the tests, $N \le 2000$

## Examples

### Example 1

Input:
```
4 11
((202))+0*7
```

Output:
```
4
```

Explanation:

There are $4$ valid substrings: $20$, $0$, $0$, $0 \cdot 7$.

### Example 2

Input:
```
3 10
7002*(4+5)
```

Output:
```
7
```

Explanation:

There are $7$ valid substrings: $0$, $0$, $7002$, $4+5$, $(4+5)$, $2 \cdot (4+5)$, $7002 \cdot (4+5)$.

### Example 3

Input:
```
5 15
51664+((7)+(8))
```

Output:
```
3
```

Explanation:

There are $3$ valid substrings: $5$, $(7)+(8)$, $((7)+(8))$.

### Example 4

Input:
```
10 30
(10+20*30+40)*50+60*(70+80*90)
```

Output:
```
56
```
