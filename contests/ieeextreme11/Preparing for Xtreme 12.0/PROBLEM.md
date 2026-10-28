# Preparing for Xtreme 12.0

**IEEEXtreme 11.0** · Time limit: 1000 ms · Memory limit: 128 MB

**CS Academy:** <https://csacademy.com/ieeextreme-practice/task/72a7d67e7e18f4f7d033f7f5a5a09bef/>

This is Alice’s first programming contest.  Since she has had such a great time, she has decided to prepare for Xtreme 12.0 in a methodical way.  She asked her teammate, who has competed in previous Xtreme contests, for a list of up to $20$ of the most important topics to study.  With this list in hand, she borrowed a large number of books from the library, which collectively contain all of these topics.  She is determined to read each of the books, cover to cover, but she does not have enough time to read them all.

Please help her plan for next year, by finding the minimum amount of time she will need to read a subset of these books, so that all of the important topics are covered.

## Standard input

The input contains <Latex value="b"/> <Latex value="(1 \leq b \leq 100)"/> lines which describe each book. These lines have the following form:

- <Latex value="[\text{time}]\ [\text{topic}_1]\ [\text{topic}_2]\ ...\ [\text{topic}_n]"/>

Where

- <Latex value="[\text{time}]"/> is the time, in minutes, required to read the book. This will be a non-negative integer less than $10^6$.
- <Latex value="[\text{topic}_i]"/> is the $i^{th}$ topic covered in the book.

## Standard output

On standard output, print on a line by itself, the minimum time, in minutes, required for Alice to read books that cover all of the topics listed.

## Constraints and notes

- $1 \leq b \leq 100$
- Each book will have up to $20$ topics.
- The time requried to read a book is a non-negative integer less than $10^6$
- There will be at most $20$ total topics
- Each topic will be comprised of a string containing letters, numbers, and the underscore (but no whitespace).
- Each of the topics on the list will be covered by at least one book.

## Examples

### Example 1

Input:
```
300 Backtracking Dynamic_Programming Greedy
125 Dynamic_Programming
35 Backtracking
85 Greedy
120 Backtracking Dynamic_Programming
80 Greedy Backtracking
```

Output:
```
200
```

Explanation:

If Alice reads the last two books, she will cover all three of the topics in only 200 minutes.  There is no way for her to cover these topics more quickly.
