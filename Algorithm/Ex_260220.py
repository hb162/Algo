def numIslands(graph):
    if not graph:
        return 0
    row = len(graph)
    col = len(graph[0])
    count = 0
    for i in range(row):
        for j in range(col):
            if graph[i][j] == 1:
                DFS(graph, row, col, i, j)
                count = count + 1
    return count


def DFS(graph, row, col, x, y):
    if graph[x][y] == 0:
        return
    graph[x][y] = 0
    if x != 0:
        DFS(graph, row, col, x - 1, y)
    if x != row - 1:
        DFS(graph, row, col, x + 1, y)
    if y != 0:
        DFS(graph, row, col, x, y - 1)
    if y != col - 1:
        DFS(graph, row, col, x, y + 1)


graph1 = [[1, 1, 1, 1, 0],
          [1, 1, 0, 1, 0],
          [1, 1, 0, 0, 0],
          [0, 0, 0, 0, 0]]

graph2 = [[1, 1, 0, 0, 0],
          [1, 1, 0, 0, 0],
          [0, 0, 1, 0, 0],
          [0, 0, 0, 1, 1]]
print(numIslands(graph2))
