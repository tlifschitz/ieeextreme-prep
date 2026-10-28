# Xtreme Rappers

**IEEEXtreme 13.0** · Time limit: 100 ms · Memory limit: 256 MB

**CS Academy:** <https://csacademy.com/ieeextreme-practice/task/xtreme-rappers/>

Rapper CrissyChris and her friend, JaCe, will participate in Gold Level, one of the most important events of freestyle in the world. They are training improvising 3-word phrases, where each one has to contribute at least one word.

They want to improvise the maximum number of phrases without repeating words (a word can be used only in one phrase), CrissyChris and JaCe select an assortment of words from Ctoke’s database (Ctoke is one of the oldest rappers in freestyle and his database contains only unique words). CrissyChris and JaCe both selects $K$ and $J$ words from the database respectively. CrissyChris and JaCe never have words in common.

CrissyChris is an actual legend within IEEE and has supported the IEEEXtreme competition for the past 13 years in one way or another; whether it was all those late nights throughout the competitions or purchasing and shipping all of the top 100 prizes!  She has recently moved on within IEEE to another department.  This challenge is a tribute to her and all she has done to enrich the competition through the years!  Farewell Christine Eldridge, you will be missed!

## Standard input

One line with two integers $K$ and $J$, representing the number of words available for each rapper.

## Standard output

Print the maximum number of 3-word phrases they can improvise together.

# Constraints and notes

- $0 \leq K, J \leq 10^{10}$

## Examples

### Example 1

Input:
```
4 3
```

Output:
```
2
```

Explanation:

With the sample input, we can form at most two 3-word phrases. One phrase can have 2 words from JaCe and 1 word from CrissyChris and the other phrase can have 2 words from CrissyChris and 1 from JaCe.

### Example 2

Input:
```
0 10000000000
```

Output:
```
0
```

Explanation:

Without words for CrissyChris no phrases can be created.
