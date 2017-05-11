from collections import deque

import numpy as np
from scipy.optimize import linprog as simplex

#######################################################################
#                           Problem Setting                           #
#######################################################################

costs = np.array([[36, 39, np.NaN],
                  [36, 39, 45],
                  [np.NaN, 33, 42]])
min_demand = np.array([320, 170, 190]).reshape((3, 1))
ticket = np.array([45, 45, 24]).reshape((3, 1))
capacity = np.array([[20, 15, np.NaN],
                     [18, 13, 10],
                     [np.NaN, 14, 8]])
avail_planes = np.array([15, 14, 18]).reshape((3, 1))
avail_flights = 3 * avail_planes

profit = ticket - costs
p = list(profit.flatten())
p = p[:2] + p[3:6] + p[7:]
profit = np.concatenate([np.zeros_like(p), np.array(p)])

c = list(capacity.flatten())
c = c[:2] + c[3:6] + c[7:]
capacity = np.array(c)

demand1 = np.zeros((3, 3))
demand1[0, :] = 1
demand2 = np.zeros((3, 3))
demand2[1, :] = 1
demand3 = np.zeros((3, 3))
demand3[2, :] = 1
demand = np.array([demand1.flatten(), demand2.flatten(), demand3.flatten()])
demand = np.concatenate([demand[:, :2], demand[:, 3:6], demand[:, 7:]], axis=1)

flights1 = np.zeros((3, 3))
flights1[:, 0] = 1
flights2 = np.zeros((3, 3))
flights2[:, 1] = 1
flights3 = np.zeros((3, 3))
flights3[:, 2] = 1
flights = np.array([flights1.flatten(), flights2.flatten(), flights3.flatten()])
flights = np.concatenate([flights[:, :2], flights[:, 3:6], flights[:, 7:]], axis=1)

A = np.concatenate([np.concatenate([flights, np.zeros_like(flights)], axis=1),
                    np.concatenate([np.diag(-capacity.flatten()), np.identity(7)], axis=1),
                    np.concatenate([np.zeros_like(demand), -demand], axis=1)], axis=0)

b = np.concatenate([avail_flights, np.zeros((7, 1)), -min_demand], axis=0)

#######################################################################
#                        Branch & Cut Solution                        #
#######################################################################


best_solution = None
best_value = -np.inf
subproblems = deque([(A, b)])
nodes_opened = 0

while subproblems:
    A_parent, b_parent = subproblems.popleft()
    nodes_opened += 1

    # Solve relaxed subproblem
    res = simplex(-profit, A_parent, b_parent)
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
    constrain_1 = np.zeros((1, len(profit)))
    constrain_1[0, branch_i] = 1
    A_child_1 = np.concatenate([A_parent, constrain_1])
    b_child_1 = np.concatenate([b_parent, np.array([[down]])])
    subproblems.append((A_child_1, b_child_1))

    up = np.ceil(res.x[branch_i])
    constrain_2 = np.zeros((1, len(profit)))
    constrain_2[0, branch_i] = -1
    A_child_2 = np.concatenate([A_parent, constrain_2])
    b_child_2 = np.concatenate([b_parent, np.array([[-up]])])
    subproblems.append((A_child_2, b_child_2))

print("Solution:")
print(best_solution)
print("Optimal value:", end=' ')
print(best_value)
print("Subproblems solved:", end=' ')
print(nodes_opened)
