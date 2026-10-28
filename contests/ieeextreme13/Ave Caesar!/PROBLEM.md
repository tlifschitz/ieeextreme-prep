# Ave Caesar!

**IEEEXtreme 13.0** · Time limit: 1000 ms · Memory limit: 256 MB

**CS Academy:** <https://csacademy.com/ieeextreme-practice/task/ave-caesar/>

Tired of making ciphers and brutalizing triangles, Caesar decided to impress Tiranca the unicornosaurus with something else, his obsession with algebraic closures! Skeptic of his skill, Tiranca gives him the following problem:

A /valid string/ is either:

1. A string consisting of a single character
1. The concatenation of $2$ /valid strings/ $A$ and $B$,  if $A \le B$ lexicographically.

Given $N$ strings, decide which are /valid strings/.

## Standard input

- The first line contains an integer $N$, the number of given strings.
- The following $N$ lines contain a string in each line.

## Standard output

The output should contain a single line with $N$ characters, the $i$-th being `1` if the $i^{th}$ string from the input is valid, `0` if not.

## Constraints and notes

- The total length of the strings will be smaller than $10^6$
- All strings contain only uppercase characters

## Examples

### Example 1

Input:
```
5
BBBABB
AABAAB
AABAA
BBABAB
ABBBBA
```

Output:
```
01000
```
