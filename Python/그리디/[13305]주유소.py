# -*- coding: utf-8 -*-
"""
Created on Fri Feb 26 18:23:21 2021

@author: Jiyun
"""

n = int(input())
dist = list(map(int, input().split()))
price = list(map(int, input().split()))
temp = price[0]
result = 0

for i in range(n-1):
    if temp > price[i]:
        temp = price[i]
    result += temp * dist[i]
    
print(result)