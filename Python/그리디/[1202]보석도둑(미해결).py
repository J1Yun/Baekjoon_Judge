# -*- coding: utf-8 -*-
"""
Created on Fri Feb 26 20:18:06 2021

@author: Jiyun

시간초과
"""

n, k = map(int, input().split())
mv = []
c = []
for i in range(n):
    mv.append(tuple(map(int, input().split())))
for i in range(k):
    c.append(int(input()))
    
mv.sort(key = lambda x : x[0])
c.sort()
result = 0
for i in c:
    j, best = 0, (0,0)
    while len(mv)> j and mv[j][0] <= i:
        if best[1] < mv[j][1]:
            best = mv[j]
        j += 1
    if best != (0,0):
        result += best[1]
        mv.remove(best)

print(result)
    