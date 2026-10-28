**CS Academy:** <https://csacademy.com/ieeextreme-practice/task/labradoodle/>

# Labradoodle

**IEEEXtreme 17.0** · Time limit: 5000 ms · Memory limit: 256 MB

Sporks, labradoodles, and chocoholics are all examples where two words are blended into one. Your challenge to determine whether a word is a blended word given a dictionary of words.

For this challenge, we assume that the blended word is created as follows:

1) A dictionary word is chosen and a prefix with at least length 3 is taken from this word

2) Another (maybe the same) dictionary word is chosen and a suffix with at least length 3 is taken from this word

The prefix and the suffix are combined to create the blended word. If the prefix ends with the same letter that the suffix starts with, one of these matching letters may be dropped.

## Standard Input

Input begins with two-space separated integers *n* and *m*. The next *n* lines contain a word from the dictionary, consisting of lowercase letters only.  The remaining *m* lines contain words, consisting only of lowercase letters, that may be blended words.

## Standard Output

For each of the potential blended words, output one of the following:

- `ambiguous`, if there is more than one dictionary word pair that could create the blended word
- `none`, if no dictionary word pairs could create the blended word
- Otherwise. the dictionary word that contributes the prefix, followed by a space, followed by the dictionary word that provides the suffix.

## Constraints and notes

- $1 \leq n \leq 10,000$
- $1 \leq m \leq 10,000$

Each dictionary word will be made up of lowercase ASCII letters and have between 1 and 50 characters, inclusive.

Each potential blended word will be made up of lowercase ASCII letters and have between 1 and 100 characters, inclusive.

Note that none of the potential blended words will also be dictionary words.  However, the same dictionary word can provide both the prefix and the suffix of a blended word.

## Examples

### Example 1

Input:
```
6 7
spoon
fork
labrador
poodle
form
car
spork
labradoodle
fordle
cardor
lark
spoooon
labradabrador
```

Output:
```
spoon fork
labrador poodle
ambiguous
car labrador
none
spoon spoon
labrador labrador
```

Explanation:

For "spork", we can combine the prefix "spo" from "spoon" with the suffix "ork" from "fork". Since the prefix ends with the same letter as the suffix, we can combine these letters and use only one "o".

"fordle" is ambiguous because it can be made with "fork" and "poodle" as well as "form" and "poodle".

"lark" cannot be a blended word because it is too short.

With "spoooon" and "labradabrador" note that a blended word can use the same word for the prefix and suffix.
