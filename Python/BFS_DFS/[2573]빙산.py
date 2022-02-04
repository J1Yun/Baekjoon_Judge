from collections import deque
import sys
input = sys.stdin.readline

graph = []
n, m = map(int, input().split())
for _ in range(n):
    graph.append(list(map(int, input().split())))


dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]
def bfs(ix, iy):
    queue = deque()
    queue.append((ix, iy))
    visited[ix][iy] = 1
    while queue:
        x, y = queue.popleft()
        for t in range(4):
            nx = x + dx[t]
            ny = y + dy[t]
            if graph[nx][ny] and not visited[nx][ny]:
                visited[nx][ny] = 1
                queue.append((nx, ny))
    
result = 0
while True:
    temp = [[0]*m for _ in range(n)]
    for i in range(1, n-1):
        for j in range(1, m-1):
            if graph[i][j]:
                water = 0
                for k in range(4):
                    ni = i + dx[k]
                    nj = j + dy[k]
                    if not graph[i+dx[k]][j+dy[k]]:
                        water += 1
                if graph[i][j] - water > 0:
                    temp[i][j] = graph[i][j] - water
    graph = temp
    result += 1
    visited = [[0]*m for _ in range(n)]
    count = 0
    for i in range(1, n-1):
        for j in range(1, m-1):
            if graph[i][j] and not visited[i][j]:
                bfs(i, j)
                count += 1
    if count != 1:
        break
    
if count > 1:  
    print(result)
else:
    print(0)

