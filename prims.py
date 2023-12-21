# -*- coding: utf-8 -*-
"""
Created on Thu Dec 21 07:07:15 2023

@author: sgpdh
"""

class Graph:
    def __init__(self):
        self.vertices = set()
        self.edges = []

    def add_edge(self, u, v, weight):
        self.vertices.update({u, v})
        self.edges.append((weight, u, v))

def prim(graph):
    minimum_spanning_tree = []
    visited = set()
    start_vertex = next(iter(graph.vertices))  # Start from an arbitrary vertex
    visited.add(start_vertex)

    while len(visited) < len(graph.vertices):
        available_edges = [
    (weight, u, v) 
    for weight, u, v in graph.edges 
    if u in visited and v not in visited
]

        available_edges.sort()

        weight, u, v = available_edges.pop(0)

        if v not in visited:
            visited.add(v)
            minimum_spanning_tree.append((u, v, weight))

    return minimum_spanning_tree

# Example usage with the provided adjacency matrix
G = [
    [0, 2, 0, 6, 0],
    [2, 0, 3, 8, 5],
    [0, 3, 0, 0, 7],
    [6, 8, 0, 0, 9],
    [0, 5, 7, 9, 0]
]

# Create a Graph object and add edges from the adjacency matrix
g = Graph()
for i in range(len(G)):
    for j in range(len(G[i])):
        if G[i][j] != 0:
            g.add_edge(i, j, G[i][j])

minimum_spanning_tree = prim(g)
print("Minimum Spanning Tree:")
for edge in minimum_spanning_tree:
    print(f"{edge[0]} -- {edge[1]} : {edge[2]}")
