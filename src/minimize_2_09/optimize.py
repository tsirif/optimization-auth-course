#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np
from numpy.random import random


class Optimizer(object):
    """Base class for unconstrained iterative optimization methods
    for non-linear unimodal functions of one real variable.

    :param float delta: Maximum error of an achieved solution from the optimal
       function arguments, the trust region.
    :param int max_iters: Maximum iterations allowed.
    """
    def __init__(self, delta, max_iters=10000):
        super(Optimizer, self).__init__()
        self.delta = delta
        self.max_iters = max_iters
        self.history = None

    def __call__(self, f0, f1=None, f2=None, start=None):
        """Execute optimization routine.

        Parameters
        ----------
        callable f0 : Function to be optimized, takes a float input and outputs
           float output.
        callable f1 : `f0`'s first derivative, optional
        callable f2 : `f0`'s second derivative, optional
        list start : starting position for optimization, optional

        .. note:: Iteration history is recorded in :attr:`history`. Thus this variable
           changes with each call.

        Returns
        -------
        tuple(int, float, float, bool): if it succedeed, it returns the number
        of iterations until conclusion, optimal function argument
        and value. False means that maximum iteration number has been reached.

        """
        self.f0 = f0
        self.f1 = f1
        self.f2 = f2
        if not start:
            start = np.random.random(2) * 5  # at interval [0, 5]
        else:
            start = np.asarray(start)
        self.iters = 0
        self.history = []
        if start.size > 1:
            start.sort()

        solution = self.exec_method(start)

        self.history = np.array(self.history).T
        succ = True
        if self.iters == self.max_iters:
            succ = False

        return (self.iters, solution, self.f0(solution), succ)

    def exec_method(self, start):
        raise NotImplementedError('Base cannot be called, please implement a method!')


class Newton(Optimizer):
    """Implements Newton (2nd order) optimization method.

    :param float delta: see :class:`Optimizer`
    :param int max_iters: see :class:`Optimizer`
    :param float lrate: learning rate coefficient, multiplies parameter displacement
    :param bool backtracking: True, if we are going to use a backtracking strategy to
       "ensure" convergence conditions.

    .. note:: We record in for visualization of the minimized quadratic approximation
       :attr:`parabola` that occurs in each iteration step.

    """
    def __init__(self, delta, max_iters=10000, lrate=1.0, backtracking=False):
        super(Newton, self).__init__(delta, max_iters)
        self.backtracking = backtracking
        self.lrate = lrate
        self.parabola = []

    def iterate(self, x, lrate, eps=1e-7):
        a = self.f2(x) / 2
        b = self.f1(x) - 2 * a * x
        c = self.f0(x) - a * x**2 - b * x
        self.parabola.append((a, b, c))  # for visualization
        # eps is for numerical stability, if second derivative is close to zero
        return x - lrate * self.f1(x) / (self.f2(x) + eps)

    def backtrack(self, x, xcand, c=0.99):
        iters = 0
        # Try to satisfy strong curvature condition
        while abs(self.f1(xcand)) > c * abs(self.f1(x)) and iters < self.max_iters:
            xcand = (x + xcand) / 2  # Actually it cuts learning rate in half
            iters += 1
        return xcand

    def exec_method(self, start):
        x = start
        self.history.append((x,))
        xprev = -np.inf
        self.parabola = []

        while abs(xprev - x) > self.delta and self.iters < self.max_iters:
            t = self.iterate(x, self.lrate)
            if self.backtracking:
                t = self.backtrack(x, t)
            xprev, x = x, t

            self.iters += 1
            self.history.append((x,))

        self.parabola.append((0, 0, 0))
        self.parabola = np.array(self.parabola).T
        return x


class IntervalContractor(Optimizer):
    def exec_method(self, start):
        a = start[0]
        b = start[1]

        interval = self.pre(a, b)  # a < x < y < b
        self.history.append(interval)

        while abs(a - b) > self.delta + self.delta**2 and self.iters < self.max_iters:
            interval = self.contract(*interval)
            a = interval[0]
            b = interval[-1]

            self.iters += 1
            self.history.append(interval)

        return (a + b) / 2

    def contract(self, *inteval):
        raise NotImplementedError('Please implement a trust region contraction policy!')

    def pre(self, a, b):
        return a, b


class Fibonacci(IntervalContractor):
    """Implements Fibonacci search method."""
    phi = (1 + np.sqrt(5)) / 2

    def pre(self, a, b):
        d = b - a
        nf = 2 * (d / self.delta)

        n = np.log(nf * np.sqrt(5) + 0.5) / np.log(self.phi)
        n = int(np.floor(n))
        near_fibo = np.round(self.phi**n / np.sqrt(5))
        near_fibo2 = np.round(self.phi**(n - 1) / np.sqrt(5))

        d1 = near_fibo * (self.delta / 2)
        d2 = near_fibo2 * (self.delta / 2)

        return a, a + d2, a + d1, b

    def contract(self, a, x, y, b):  # a < x < y < b
        d = y - x

        if self.f0(x) < self.f0(y):
            return (a, a + d, x, y)
        else:
            return (x, y, b - d, b)


class GoldenSection(IntervalContractor):
    """Implements golden section search method."""
    phi = (1 + np.sqrt(5)) / 2

    def pre(self, a, b):
        d0 = b - a
        d1 = (self.phi - 1) * d0  # phi**-1 == phi - 1
        return a, b - d1, a + d1, b

    def contract(self, a, x, y, b):  # a < x < y < b
        d = (self.phi - 1) * (y - a)

        if self.f0(x) < self.f0(y):
            return (a, y - d, x, y)
        else:
            return (x, y, x + d, b)


class ParabolicInterpolation(IntervalContractor):
    """Implements parabolic Interpolation search method."""
    def minimize_parabola(self, a, b, c):
        """Apply formula's for quadratic's minimizer."""
        a0, b0, c0 = self.f0(a), self.f0(b), self.f0(c)
        n = a0 * (c**2 - b**2) + b0 * (a**2 - c**2) + c0 * (b**2 - a**2)
        d = 2 * (a0 * (c - b) + b0 * (a - c) + c0 * (b - a))
        x = n / d

        #  u = np.array([[a], [b], [c]])
        #  A = np.concatenate([u**2, u, np.ones((3, 1))], axis=1)
        #  coeff = np.linalg.solve(A, self.f0(u)).reshape(3)
        #  x2 = -coeff[1] / (2 * coeff[0])
        #  assert(np.isclose(x, x2))
        return x

    def pre(self, a, b):
        d = b - a
        x = a
        iters = 0
        while (self.f0(x) >= self.f0(a) or self.f0(x) >= self.f0(b)) and \
                iters < self.max_iters:
            x = a + d / 3 + (d / 2 - d / 3) * random()
            iters += 1
        assert(iters != self.max_iters)
        y = self.minimize_parabola(a, b, x)
        return (a, x, y, b) if x < y else (a, y, x, b)

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


class CubicInterpolation(IntervalContractor):
    """Implements cubic interpolation search method."""
    def minimize_cubic(self, a, b):
        """Apply formula's for cubic's minimizer."""
        a0, a1 = self.f0(a), self.f1(a)
        b0, b1 = self.f0(b), self.f1(b)

        z = (3 * (a0 - b0)) / (b - a) + a1 + b1
        w = np.sqrt(z**2 - a1 * b1)
        x = b - ((b1 + w - z) * (b - a)) / (b1 - a1 + 2 * w)

        #  A = np.array([[a**3, a**2, a, 1], [3*a**2, 2*a, 1, 0],
        #                [b**3, b**2, b, 1], [3*b**2, 2*b, 1, 0]])
        #  b = np.array([[self.f0(a)], [self.f1(a)], [self.f0(b)], [self.f1(b)]])
        #  c = np.linalg.solve(A, b).reshape(4)
        #  D = (2*c[1])**2 - 4*(3*c[0])*c[2]
        #  x2 = (-2*c[1] + np.sqrt(D)) / (6*c[0])
        #  assert(np.isclose(x, x2))
        return x

    def pre(self, a, b):
        if self.f1(a) <= 0 and self.f1(b) >= 0:
            return a, b
        s = 2.0
        while self.f0(a + s) - self.f0(a) > 10:
            s *= 0.5
        x = a
        y = a + s
        while self.f1(y) < 0 and self.f0(y) < self.f0(x):
            s *= 2
            x, y = y, a + s
        return x, y

    def contract(self, a, b):  # a < b
        x = self.minimize_cubic(a, b)
        if self.f1(x) > 0:
            return a, x
        elif self.f1(x) < 0:
            return x, b
        else:
            return x, x


class Dichotomous(IntervalContractor):
    """Implements dichotomous search algorithm."""
    def contract(self, a, b):  # a < b
        x = (a + b) / 2
        if self.f1(x) > 0:
            return a, x
        else:
            return x, b
