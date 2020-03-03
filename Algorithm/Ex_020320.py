def find_cycle(graph):
    marked = {u: False for u in graph}
    for u in graph:
        if not marked[u]:
            if DFS(graph, u, u, marked):
                return True
    return False


def DFS(graph, u, previous_node, marked):
    marked[u] = True
    for v in graph[u]:
        if marked[v] and v != previous_node:
            return True
        if not marked[v]:
            if DFS(graph, v, u, marked):
                return True
    return False


graph = {0: {1, 2},
         1: {0, 3},
         2: {0, 4},
         3: {1},
         4: {2},
         }
print(find_cycle(graph))
