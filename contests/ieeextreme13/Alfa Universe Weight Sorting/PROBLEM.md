**CS Academy:** <https://csacademy.com/ieeextreme-practice/task/alfa-universe-weight-sorting/>

# Alfa Universe Weight Sorting

**IEEEXtreme 13.0** · Time limit: 1000 ms · Memory limit: 256 MB

There are several races in Alpha universe and each one of them has a different weight. For some pairs of races, you are given the result of comparing their weight. From transitivity, you can deduce the order of some of the pairs that you are not given, but other pairs are not known. For example, if $A > B$ and $B > C$, you can deduce that $A > C$.

A /valid ordering/ is a permutation of all the races, such that for each pair $(A, B)$, if $A < B$ then $A$'s index in the permutation is smaller than $B$'s index.

Someone is asking you to compare the weight of two races that cannot be deduced from the known compared pairs. You want to answer it by providing a minimal number of /valid orderings/, such that:

- For every pair $(A, B)$, where it cannot be deduced which of them is lighter and which is heavier, there is at least one ordering where $A$ comes before $B$, and at least one ordering where $B$ comes before $A$.

For example, if there are four races: $A$, $B$, $C$ and $D$ and you know that:

1. The weight of $C$ is less than that of $B$;
1. The weight of $B$ is less than $D$;
1. And that the weight of $C$ is less than $A$.

In this case the six pairs are divided into the four known orders:

1. $C < A$
1. $B < D$
1. $C < B$
1. $C < D$

Two are unknown:

1. $A ? B$
1. $A ? D$

You can provide the following two /valid orderings/:

- $C < A < B < D$
- $C < B < D < A$

Where all these permutations obey all four known weight order relations and for any unknown pair there exists at least one permutation that cover each order of the pair.

Your task is to find the minimal number or permutations, $N$, and print the $N$ /valid orderings/.

## Standard input

The first line contains the number of races, $N$, and the number of known comparisons $M$.

The following $M$ lines contains the pairs in the format $XY$ where $X$ and $Y$ are uppercase letters representing the race.

## Standard output

The first line is the minimal number $K$ of permutations needed.

Each of the next $K$ lines should contains a permutation of the first $N$ letters of the alphabet.

- $K=0$ means that the problem can not be solved (the known comparisons are not transitive).
- $K=1$ means that there are no undetermined pairs and the next line is the only permutation that adheres to all the given constrains.

## Constraints and notes

- $1 \leq N \leq 26$ The races are denoted by the first $N$ letters in the English alphabet.
- $0 \leq M \leq 325$ You may assume that the input is in the correct format
- *This is an NP problem and it may not be possible for anyone to solve all the test cases within the time limits*

## Examples

### Example 1

Input:
```
4 4
CA
BD
CB
CD
```

Output:
```
2
CABD
CBDA
```

Explanation:

This sample is the example given above.

### Example 2

Input:
```
3 2
CA
AB
```

Output:
```
1
CAB
```

Explanation:

The given comparisons allow for only one permutation: $C < A < B$.

### Example 3

Input:
```
10 10
AB
AJ
DF
DC
FA
AC
EB
IH
JD
AI
```

Output:
```
0
```

Explanation:

Take the 3rd, 5th, 2nd and 10th comparisons and we get a contradiction: $D < F < A < J < D$.
