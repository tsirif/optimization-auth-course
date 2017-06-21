---
title: "Minimize sum of univariate functions on circle of 1-norm"
permalink: /extras/exercise5
excerpt: "Prove existence of some k s.t..."
date: 2017-06-20
---

We have the following optimization problem:

$$\begin{align*}
\text{min } &f(x) = \displaystyle\sum_{i=1}^{N} f_i(x_i) \\
\text{s.t. }&\displaystyle\sum_{i=1}^{N} x_i = 1 \\
            &x_i \geq 0, \quad \forall i \in \{1,...,N\} \\
\end{align*}$$

Assume that point $$x^* = [x^*_1,...,x^*_N]^T$$ is the solution of the problem above.
Show that there exists some $$k$$ such that:

$$
f_i'(x^*_i) \geq k \land (f_i'(x^*_i) - k)x^*_i = 0, \forall i \in \{1,...,N\}
$$

## Solution 

By simple application of the necessary KKT conditions on this specific problem, we
can derive the requested relations:

**Lagrangian**:
$$
\mathfrak{L}(x, k, \mu) = \displaystyle\sum_{i=1}^{N} f_i(x_i) + k ( 1 - \displaystyle\sum_{i=1}^{N} x_i ) -\displaystyle\sum_{i=1}^{N} \mu_i x_i
$$

$$\begin{align}
& \frac{\partial\mathfrak{L}}{\partial x_i} = f_i'(x_i) - k - \mu_i \\
& \nabla_x \mathfrak{L}(x^*, k^*, \mu^*) = 0 \\
\overset{(1)}{\Rightarrow}\quad & f_i'(x^*_i) - k^* = \mu^*_i \quad \forall i \in \{1,...,N\} \\
\end{align}$$

By the *dual feasibility* and *complementary slackness* conditions, we then
immediately have from $$(3)$$:

$$\begin{align*}
\text{(dual feasibility) } m^*_i \geq 0 \overset{(3)}{\Rightarrow}\quad &f_i'(x^*_i) \geq k^* \\
\text{(compl. slackness) } m^*_i (-x^*_i) = 0 \overset{(3)}{\Rightarrow}\quad &(f_i'(x^*_i) - k^*)x^*_i = 0, \quad \forall i \in \{1,...,N\} \\
\end{align*}$$
