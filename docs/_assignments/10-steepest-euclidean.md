---
title: Steepest direction for the Euclidean norm
permalink: /assignments/steepest-euclidean
excerpt: "Which is the steepest direction for the Euclidean norm?"
date: 2017-06-17
---

Prove that for each non-critical point in the domain of a function, $$f$$, the
direction, in which the maximum rate of reduction in the function's value is observed,
corresponds to the vector defined by the opposite to the function's gradient to that
point. Candidate directions are chosen to have the same magnitude in Euclidean norm,
$$\mathcal{L}^2$$.

## Solution

For each point $$\mathbf{x}$$, we are asking to determine the direction, $$\mathbf{u}$$, which leads to the
maximum rate of reduction of the quantity $$F(\lambda) = f(\mathbf{x} + \lambda \mathbf{u})$$. In other
words:

$$\begin{align*}
  \min_{\mathbf{u}} \quad& \frac{df(\mathbf{x})}{d\lambda} = \left. \frac{dF}{d\lambda} \right|_{\lambda = 0} = \\
  & \left(\left. \frac{df(\mathbf{x} + \lambda \mathbf{u})}{d(\mathbf{x} + \lambda \mathbf{u})} \right|_{\lambda = 0}\right) \cdot \left. \frac{d(\mathbf{x} + \lambda \mathbf{u})}{d\lambda} \right|_{\lambda = 0} = 
  \nabla f(\mathbf{x}) \cdot \mathbf{u} \\
  \text{s.t.} \quad& ||\mathbf{u}||_2 = 1 \text{ ,} \\
\end{align*}$$

where the gradient is taken to be a row-vector.

Using Cauchy-Schwarz inequality:

$$
\nabla f(\mathbf{x}) \cdot \mathbf{u} \geq -||\nabla f(\mathbf{x})||_2 \cdot
||\mathbf{u}||_2 = -||\nabla f(\mathbf{x})||_2 \text{ ,}
$$

where equality is taken for antiparallel vectors, so:

$$
\mathbf{u} = -\frac{\nabla f(\mathbf{x})}{||\nabla f(\mathbf{x})||_2}
$$
