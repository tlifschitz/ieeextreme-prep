**CS Academy:** <https://csacademy.com/ieeextreme-practice/task/icarus/>

Icarus
Time limit: 1250 ms
Memory limit: 256 MB

Icarus is caught in a maze again, but this time he is determined to escape. Your task is to make sure Icarus stays trapped forever.

The maze can be seen as a binary tree, where each node corresponds to a room. From any room, Icarus can move to one of at most three neighbouring rooms, corresponding to the parent, left son or right son of the current node, if they exist. One of the rooms contains a secret door that leads to the exit. Your goal is to make sure that room is never visited.

Icarus starts in a node A and then moves according to a predefined plan. He has a string S which contains only the letters L, R and U. Icarus will use the string S to navigate the maze. Starting in node A, he will decide where to move next according to the value of the first character of S:

L corresponds to the left son
R corresponds to the right son
U corresponds to the parent node

After the first move, Icarus will repeat the process using the second character of S, and so on. When reaching the final character of S, he will start again from the beginning of the string. If at any given moment the node where Icarus would like to move does not exist, the current character is skipped and the process continues.

Given the string S, you should build a binary tree, choose a starting node A and an exit node B, in such a way that Icarus never visits node B and stays trapped forever.

Standard input
The first line contains the string S.

Standard output
The first line should contain three integers N, A and B, representing the number of nodes of the binary tree, the starting node and the exit node, respectively.

Next, for each node 
i from 1 to N, output two integers, representing the left son and the right son of 
i. In case node i doesn't have a left or right son, output 0 instead.

Constraints and notes
1≤∣S∣≤2000
1≤N≤2∗∣S∣

If there is no solution given the constraints, output −1