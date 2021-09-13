from collections import deque
import copy
import sys
input = sys.stdin.readline

graph = []
n, m = map(int, input().split())
for _ in range(n):
    graph.append(list(map(int, input().split())))

temp = []
for i in range(n):
    for j in range(m):
        temp.append((i,j))
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
result = 0
combination = []
for i in range(n*m-2):
    for j in range(i+1, n*m-1):
        for k in range(j+1, n*m):
            if not graph[temp[i][0]][temp[i][1]] and not graph[temp[j][0]][temp[j][1]] and not graph[temp[k][0]][temp[k][1]]:
                combination.append([temp[i], temp[j], temp[k]])
for comb in combination:
    temp_graph = copy.deepcopy(graph)
    for x, y in comb:
        temp_graph[x][y] = 1
    visited = [[0]*m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            queue = deque()
            if temp_graph[i][j] == 2 and visited[i][j] == 0:
                queue.append((i, j))
                while queue:
                    x, y = queue.popleft()
                    for k in range(4):
                        nx = x + dx[k]
                        ny = y + dy[k]
                        if nx<0 or ny<0 or nx>=n or ny>=m:
                            continue
                        if temp_graph[nx][ny] == 0 and visited[nx][ny] == 0:
                            temp_graph[nx][ny] = 2
                            visited[nx][ny] = 1
                            queue.append((nx, ny))
                            
    count = 0
    for i in range(n):
        count += temp_graph[i].count(0)
    result = max(result, count)

print(result)