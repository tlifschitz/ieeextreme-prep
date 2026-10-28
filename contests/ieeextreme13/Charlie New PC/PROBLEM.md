# Charlie New PC

**IEEEXtreme 13.0** · Time limit: 2000 ms · Memory limit: 256 MB

**CS Academy:** <https://csacademy.com/ieeextreme-practice/task/charlie-new-pc/>

Charlie has been given money to build a new PC. He needs your help to select components, using as much of the money as possible, without going over the budget. There are a number of component types to choose from (e.g. RAM, hard drive, processor, etc.), and he must select exactly one of each component type for the computer.

## Standard input

The first line of the input specifies an integer $T$, the number of test cases. Each test case begins with an integer $B$, which represents the maximum amount that Charlie can spend. The next line contains an integer $N$, which represents the number of component types. The next line contains $N$ space separated integers that represent the number of options $K_i$, for each component type $1 \le i \le N$. Each of the next $N$ lines contain the costs for the components. The $i^{th}$ line contains a space separated list of $K_i$ integers indicating the costs of each component option.

## Standard output

For each test case, you should output a single line with the maximum cost of the computer, using exactly one of each component types. The cost needs to be less or equal to the maximum amount available $B$. If there is no configuration that can be constructed for the given budget, the output should be `0`.

## Constraints and notes

- $1 \le T \leq 10$
- $1 \leq B \le 2*10^9$
- $1 \leq N \leq 10$
- $1 \leq K_i \leq 100$
- The sum of all options $K_i \le 100$
- The costs of the components are integers between $1$ and $2*10^9$

## Examples

### Example 1

Input:
```
1
50
4
3 2 1 2
15 10 49
11 17
10
13 23
```

Output:
```
50
```

Explanation:

In the sample input, there is one test case.

This test case has a *b* budget of 50, and there are 4 types of components.

- Three options for component 1, with cost 15, 10, and 49;
- Two options for component 2, with cost 11 and 17;
- One options for component 3, with costs 10;
- Two options for component 4, with cost 13 and 23.

The most expensive computer that Charlie can build will cost 50, choosing the 10 option for component 1, the 17 option for component 2, the 10 option for component 3, and the 13 option for component 4.
