# King's Order

**IEEEXtreme 18.0** · Time limit: 500 ms · Memory limit: 256 MB

**CS Academy:** <https://csacademy.com/ieeextreme-practice/task/kings-order/>

In the kingdom of Lexiconia, King Algorithmus gave his loyal knights a monumental task: to complete a series of important projects. These projects were divided into different groups, each identified by its group ID. The projects had to be completed in a particular order, as some depended on others being finished first. To add to the challenge, the King decreed that the the final project order must follow the kingdom's ancient rules of order:

- If there are multiple projects with no pending dependencies to execute, choose the one with lowest group ID.
- If there are multiple projects with no pending dependencies to execute and with the lowest group ID, choose the one with lowest project ID.

Each knight had a project to oversee, and the projects belonged to specific groups. However, there were dependencies between the projects that could not be ignored. The knights needed to figure out a valid order to complete all the projects, making sure they followed the dependencies and arranged them following the kingdom's order.

As they gathered in the Great Hall, the knights realized the complexity of the task. Could they find the right sequence to complete all the projects, or would the kingdom fall into disarray due to an unresolvable cycle of dependencies? Now, it's up to you, the royal advisor, to determine if there is a valid project order that respects all dependencies, or if the kingdom’s projects are trapped in a cycle that makes completion impossible.

Can you guide the knights and ensure the proper order of projects, or will Lexiconia be lost to chaos?

## Standard input

The first line contains two integers $N$ and $M$, representing the number of projects and the number of dependencies, respectively.

The second line contains $N$ integers representing the group IDs of each project, where the $i$-th integer represents the group ID of project $i$.

The next $M$ lines each contain two integers $A$ and $B$, indicating that project $A$ must be completed before project $B$.

## Standard output

Output a single line containing a valid project order such that all dependencies are satisfied, and the sequence is lexicographically minimal according to the kingdom's order. If there is no valid order (i.e., the dependency graph has a cycle), output `-1`.

## Constraints and notes

- $1 \leq N \leq 1000$
- $0 \leq M \leq 10000$
- The group IDs will be integers between $1$ and $10^9$
- $1 \leq A \not = B \leq N$ for every dependency.

## Examples

### Example 1

Input:
```
4 4
2 1 1 3
1 2
2 3
3 4
1 3
```

Output:
```
1 2 3 4
```

Explanation:

<Graph indexType="custom" directed="true" height="200" width="300"

nodes={[

{options:{fixed:true},label:"1",center:{x:50.6,y:160}},

{options:{fixed:true},label:"2",center:{x:100,y:50}},

{options:{fixed:true},label:"3",center:{x:160,y:145}},

{options:{fixed:true},label:"4",center:{x:253.8,y:40}}

]} edges={[{source:0,target:1},{source:1,target:2},{source:2,target:3},{source:0,target:2}]}

/>

It's easy to see that the only possible way to order the projects is $1, 2, 3, 4$.

### Example 2

Input:
```
3 2
1 2 1
1 2
2 1
```

Output:
```
-1
```

Explanation:

Since there is a dependency from project $1$ to project $2$ in both ways, there is no valid way to order the projects.

### Example 3

Input:
```
5 4
10 7 7 1 4
5 1
4 5
2 5
3 4
```

Output:
```
2 3 4 5 1
```

Explanation:

The dependencies between the projects look as follows:

<Graph indexType="custom" directed="true" height="200" width="300" nodes={[

{options:{fixed:true}, label:"1",center:{x:205,y:166}},

{options:{fixed:true}, label:"2",center:{x:40,y:40}},

{options:{fixed:true}, label:"3",center:{x:260,y:65}},

{options:{fixed:true}, label:"4",center:{x:160,y:55}},

{options:{fixed:true}, label:"5",center:{x:100,y:130}}]} edges={[{source:2,target:3},{source:4,target:0},{source:3,target:4},{source:1,target:4}]} />

Initially, it's possible to choose projects $2$ and $3$, since both projects have the same group ID, the one with lowest project ID must be chosen, so project $2$ is selected to be the first one in the final order.

Then, we only have one way to choose the remaining projects, which is $3, 4, 5, 1$.

Finally, we have the order $2, 3, 4, 5, 1$.
