# -*- coding: utf-8 -*-
"""
Created on Sat Feb 27 20:51:31 2021

@author: Jiyun
"""

t = int(input())
for _ in range(t):
    n = int(input())
    array = list(map(int, input().split()))
    mx = array[-1]
    result = 0
    for i in range(n-2,-1,-1):
        if array[i] > mx:
            mx = array[i]
        else:
            result += mx - array[i]
    print(result)