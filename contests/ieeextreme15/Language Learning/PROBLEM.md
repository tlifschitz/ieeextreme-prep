# Language Learning

**IEEEXtreme 15.0** · Time limit: 2000 ms · Memory limit: 256 MB

**CS Academy:** <https://csacademy.com/ieeextreme-practice/task/language-learning/>

Abhishek is a student who loves to learn new languages. He does this by making different sentences from a word list given by his friend Zhang Yu. More specifically, he makes a sentence by picking a subsequence of words (not necessarily consecutive) from the word list without changing their order.

Today Zhang gives Abhishek a list of $N$ words for him to learn a special language. The words in the list contain only lowercase letters `a` to `z`. Abhishek will learn this special language in a special way based on an integer $K$: He cannot choose any pair of words $(w_1, w_2)$ in a sentence if their indices differ by at most $K$. In other words, if $w_1$ is at index of $i$ and $w_2$ is at index $j$ in the word list, then they must satisfy $|i - j| > K$ to be chosen together.

To understand how efficiently he is learning this special language, Abhishek asks you to print the number of unique sentences he can make from the word list, modulo $1\,000\,000\,007$ ($10^9 + 7$).

## Standard input

The first line contains a single integer $T$, the number of test cases.

Each test case has two integers $N$ and $K$ separated by space on the first line. The next $N$ lines each have a string that consists of lowercase English letters, describing one word in the list.

## Standard Output

For each test case, output the number of unique sentences modulo $1\,000\,000\,007$ ($10^9 + 7$) on a single line.

## Constraints and notes

- $1 \leq T \leq 1000$
- $1 \leq N \leq 10^{5}$
- $0 \leq K < N$
- The length of any word is between $1$ to $10$.
- The sum of $N$ over all test cases in one test file does not exceed $2 \cdot 10^{6}$.

## Examples

### Example 1

Input:
```
1
7 1
a
abc
abc
a
dac
a
a
```

Output:
```
16
```

Explanation:

There is a single test case. The following $16$ sentences are valid:

```
a
a a
a abc
a dac
a a a
a abc dac
a abc a
a dac a
a abc dac a
abc
abc a
abc dac
abc a a 
abc dac a
dac
dac a
```

Each of these sentences can be formed by picking a subsequence of words without violating the constraint regarding $K$. For example, this sentence `a abc dac a` can be formed by picking words at indices $\{0, 2, 4, 6\}$ respectively. All pairs of indices differ by more than $K=1$.
