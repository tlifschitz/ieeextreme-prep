# Xtreme Teams

**IEEEXtreme 15.0** · Time limit: 2000 ms · Memory limit: 256 MB

**CS Academy:** <https://csacademy.com/ieeextreme-practice/task/xtreme-teams/>

In IEEEXtreme, each team consists of three students. The contest may challenge the students with problems on $M$ topics. There are $N$ students at a school who are known to specialize in some of those $M$ topics (possibly none, possibly all). In order to achieve best performance, for each of the $M$ topics, a team should have at least one student who specializes in that topic. In how many ways can a single team be formed by choosing $3$ students from the $N$ students, so that at least one student specializes in each of the $M$ topics?

## Standard input

The input begins with a single integer $T$ on the first line, the number of test cases.

The first line of each test case has two integers $N$ and $M$. The next $N$ lines each have a string of length $M$ that represents the topic specialties of one student. For each student, the $i$th letter is `y` if he/she specializes in topic $i$, or `n` otherwise.

## Standard output

For each test case, output the number of different ways to choose $3$ students to form a team on a single line.

## Constraints and notes

- $1 \leq T \leq 15$
- $3 \leq N \leq 5\,000$
- $1 \leq M \leq 18$
- For $33\%$ of the test files, $N \leq 100$, $M \leq 12$.
- For $66\%$ of the test files, $M \leq 12$.

## Examples

### Example 1

Input:
```
4
4 3
ynn
nyn
yyn
yny
4 5
yyyyy
yyynn
nyyyn
nnnny
5 4
ynnn
nynn
nnyn
nnny
nnnn
6 6
yynnyy
yynnyy
nnyyyy
nnyyyy
yyyynn
yyyynn
```

Output:
```
3
4
0
20
```

Explanation:

There are $4$ test cases. The first $3$ cases are explained below.

- Case $1$: The last student must be on the team because only that student is specialized in topic $3$. The other two team members can be chosen freely from the first three students, so there are $3$ ways.
- Case $2$: The first student can team up with any other two students. Additionally, the last three students can form a team.
- Case $3$: There are $4$ topics but all students only specialize in at most one topic. So there is no way to form a team.
