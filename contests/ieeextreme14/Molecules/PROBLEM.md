# Molecules

**IEEEXtreme 14.0** · Time limit: 1000 ms · Memory limit: 256 MB

**CS Academy:** <https://csacademy.com/ieeextreme-practice/task/molecules/>

As you may remember, in the IEEEXtreme 10.0 there was a challenge called Counting Molecules. In that challenge, you had a machine that counted the number of molecules in a cup of soda which contains distilled water ($H_2O$), carbon dioxide ($CO_2$), and glucose ($C_6H_{12}O_6$).  Given a cup of sample liquid, the machine reported the number of atoms of carbon, hydrogen, and oxygen as three integers $C$, $H$, and $O$ respectively. You were asked to determine if the given number of atoms was consistent with a mixture containing only water, carbon dioxide, and glucose molecules. The answer could be `Error` when it was impossible to have a mixture of only water, carbon dioxide, and glucose molecules with the reported numbers of atoms.

In this challenge, you have the same machine that reports $C$, $H$, and $O$ for a given liquid sample. We ask you to find the smallest number of atoms that needs to be added and/or discarded so that it is possible that the sample is a mixture of only water, carbon dioxide, and glucose.

## Standard input

The input contains a single integer $T$ on the first line, the number of test cases.

Each of the next $T$ lines has three integers $C$, $H$, and $O$ giving one test case.

## Standard output

For each test case output the minimum number of atoms that needs to be added and/or discarded so that the sample becomes possibly a mixture of only water, carbon dioxide, and glucose. When the given numbers of atoms can already form a mixture of only water, carbon dioxide, and glucose, output zero.

## Constraints and notes

- $1 \leq T \leq 40$
- $0 \leq C, H, O \leq 10^6$
- It is allowed to discard all atoms. Zero atoms are considered a valid (empty) mixture.

## Examples

### Example 1

Input:
```
4
2 2 2
126 482 255
0 200 0
0 2 1
```

Output:
```
2
1
100
0
```

Explanation:

- Test case $1$: Adding one oxygen atom and removing a carbon atom makes it possible to be a mixture of $1$ water molecule and $1$ carbon dioxide molecule.
- Test case $2$: $7$ molecules of $CO_2$, $121$ molecules of water and $20$ molecules of glucose give $7+6*20=127$ carbon atoms, $2*121+12*20=482$ hydrogen atoms, and $2*7+1*121+6*20=255$ atoms of oxygen, yielding only one extra atom (carbon).
- Test case $3$: We may add $100$ oxygen atoms to have $100$ water molecules.
- Test case $4$: Without adding or discarding any atoms, a single water molecule may have the given atoms.
