"""
Hi, here's your problem today. This problem was recently asked by Facebook:

Given an undirected graph, determine if a cycle exists in the graph.

Here is a function signature:

def find_cycle(graph):
"""


def find_cycle(graph):
    visited = {u: False for u in graph}
    for u in graph:
        if not visited[u]:
            if DFS(graph, u, u, visited):
                return True
    return False


def DFS(graph, u, previous_node, visited):
    visited[u] = True
    for v in graph[u]:
        if visited[v] and v != previous_node:
            return True
        if not visited[v]:
            if DFS(graph, v, u, visited):
                return True
    return False


graph = {0: {1, 2},
         1: {0, 3},
         2: {0, 4},
         3: {1},
         4: {2},
         }
print(find_cycle(graph))


#Time complexity O(V+E)
#V là: vertex
#E là đỉnh