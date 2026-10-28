# Rescue Mission

**IEEEXtreme 14.0** · Time limit: 3000 ms · Memory limit: 256 MB

**CS Academy:** <https://csacademy.com/ieeextreme-practice/task/rescue-mission/>

A group of Xtreme soldiers are fighting a tough war but are unfortunately trapped within the enemy territory. But don't worry, they managed to find $N$ hideouts along a long battle line. The hideouts are numbered $1$ to $N$. Initially there are $S_i$ soldiers at hideout $i$.

There is a safe rendezvous location. Each hideout has one path to the rendezvous location. However, since the enemies are heavily patrolling the area, that path between the rendezvous location and hideout $i$ cannot be taken unless the weather around hideout $i$ is foggy.

You are planning a rescue mission to safely evacuate these soldiers in the next $D$ days. You are able to forecast that on day $i$, the hideouts numbered $L_i, L_i+1, ...R_{i}$ will have foggy weather, and will be able to gather at the rendevouz location. You will send a vehicle that can evacuate $V_i$ soldiers. The remaining soldiers must go back to the hideouts. The soldiers do not necessarily need to go back to the hideout where they came from. Instead, they can go to any hideout with a number between $L_i$ and $R_i$. Each hideout may have an arbitrary number of soldiers at any time, including zero.

If you coordinate the movements of the soldiers carefully, what is the maximum total number of soldiers you can evacuate?

## Standard input

There is a single integer $N$ on the first line, the number of hideouts. The second line has $N$ integer. The $i$-th integer is $S_i$.

The next line has a single integer $D$, the number of days. Each of the next $D$ lines has three integers $L_i$, $R_i$, and $V_i$. They indicate that on day $i$ hideouts $L_i, L_i+1, ... R_i$ will have foggy weather, and you will send a vehicle to the rendezvous location that can evacuate $V_i$ soldiers from these hideouts.

## Standard output

Output the maximum total number of soldiers you can evacuate.

## Constraints and notes

- $1 \leq N \leq 10^5$
- $0 \leq S_i \leq 10^4$
- $1 \leq D \leq 5\,000$
- $1 \leq  L_i \leq R_i \leq N$
- $1 \leq V_i \leq 10^9$

- For $30\%$ of the test data, $D \leq 50$ and $N \leq 50$.
- For $60\%$ of the test data, $D \leq 50$.

## Examples

### Example 1

Input:
```
4
5 4 3 2
4
1 2 4
1 1 3
2 4 1
3 3 4
```

Output:
```
12
```

Explanation:

At the beginning, the number of soldiers at the hideouts are $[5, 4, 3, 2]$. On day $1$, there are $9$ soldiers from hideout $1$ and $2$ that can be evacuated. The vehicle takes $4$, and the $3$ of the $5$ remaining soldiers can go to hideout $1$ to wait for the vehicle on day $2$. The other $2$ remaining soldiers go to hideout $2$. The number of soldiers at the hideouts are therefore $[3, 2, 3, 2]$. After day $2$, the numbers become $[0, 2, 3, 2]$. On day $3$, we can evacuate one solder from hideout $2$, and let the other soldier there go to hideout $3$. The numbers of soldiers at the hideouts become $[0, 0, 4, 2]$. On the last day, the $4$ soldiers at hideout $3$ will be evacuated.

### Example 2

Input:
```
3
7 8 7
6
1 2 1
2 3 1
3 3 9
2 3 1
1 2 1
1 1 9
```

Output:
```
22
```

Explanation:

At the beginning, we have $[7, 8, 7]$ soldiers. In the first two days, two soldiers can be evacuated, and at the same time all soldiers can move to hideout $3$, getting $[0, 0, 20]$ by the end of day $2$. On day $3$ we can evacuate $9$ soldiers, getting $[0, 0, 11]$. Then on day $4$ and $5$ two soldiers can be evacuated, and at the same time all soldiers can move to hideout $1$, getting $[9, 0, 0]$. On the last day all the remaining soldiers can be evacuated.
