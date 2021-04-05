# -*- coding: utf-8 -*-
"""
Created on Sat Feb 27 16:01:33 2021

@author: Jiyun
"""

n, k = map(int, input().split())
array = list(map(int, input().split()))
tap = []
count = 0
for i in range(k):
    if array[i] in tap:
        continue
    elif len(tap) < n:
        tap.append(array[i])
    else:
        pick = False
        for j in range(n):
            if tap[j] not in array[i+1:]:
                tap[j] = array[i]
                pick = True
                count += 1
                break
        if pick == False:
            for j in range(k-1,i,-1):
                if array[j] in tap and array[j] not in array[i+1:j]:
                    tap[tap.index(array[j])] = array[i]
                    count += 1
                    break

print(count)        