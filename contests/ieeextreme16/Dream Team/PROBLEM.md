**CS Academy:** <https://csacademy.com/ieeextreme-practice/task/dream-team/>

# Dream Team

**IEEEXtreme 16.0** · Time limit: 1000 ms · Memory limit: 500 MB

Alice is the general manager for a basketball team with an unusual requirement.  Her goal is to assemble a five-player team that is as strong as possible without exceeding the budget on the total salary.

She has determined the fair value for the available players at each position - point guard, shooting guard, small forward, power forward, and center.  Because these are the fair values, the strength of the team can be measured by the sum of all players' salaries.  A stronger team will have a larger total salary.

She would like your help in determining the best players to choose.

## Standard input

Each input has a single test case.

The first line of input contains a single integer $B$, which gives Alice's budget.

The second line contains an integer $P$, which gives the number of point guards available.  The next $P$ lines contain one of these player's names, followed by a space, and then an integer $W_i$, representing the player's salary.

The next line contains an integer $G$, which gives the number of shooting guards available.  The next $G$ lines contain one of these player's names, followed by a space, and then an integer $W_i$, representing the player's salary.

The next line contains an integer $S$, which gives the number of small forwards available.  The next $S$ lines contain one of these player's names, followed by a space, and then an integer $W_i$, representing the player's salary.

The next line contains an integer $F$, which gives the number of power forwards available.  The next $F$ lines contain one of these player's names, followed by a space, and then an integer $W_i$, representing the player's salary.

The next line contains an integer $C$, which gives the number of centers available.  The next $C$ lines contain one of these player's names, followed by a space, and then an integer $W_i$, representing the player's salary.

## Standard output

For each input, create output five lines with the team with the highest total salary that is less than or equal to $B$.  The lines should contain a single name of a player in the following order:  point guard, shooting guard, small forward, power forward, and center.

In the case of a tie, you should output just one team - the team whose names, in the order of output, come first in alphabetical order.  Consider the following examples:

- Suppose that two teams had the same largest salary that met the constraint.  The list of players, in the problem's specified order, for the first team is "smyth evans franks kim chen" (with new lines between the player names).  The list of players for the second team, in the specified order, is "smyth wang agarwal andersen melnyk".  In this case, we would output the first team since it comes first in alphabetical order (the "e" in "evans" comes before "w" in "wang").
- Suppose that two tied teams had players "smythe evans franks kim chen" and "smyth wang agarwal andersen melnyk".  In this case, we would output the second team since the newline character after "smyth" comes before the "e" in "smythe", in alphabetical order.

## Constraints and notes

- $1 \leq B \leq 10^9$
- $1 \leq W_i \leq 10^9$
- $1 \leq P \leq 500$
- $1 \leq G \leq 400$
- $1 \leq S \leq 100$
- $1 \leq F \leq 50$
- $1 \leq C \leq 40$

Each player's name will be a unique string made up of only lowercase letters, up to 10 characters long.  No player will appear in the input more than once.

You are guaranteed that there will be at least one team whose total salary meets the budget constraint.

## Examples

### Example 1

Input:
```
235000
3
curry 40000
nash 20000
johnson 10000
3
jordan 50000
wade 20000
bryant 80000
1
james 30000
1
duncan 60000
1
oneal 100000
```

Output:
```
nash
wade
james
duncan
oneal
```

Explanation:

In the testcase, the budget is $235,000$.

There are 3 point guards, 3 shooting guards, and 1 of each of the remaining positions.

The best team that can be made, without exceeding the budget, contains the following players:

- nash, with a salary of 20,000
- wade, with a salary of 20,000
- james, with a salary of 30,000
- duncan, with a salary of 60,000
- oneal, with a salary of 100,000

The total of the salaries is 230,000, which is less than or equal to the budget.
