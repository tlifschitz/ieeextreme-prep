# Merchant Association

**IEEEXtreme 13.0** · Time limit: 3000 ms · Memory limit: 512 MB

**CS Academy:** <https://csacademy.com/ieeextreme-practice/task/merchant-association/>

As the leader of the Xtreme Merchant Association you are trying to expand its already lucrative trading business. There are $n$ towns in the state, numbered $1$ to $n$. The towns are connected by $n - 1$ bidirectional roads. All towns buy and sell the same type of goodies. Town $i$ buys and sells one goodie for a price of $p_i$ dollars.

Within the association, there are $k$ merchants located at $k$ different starting towns. Each merchant may choose a destination town and travel to it from his/her starting town. The merchant must visit each town on the chosen path exactly once and cannot go back. To avoid competition inside the Xtreme Association, no two merchants' travel paths can include the same town (in particular, one merchant cannot visit another merchant's starting town). A merchant may buy exactly one goodie at any town on the travel path, and sell that goodie at the destination town for a profit. Each merchant may only buy and sell once, but may choose not to travel and stay at the starting town if no profit can be made.

The goal of the association is for all the merchants together to make the largest possible profit. Look at the goodie prices closely and instruct the merchants about where their destinations should be and how they should buy and sell. What is the optimal total profit the merchants can make?

## Standard input

The input has one integer $n$ on the first line representing the number of towns.

The second line has $n$ integers describing the prices at each town. The $i$th integer is $p_i$.

Each of the next $n - 1$ lines has two integers $x, y$ describing one bidirectional road connecting town $x$ to town $y$.

Lastly there is a line with an integer $k$, the number of merchants. This is followed by a line with $k$ distinct integers giving the starting towns of each merchant.

## Standard output

Output a single integer, the largest total profit the merchants can make.

## Constraints and notes

- $1 \leq n \leq 2 \times 10^5$
- $1 \leq p_i \leq 10^9$
- $1 \leq k \leq n$
- It is guaranteed that all towns are connected by roads.

## Examples

### Example 1

Input:
```
12
3 1 2 3 5 6 7 2 2 4 10 11
1 2
1 3
4 2
5 2
3 6
6 7
6 8
6 9
8 10
9 11
9 12
5
3 8 4 11 12
```

Output:
```
12
```

Explanation:

- The merchant starting at town $4$ travels to town $5$, buying at town $2$ for $1$ dollar and selling at town $5$ for $5$ dollars (earning $4$ dollars).
- The merchant starting at town $3$ travels to town $1$, buying at town $3$ for $2$ dollars and selling at town $1$ for $3$ dollars (earning $1$ dollar).
- The merchant starting at town $8$ travels to town $10$, buying at town $8$ for $2$ dollars and selling at town $10$ for $4$ dollars (earning $2$ dollars).
- The merchant starting at town $11$ travels to town $7$, buying at town $9$ for $2$ dollars and selling at town $7$ for $7$ dollars (earning $5$ dollars).
- The merchant starting at town $12$ does not travel.
