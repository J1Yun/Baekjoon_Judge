# -*- coding: utf-8 -*-
"""
Created on Thu Jul 15 18:35:11 2021

@author: Jiyun
"""
from collections import deque

n, k = map(int, input().split())
graph = [-1] * 100001
dq = [1, -1, 2]

def bfs(start):
    queue = deque()
    queue.append(start)
    graph[start] = 0
    
    while queue:
        q = queue.popleft()
        
        for i in dq:
            nq = q * 2 if i == 2 else q + i
            if 0 <= nq <= 100000 and graph[nq] == -1:
                queue.append(nq)
                graph[nq] = graph[q] + 1
            if nq == k:
                return graph[nq]

print(bfs(n))