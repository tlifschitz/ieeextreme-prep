**CS Academy:** <https://csacademy.com/ieeextreme-practice/task/different_xor/>

# Different Xor Values

**IEEEXtreme 17.0** · Time limit: 1000 ms · Memory limit: 256 MB

You are given an integer sequence $a$ of length $n$ and want to play a game with your friend. The game consists of selecting a contiguous subsequence $a_{l}, \ldots, a_{r}$, define an empty set $S$ and then make the maximum number of possible moves.

A move over a subsequence $a_{l}, \ldots, a_{r}$ consists of choosing some positions (possibly none) $l \leq i_{1} < \ldots < i_{k} \leq r$ such that the Bitwise XOR of the elements $a_{i_{1}} \oplus \ldots \oplus a_{i_{k}}$ is not present in $S$ and then insert this value in it. (The Bitwise XOR of an empty sequence is $0$).

Since you can choose any contiguous subsequence of $a$, you want to know how many moves will be made in total after every different possible game. In other words, let $Q(l, r)$ be the maximum number of moves over the subsequence $a_{l}, \ldots, a_{r}$ in one game, then you want to compute

$\sum\limits_{l = 1}^{n}\sum\limits_{r = l}^{n}Q(l, r)$

Since the answer could be large, print it modulo $10^{9} + 7$.

## Standard Input

The first line of input contains an integer $t$, the number of testcases.

The first line of each testcase contains an integer $n$, the length of the sequence.

The second line of each testcase contains $n$ integers $a_{i}$, where the $i$-th integer is the $i$-th element of the sequence.

## Standard Output

For each testcase, print a single line with the answer to the problem.

## Constraints and notes

- $(1 \leq t \leq 5)$
- $(1 \leq n \leq 10^{5})$
- $(0 \leq a_{i} \leq 10^{6})$

## Examples

### Example 1

Input:
```
3
2
1 0
2
1 1
3
3 3 2
```

Output:
```
5
6
16
```

Explanation:

For the first testcase, we have the following subsequences:

- $\{1\}$, in which $2$ moves can be made: one with value $1$ (choosing the only element of the subsequence) and another one with value $0$ (empty).
- $\{0\}$, in which $1$ move can be made: one with value $0$ (either choosing the only element or none).
- $\{1, 0\}$, in which **2** moves can be made: one with value $1$ (either choosing the first or the two values) and another one with $0$ (either choosing the second value or none of them).

For the second testcase, we have the following subsequences:

- $\{1\}$, in which $2$ moves can be made: one with value $1$ (choosing the only element of the subsequence) and another one with value $0$ (empty).
- $\{1\}$, in which $2$ moves can be made: one with value $1$ (choosing the only element of the subsequence) and another one with value $0$ (empty).
- $\{1, 1\}$, in which $2$ moves can be made: one with value $1$ (either choosing only one element) and another one with $0$ (either choosing both elements or none of them).

For the third testcase, we have the following subsequences:

- $\{3\}$, in which $2$ moves can be made: one with value $3$ (choosing the only element of the subsequence) and another one with value $0$ (empty).
- $\{3\}$, in which $2$ moves can be made: one with value $3$ (choosing the only element of the subsequence) and another one with value $0$ (empty).
- $\{2\}$, in which $2$ moves can be made: one with value $2$ (choosing the only element of the subsequence) and another one with value $0$ (empty).
- $\{3, 3\}$, in which $2$ moves can be made: one with value $3$ (either choosing only one element) and another one with $0$ (either choosing both elements or none of them).
- $\{3, 2\}$, in which $4$ moves can be made: one with value $1$ (choosing both elements), one with value $2$ (choosing only the second element), one with value $3$ (choosing only the first element) and another one with $0$ (choosing none of the elements).
- $\{3, 3, 2\}$, in which $4$ moves can be made: one with value $1$ (choosing one $2$ and one $3$), one with value $2$ (choosing only the element with value $2$), one with value $3$ (choosing any of the elements with value $3$) and another one with $0$ (choosing none of the elements or two elements with value $3$).
