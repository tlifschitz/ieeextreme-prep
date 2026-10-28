# Elementary

**IEEEXtreme 11.0** · Time limit: 1000 ms · Memory limit: 128 MB

**CS Academy:** <https://csacademy.com/ieeextreme-practice/task/c787255968c972c653677a52599ecc2f/>

Write a program that converts a word in the English dictionary (a string of lower case letters) into a number. Below are some examples of input-output pairs and there is a server that can give you more outputs for given inputs.

Your task is to find out what the functions does and program it.

## Standard input

On the first line there will be an integer $n$, the number of lines that will follow.

Lines $2, ..., n + 1$ will contain one word on each one.

## Standard output

Print a list of $n$ numbers, one per line.

For the given tests, each number will be smaller or equal to $10^6$.

## Examples

### Example 1

Input:
```
15
ieeextreme
one
brainteaser
snow
unicorn
laparoscopy
overcautiousness
cosmos
conclusion
wisconsin
binationalism
barbascos
cacophonic
inosculate
pneumonoconiosis
```

Output:
```
0
1
2
3
4
5
6
7
8
9
10
11
12
13
48
```

### Example 2

Input:
```
6
monkey
frog
bison
chinook
puffin
rhinoceros
```

Output:
```
0
1
2
3
4
6
```

### Example 3

Input:
```
5
kale
asparagus
broccoli
spinach
chocolate
```

Output:
```
0
1
2
3
4
```

## Sample Tester

Here's a helper so you can test the server:

- Modify the input (left), and hit compute.
- You are allowed to interrogate at most $100$ strings of length at most $100$, each.
- There is a limit of $10$ interrogations per minute.

<ServerInputTest type="elementary" height={300} input="3\nOk\nNotOk\nFine" />

---
