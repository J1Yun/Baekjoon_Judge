# -*- coding: utf-8 -*-
"""
Created on Thu Feb 25 21:23:59 2021

@author: Jiyun
"""
i = 0
while 1:
    l, p, v = map(int, input().split())
    if l == 0:
        break
    i += 1
    count = 0
    count += l * (v // p)
    if v % p < l:
        count += v % p
    else:
        count += l
    
    print('Case',str(i)+':',str(count))
    
    