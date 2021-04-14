# -*- coding: utf-8 -*-
"""
Created on Mon Feb 22 21:29:24 2021

@author: Jiyun
"""

n = int(input())
g = []
for i in range(n):
    g.append(int(input()))
    
g.sort()
weight = []
for i in g:
    weight.append(i*n)
    n -= 1

print(max(weight))