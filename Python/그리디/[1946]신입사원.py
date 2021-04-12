# -*- coding: utf-8 -*-
"""
Created on Tue Feb 23 19:13:45 2021

@author: Jiyun
"""
import sys
t=int(sys.stdin.readline())

for i in range(t):
    n = int(sys.stdin.readline())
    score = []
    for _ in range(n):
        a, b = map(int,sys.stdin.readline().split())
        score.append((a,b))
    score.sort(key = lambda x : x[0])
    count = 1
    small = score[0][1]
    for j in range(1,n):
        if score[j][1] < small:
            small = score[j][1]
            count += 1
            
    print(count)