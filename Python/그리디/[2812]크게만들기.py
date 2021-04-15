# -*- coding: utf-8 -*-
"""
Created on Sat Feb 27 17:41:19 2021

@author: Jiyun
"""

n, k = map(int, input().split())
num = list(input())
temp = []
for i in range(n):
    while k > 0 and len(temp) > 0 and int(temp[-1]) < int(num[i]):
        del temp[-1]
        k -= 1
    temp.append(num[i])
print(int(''.join(temp[:len(temp)-k])))