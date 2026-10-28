# Hotel Wiring

**IEEEXtreme 14.0** · Time limit: 2000 ms · Memory limit: 256 MB

**CS Academy:** <https://csacademy.com/ieeextreme-practice/task/hotel-wiring/>

A construction company has decided to let an inexperienced electrician work on power supply wiring for their newest hotel building. After the construction and wiring of the building has been completed, it was identified that the electrician has made a mistake in wiring and it will take a significant amount of time to fix the issue.

The hotel consists of $M$ floors and each floor has $N$ rooms. Power supply to rooms is controlled by one master switch on each floor. By design, power is supplied to all the rooms on a floor if and only if the master switch of that floor is on. However due to the electrician's mistake in wiring, some rooms have incorrect wiring and their power is supplied the other way around. A room with incorrect wiring receives power if and only if the master switch of its floor is off.

There can be both correctly and incorrectly wired rooms on a same floor. For example, consider a floor has $4$ rooms with correct wiring and $2$ rooms with incorrect wiring. If the master switch of that floor is on, $4$ rooms will have power and $2$ rooms will not have power. If the master switch is off, then, $4$ rooms will not have power and $2$ rooms will have power.

The company does not want to spend extra money to fix the wiring mistake. Instead, they decide to first turn on all the master switches, and then turn off exactly $K$ of them to maximize the total number of rooms across all floors that will receive power.

## Standard input

The first line has a single integer $T$, the number of test cases.

For each test case, the first line consists of there integers $M$, $N$ and $K$ where $M$ is the number of floors in the hotel, $N$ is the number of rooms per floor, and $K$ is the exact number of master switches that will be turned off.

For each of the the next $M$ lines, there is a single integer between $0$ and $N$ that indicates the number of rooms that are wired correctly on one floor.

## Standard output

For each test case, output in a single line the maximum number of rooms that may receive power.

## Constraints and notes

- $1 \leq T \leq 20$
- $1 \leq K \leq M \leq 10^{6}$
- $1 \leq N \leq 10^{6}$
- The sum of $M$ across all test cases in a single test file is at most $2 \cdot 10^6$.

## Examples

### Example 1

Input:
```
2
2 2 1
2
0
2 4 2
0
3
```

Output:
```
4
5
```

Explanation:

There are two test cases in this sample test file.

In the first test case, there are two floors with two rooms on each floor. On the first floor, both rooms have correct wiring and on the second floor, both rooms have incorrect wiring. Since $K=1$, the master switch on the second floor can be turned off to supply power to both rooms. Hence, all rooms in the hotel can receive power.

In the second test case, there are two floors with four rooms on each floor. On the first floor, all rooms have incorrect wiring and on the second floor, $1$ room has incorrect wiring and $3$ have correct wiring. Since $K=2$, the master switches on both of the floors must be turned off. As a result, the number of rooms with power supply are $4$ on the first floor and $1$ on the second floor.
