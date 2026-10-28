# Magical Stones II

**IEEEXtreme 14.0** · Time limit: 1000 ms · Memory limit: 256 MB

**CS Academy:** <https://csacademy.com/ieeextreme-practice/task/magical-stones-2/>

You are practicing your alchemy skill over a pile of magical stones. A magical stone has $N$ possible states numbered from $1$ to $N$. In the beginning, you have exactly one magical stone that is in each state $i$.

You know two magic spells: the /white/ spell, and the /black/ spell. When you cast the white spell, a stone that is in state $i$ will transform into a stone in state $W_i$. When you cast the black spell, a stone that is in state $i$ will transform to a stone in state $B_i$. Whenever two stones are in a same state $i$, they will purify each other, and combine into a single more powerful stone in state $i$. Multiple stones in a same state will combine at the same time.

You would like to obtain one single magical stone that is the purest and the most powerful of all. You will cast a sequence and black and white spells and combine all the $N$ stones you have into one. The final stone can be in any state. Is this ever possible?

## Standard input

The input has a single integer $T$ on the first line, the number of test cases.

Each test case has single integer $N$ on the first line. The next two lines each have $N$ integers. The first line gives $W_1, ... W_N$. The second line gives $B_1, ... B_N$.

## Standard output

Output one line for each test case.

If it is possible to combine all the $N$ stones into one, output a string that is the sequence of magic spells you will cast. Output `W` for a white spell and `B` for a black spell. If there are multiple possible sequences, you may output any of them. You do not need to find a shortest sequence of spells. However since you don't want to spend the whole $24$ hours casting spells, you must output a sequence of no more than $10^6$ spells.

If it is impossible to combine all the stones into one, output a single word `impossible`.

## Constraints and notes

- $1 \leq T \leq 30$
- $2 \leq N \leq 100$
- $1 \leq W_i, B_i \leq N$. It is possible that $W_i = i$ or $B_i = i$.
- It can be shown that if is possible to combine all stones into one, then there exists a sequence of no more than $10^6$ magic spells to do so.
- Your answer is considered correct as long as you have a single stone at the end of the spell sequence. That is, it is allowed to cast redundant spells after successfully combining the stones into one.

- For $25\%$ of the test data, $N \leq 20$

## Examples

### Example 1

Input:
```
3
4
2 3 4 1
3 3 2 3
5
1 2 3 4 5
2 3 4 5 5
4
2 3 4 1
4 1 2 1
```

Output:
```
BWWB
BBBBWW
impossible
```

Explanation:

Case $1$: The states the stones are in after each spell are:

- At the beginning: $\{1,2,3,4\}$
- After a black spell: $\{2, 3\}$
- After a white spell: $\{3,4\}$
- After a white spell: $\{1,4\}$
- After a black spell: $\{3\}$

Case $2$: After four black spells you will obtain a single stone in state $5$. It is okay that you cast some redundant spells after that, as long as the total number of spells does not go above $10^6$.

Case $3$: The white spell does not allow you to combine any stones. Using only black spells will be able to combine the stones that are initially in states $1, 3$ and initially in states $2, 4$, but not all the states.
