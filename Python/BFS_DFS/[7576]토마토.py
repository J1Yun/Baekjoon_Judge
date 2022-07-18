# -*- coding: utf-8 -*-
"""
Created on Wed Jul 14 23:03:08 2021

@author: Jiyun
"""
from collections import deque

m, n = map(int, input().split())
graph = []
queue = deque()

for i in range(n):
    temp = list(map(int, input().split()))
    graph.append(temp)
    for j in range(m):
        if temp[j] == 1:
            queue.append((i,j))
    
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs():
    global queue
    result = 1
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx<0 or ny<0 or nx>=n or ny>=m:
                continue
            if graph[nx][ny] == -1:
                continue
            if graph[nx][ny] == 0:
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx, ny))
                result = max(result, graph[nx][ny])
    return result -1

result = bfs()
for i in graph:
    if 0 in i:
        result = -1
        break
print(result)
    