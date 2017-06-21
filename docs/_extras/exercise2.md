---
title: "Prove that matrix is positive definite"
permalink: /extras/exercise2
excerpt: "H is positive-definite."
date: 2017-06-20
---

Given function $$f(x), x \in \mathbb{R^n}$$ and its gradient $$g = \nabla f(x)$$,
prove that matrix $$H$$ is positive definite, if vector $$p \in \mathbb{R^n}$$
defines a descending direction.

$$
H = I_n - \frac{pp^T}{p^Tg} - \frac{gg^T}{g^Tg} \text{ , } I_n \text{ is identity
matrix}
$$

## Solution

By definition:

$$\begin{align}
& z^T(I_n - \frac{pp^T}{p^Tg} - \frac{gg^T}{g^Tg})z = \\
& z^T I_n z - \frac{(z^T p)(p^T z)}{p^Tg} - \frac{(z^T g)(g^T z)}{g^Tg} = \\
& ||z||^2 - \frac{|z^T p|^2}{p^Tg} - \frac{|z^T g|^2}{||g||^2} \geq
\quad \text{(Cauchy-Schwarz)} \\
& ||z||^2 - \frac{|z^T p|^2}{p^Tg} - \frac{||z||^2 ||g||^2}{||g||^2} = \\
& - \frac{|z^T p|^2}{p^Tg} \geq 0 \quad (p^Tg < 0 \text{ - descending})
\end{align}$$

Equality at $$(3)$$ is satisfied for colinear $$z$$ and $$g$$ and equality at $$(5)$$
for orthogonal $$z$$ and $$p$$. As $$p$$ is a descending direction, these conditions
cannot be simultaneously satisfied. Thus:

$$
z^THz > 0 \quad \forall z \neq 0 \text{ ,}
$$

hence $$H$$ is positive definite.
