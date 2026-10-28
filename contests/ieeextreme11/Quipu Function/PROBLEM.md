**CS Academy:** <https://csacademy.com/ieeextreme-practice/task/5802db6cc4107baa3e135d06a31494b5/>

# Quipu Function

**IEEEXtreme 11.0** · Time limit: 1000 ms · Memory limit: 10 MB

Today is your first math class in Peru. Probably you know that Peruvian teachers include words in Quechua language in their classes.

In this context, your teacher defines a curious function $q(n, d)$ for a pair of positive integers $n$ and $d$. This function is called /Quipu Function/ and it's defined as the number of divisors of $n$ which are not divisible by $d$.

The math class about /Quipu function/ was amazing. After class, some students try to challenge the teacher. They ask questions like the following: "Given the positive integers $a$, $b$ and $d$ (where $d$ is a prime number), can you tell me the result of next expression:

$\sum_{i=a}^{b} q(i, d)$ where $q$ is the /Quipu Function/".

Unfortunately, the teacher got tired but he wants to answer all the questions by his students. Since he knows that you are the best programmer in class, he wants to know if you can help him by creating an application to compute the results for the student questions.

## Standard input

In the first line there are three integers <Latex value="t"/> <Latex value="(1 \leq t \leq 5)"/>, <Latex value="a"/> and <Latex value="b"/> (<Latex value="1 \leq a \leq b \leq 10^{12}"/> and <Latex value="b - a \leq 10^{5}"/>), where <Latex value="t"/> represents the number of students (queries). In each one of the next <Latex value="t"/> lines there is one prime integer <Latex value="d_{i}"/> <Latex value="(d_{i} < 10^{12}"/>).

## Standard output

For each query you need to write the result of the target expression given $a$, $b$ and $d_{i}$.

## Constraints and notes

- $1 \leq t \leq 5$
- $1 \leq a \leq b \leq 10^{12}$
- $b - a \leq 10^{5}$
- $2 \leq d_i \leq 10^{12}$, $d_i$  is prime

## Examples

### Example 1

Input:
```
2 3 6
3
5
```

Output:
```
8
10
```

Explanation:

In the sample input $t = 2$, so you have to answer to two questions where $a = 3$ and $b = 6$.

In the first question, $d = 3$ so we need to sum the following:

- $q(3,3) = 1$: the divisors are $\{1,3\}$, but $3$ is not counted because $d|3$
- $q(4,3) = 3$: the divisors are $\{1, 2, 4\}$
- $q(5,3) = 2$: the divisors are $\{1, 5\}$
- $q(6,3) = 2$: the divisors are $\{1,2,3,6\}$, but $3$ and $6$ are not counted because $d|3$ and $d|6$.

So the sum $1 + 3 + 2 + 2 = 8$.

In the second question, $d = 5$ so we need to sum the following:

- $q(3,5) = 2$: the divisors are $\{1,3\}$
- $q(4,5) = 3$: the divisors are $\{1, 2, 4\}$
- $q(5,5) = 1$: the divisors are $\{1, 5\}$, but $5$ is not counted because $d|5$.
- $q(6,5) = 4$: the divisors are $\{1,2,3,6\}$

So the sum $2 + 3 + 1 + 4 = 10$.

Note about this notation $x|y$: the $|$ sign means that $x$ divides $y$, or that $\frac{y}{x}$ is an integer.
