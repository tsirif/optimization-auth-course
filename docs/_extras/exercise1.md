---
title: "Special case of Cauchy-Schwarz"
permalink: /extras/exercise1
excerpt: "Find critical points and characterize them."
date: 2017-06-20
---

Calculate and characterize the critical points of the following function:

$$
f(x_1, x_2, x_3) = \left( \displaystyle\sum_{i=1}^{3} a_{i}^{2} \right)
                   \left( \displaystyle\sum_{i=1}^{3} x_{i}^{2} \right) -
                   \left( \displaystyle\sum_{i=1}^{3} a_{i}x_{i} \right)^2 \text{ ,}
$$

where $$a_i$$, $$i=1,2,3$$ are constants.

## Solution

$$\begin{align}
  \nabla f = &\begin{bmatrix}
                \left( \displaystyle\sum_{i=1}^{3} a_{i}^{2} \right) 2 x_1 - 2 \left( \displaystyle\sum_{i=1}^{3} a_{i}x_{i} \right) a_1 \\
                \left( \displaystyle\sum_{i=1}^{3} a_{i}^{2} \right) 2 x_2 - 2 \left( \displaystyle\sum_{i=1}^{3} a_{i}x_{i} \right) a_2 \\
                \left( \displaystyle\sum_{i=1}^{3} a_{i}^{2} \right) 2 x_3 - 2 \left( \displaystyle\sum_{i=1}^{3} a_{i}x_{i} \right) a_3 \\
              \end{bmatrix}^{T} = 0 \qquad \Rightarrow \\
 & \begin{Bmatrix}
     \left( \displaystyle\sum_{i=1}^{3} a_{i}^{2} \right) x_1 = \left( \displaystyle\sum_{i=1}^{3} a_{i}x_{i} \right) a_1 \\
     \left( \displaystyle\sum_{i=1}^{3} a_{i}^{2} \right) x_2 = \left( \displaystyle\sum_{i=1}^{3} a_{i}x_{i} \right) a_2 \\
     \left( \displaystyle\sum_{i=1}^{3} a_{i}^{2} \right) x_3 = \left( \displaystyle\sum_{i=1}^{3} a_{i}x_{i} \right) a_3 \\
   \end{Bmatrix} \qquad \Rightarrow \text{not all } a_i \text{ are zero} \\
 & \begin{Bmatrix}
     x_1 a_2 = x_2 a_1 \\
     x_2 a_3 = x_3 a_2 \\
     x_3 a_1 = x_1 a_3 \\
   \end{Bmatrix} \text{ or } \left\{ \displaystyle\sum_{i=1}^{3} a_{i}x_{i} = 0 \right\} \qquad \Rightarrow \\
 & \begin{Bmatrix}
     x_1 = \lambda a_1 \\
     x_2 = \lambda a_2 \\
     x_3 = \lambda a_3 \\
   \end{Bmatrix} \text{ or } \left\{ x_i = 0, i=1,2,3 \right\} \quad \text{(due to (1))} \qquad \Leftrightarrow \\
 & \begin{Bmatrix}
     x_1 = \lambda a_1 \\
     x_2 = \lambda a_2 \\
     x_3 = \lambda a_3 \\
   \end{Bmatrix} \qquad \lambda \in \mathbb{R} \\ 
\end{align}$$

Relation $$(3)$$ is obtained by multiplying per parts the equations in relation
$$(2)$$. We infer that all critical points lie on the line which is colinear to
vector $$\vec{a}$$.

$$\begin{align}
  \nabla^2 f = &\begin{bmatrix}
                 2\left( \displaystyle\sum_{i=1}^{3} a_{i}^{2} \right) - 2a_1^2 & -2a_1 a_2 & -2a_1 a_3 \\
                 -2a_1 a_2 & 2\left( \displaystyle\sum_{i=1}^{3} a_{i}^{2} \right) - 2a_2^2 & -2a_2 a_3 \\
                 -2a_1 a_3 & -2a_2 a_3 & 2\left( \displaystyle\sum_{i=1}^{3} a_{i}^{2} \right) - 2a_3^2  \\
               \end{bmatrix} = \\
               &\begin{bmatrix}
                 2(a_2^2 + a_3^2) & -2a_1 a_2 & -2a_3 a_1 \\
                 -2a_1 a_2 & 2(a_3^2 + a_1^2) & -2a_2 a_3 \\
                 -2a_3 a_1 & -2a_2 a_3 & 2(a_1^2 + a_2^2) \\
               \end{bmatrix} \geq 0 \quad \forall \vec{x}
\end{align}$$

Also, we can see that:

$$\begin{align}
  \nabla^{(n)} f = 0 \quad \forall n > 2
\end{align}$$

This means that function $$f$$ is convex everywhere, except a direction in which it
is linear. Testing for direction $$\vec{x} = \lambda \vec{a}$$, shows that $$\nabla^2
f \cdot \lambda \vec{a} = 0$$. Also, $$(8)$$ shows that in the linear direction, $$f$$
should also be constant. Indeed, testing for the critical line of points in the original
function, we get:

$$
f(\lambda a_1, \lambda a_2, \lambda a_3) =
                   \left( \displaystyle\sum_{i=1}^{3} a_{i}^{2} \right)
                   \lambda^2 \left( \displaystyle\sum_{i=1}^{3} a_{i}^{2} \right) -
                   \left( \displaystyle\sum_{i=1}^{3} a_{i}\lambda a_{i} \right)^2 =
                   0 \quad \forall \lambda \in \mathbb{R}
$$

Thus, we infer that $$\vec{x} = \lambda \vec{a} \quad \forall \lambda$$
corresponds to global minimizers.

### Proving (7)

$$\begin{align*}
&\begin{vmatrix}
  a_2^2 + a_3^2
\end{vmatrix} > 0 \\
&\begin{vmatrix}
  a_2^2 + a_3^2 & -a_1 a_2 \\
  -a_1 a_2 & a_1^2 + a_3^2 \\
\end{vmatrix} = (a_2^2 + a_3^2)(a_1^2 + a_3^2) - (a_1 a_2)^2 = (a_2 a_3)^2 + (a_3 a_1)^2 + a_3^4 > 0 \\
&\begin{vmatrix}
  a_2^2 + a_3^2 & -a_1 a_2 & -a_3 a_1 \\
  -a_1 a_2 & a_3^2 + a_1^2 & -a_2 a_3 \\
  -a_3 a_1 & -a_2 a_3 & a_1^2 + a_2^2 \\
\end{vmatrix} = (a_2^2 + a_3^2) \left( (a_1 a_2)^2 + (a_3 a_1)^2 + a_1^4 \right) + \\
               & a_1 a_2 (-a_1 a_2^3 -a_1^3 a_2 -a_1 a_2 a_3^2) - a_3 a_1 (a_1 a_2^2
               a_3 + a_3^3 a_1 + a_3 a_1^3) = \\
               & (a_1 a_2^2)^2 + 2(a_1 a_2 a_3)^2 + (a_1^2 a_2)^2 + (a_3^2 a_1)^2 +
               (a_3 a_1^2)^2 \\
               & -(a_1 a_2^2)^2 - (a_1^2 a_2)^2 - (a_1 a_2 a_3)^2 - (a_1 a_2 a_3)^2
               - (a_3 a_1^2)^2 - (a_3^2 a_1)^2 = 0 \\
\end{align*}$$
