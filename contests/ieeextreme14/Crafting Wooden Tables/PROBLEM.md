# Crafting Wooden Tables

**IEEEXtreme 14.0** · Time limit: 1000 ms · Memory limit: 256 MB

**CS Academy:** <https://csacademy.com/ieeextreme-practice/task/crafting-wooden-tables/>

A lot of people are stuck at home due to the unfortunate pandemic this year. They thus resort to building their wonderful home on a deserted island. Rolan is such an deserted islander.

To live a fruitful life on a deserted island, Rolan needs to craft a lot of furniture. One of Rolan's favorite, is the /wooden table/. Crafting a wooden table requires $C$ pieces of wood, which is a resource obtainable by chopping trees on the island. Rolan has a pocket of limited size that can hold the wood and the crafted wooden tables. Her pocket has $N$ slots, and each slot can hold either a single wooden table, or a pile of wood with at most $P$ pieces of wood.

Rolan has $W$ pieces of wood at the beginning and can distribute them into the $N$ pocket slots arbitrarily. To craft a wooden table, Rolan takes $C$ pieces of wood from any of the pocket slots, removing them from those slots. If any pile of wood becomes empty, the pocket slot becomes free. If there is no free slot in Rolan's pocket, the crafting stops. Otherwise, the crafted wooden table will be placed in a free pocket slot. Rolan repeats the crafting until no more wooden tables can be crafted.

How many wooden tables will Rolan eventually have?

## Standard input

The input has four integers $C, N, P, W$ on a single line.

## Standard output

Output a single integer, the number of wooden tables that Rolan can craft.

## Constraints and notes

- $1 \leq C, N, P, W \leq 10^{15}$
- $W \leq N \cdot P$
- For $60\%$ of the test data, $C, N, P, W \leq 10^6$

## Examples

### Example 1

Input:
```
4 3 3 8
```

Output:
```
2
```

Explanation:

Rolan distributes the wood into the pocket as $[3, 3, 2]$. Each integer denotes the number of wood pieces in a pile. Let $T$ denote a wooden table. The first crafted table will be placed as $[3, 1, T]$. Then a second table can be crafted and placed as $[T, 0, T]$.

### Example 2

Input:
```
2 3 3 8
```

Output:
```
1
```

Explanation:

Initial pocket is $[3, 3, 2]$. Crafting a wooden table consumes $2$ pieces of wood. Only one table can be crafted and the pocket is $[3, 3, T]$.

### Example 3

Input:
```
10 3 3 8
```

Output:
```
0
```

Explanation:

Crafting a wooden table requires $10$ pieces of wood. But Rolan does not have that many pieces of wood.
