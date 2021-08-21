from collections import deque
import copy

n = int(input())
graph = []
for _ in range(n):
    graph.append(list(input()))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
graph1 = copy.deepcopy(graph)

def bfs0(x, y):
    queue = deque()
    color = graph[x][y]
    queue.append((x, y))
    graph[x][y] = 0
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx<0 or ny<0 or nx>=n or ny>=n:
                continue
            if graph[nx][ny] != color:
                continue
            queue.append((nx, ny))
            graph[nx][ny] = 0

def bfs1(x, y):
    queue = deque()
    color = graph1[x][y]
    queue.append((x, y))
    graph1[x][y] = 0
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx<0 or ny<0 or nx>=n or ny>=n:
                continue
            if color == graph1[nx][ny] or {color, graph1[nx][ny]} == {'G', 'R'}:
                queue.append((nx, ny))
                graph1[nx][ny] = 0

count, count1 = 0, 0
for i in range(n):
    for j in range(n):
        if graph[i][j] != 0:
            bfs0(i,j)
            count += 1
        if graph1[i][j] != 0:
            bfs1(i,j)
            count1 += 1

print(count, count1)