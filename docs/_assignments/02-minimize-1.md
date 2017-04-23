---
title: "Constrained minimization: graphical solution" 
permalink: /assignments/minimize-1
excerpt: "Find graphically the solution to this minimization problem."
date: 2017-04-23
---

Find *graphically* the solution to the following constrained minimization problem:

$$\begin{align*}
  \text{minimize} \quad& (x_1 - 3)^2 + (x_2 - 2)^2 \\
  \text{s.t.} \quad& x_1^2 - x_2 - 3 \leq 0 \\
                   &x_2 - 1 \leq 0 \\
                   &-x_1 \leq 0 \\
\end{align*}$$

## Solution

In the following graph, created with [this][script] Python script, there is a 2D
representation of the problem. We can see the contour lines of the original function
to be minimized $$(x_1 - 3)^2 + (x_2 - 2)^2$$ and its (unconstrained) minimum at
$$(3, 2)$$. In addition, the *feasible region* of the constrained problem is filled
with **orange** color.

![Problem image](/assets/images/02-minimize-1.png "Contours and boundaries"){: .align-center} 

As it can be seen, the (unconstrained) objective function is minimized outside the
feasible region of the constrained problem. This means, as also this graph suggests,
that the minimum of the constrained problem will lie on the boundaries of the feasible
region. As the contours are representing equivalued manifolds on the objective function,
moving along the curve preserves the function's value. However, moving away results in
change. If another curve has a section with a contour line, moving
along that curve from that point of section results in changing value because the
direction of infinitesimal movement is not aligned with the contour. As a result,
we are looking for points in the feasibility boundary on which infinitesimal movement
leaves the value invariant. On these points the boundary must be touching a contour.[^1]

[^1]: Intuition originates from [Karush–Kuhn–Tucker conditions][KKT]

As we move from contours with minimum value (point $$(3, 2)$$) to contours with higher value,
the first contour touching the boundary corresponds to value of $$2$$. This is the
minimum value of the constrained problem and it happens at the point $$(2, 1)$$, as
it can be seen from the graph.

[script]: https://github.com/tsirif/optimization-auth-course/blob/master/src/02-minimize-1.py 
[KKT]: https://en.wikipedia.org/wiki/Karush%E2%80%93Kuhn%E2%80%93Tucker_conditions
