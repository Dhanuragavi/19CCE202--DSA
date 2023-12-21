# -*- coding: utf-8 -*-
"""
Created on Thu Dec 21 07:45:40 2023

@author: sgpdh
"""

class Graph:
    def __init__(self, num_vertices):
        self.V = num_vertices
        self.E = []

    def add_edge(self, u, v, w):
        self.E.append((u, v, w))

    def dynamic_p(self, source):
        dist = [float('inf')] * self.V
        pred = [None] * self.V
        dist[source] = 0

        for _ in range(self.V - 1):
            for u, v, w in self.E:
                if dist[u] + w < dist[v]:
                    dist[v] = dist[u] + w
                    pred[v] = u

        for u, v, w in self.E:
            if dist[u] + w < dist[v]:
                raise ValueError("Graph contains a negative cycle")

        return dist, pred


# Example usage:
g = Graph(5)
g.add_edge(0, 1, 6)
g.add_edge(0, 3, 7)
g.add_edge(1, 2, 5)
g.add_edge(1, 3, 8)
g.add_edge(1, 4, -4)
g.add_edge(2, 1, -2)
g.add_edge(3, 2, -3)
g.add_edge(3, 4, 9)
g.add_edge(4, 0, 2)
g.add_edge(4, 2, 7)

src = 4
distances, predecessors = g.dynamic_p(src)

print(f"Shortest distances from source vertex {src}: {distances}")
print(f"Predecessors: {predecessors}")
