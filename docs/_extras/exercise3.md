---
title: "Play with quadratic form"
permalink: /extras/exercise3
excerpt: "A fact about quadratic functions"
date: 2017-06-20
---

Let $$f$$ be the following quadratic function:

$$
f(x) = \frac{1}{2}x^TQx + p^Tx, x \in \mathbb{R^n}
$$

1. Calculate point $$x_c \in \mathbb{R^n}$$ which is defined as the point which
   minimizes function $$f(x)$$ in the direction $$d = -\nabla f(x)$$, passing through
   the space origin.
2. Show that function $$f(x)$$ is strictly decreasing in the line section $$x_c \to
   x_*$$, where $$x_*$$ is the point which minimizes $$f(x)$$.

## Solution

We assume that matrix $$Q$$ is positive definite, so that that $$f$$ has a
minimizer as the problem's expression supports.

### Subproblem 1

$$\begin{align}
  & \nabla f(x) = x^T Q + p^T  \\
  & \nabla^2 f(x) = Q > 0  \implies f \text{ is strictly convex} \\
\end{align}$$

Since direction passes through the space origin, $$\exists \lambda_0 > 0$$:

$$\begin{align}
x + \lambda_0 d = 0 \Leftrightarrow d = -\frac{1}{\lambda_0} x
\end{align}$$

So we would like to minimize:

$$\begin{align*}
& \min_{\lambda} f(x + \lambda d) = f(x - \lambda x) = f((1-\lambda)x), \lambda > 0 \\
& \frac{df((1-\lambda)x)}{d\lambda} = \nabla f((1-\lambda)x) \cdot (-x) = \\
& \left( (1-\lambda)x^T Q + p^T \right) (-x) = -(1-\lambda)x^TQx - p^Tx = 0 \Rightarrow \\
& 1 - \lambda_c = - \frac{p^Tx}{x^TQx}  \overset{(3)}{\Rightarrow} x_c =
(1-\lambda_c) x =  - \frac{p^Tx}{x^TQx}x
\end{align*}$$

### Subproblem 2

$$\begin{align*}
& \nabla f(x_*) = 0 \overset{(1)}{\Rightarrow} x_*^TQ + p^T = 0 \Leftrightarrow x_* =
-Q^{-1}p \\
& \\
& x_c \to x_*: x = (1-\lambda)x_c + \lambda x_* \quad , 0 \leq \lambda \leq 1 \\
& \\
& \min_{\lambda} f\left((1-\lambda)x_c + \lambda x_*\right) \qquad \Rightarrow \\
& \\
& \frac{df\left((1-\lambda)x_c + \lambda x_*\right)}{d\lambda} = 
\nabla f\left((1-\lambda)x_c + \lambda x_*\right) \cdot (x_* - x_c) = \\
& \left[ \left((1-\lambda)x_c + \lambda x_*\right)^T Q + p^T \right] (x_* - x_c) = \\
& (1 - \lambda) x_c^T Q x_* - (1 - \lambda) x_c^T Q x_c + \lambda x_*^T Q x_* - \lambda x_*^T Q x_c
+ p^T x_* - p^T x_c = \\
& -(1 - \lambda) x_c^T Q Q^{-1}p - (1 - \lambda) x_c^T Q x_c + \lambda p^T Q^{-1} Q Q^{-1} p
+ \lambda p^T Q^{-1} Q x_c - p^T Q^{-1} p - p^T x_c = \\
& -(1 - \lambda)(x_c^T Q Q^{-1} p + p^Tx_c) - (1 - \lambda)p^TQ^{-1}p - (1 - \lambda) x_c^T Q x_c = \\
& - (1 - \lambda)(p^T + x_c^TQ)(Q^{-1}p + x_c) = \\ 
& - (1 - \lambda)(p^TQ^{-1} + x_c^T)Q(Q^{-1}p + x_c) = \\ 
& - (1 - \lambda)(Q^{-1}p + x_c)^TQ(Q^{-1}p + x_c) < 0 \quad \forall \lambda \in (0,
1) \\ 
\end{align*}$$

Thus, in line section $$x_c \to x_*$$, function $$f(x)$$ is strictly decreasing.
