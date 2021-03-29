# -*- coding: utf-8 -*-
"""
Created on Sun Feb 21 19:09:31 2021

@author: Jiyun
"""

n, k = map(int, input().split())
a= []
for i in range(n):
    a.append(int(input()))
count = 0

for i in range (n-1, -1, -1):
    count += k//a[i]
    k %= a[i]

print(count)