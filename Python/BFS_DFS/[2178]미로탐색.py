# -*- coding: utf-8 -*-
"""
Created on Wed Jul 14 16:22:00 2021

@author: Jiyun
"""
from collections import deque

n, m = map(int, input().split())
graph = []

for i in range(n):
    graph.append(list(map(int, input())))
                 
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
                 
def bfs(x,y):
    queue = deque()
    queue.append((x, y))
    
    while queue:
        x, y = queue.popleft()
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            if graph[nx][ny] == 1:
                queue.append((nx, ny))
                graph[nx][ny] = graph[x][y] + 1
    
    return graph[n-1][m-1]

print(bfs(0, 0))