# Bus Company

**IEEEXtreme 15.0** · Time limit: 6000 ms · Memory limit: 256 MB

**CS Academy:** <https://csacademy.com/ieeextreme-practice/task/buscompany/>

Lima is known by its tree-shaped road networks. Thus, there are $N$ cities numbered from $1$ to $N$ and there are exactly $N - 1$ bidirectional roads that connect them and there exists a path between any pair of cities. There are two bus companies, A and B, that are being frequently compared by the Ministry of Transportation. Each city has exactly one bus stop, which is owned by one of the two companies.

The Ministry of Transportation may try to compare the two companies, and identify a winner company following these steps:

- Choose two cities $u$ and $v$ and consider the simple path $(u, v)$ between them. A simple path is a path that doesn't visit the same city twice.
- For each company, compute the average length of all the simple paths that start in a city $a$ and end in a city $b$ such that both bus stops at $a$ and $b$ are owned by this company and the path $(a, b)$ contains path $(u, v)$. That is, all cities in the path from $u$ to $v$ are contained in the path from $a$ to $b$. If there are no such paths, the value is considered $\infty$.
- Declare that the company that has a smaller average length is the winner company.

Additionally, a company can buy the bus stop at some city $u$, in which case the ownership of the bus stop at city $u$ changes.

You will receive $Q$ events that happen in order, which can be one of the two types:

- Transaction Event: The bus stop in city $u$ was bought by the other company (if it was owned by company A, now belongs to company B, and vice versa).
- Comparison Event: Two cities $u$ and $v$ are chosen to compare the two companies. Check which company wins or if there is a tie.

## Standard input

The first line contains a single integer $N$, indicating the total number of cities.

The second line contains $N$ integers $0$ or $1$, indicating whether city $i$ initially belongs to company A or B, respectively.

The next $N-1$ lines each contain $2$ integers $a$ and $b$, indicating there is a bidirectional road between city $a$ and city $b$.

Line $N+2$ contains an integer $Q$, the number of events. The following $Q$ lines contain the events. Each event is either $1 ~u$ (transaction event), or $2 ~u ~v$ (comparison event).

## Standard Output

For each comparison event print `A` if company A wins, `B` if company B wins,  or `TIE` if there is a tie between both companies.

## Constraints and notes

- $N \geq 2$
- $N, Q \leq 2 \cdot 10^5$
- In all events, $1 \leq u, v \leq N, u \neq v$.
- The road network forms a tree.
- There is at least one comparison event.

- For $5\%$ of the test files, $N, Q \leq 10^3$.
- For $10\%$ of the test files, $N, Q \leq 10^4$.
- For $30\%$ of the test files, $N, Q \leq 10^5$.

## Examples

### Example 1

Input:
```
8
1 0 0 0 0 1 0 0
1 3
5 8
6 2
1 5
5 4
2 7
5 2
6
2 2 6
2 8 7
1 8
1 1
2 8 7
2 2 5
```

Output:
```
B
A
TIE
A
```

Explanation:

The road network and the initial ownerships of the bus stops are illustrated below.

<Graph indexType="custom" height="400" width="400" nodes={[{label:"1/B",center:{x:237.5,y:149.6}},{label:"6/B",center:{x:145.7,y:187.4}},{label:"3/A",center:{x:190.6,y:167}},{label:"5/A",center:{x:229.6,y:197.4}},{label:"8/A",center:{x:267.9,y:227.2}},{label:"2/A",center:{x:184.9,y:215.8}},{label:"4/A",center:{x:222.8,y:247.1}},{label:"7/A",center:{x:176.2,y:263.5}}]} edges={[{source:0,target:2},{source:3,target:4},{source:1,target:5},{source:0,target:3},{source:3,target:6},{source:5,target:7},{source:3,target:5}]} />

There are $6$ events.

- Event $1$: Compare companies given $u=2, v=6$.

Company A: Bus stops owned by company A are at cities $\{2,3,4,5,7,8\}$. There are $15$ simple paths between two of these cities. None of them contains path $(2, 6)$. So the average path length for company A is $\infty$.

Company B: Bus stops owned by company B are at cities $\{1,6\}$.  There is a single simple path between these two cities that contains the path $(2, 6)$. Average path length for company B is thus the length of this path, which is $3$.

Therefore company B wins.

- Event $2$: Compare companies given $u=8, v=7$.

Company A: Among the $15$ simple paths, only $(7, 8)$ contains $(u, v)$. A's average path length is $3$.

Company B: The only path $(1, 6)$ does not contain $(u, v)$. B's average path length is $\infty$.

Therefore company A wins.

- Event $3$: The bus stop at city $8$ was bought by the opposite company (its ownership switched from A to B).
- Event $4$: The bus stop at city $1$ was bought by the opposite company (its ownership switched from B to A).

After these two events, the ownerships of the bus stops are below:

<Graph indexType="custom" height="400" width="400" nodes={[{label:"1/A",center:{x:237.5,y:149.6}},{label:"6/B",center:{x:145.7,y:187.4}},{label:"3/A",center:{x:190.6,y:167}},{label:"5/A",center:{x:229.6,y:197.4}},{label:"8/B",center:{x:267.9,y:227.2}},{label:"2/A",center:{x:184.9,y:215.8}},{label:"4/A",center:{x:222.8,y:247.1}},{label:"7/A",center:{x:176.2,y:263.5}}]} edges={[{source:0,target:2},{source:3,target:4},{source:1,target:5},{source:0,target:3},{source:3,target:6},{source:5,target:7},{source:3,target:5}]} />

- Event $5$: Compare companies given $u=8, v=7$.

Company A: Bus stops owned by company A are at cities $\{1, 2, 3, 4, 5, 7\}$. There are $15$ simple paths between two of these cities. None of these paths contains $(u, v)$. A's average path length is $\infty$.

Company B: Bus stops owned by company B are at cities $\{6, 8\}$.  There is a single simple path between these two cities. It does not contains $(u, v)$. B's average path length is $\infty$.

Both companies have an average path length of $\infty$. Therefore it is a tie.

- Event $6$: Compare companies given $u =2, v = 5$.

Company A: There are $8$ simple paths that contains $(u, v)$ that start and end at two cities with a bus stop owned by A: $(1, 2), (1, 7), (2, 3), (2, 4), (2, 5), (3, 7), (4, 7), (5, 7)$. The lengths of these paths are $2, 3, 3, 2, 1, 4, 3, 2$. Their average is $2.5$.

Company B: The path $(6, 8)$ contains $(u, v)$. Its length is $3$, which is also the average path length of B.

Therefore company A has a smaller average path length and is the winner.
