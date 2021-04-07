# -*- coding: utf-8 -*-
"""
Created on Thu Feb 25 21:56:40 2021

@author: Jiyun
"""

n = int(input())
array = []
result = 0
for i in range(n):
    array.append(int(input()))

array.sort(reverse=True)
while len(array) > 0 :
    if len(array) == 1:
        result += array[0]
        break
    
    if array[0] <= 0:
        array.sort()
        result += array[0] * array[1]
        del array[0:2]
    else:
        if array[1] <= 1:
            result += array[0]
            del array[0]
        else:
            result += array[0] * array[1]
            del array[0:2]
        
print(result)