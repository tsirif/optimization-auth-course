#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import absolute_import

from itertools import zip_longest
from collections import OrderedDict, defaultdict as dd

import numpy as np
import matplotlib.pyplot as plt
from matplotlib import animation
from matplotlib.ticker import MaxNLocator

from optimize import (Newton, Fibonacci, GoldenSection, ParabolicInterpolation,
                      CubicInterpolation, Dichotomous)


animation.rcParams['savefig.dpi'] = 120

class TrajectoryAnimation(animation.FuncAnimation):

    def __init__(self, *paths, x=None, coeff=None, fig=None, axes=None, labels=[],
                 frames=None, interval=600, repeat_delay=20, blit=True, **kwargs):
        self.fig = fig
        self.axes = axes
        self.paths = paths
        self.x = x

        if frames is None:
            frames = max(path.shape[1] for path in paths)
        frames *= 2
        frames += 2

        self.parabola = [axis.plot([], [], '-', color='r', lw=0.5, alpha=0.8)[0]
                         for axis, label in zip_longest(axes, labels)]
        self.minima = [axis.plot([], [], 's', color='r', alpha=0.8)[0]
                       for axis in axes]
        self.lines = [axis.plot([], [], label=label, lw=2)[0]
                      for axis, label in zip_longest(axes, labels)]
        self.points = [axis.plot([], [], 'o', color=line.get_color())[0]
                       for axis, line in zip_longest(axes, self.lines)]

        super(TrajectoryAnimation, self).__init__(fig, self.animate, init_func=self.init_anim,
                                                  frames=frames, interval=interval, blit=blit,
                                                  repeat_delay=repeat_delay, **kwargs)

    def init_anim(self):
        for line, point, parabola, minimum in zip(self.lines, self.points,
                                                  self.parabola, self.minima):
            parabola.set_data([], [])
            minimum.set_data([], [])
            line.set_data([], [])
            point.set_data([], [])
        return self.lines + self.points + self.parabola + self.minima

    def animate(self, i):
        for line, point, parabola, minimum, path in zip(self.lines, self.points,
                                                        self.parabola, self.minima, self.paths):
            it = i // 2
            if it >= path.shape[1]:
                continue
            if i % 2 == 0:
                line.set_data(*path[0:2, :it+1])
                point.set_data(*path[0:2, it:it+1])
            else:
                if it >= path.shape[1] - 1:
                    continue
                para = lambda x: path[2, it]*x**2 + path[3, it]*x + path[4, it]
                mini = -path[3, it] / (2*path[2, it])
                parabola.set_data(self.x, para(self.x))
                minimum.set_data(mini, para(mini))

        return self.lines + self.points + self.parabola + self.minima


class IntervalAnimation(animation.FuncAnimation):

    def __init__(self, *paths, labels=[], fig=None, axes=None, frames=None,
                 interval=600, repeat_delay=20, blit=True, **kwargs):
        self.fig = fig
        self.axes = axes
        self.paths = paths

        if frames is None:
            frames = max(path.shape[1] for path in paths)
        frames *= 2
        frames += 2

        self.intervals = [axis.plot([], [], 'D-', color='m', label=label)[0]
                          for axis, label in zip_longest(axes, labels)]
        self.left_descent = [axis.plot([], [], lw=2)[0]
                             for axis in axes]
        self.lselected = [[] for line in self.left_descent]
        self.right_descent = [axis.plot([], [], lw=2)[0]
                              for axis in axes]
        self.rselected = [[] for line in self.right_descent]
        self.next_points = [axis.plot([], [], 's-.', color='y')[0]
                            for axis in axes]

        super(IntervalAnimation, self).__init__(fig, self.animate, init_func=self.init_anim,
                                                frames=frames, interval=interval, blit=blit,
                                                repeat_delay=repeat_delay, **kwargs)

    def init_anim(self):
        iteranim = zip(self.left_descent, self.lselected,
                       self.right_descent, self.rselected,
                       self.next_points, self.intervals)
        for lline, ls, rline, rs, next_point, interval in iteranim:
            lline.set_data([], [])
            ls.clear()
            rline.set_data([], [])
            rs.clear()
            next_point.set_data([], [])
            interval.set_data([], [])
        return self.left_descent + self.right_descent + self.next_points + self.intervals

    def animate(self, i):
        iteranim = zip(self.left_descent, self.lselected,
                       self.right_descent, self.rselected,
                       self.next_points, self.intervals, self.paths)
        it = i // 2
        for lline, ls, rline, rs, next_point, interval, path in iteranim:
            if it >= path.shape[1]:
                continue
            if i % 2 == 1:
                if it < path.shape[1] - 1:
                    if path[0, it] == path[0, it+1]:
                        if path.shape[0] == 8:
                            if not rs:
                                rs.append([path[3, it], path[3+4, it]])
                            rs.append([path[3, it+1], path[3+4, it+1]])
                        else:
                            if not rs:
                                rs.append([path[1, it], path[3, it]])
                            rs.append([path[1, it+1], path[3, it+1]])
                            ax, ay = (path[1, it+1], path[3, it+1])
                    else:
                        if path.shape[0] == 8:
                            if not ls:
                                ls.append([path[0, it], path[4, it]])
                            ls.append([path[0, it+1], path[4, it+1]])
                        else:
                            if not ls:
                                ls.append([path[0, it], path[2, it]])
                            ls.append([path[0, it+1], path[2, it+1]])
                            ax, ay = (path[0, it+1], path[2, it+1])
                else:
                    if path.shape[0] == 8:
                        ls.append([sum(path[[0,3], it])/2, sum(path[[4,7], it])/2])
                    else:
                        ls.append([sum(path[0:2, it])/2, sum(path[2:, it])/2])
                        ax, ay = [sum(path[0:2, it])/2, sum(path[2:, it])/2]

                if path.shape[0] == 8:
                    next_point.set_data(path[1:3, it], path[5:7, it])
                else:
                    next_point.set_data([ax], [ay])
            else:
                # Draw left and right descent lines
                if ls:
                    track = np.asarray(ls).T
                    lline.set_data(*track)
                if rs:
                    track = np.asarray(rs).T
                    rline.set_data(*track)
                # Draw interval
                if path.shape[0] == 8:
                    interval.set_data(path[[0, 3], it], path[[4, 7], it])
                else:
                    interval.set_data(path[[0, 1], it], path[[2, 3], it])
        return self.left_descent + self.right_descent + self.next_points + self.intervals


#  Setup test functions  #
x = []
y = []
minimum = []
xlims = []
# Function 1 : x**3 - x + 2
f00 = lambda x: x**3 - x + 2
f01 = lambda x: 3*x**2 - 1
f02 = lambda x: 6*x


#  Find optimals  #
def minimize_cubic(c):
    D = (2*c[1])**2 - 4*(3*c[0])*c[2]
    return (-2*c[1] + np.sqrt(D)) / (6*c[0])


x0_opt = minimize_cubic([1, 0, -1, 2])
x0min, x0max, x0step = -0.5, 2.5, .1
xlims.append((x0min, x0max))
x0 = np.arange(x0min, x0max + x0step, x0step)
x.append(x0)
y0 = f00(x0)
y.append(y0)
y0_opt = f00(x0_opt)
minimum0 = np.array([[x0_opt], [y0_opt]])
minimum.append(minimum0)

# Function 2
x1_opt = -np.log(2)/2
f10 = lambda x: np.e**(x + 3*(x-x1_opt) -0.5) + np.e**(x - 3*(x-x1_opt) -0.5) + np.e**(-x-0.5)
f11 = lambda x: 4*np.e**(x + 3*(x-x1_opt) -0.5) - 2*np.e**(x - 3*(x-x1_opt) -0.5) - np.e**(-x-0.5)
f12 = lambda x: 16*np.e**(x + 3*(x-x1_opt) -0.5) + 4*np.e**(x - 3*(x-x1_opt) -0.5) + np.e**(-x-0.5)
y1_opt = f10(x1_opt)
minimum1 = np.array([[x1_opt], [y1_opt]])
minimum.append(minimum1)
x1min, x1max, x1step = -1.2, 0.6, 0.01
xlims.append((x1min, x1max))
x1 = np.arange(x1min, x1max + x1step, x1step)
x.append(x1)
y1 = f10(x1)
y.append(y1)

#  Execute Methods  #
results0 = {}
histories0 = OrderedDict()
results1 = {}
histories1 = OrderedDict()
optimizers = [Newton, Newton, Fibonacci, GoldenSection, ParabolicInterpolation,
              CubicInterpolation, Dichotomous]
methods = list(map(lambda opti_type: opti_type.__name__, optimizers))

parabolas0 = {}
parabolas1 = {}
opti = Newton(delta=0.05)
results0['Newton'] = opti(f00, f01, f02, start=0.05)
histories0['Newton'] = opti.history
parabolas0['Newton'] = opti.parabola
opti.backtracking = True
results0['dampedNewton'] = opti(f00, f01, f02, start=0.05)
histories0['dampedNewton'] = opti.history
parabolas0['dampedNewton'] = opti.parabola
opti.delta = 1e-2
opti.backtracking = False
results1['Newton'] = opti(f10, f11, f12, start=-1.0)
histories1['Newton'] = opti.history
parabolas1['Newton'] = opti.parabola
opti.backtracking = True
results1['dampedNewton'] = opti(f10, f11, f12, start=-1.0)
histories1['dampedNewton'] = opti.history
parabolas1['dampedNewton'] = opti.parabola
parabolas = [parabolas0, parabolas1]
for opti_type in optimizers[2:]:
    opti = opti_type(delta=0.05)
    results0[opti_type.__name__] = opti(f00, f01, f02, start=[0.0, 2.0])
    histories0[opti_type.__name__] = opti.history
    opti.delta = 1e-2
    results1[opti_type.__name__] = opti(f10, f11, f12, start=[-1.0, 0.4])
    histories1[opti_type.__name__] = opti.history

paths0 = [np.concatenate([hist, f00(hist)], axis=0) for hist in histories0.values()]
paths1 = [np.concatenate([hist, f10(hist)], axis=0) for hist in histories1.values()]
paths = [paths0, paths1]

anims = dd(list)
titles = ['$x^3 - x + 2$',
          '$e^{x+3(x+0.5ln(2))-0.5} + e^{x-3(x+0.5ln(2))-0.5} + e^{-x-0.5}$']
# Plot function
for p in range(2):
    fig, ax = plt.subplots(nrows=1, ncols=2, figsize=(10, 5))
    fig.suptitle(titles[p])
    for axis in ax:
        axis.plot(x[p], y[p])
        axis.plot(*minimum[p], 'r*', markersize=10)
        axis.set_xlim(xlims[p])
        axis.set_xlabel('$x$')
        axis.set_ylabel('$y$')
    newton_paths = (np.concatenate([paths[p][0], parabolas[p]['Newton']]),
                    np.concatenate([paths[p][1], parabolas[p]['dampedNewton']]))
    newton_labels = ['Newton', 'damped Newton']
    anim = TrajectoryAnimation(*newton_paths, x=x[p], fig=fig, axes=ax, labels=newton_labels)
    for axis in ax:
        axis.legend(loc='upper left')
    anims['Newton'].append(anim.to_html5_video())

for i in range(2, len(methods)):
    fig, ax = plt.subplots(nrows=1, ncols=2, figsize=(10, 5))
    ps = []
    for j in range(2):
        ax[j].set_title(titles[j])
        ax[j].plot(x[j], y[j])
        ax[j].plot(*minimum[j], 'r*', markersize=10)
        ax[j].set_xlim(xlims[j])
        ax[j].set_xlabel('$x$')
        ax[j].set_ylabel('$y$')
        ps.append(paths[j][i])
    anim = IntervalAnimation(*ps, labels=(2*methods[i:i+1]), fig=fig, axes=ax)
    for axis in ax:
        axis.legend(loc='upper left')
    anims[methods[i]].append(anim.to_html5_video())

#  plt.show()
# Create report...
intro = \
r"""---
title: "Univariate optimization"
permalink: /assignments/minimize-2
excerpt: "Perform univariate and unimodal function optimization."
date: 2017-05-18
---

Minimize $$f(x) = x^3 - x + 2$$ with minimizer accuracy $$0.05$$ within
the interval $$[0,2]$$.

Various algorithms, which perform univariate optimization, were implemented in this
exercise. The methods can be found in [**optimize.py**][opti] Python script, while the
code for experiments and visualization in [results.py][res]. True minimum is achieved
at $$x \approx {minimum[0][0]:.4f}$$ with value $$f(x) \approx {minimum[1][0]:.4f}$$. For each
method, we also present a demonstration with a second function.

"""

golden_section = \
r"""## Zeroth order methods (gradient-free)

### Golden section search

A function must be strictly unimodal in $$[a, b]$$, in order to be
minimized by the golden section method. At each step, the trust interval is "cut" twice
in golden sections and then it is contracted so that it still contains the local
minimum. The useful property of golden ratio, $$\varphi = \frac{1 + \sqrt{5}}{2} \approx 1.618$$,
is that an interval $$d_0$$ which is split to $$d_1 + d_2$$ by $$d_0 / d_1 =
\varphi$$, has also $$d_1 / d_2 = \varphi$$. Consequently, the initial interval is
contracted by a constant ratio, $$\varphi^{-1} = \varphi - 1$$, at each step and we
can also evaluate a single new trial point at each next step (instead of two).

"""

rest_report = \
r"""```python
def contract(self, a, x, y, b):  # a < x < y < b
    d = (self.phi - 1) * (y - a)

    if self.f0(x) < self.f0(y):
        return (a, y - d, x, y)
    else:
        return (x, y, x + d, b)
```

{anims[GoldenSection][0]}

After {results[GoldenSection][0]} iterations, it reaches $$x = {results[GoldenSection][1]:.4f}$$
with value $$f(x) = {results[GoldenSection][2]:.4f}$$.

### Fibonacci search

Using fibonacci search relies on the fact that the ratio of two consecutive fibonacci
numbers approximates $$\varphi$$. As with the golden section method, the function must
be strictly unimodal in the initial interval, which is always contracted so that it
contains the minimum.

```python
def contract(self, a, x, y, b):  # a < x < y < b
    d = y - x

    if self.f0(x) < self.f0(y):
        return (a, a + d, x, y)
    else:
        return (x, y, b - d, b)
```

{anims[Fibonacci][0]}

After {results[Fibonacci][0]} iterations, it reaches $$x = {results[Fibonacci][1]:.4f}$$
with value $$f(x) = {results[Fibonacci][2]:.4f}$$.

### Powell's parabolic interpolation

At each iteration, this method fits a quadratic polynomial approximation of the
function at points $$a < b < c$$ and replaces one of these points with its minimizing
point. The initial triplet must be selected so that $$f(a) > f(b)$$, $$f(b) < f(c)$$,
and a local minimum of the function lies within $$[a,c]$$, in which the function also
is unimodal.

```python
def contract(self, a, x, y, b):  # a < x < y < b
    x0, y0 = self.f0(x), self.f0(y)
    if not np.isclose(x0, y0):
        if x0 < y0:
            z = self.minimize_parabola(a, x, y)
            return (a, z, x, y) if z < x else (a, x, z, y)
        else:
            z = self.minimize_parabola(x, y, b)
            return (x, y, z, b) if y < z else (x, z, y, b)
    elif abs(y - a) <= self.delta:
        return (a, x, x, y)
    elif abs(b - x) <= self.delta:
        return (x, y, y, b)
    else:
        return self.pre(a, b)  # reached symmetry? begin again
```

{anims[ParabolicInterpolation][0]}

After {results[ParabolicInterpolation][0]} iterations, it reaches $$x = {results[ParabolicInterpolation][1]:.4f}$$
with value $$f(x) = {results[ParabolicInterpolation][2]:.4f}$$.

## First order methods (gradient-based)

### Dichotomous search

As with other methods presented, dichotomous search needs that the function is
strictly unimodal in the initial interval, which also contains the minimum. At each
iteration, the function's first derivative is evaluated at trust region's middle
point and the interval is contracted properly. As a result, contraction is happening
by the constant ratio of $$0.5$$.

```python
def contract(self, a, b):  # a < b
    x = (a + b) / 2
    if self.f1(x) > 0:
        return a, x
    else:
        return x, b
```

{anims[Dichotomous][0]}

After {results[Dichotomous][0]} iterations, it reaches $$x = {results[Dichotomous][1]:.4f}$$
with value $$f(x) = {results[Dichotomous][2]:.4f}$$.

### Davidon's cubic interpolation

It fits a cubic polynomial approximation to the function that we want to
minimize, using $$f(a), f(b), f'(a), f'(b), \quad a < b$$. Each iteration happens
so that it is guaranteed for a local minimum to exist in such interval $$[a, b]$$. A
local minimum must exist in the initial interval selection too.
The minimizer of the cubic approximation lies within $$[a, b]$$ and it replaces one
of the two boundary points as shown in the code section below.

```python
def contract(self, a, b):  # a < b
    x = self.minimize_cubic(a, b)
    if self.f1(x) > 0 or self.f0(x) > self.f0(a):
        return a, x
    else:
        return x, b
```

{anims[CubicInterpolation][0]}

After {results[CubicInterpolation][0]} iterations, it reaches $$x = {results[CubicInterpolation][1]:.4f}$$
with value $$f(x) = {results[CubicInterpolation][2]:.4f}$$.

## Second order methods: Newton's

Newton's method performs descent in the steepest direction under the Hessian norm of
the function. This can be shown to mean that, at each iteration, the unnormalized update
consists of the negative gradient left multiplied by the inverse Hessian, or second derivative.
It is necessary that the function is twice differentiable, in order to use this
method. Each iteration moves the point estimation to the minimizer of the quadratic
approximation of the function at the current point. In the code section below, there
is also a backtracking mechanism implemented, which adapts the updated estimation,
if a certain strong curvature condition has not been met by the Newton step alone.

```python
def iterate(self, x, lrate, eps=1e-7):
    # eps is for numerical stability, if second derivative is close to zero
    return x - lrate * self.f1(x) / (self.f2(x) + eps)

def backtrack(self, x, xcand, c=0.99):
    iters = 0
    # Try to satisfy strong curvature condition
    while abs(self.f1(xcand)) > c * abs(self.f1(x)) and iters < self.max_iters:
        xcand = (x + xcand) / 2  # Actually it cuts learning rate in half
        iters += 1
    return xcand
```

{anims[Newton][0]}

{anims[Newton][1]}

After **{results[Newton][0]}** iterations, pure Newton method reaches at $$x = {results[Newton][1]:.4f}$$
with value $$f(x) = {results[Newton][2]:.4f}$$. However, Newton with backtracking reaches
faster at $$x = {results[dampedNewton][1]:.4f}$$ with value $$f(x) = {results[dampedNewton][2]:.4f}$$, after
**{results[dampedNewton][0]}** iterations.

[opti]: https://github.com/tsirif/optimization-auth-course/blob/master/src/minimize_02_9/optimize.py
[res]: https://github.com/tsirif/optimization-auth-course/blob/master/src/minimize_02_9/results.py
"""

introf = intro.format(minimum=minimum0)
restf = rest_report.format(anims=anims, results=results0)
final_report = introf + golden_section + restf
print(final_report)
