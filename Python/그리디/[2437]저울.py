# -*- coding: utf-8 -*-
"""
Created on Fri Feb 26 19:23:11 2021

@author: Jiyun
"""

n = int(input())
array = list(map(int, input().split()))
array.sort()

result = 1
for i in array:
    if result < i:
        break
    result += i

print(result)