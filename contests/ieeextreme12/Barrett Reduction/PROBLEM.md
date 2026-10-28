# Barrett Reduction

**IEEEXtreme 12.0** · Time limit: 500 ms · Memory limit: 256 MB

**CS Academy:** <https://csacademy.com/ieeextreme-practice/task/barrett-reduction/>

The $\text{C++}$ compiler optimizes the division by a constant $D$ by multiplying your number by a constant $A$ and then shifting the result $B$ bits. This process is called [Barrett reduction](https://en.wikipedia.org/wiki/Barrett_reduction).

In this challenge we'll consider the division of an `unsigned 32 bit integer` by another `unsigned 32 bit integer`.

Given $A$ and $B$, your task is to find the minimum possible value of $D$, for which the division is correct.

*Note*: it's guaranteed that for the given values $A$ and $B$ there exists an integer $D$ such that for every number $0 \leq X < 2^{31}$, $\lfloor \frac{X}{D} \rfloor = \lfloor \frac{X \times A}{2^{B}} \rfloor$, where $\lfloor X \rfloor$ represents the floor (integer part) of the result.

E.g: $\lfloor 0.4 \rfloor = 0$, $\lfloor 6.8 \rfloor = 6$.

*Note* that the challenge only uses unsigned integers, so there are no problems regarding using floor on negative numbers.

## Standard input

The first line contains two integers $A$ and $B$.

## Standard output

The first line should contain one integer $D$.

## Constraints and notes

- $0 \leq A < 2^{32}$
- $0 \leq B \leq 63$
- $1 \leq D < 2^{31}$

## Examples

### Example 1

Input:
```
3435973837 35
```

Output:
```
10
```

Explanation:

Here are some examples of divisions.

$\lfloor \frac{5}{10} \rfloor = 0$

$\lfloor \frac{5 \times 3435973837}{2^{35}} \rfloor = \lfloor \frac{17179869185}{2^{35}} \rfloor = 0$

$\lfloor \frac{17}{10} \rfloor = 1$

$\lfloor \frac{17 \times 3435973837}{2^{35}} \rfloor = \lfloor \frac{58411555229}{2^{35}} \rfloor = 1$

$\lfloor \frac{35}{10} \rfloor = 3$

$\lfloor \frac{35 \times 3435973837}{2^{35}} \rfloor = \lfloor \frac{120259084295}{2^{35}} \rfloor = 3$
