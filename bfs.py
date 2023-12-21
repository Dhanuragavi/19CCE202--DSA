def bfs(start, graph):
    v_s = [False] * len(graph)
    queue = []

    v_s[start] = True
    queue.append(start)

    while queue:
        v = queue.pop(0)
        print("bfs starting from vertex", start,"is",v,"\t")

        for i in graph[v]:
            if not v_s[i]:
                v_s[i] = True
                queue.append(i)

# Example usage:
graph = {
    0: [1, 2, 3],
    1: [0],
    2: [0, 3],
    3: [0, 2, 4],
    4: [3],
}

start_node = 2
bfs(start_node, graph)
