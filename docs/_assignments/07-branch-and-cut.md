---
title: "Airplane management: Branch-and-Cut"
permalink: /assignments/airplanes
excerpt: "Allocate airplanes to flights and maximize profit."
date: 2017-05-11
---

Given the following stats of a small airplane company, find the optimal airplane
allocation to each flight course for the next week so that the company's profit
is maximized.

| ---
| Flight course | Minimum num of passengers expected | Ticket Price
| -: | :-: | :-: | :-:
| **001** | 320 | 45
| **002** | 170 | 45
| **003** | 190 | 24

_**Unit Transportation Cost** of (Flight Course vs Plane Type)_
{: .text-center .notice--info}

| ---
| | A | B | C
| -: | :-: | :-: | :-:
| **001** | 36 | 39 | -
| **002** | 36 | 39 | 45
| **003** | - | 33 | 42

_**Passenger Capacity** of (Flight Course vs Plane Type)_
{: .text-center .notice--info}

| ---
| | A | B | C
| -: | :-: | :-: | :-:
| **001** | 20 | 15 | -
| **002** | 18 | 13 | 10
| **003** | - | 14 | 8
| **Available Planes** | 15 | 14 | 18

Also, a single plane is allowed to fly up to 3 times per week.

## Representation

Denote $$x_i$$ the number of flights to be allocated at a (flight course, plane type)
combination and $$y_i$$ the number of passengers expected to travel with a
(flight course, plane type) combination. $$x_i$$ and $$y_i$$ are enumerated in
row-major order with respect to the matrices above. The problem then, can be
represented by the following integer linear programming problem:

$$\begin{align*}
  \text{maximize} \quad& 9y_1+6y_2+9y_3+6y_4-9y_6-18y_7 \\
      \text{s.t.} \quad& x_1 + x_3 \leq 45, \\
                       & x_2 + x_4 + x_6 \leq 42, \\
                       & x_5 + x_7 \leq 54, \\
                       & 20x_1 \geq y_1, \quad 15x_2 \geq y_2, \\
                       & 18x_3 \geq y_3, \quad 13x_4 \geq y_4, \quad 10x_5 \geq y_5, \\
                       & 14x_6 \geq y_6, \quad 8x_7 \geq y_7, \\
                       & y_1 + y_2 \geq 320, \\
                       & y_3 + y_4 + y_5 \geq 170, \\
                       & y_6 + y_7 \geq 190 \\
                       & x_i, y_i \geq 0, \quad x_i, y_i \in \mathbb{Z} \quad \forall i \in \{1,...,7\}
\end{align*}$$

## Solution

In order to solve this problem, we are going to use a branch and cut algorithm,
implemented in [this][script] Python script. Please find the description of this
algorithm in its comments.

The solution, found by this script, is presented in the table below. The optimal value
for this solution is **8928** and it has solved for 9 LP relaxation subproblems, using the
**simplex** algorithm, until it found the maximum.

| ---
|**#Flights** | A | B | C | **#Passengers##** | A | B | C
| -: | :-: | :-: | :-: | -: | :-: | :-: | :-:
| **001** | 45 | 29 | -  | **001** | 900 | 435 | -
| **002** | 0 | 0 | 17 | **002** | 0 | 0 | 170
| **003** | - | 13 | 1 | **003** | - | 182 | 8

[script]: https://github.com/tsirif/optimization-auth-course/blob/master/src/branch_and_cut_07.py 
