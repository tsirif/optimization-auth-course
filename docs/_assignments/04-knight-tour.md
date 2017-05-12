---
title: "Knight's tour"
permalink: /assignments/knight-tour
excerpt: "Modelling a problem with graphs."
date: 2017-04-23
---

![Problem image]({{ "/assets/images/04-knight-tour.png" | absolute_url}} "A 4x4 chessboard"){: .align-left} 
Model the knight's tour problem. What is the equivalent problem in graph optimization?

## Solution

The knight's tour problem can be modelled by establishing an isomorphic (one-to-one)
relation to a properly constructed graph.

Such a model can be a graph whose vertices correspond one-to-one to a chessboard's
squares. An edge between a pair of vertices, in such a model, exists if and only if
there exists a valid knight move from/to the squares corresponding to a candidate
pair of vertices.

Given a starting square (vertex in graph analogue), the knight's tour problem
corresponds to **finding a Hamiltonian path** in the graph model starting from the
initial vertex. A Hamiltonian path is a sequence of vertices, such that:

  1. Each vertex of a graph is **contained exactly once** in the sequence,
  2. Two consecutive vertices are associated by an edge.

For a $$4 \times 4$$ chessboard, such a model can be described by the following
definitions in Python language (see [here][script] for the full script):

First of all, we must choose symbols for the chessboard's squares. We can choose
to enumerate row-wise squares, associating a unique number to each square, as follows:

### Vertices

$$
\begin{array}{c|c|c|c}
  0 & 1 & 2 & 3 \\ \hline
  4 & 5 & 6 & 7 \\ \hline
  8 & 9 & 10& 11 \\ \hline
  12 & 13 & 14 & 15
\end{array}
$$

### Edges

```python
graph[0] = [6, 9]
graph[1] = [7, 8, 10]
graph[2] = [4, 9, 11]
graph[3] = [5, 10]
graph[4] = [2, 10, 13]
graph[5] = [3, 11, 12, 14]
graph[6] = [0, 8, 13, 15]
graph[7] = [1, 9, 14]
graph[8] = [1, 6, 14]
graph[9] = [0, 2, 7, 15]
graph[10] = [1, 3, 4, 12]
graph[11] = [2, 5, 13]
graph[12] = [5, 10]
graph[13] = [4, 6, 11]
graph[14] = [5, 7, 8]
graph[15] = [6, 9]
```

The *naive* $$O(n 8^n)$$ algorithm provided in the [script][script] tells that there is
no solution for the $$4 \times 4$$ knight's tour problem.

[script]: https://github.com/tsirif/optimization-auth-course/blob/master/src/knight_tour_04.py 
