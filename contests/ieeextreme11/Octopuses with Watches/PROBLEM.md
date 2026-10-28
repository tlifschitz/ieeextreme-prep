**CS Academy:** <https://csacademy.com/ieeextreme-practice/task/59d4aae501fe4ced9ffbf3737acd18a2/>

# Octopuses with Watches

**IEEEXtreme 11.0** · Time limit: 1000 ms · Memory limit: 5 MB

IBM puzzlemaster asked, on March 2017 a challenge about [eight octopuses where each one of them has eight watches](https://www.research.ibm.com/haifa/ponderthis/challenges/March2017.html).

Your challenge is to write a program for a generalization of the problem – to find the maximal number of watches that can be adjusted to either $3$, $6$, $9$ or $12$ according to the rules of the game.

Using a sequence of operations of two types:

1. Add an hour to all the watches of a single octopus.
1. Add an hour to a specific watch for all the octopuses.

and given the hour setting of $n \times m$ watches ($m$ watches for each of the $n$ octopuses) compute the maximal number of watches that can be adjusted to either $3$, $6$, $9$ or $12$.

## Standard input

On the first line of the input there will be two integers $n$ and $m$ ($0 < n \leq m < 10$).

On the following $n$ lines there will be $m$ integers in the interval $[1,12]$, each one representing the configuration of one of the watches.

## Standard output

Output a single integer, the maximal number of watches that can be adjusted to either $3$, $6$, $9$ or $12$.

## Constraints and notes

- $0 < n \leq m < 10$

## Examples

### Example 1

Input:
```
8 8
1 2 3 4 5 6 7 8
2 4 6 8 10 12 2 4
3 6 9 12 3 6 9 12
4 8 12 4 8 12 4 8
5 10 3 8 1 6 11 4
6 12 6 12 6 12 6 12
7 2 9 4 11 6 1 8
8 4 12 8 4 12 8 4
```

Output:
```
43
```

### Example 2

Input:
```
3 4
3 1 4 1
5 9 2 6
5 3 5 8
```

Output:
```
10
```
