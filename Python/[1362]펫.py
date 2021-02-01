# -*- coding: utf-8 -*-
"""
Created on Sat Jan 30 15:55:40 2021

@author: Jiyun
"""
i = 0
while 1:
    o, w = map(int, input().split())
    if o==0 and w==0:
        break
    while 1:
        if w <= 0:
            command = input().split()
            if command[0]=='#':
                break
            else:
                continue
        else:
            command = input().split()
            if command[0]=='E':
                w -= int(command[1])
            elif command[0]=='F':
                w += int(command[1])
            elif command[0]=='#':
                break
    i += 1
    if o//2 < w and w < o*2:
        print(i, ':-)')
    elif w <= 0:
        print(i, 'RIP')
    else:
        print(i, ':-(')
