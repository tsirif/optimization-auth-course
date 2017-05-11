---
title: "Minimize petroleum transportation cost"
permalink: /assignments/petroleum
excerpt: "Solve a linear program."
date: 2017-04-23
---

Follows the naming of quantities to be transported:

  * East Chicago -> Des Plaines: $$x_1$$
  * Hammond -> Des Plaines: $$x_2$$
  * Hammond -> Niles: $$x_3$$
  * East Chicago -> Niles: $$x_4$$

$$\begin{align*}
  \text{minimize} \quad& 16x_1+7x_2+14x_3+8x_4 \\
      \text{s.t.} \quad& x_4 + x_1 \geq 50 \\
                       & x_1 + x_2 \geq 100 \\
                       & x_2 + x_3 \geq 120 \\
                       & x_3 + x_4 \geq 70 \\
                       & x_i \geq 0 \quad \forall i \in \{1,2,3,4\}
\end{align*}$$


## Solution

We are going to solve the dual problem instead, using the Simplex algorithm.
This is done because the dual problem is expected to be in canonical form without
any further transformations. Indeed, applying the duality transformation yields:

$$\begin{align*}
  \text{maximize} \quad& 50u_1+100u_2+120u_3+70u_4 \\
      \text{s.t.} \quad& u_1 + u_2 \leq 16 \\
                       & u_2 + u_3 \leq 7 \\
                       & u_3 + u_4 \leq 14 \\
                       & u_4 + u_1 \leq 8 \\
                       & u_i \geq 0 \quad \forall i \in \{1,2,3,4\}
\end{align*}$$

### Starting canonical tableau

$$
  \begin{array}{cr}
    \begin{matrix}
      u_1 & u_2 & u_3 & u_4 & s_1 & s_2 & s_3 & s_4 & m & b 
    \end{matrix} \\
    \begin{bmatrix}
      1   &  1  & 0   &  0  &  1  &  0  &  0  &  0  & 0 & 16 \\
      0   &  1  &  1  & 0   &  0  &  1  &  0  &  0  & 0 & 7 \\
      0   &  0  &  1  &  1  & 0   &  0  &  1  &  0  & 0 & 14 \\
      1   & 0   &  0  &  1  &  0  & 0   &  0  &  1  & 0 & 8 \\
      -50 & -100 & -120 & -70 &  0 & 0 &  0  &  0  & 1 & 0
    \end{bmatrix}
  \end{array}
$$

### First iteration

We pick a column with the most negative number in the last row, i.e. $$u_3$$ column
with value $$-120$$ and the row with the smallest ratio $$b_i/u_{3, i}$$, i.e row $$2$$
with ratio $$7$$.

```python
a[4, :] += 120 * a[1, :]
a[2, :] -= 1 * a[1, :]
```

$$
  \begin{array}{cr}
    \begin{matrix}
      u_1 & u_2 & u_3 & u_4 & s_1 & s_2 & s_3 & s_4 & m & b 
    \end{matrix} \\
    \begin{bmatrix}
      1&   1&   0&   0&   1&   0&   0&   0&   0&  16\\
      0&   1&   1&   0&   0&   1&   0&   0&   0&   7\\
      0&  -1&   0&   1&   0&  -1&   1&   0&   0&   7\\
      1&   0&   0&   1&   0&   0&   0&   1&   0&   8\\
    -50&  20&   0& -70&   0& 120&   0&   0&   1& 840
    \end{bmatrix}
  \end{array}
$$

### Second iteration

We pick a column with the most negative number in the last row, i.e. $$u_4$$ column
with value $$-70$$ and the row with the smallest ratio $$b_i/u_{4, i}$$, i.e row $$3$$
with ratio $$7$$.

```python
a[4, :] += 70 * a[2, :]
a[3, :] -= 1 * a[2, :]
```

$$
  \begin{array}{cr}
    \begin{matrix}
      u_1 & u_2 & u_3 & u_4 & s_1 & s_2 & s_3 & s_4 & m & b 
    \end{matrix} \\
    \begin{bmatrix}
      1&    1&    0&    0&    1&    0&    0&    0&    0&   16\\
      0&    1&    1&    0&    0&    1&    0&    0&    0&    7\\
      0&   -1&    0&    1&    0&   -1&    1&    0&    0&    7\\
      1&    1&    0&    0&    0&    1&   -1&    1&    0&    1\\
    -50&  -50&    0&    0&    0&   50&   70&    0&    1& 1330
    \end{bmatrix}
  \end{array}
$$

### Third iteration

We pick a column with the most negative number in the last row, i.e. $$u_1$$ column
with value $$-50$$ and the row with the smallest ratio $$b_i/u_{1, i}$$, i.e row $$4$$
with ratio $$1$$.

```python
a[4, :] += 50 * a[3, :]
a[0, :] -= 1 * a[3, :]
```

$$
  \begin{array}{cr}
    \begin{matrix}
      u_1 & u_2 & u_3 & u_4 & s_1 & s_2 & s_3 & s_4 & m & b 
    \end{matrix} \\
    \begin{bmatrix}
      0&    0&    0&    0&    1&   -1&    1&   -1&    0&   15\\
      0&    1&    1&    0&    0&    1&    0&    0&    0&    7\\
      0&   -1&    0&    1&    0&   -1&    1&    0&    0&    7\\
      1&    1&    0&    0&    0&    1&   -1&    1&    0&    1\\
      0&    0&    0&    0&    0&  100&   20&   50&    1& 1380
    \end{bmatrix}
  \end{array}
$$

This is the final iteration of the Simplex algorithm because the feasible solution
that is represented by the matrix above is the optimal. This is seen by checking the
last row for negative numbers. Since all numbers in the last row are non-negative,
the algorithm stops.

  * Non-basic variables: $$u_2, s_2, s_3, s_4 = 0$$
  * Basic variables: $$u_1 = 1, \quad u_3 = 7, \quad u_4 = 7, \quad s_1 = 15$$
  * Maximum: $$m = 1380$$

Since the primal problem is a linear program, the strong duality theorem[^1] holds.
This means that the primal optimal objective is equal to the dual. Also, it is known
that the solution of a linear program lies on the boundary of the feasibility region.
Since simplex algorithm navigates through the vertices of a --- 4-dimensional in this
problem --- polytope, we expect that the feasible candidate solutions (points in 4D)
can be enumerated by solving all possible $$4 \times 4$$ linear systems which result
from the boundary conditions. In this particular problem, we can observe that a point solution
does not arise when we pick all $$4$$ possible non-trivial conditions. This is because
the matrix:

$$
\begin{bmatrix}
  1 & 0 & 0 & 1 \\
  1 & 1 & 0 & 0 \\
  0 & 1 & 1 & 0 \\
  0 & 0 & 1 & 1
\end{bmatrix}
$$

is singular and in particular has *rank* equal to 3. This means that picking any
3 of these initial boundary conditions will suffice to solve for the exact optimal
solution, when someone already has the optimal objective value. This *"inverse
linear program"* syllogism is particular to this setting. So the final solution is:

$$
  \begin{bmatrix}
    16 & 7 & 14 & 8 \\
    1 & 0 & 0 & 1 \\
    1 & 1 & 0 & 0 \\
    0 & 1 & 1 & 0
  \end{bmatrix} \cdot
  \begin{bmatrix}
    x_1 \\ x_2 \\ x_3 \\ x_4
  \end{bmatrix} = 
  \begin{bmatrix}
    1380 \\ 50 \\ 100 \\ 120
  \end{bmatrix} \Rightarrow
$$

$$
  \overrightarrow{x} =
  \begin{bmatrix}
    0 \\ 100 \\ 20 \\ 50
  \end{bmatrix}
$$

[^1]: [Strong duality theorem](https://en.wikipedia.org/wiki/Strong_duality)
