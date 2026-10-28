# Magical Stones I

**IEEEXtreme 14.0** · Time limit: 2000 ms · Memory limit: 256 MB

**CS Academy:** <https://csacademy.com/ieeextreme-practice/task/magical-stones/>

You are practicing your alchemy skill over a pile of magical stones. A magical stone has $N$ possible states numbered from $1$ to $N$. In the beginning, you have exactly one magical stone that is in each state $i$.

You know one magic spell. When you cast the spell, a stone that is in state $i$ will transform into a stone in state $S_i$. Whenever two stones are in a same state $i$, they will purify each other, and combine into a single more powerful stone in state $i$. Multiple stones in a same state will combine at the same time.

You would like to obtain exactly $K$ magical stones in the end. What is the minimum number of spells you have to cast to achieve that? Since you are not sure which $K$ best satisfies your needs, you are going to answer this question for many choices of $K$.

## Standard input

The input has a single integer $N$ on the first line.

The second line has $N$ integers. The $i$-th is $S_i$.

The next line has a single integer $Q$.

Each of the next $Q$ lines has a single integer $K$ as a query, for which you need to determine the minimum number spells required to obtain exactly $K$ magical stones.

## Standard output

For each query, output the minimum number of spells required on a single line. If it is impossible to obtain exactly $K$ stones, output $-1$.

## Constraints and notes

- $2 \leq N \leq 10^5$
- $1 \leq S_i \leq N$. It is possible that $S_i = i$.
- $1 \leq Q \leq 10^5$
- In all queries $1 \leq K < N$
- For $50\%$ of the test data, $N \leq 1\,000, Q \leq 1\, 000$.

## Examples

### Example 1

Input:
```
5
3 3 2 3 1
4
3
2
1
4
```

Output:
```
1
2
-1
-1
```

Explanation:

Initially, you have one stone in each of the $5$ states $\{1,2,3,4,5\}$. When you cast the first spell, the stone state in $3$ transforms to state $2$ ($S_3=2$). The stone in state $5$ transforms to state $1$ ($S_5=1$).  The stones in state $1, 2, 4$ transform to state $3$ ($S_1,S_2,S_4=3$). They purify each other and become one stone in state $3$. Therefore after one spell, you will have three stones in states $\{1,2,3\}$. After a second spell, you will have two stones in states $\{2, 3\}$. You will not be able to combine the last two stones into one. You also cannot obtain four stones.
