# Linearly Separable Samples

**IEEEXtreme 14.0** · Time limit: 5000 ms · Memory limit: 256 MB

**CS Academy:** <https://csacademy.com/ieeextreme-practice/task/linearly-separable-samples/>

A linear classifier, especially the Support Vector Machine (SVM), is a popular tool in the task of pattern recognition and artificial intelligence. An essential problem for the linear classifier is whether the given samples are linearly separable.

Let’s consider the 2D cases without the bias term. Each sample has two features, $x_{1} \in \mathbb R$ and $x_{2} \in \mathbb R$, and a label $y \in \{ 1,-1\}$. You will be given $T$ queries. For each query you are given a group of points on a 2D plane, your task is to determine whether the positive samples (labelled $1$) and the negative samples (labelled $-1$) can be separated by a line through the origin $(0,0)$. If a line goes through some positive and/or negative points but separates all other points, it can be also accepted.

Mathematically speaking, you are asked to find whether there exist $w_{1} \in \mathbb R$ and $w_{2} \in \mathbb R$ , $s. t.$

<Latex value="\langle[ w_{1},w_{2}], [x_{1},x_{2}]\rangle  = w_{1}x_{1}+w_{2}x_{2}\ge0\;\mathrm{IFF}\;y=1 " />

<Latex value="\langle[ w_{1},w_{2}], [x_{1},x_{2}]\rangle  = w_{1}x_{1}+w_{2}x_{2}\leq0\;\mathrm{IFF}\;y=-1 " />

hold for all samples $(x_1,x_2),y$.

## Standard input

The first line of the input has an integer $T$ which represents the number of queries. Then, $T$ queries follow. The first line of each query has an integer $N$ that denotes the number of points in the query. Each of the following $N$ rows has two floating point numbers and an integer separated by single spaces. They represent the two features $x_{1}$, $x_{2}$ and the label $y$ of one point.

## Standard output

For each query, output the answer on a single line. Output `YES` if the given points can be separated by a line through the origin, and `NO` otherwise.

## Constraints and notes

- $1\leq T\leq10$
- $1 \leq N \leq 10^5$
- $-100.0 \leq x_{1},x_{2} \leq 100.0$
- $y=1$ or $y=-1$
- $x_1, x_2$ are given with at most two decimal points.
- Points may overlap and have the same $x_1, x_2$.
- For $50\%$ of the test data, $1 \leq N \leq 5\,000$

## Examples

### Example 1

Input:
```
2
9
-2.0 1.0 1
2.0 2.0 -1
4.0 2.5 -1
4.0 0.5 -1
-1.0 -1.0 1
4.0 1.5 -1
-3.0 -1.0 1
2.0 3.0 -1
-4.0 1.0 1
4
2.0 2.0 1
2.0 -2.0 -1
-2.0 2.0 -1
-2.0 -2.0 1
```

Output:
```
YES
NO
```

Explanation:

<Geometry circles={[]}

points={[{x:-2 , y:1 , label:"+"},{x:2 , y:2 , label:"-"},{x: 4, y: 2.5, label:"-"},{x: 4, y: 0.5, label:"-"},{x:-1 , y:-1 , label:"+"},{x:4 , y:1.5 , label:"-"},{x:-3 , y:-1 , label:"+"},{x:2 , y:3 , label:"-"},{x:-4 , y:1 , label:"+"}]} lines={[{a: 2, b: 1, c: 0}, {a: 0, b: 1, c: 0}, {a: 1, b: 0, c: 0}]} polygons={[]} segments={[]} xDomain={[-5, 5]} yDomain={[-5, 5]}/>

For the first query, it can be seen from the figure that those points can be separated by the line there.

<Geometry circles={[]}

points={[{x:2 , y:2 , label:"+"},{x:2 , y:-2 , label:"-"},{x: -2, y: 2, label:"-"},{x: -2, y: -2, label:"+"}]} lines={[{a: 0, b: 1, c: 0}, {a: 1, b: 0, c: 0}]} polygons={[]} segments={[]}

xDomain={[-3, 3]} yDomain={[-3, 3]}/>

For the second query, it is the famous XOR case. It's impossible to separate the four points using just one line.
