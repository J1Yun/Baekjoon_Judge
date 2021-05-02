# -*- coding: utf-8 -*-
"""
Created on Sun Feb 28 13:52:51 2021

@author: Jiyun
"""
cursor = list(input())
n = int(input())
stack = []
for i in range (n):
    command = list(input().split())
    if command[0] == 'L' and cursor != []:
        stack.append(cursor.pop())
    elif command[0] == 'D' and stack != []:
        cursor.append(stack.pop())
    elif command[0] == 'B'and cursor != []:
        cursor.pop()
    elif command[0] == 'P':
        cursor.append(command[1])

print(''.join(cursor + list(reversed(stack))))