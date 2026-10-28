**CS Academy:** <https://csacademy.com/ieeextreme-practice/task/BadPasswords/>

# Bad Passwords

**IEEEXtreme 17.0** · Time limit: 3000 ms · Memory limit: 256 MB

Xtreme Insecurity, Inc. has a password policy that requires users to change their password every month. Some users have a hard time remembering the password when they change it, so they have taken to using iterated passwords, in which most of the password stays the same, except for a small part that is incremented or decremented. An example would be changing a password from "Secret16!" to "Secret18!" or "PasswordOctober" to "PasswordSeptember".

For this problem, you will be given lists of iterated sequences. You will reject a password change from $p_{old}$ to $p_{new}$ if $p_{old}$ can be expressed as a string $a + s_1 + b$ and $p_{new}$ can be expressed as a string $a + s_2 + b$, where:

- $+$ is the string concatenation operator,
- $a$ is a common prefix of length 0 or longer,
- $s_1$ and $s_2$ are strings from the same iterated sequence, and
- $b$ is a common suffix of length 0 or longer.

For example, if "16" and "18" are in the same iterated sequence, we would reject the change from "Secret16!" to "Secret18!" because the two passwords can be expressed as "Secret" + "16" + "!" and "Secret" + "18" + "!".  These strings have identical prefixes and suffixes, and "16" and "18" are in the same sequence.

Similarly, if "October" and "September" were in the same iterated sequence, we would reject the change "PasswordOctober" to "PasswordSeptember", since these strings can be expressed as "Password" + "October" + "" and "Password" + "September" + "".

## Standard Input

The first line contains an integer $n$, indicating the number of iterated sequences.

The next $n$ lines each give a sequence of iterated values.  The $i^{th}$ line starts with an integer, $m_i$ giving the number of iterated values in the sequence $S_i$. The remainder of the line contains the list of $m$ space-separated values in the sequence.

The next line presents an integer $p$, which denotes the number of password changes to examine.  The subsequent $p$ lines have two space separated values specifying the old password and the new one, respectively.

## Standard Output

For each password change pair, you should output "REJECT" if $p_{old}$ and $p_{new}$ if we should reject the change according to the rules above.

 Otherwise, you should output "OK".

## Constraints and notes

- $1 \leq n \leq 10$
- $2 \leq m \leq 250$
- $1 \leq p \leq 1000$

All iterated values will be at most 10 characters. They will be ASCII values and include letters, numbers and punctuation.

The passwords will be at most 1000 characters long.

None of the iterated values or passwords will include white-space characters.

The new password will always differ from the old password in at least one character.

Note that the matching of strings should be case-sensitive.

## Examples

### Example 1

Input:
```
6
10 0 1 2 3 4 5 6 7 8 9
12 January February March April May June July August September October November December
7 Monday Tuesday Wednesday Thursday Friday Saturday Sunday
3 qwerty asdf zxcv
2 ana bob
3 ? . !
20
password1 password2
Pass123 pass124
ShhMonday ShhMarch
January23 March23
ABCJanuary MarchABC
January23 february23
Tuesday Sunday
xyz123 124xyz
zxcvz qwertyz
asdfasdf asdfzxcv
asdfasdf zxvcasdf
bobobob anaobob
bobobob boboana
banana bbobna
banana banbob
banana baboba
password!!! !password!!
password!!! password???
password?!! password?!?
password!!! password!?!
```

Output:
```
REJECT
OK
OK
REJECT
OK
OK
REJECT
OK
REJECT
REJECT
OK
REJECT
REJECT
REJECT
REJECT
OK
OK
OK
REJECT
REJECT
```

Explanation:

We reject the change of "password1" to "password2" because we can express these strings as "password" + "1" + "" and "password" + "2" + "".  These strings share a common prefix and suffix, and "1" and "2" are present in the first sequence.

The change from "Pass123" to "pass124" is OK because the comparisons are case sensitive.  The only way to express these strings with a common prefix and suffix is "" + "Pass123" + "" and "" + "pass124" + "".  Note that none of the iterated sequences contain these middle strings.

The change from "SshMonday to "SshMarch" is OK. We can express these passwords as "Ssh" + "Monday" + "" and "Ssh" + "March" + "".  However, "Monday" and "March" are in different iterated sequences.

We reject the change of "January23" to "March23" because we can express these strings as "" + "January" + "23" and "" + "March" + "23".  Note that "January" and "March" are in the same iterated sequence.
