**CS Academy:** <https://csacademy.com/ieeextreme-practice/task/caesar_redux/>

# Caesar Redux

**IEEEXtreme 17.0** · Time limit: 1000 ms · Memory limit: 256 MB

The Caesar cipher is a simple encryption technique that was used by Julius Caesar to send secret messages to his allies. It works by shifting the letters in the plaintext message by a certain number of positions. Decryption is performed by shifting in the opposite direction by the same number of positions.

A program that implements this technique is needed to encrypt a plaintext message or decrypt a ciphertext messages. Spaces are not affected by encryption or decryption.

You need to determine whether the value that is provided is plaintext or ciphertext. If the value provided is plaintext, you should output the encrypted message given the shift value above. If the provided value is ciphertext, you should output the decrypted message.

## Standard Input

Input begins with an integer $n$ on a line by itself that indicates how many messages are in the input.

The next $2 n$ lines contain a line with the shift amount followed by a line with either a plaintext or a ciphertext message.

## Standard Output

For each message in the input, output the plaintext if the message is ciphertext, or the ciphertext if the message is plaintext.

## Constraints and notes

- $1 \leq n \leq 25$
- The shift value will be between 1 and 25, inclusive.
- Each message will consist of lowercase letters and spaces, and contain between 3 and 300 characters.
- If the message provided contains the word "the", then it is plaintext. Otherwise, it is ciphertext.

## Examples

### Example 1

Input:
```
2
19
we accept the ieeextreme challenge
19
qbspbz jhlzhy olsk aol vmmpjl vm wvuapmle theptbz wypvy av iljvtpun kpjahavy
```

Output:
```
dl hjjlwa aol pllleayltl johsslunl
julius caesar held the office of pontifex maximus prior to becoming dictator
```
