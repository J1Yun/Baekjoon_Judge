# -*- coding: utf-8 -*-
"""
Created on Mon Feb 22 18:59:50 2021

@author: Jiyun
"""


m = input()
math=[]
t = ''
for i in m:
    if i == '-' or i == '+':
        math.append(int(t))
        math.append(i)
        t =''
    else:
        t += i
math.append(int(t))

temp = [math[0]]
for i in range(1,len(math)-1, 2):
    if math[i] == '+':
        temp[-1] = temp[-1] + math[i+1]
    else:
        temp.append('-')
        temp.append(math[i+1])
        
result = temp[0]
for i in range(2, len(temp), 2):
    result -= temp[i]

print(result)