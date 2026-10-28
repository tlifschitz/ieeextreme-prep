# Corporation

**IEEEXtreme 18.0** · Time limit: 1000 ms · Memory limit: 256 MB

**CS Academy:** <https://csacademy.com/ieeextreme-practice/task/corporation/>

There is a corporation with $N$ employees with ids $1, 2, \ldots, N$. Each employee has some initial monthly salary. There are two types of events:

- Type 0: All employees from $l$ to $r$ have their salary changed to $c$.
- Type 1: Each employee from $l$ to $r$ gets their salary changed by $c$ (where $c$ can be negative).

After each event, each employee's happiness increases by $1$ if their salary has just increased and decreases by $1$ if their salary has just decreased — nothing happens if their salary didn’t change.

There are also two types of queries:

- Type 2: What’s the average salary of all employees from $l$ to $r$?
- Type 3: What’s the average happiness of all employees from $l$ to $r$?

Process $Q$ events and queries.

# Input

The first line contains two integers $N$ and $Q$. The next line contains $N$ integers representing the initial salaries of the employees. The next $Q$ lines describe consecutive events and queries, formatted as follows:

- For type 0: `0 l r c`
- For type 1: `1 l r c`
- For type 2: `2 l r`
- For type 3: `3 l r`

# Output

For each query of type 2 and type 3, output the result on a new line. The result should be printed as a fraction of the form $P/Q$ where $P$ and $Q$ are coprime integers ($\text{gcd}(P, Q) = 1$).

# Constraints and notes

- $1 \leq N, Q \leq 2 \cdot 10^5$
- The initial salaries are integers from the interval $[1, 10^9]$
- $1 \leq l \leq r \leq N$
- $-10^9 \leq c \leq 10^9$
- Salary values can become negative after some events
- The inital happiness level of each employee is $0$

## Examples

### Example 1

Input:
```
5 8
1 3 5 4 2
1 2 5 -1
2 1 4
0 2 3 3
3 1 5
1 4 5 3
0 3 4 5
3 1 5
2 2 5
```

Output:
```
5/2
-4/5
-2/5
17/4
```
