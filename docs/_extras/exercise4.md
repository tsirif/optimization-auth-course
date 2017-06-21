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
\text{min } &f(x)=c^Tx + \frac{1}{2} x^T H x \\
\text{s.t. } &Ax \leq b \\
\end{align*}$$

and

$$\begin{align*}
\text{min } &g(v)=h^Tv + \frac{1}{2} v^T G v \\
\text{s.t. } &v \geq 0 \quad \text{,} \\
\end{align*}$$

where $$G = AH^{-1}A^T$$ and $$h = AH^{-1}c + b$$. Comment on the relation between
Karush-Kuhn-Tucker conditions of these two problems.

## Solution

### First problem

$$\begin{align*}
\text{min } &f(x)=c^Tx + \frac{1}{2} x^T H x \quad, x \in \mathbb{R^n} \\
\text{s.t. } &Ax \leq b \\
\text{or equiv. } &Ax - b \leq 0  \\
\end{align*}$$

The generalized Lagrangian which corresponds to this problem is described by:

$$\begin{align*}
\mathfrak{L}(x, \mu) = &f(x) + \displaystyle\sum_{i=1}^{m} \mu_i (a_i^T x - b_i) = \\
                       &c^T x + \frac{1}{2} x^T H x + \mu^T(Ax - b) \\
\end{align*}$$

**First Order Necessary KKT Conditions**

$$\begin{align}
& c^T + x^T H + \mu^T A = 0 \qquad (\nabla_x \mathfrak{L} = 0) \\
& Ax - b \leq 0 \qquad \text{(primal feasibility)} \\
& \mu \geq 0 \qquad \text{(dual feasibility)} \\
& \mu \odot (Ax - b) = 0 \qquad \text{(complementary slackness),} \\
\end{align}$$

where $$\odot$$ denotes elementwise multiplication.

### Second problem

$$\begin{align*}
\text{min } &g(v)=h^Tv + \frac{1}{2} v^T G v \quad, v \in \mathbb{R^m}\\
\text{s.t. } &v \geq 0 \\
\text{or equiv. } &-v \leq 0  \\
\end{align*}$$

The generalized Lagrangian which corresponds to this problem is described by:

$$\begin{align*}
\mathfrak{L'}(v, \rho) = &g(v) + \displaystyle\sum_{i=1}^{m} \rho_i (- v_i) = \\
                         &h^T v + \frac{1}{2} v^T G v + \rho^T(-v) \\
\end{align*}$$

**First Order Necessary KKT Conditions**

$$\begin{align}
& h^T + v^T G + \rho^T = 0 \qquad (\nabla_x \mathfrak{L'} = 0) \\
& v \geq 0 \qquad \text{(primal feasibility)} \\
& \rho \geq 0 \qquad \text{(dual feasibility)} \\
& \rho \odot (-v) = 0 \qquad \text{(complementary slackness),} \\
\end{align}$$

### Relation between conditions

We are going to manipulate expression $$(5)$$ algebraically, so that we can reveal an
equivalence between the two problems under some bijective transformation.

$$\begin{align}
(5) \Leftrightarrow\quad &(AH^{-1}c + b)^T + v^T AH^{-1}A^T - \rho^T = 0 \\
    \Leftrightarrow\quad &c^T H^{-1} A^T + b^T + v^T A H^{-1} A^T - \rho^T = 0  \\
    \Leftrightarrow\quad &\left( c^T + (b^T - \rho^T)A^{-T}H + v^T A \right) H^{-1} A^T = 0 \\
\text{(}A\text{ must be non-singular)} \Leftrightarrow &c^T + (b^T - \rho^T)A^{-T}H +
v^T A = 0 \\
\end{align}$$

Equation $$(12)$$ shows similarity with equation $$(1)$$. Indeed, under the following
affinic transformation on the problems' variables, the set of all 4 conditions of both
problems are equivalent:

$$\begin{align*}
& v = \mu \\
& \rho = b - Ax \\
\end{align*}$$

Note that matrix $$A$$ needs to be non-singular in order for this transformation to
be a bijections and also respect $$(11) \Leftrightarrow (12)$$.

Indeed:

$$\begin{align*}
& (5) \overset{(12)}{\Leftrightarrow} c^T + (x^TA^T)A^{-T}H + \mu^T A = 0 \Leftrightarrow (1) \\
& (6) \Leftrightarrow \mu \geq 0 \Leftrightarrow (3) \\
& (7) \Leftrightarrow b - Ax \geq 0 \Leftrightarrow (2) \\
& (8) \Leftrightarrow (b - Ax) \odot (-\mu) = 0 \Leftrightarrow (4) \\
\end{align*}$$
