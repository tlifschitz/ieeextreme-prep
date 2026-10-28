# Triumvirates

**IEEEXtreme 18.0** · Time limit: 1000 ms · Memory limit: 512 MB

**CS Academy:** <https://csacademy.com/ieeextreme-practice/task/triumvirates/>

They say that two heads are better than one. Well, what's better than two heads? Three heads, of course.

For this problem, you've got a group of $N$ friends, where $N$ is a multiple of $3$. Each is located in a 2D location, given by their coordinates. We want to group them together in triumvirates (which here will mean groups of three friends, one for each E in IEEE). We define the stability of a triumvirate as the difference between the longest distance and the shortest distance between any two members of that triumvirate.

## Standard input

The first line of the input contains the number $N$ and the next $N$ lines contain a pair of integer coordinates of the friends, in order from the ones with index $0$ to $N-1$.

## Standard output

The output should contain $N / 3$ lines, where each line should contain the indices of the points in the input that should form groups. Each index from $0$ to $N-1$ must be included in exactly one line.

## Scoring

Your score for a test case is the sum of all the stabilities for all triumvirates.

As this is an optimization task, you should get a score that's as low as possible. The number of points you get will be considered relative to the best solution of any contestant for that test case. To be precise, the formula for points per test case is:

$\text{TestValue} * \frac{\text{BestScore}}{\text{YourScore}}$ where $\text{BestScore}$ is the best score on that test case among all contestants, and YourScore is your score on that test case.

The test value is the same for all test cases.

## Constraints and notes

- $N \leq 99\ 999$.
- All the coordinates in the input fit into signed 32 bit integers.
- It's guaranteed that the best score for each test is strictly greater than $0$.
- Note that the time limit is the same for all programming languages.

## Examples

### Example 1

Input:
```
9
26 28
22 1
4 26
6 28
21 15
14 14
3 2
20 22
21 10
```

Output:
```
0 1 2
6 3 8
5 7 4
```

Explanation:

The three triumvirates are shown below:

            <Geometry width={350} height={315} xDomain={[-2, 32]} yDomain={[-2, 32]} lines={[]} circles={[]} segments={[]}

                      points={[{x: 26, y: 28, label: "0"}, {x: 22, y: 1, label: "1"}, {x: 4, y: 26, label: "2"}, {

                          x: 6,

                          y: 28,

                          label: "3"

                      }, {x: 21, y: 15, label: "4"}, {x: 14, y: 14, label: "5"},

 {x: 3, y: 2, label: "6"},

{x: 20, y: 22, label: "7"}, {

                          x: 21,

                          y: 10,

                          label: "8"

                      }]}

                      polygons={[[{x: 26, y: 28}, {x: 22, y: 1}, {x: 4, y: 26}], [{x: 6, y: 28}, {x: 3, y: 2}, {x: 21, y: 10}], [{x: 21, y: 15}, {x: 14, y: 14}, {x: 20, y: 22}]]}

            />
