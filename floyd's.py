# -*- coding: utf-8 -*-
"""
Created on Thu Dec 21 00:42:10 2023

@author: sgpdh
"""

class Graph:
    def __init__(self, num_v):
        self.num_v = num_v
        self.graph = []
        for i in range(num_v):
           row=[float('inf')] * num_v
           self.graph.append(row)
                

    def add_edge(self, u, v, weight):
        self.graph[u][v] = weight

    def floyd_s(self):
        dis_matrix = []
        for row in self.graph:
            dis_matrix.append(row[:])

        

        for k in range(self.num_v):
            for i in range(self.num_v):
                for j in range(self.num_v):
                    if dis_matrix[i][k] + dis_matrix[k][j] < dis_matrix[i][j]:
                        dis_matrix[i][j] = dis_matrix[i][k] + dis_matrix[k][j]

        return dis_matrix


# Example usage with input in matrix form:
matrix_input = [
    [0, 5, 10, float('inf')],
    [float('inf'), 0, 3, 7],
    [float('inf'), float('inf'), 0, 1],
    [float('inf'), float('inf'), float('inf'), 0]
]

g = Graph(len(matrix_input))

for i in range(len(matrix_input)):
    for j in range(len(matrix_input[i])):
        if matrix_input[i][j] != float('inf'):
            g.add_edge(i, j, matrix_input[i][j])

shortest_paths = g.floyd_s()

print("Shortest paths between all pairs of vertices:")
for i in range(g.num_v):
    for j in range(g.num_v):
        print("From", i,"to", j ,":",shortest_paths[i][j])
