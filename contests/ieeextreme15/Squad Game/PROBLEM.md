# Squad Game

**IEEEXtreme 15.0** · Time limit: 2000 ms · Memory limit: 1024 MB

**CS Academy:** <https://csacademy.com/ieeextreme-practice/task/squad-game/>

Three groups of players are standing on a field to play a Squad game. Each group has exactly $N$ players, and there are $3N$ players in total. The Squad game is played in teams. Each team has exactly $3$ players -- one from each group. Every team controls the triangular area formed by the three points at which the three team members are standing. Players may share their standing points, and a team is allowed to control an area of zero.

The Squad game would become the most interesting when the sum of areas controlled by all the $N$ teams is minimized. How should the players form their teams to make the game most interesting?

## Standard input

The first line contains an integer $N$. This is followed by $3N$ lines that each have the $X$ and $Y$ coordinates of one player. The first $N$ lines are for players from the first group, the next $N$ lines are for players from the second group, and the last $N$ lines are for players from the third group.

## Standard output

Write $N$ triplets to the output file, one triplet per line. Each triplet has three $1$-based indices $a, b, c$ between $1$ and $N$ to describe a team consisting of player $a$ from the first group, player $b$ from the second group, and player $c$ from the third group. Every player must be assigned to a team.

## Constraints and notes

- All coordinates are integers between $0$ and $10^6$.
- The score per test is $\frac{Smallest Area}{Your Area}$, where $Smallest Area$ is the smallest area among all competition submissions, and $Your Area$ is your response on that test case.
- All tests are worth the same number of points, and their total value is normalized to $100$ points.
- Scores are independent between your submissions. That means that if you have a submission that scores better on test case $1$, and another that scores better on test case $2$, these will *not* be merged, and only your best overall submission will be considered.
-  Unlike for other tasks, the time limit is the same for all programming languages.
- For $8.33\%$ of the test files $1 \le N \le 7$
- For $33.33\%$ of the test files $1 \le N \le 300$
- For all the test files $1 \le N \le 100\,000$

## Examples

### Example 1

Input:
```
4
6 2
8 8
3 5
1 2
8 6
7 5
3 6
6 4
2 2
2 1
0 3
2 2
```

Output:
```
1 4 1
2 1 2
3 3 3
4 2 4
```

Explanation:

In the figure below, players in the first group are marked in blue, the second group in red and the third group in black:

<Geometry width={350} height={315} xDomain={[-1, 9]} yDomain={[0, 9]} lines={[]} circles={[]} segments={[]} points={[{x: 6, y: 2, color: "blue", label: "1"},{x: 8, y: 8, color: "blue", label: "2"},{x: 3, y: 5, color: "blue", label: "3"},{x: 1, y: 2, color: "blue", label: "4"},{x: 8, y: 6, color: "red", label: "1"},{x: 7, y: 5, color: "red", label: "2"},{x: 3, y: 6, color: "red", label: "3"},{x: 6, y: 4, color: "red", label: "4"},{x: 2, y: 2, color: "black", label: "1&4"},{x: 2, y: 1, color: "black", label: "2"},{x: 0, y: 3, color: "black", label: "3"},{x: 2, y: 2, color: "black", label: ""}]} polygons={[[{x: 6, y: 2}, {x: 6, y: 4}, {x: 2, y: 2}], [{x: 8, y: 8}, {x: 8, y: 6}, {x: 2, y: 1}], [{x: 3, y: 5}, {x: 3, y: 6}, {x: 0, y: 3}], [{x: 1, y: 2}, {x: 7, y: 5}, {x: 2, y: 2}]]} />
