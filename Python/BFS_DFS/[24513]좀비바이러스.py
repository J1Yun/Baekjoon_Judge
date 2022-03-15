from collections import deque

n, m = map(int, input().split())
graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))

for i in range(n):
    for j in range(m):
        if graph[i][j] == 1:
            virus1 = (i, j)
        elif graph[i][j] == 2:
            virus2 = (i, j)
            
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
queue1 = deque()
queue2 = deque()
queue1.append(virus1)
queue2.append(virus2)
temp = deque()
time = [[0]*m for _ in range(n)]
t = 0
while queue1 or queue2:
    t += 1
    temp.clear()
    while queue1:
        x1, y1 = queue1.popleft()
        if graph[x1][y1] == 3:
            continue
        for i in range(4):
            nx1 = x1 + dx[i]
            ny1 = y1 + dy[i]
            if nx1 < 0 or nx1 >= n or ny1 < 0 or ny1 >= m or graph[nx1][ny1] in (-1, 1, 3):
                continue
            if graph[nx1][ny1] == 2 and time[nx1][ny1] != t:
                continue
            graph[nx1][ny1] += 1
            time[nx1][ny1] = t
            if graph[nx1][ny1] != 3:
                temp.append((nx1, ny1))
    queue1 += temp
    temp.clear()
    while queue2:
        x2, y2 = queue2.popleft()
        if graph[x2][y2] == 3:
            continue
        for j in range(4):
            nx2 = x2 + dx[j]
            ny2 = y2 + dy[j]
            if nx2 < 0 or nx2 >= n or ny2 < 0 or ny2 >= m or graph[nx2][ny2] in (-1, 2, 3):
                continue
            if graph[nx2][ny2] == 1 and time[nx2][ny2] != t:
                continue
            graph[nx2][ny2] += 2
            time[nx2][ny2] = t
            if graph[nx2][ny2] != 3:
                temp.append((nx2, ny2))
    queue2 += temp

result = [0, 0, 0]
for i in range(n):
    for j in range(m):
        if graph[i][j] not in (0, -1):
            result[graph[i][j]-1] += 1
print(' '.join(map(str, result)))