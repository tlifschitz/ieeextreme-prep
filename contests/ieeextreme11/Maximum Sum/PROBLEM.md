# Maximum Sum

**IEEEXtreme 11.0** · Time limit: 1000 ms · Memory limit: 256 MB

**CS Academy:** <https://csacademy.com/ieeextreme-practice/task/04dfa70efd936271ae191cb1a97eb876/>

Given a sequence that contains $n$ ($1 \leq n \leq 10^5$) integers, represented by ${a_1, a_2,...,a_n}$ ($0 \leq a_i \leq 10^5$), you have the amazingly easy task to reorder the sequence and maximize the formula $\sum_{i = 1}^{n - 1}{a_i * a_{i + 1}}$.

## Standard input

The first line of the input will contain an integer $t$ ($1 \leq t \leq 25$), which is the number of test cases to follow.

Each test case is composed of two lines:

- The first line of each test case contains an integer $n$, which is the length of the sequence.
- The second line of the test case contains $n$ integers indicating the ${a_1, a_2,...,a_n}$ sequence, each integer is separated by one space.

## Standard output

The output should contain $2*t$ lines, two lines for each test case:

- The first line of each test case should contain the maximum sum.
- The second line of the test case should contain $n$ integers indicating the reordered sequence. If there is more than one solution, print the one with the smallest alphabetical order.

## Contraints and notes

- $1 \leq t \leq 25$
- $1 \leq n \leq 10^5$
- $0 \leq a_i \leq 10^5$
- Sequence $a$ is considered smaller than sequence $b$ if and only if there is a position $i$ that satisfies $a_1 = b_1, a_2 = b_2,..., a_{i - 1} = b_{i - 1}, a_{i} < b_{i}$.

## Examples

### Example 1

Input:
```
4
10
1 2 1 5 4 2 1 1 8 9
3
5 2 0
9
5 9 0 0 4 6 2 3 2
4
2 1 7 1
```

Output:
```
173
1 1 1 2 4 8 9 5 2 1 
10
0 2 5 
152
0 0 2 3 5 9 6 4 2 
23
1 2 7 1 
```
