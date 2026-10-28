**CS Academy:** <https://csacademy.com/ieeextreme-practice/task/robot-versus-fan/>

# Robot versus Fan

**IEEEXtreme 16.0** · Time limit: 3000 ms · Memory limit: 256 MB

*This problem is sponsored by Huawei.*

A ceiling fan is blowing dust around a square room in a regular pattern.  At the same time, a robot vacuum is following a path through the room. Your task is to see if the robot will be able to capture the dust, and if so, how long it will take.

You are given a grid that divides the room into cells. Each cell has one of the following directional symbols: '>', '<', '^', and 'v'.  The robot always starts in the cell at the upper, left corner. At each timestep, it moves to the adjacent cell indicated by the direction of the symbol in its current cell. The robot will never be directed to move outside of the room.

The dust moves in a periodic pattern through the room. You are given its position at each timestep in one iteration of the pattern. After it completes an iteration, it repeats the pattern. If the robot and the dust are in the same location at the same timestep, the robot vacuum will capture the dust.

## Standard input

The input begins with an integer $T$ on a line by itself, giving the number of test cases.

Each test case begins with an integer $r$ on a line by itself, that gives the length of one wall of the room.  Since the room is square, the width is equal to the length.

The next $r$ lines give the pattern that the robot will follow in the room.  Each line will have $r$ symbols, chosen from the following: '>', '<', '^', and 'v'.

Next there is an integer $d$ which gives the length of the pattern that the dust follows.

The following $d$ lines contain two space-separated integers. Starting at $i = 0$, the line $i$ contains $(r_i,c_i)$ indicating that at timestep $i$ the dust will be in row $r_i$ and column $c_i$.  Note that the first row is numbered 0, and the first column is numbered 0.  Also, after the dust is in the last position in the input, the pattern repeats and it is moved back to $(r_0,c_0)$.

## Standard output

Output consists of one line per testcase.  The line should read "never" if the dust will never be captured by the robot vacuum.  Otherwise, it should contain the number of timesteps needed for the robot to capture the dust.

## Constraints and notes

- $1 \leq T \leq 10$
- $3 \leq r \leq 400$
- $1 \leq d \leq 160,000$
- $0 \leq r_i, c_i \lt r$ for $0 \leq i \lt d$

## Examples

### Example 1

Input:
```
3
4
>>>v
^v<<
^>>v
^<<<
3
1 1
2 2
3 0
3
>>v
>^<
^^^
2
2 0
1 1
4
>>>v
^<<v
>>^v
^<<<
4
1 1
2 2
1 1
3 0
```

Output:
```
6
never
14
```

The table below gives the robot vacuum and dust positions as a (row, column) pair.  Note that the dust locations repeat every three timesteps.  Since the robot and the dust are in the same position at timestep 6, you would output 6.

```
| Timestep | Robot | Dust  |
| -------- | ----- | ----- |
| 0        | (0,0) | (1,1) |
| 1        | (0,1) | (2,2) |
| 2        | (0,2) | (3,0) |
| 3        | (0,3) | (1,1) |
| 4        | (1,3) | (2,2) |
| 5        | (1,2) | (3,0) |
| 6        | (1,1) | (1,1) |
```

For the second test case, the first few positions for the robot and the dust are given in the table below.  Note that the robot never visits cell (2,0).  The robot and the dust both visit (1,1), but in the table, the robot only visits in even timesteps and the dust only visits in odd timesteps.  This pattern would repeat forever without the robot and dust ever being in the same cell.  Thus, you would output "never".

```
| Timestep | Robot | Dust  |
| -------- | ----- | ----- |
| 0        | (0,0) | (2,0) |
| 1        | (0,1) | (1,1) |
| 2        | (0,2) | (2,0) |
| 3        | (1,2) | (1,1) |
| 4        | (1,1) | (2,0) |
| 5        | (0,1) | (1,1) |
| 6        | (0,2) | (2,0) |
| 7        | (1,2) | (1,1) |
| 8        | (1,1) | (2,0) |
| ...      | ...   | ...   |
```

The table below gives the positions of the robot and the dust for the third testcase, where the expected output is 14.

```
| Timestep | Robot | Dust  |
| -------- | ----- | ----- |
| 0        | (0,0) | (1,1) |
| 1        | (0,1) | (2,2) |
| 2        | (0,2) | (1,1) |
| 3        | (0,3) | (3,0) |
| 4        | (1,3) | (1,1) |
| 5        | (2,3) | (2,2) |
| 6        | (3,3) | (1,1) |
| 7        | (3,2) | (3,0) |
| 8        | (3,1) | (1,1) |
| 9        | (3,0) | (2,2) |
| 10       | (2,0) | (1,1) |
| 11       | (2,1) | (3,0) |
| 12       | (2,2) | (1,1) |
| 13       | (1,2) | (2,2) |
| 14       | (1,1) | (1,1) |
```
