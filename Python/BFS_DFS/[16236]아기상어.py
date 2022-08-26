from collections import deque

n = int(input())
graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))
m = 0
for i in range(n):
    for j in range(n):
        if graph[i][j] == 9:
            x, y = i, j
        elif graph[i][j]:
            m += 1
size = 2
dx, dy = [-1, 0, 0, 1], [0, -1, 1, 0]
def bfs(x, y, visited):
    visited[x][y] = 1
    queue = deque()
    queue.append((x, y, 0))
    temp = 0
    selected = (n, n, -1)
    while queue:
        x, y, s = queue.popleft()
        if temp != s and selected[-1] != -1:
            return selected
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= n or visited[nx][ny] or graph[nx][ny] > size:
                continue
            if graph[nx][ny] and graph[nx][ny] < size:
                selected = min(selected, (nx, ny, s+1))
            visited[nx][ny] = 1
            queue.append((nx, ny, s+1))
        temp = s
    return (-1, -1, -1)
            

result, count = 0, 0
graph[x][y] = 0
while 1:
    visited = [[0]*n for _ in range(n)]
    x, y, s = bfs(x, y, visited)
    if s == -1:
        break
    graph[x][y] = 0
    result += s
    count += 1
    if count == size:
        size += 1
        count = 0
print(result)