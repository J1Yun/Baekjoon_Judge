# -*- coding: utf-8 -*-
"""
Created on Wed Jul 14 20:07:09 2021

@author: Jiyun
"""
from collections import deque

n = int(input())
m = int(input())

graph = []
for _ in range(m):
    graph.append(set(map(int, input().split())))
    
def bfs(x):
    visited = []
    queue = deque()
    queue.append(x)
    visited.append(x)
    count = 0
    while queue:
        q = queue.popleft()
        for i in range(1, n+1):
            if {q, i} in graph and i not in visited:
                queue.append(i)
                visited.append(i)
                count += 1
                
    return count
        
print(bfs(1))
