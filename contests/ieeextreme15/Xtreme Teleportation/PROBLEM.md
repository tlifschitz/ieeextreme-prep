# Xtreme Teleportation

**IEEEXtreme 15.0** · Time limit: 6000 ms · Memory limit: 256 MB

**CS Academy:** <https://csacademy.com/ieeextreme-practice/task/teleportation/>

Teleport-X is a company that provides a teleportation system in $N$ cities. This company has built $N-1$ tunnels connecting $N$ cities so that all cities are connected. Those tunnels have some radiations that can be used as energy for the teleportation. The $i$-th tunnel is connecting city $U[i]$ and city $V[i]$ directly with radiation $R[i]$ (The value of $R[i]$ can be positive or negative).

To use the teleportation system, the passengers need a teleportation device. This device has a required radiation limit $L$. This means that this device can be used to teleport from city $A$ to city $B$ if and only if the sum of radiations for all tunnels in the simple path from $A$ to $B$ is not less than $L$. Simple path is a path so that each tunnel can only be traversed at most once in that path. If the sum of radiations is less than $L$, then the device will not work.

For example, if the simple path from $A$ to $B$ is using tunnels $t[1], t[2], ..., t[k]$, then the teleportation device with required radiation limit $L$ can be used to teleport from $A$ to $B$ if and only if $total\_radiation(A, B) = R[t[1]] + R[t[2]] + ... + R[t[k]] \ge L$. Please note that after one teleportation, the radiation level on the device will be reset to $0$ again, because the radiation happens instantaneously. So, even if the passengers do some consecutive teleportations, then the total radiation for each teleportation will not be influenced by other teleportations.

You will be given $Q$ queries. For each query, you will be given city $X[j]$ and city $Y[j]$, and you should determine the maximum $L$ so that it is still possible to use a teleportation device with required radiation limit $L$ to go from city $X[j]$ to city $Y[j]$ by teleporting one or more times (you can visit any other cities multiple times before arriving at city $Y[j]$).

## Standard input

The first line of the input contains two integers $N$ and $Q$ representing the number of cities and the number of queries respectively.

The next $N-1$ lines describe the tunnels. Each line contains three integers separated by single spaces, $U[i]$, $V[i]$, and $R[i]$ indicating that the $i$-th tunnel connects city $U[i]$ and city $V[i]$ and has radiation $R[i]$.

The next $Q$ lines describe the queries. Each line contains two integers separated by single spaces, $X[j]$ and $Y[j]$, indicating that you should determine the maximum $L$ so that it is still possible to use a teleportation device with required radiation limit $L$ to go from city $X[j]$ to city $Y[j]$ by teleporting one or more times (you can visit any other cities multiple times before arriving at city $Y[j]$).

## Standard output

The output should contain $Q$ lines. The $j$-th line contains an integer that is the answer to the $j$-th query.

## Constraints and notes

- $2 \leq N \leq 100\,000$
- $1 \leq U[i], V[i] \leq N$
- $U[i] \neq V[i]$
- $-10^9 \leq R[i] \leq 10^9$
- $1 \leq Q \leq 200\,000$
- $1 \leq X[j], Y[j] \leq N$
- $X[j] \neq Y[j]$

- For $25\%$ of the test data, $N, Q \leq 100$.
- For $50\%$ of the test data, $N, Q \leq 1\,000$.

## Examples

### Example 1

Input:
```
6 5
1 2 1
2 3 2
3 4 -1
4 5 -4
4 6 3
1 3
2 6
6 3
4 5
3 2
```

Output:
```
3
4
3
-1
3
```

Explanation:

Below is the illustration of the tunnels.

<Graph indexType="custom" height="400" width="400" nodes={[{label:1,center:{x:153.9,y:363.8}},{label:2,center:{x:82.5,y:207.9}},{label:3,center:{x:187.1,y:71.9}},{label:4,center:{x:247.8,y:228.5}},{label:5,center:{x:356.2,y:103.7}},{label:6,center:{x:325.7,y:374.2}}]} edges={[{label:"1",source:0,target:1},{label:"2",source:1,target:2},{label:"-1",source:2,target:3},{label:"-4",source:3,target:4},{label:"3",source:3,target:5}]} />

- In the first query, we can teleport from city $1$ to city $3$ directly with $total\_radiation(1, 3) = 3$. So, we can use a device with $L = 3$. There is no way we can reach city $3$ from city $1$ if $L > 3$.
- In the second query, the maximum $L$ is $4$. We can also teleport from city $2$ to city $6$ directly with $total\_radiation(2, 6) = 4$.
- In the third query, the maximum $L$ is $3$. First, We can teleport from city $6$ to city $1$ with $total\_radiation(6, 1) = 5$. And then, we can teleport from city $1$ to city $3$ with $total\_radiation(1, 3) = 3$.
- In the fourth query, the maximum $L$ is $-1$. First, We can teleport from city $4$ to city $6$ with $total\_radiation(4, 6) = 3$. And then, we can teleport from city $6$ to city $5$ with $total\_radiation(6, 5) = -1$.
- In the fifth query, the maximum $L$ is $3$. First, we can teleport from city $3$ to city $1$ with $total\_radiation(3, 1) = 3$. And then, we can teleport from city $1$ to city $6$ with $total\_radiation(1, 6) = 5$. And finally, we can teleport from city $6$ to city $2$ with $total\_radiation(6, 2) = 4$.
