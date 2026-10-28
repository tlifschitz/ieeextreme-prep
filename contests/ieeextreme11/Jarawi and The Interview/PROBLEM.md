**CS Academy:** <https://csacademy.com/ieeextreme-practice/task/6f960361da7beb7f3a083f4776c2cf79/>

# Jarawi and The Interview

**IEEEXtreme 11.0** · Time limit: 2000 ms · Memory limit: 256 MB

Today Jarawi had a job interview for a very important tech company, the interviewer asked him to solve the next problem:

Given a string <Latex value="s"/> <Latex value="(1 \leq |s| \leq 10^6)"/>, answer <Latex value="q"/> <Latex value="(1 \leq q \leq 5 * 10^4)"/> queries. For each query he received a string <Latex value="p_i"/> <Latex value="(1 \le |p_i| \le 100)"/> and he had to determine the size of the longest suffix of <Latex value="p_i"/> which is a <Definition term="subsequence"/> of <Latex value="s"/> (a suffix of a string is a <Definition term="substring"/> that occurs at the end).

Unfortunately Jarawi could not solve the task, so he wants to know if you can solve it.

## Standard input

The first line contains a string $s$.

The second line contains an integer $q$.

Each of the next $q$ lines contains a string $p_i$.

## Standard output

For each query you need to print the size of the longest suffix of $p_i$ which is a subsequence of $s$.

## Constraints and notes

- $1 \leq |s| \leq 10^6$
- $1 \leq q \leq 5 * 10^4$
- $1 \le |p_i| \le 100$
- All strings contain only lower case letters of the English alphabet.

## Examples

### Example 1

Input:
```
xaybaba
2
aaba
yx
```

Output:
```
4
1
```

Explanation:

The first query is "aaba" which has the next suffixes {"a","ba","aba","aaba"}, all of them are subsequence of "xaybaba", so the longest has size 4.

The second query is "yx" which has the next suffixes {"x", "yx"}, only "x" is subsequence of "xaybaba" and it has size 1.
