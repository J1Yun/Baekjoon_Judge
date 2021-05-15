# -*- coding: utf-8 -*-
"""
Created on Mon Mar  8 22:55:05 2021

@author: Jiyun
"""
key = input()
string = input()
length = len(string)
f, b, l = 0, length-1, len(key)
front = []
back = []
end = False
while f < length :
    while f <= b or (end == True and f < length):
        front.append(string[f])
        f += 1
        if f == b + 1:
            end = True
        if ''.join(front[-l:]) == key:
            del front[-l:]
            break
    while f <= b:
        back.append(string[b])
        b -= 1
        if f == b + 1:
            end = True
        if ''.join(back[-l:]) == ''.join(reversed(key)):
            del back[-l:]
            break
        
print(''.join(front[:b+2] + list(reversed(back))))