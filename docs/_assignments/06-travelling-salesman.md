---
title: "Travelling Salesman Problem"
permalink: /assignments/travelling
excerpt: "Find shortest Hamiltonian cycle."
date: 2017-04-23
---

![Problem image]({{ "/assets/images/06-travelling-salesman.png" | absolute_url}} "Graph input."){: .align-left} 

Find the shortest Hamilton cycle on this graph.

## Solution

We are going to use an exhaustive $$O(n!)$$ algorithm implemented in this Python [script][script].
The results from this algorithm coincide with the $$O(n^2)$$ greedy approach described in the lesson.
The shortest cycle is the path $$(4, 5, 3, 6, 1, 2)$$ and has total length of $$192$$.

[script]: https://github.com/tsirif/optimization-auth-course/blob/master/src/travelling_06.py 
