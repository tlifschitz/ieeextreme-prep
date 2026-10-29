**CS Academy:** <https://csacademy.com/ieeextreme-practice/task/sequence-decomposition/>

Sequence Decomposition
Time limit: 1000 ms
Memory limit: 256 MB

An ancient ancestral saying states that the number 112012 brings good luck in any form it may appear (that is, as the number 112012, as the sequence {1, 1, 2, 0, 1, 2}, among others). Moreover, it is said that a sequence of characters consisting only of 0, 1, and 2 is considered fortunate if it can be decomposed into multiple subsequences {1, 1, 2, 0, 1, 2}.

Miguel has some fortunate sequences, and he will only give them to you if you can find a valid decomposition for each one. It's your time to show what you're capable of!

Note: A subsequence of a sequence S is a sequence that can be derived from S by deleting zero or more elements without changing the order of the remaining elements.
For example, the sequence {1, 2, 3, 2, 3} contains {1, 2, 2} and {1, 3, 2} as subsequences but {2, 3, 1} is not contained as a subsequence.

Standard input

The first line contains an integer T, denoting the number of sequences.
Each of the next T lines contains a sequence Sᵢ to be decomposed.

Standard output

For each sequence Sᵢ, in the order of input, print |Sᵢ| / 6 lines, each containing 6 integers in increasing order, representing the indices of a subsequence {1, 1, 2, 0, 1, 2} such that all of them together decompose the sequence Sᵢ.
If there are multiple valid answers, you may print any of them.

Constraints and notes

1 ≤ T ≤ 2 × 10⁵

1 ≤ |Sᵢ| ≤ 6 × 10⁵

The total sum of |Sᵢ| over all test cases does not exceed 3 × 10⁶.

Sᵢ is fortunate for all i = 1, ..., T.