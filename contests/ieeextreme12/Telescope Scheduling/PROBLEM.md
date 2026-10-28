# Telescope Scheduling

**IEEEXtreme 12.0** · Time limit: 10000 ms · Memory limit: 256 MB

**CS Academy:** <https://csacademy.com/ieeextreme-practice/task/telescope-scheduling/>

Joe and his friends want to observe the stars tonight using a unique telescope. Joe is an astronomy student and has a list of each of the stars that will be visible in the sky. Each star appears inside a certain time window with the possibility of multiple stars to overlap, so the group assigned a value to each star indicating the desirability of observing it.

The input consists on a list $L$ of time intervals in which the stars will be available for observation. Each interval $i \in L$ consists of the following elements:

- a start time $S_i$ after which the star will be available for observation;
- a finish time $F_i$ after which the star will no longer be available;
- a positive integer $D_i$ indicating the desirability to see the $i$-th star.

In order to satisfy the desirability of seeing the $i$-th star, the observations must be performed by the telescope for the entire time period from $S_i$ to $F_i$ (inclusive). Thus, two stars, $i$ and $j$, are not simultaneously observable (i.e. they *conflict*) if the time interval $[S_i,F_i]$ intersects the time interval $[S_j,F_j]$. Given the list $L$ of time intervals of availability of the stars in the sky, the optimization problem is to schedule the observations in a non-conflicting way so as to maximize the total desirability of the observations that are included in the schedule.

## Standard input

The first line of the input contains a positive integer $N$ indicating the number of stars.

Each of the following $i$ lines, $1 \leq i \leq N$, indicates the start ($S_i$) and finish ($F_i$) times of each star together with the desirability $D_i$ of seeing that star.

## Standard output

Print the sum of the desirability of the stars included in the schedule on the first line.

## Constraints and notes

- $1 \leq N \leq 10^4$
- $0 \leq S_i,F_i \leq 1\ 000$
- $1 \leq D_i \leq 5\ 000$

## Examples

### Example 1

Input:
```
7
2 7 3
6 11 5
4 17 4
13 23 2
9 30 3
24 28 5
0 5 5
```

Output:
```
17
```

Explanation:

Star 2 is in conflict with star 1, 3, and 5 and it has a higher desirability (5), so star 1, 3 and 5 are not observed.

All the desirability of the other stars adds up to `17`.
