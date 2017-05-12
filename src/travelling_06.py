#!/usr/bin/env python
# -*- coding: utf-8 -*-
import argparse
import math


def solve():
    graph = {}
    graph[1] = list(zip(range(1, 7), (math.inf, 13, 51, 78, 68, 51)))
    graph[2] = list(zip(range(1, 7), (13, math.inf, 60, 70, 68, 61)))
    graph[3] = list(zip(range(1, 7), (51, 60, math.inf, 56, 35, 2)))
    graph[4] = list(zip(range(1, 7), (78, 70, 56, math.inf, 21, 57)))
    graph[5] = list(zip(range(1, 7), (68, 68, 35, 21, math.inf, 36)))
    graph[6] = list(zip(range(1, 7), (51, 61, 2, 57, 36, math.inf)))

    min_cost = math.inf
    best_cycles = []
    init = 2  # Any initial vertex would yield all Hamiltonians, as it should be in any one by definition
    seqs = [([init], 0)]
    for i in range(6):  # * O(N)
        if not seqs:
            break
        new_seqs = []
        for seq, running_cost in seqs:  # * O(1*(N-1)*...*(N-i+1))
            for vertex, cost in graph[seq[-1]]:  # * O(N)
                if i == 5 and vertex == seq[0]:
                    new_seqs.append((list(seq), running_cost + cost))
                    break
                if vertex in seq:  # * O(i)
                    # cannot go there, already have been
                    continue
                new_seqs.append((list(seq) + [vertex], running_cost + cost))
        seqs = list(new_seqs)

    for seq, total_cost in seqs:
        if total_cost < min_cost:
            min_cost = total_cost
            best_cycles = [seq]
        elif total_cost == min_cost:
            best_cycles.append(seq)

    print("Best cycles:")
    print(best_cycles)
    print("Minimum cost:")
    print(min_cost)


if __name__ == "__main__":
    solve()
