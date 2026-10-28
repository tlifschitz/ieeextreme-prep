# Bridge Construction

**IEEEXtreme 15.0** · Time limit: 5000 ms · Memory limit: 512 MB

**CS Academy:** <https://csacademy.com/ieeextreme-practice/task/bridge/>

There are two islands. There are $N_1$ villages on the first island connected by $N_1 - 1$ bidirectional roads. There are $N_2$ villages on the second island connected by $N_2 - 1$ bidirectional roads. It is possible to travel between any pair of two villages on a same island via the roads. It takes exactly one unit of time to travel through any single road on either island.

The villagers plan to build a bidirectional bridge between the two islands that connects one village from one island to another village from the other island. It will take exactly one unit of time to travel through the bridge. After the bridge is built, it will be possible to travel between any pair of the $N_1 + N_2$ villages. The villagers would like to build the bridge so that the maximum travel time between any pair of villages is minimized. Where should they build the bridge?

## Standard input

The first line of the input has a single integer $T$, the number of test cases.

Each test case first describes the roads on the first island. It starts with a single integer $N_1$ on the single line. The villages on the first island are numbered from $1$ to $N_1$. The next following $N_1 - 1$ lines describe the roads on the first island. Each line has two integers $a$ and $b$, meaning that there is a bidirectional road connecting village $a$ and village $b$ on the first island. Roads on the second island are then described in a same format, starting with $N_2$ on a single line, followed by $N_2 - 1$ lines each with a pair of villages on the second island.

## Standard output

For each test case output two lines. The first line contains the smallest maximum travel time between any pair of villages after the bridge is built. The second line has two space-separated integers $x, y$ ($1 \leq x \leq N_1, 1 \leq y \leq N_2$), indicating that the bridge should be built between village $x$ on the first island and village $y$ on the second island. If there exist multiple ways to build the bridge, you can output any $x, y$ that yields a smallest maximum travel time.

## Constraints and notes

- $1 \leq T \leq 10$
- $2 \leq N_1, N_2 \leq 10^5$
- For $60\%$ of the test files, $N_1, N_2 \leq 50$.

## Examples

### Example 1

Input:
```
3
8
1 2
2 3
3 4
4 5
2 6
3 7
4 8
4
1 2
1 3
1 4
7
1 2
2 3
3 4
5 6
6 3
3 7
4
1 2
2 3
3 4
2
1 2
2
2 1
```

Output:
```
4
3 1
5
3 3
3
2 2
```

Explanation:

There are $3$ test cases.

- Case $1$: The two islands and their roads are shown below. One optimal way to build the bridge (shown in blue) is to connect village $3$ from the first island to village $1$ of the second island.

<Graph indexType="custom" height="400" width="400" nodes={[{label:1,center:{x:148.4,y:253.6}},{label:2,center:{x:182.1,y:219.6}},{label:3,center:{x:217.7,y:189.7}},{label:4,center:{x:176.5,y:169}},{label:5,center:{x:227.3,y:148.1}},{label:"8",center:{x:187.9,y:122.1}},{label:"6",center:{x:138.2,y:199.5}},{label:"7",center:{x:264.6,y:183.8}},{label:"1 ",center:{x:228.2,y:230.2}},{label:"2 ",center:{x:276.1,y:231.9}},{label:"3 ",center:{x:196.2,y:267}},{label:"4 ",center:{x:246.3,y:273.9}}]} edges={[{source:0,target:1},{source:1,target:2},{source:2,target:3},{source:3,target:4},{source:1,target:6},{source:2,target:7},{source:3,target:5},{source:8,target:9},{source:8,target:10},{source:8,target:11},{source:2,target:8,color:"blue"}]} />

- Case $2$: The two islands and the bridge are shown similarly as in Case $1$.

<Graph indexType="custom" height="400" width="400" nodes={[{label:1,center:{x:264.2,y:248.6}},{label:2,center:{x:265.1,y:199.1}},{label:3,center:{x:222.5,y:225.8}},{label:4,center:{x:222.4,y:275}},{label:"1 ",center:{x:259,y:149.4}},{label:"2 ",center:{x:221.9,y:178.9}},{label:"3 ",center:{x:180.7,y:202}},{label:"4 ",center:{x:184.6,y:151.3}},{label:"6 ",center:{x:180.5,y:251.5}},{label:"5 ",center:{x:139,y:224.6}},{label:"7 ",center:{x:141.2,y:174.4}}]} edges={[{source:0,target:1},{source:4,target:5},{source:5,target:6},{source:6,target:7},{source:9,target:8},{source:8,target:6},{source:6,target:10},{source:2,target:6,color:"blue"},{source:1,target:2},{source:2,target:3}]} />

- Case $3$: Connecting any pair of villages can yield the smallest maximum travel time of $3$, so answers other than `2 2` may also be accepted.
