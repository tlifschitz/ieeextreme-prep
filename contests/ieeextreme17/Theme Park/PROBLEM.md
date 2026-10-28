**CS Academy:** <https://csacademy.com/ieeextreme-practice/task/theme_park/>

# Theme Park

**IEEEXtreme 17.0** · Time limit: 2000 ms · Memory limit: 256 MB

Xtreme Fun uses a very different model for their amusement park. Customers purchase tickets at the gate and pay for rides with these tickets. However, the charge for the ride is not fixed, and depends instead on which ride they just finished.

They would like to add to the excitement of this model by changing some of the costs, so that rather than charging a customer, they give extra tickets to a customer if they choose a particular sequence of rides. For example, rather than having a customer pay for tickets, the park could give a customer 100 tickets for choosing to go on the Scrambler ride right after the Chaos ride. The organizers would like to be able to give the maximum number of tickets away, but they want to make sure that customers would eventually run out of tickets.

## Standard Input

Input begins with an integer $t$ that indicates how many testcases occur in the input.

Each testcase begins with two integers $n$ and $d$ on a line by itself. $n$ indicates how many rides that park contains, and $d$ is the number of ride sequences for which the organizers want to give tickets away.

The following $n \times (n-1)$ lines describe the cost of a ride in the park.  The $i^{th}$ line is in the form:

  $ride_{i1}$ $ride_{i2}$ $t_{i}$

which indicates the cost for riding $ride_{i2}$ after $ride_{i1}$ is $t_i$ tickets.

## Standard Output

For each testcase in the input, output the maximum number of tickets that can be given out on $d$ sequences in the park.  Each one of the paths should give away at least one ticket.

## Constraints and notes

- $1 \leq t \leq 10$
- $1 \leq n \leq 500$
- $1 \leq d \leq 2$
- $2 \leq t_i \le 10^6$ for all valid $i$

The rides will be made up of an alphanumeric string of no more than 10 characters (i.e. no spaces).

The size of each input file will be less than 7 megabytes.

## Examples

### Example 1

Input:
```
3
3 1
chaos scrambler 31
chaos carousel 17
carousel chaos 53
scrambler chaos 37
scrambler carousel 23
carousel scrambler 19
3 1
chaos scrambler 37
chaos carousel 17
carousel chaos 53
scrambler chaos 31
scrambler carousel 23
carousel scrambler 19
4 2
a b 40
a c 20
a d 20
b a 30
b c 30
b d 20
c a 20
c b 20
c d 40
d a 30
d b 20
d c 30
```

Output:
```
52
49
58
```

Explanation:

In the first testcase, we can give customers 52 tickets for riding the carousel after riding chaos.  Note that if we gave them 53 tickets, they would be able to continuously ride the following rides, with no decrease in tickets, since riding the chaos after the carousel costs 53 tickets:

chaos->carousel->chaos

In the second testcase, we can give customers 49 tickets for riding the carousel after riding chaos.  Note that if we gave them 50 tickets, they would be able to continuously ride the following rides, with no decrease in tickets:

chaos->carousel->scrambler->chaos

In the third testcase, we can give away a maximum of 58 tickets for two ride sequences.
