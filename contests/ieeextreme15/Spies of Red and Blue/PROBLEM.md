# Spies of Red and Blue

**IEEEXtreme 15.0** · Time limit: 2000 ms · Memory limit: 256 MB

**CS Academy:** <https://csacademy.com/ieeextreme-practice/task/spies/>

Red and Blue are two countries currently engaged in a battle for world dominance in an era of the cold war. Since information is key in winning this war, both countries have invested time, money, and effort in developing spy agencies and have spies across the world to provide them with information in order to act as quickly as possible.

In order to retain secrecy, the spy agencies are structured such that a spy will only report to their immediate senior. Any information received by a spy will be passed to their immediate senior till it reaches the head of the spy agency with $R_1$ and $B_1$ being the head of spy agencies of Red and Blue. Spies may be turned over to the other side and the compromised spies will get a new immediate senior to whom he/she will report information.

<Graph indexType="custom" height="260" width="500" nodes={[{options:{fixed:true},label:"B1",center:{x:247.1,y:26.2}},{options:{fixed:true},label:"B2",center:{x:226.2,y:92.3}},{options:{fixed:true},label:"B3",center:{x:279.5,y:92.2}},{options:{fixed:true},label:"R1",center:{x:147.8,y:24.2}},{options:{fixed:true},label:"R2",center:{x:148,y:92}},{options:{fixed:true},label:"R3",center:{x:150.9,y:162}},{options:{fixed:true},label:"R4",center:{x:151.9,y:232}}]} edges={[{source:1,target:0,directed:1},{source:2,target:0,directed:1},{source:6,target:5,directed:1},{source:5,target:4,directed:1},{source:4,target:3,directed:1}]} />

In the above spy reporting structure, Red has $4$ spies and Blue has $3$ spies with $R_1$ and $B_1$ being the head of their respective countries. It will take $3$ interactions for information to reach $R_1$ from $R_4$, and it will take $1$ interaction for information to reach $B_1$ from $B_2$. If $B_2$ had turned over to the red country with $R_3$ as his immediate senior, then, the information from $B_2$ will never reach $B_1$, and it will reach $R_1$ via $R_3$ with $3$ interactions instead (as shown below).

<Graph indexType="custom" height="260" width="500" nodes={[{options:{fixed:true},label:"B1",center:{x:247.1,y:26.2}},{options:{fixed:true},label:"B2",center:{x:226.2,y:92.3}},{options:{fixed:true},label:"B3",center:{x:279.5,y:92.2}},{options:{fixed:true},label:"R1",center:{x:147.8,y:24.2}},{options:{fixed:true},label:"R2",center:{x:148,y:92}},{options:{fixed:true},label:"R3",center:{x:150.9,y:162}},{options:{fixed:true},label:"R4",center:{x:151.9,y:232}}]} edges={[{source:1,target:5,directed:1},{source:2,target:0,directed:1},{source:6,target:5,directed:1},{source:5,target:4,directed:1},{source:4,target:3,directed:1}]} />

Given the spies' organizational structure of Red and Blue countries and the sequence of events as to which spy receives the information or is turned over, find which country will win the information war by getting information faster and how many interactions will it take to pass the information to its head of spy agency.

## Standard input

The first line has a single integer $T$, the number of test cases.

For each test case, the first line consists of three integers $N_R$, $N_B$, and $E$, where $N_R$ is the number of spies in the Red country, $N_B$ is the number of spies in the Blue country, and $E$ is the number of events that will occur. The spies in the Red countries are named $R_1, R_2, \dots R_{N_R}$, and the spies in the Blue countries are named $B_1, B_2, \dots B_{N_B}$.

The second line has $N_R-1$ space separated strings. The $i$th of these strings is the name of the immediate senior of spy $R_{i+1}$.

The third line has $N_B-1$ space separated strings. The $i$th of these strings is the name of the immediate senior of spy $B_{i+1}$.

The next $E$ lines each describe an event. An event is one of the two types:

- `c` $x$ $y$: There is a spy crossover. Spy $x$ now reports to spy $y$ as his/her immediate senior.
- `w` $x$ $y$: There is a piece of battle information received by spy $x$ and spy $y$ at the same time.

Note that due to the crossovers, $x$ $y$ can be originally spies of a same country. A same crossover may happen multiple times.

## Standard output

For each battle information event `w` , output the winner country of the information war, along with $k$, the minimum number of interactions required for the piece of information to reach its head of spy agency. There can be four possible output scenarios:

- `RED` $k$: The information reaches $R_1$ first, in $k$ interactions.
- `BLUE` $k$:  The information reaches $B_1$ first, in $k$ interactions.
- `TIE` $k$: The information reaches $R_1$ and $B_1$ at the same time, in $k$ interactions.
- `NONE`: The information reaches neither $R_1$ nor $B_1$.

Note that $k$ does not need to be printed for the `NONE` scenario.

## Constraints and notes:

- $1 \leq T \leq 30$
- $2 \leq N_R, N_B \leq 1\,000$
- $1 \leq E \leq 1\,000$
- Initially before all the events, the spy reporting structure guarantees that information received by any Red country spy can reach $R_1$, and information received by any Blue country spy can reach $B_1$.
- In a crossover event, spy $x$ is not $R_1$ and not $B_1$.
- In each event, $x, y$ are both valid spy names from either country. $x \neq y$.

## Examples

### Example 1

Input:
```
1
4 4 6
R1 R2 R3
B1 B1 B2
w R2 B2
w R4 B3
c B2 R3
w R4 B2
c R3 B4
w R4 B2
```

Output:
```
TIE 1
BLUE 1
RED 3
NONE
```

Explanation:

#### Output 1:

- Path for Red: $R_2 \rightarrow R_1$: The number of interactions is $1$.
- Path for Blue: $B_2 \rightarrow B_1$: The number of interactions is $1$.

#### Output 2:

- Path for Red: $R_4 \rightarrow R_3 \rightarrow R_2 \rightarrow R_1$: Number of interaction is $3$.
- Path for Blue: $B_3 \rightarrow B_1$: Number of interaction is $1$.

#### Output 3:

- Path for Red: $R_4 \rightarrow R_3 \rightarrow R_2 \rightarrow R_1$: Number of interaction is $3$.
- Path for Blue: No possible path for Blue.

#### Output 4:

- There exists a cycle $R_4\rightarrow R_3\rightarrow B_4\rightarrow B_2\rightarrow R_3\rightarrow B_4$, so that the information will never reach $R_1$ or $B_1$.
