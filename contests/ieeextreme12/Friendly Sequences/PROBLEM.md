# Friendly Sequences

**IEEEXtreme 12.0** · Time limit: 1000 ms · Memory limit: 256 MB

**CS Academy:** <https://csacademy.com/ieeextreme-practice/task/friendly-sequences/>

Semar and Petruk are best friends and they love playing with integer sequences. Semar has a sequence that contains $N$ integers, represented by $\{B_1, B_2, \ldots, B_N\}$. Semar asks Petruk to count how many integer sequences $\{A_1, A_2, \ldots, A_N\}$ have the following properties:

- $0 \leq A_1 \leq \ldots \leq A_n$
- $A_1 \leq B_1$
- $A_1 + A_2 \leq B_2$
- $A_1 + A_2 + A_3 \leq B_3$
- $\ldots$
- $A_1 + \ldots + A_N \leq B_N$

Your task is to help Petruk find the answer.

## Standard input

The first line of the input contains integer $N$.

The second line of the input contains $N$ integers representing the $\{B_1, B_2, \ldots, B_N\}$ sequence, each integer is separated by one space.

## Standard output

Print one integer representing the number of sequences with the given property.

As this number can be very large, output its value modulo $10^9+7$.

## Constraints and notes

- $1 \leq N \leq 10^5$
- $0 \leq B_i \leq 2\ 000$

## Examples

### Example 1

Input:
```
2
1 2
```

Output:
```
4
```

Explanation:

There are $4$ possible sequences: {0, 0}, {0, 1}, {0, 2}, and {1, 1}.

### Example 2

Input:
```
4
13 51 30 73
```

Output:
```
39564
```
