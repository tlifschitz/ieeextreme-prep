**CS Academy:** <https://csacademy.com/ieeextreme-practice/task/resaturant_cipher/>

# Restaurant Cipher

**IEEEXtreme 17.0** · Time limit: 1000 ms · Memory limit: 256 MB

Ali always asks his chef to cook some specific recipes. They wanted to have some fun, so, they agreed to name some recipes with just the letters: A, B, C, D, E, F and G, and not more. Now, if Ali wants a recipe, he sends a secret message to his chef that asks for a single recipe.

Your task is to break Ali's scheme for creating the secret messages, based on the example messages in the testcase below.

## Standard Input

Input begins with an integer $n$ on a line by itself that indicates how many secret messages are in the input.

The next $n$ lines each contain a secret message.

## Standard Output

For each secret message, output a line with a single letter that indicates which recipe is being requested.

## Constraints and notes

- $1 \leq n \leq 20$

Each message will consist of lowercase letters, spaces, and punctuation.  Each message will contain no more than 50,000 characters.

## Examples

### Example 1

Input:
```
5
my cat is so cute.
the baby is crying.
ieeextreme is tricky!
i want to buy a avocado for guacamole.
good grief, this task requires a gigantic genious.
```

Output:
```
C
B
E
A
G
```
