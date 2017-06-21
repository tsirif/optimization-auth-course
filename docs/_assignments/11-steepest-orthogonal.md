---
title: Orthogonality of consecutive steepest directions 
permalink: /assignments/steepest-orthogonal
excerpt: "Prove orthogonality of consecutive search directions"
date: 2017-06-17
---

Prove that for each two consecutive steps in a steepest descend method (with exact
line search), the proposed search directions are orthogonal.

$$\mathbf{d}_k^T \cdot \mathbf{d}_{k+1} = 0$$

## Proof

At each step $$k$$ of the optimization process, we have minimized across $$\lambda$$
for the quantity $$F(\lambda) = f(\mathbf{x}_k + \lambda \mathbf{d}_k)$$ (line
search). Denote the optimal $$\lambda$$ value with $$\lambda_k$$. It is then
necessary that: 


$$\begin{align*}
0 &= \left. \frac{dF(\lambda)}{d\lambda} \right|_{\lambda_k} = \\
\left. \frac{df(\mathbf{x}_k + \lambda \mathbf{d}_k)}{d\lambda} \right|_{\lambda_k} &= \left(\left. \frac{df(\mathbf{x} + \lambda \mathbf{d}_k)}{d(\mathbf{x}_k + \lambda \mathbf{d}_k)} \right|_{\lambda_k}\right) \cdot \left. \frac{d(\mathbf{x}_k + \lambda \mathbf{d}_k)}{d\lambda} \right|_{\lambda_k} = \\
\nabla f(\mathbf{x}_{k+1}) \cdot \mathbf{d}_k &\Rightarrow \mathbf{d}_{k+1}^T \cdot \mathbf{d}_k = 0 \text{ ,}\\
\end{align*}$$


since we have shown in the [previous exercise]({{ "/assignments/steepest-euclidean" | absolute_url}}) that
$$\mathbf{d}_k$$ is parallel to $$-\nabla f(\mathbf{x}_k)$$.
