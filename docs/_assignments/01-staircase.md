---
title: "Minimum length staircase"
permalink: /assignments/staircase
excerpt: "Find a stair of minimum length subject to a constrain."
date: 2017-04-23
---

![Problem image]({{ "/assets/images/01-staircase.png" | absolute_url}} "Staircase above a block."){: .align-left} 
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

$$\begin{align*}
  & y = \frac{y_0 - 0}{0 - x_0} \times (x - x_0) \qquad \Leftrightarrow \\
  & y = - \frac{y_0}{x_0} \times x + y_0
\end{align*}$$  

For the ladder to be placed in a feasible way, point $$B'(a, b)$$ needs to be below
it. This condition translates to the following constrain relation:


$$
  b \leq - \frac{y_0}{x_0} \times a + y_0 \qquad \Leftrightarrow
$$  

$$\begin{equation}
  x_0 b \leq y_0 x_0 - y_0 a = y_0 (x_0 - a) \qquad \Leftrightarrow
\end{equation}$$  

$$\begin{equation}
  y_0 \geq \frac{x_0 b}{x_0 - a}
\end{equation}$$  

The objective function to be minimized is the length of this stair, or the length
of $$AB\Gamma$$ triangle's hypotenuse: $$f(x_0, y_0) = \sqrt{x_0^2 + y_0^2}$$
which is lower bounded due to the constrain $$(2)$$ by:  

$$\begin{equation}
  f(x_0, y_0) = \sqrt{x_0^2 + y_0^2} \geq \sqrt{x_0^2 + \frac{x_0 b}{x_0 - a}} = f_1(x_0) \quad \forall x_0 > a
\end{equation}$$

Equality is taken when stair "leans" upon the orthogonal block. 

Minimizing the objective function $$f_1$$ would need to find the roots of a 3rd-degree
polynomial. So instead we are going to keep the constrain and solve this minimization
problem using **Lagrange multipliers** by noting that the minimum of the constrained problem
is achieved on the boundary of the feasible region, as suggested by inequality $$(3)$$.
The equivalent problem becomes:  

$$\begin{align*}
  & \text{minimize} \quad f(x, y) = \sqrt{x^2 + y^2} \\
  & \text{w.r.t.} \quad x > a, y > b \\
  & \text{s.t.} \quad y x -  a y - b x = 0
\end{align*}$$

The Lagrangian of this problem is: $$L(x, y, \lambda) = \sqrt{x^2 + y^2} - \lambda (yx-ay-bx)$$  
Equating the gradient of $$L$$ to zero, gives us the following system:  

$$
  \nabla_{x,y,\lambda} L = 0 \qquad \Rightarrow
$$

$$\begin{equation}
  yx-ay-bx=0 \qquad (^{\partial}/_{\partial \lambda})
\end{equation}$$

$$\begin{equation}
  \frac{x}{\sqrt{x^2 + y^2}} - \lambda y + \lambda b = 0 \qquad (^{\partial}/_{\partial x})
\end{equation}$$

$$\begin{equation}
  \frac{y}{\sqrt{x^2 + y^2}} - \lambda x + \lambda a = 0 \qquad (^{\partial}/_{\partial y})
\end{equation}$$

Then:

$$\begin{equation}
(5,6) \Leftrightarrow
\begin{Bmatrix}
  x = \lambda \sqrt{x^2 + y^2} (y-b)  \\ 
  y = \lambda \sqrt{x^2 + y^2} (x-a)  \\ 
\end{Bmatrix}
\Rightarrow
\frac{x}{y} = \frac{y-b}{x-a}
\end{equation}$$

$$\begin{equation}
  (4) \Leftrightarrow \frac{y}{x} = \frac{b}{x-a}
\end{equation}$$

$$\begin{align*}
  (7 \times 8) &\Rightarrow (x-a)^2 = b(y-b) =^{(8)} b(\frac{xb}{x-a} - b) = \frac{ab^2}{x-a} \\
  &\Leftrightarrow (x-a)^3 = ab^2 \Rightarrow^{(x > a)}
\end{align*}$$

$$\begin{equation}
  x^* = a + \sqrt[3]{ab^2}
\end{equation}$$

$$\begin{equation}
  (4, 9) \Rightarrow y^* = b + \sqrt[3]{a^2b}
\end{equation}$$

Finally, the **optimal stair** corresponds to the following line:

$$
  y = - \frac{b + \sqrt[3]{a^2b}}{a + \sqrt[3]{ab^2}} x + b + \sqrt[3]{a^2b}
$$
