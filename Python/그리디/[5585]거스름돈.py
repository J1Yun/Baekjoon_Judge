# -*- coding: utf-8 -*-
"""
Created on Mon Feb 22 18:54:01 2021

@author: Jiyun
"""

coin = [500, 100, 50, 10, 5, 1]
count = 0

n = int(input())
rest = 1000 - n

for i in coin:
    count += rest//i
    rest %= i

print(count)