# Scheduler Redux

**IEEEXtreme 16.0** · Time limit: 1000 ms · Memory limit: 256 MB

**CS Academy:** <https://csacademy.com/ieeextreme-practice/task/scheduler-redux/>

This is a harder version of the [Scheduler](https://csacademy.com/ieeextreme16/task/scheduler/) problem.

In this challenge you must figure out how quickly $N$ jobs can be completed by $M$ workers. Each job will take $2^x$ amount of time, where $x$ is a positive integer.

Since the amount of time could be quite large, you should indicate the amount of time needed modulo $10^9 + 7$.

*In this harder version of the problem, two jobs CAN have the same time to finish.*

## Standard input

Each input has a single test case.

The input begins with a line containing two space-separated integers, $N$ and $M$.  $N$ specifies the number of jobs, and $M$ specifies the number of workers.

The next line of input contains $N$ integers, where the $i^{th}$ integer, $X_i$, indicates that job $i$ takes $2^{X_i}$ time.

## Standard output

Output the minimum amount of time required to complete all of the jobs, modulo $10^9 + 7$.

## Constraints and notes

- $1 \leq N \leq 100,000$
- $1 \leq M \leq 20$
- $0 \leq X_i \leq 100,000$

## Examples

### Example 1

Input:
```
5 2
1 1 2 2 2
```

Output:
```
8
```

Explanation:

The job times are 2, 2, 4, 4, and 4, respectively.

One of the strategies is to give jobs 1, 2, and 3 to worker 1, and job 4 and 5 to worker 2.

The total time for worker 1 is 8 (from 2 + 2 + 4).  The total time for worker 2 is also 8 (from 4 + 4).  Thus, the time needed is 8.

### Example 2

Input:
```
3 1
1 2 2
```

Output:
```
10
```

### Example 3

Input:
```
5 2
9998 9998 9998 9999 10000
```

Output:
```
382014751
```
