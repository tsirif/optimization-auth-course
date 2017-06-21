---
title: "Prove that problems are equivalent"
permalink: /extras/exercise6
excerpt: "Using slack variables one can create equivalent problems..."
date: 2017-06-20
---

$$\begin{align}
\min_{x} &f(x) \\
\text{s.t. } &g_i(x) \leq 0, \forall i \in \{1,...,m\} \\
             &h_j(x) = 0, \forall j \in \{1,...,l\} \\
\end{align}$$

Prove that the aforementioned optimization problem is equivalent to the following:

$$\begin{align}
\min_{x,s} &f(x) \\
\text{s.t. } &\displaystyle\sum_{i=1}^{m} \left( g_i(x) + s_i^2 \right)^2 +\displaystyle\sum_{j=1}^{l} h_j^2(x) = 0 \text{ ,} \\
\end{align}$$

where $$s_1,...,s_m$$ are extra slack variables.

## Solution

The objective function is exactly the same for both problems ($$(1) \equiv (4)$$).
We are also going to establish equivalence to the set of constraints of these
problems. Starting from the latter:

$$\begin{align*}
(5) \Leftrightarrow \quad &\left\{ \begin{array}{lr}
                                      g_i(x) + s_i^2 = 0&, \forall i \in \{1,...,m\} \\
                                      h_j(x) = 0&, \forall j \in \{1,...,l\} \\
                                    \end{array} \right. \\
\Leftrightarrow \quad &\left\{  \begin{array}{lr}
                                  g_i(x) = -s_i^2 \leq 0&, \forall i \in \{1,...,m\} \\
                                  h_j(x) = 0&, \forall j \in \{1,...,l\} \\
                                \end{array} \right. \\
\Leftrightarrow \quad &\left\{  \begin{array}{lr}
                                  &(2) \\
                                  &(3) \\
                                \end{array} \right. \\
\end{align*}$$

### Corollary (sum of non negatives)

$$\begin{align}
& \text{let } a_i \geq 0, i \in \{1,...,N\}, \text{ then} \\
& \displaystyle\sum_{i=1}^{N} a_i = 0 \Leftrightarrow a_j + \displaystyle\sum_{\substack{i=1 \\ i \neq j }}^{N} a_i = 0 \\
\Leftrightarrow & a_j = - \displaystyle\sum_{\substack{i=1 \\ i \neq j }}^{N} a_i \leq^{(6)} 0 \\
\overset{(6)}{\Leftrightarrow} &a_j = 0, \quad \forall j \in \{1,...,N\} \\
\end{align}$$
