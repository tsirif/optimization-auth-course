---
title: "Minimum length staircase"
permalink: /assignments/staircase
excerpt: "Find a stair of minimum length subject to a constrain."
date: 2017-04-23
---

![Problem image](/assets/images/01-staircase.png "Staircase above a block."){: .align-left} 
Find the stair of minimum length which can be supported by the floor and the wall with
respect to an orthogonal block with dimensions *axb*.

## Solution

From the constrain of the block, we can infer that $$ x_0 > a > 0 $$ and $$ y_0 > b > 0 $$.
Having $$x_0$$ or $$y_0$$ below these bounds will result in the ladder passing through the
block which is unfeasible by the problem statement.

Each $$x_0 > a$$ --- corresponding to a *"floor"* point $$(x_0, 0)$$ in 2D space --- can be associated with
a $$y_0 > b$$ --- corresponding to a *"wall"* point $$(0, y_0)$$ in 2D space --- with which
they define a unique line, which is considered to be the ladder in question. The
ladder's equation is then given by:

$$
\begin{align*}
  & y = \frac{y_0 - 0}{0 - x_0} \times (x - x_0) \Leftrightarrow \\
  & y = - \frac{y_0}{x_0} \times x + y_0
\end{align*}
$$

For the ladder to be placed in a feasible way, point $$B'(a, b)$$ needs to be below
it. This condition translates to the following constrain relation:

$$
\begin{align*}
  & b \leq - \frac{y_0}{x_0} \times a + y_0 \Leftrightarrow \\
  & x_0 b \leq y_0 x_0 - y_0 a = y_0 (x_0 - a) \Leftrightarrow \\
  & y_0 \geq \frac{x_0 b}{x_0 - a}
\end{align*}
$$

The objective function to be minimized is the length of this stair, or the length
of $$AB\Gamma$$ triangle's hypotenuse: $$f(x_0, y_0) = \sqrt{x_0^2 + y_0^2}$$
which is lower bounded due to the constrain by:

$$
f(x_0, y_0) = \sqrt{x_0^2 + y_0^2} \geq \sqrt{x_0^2 + \frac{x_0 b}{x_0 - a}} = f_1(x_0) \quad \forall x_0 > a
$$

Equality is taken when stair "leans" upon the orthogonal block. 

