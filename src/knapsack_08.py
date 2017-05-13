#!/usr/bin/env python
# -*- coding: utf-8 -*-

from collections import deque, defaultdict as dd
import numpy as np
from scipy.optimize import linprog as simplex


def solve_branch_cut(weights, values, max_w):
    values = np.asarray(values)
    best_solution = None
    best_value = -np.inf
    subproblems = deque([(np.asarray(weights).reshape(1, 3),
                          np.asarray(max_w).reshape(1, 1))])
    nodes_opened = 0

    while subproblems:
        A_parent, b_parent = subproblems.popleft()
        nodes_opened += 1
        if nodes_opened % 5 == 0:
            print(nodes_opened)

        # Solve relaxed subproblem
        res = simplex(-values, A_parent, b_parent)
        if not res.success:
            if res.status == 1:
                print("Iteration limit reached... mby cycles?")
            elif res.status == 2:
                continue  # Infeasible subproblem
            else:
                print("Subproblem appears to be unbounded... mby bad initial problem?")
        # Filter relaxed solution for zeros
        res.x[np.isclose(res.x, 0)] = 0

        # Check if subspace's relaxed optimal value is above current best value
        if -res.fun <= best_value:
            continue  # skip branching on this subproblem

        # Find basic fractional elements
        fracts = []
        for i in range(len(res.x)):
            if not res.x[i].is_integer():
                fracts.append(i)
        # Check if solution is in integer space
        if not fracts:
            best_solution = res.x.astype('int')
            best_value = int(-res.fun)
            continue

        # Select a fractional element to branch from
        branch_i = fracts[0]

        # Create new constrains
        down = np.floor(res.x[branch_i])
        constrain_1 = np.zeros((1, len(values)))
        constrain_1[0, branch_i] = 1
        A_child_1 = np.concatenate([A_parent, constrain_1])
        b_child_1 = np.concatenate([b_parent, np.array([[down]])])
        subproblems.append((A_child_1, b_child_1))

        up = np.ceil(res.x[branch_i])
        constrain_2 = np.zeros((1, len(values)))
        constrain_2[0, branch_i] = -1
        A_child_2 = np.concatenate([A_parent, constrain_2])
        b_child_2 = np.concatenate([b_parent, np.array([[-up]])])
        subproblems.append((A_child_2, b_child_2))

    return best_solution, best_value, nodes_opened


def solve_dynamic(weights, values, max_w):
    opt_values = np.zeros(max_w + 1, dtype='int')
    sols = dd(lambda: set([(0, ) * len(values)]))

    for w in range(1, max_w + 1):
        for i in range(len(values)):
            if w < weights[i]:
                continue
            choice = values[i] + opt_values[w - weights[i]]
            if choice >= opt_values[w]:
                t = []
                for sol in list(sols[w - weights[i]]):
                    s = list(sol)
                    s[i] += 1
                    t.append(tuple(s))
                if choice > opt_values[w]:
                    sols[w] = set(t)
                    opt_values[w] = choice
                else:
                    sols[w] |= set(t)

    return list(map(lambda x: np.asarray(x), list(sols[max_w]))), opt_values[max_w]


if __name__ == "__main__":
    ##############
    #  Preamble  #
    ##############
    weights = [5, 8, 3]
    values = [5, 6, 4]
    max_w = 30
    ##############
    #  Solution  #
    ##############
    print("We need one of each types (problem's restriction).")
    print("so we solve the problem for y = x - 1, x >= 1, y >= 0.")
    print()
    necessary = np.ones(len(weights), dtype='int')
    max_w -= sum(weights)
    print("Equivalently: Maximize values * y, s.t. weights * y <= max_w, y >= 0 integer.")
    print("Then add to the optimal solution plus 1 to each item...")
    print("and plus sum(values) to the optimal value found.")
    print()

    print("Solution with integer programming (branch-and-cut method).")
    bs, bv, nodes = solve_branch_cut(weights, values, max_w)
    print("Solution:", bs + necessary)
    print("Optimal value:", bv + sum(values))
    print("Subproblems solved:", nodes)
    print()

    print("Solution with dynamic programming (unbounded knapsack).")
    bss, bv = solve_dynamic(weights, values, max_w)
    print("Solutions:", [list(sol + necessary) for sol in bss])
    print("Optimal value:", bv + sum(values))
