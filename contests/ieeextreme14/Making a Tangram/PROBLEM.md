# Making a Tangram

**IEEEXtreme 14.0** · Time limit: 1000 ms · Memory limit: 256 MB

**CS Academy:** <https://csacademy.com/ieeextreme-practice/task/making-tangram/>

In this challenge you are to create a beautiful tangram from a board of $N \times N$ cells. The board will be cut into $N$ tangram pieces. Each piece consists of exactly $N$ cells that are $4$-connected (up, down, left, right). All the tangram pieces shall together fit into the $N \times N$ board without extra or empty cells. To make the tangram fun, each piece will have a distinct color, and no two pieces shall be of a same shape.

Two tangram pieces are said to have a same shape if one can be rotated clockwise or counterclockwise to look exactly the same as the other. For example, the following four pieces are the same:

```
 X    X   XX     X
XX   XXX   XX  XXX
 XX  X     X    X
```
These two pieces have different shapes:

```
  X  X
XXX  XXX
```
A tangram piece is allowed to have holes, such as:

```
XXX
X X
XXX
```

Now it is up to you to design the tangram in whatever way you like!

## Standard input

The first line of the input has a single integer $T$, the number of test cases.

Each of the next $T$ lines has one test case with a single integer $N$, the size of the board.

## Standard output

For each test case, output any tangram design that satisfies the requirement. The output has $N$ lines, each with $N$ characters. Mark each tangram piece with any unique character from the alphabet: lowercase letters `a-z`, uppercase letters `A-Z`, or digits `0-9`. Any valid tangram will be accepted.

If there is no way to cut the board to make the tangram, output `impossible`  on a single line.

## Constraints and notes

- $1 \leq T \leq 20$
- $2 \leq N \leq 62$

## Examples

### Example 1

Input:
```
2
5
3
```

Output:
```
XXXTr
XTTTr
XTErr
mmEEr
mmmEE
impossible
```

Explanation:

In the first test case $N = 5$, note that you may pick any characters from the alphabet to color the tangram pieces.

In the second test case $N = 3$, only these two types pieces can be made. Therefore you cannot cut the board into three different pieces.

```
XX
X   XXX
```
