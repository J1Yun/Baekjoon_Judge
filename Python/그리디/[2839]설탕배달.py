# -*- coding: utf-8 -*-
"""
Created on Sun Feb 21 18:03:21 2021

@author: Jiyun
"""

n = int(input())
count = 0

while 1:
    if n % 5 == 0:
        n -= 5
        count += 1
    elif n % 3 == 0:
        n -= 3
        count += 1
    else:
        n -= 5
        count += 1
    
    if n <= 0:
        break

if n == 0:
    print(count)
if n < 0:
    print(-1)