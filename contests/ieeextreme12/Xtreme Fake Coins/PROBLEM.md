# Xtreme Fake Coins

**IEEEXtreme 12.0** · Time limit: 500 ms · Memory limit: 256 MB

**CS Academy:** <https://csacademy.com/ieeextreme-practice/task/xtreme-fake-coins/>

## ![](images/Zodiac-woodcut-scales.png)

Help IBM research's puzzlemaster to verify solutions for [May 2018's challenge](http://www.research.ibm.com/haifa/ponderthis/challenges/May2018.html).

There are $N$ coins, represented by the first $N$ capital letters of the English alphabet. Exactly two of them are counterfeit and have a slightly smaller weight. $M$ weightings using a double-pan balance scale have been performed, but they may not uniquely determine the pair of counterfeit coins.

Find all counterexamples of two pairs of coins $((a, b), (c, d)) \ (a < b, \ a \leq c, \ c < d,\ (a, b) \neq (c, d))$ whose weights are indistinguishable with respect to the $M$ weightings.

## Standard input

The first line contains two comma separated integers, $N$ and $M$.

The next $M$ lines contain two strings of disjoint subsets of the first $N$ English capital letters, separated by a `-` sign.

There always is an equal amount of coins on both sides.

## Standard output

List of lexicographically ordered counterexamples for the solution.

Each of them consists of two letters, an `=` sign and then another two letters.

A counterexample is a set of two pairs that cannot be distinguished by the set of $M$ weightings.

## Constraints and notes

- $0 \leq M \leq 10$
- $2 \leq N \leq 26$
- The counterexamples should be formed using only the first $N$ letters

## Examples

### Example 1

Input:
```
11,4
ABCDE-FGHIJ
AHJ-FBD
AGI-KCE
BJ-IE
```

Output:
```
AC=AK
AG=AH
BC=BK
BE=CD
BE=DK
BH=BJ
BH=DJ
BI=DG
BJ=DJ
CD=DK
CE=EK
CG=DH
CH=EJ
CI=EG
CI=EI
EG=EI
FH=GK
GH=IJ
```

Explanation:

In the first weighting we are comparing `ABCDE` on the left pan and `FGHIJ` on the right; on the last weighting we compare `BJ` on the left with `IE` on the right. In the answer we give all the cases where the proposed solution does not work. For example the last line (`GH = IJ`) means that we can not distinguish between the case where `G` and `H` are counterfeited and the case where `I` and `J` are counterfeited. The reason is that in both cases the four results of the four weightings are the same:

- `ABCDE > FGHIJ`
- `AHJ < FBD`
- `AGI < KCE`
- `BJ = IE`

### Example 2

Input:
```
15,5
ABCDE-FGHIJ
ACEGI-BDFHJ
ABCKL-FDEMN
EGOBH-IJLMN
DEGKL-FMIBC
```

Output:
```
AB=BC
AE=EK
AF=CF
AH=BG
AI=CI
AM=CM
AM=CN
BM=BN
CM=CN
DG=EH
FH=FO
FJ=FM
FJ=FN
FJ=JM
FK=HJ
FK=JO
FM=FN
FM=JM
FN=JM
HJ=JO
IK=IL
IM=IN
JK=JL
KM=LM
KN=LN
```

Explanation:

The first line in the solution (`AB = BC`) is because

- `ABCDE < FGHIJ`
- `ACEGI = BDFHJ`
- `ABCKL < FDEMN`
- `EGOBH < IJLMN`
- `DEGKL > FMIBC`

### Example 3

Input:
```
7,3
ADE-BCG
AG-BE
AC-DG
```

Output:
```

```

Explanation:

This solution is correct so there is no counterexample.
