# Gotta Catch 'Em All

**IEEEXtreme 11.0** · Time limit: 250 ms · Memory limit: 128 MB

**CS Academy:** <https://csacademy.com/ieeextreme-practice/task/e610aba28810ebcf2d3998692269b5a0/>

Pokémon trainer Blue is starting his journey in the world of Pokémon and dreams of becoming a Pokémon master. Blue will be travelling to Viridian city for his first gym battle with his Pokémon Pikachu, but, in order to do so he has to pass through the Viridian forest. Blue's rival, Red is determined to stop Blue from becoming a Pokémon master. Hence, Red has laid traps in the Viridian forest with enemy Pokémon. These Pokémon will prevent Blue from proceeding further into the forest unless his Pikachu battles and defeats them. For each battle, Pikachu loses a portion of its health. Lucky for Blue, there are some unused health potions available in the forest. These potions can restore Pikachu's health. Can Pikachu fight all the enemy Pokémon? Will Blue reach the Viridian city? Or will Red be successful in his attempt to prevent Blue from becoming Pokémon master?

The Viridian forest can be represented as an $r \times c$ ($2 \leq r, c \leq 200$) grid. Blue starts from location $(1,1)$ (which is on the top left part of the map) and needs to exit the Viridian forest from location $(r,c)$ in order to go to Viridian city. At any cell $(i,j)$, Blue can only move down $(i+1,j)$ or right $(i,j+1)$ and he cannot move outside the grid. In any cell $(i,j)$ in the grid, there can either be a health potion or an enemy Pokémon which battles with Pikachu. Potions will be represented using positive integer and will increase Pikachu's health the value in the cell. Enemy Pokémon will be represented using negative integers and will reduce Pikachu's health by the value in the cell. If Pikachu's health drops to $0$ or less, Pikachu will no longer be able to fight and Blue will have to go back to his home. Then Red will be successful in his attempt and Blue will never complete his dream of becoming a Pokémon master.

Blue does not want to lose, but, is unable to plan his journey through the Viridian forest. So, he needs your help to plan the journey for him so that Pikachu trains until he increases his health capacity to the minimum health needed to defeat all the Pokémon in their journey to Viridian city.

## Standard input

On the first line of the input there will be two integers $r$ and $c$ which give the size of the Viridian forest.

On the following $r$ lines there will be a $c$ integers, each one representing the value of each cell in the forest $(i,j)$ starting from position $(1,1)$. Cells containing negative values contain enemy Pokémon and cells with positive values contain potions.

Cells $(1,1)$ and $(r,c)$ are always $0$.

## Standard output

Output a single integer, the minimum health that Pikachu needs for the journey.

## Constraints and notes

- $2 \leq r, c \leq 200$
- The elements of the grid are integers in the interval $[-1\,000, 1\,000]$

## Examples

### Example 1

Input:
```
2 2
0 -2
2 0
```

Output:
```
1
```

Explanation:

Blue can take the path from $(1,1)$ -> $(2,1)$ -> $(2,2)$. Pikachu needs to have health of $1$ since there are no battles to be fought.

### Example 2

Input:
```
3 3
0 1 2
-2 -9 -4
-8 5 0
```

Output:
```
2
```

Explanation:

Blue can take the path from $(1,1)$ -> $(1,2)$ -> $(1,3)$ -> $(2,3)$ -> $(3,3)$. Pikachu needs to have health of $2$ since there is $1$ battle to be fought and there are $2$ potions in the path.
