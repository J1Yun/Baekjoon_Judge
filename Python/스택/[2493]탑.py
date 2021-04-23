# -*- coding: utf-8 -*-
"""
Created on Sat Mar  6 23:35:04 2021

@author: Jiyun
"""

n = int(input())
array =list(map(int, input().split()))
stack = []
result = [0] * n
for i in range(n):
    while stack and array[stack[-1]] < array[i]:
        stack.pop()
    if stack:
        result[i] = stack[-1] + 1
    stack.append(i)
    
print(' '.join(map(str,result)))
    