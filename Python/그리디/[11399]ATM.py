# -*- coding: utf-8 -*-
"""
Created on Sun Feb 21 18:30:43 2021

@author: Jiyun
"""

n = int(input())
p = list(map(int, input().split()))

p.sort()
answer = 0
temp = 0
for i in range(n):
    temp += p[i]
    answer += temp

print(answer)