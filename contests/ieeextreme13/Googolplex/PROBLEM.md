**CS Academy:** <https://csacademy.com/ieeextreme-practice/task/googolplex/>

# Googolplex

**IEEEXtreme 13.0** · Time limit: 300 ms · Memory limit: 256 MB

The Alpha universe is much larger than our current universe and the distance between different planets is in the order of a few googolplex meters. A googolplex is a large number equal to $10^{10^{100}}$. In decimal notation, it is written as the digit $1$ followed by $10^{100}$ zeros. Light travels at a speed of $3 \times 10^8$ meters per second. Hence, even light would take a really long time to travel one googolplex meters! Humans in the Alpha universe have the technology to travel at the speed of light, but since the distance between planets is still very large. The time to travel between different planets is more than the life span of normal humans, making it impossible to travel between planets directly.

Fortunately, in the Alpha universe there are some wormholes which shorten the distances by acting as tunnels connecting Earth to different planets. To travel from Earth to a distant planet which is $X$ googolplex meters away, you would need to take the wormhole $Y$ to shorten the distance. In this universe, the time $t$, in seconds, spent in the wormhole is given by the formula $t = (X^{\text{googolplex}+T})$ mod $10^Y$ where $T$ is the time of the day (the time in seconds after 12:00 UTC).

For example, if a planet is $5$ googolplex meters away and is using wormhole $2$, then the time spent in wormhole is given by $t = (5^{\text{googolplex}+T})$ mod $10^2$  seconds at the time of day $T$. Output the minimum time spent in the wormhole by determining the optimal time of day $T$.

For example, at time of the day $T=10$, the time spent in the wormhole is ($5^{googolplex+10}$) mod $10^2$. $T$ can vary from $0$ to $86399$.

## Standard input

The first line contains an integer $N$, the number of test cases.

Each of the next $N$ lines contains two integers $X$ and $Y$.

## Standard output

Output a single integer for each test case denoting the minimum time spent in the wormhole.

## Constraints and notes

- $1 \leq N \leq 20$
- $1 \leq X \leq 10^8$
- $1 \leq Y \leq 9$
- $0 \leq T \leq 86399$

## Examples

### Example 1

Input:
```
1
2 4
```

Output:
```
16
```

Explanation:

There is 1 test case. The distant planet is 2 googolplex meters away and the wormhole used to travel is 4. Hence, the distance is ($2^{googolplex+T}$) mod $10^4$. The minimum time is 16 seconds when time of day $T = 4$ .

### Example 2

Input:
```
3
5 1
100 3
3 5
```

Output:
```
5
0
1
```

Explanation:

There are 3 test cases. The expected outputs are `5`, `0`, and `1`.
