---
title: "Airplane management: Branch-and-Cut"
permalink: /assignments/airplanes
excerpt: "Allocate airplanes to flights and maximize profit."
date: 2017-05-11
---

Given the following stats of a small airplane company, find the optimal airplane
allocation to each flight course for the next week so that the company's profit
is maximized.

| ---
| Flight course | Minimum num of passengers expected | Ticket Price
| -: | :-: | :-: | :-:
| **001** | 320 | 45
| **002** | 170 | 45
| **003** | 190 | 24

_**Unit Transportation Cost** of (Flight Course vs Plane Type)_
{: .text-center .notice--info}

| ---
| | A | B | C
| -: | :-: | :-: | :-:
| **001** | 36 | 39 | -
| **002** | 36 | 39 | 45
| **003** | - | 33 | 42

_**Passenger Capacity** of (Flight Course vs Plane Type)_
{: .text-center .notice--info}

| ---
| | A | B | C
| -: | :-: | :-: | :-:
| **001** | 20 | 15 | -
| **002** | 18 | 13 | 10
| **003** | - | 14 | 8
| **Available Planes** | 15 | 14 | 18

Also, a single plane is allowed to fly up to 3 times per week.

## Representation

Denote $$x_i$$ the number of flights to be allocated at a (flight course, plane type)
combination and $$y_i$$ the number of passengers expected to travel with a
(flight course, plane type) combination. $$x_i$$ and $$y_i$$ are enumerated in
row-major order with respect to the matrices above. The problem then, can be
represented by the following integer linear programming problem:

$$\begin{align*}
  \text{maximize} \quad& 9y_1+6y_2+9y_3+6y_4-9y_6-18y_7 \\
      \text{s.t.} \quad& x_1 + x_3 \leq 45, \\
                       & x_2 + x_4 + x_6 \leq 42, \\
                       & x_5 + x_7 \leq 54, \\
                       & 20x_1 \geq y_1, \quad 15x_2 \geq y_2, \\
                       & 18x_3 \geq y_3, \quad 13x_4 \geq y_4, \quad 10x_5 \geq y_5, \\
                       & 14x_6 \geq y_6, \quad 8x_7 \geq y_7, \\
                       & y_1 + y_2 \geq 320, \\
                       & y_3 + y_4 + y_5 \geq 170, \\
                       & y_6 + y_7 \geq 190 \\
                       & x_i, y_i \geq 0, \quad x_i, y_i \in \mathbb{Z} \quad \forall i \in \{1,...,7\}
\end{align*}$$

## Description

In order to solve this problem, we are going to use a branch and cut algorithm,
implemented in [this][script] Python script.

We first define variables which will hold the `best_solution` and the `opt_value`.
Also, we initialize a queue, which will contain LP relaxation sub-problems to be
solved, with the original problem's constraints.

```python
best_solution = None
opt_value = -np.inf
subproblems = deque([(A, b)])
```

We iterate over sub-problems until their queue is empty. In each iteration,
we pop one LP relaxation sub-problem and solve it with **simplex** algorithm, using SciPy's
[implementation][scipy-simplex].

```python
while subproblems:
    A_parent, b_parent = subproblems.popleft()
    res = simplex(-profit, A_parent, b_parent)
```

Then, we check whether the sub-problem has been solved successfully. If solution is
infeasible, we proceed to the next iteration. If the upper bound for the optimal value
of current sub-problem's branch is found to be lower or equal to our knowledge of
the current optimal integer solution, we also proceed to the next iteration. 

```python
if -res.fun <= opt_value:
    continue  # skip branching on this subproblem
```

We then list the indices of a solution's fractional elements, `fracts`. If there are
no fractional elements, then we have reached a better integer solution and so we
record it and proceed to the next sub-problem.

```python
if not fracts:
    best_solution = res.x.astype('int')
    opt_value = int(-res.fun)
    continue
```

If there are indeed any fractional elements left, we choose one and create two additional
LP relaxation problems. These two new sub-problems consist of the current
sub-problem's constraints plus a new one. The first new constraint is for the chosen
element's value not to be higher than the floor of the current fractional value.
The second one is for the chosen element's value not to be lower than the ceiling of
the current fractional value.

```python
down = np.floor(res.x[branch_i])
constrain_1 = np.zeros((1, len(profit)))
constrain_1[0, branch_i] = 1
A_child_1 = np.concatenate([A_parent, constrain_1])
b_child_1 = np.concatenate([b_parent, np.array([[down]])])
subproblems.append((A_child_1, b_child_1))

up = np.ceil(res.x[branch_i])
constrain_2 = np.zeros((1, len(profit)))
constrain_2[0, branch_i] = -1
A_child_2 = np.concatenate([A_parent, constrain_2])
b_child_2 = np.concatenate([b_parent, np.array([[-up]])])
subproblems.append((A_child_2, b_child_2))
```

## Solution

The solution is presented in the table below.
The optimal value has been found to be **8928** and the script has solved for 9 LP relaxation
sub-problems, using the **simplex** algorithm, until it found the maximum.

| ---
|**#Flights** | A | B | C | **#Passengers** | A | B | C
| -: | :-: | :-: | :-: | -: | :-: | :-: | :-:
| **001** | 45 | 29 | -  | **001** | 900 | 435 | -
| **002** | 0 | 0 | 17 | **002** | 0 | 0 | 170
| **003** | - | 13 | 1 | **003** | - | 182 | 8

[script]: https://github.com/tsirif/optimization-auth-course/blob/master/src/branch_and_cut_07.py 
[scipy-simplex]: https://docs.scipy.org/doc/scipy-0.18.1/reference/optimize.linprog-simplex.html
