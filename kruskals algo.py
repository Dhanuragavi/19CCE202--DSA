# -*- coding: utf-8 -*-
"""
Created on Thu Dec 21 07:41:12 2023

@author: sgpdh
"""

class Graph:
    def __init__(self, vertices):
        self.vertices = vertices
        self.edges = []

    def add_edge(self, u, v, weight):
        self.edges.append((u, v, weight))

def selection_sort(edges):
    n = len(edges)
    for i in range(n):
        min_index = i
        for j in range(i + 1, n):
            if edges[j][2] < edges[min_index][2]:
                min_index = j
        edges[i], edges[min_index] = edges[min_index], edges[i]

def kruskal(graph):
    minimum_spanning_tree = []
    selection_sort(graph.edges)
    parent = list(range(graph.vertices))

    def find(node):
        if parent[node] != node:
            parent[node] = find(parent[node])
        return parent[node]

    def union(root1, root2):
        parent[root1] = root2

    for edge in graph.edges:
        u, v, weight = edge
        root1 = find(u)
        root2 = find(v)

        if root1 != root2:
            union(root1, root2)
            minimum_spanning_tree.append(edge)

    return minimum_spanning_tree

# Example usage:
g = Graph(5)
g.add_edge(0, 1, 2)
g.add_edge(0, 3, 1)
g.add_edge(1, 2, 3)
g.add_edge(1, 3, 2)
g.add_edge(2, 3, 4)

minimum_spanning_tree = kruskal(g)
print("Minimum Spanning Tree:")
for edge in minimum_spanning_tree:
    print(f"{edge[0]} -- {edge[1]} : {edge[2]}")
