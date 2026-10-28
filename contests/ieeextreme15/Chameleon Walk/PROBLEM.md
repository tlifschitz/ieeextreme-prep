# Chameleon Walk

**IEEEXtreme 15.0** · Time limit: 6000 ms · Memory limit: 256 MB

**CS Academy:** <https://csacademy.com/ieeextreme-practice/task/chameleon/>

There lives a happy chameleon in a large forest. On one cozy afternoon Ms. Chameleon decides to take a walk. There are $N$ junctions in the forest numbered $1$ to $N$, and $M$ bidirectional paths of various lengths connecting these junctions. Ms. Chameleon starts at junction $1$ and would like to walk to junction $N$. She walks at a constant speed of one unit distance per second.

All the junctions in the forest are safe for Ms. Chameleon. However the paths may be dangerous. Each path in the forest has a color represented by one of the first $5$ lowercase letters `a` to `e`. If Ms. Chameleon walks on a path of which the color is different than her own color, she would be noticed and caught by the birds hovering over the forest. Therefore Ms. Chameleon must change her own color to the color of the path in order to take a path of a color that is currently different from her own color. Ms. Chameleon may change into any color, and initially her color is `a`.

Ms. Chameleon chooses a *positive* integer value $C$ for her walk, which is the number of seconds she takes to change her color once. The value $C$ remains constant during the entire walk. As changing color quickly is very tiring and Ms. Chameleon is not that energetic, she would like to change color as slowly as possible. Yet she does not want the walk to take too long. She wants to find the largest possible integer $C$ so that she can arrive at junction $N$ within $K$ seconds.

## Standard input

The input has a single integer $T$ on the first line, the number of test cases.

Each test case has three integers $N$, $M$, and $K$ on the first line.

Each of the next $M$ lines describes a bidirectional path in the forest. A path is given by three integers $x, y, d$ and a single lowercase letter $c$. $x, y$ are the two junctions the path connects. $d$ is the distance of the path. $c$ is the color of the path.

## Standard output

For each test case, output the largest value of $C$ Ms. Chameleon may choose so that she can arrive at junction $N$ in no more than $K$ seconds. If Ms. Chameleon cannot arrive at junction $N$ in time regardless of what $C$ she chooses, output `impossible`. If $C$ can be infinitely large, output `relaxing`.

## Constraints and notes

- $1 \leq T \leq 10$
- $2 \leq N \leq 2 \cdot 10^4$
- $1 \leq M \leq 2 \cdot 10^4$
- $1 \leq K \leq 10^9$
- For each path, $1 \leq x, y \leq N, x \neq y, 1 \leq d \leq 10^4$. The color $c$ is a lowercase letter among `a`, `b`, `c`, `d`, and `e`.
- There can be multiple paths between a same pair of junctions.
- It is guaranteed that it is possible to reach junction $N$ from junction $1$ if all paths can be taken regardless of their colors.
- For $66\%$ of the test data, it is guaranteed that if there exists some value of $C$ that works, then the largest feasible value of $C$ does not exceed $50$. In other words, if the answer is neither `impossible` nor `relaxing`, then the answer is an integer between $1$ and $50$.

## Examples

### Example 1

Input:
```
5
5 6 60
1 2 20 a
1 3 40 a
2 3 10 b
2 4 10 b
5 4 10 a
5 3 20 b
5 6 50
1 2 20 a
1 3 40 a
2 3 10 b
2 4 10 b
5 4 10 a
5 3 20 b
2 1 10
1 2 10 b
2 1 10
1 2 20 a
2 1 10
1 2 10 a
```

Output:
```
10
5
impossible
impossible
relaxing
```

Explanation:

- Case $1$: Ms. Chameleon can take the path $1 \rightarrow 2 \rightarrow 3 \rightarrow 5$. She needs to change color once using $10$ seconds before taking path $(2, 3)$.
- Case $2$: This test case has the same forest as case $1$. Ms. Chameleon must take the path $1 \rightarrow 2 \rightarrow 4 \rightarrow 5$. She must change color twice along the way and change color more quickly. She cannot take the path in sample $1$, because that path is too long and does not allow her to arrive at the destination in time even if she chooses $C = 1$.
- Case $3$:  Ms. Chameleon must be able to change color instantly ($C = 0$) in order to arrive at junction $N$ in time. However, $C$ has to be a positive integer.
- Case $4$:  The only path has distance $20$, and there is no way to reach junction $N$ in $10$ seconds.
- Case $5$:  Ms. Chameleon does not need to change color and can still arrive at junction $N$ in time. So $C$ can be infinitely large.
