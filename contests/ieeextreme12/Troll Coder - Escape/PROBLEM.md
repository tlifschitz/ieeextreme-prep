# Troll Coder - Escape

**IEEEXtreme 12.0** · Time limit: 10000 ms · Memory limit: 256 MB

**CS Academy:** <https://csacademy.com/ieeextreme-practice/task/troll-coder-escape/>

The treasure is in your hands but there is only one way out of the island: the same way you used to get in! You have to cross the bridge again and the Troll is there waiting for you.

You are now faced with the same sequence guessing game, each sequence with exactly $N=100$. You have to solve every test with a maximum of $N+1$ queries to successfully cross the bridge, but the more queries you use the more treasure you will lose to the Troll.

You final score for this challenge will be based on the average number of queries needed per test case. If you use $N+1$ queries on all the tests you will not score any points.

## Interaction

At the beginning, you must read $T$, the number of test cases.

At the beginning of each test case, the Troll will give you a single integer $N$ which will represent the length of the sequence.

To submit a query, your program should output the letter `Q` followed by a space and by a binary sequence of length $N$ with each bit separated by a space. After each query you will receive an integer denoting the number of correct bits. The last submission will be your final answer and it should start with an `A` followed by a space and by a binary sequence of length $N$ with each bit separated by a space.

## Scoring

Assuming you provided a correct solution for all test cases, the scoring is computed as follows: let $A$ be the average of number of `Q` queries over all cases, then your score will be $5 \cdot (80 - A)$. In case this is negative, you will score $0$ points. In case this is greater than $100$, you will score $100$ points.

## Constraints and notes

- This task is *NOT* <Definition term="adaptive task" value="adaptive"/>
- You will be scored based on a single run of $T = 100$, with $N = 100$ for each test case.
- Your program can submit at most $N + 1$ queries before arriving at the correct answer.

## Examples

### Example 1

Input:
```
2
6
1 0 1 1 0 1
6
0 0 1 0 1 1
```

Output:
```

```

Explanation:

For clarity, the example uses $N=6$, but the actual test cases will consist solely of $N=100$.
