---
title: "Unbounded knapsack problem"
permalink: /assignments/knapsack
excerpt: "Solve an unbounded knapsack problem with DP and IP."
date: 2017-05-15
---

Solve the following knapsack problem using (1) integer programming and
(2) dynamic programming.

We have three types of products that we want to carry over in a sack. Their weight and value
per product unit are described by the list of tuples: `[(5, 5), (8, 6), (3, 4)]`.
Our sack can only hold up to **30** units of weight and also we would like to have at
least one product out of each type. Which is the optimal selection of products?

## Representation

This problem is an instance of the unbounded version of the knapsack problem. Its
solution, as the numbers of products selected for each type, is restricted to
integers, however is not upper bounded. Specifically, it is requested that $$x_i \geq 1$$ for
each product type $$i$$. Transforming the problem to restrict for $$y_i \geq 0$$, by
applying $$x_i = 1 + y_i$$, yields the following optimization problem:

$$\begin{align*}
  \text{maximize} \quad& 5y_1 + 6y_2 + 4y_3   \\
      \text{s.t.} \quad& 5y_1 + 8y_2 + 3y_3 \leq 14, \\
                       & y_i \geq 0, y_i \in \mathbb{Z} \quad \forall i \in \{1,2,3\}
\end{align*}$$

This formulation is equivalent to the original problem, if we take into account that
the objective function is shifted with a constant factor of `-sum(values) == -15`
and maximum allowed weight also by a constant factor of `- sum(weights) == -16`. In
addition: $$x_i = 1 + y_i \quad \forall i \in \{1, 2, 3\}$$.

## Solution

Both methods find the same unique solution to this problem: `(2, 1, 4)` with optimal
value of **32**. Code can be found in [this][script] Python script.

### Dynamic Programming

We will now describe the dynamic programming solution used. Method `solve_dynamic`
implements it.

First, initialize an array (`opt_values`) of length `max_w + 1` containing the worst possible value,
 0, for each $$w \in \{0,...,max\_w\}$$. Also, initialize a map (`sols`) to return the worst
 possible solution `(0, 0, 0)`.

```python
opt_values = np.zeros(max_w + 1, dtype='int')
sols = dd(lambda: set([(0, ) * len(values)]))
```

Then, begin an iteration over $$\{1,...,max\_w\}\times\text{values}$$ in row-major
order.

```python
for w in range(1, max_w + 1):
    for i in range(len(values)):
```

For each of the three product types, we consider including a single product in the
optimal solution for the optimization problem which has maximum weight equal to `w`.
A product participates in the optimal solution, if it can fit in a sack of capacity `w`
**and** it offers the maximum value versus the rest of the product types. This
relation can be described by the following recursive formula:

$$
opt\_values[w] = \text{max} \{v_i + opt\_values[w - w_i] : w_i \geq w\} 
$$

```python
if w < weights[i]:
    continue
choice = values[i] + opt_values[w - weights[i]]
```

If a candidate selection is the best one, we then check for the optimal solutions
corresponding to `w - weights[i]` and increment by one the element of that product
type for each solution.

```python
if choice >= opt_values[w]:
    t = []
    for sol in list(sols[w - weights[i]]):
        s = list(sol)
        s[i] += 1
        t.append(tuple(s))
    if choice > opt_values[w]:
        sols[w] = set(t)
        opt_values[w] = choice
    else:
        sols[w] |= set(t)
```

**Note** that we allow for multiple solutions which can correspond to optimal values
for each weight value.
{: .notice--primary} 

### Integer Programming

The integer programming method is implemented in method `solve_branch_cut` and it is
described by its documentation, as well as in the solution for the [airplane
management]({{ "/assignments/airplanes#description" | absolute_url}}) problem.
It solves for 7 LP relaxation sub-problems before reaching to a conclusion. 

[script]: https://github.com/tsirif/optimization-auth-course/blob/master/src/knapsack_08.py 
