# Binary Quilts

**IEEEXtreme 10.0** · Time limit: 2000 ms · Memory limit: 512 MB

**CS Academy:** <https://csacademy.com/ieeextreme-practice/task/binary-quilts/>

Binary Quilts Incorporated uses custom machinery to make square blankets that consist of $25$ black or white squares that are sewn together.  Whenever they want to change designs for the blankets, they are limited to a small set of operations, and they would like your help to find the fewest operations needed to change from one design to another.

The designs are specified as a $5$ by $5$ matrix.  The operations that are available change a square region of the matrix.  This square region can be any contiguous $1\times 1$, $2\times2$, $3\times3$, $4\times4$, or $5\times5$ portion of the matrix.  The operations on these square regions are:

- Flip a square region of the matrix horizontally.
- Flip a square region of the matrix vertically.
- Negate a square region, i.e. invert all of the colors in this region.

Please see the explanation of the sample input below, for figures with these operations.

## Standard input

The first line of input contains $t$, which gives the number of test cases.

Each test case is preceded by a blank line.

The test case consists of $5$ lines.  The first $5$ characters in the $i^{th}$ line of the test case represent the $i^{th}$ row of the source matrix. The sixth character in the row is a space.  The last $5$ characters in the row represent the $i^{th}$ row of the target matrix.  The `X` character is used to represent a black square and the `.` character is used to represent a white square.

## Standard output

For each test case, you should output, on a line by itself, the minimum number of operations needed to transform the source matrix into the target matrix.

## Constraints and notes

- $1 \leq t \leq 5$

## Examples

### Example 1

Input:
```
4

..... .....
..... .X...
.X.X. XXX..
..X.. .X...
.X.X. .X...

..... .....
XXX.. XXXX.
X..X. XXXX.
X.... X....
X.... XXXX.

..... .....
X...X XXXX.
XX.XX XXXX.
X.X.X X....
X...X XXXX.

..X.. ..X..
..X.. .X.X.
..X.. .X.X.
..X.. .X.X.
..X.. ..X..
```

Output:
```
4
3
3
1
```

Explanation:

In the first test case, the source matrix can be transformed to the target matrix with four operations.  For example,

1. Vertical Flip: ![](images/1493729855-44331327.png)
1. Horizontal Flip: ![](images/1493729855-643563233.png)
1. Vertical Flip:![](images/1493729855-3433872600.png)
1. Negate: ![](	https://publicmedia1.csacademy.com/public/1493729855-466834891.png)

In the second test case, the source matrix can be transformed to the target matrix with three operations. For example,

1. Negate:![](images/1493729855-144575637.png)
1. Negate:![](images/1493729855-4236107936.png)
1. Negate:![](images/1493729855-876254929.png)

In the third test case, the source matrix can be transformed to the target matrix with three operations. For example,

1. Negate:![](images/1493729855-2693749376.png)
1. Horizontal Flip (or a vertical flip or negate):![](images/1493729855-749812849.png)
1. Negate (or a vertical flip):![](images/1493729855-3307292015.png)

In the fourth test case, the source matrix can be transformed to the target matrix with a single negate operation:

![](images/1493729855-3606405439.png)
