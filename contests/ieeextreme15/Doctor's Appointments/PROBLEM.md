# Doctor's Appointments

**IEEEXtreme 15.0** · Time limit: 6000 ms · Memory limit: 256 MB

**CS Academy:** <https://csacademy.com/ieeextreme-practice/task/appointment/>

The global pandemic has caused the Doctor Xtreme's office to become ultra busy. There are $N$ patients numbered $1$ to $N$ that need to see Doctor Xtreme in the following $N$ days. On each day Doctor Xtreme will have a single appointment to see one of the $N$ patients. Each patient $i$ has provided his/her available time window as two integers $L_i, R_i$, which means that he/she can come to see Doctor Xtreme on any day between the $L_i$th day and the $R_i$th day (inclusive on both ends).

Can Doctor Xtreme successfully schedule $N$ appointments to see all the $N$ patients?

## Standard input

The first line of input contains a single integer $T$, the number of test cases.

Each test case begins with an integer $N$ on the first line, the number of patients. The next $N$ lines each have two integers, describing the available time window of one patient. The $i$th line has $L_i$ and $R_i$.

## Standard output

For each test case output a single line.

If it is possible for Doctor Xtreme to see all the $N$ patients, output $N$ space-separated integers on a single line. The $i$th of these integers is the patient that Doctor Xtreme will see on the $i$th day. If there are multiple ways to schedule the $N$ appointments, you may output any of them.

If Doctor Xtreme cannot see all the $N$ patients, output `impossible`.

## Constraints and notes

- $1 \leq T \leq 30$
- $2 \leq N \leq 10^5$
- $1 \leq L_i \leq R_i \leq N$
- For $60\%$ of the test files, $N \leq 10$.
- For $80\%$ of the test files, $N \leq 1\,000$.

## Examples

### Example 1

Input:
```
3
3
1 1
1 2
2 3
2
1 2
1 2
2
1 1
1 1
```

Output:
```
1 2 3
1 2
impossible
```

Explanation:

There are $3$ test cases.

- Case $1$: Patient $1$ can see the doctor on day $1$. Patient $2$ may see the doctor on either day $1$ or day $2$. Patient $3$ may see the doctor on either day $2$ or day $3$. Therefore the doctor has only one way to schedule the appointments: see patient $1$ on day $1$, patient $2$ on day $2$, and patient $3$ on day $3$.
- Case $2$: Both patients can see the doctor on both days. Both `1 2` and `2 1` will be accepted.
- Case $3$: Neither patient can come on day $2$, and it is thus impossible to see both patients.
