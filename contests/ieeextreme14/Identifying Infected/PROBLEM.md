# Identifying Infected

**IEEEXtreme 14.0** · Time limit: 2000 ms · Memory limit: 256 MB

**CS Academy:** <https://csacademy.com/ieeextreme-practice/task/identifying-infected/>

Bad-virus is a highly contagious virus that can seriously complicate people’s health. This virus is only spread from person to person and the only way to prevent infection (not $100\%$ safe) is by wearing masks.

Chief of epidemiology has received the first case of bad-virus in your country, this case is imported from the other country. In this context, in coordination with the president, it was decided to close the country's borders, prohibit encounters of more than two persons and make the use of masks mandatory. But in order not to affect the economy, no type of quarantine will be carried out.

Two days later, Chief of epidemiology has been notified about the second case of bad-virus (now necessarily is a national case). Knowing that there are $N$ persons in the country (including the imported case) enumerated by an integer from 1 to $N$, they ask you to identify all people who necessarily are infected. For this task, the department of epidemiology provides you with a list of the $M$ encounters of two persons during this time. You will be given $Q$ scenarios that you should handle separately. In the $i$-th scenario, you will be given the IDs of the first and the second case of bad-virus, and you should count how many people that can be $100\%$ identified as infected (including the first and the second case).

## Standard input

The first line contains two integers $N$ and $M$, denoting the number of persons and number of encounters respectively.

Each one of the next $M$ lines contains two different integers $A_i$ and $B_i$, denoting the two persons in the encounter (there aren't two equal pairs of integers).

The next line contains an integer $Q$, denoting the number of scenarios.

Each one of the next $Q$ lines contains two different integers $F_i$ and $S_i$, denoting the first and second case of bad-virus in the $i$-th scenario.

## Standard output

For each scenario, output the number of people that can be $100\%$ identified as infected on a single line.

## Constraints and notes

- $2 \leq N \leq 10^{5}$
- $1 \leq M, Q \leq 2 \times 10^{5}$
- $1 \leq A_i \lt B_i \leq N$ for all $1 \leq i \leq M$
- $A_i \ne A_j$ or $B_i \ne B_j$ for all $1 \leq i < j \leq M$
- $1 \leq F_i, S_i \leq N$ and $F_i \ne S_i$ for all $1 \leq i \leq Q$
- For each scenario, it is guaranteed that there is at least a sequence of encounters so that the second case is originally infected from the first case.

- For $30\%$ of the test data, $N \leq 100$ and $M, Q \leq 200$.
- For $60\%$ of the test data, $N \leq 1\,000$ and $M, Q \leq 2\,000$.

## Examples

### Example 1

Input:
```
6 5
1 2
1 3
2 4
3 4
4 5
2
1 5
4 3
```

Output:
```
3
2
```

Explanation:

Below is the illustration of the encounters.

<Graph indexType="custom" height="400" width="400" nodes={[{label:1,center:{x:83.2,y:204.2}},{label:2,center:{x:159.8,y:340.4}},{label:3,center:{x:167,y:70.8}},{label:4,center:{x:231.7,y:205.5}},{label:5,center:{x:379.9,y:186.3}},{label:"6",center:{x:314.4,y:328.9}}]} edges={[{source:2,target:3},{source:0,target:1},{source:0,target:2},{source:1,target:3},{source:3,target:4}]} />

In the first scenario, there are only two ways such that the fifth person can be infected by the first person, i.e. $1 \rightarrow 2 \rightarrow 4 \rightarrow 5$ and $1 \rightarrow 3 \rightarrow 4 \rightarrow 5$. We cannot identify which one of the second and the third person that is actually infected. So, the people that can be $100\%$ identified as infected are $1$, $4$, and $5$.

In the second scenario, the people that can be $100\%$ identified as infected are $3$ and $4$.
