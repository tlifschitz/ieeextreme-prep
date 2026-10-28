# Xtreme Winners

**IEEEXtreme 15.0** · Time limit: 500 ms · Memory limit: 256 MB

**CS Academy:** <https://csacademy.com/ieeextreme-practice/task/xtreme-winners/>

<Quote value="I have only made this letter longer because I have not had the time to make it shorter." source="Blaise Pascal (Letter 16, 1657)" />

Write a program that reads an IEEEXtreme winner team name and prints the number of the competition edition they won.

The programs which correctly solve all $14$ years will be scored by the number of characters in the source code (the shorter the better). You must pass all test cases (including the examples) to get any points for this task.

We're also making it incredibly easy for you, by just giving your the chronological list of winners:

```
Team 1
Knapsackers@UNT
MoraSeekers
SurpriseTeam
CuSAT
DongskarPedongi
cofrades
viRUs
TeamName
TeamEPFL1
whatevs
WildCornAncestors
TheCornInTheFields
Aurora
```

## Standard input

The first line will contain the name of a team that won a past Xtreme.

## Standard output

The first line of your output should contain a single integer between $1$ and $14$, the number of the edition that was won by the team in the input.

## Constraints and notes

- Team names are always provided as they are listed above, with the same letter cases and format.
- You must solve all tests, including the examples, correctly to get any points.
- The scoring function will be $(\frac{\text{ShortestCode}}{\text{YourSourceLength}})^2$, where $\text{ShortestCode}$ is the shortest competitor code that passes all tests.
- For convenience, whitespaces in the beginning and end of the solution code will be ignored. All the other characters are counted.

## Examples

### Example 1

Input:
```
Team 1
```

Output:
```
1
```

### Example 2

Input:
```
Aurora
```

Output:
```
14
```
