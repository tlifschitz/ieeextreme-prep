# Finding Shelter

**IEEEXtreme 10.0** · Time limit: 2000 ms · Memory limit: 512 MB

**CS Academy:** <https://csacademy.com/ieeextreme-practice/task/finding-shelter/>

A group of $N$ soldiers found themselves in a dangerous zone and are under heavy fire from the enemy. Gigel the commander has a map with the position of the soldiers and knows the coordinates of $N$ safety shelters with a capacity of one person each. Gigel wants to make a plan to save the soldiers with the lowest risk. The risk of a soldier being hurt is the distance between him and his assigned shelter. Gigel wants each soldier to have a good chance of surviving, so the maximal distance between a soldier and his assigned shelter should be as low as possible. If there are multiple solutions, he also wants to minimize the sum of distances to lower the total risk.

Given $N$, the positions of the $N$ soldiers, and the position of the $N$ shelters, you have to assign a shelter to each soldier. Find the lowest distance and the sum of distances.

## Standard input

The first line contains the integer $N$, on a line by itself.

The next *N* lines contain two space-separated floating point numbers, with the $i^{th}$ line giving the $x$ and $y$ coordinates for the $i^{th}$  soldier.

The next $N$ lines contain two space-separated floating point numbers, with the $i^{th}$ line giving the $x$ and $y$ coordinates for the $i^{th}$ shelter.

The floating point numbers will not have more than three digits after the decimal point.

## Standard output

The first line of output should contain the maximal distance between a soldier and his shelter.

The second line of output should contain the sum of the distances that all soldiers must travel.

Note that these numbers must be within $10^{-4}$ of the expected output.

## Constraints and notes

- $1 \leq N \leq 500$
- $0 \leq x, y \leq 1000$
- The distance between a soldier and a shelter is equal to the [Euclidean distance](https://en.wikipedia.org/wiki/Euclidean_distance) between their coordinates.

## Examples

### Example 1

Input:
```
4
0.0 0.0
0.0 1.0
1.0 0.0
1.0 1.0
2.0 0.0
0.0 2.0
0.0 1.0
1.0 0.0
```

Output:
```
1
4
```

Explanation:

You can assign soldier $1$ to shelter $3$, soldier $2$ to shelter $2$, soldier $3$ to shelter $1$ and soldier $4$ to shelter $4$. There is no other assignment with lower maximal distance or with equal maximal distance but lower sum of distances.
