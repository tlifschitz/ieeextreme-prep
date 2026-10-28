# Scheduler

**IEEEXtreme 16.0** · Time limit: 1000 ms · Memory limit: 256 MB

**CS Academy:** <https://csacademy.com/ieeextreme-practice/task/scheduler/>

This is an easier version of the [Scheduler Redux](https://csacademy.com/ieeextreme16/task/scheduler-redux/) problem.

In this challenge you must figure out how quickly $N$ jobs can be completed by $M$ workers. Each job will take $2^x$ amount of time, where $x$ is a non-negative integer.

Since the amount of time could be quite large, you should indicate the amount of time needed modulo $10^9 + 7$.

*In this easier version of the problem, no two jobs will have the same time to finish.*

## Standard input

Each input has a single test case.

The input begins with a line containing two space-separated integers, $N$ and $M$.  $N$ specifies the number of jobs, and $M$ specifies the number of workers.

The next line of input contains $N$ integers, where the ith integer, $X_i$, indicates that job i takes $2^{X_i}$ time.

## Standard output

Output the minimum amount of time required to complete all of the jobs, modulo $10^9 + 7$.

## Constraints and notes

- $1 \leq N \leq 100,000$
- $1 \leq M \leq 20$
- $0 \leq X_i \lt 100,000$
- For any $i \neq j$, $X_i \neq X_j$

## Examples

### Example 1

Input:
```
4 3
0 1 2 4
```

Output:
```
16
```

Explanation:

The job times, respectively, are 1, 2, 4, 16.

One strategy is to give job 1 and 3 to Worker 1, Job 2 to Worker 2, and Job 4 to Worker 3. Worker 1 would complete the jobs in 5 time units (1 + 4). Worker 2 would complete the job in 2 time units, and worker 3 would complete the job in 16 units. So, the time needed is 16.

### Example 2

Input:
```
2 1
1 2
```

Output:
```
6
```

### Example 3

Input:
```
5 5
1 2 4 9999 10000
```

Output:
```
905611805
```
