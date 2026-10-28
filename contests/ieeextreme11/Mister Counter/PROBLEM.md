# Mister Counter

**IEEEXtreme 11.0** · Time limit: 1000 ms · Memory limit: 128 MB

**CS Academy:** <https://csacademy.com/ieeextreme-practice/task/3dd761f749054a509a0012c5beee0e35/>

Do you know Mr. Counter? Well, he is obsessed with counting. For instance, he counts the number of distinct configurations that a phone number might have with $k$ digits, also the number of ways he can dress up with his current clean clothes. This time he has been thinking of a more complicated task.

For any array $a$ of *distinct* integers, Mr. Counter denotes by $F_a$ an array that has the following properties:

1. It contains the same elements as $a$
1. $F_a$ is lexicographically greater than $a$
1. From all the arrays that respect property 2, $F_a$ is the lexicographically smallest one.
1. If there no array lexicographically greater than $a$, $F_a$ is equal to $a$.

/An array/  <Latex value="a"/> /is considered smaller than another array/ <Latex value="b"/> /if and only if there is a position/ <Latex value="i"/> /that satisfies/ $a_1 = b_1$, $a_2 = b_2$, ..., $a_{i - 1} = b_{i - 1}$, $a_{i} < b_{i}$.

Mr. Counter also defines the /cost/ of an array $a$ as the number of indices where $a$ differs from $F_a$.

Now it's your turn to help with a special task. Mr. Counter has an array $a$ consisting of <Latex value="n"/> *distinct* integers and he asks you $q$ queries. Each query consists of two indices $l$ and <Latex value="r"/> $(1 \leq l \leq r \leq n)$. Find the cost of the <Definition term="subarray"/> <Latex value="a_{l...r}"/>.

## Standard input

The first line contains an integer $n$ representing the number of elements $a$.

The second line contains the $n$ elements of $a$.

The third line contains the number of queries $q$.

Each of the next $q$ lines contains two numbers $l$ and $r$ ($1 \leq l \leq r \leq n$).

## Standard output

Print the answer for each query on a different line.

## Constraints and notes

- $1 \leq n \leq 250\,000$
- $0 \leq a_i \leq 10^9$
- $1 \leq q \leq 250\,000$

## Examples

### Example 1

Input:
```
5
5 4 3 2 1
2
1 5
2 4
```

Output:
```
0
0
```

### Example 2

Input:
```
6
0 2 7 5 4 3
2
1 2
1 6
```

Output:
```
2
5
```
