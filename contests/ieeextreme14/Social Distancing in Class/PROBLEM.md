# Social Distancing in Class

**IEEEXtreme 14.0** · Time limit: 1000 ms · Memory limit: 256 MB

**CS Academy:** <https://csacademy.com/ieeextreme-practice/task/social-distancing/>

The School of Xtreme is considering reopening in-person class for the best learning experience. To maximize social distancing, the school wants to seat the students in a classroom such that the sum of squared distances between all pairs of students is maximized. There are $N$ students in the class numbered from $1$ to $N$. There are exactly $N-1$ pairs of students who are best friends. The best friend relationships form a tree structure, so that if everyone keeps sharing a story with his/her best friends, the story will eventually be shared across the whole class. To keep the students happy, we need to keep everyone no farther than $1$ meter from each of their best friends.

The classroom can be thought of as a Euclidean plane of infinite size, and the students are points on this plane. What is the maximum possible sum of squared distances between every pair of students, if they are seated optimally?

## Standard input

The first line of input has a single integer $N$, the of the number of students.

The next $N-1$ lines each have a single integer, giving $B_2, B_3, ... B_N$, where $B_i$ is the best friend of student $i$.

## Standard output

Output a single line including the maximum possible sum of squares of distances. Your answer is considered correct if it has an absolute or relative error of $10^{-6}$ from the correct answer.

## Constraints and notes

- $1 \leq N \leq 10^5$
- $B_i < i$
- It is fine for two students to be seated at the same location.
- For $30\%$ of the test data, $N \le 500$
- For $60\%$ of the test data, $N \le 5\,000$

## Examples

### Example 1

Input:
```
3
1
1
```

Output:
```
6
```

Explanation:

There are $3$ students. Both student $2$'s and student $3$'s best friends are student $1$. We can let the three students sit in a row, with student $1$ being in the middle and the other two students on the two sides at exactly $1$ meter from student $1$. The pairwise Euclidean distances in this optimal solution is $\{1, 1, 2\}$. Sum of their squares is $6$. The figure illustrates this arrangement.

Note that the absolute coordinates of the students do not matter. Only the relative distances between them affect the answer.

<Geometry xDomain={[0,4]} yDomain={[0, 2]} circles={[]} points={[{x: 2, y: 1, label: 1},{x: 1, y: 1, label: 2},{x: 3, y: 1, label: 3}]} lines={[]} polygons={[]} segments={[{x1: 1, y1: 1, x2: 2, y2: 1}, {x1: 2, y1: 1, x2: 3, y2: 1}]}/>

### Example 2

Input:
```
5
1
2
3
4
```

Output:
```
50.0
```
