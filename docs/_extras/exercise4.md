---
title: "Minimize quadratics with linear constraints"
permalink: /extras/exercise4
excerpt: "Comment on KKT conditions of 2 problems."
date: 2017-06-20
---

Let vectors $$c \in \mathbb{R^n}$$, $$b \in \mathbb{R^m}$$ vectors, matrix
$$A \in \mathbb{R^{mxn}}$$, positive definite matrix $$H \in \mathbb{R^{nxn}}$$ and
the following constrained optimization problems:

$$\begin{align*}
& \text{min } f(x)=c^Tx + \frac{1}{2} x^T H x \\
& \text{s.t. } Ax \leq b \\
\end{align*}$$

and

$$\begin{align*}
& \text{min } g(v)=h^Tv + \frac{1}{2} v^T G v \\
& \text{s.t. } v \geq 0 \quad \text{,} \\
\end{align*}$$

where $$G = AH^{-1}A^T$$ and $$h = AH^{-1}c + b$$. Comment on the relation between
Karush-Kuhn-Tucker conditions of these two problems.

## Solution

