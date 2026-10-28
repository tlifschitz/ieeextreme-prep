# Cheap Construction

**IEEEXtreme 18.0** · Time limit: 1000 ms · Memory limit: 256 MB

**CS Academy:** <https://csacademy.com/ieeextreme-practice/task/cheap-construction/>

Moto Archipelago has $N$ islands numbered $1$ to $N$. Its manager wants to connect the islands with bridges with the help of Kashi Construction Company.

Kashi Construction Company works based on a string of lowercase alphabet $S$, which has one character for each of the $N$ islands. Let $S[l,r]$ be the substring of $S$ that starts at the $l$-th character and ends at the $r$-th character (characters are numbered from $1$). Also let $(u,v)$ denote a bridge connecting the islands numbered $u$ and $v$. The company can accept a string $T$ then do the following operation.

- For every $l$ and $r$ where $S[l,r] = T$, build the following bridges: $(l,l+1)$, $(l+1,l+2)$, ..., $(r-1,r)$.

For example, let $S =$ `aabcabcaa` and $T =$ `abca`.

- $S[2,5] = T$, so these bridges are built: $(2,3)$, $(3,4)$, and $(4,5)$.
- $S[5,8] = T$, so these bridges are built: $(5,6)$, $(6,7)$, and $(7,8)$.

Note that in this example, the islands are grouped into $3$ connected components: $\{1\}$, $\{2,3,4,5,6,7,8\}$, and $\{9\}$. Two islands are in the same connected component if and only if there is a sequence of bridges and islands that connects the two islands.

Sending a string to Kashi Construction Company has significant cost, so the manager wants to send *exactly one string*, and it has to be as short as possible. However, the resulting number of connected components is not decided yet, so the manager asks you to answer the following question for each $k$ from $1$ to $N$.

- What is the length of the shortest string that can be sent to Kashi Construction Company so that Moto Archipelago has $k$ connected components? If such string does not exist, answer with `0`.

## Standard input

The first line of input contains one string of lowercase alphabet $S$.

## Standard output

The output should contain $N$ integers in one line. The $i$-th integer should represent the answer for $k = i$.

## Constraints and notes

- $1 \le N \le 5000$.

## Examples

### Example 1

Input:
```
aabcabcaa
```

Output:
```
9 8 4 6 3 4 2 0 1
```

Explanation:

There are multiple strings that can be sent to Kashi Construction Company so that Moto Archipelago has $3$ connected components, such as `abca` and `aabcabc`. Out of all of them, the length of the shortest one is $4$, so the answer for $k = 3$ is $4$.

There is no string that can be sent to Kashi Construction Company so that Moto Archipelago has $8$ connected components, so the answer for $k = 8$ is $0$ .

### Example 2

Input:
```
kkkk
```

Output:
```
2 0 0 1
```

### Example 3

Input:
```
sktm
```

Output:
```
4 3 2 1
```
