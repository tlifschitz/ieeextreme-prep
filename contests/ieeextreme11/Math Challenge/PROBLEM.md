# Math Challenge

**IEEEXtreme 11.0** · Time limit: 500 ms · Memory limit: 64 MB

**CS Academy:** <https://csacademy.com/ieeextreme-practice/task/7df0da0b0477307be410f4772c739528/>

Paola is a strict Math teacher.

She challenged her students to calculate $a^{\binom{b}{c}}$ where $\binom{b}{c} = \frac{b!}{c! * (b-c)!}$.

Are you up to the challenge? Can you calculate this number?

## Standard input

The input begins with an integer <Latex value="t"/> <Latex value="(1 \leq t \leq 10)"/>, giving the number of test cases in the input.

Each of the following $t$ lines represent a different test case and consist of three integers $a$, $b$, $c$ (<Latex value="1 \leq a, b, c \leq 10^6"/> and <Latex value="b \geq c"/>).

## Standard output

Output $t$ lines, for each case print the result modulo <Latex value="10^9+7"/>.

## Constraints and notes

- $1 \leq t \leq 10$
- $1 \leq a, b, c \leq 10^6$
- $b \geq c$

## Examples

### Example 1

Input:
```
3
1 5 5
2 10 2
3 9 4
```

Output:
```
1
371842544
665507626
```

### Example 2

Input:
```
3
2 5 3
3 8 4
1 1000000 500000
```

Output:
```
1024
662963356
1
```
