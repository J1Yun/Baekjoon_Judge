# -*- coding: utf-8 -*-
"""
Created on Sun Feb 21 19:44:15 2021

@author: Jiyun
"""

n = int(input())
time = []
result = []
for i in range(n):
    time.append(tuple(map(int, input().split())))

time.sort(key=lambda x:(x[1],x[0]))

result.append(time[0])
for i in range(1,n):
    if result[-1][1] <= time[i][0]:
        result.append(time[i])

print(len(result))