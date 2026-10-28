# Poker Tournament

**IEEEXtreme 16.0** · Time limit: 5000 ms · Memory limit: 512 MB

**CS Academy:** <https://csacademy.com/ieeextreme-practice/task/poker-tournament/>

There are $N$ towns numbered from $0$ to $N-1$. Each town has a poker club, where the $i$-th one has $A_i$ members. Members of different clubs are distinguishable, but members of the same club are not. For all poker tournaments, if the $i$-th club decides to participate, it has to send at least $1$ and no more than $A_i$ members. If a club doesn't participate, we assume that it has sent $0$ of it's members.

Your task is to process $q$ events of three types:

Type 0: Given $L_i, R_i, C_i$ change the value of $A_j$ to $C_i$ for every $j$ satisfying $L_i \leq j \leq R_i$,

Type 1: Given $L_i, R_i, C_i$ change the value of $A_j$ to $max(A_j, C_i)$ for every j satisfying $L_i \leq j \leq R_i$,

Type 2: Given $L_i, R_i, K_i$, a tournament is taking place where only clubs numbered from $L_i$ to $R_i$ can participate and **exactly** $K_i$ clubs participate. Count the number of different sets of players that could appear in the tournament modulo $998244353$. Two sets of players are considered different if there exists a club that has sent a different number of players in those sets.

## Standard input

The first line of input contains two integers $N$ and $Q$. The next line contains $N$ numbers $A_i$. The next $Q$ lines describe consecutive events. Description of the $i$-th event starts with a number $T_i$ denoting the type of the $i-th$ event. If $T_i = 0$ or $T_i=1$, three numbers $L_i$, $R_i$, $C_i$ follow. Otherwise three numbers $L_i$, $R_i$, $K_i$ follow.

## Standard output

The $i$-th line of output should contain the answer to the $i$-th Type 2 event $-$ number of different sets of players that could play in the $i$-th tournament.

## Constraints and notes

- $1 \leq N, Q \leq 5\cdot10^4$,
- $0 \leq A_i < 998244353$ for $i$ from $0$ to $N-1$,
- $0 \leq T_i \leq 2$ for $i$ from $0$ to $Q-1$,
- $0 \leq L_i \leq R_i < N$ for $i$ from $0$ to $Q-1$,
- $0 \leq C_i < 998244353$ for $i$ from $0$ to $Q-1$,
- $1 \leq K_i \leq 50$ for $i$ from $0$ to $Q-1$

## Examples

### Example 1

Input:
```
10 9
1 2 3 4 5 6 7 8 9 10
0 4 9 3
1 7 7 5
2 2 8 1
0 4 9 4
1 3 6 5
2 0 9 3
0 3 9 10
1 3 7 8
2 3 6 2
```

Output:
```
24
6310
600
```
