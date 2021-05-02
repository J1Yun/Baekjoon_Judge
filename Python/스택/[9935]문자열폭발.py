# -*- coding: utf-8 -*-
"""
Created on Sun Mar  7 19:05:06 2021

@author: Jiyun
"""

string = list(input())
bumb = input()
stack = []
length = len(bumb)
for i in string:
    stack.append(i)
    if ''.join(stack[-length:]) == bumb:
        del stack[-length:]
if stack == []:
    print('FRULA')
else:
    print(''.join(stack))