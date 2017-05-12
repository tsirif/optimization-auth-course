#!/usr/bin/env python
# -*- coding: utf-8 -*-
from collections import defaultdict as dd
import argparse


def solve(init):
    # 1. one-to-one association of squares to numbers (symbols for vertices)
    # --- row-wise enumeration of a 4x4 chessboard's squares
    graph = dd(list)
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

    seqs = [[init]]
    path_found = False
    print('Init square: {}'.format(init))
    if init < 0 or init > 15:
        print('Warning: There is not a vertex associated with that number')
    for i in range(15):  # * O(N)
        if not seqs:
            break
        new_seqs = []
        for seq in seqs:  # * O(8**(i-1))
            next_squares = graph[seq[-1]]
            for square in next_squares:  # * O(8)
                if square in seq:  # * O(i)
                    # cannot go there, already have been
                    continue
                new_seqs.append(seq + [square])
        #  print(i)
        #  print(new_seqs)
        seqs = new_seqs
    print('Paths found:')
    print(path_found)
    print(seqs)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('N', type=int, help='Total number of squares in a square chessboard')
    args = parser.parse_args()
    solve(args.N)
