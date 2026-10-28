# PIEEEXMan

**IEEEXtreme 12.0** · Time limit: 1000 ms · Memory limit: 256 MB

**CS Academy:** <https://csacademy.com/ieeextreme-practice/task/pieeexman/>

Everyone knows about the classic arcade game Pac-Man. This year, you're about to be playing in a special variation of it, called the PIEEEXMan. In this variation PIEEEXMan, our hero, munches his way around the maze collecting cherries, while Bob the Bear, our anti-hero, can't eat our hero, like the monsters in the original game, so instead he is looking to steal as many cherries as he can.

The maze is a $0$-based $(2N + 1) \times (2M + 1)$ matrix of characters $A$. The cells are represented by the pairs $(i, j)$ where $i$ and $j$ are odd integers. Moving throughout the cells can be done in the $4$ directions: upward, downward, leftward and rightward; however it may be restricted by a wall. The character of the matrix directly in the direction you are facing encodes this information. For example, if $A_{i - 1, j}$ contains a wall, then you cannot go from $(i, j)$ to $(i - 2, j)$ (which is the cell located immediately upward).

You are playing in the role of PIEEXMan, while the judge is playing Bob. You start first.

## Interaction

The judge will print two integers $N$ and $M$, followed by a $A$, which is encoded as follows:

<Table columns={[ {headerName: "Character", fieldName: "character"}, {headerName: "Encoding", fieldName: "encoding"}, {headerName: "Where", fieldName: "where"}]} rows={[

 {character: "`1`", encoding: "PIEEXMan's initial position", where: "only one, located in a cell"},

 {character: "`2`", encoding: "Bob the Bear's initial position", where: "only one, located in cell"},

 {character: "`#`", encoding: "Wall", where: "not in a cell"},

 {character: "`.`", encoding: "Empty", where: "anywhere"},

 {character: "`@`", encoding: "Cherry", where: "located in a cell"},

]} />

The moves you can make are as follows:

<Table columns={[ {headerName: "Character", fieldName: "character"}, {headerName: "Encoding", fieldName: "encoding"}]} rows={[

 {character: "`U`", encoding: "Move upward"},

 {character: "`D`", encoding: "Move downward"},

 {character: "`L`", encoding: "Move leftward"},

 {character: "`R`", encoding: "Move rightward"},

 {character: "`W`", encoding: "Wait"},

]} />

The judge makes the same type of moves. The game ends when the judge will print a move followed by the `X` character. In this case, you must end the interactions to get a proper verdict.

## Download materials & maps

For this challenge there are $6$ maps and numerous *judges* whith whom you will compete to collect the cherries. There are $6$ examples, each of them coresponding to one map and one *judge*. Not all *judges* are used in the examples.

You can download the [maps in txt and bmp format](https://publicmedia1.csacademy.com/public/1539999192-2276335312.zip). The $\text{txt}$ is the same as the one received in the interaction. The $\text{image}$ is just a nice graphic representation of the map to help you better visualize it.

## Scoring

Let $A$ be the number of cherries you have collected, $B$ be the number of cherries the judge has collected and $C$ be the total number of cherries in the maze, then you score will be $5 \cdot (1 + \frac{A - B - 1}{C + 1})$.

## Constraints and notes

- This task is *NOT* <Definition term="adaptive task" value="adaptive"/>
- $1 \leq N, M \leq 30$
- A cherry may not be collected twice

## Simulation

#### To see a simulation of a game follow the steps below

- Select a map that you would like to see a simulation for
- Open the *moves* link for the selected map
- Enter *all* the moves into the `moves` input box which is located below the simulation panel
- Open the *state* link for the selected map (the state is the same as the one that can be downloaded in the materials section)
- Enter the map description into the `state` input box which is located below the simulation panel
- Click the orange `Reload` button
- To see the simulation click the `play` button

#### Hints

- You can speed up the simulation replay (maximum of $16 \times$)
- You can enter your own simulation into the `moves` input box. Just beware that it *must* contain both your moves and the judges moves.
- You can use the simulation to see a replay of your code on the examples. To do this, click the `Run Examples` button. Expand an example by clicking the `>`character in the `examples panel`. Carefully select the `interaction` and paste it into the $2$ `input boxes`
- Beware that the `interaction` might look like the following (see below). You must split it accordingly before pressing the `Reload` button.
```
3 3
#######
#.#.#2#
#####.#
#..@..#
#.#####
#1#.#.#
#######UWRWX
```

<Table columns={[

	{headerName: "Map Number", fieldName: "number"},

	{headerName: "Example of Moves", fieldName: "moves"},

	{headerName: "Map state", fieldName: "state"}

	]} rows={[

	{

		number: "0",

		moves: "[]()",

		state: "[]()",

	},

	{

		number: "1",

		moves: "[]()",

		state: "[]()",

	},

	{

		number: "2",

		moves: "[]()",

		state: "[]()",

	},

	{

		number: "3",

		moves: "[]()",

		state: "[]()",

	},

	{

		number: "4",

		moves: "[]()",

		state: "[]()",

	},

	{

		number: "5",

		moves: "[]()",

		state: "[]()",

	},

]} />

<MazeProblemWidget />

## Examples

### Example 1

Input:
```
0
3 3
#######
#.#.#2#
#####.#
#..@..#
#.#####
#1#.#.#
#######
```

Output:
```

```

Explanation:

You may notice that the interaction ended abruptly because the judge printed a move, followed by `W` at the end.


### Example 2

Input:
```
2
7 7
###############
#@#@#.......#2#
#.#.#####.###.#
#.#.#.#.#.#...#
#.#.#.#.#.#.###
#@.......@.@#.#
#######.#.#.#.#
#.......#.#...#
#.#.#.#.#.#####
#.#.#@#.#....@#
#####.#.###.#.#
#.....#...#.#.#
#.###.###.#.###
#1#.#@#@..#@.@#
###############
```

Output:
```

```

### Example 3

Input:
```
1
11 11
#######################
#.........#..........2#
#.#######.#.#.#########
#.#@.@.@#.#.#........@#
#.#####.#.#.#.#####.#.#
#......@#.#.#.#@#...#.#
#########.#.#.#.#.###.#
#.......#.#.#.#.#@#@..#
#.#.#.#.#.#.#.#.#######
#.#@#@#@#.#.#......@.@#
#.#######.#.###########
#@.........@.........@#
###########.#.#######.#
#@.@......#.#.#@#@#@#.#
#######.#.#.#.#.#.#.#.#
#..@#@#.#.#.#.#.......#
#.###.#.#.#.#.#########
#.#...#@#.#.#.#@......#
#.#.#####.#.#.#.#####.#
#@........#.#.#@.@.@#.#
#########.#.#.#######.#
#1..........#.........#
#######################
```

Output:
```

```

### Example 4

Input:
```
3
23 23
###############################################
#1.@.@.@....#@.@.@.@.@......#...........#.....#
#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.###.#.#.#.#.#
#......@.....@.........@.@.@.@.@.@.....@.@.@.@#
###.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.###.#
#...#..@....#@..#...........#.#..@.....@....#.#
#####.#.#.#.#.###.#.###.#####.###.#.#.#.#.#.#.#
#@.@.@.@....#@.@.@.@....#.....#..@..#..@......#
#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#
#@..#..............@.......@.@.@.@.....@.@.@.@#
#.#.#.#######.#.#.#.#.#.#.#.#.#.#.#.###.#.#.#.#
#@....#.#.....#....@..#.#..@.................@#
#.#.#.#.###.#.#.#.#.#.###.#.#####.###.###.###.#
#@..#..@.@.@.@....#@....#..@......#.#...#....@#
#.#.#.#.#.#.#.#.#.#.#.#.###.#.###.#.#.#.###.#.#
#@....#@.....@.....@.......@#....@.@.@.@.....@#
#.###.#.#.#.#.#.###.#######.#.###.#.#.#.#####.#
#@.....@....#@.....@.......@..#..@.....@#.#..@#
#.#.###.#.#.#.#####.#.###.#.#.###.###.#.#.#.#.#
#@.@.@.@.....@.@.@.@..#....@#....@..#..@#....@#
#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.###.#.#.#.#
#.............#............@.@.@.@..#..@.@.@.@#
#.#.#.#.#.#.#.###.###.#.#.#.#.#.#.###.#.###.###
#.....#.#.....#...#.........#...#.....#.#.....#
###.###.#.###.#.#.#.#.#.#.###.###.#.#.#.#.#.#.#
#@.@.@.@..#..@.@.@.@............#.............#
#.#.#.#.###.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#
#@....#@..#..@....#@....#..@.@.@.@.....@.@.@.@#
#.#.#.#.#.###.###.#.#.###.#.#####.#.#.#.###.#.#
#@..#.#@.....@..#..@.......@.....@#....@.....@#
#.#####.#.#.#.###.#.#######.###.#.#.#.#.#.###.#
#@.....@.@.@.@....#@.......@.....@.....@#....@#
#.#.###.#.#.#.###.#.###.#.#.#.#.#.#.#.#.#.#.#.#
#@....#...#.#......@..#....@#....@.@.@.@..#..@#
#.###.###.###.#####.#.###.#.#.#.#.#.###.#.#.#.#
#@.................@..#.#..@....#.....#.#....@#
#.#.#.#.###.#.#.#.#.#.#.#.#.#.#.#.#######.#.#.#
#@.@.@.@.....@.@.@.@.......@..............#..@#
#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#
#......@..#..@..#.....#....@.@.@.@#....@.@.@.@#
#.#.#.#.#.#.#.###.#####.###.#.###.#.#.#.#.#####
#.#....@.....@..#.#...........#..@#....@..#...#
#.###.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.###
#@.@.@.@.....@.@.@.@.@.@.........@.....@......#
#.#.#.#.#.###.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#
#.....#...........#......@.@.@.@.@#....@.@.@.2#
###############################################
```

Output:
```

```

### Example 5

Input:
```
3
21 21
###########################################
#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#
###########################################
#.#.#......@........#.#..............@#.#.#
#####.#####.#######.###.#######.#####.#####
#.#.#@#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#@#.#.#
#####.#####.#######.###.#######.#####.#####
#.#.#..........................@......#.#.#
#####.#####.###.###########.###.#####.#####
#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#
#####.#####.###.###########.###.#####.#####
#.#.#@......#.#....@#.#.....#.#.......#.#.#
###########.#######.###.#######.###########
#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#
###########.#######.###.#######.###########
#.#.#.#.#.#.#.#......@......#.#.#.#.#.#.#.#
###########.###.#####.#####.###.###########
#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#
###########.###.#####.#####.###.###########
#.#@........#.#.#.#@.@.@#.#.#.#@.......@#.#
###########.###.###########.###.###########
#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#
###########.###.###########.###.###########
#.#.#.#.#.#.#.#......@......#.#.#.#.#.#.#.#
###########.###.###########.###.###########
#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#
###########.###.###########.###.###########
#.#.#......@.......@#.#@.........@....#.#.#
#####.#####.#######.###.#######.#####.#####
#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#
#####.#####.#######.###.#######.#####.#####
#.#.#@..#.#................@....#.#..@#.#.#
#######.###.###.###########.###.###.#######
#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#
#######.###.###.###########.###.###.#######
#.#.#.......#.#@....#.#.....#.#......@#.#.#
#####.#############.###.#############.#####
#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#
#####.#############.###.#############.#####
#.#.#1.................@.............2#.#.#
###########################################
#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#
###########################################
```

Output:
```

```

### Example 6

Input:
```
3
19 19
#######################################
#1..#.........#@....#@..#@...........@#
#.#.#.#######.#####.###.#.###########.#
#..@..#@.........@#@...........@.....@#
#####.###.#######.#.###.#.#####.#######
#..@#...#.#@......#.#@#.#....@#.......#
#.###.###.###.#####.#.#.#####.#######.#
#.....#....@..#...........#....@.....@#
###.#####.###.#####.#########.#.#######
#..@........#.............#@..#.#@....#
#.###.###################.###.#.###.#.#
#.#@..........#@.......@..#@..#.#@#@#.#
#.#########.#.#.###.#.#.#.#.#.#.#.###.#
#....@....#.#.#.#@..#@#.#.#.#.#@......#
#########.#.#.#.###.###.#.#.#.#######.#
#..@#.....#.#@....#..@#.....#.......#.#
#.#########.#.#############.#######.#.#
#@.........@#........@#....@.......@#@#
###########.###########.###############
#2..........#..........@#.....#@......#
#.#.#.#######.#####.#.#####.#.###.###.#
#.#.#......@#...#@..#.....#@#...#..@#.#
#.#.#######.###.#####.###.#####.###.#.#
#.#............@#@....#@..#@....#..@#.#
#.#.#######.#########.###.#####.#.###.#
#.#.#..@..#............@#.#....@#..@#@#
#.#.#.###.###############.#.#######.#.#
#.#@.....@#.............#.#........@#@#
#.#####.#.#.###########.#.#.#########.#
#@#.....#.#.#..@#.....#.#.#...........#
#.#.###.#.#.#.###.###.#.#.#.###########
#.#.#@..#.#.#.....#@.@#.#..@.........@#
#.#.###.#.#.#.#########.#############.#
#.#..@#.#.#.#..@.......@......#......@#
#.#####.#.#.#################.#.#######
#.#@.@..#..@#........@.@#.....#@......#
#.#########.#.###########.###########.#
#@..........#............@............#
#######################################
```

Output:
```

```
