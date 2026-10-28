# Training Plan

**IEEEXtreme 15.0** · Time limit: 4000 ms · Memory limit: 256 MB

**CS Academy:** <https://csacademy.com/ieeextreme-practice/task/training-plan/>

Your friend, Jason, wants to train for a 10K race and is struggling to maintain a consistent training schedule. You want to help your friend reach his goal and offer to create a training plan for him.

Jason gets bored easily when running alone. Fortunately, you have found a running team in your area that arranges daily trainings. The workouts have different paces, durations, routes, and people joining. Jason has graded each day's training based on his preferences, i.e., he has assigned an integer grade to each day's training. You would like to maximize the chances of your friend finishing the training plan by adjusting it to his preferences as much as possible.

More specifically, Jason's training plan will span $M$ consecutive periods. Each period has $X$ days, and the $1$st day of each period follows the $X$th day of the previous period. For each period, you want to select exactly $Y$ trainings out of the $X$ available. You must pick these $M\cdot Y$ trainings in a way that maximizes the sum of their grades. However, since you don't want your friend to get injured, you have to be careful and make sure you do not pick more than $K$ consecutive trainings anywhere in the whole training plan.

## Standard input

The first line contains a single integer $T$, the number of test cases.

Each test case starts with a line containing four integers $M$, $X$, $Y$ and $K$. Then $M$ lines follow, each containing $X$ integers. The $i$th line give the grades Jason assigned to each day's training in the $i$th period.

## Standard output

For each test case, output a single line containing a single integer: the sum of the grades of the best training plan you can create for your friend. If no training plan can be created under the given constraints, print `IMPOSSIBLE`.

## Constraints and notes

- $1 \leq T \leq 10$
- $1 \leq M \leq 1000$
- $1 \leq X \leq 1000$
- $1 \leq Y \leq X$
- $1 \leq K \leq 20$
- All grades are non-negative integers smaller than $1000$.
- The sum of the products of $M \cdot X \cdot Y \cdot K$ for all $T$ test cases does not exceed $10^7$.

## Examples

### Example 1

Input:
```
4
1 7 4 3
5 1 5 1 5 1 5
1 7 4 3
1 1 5 5 5 5 1
2 7 1 2
1 1 1 7 1 1 1
1 1 1 7 1 1 1
1 7 6 2
1 1 1 1 1 1 1
```

Output:
```
20
16
14
IMPOSSIBLE
```

Explanation:

There are $4$ test cases.

- Case $1$: The training plan will last for $1$ period of $7$ days (a week). We need to pick $4$ trainings for the week, but cannot pick more than $3$ trainings in a row. The best training plan has a grade sum of `20` and consists of the trainings with a grade of $5$.
- Case $2$: We have the same parameters as Case $1$, but we cannot pick the biggest trainings anymore, since this would violate our constraint and potentially injure our friend. The best training plan now has a grade sum of `16` and can be obtained in multiple ways.
- Case $3$: The training plan will last for $2$ periods of $7$ days each (two weeks). We need to pick $1$ training each week and cannot have more than $2$ trainings in a row. The best training plan now has a grade sum of `14` and consists of the two trainings with a grade of $7$.
- Case $4$: Any $3$ consecutive trainings are to be avoided. We can at most pick $5$ trainings under the constraint.
