# Bearcity Renting

**IEEEXtreme 13.0** · Time limit: 1000 ms · Memory limit: 256 MB

**CS Academy:** <https://csacademy.com/ieeextreme-practice/task/bearcity-renting/>

Vangelis the Bear and its friend Charlie want to open their own store in Bearcity. They need to decide which place they will rent to start their store. Since they will constantly need to buy supplies to the store, they want to find a place near a warehouse.

Bearcity used to be a small town, so all the streets are only one way and there is always a heavy traffic jam. The new mayor, Lisa the bear, seeing that the city is expanding, wants to turn some one-way streets into two-way streets. Some conversion cost is associated with each street. Lisa wants to make some conversions in a way that the total cost of conversion is minimized, keeping in mind that all warehouse points should be connected by two-way roads.

Vangelis and Charlie, after coming to know about this idea, decided to rent a place on a two-way street, so clients can come and go easily from the store. As there can be more than one conversion plan, help Vangelis and Charlie decide how many streets are part of all possible conversion plans.

## Standard input

The first line of the input contains two positive integers. The first one indicates the number $N$ of warehouses considered in the conversion plan and the second one the number $M$ of streets. The next $M$ lines are triplets indicating, for each street, its endpoints $u$ and $v$, followed by its conversion cost.

## Standard output

Output a single value representing the number of streets that are part of all possible conversion plans.

## Constraints and notes

- $1 \leq N \leq 10^5$
- $1 \leq M \leq 2*10^5$
- The cost of conversion $c_s$ for each street $s$: $1 \leq c_s \leq 10^4$
- There is at most one road connecting two warehouses
- It is guaranteed at least one conversion plan exists

## Examples

### Example 1

Input:
```
3 3
1 2 2
3 1 2
2 3 1
```

Output:
```
1
```

Explanation:

<Graph indexType="custom" height="200" width="200" forcePaused={true}

nodes={[

  {label:"1",center:{x:100,y:30}},

  {label:"2",center:{x:30,y:150}},

  {label:"3",center:{x:170,y:150}}

]}

edges={[

  {label:"2",source:0,target:1},

  {label:"2",source:2,target:0},

  {label:"1",source:1,target:2}]

} />

There are 2 possible minimum cost conversion plans: $(1, 3), (2, 3)$ or $(1, 2), (2, 3)$. Only the street $(2, 3)$ occurs in both of them.

### Example 2

Input:
```
6 9
1 2 2
1 3 1
1 6 2
2 4 2
2 5 2
4 3 2
3 5 2
4 5 4
5 6 4
```

Output:
```
2
```

Explanation:

<Graph indexType="custom" height="300" width="300" forcePaused={true}

nodes={[

  {label:"1",center:{x:270,y:30}},

  {label:"2",center:{x:30,y:30}},

  {label:"3",center:{x:270,y:270}},

  {label:"4",center:{x:30,y:270}},

  {label:"5",center:{x:100,y:190}},

  {label:"6",center:{x:190,y:130}}

]}

edges={[

  {label:"2",source:0,target:1},

  {label:"1",source:0,target:2},

  {label:"2",source:0,target:5},

  {label:"2",source:1,target:3},

  {label:"2",source:1,target:4},

  {label:"2",source:3,target:2},

  {label:"2",source:2,target:4},

  {label:"4",source:3,target:4},

  {label:"4",source:4,target:5},

  {label:"2",source:5,target:5}

]} />

Only the roads $(1, 3)$ and $(1, 6)$ are part of all possible conversion plans.
