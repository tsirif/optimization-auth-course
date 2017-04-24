#!/usr/bin/env python
# -*- coding: utf-8 -*-
import math

# This is the input: a directed graph
# It is represented as a map from a vertex (char) to a list of tuples.
# Each tuple is the neighboring vertex along with the corresponding edge's cost.
GRAPH = {}
GRAPH['A'] = [('B', 7), ('C', 1)]
GRAPH['B'] = [('C', 5), ('D', 1), ('E', 2)]
GRAPH['C'] = [('B', 2), ('E', 9)]
GRAPH['D'] = [('E', 3)]
GRAPH['E'] = []


def extract_min(keys, criterion):
    """
    Extracts best key from a list of `keys`. The best key has the lowest value
    of `criterion`.
    """
    best_key = None
    min_dist = math.inf
    for key in keys:
        if criterion[key] < min_dist:
            best_key = key
            min_dist = criterion[key]
    return best_key


def shortest_from(graph, start):
    """
    Implementation of Dijkstra's algorithm.

    Parameters
    ----------
    graph : dictionary
       Mapping from vertices to list of (vertices, cost of edge).
    start : char
       Representation of the vertex to begin searching for the shortest path.

    Returns
    -------
    prev : dictionary
       Maps a vertex to another, which is the best choice to
       come in a total shortest path in graph.
    dist : dictionary
       Maps a vertex to the length of the shortest path from `start` to it.

    """
    # Init `dist` and `prev`
    dist = {}
    prev = {}
    for vertex in GRAPH:
        dist[vertex] = math.inf
    dist[start] = 0  # length to self is zero
    prev[start] = None  # By definition it is not preceeded by any vertex

    unvisited = set(GRAPH.keys())

    while unvisited:
        current = extract_min(unvisited, dist)
        unvisited -= set([current])

        for neigh, cost in graph[current]:
            alt_path = dist[current] + cost
            if alt_path < dist[neigh]:
                prev[neigh] = current
                dist[neigh] = alt_path

    return prev, dist


def construct_path(prev, end):
    """
    Constructs path starting from the `end` vertex and going backwards.

    Parameters
    ----------
    prev : dictionary
       Maps a vertex to another, which is the best choice to
       come in a total shortest path in graph.
    end : character
       Shortest path's destination vertex

    Returns
    -------
    list
       Sequence of vertices in graph consisting of shortests path from 'A' to `end`

    .. note::
       Finishes when prev[path[-1]] is None, which means that path[-1] is the
       first vertex, i.e. 'A'

    """
    path = [end]
    while path[-1]:
        path.append(prev[path[-1]])
    path.reverse()
    return path[1:]


if __name__ == "__main__":
    prev, dist = shortest_from(GRAPH, 'A')
    for vertex in GRAPH:
        if vertex == 'A':
            continue
        path = construct_path(prev, vertex)
        total_cost = dist[vertex]
        print("Path from 'A' to '{}':".format(vertex))
        print(path)
        print("Total Cost:")
        print(total_cost)
        print()
