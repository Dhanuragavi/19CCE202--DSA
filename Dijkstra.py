# -*- coding: utf-8 -*-
"""
Created on Thu Dec 21 10:37:32 2023

@author: sgpdh
"""

class Graph:
    def __init__(self, num_v):
        self.num_v = num_v
        self.graph = []
        for i in range(num_v):
            row = [0] * num_v
            self.graph.append(row)

    def print_distances(self, d):
        for i in range(len(d)):
            dis = d[i]
            print("distance of", i, "from source is:\t", dis)

    def min_dis(self, dis, visited):
        min_distance = float('inf')
        min_vertex = -1

        for v in range(self.num_v):
            if not visited[v] and dis[v] < min_distance:
                min_distance = dis[v]
                min_vertex = v

        return min_vertex

    def dijkstra(self, start):
        d = [float('inf')] * self.num_v
        d[start] = 0
        visited = [False] * self.num_v

        for j in range(self.num_v):
            curr_v = self.min_dis(d, visited)
            visited[curr_v] = True

            for k in range(self.num_v):
                weight = self.graph[curr_v][k]
                if not visited[k] and weight > 0:
                    d[k] = min(d[k], d[curr_v] + weight)

        self.print_distances(d)

# test case:
g = Graph(5)
g.graph = [
    [0, 0, 0, 0, 0 ],
    [0, 0, 2, 4, 1 ],
    [0, 2, 0, 1, 3 ],
    [0, 4, 1, 0, 6 ],
    [0, 1, 3, 6, 0 ],
    
]

g.dijkstra(1)  #source vertex

