# Poker Game

**IEEEXtreme 14.0** · Time limit: 1000 ms · Memory limit: 256 MB

**CS Academy:** <https://csacademy.com/ieeextreme-practice/task/poker-game/>

Tommy is playing a special Poker game with a standard deck of $52$ cards (Jokers excluded). There are four cards of each number: `2`, `3`, ..., `9`, `X`, `J`, `Q`, `K`, `A` (`X` stands for $10$). The suits of cards do not matter in this game, and cards of a same number are completely equivalent. Most winning hands in the original Poker game, such as flush and full house, are not available.

Tommy is dealt $K$ cards as his /initial hand/. Then $N$ community cards are dealt one by one. At any time, Tommy's /hand/ is Tommy's initial hand cards combined with the community cards. Tommy scores points if his hand meets the following categories:

- Pair: Two cards of a same number give $1$ point.
- Three of a kind: Three cards of a same number give $20$ points.
- Four of a kind: Four cards of a same number give $1\,760$ points.

For each unique card number, Tommy receives the highest points among these three. Tommy's final points are the sum of points he receives for each unique card number. For example, if Tommy's hand has a pair of `2`s,  a pair of `8`s, three `A`s, and four `K`, he scores $1 + 1 + 20 + 1\,760 = 1782$ points.

Tommy is not good at this Poker so he plays with a fixed simple strategy: Once a community card is dealt, if his points increase, he will raise the bet. Otherwise, he checks. No raise is allowed before the first community card is dealt.

You are watching Tommy playing this game, and you saw whether Tommy raised after each community card is revealed. You cannot help but wonder, what initial hand can Tommy possibly have?

## Standard input

The input begins with two integers $N$ and $K$ on the first line.

The next line has a string of length $N$ describing the community cards dealt in order.

The third line has a string of length $N$ describing Tommy's actions after each community card. The $i$-th character is `y` if Tommy raised after the $i$-th community card, or `n` otherwise.

## Standard output

Output a single line with the initial hand Tommy may have. Output the cards in the hand in sorted lexicographical order. If there are multiple possible hands, output the hand that gives the highest score. If there are still multiple hands, output the hand that is lexicographically the smallest.

The lexicographical order is defined over card numbers: `2` < `3` < ... < `9` < `X` < `J` < `Q` < `K` < `A`. For example, a hand with two `7`s, one `3`, one `A` and one `X` should be printed as `377XA`. The hand `377XA` is lexicographically smaller than `377KA`.

If Tommy's actions contradict with his assumed strategy, output a single word `impossible`.

## Constraints and notes

- $2 \leq K \leq 9$
- $1 \leq N \leq 52 - K$
- The community cards present a valid deck of cards. For example, there will not be five cards of a same number.

## Examples

### Example 1

Input:
```
9 2
AA9Q3776J
nyynnnynn
```

Output:
```
99
```

Explanation:

Tommy did not raise after the first `A` indicates that Tommy does not have `A`. Tommy raised after the second `A` because he got a pair and his score increased. Tommy raised immediately after the first `9` thus he must have a `9` in his initial hand. His other card cannot be uniquely determined. But that card cannot be `A`, `Q`, `3`, `7`, `6`, `J`, so there are seven possibilities remaining: `29`, `49`, `59`, `89`, `99`, `9X`, `9K`. Among them `99` gives the highest $22$ points.

### Example 2

Input:
```
3 2
234
yyy
```

Output:
```
impossible
```

Explanation:

Tommy raised immediately after the first `2`, `3`, `4`. This indicates that Tommy has `2`, `3`, `4` in his initial hand. However only two cards are dealt for the initial hand. Therefore this contradicts Tommy's strategy.

### Example 3

Input:
```
3 2
XXX
nyn
```

Output:
```
impossible
```

Explanation:

Tommy's score must increase after the third `X` is dealt. Tommy must raise according to his strategy but he didn't.

### Example 4

Input:
```
8 3
234567AK
nnnnnnyy
```

Output:
```
KKA
```

Explanation:

Two hands give a highest score of $21$ points: `KKA` and `KAA`. `KKA` is lexicographically smaller.
