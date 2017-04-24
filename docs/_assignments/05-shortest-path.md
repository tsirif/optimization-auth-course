---
title: "Shortest Path Problem"
permalink: /assignments/shortest-path
excerpt: "Find shortest paths between vertices of a directed graph."
date: 2017-04-23
---

![Problem image]({{ "/assets/images/05-shortest-path.png" | absolute_url}} "Graph input."){: .align-center} 

Find the shortest path from vertex $$A$$ to vertex $$E$$. What are the shortest paths from $$A$$
to each other vertices ($$B$$, $$\Gamma$$, $$\Delta$$)?

## Solution

We are going to use **Dijkstra's** [algorithm][Dijkstra]. This Python [script][script]
implements the algorithm. Code's documentation serves as explanation to the algorithm.

### Results

```python
Path from 'A' to 'B':
['A', 'C', 'B']
Total Cost:
3

Path from 'A' to 'C':
['A', 'C']
Total Cost:
1

Path from 'A' to 'D':
['A', 'C', 'B', 'D']
Total Cost:
4

Path from 'A' to 'E':
['A', 'C', 'B', 'E']
Total Cost:
5
```

[script]: https://github.com/tsirif/optimization-auth-course/blob/master/src/shortest_path_05.py 
[Dijkstra]: https://en.wikipedia.org/wiki/Dijkstra%27s_algorithm
