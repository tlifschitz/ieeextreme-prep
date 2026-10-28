# IEEE754 Emulator

**IEEEXtreme 18.0** · Time limit: 2000 ms · Memory limit: 512 MB

**CS Academy:** <https://csacademy.com/ieeextreme-practice/task/ieee754-emulator/>

The IEEE 754 single-precision floating-point format is a 32-bit binary format that represents real numbers. These 32 bits are divided into three distinct parts:

1. *Sign bit (1 bit)*:
- The first bit (bit 31) indicates the sign of the number.
- `0` means the number is positive.
- `1` means the number is negative.

2. *Exponent (8 bits)*:
- The next 8 bits (bits 30 to 23) represent the exponent of the number.
- The exponent is stored using a "biased" format, with a bias of 127. This means the actual exponent is calculated as:      $\text{exponent} = \text{exponent bits value} - 127$.
- For example, if the exponent bits are `10000001` (which is 129 in decimal), the actual exponent is $129 - 127 = 2$.

3. *Fraction (mantissa) (23 bits)*:
- The last 23 bits (bits 22 to 0) represent the fraction (mantissa) of the number.
- The IEEE 754 format assumes a "normalized" representation where the leading bit is always 1 and is not stored (it is implied). Therefore, the actual value of the mantissa is: $1 + \text{fraction bits}$

     The fraction bits represent the fractional part of the number.

The value of the floating-point number is computed as $(-1)^{\text{sign}} \times 2^{(\text{exponent} - 127)} \times (1 + \text{mantissa})$ .

For the hexadecimal value `40490fdb` = `01000000010010010000111111011011`:

- *Sign bit*: `0` (positive)
- *Exponent*: `10000000` (decimal 128, so $\text{actual exponent} = 128 - 127 = 1$)
- *Mantissa*: `10010010000111111011011` (which corresponds to a fraction slightly greater than 1)

This combination represents the number `3.1415927410125732421875` (approximately).

The addition and multiplication rules (with a calculator for testing) are explained in the following links:

- [Addition and substraction](https://numeral-systems.com/ieee-754-add/)
- [Multiplication](https://numeral-systems.com/ieee-754-converter/)

*Note*: Consider the following special rules:

- $x \times \infty \to \infty \text{ for } x>0$.
- $x \times (-\infty) \to \infty \text{ for } x<0$.
- $\infty - \infty\to \text{NaN}$.
- $0 \times \infty\to \text{NaN}$.
- $x \times  \text{NaN} \to \text{NaN}$.
- $0 \times (-0) \to -0$.

To compute approximated values of functions we will assume that we must store first an hexadecimal value and then the result of many commands which (possibly) use some previously stored values.

One of the most interesting commands is Fused Multiply-Add (FMA), which receives 3 floating point values $a$, $b$ and $c$ and computes $a \times b + c$ *with only one rounding step*. This command differs with multiplying and then adding the values since multiplication does one rounding step and addition makes another one, so precision might be lost due to this.

We will start with a single hexadecimal value $C[0]$ and then many commands follow:

- Look-Up Table (LUT): Consider that many hexadecimal values are stored in many tables $LUT[i]$ of size $2^{k_{i}}$ for some $k_{i} \geq 1$. Then, if we execute a LUT command `L i j b`, then we must compute the integer value of the bits in positions $[j, j + b - 1]$ from $C[0]$ (let this value be $mask$) and the answer will be $LUT[i][mask]$. It must be guaranteed that both $b \leq k_{i}$ and $0 \leq j \leq j + b - 1 < 32$.
- NAND Gate: If we execute a NAND command `N i j`, then we must compute the [Bitwise NAND](https://es.wikipedia.org/wiki/Puerta_NAND) of the values $C[i]$ and $C[j]$.
- Fused Multiply Add: If we execute an FMA command `F i j k`, then we must compute $C[i] \times C[j] + C[k]$.
- Constant declaration: If we execute a Constant command `C h`, then we must store the hexadecimal $h$.

Given $C[0]$, the LUTs and the commands to execute, your task is to compute the value stored by the last command.

## Standard input

The first line of input contains an integer $T$, the number of test cases.

The following lines describe $T$ test cases.

The first line of each test case contains an hexadecimal value $C[0]$ that represents a single-precision floating point value.

The second line of each test case contains an integer $L$, the number of LUTs to read.

The $p$-th of the following $L$ lines contains an integer $2^{k_{i}}$ followed by $2^{k_{i}}$ hexadecimals that represent single-precision floating point values.

The next line of each test contains an integer $Q$, the number of commands to execute.

The $n$-th of the following $Q$ lines contains a command:

- `L i j b`: Store the corresponding LUT result for this command. It is guaranteed that $0 \leq i < L$, $0 \leq j \leq j + b - 1 < 32$ and $b \leq k_{i}$.
- `N i j`:  Store the corresponding NAND result for this command. It is guaranteed that $0 \leq i, j < n$.
- `F i j k`: Store the corresponding FMA result for this command. It is guaranteed that $0 \leq i, j, k < n$.
- `C h`: Store the corresponding Constant result for this command. It is guaranteed that $h$ is an hexadecimal value.

## Standard output

Print $T$ lines, the $i$-th line must contain the value stored by the last command of the $i$-th test case.

## Constraints and notes

- $1 \leq T \leq 10^{5}$.
- $1 \leq \sum\limits_{i = 1}^{T}Q_{i} \leq 10^{5}$, which means that the total number of commands doesn't exceed $10^{5}$.
- The sum of the sizes of LUTs across the test cases doesn't exceed $10^{5}$.

## Examples

### Example 1

Input:
```
4
00000000
0
3
C bf800000
C 40800000
F 2 0 1
3f800000
0
3
C bf800000
C 40800000
F 2 0 1
40490fdb
0
3
C bf800000
C 40800000
F 2 0 1
bf800001
0
3
C bf800000
C 40800000
F 2 0 1
```

Output:
```
bf800000
40400000
41390fdb
c0a00001
```

### Example 2

Input:
```
5
00000000
0
5
C 80000000
N 0 1
N 0 2
N 2 1
N 3 4
12345678
0
5
C 80000000
N 0 1
N 0 2
N 2 1
N 3 4
cccccccc
0
5
C 80000000
N 0 1
N 0 2
N 2 1
N 3 4
cdef0123
0
5
C 80000000
N 0 1
N 0 2
N 2 1
N 3 4
01020304
0
5
C 80000000
N 0 1
N 0 2
N 2 1
N 3 4
```

Output:
```
80000000
92345678
4ccccccc
4def0123
81020304
```
