**CS Academy:** <https://csacademy.com/ieeextreme-practice/task/candy-shop/>

# Candy Shop

**IEEEXtreme 15.0** · Time limit: 3000 ms · Memory limit: 256 MB

Alice came to the candy shop. There are $N$ types of candy in the shop, numbered candy $1$ to candy $N$. Different types of candy are packed in different bag sizes. One bag of candy $i$ contains $B_i$ pieces of candy $i$ $(1 \le i \le N)$. For each candy type $i$, there are $A_i$ bags of candy $i$ available in the shop. Each bag of candy must be purchased as a whole.

Alice wants to buy *exactly* $K$ pieces of candy. She wants to know in how many different ways she can do so. Two ways are different if there exists a type of candy which Alice buys a different amount. Help Alice find the answer modulo $998\,244\,353$.

## Standard input

The first line contains two integers $N$ and $K$.

Each of the next $N$ lines describe the number of bags and the bag size of one type of candy. The $i$th line contains two integers $A_i$ and $B_i$, denoting that there are $A_i$ bags of candy $i$, and each of these bags contains $B_i$ pieces of candy $i$.

## Standard output

Output the number of different ways to buy exactly $K$ pieces of candy, modulo $998\,244\,353$.

## Constraints and notes

- $1 \le N, K \le 10^5$
- $1 \le A_i, B_i \le 10^5$
- For $60\%$ of the test files, $N, K \leq 1000$.

## Examples

### Example 1

Input:
```
3 2
1 2
1 1
2 1
```

Output:
```
3
```

Explanation:

Alice has $3$ options:

- buy one bag of candy $1$
- buy one bag of candy $2$, and one bag of candy $3$
- buy two bags of candy $3$

### Example 2

Input:
```
4 1
3 1
2 2
1 3
4 1
```

Output:
```
2
```

Explanation:

Alice can buy bag of candy $1$, or one bag of candy $4$.

### Example 3

Input:
```
3 5
2 12
4 6
6 7
```

Output:
```
0
```

Explanation:

Answer is $0$ because Alice can't buy exactly $5$ candy.
