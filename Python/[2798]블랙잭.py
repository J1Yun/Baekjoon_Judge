# -*- coding: utf-8 -*-
"""
Created on Mon Feb  1 23:49:39 2021

@author: Jiyun
"""

n, m = map(int, input().split())
card = list(map(int, input().split()))
max_sum = 0
for i in range(n-2):
    for j in range(i+1,n-1):
        for k in range(j+1, n):
            num_sum = card[i] + card[j] + card[k]
            if num_sum > max_sum and num_sum<=m:
                max_sum = num_sum

print(max_sum)