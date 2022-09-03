from copy import deepcopy
r, c, t = map(int, input().split())
graph = []
for _ in range(r):
    graph.append(list(map(int, input().split())))

dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]

def spread():
    data = deepcopy(graph)
    for x in range(r):
        for y in range(c):
            if graph[x][y] > 0:
                temp, count = graph[x][y] // 5, 0
                for i in range(4):
                    nx, ny = x + dx[i], y + dy[i]
                    if nx < 0 or nx >= r or ny < 0 or ny >= c or graph[nx][ny] == -1:
                        continue
                    data[nx][ny] += temp
                    count += 1
                data[x][y] -= temp * count
    return data

def move(x1, x2):
    data = deepcopy(graph)
    for i in range(1, c-1):
        data[x1][i+1] = graph[x1][i]
        data[x2][i+1] = graph[x2][i]
    for i in range(c-1):
        data[0][i] = graph[0][i+1]
        data[r-1][i] = graph[r-1][i+1]
    for i in range(x1):
        data[i+1][0] = graph[i][0]
        data[i][c-1] = graph[i+1][c-1]
    for i in range(x2+1, r):
        data[i-1][0] = graph[i][0]
        data[i][c-1] = graph[i-1][c-1]
    data[x1][0], data[x2][0], data[x1][1], data[x2][1] = -1, -1, 0, 0
    return data

cleaner = []
for _ in range(t):
    graph = spread()
    for i in range(r):
            if graph[i][0] == -1:
                cleaner.append(i)
    graph = move(cleaner[0], cleaner[1])

result = 0
for i in range(r):
    for j in range(c):
        if graph[i][j] > 0:
            result += graph[i][j]

print(result)

    