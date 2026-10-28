**CS Academy:** <https://csacademy.com/ieeextreme-practice/task/8761fb7efefcf1d890df1d8d91cae241/>

Blackgate Penitentiary
Time limit: 2500 ms
Memory limit: 256 MB


Vangelis the Batbear trapped all the members of Joker's Streetgang in a basement.

Your job as a police officer is to transport all gang members to Blackgate Penitentiary.

To facilitate the transport, you should form a row such that the heights of the gang members are in non-decreasing order. For each gang member you should find the minimum and the maximum position where they can be in a valid sorted row and produce a roster with this information.

Standard input
Input will start with a line that contains only one integer 
n
n, the number of crew members that were arrested. On each of the following 
n
n lines there will be a single word 
s
s and an integer 
h
h separated by a space character, where 
s
s is the name and 
h
h is the height of the crew member.

Standard output
On the output, there will be 
g
g lines. Each line will contain in alphabetical order and space separated the names of the crew members that have the same height, followed by the minimum and the maximum position where any member of the specific group can be placed. The groups should be printed in increasing order of their members' heights.

Constraints and notes
1≤n≤1000
1≤length(si​)≤10
120≤hi≤250

Names are only composed of characters of the Latin alphabet.
