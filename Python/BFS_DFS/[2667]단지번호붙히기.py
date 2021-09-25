# -*- coding: utf-8 -*-
"""
Created on Wed Jul 14 17:27:00 2021

@author: Jiyun
"""

n = int(input())
graph = []
for i in range(n):
    graph.append(list(map(int,input())))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
count = 0

def dfs(x, y):
    global count
    if x<0 or x>=n or y<0 or y>=n:
        return 0
    if graph[x][y]==0:
        return 0
    
    graph[x][y] = 0
    count += 1
    for i in range(4):
        dfs(x+dx[i], y+dy[i])
    
    return count

result = []
for i in range(n):
    for j in range(n):
        r = dfs(i, j)
        if r:
            result.append(r)
            count = 0
        
print(len(result))
result.sort()
for i in result:
    print(i)