# -*- coding: utf-8 -*-
"""
Created on Wed Feb 24 20:06:05 2021

@author: Jiyun
"""

n = int(input())
word = []
for i in range(n):
    word.append(input())

word_dict = {}
for i in word:
    length = len(i)
    for j in i:
        length -= 1
        if j in word_dict.keys():
            word_dict[j] += 10**length
        else:
            word_dict[j] = 10**length

word_dict = sorted(word_dict.values(), reverse=True)

num = 9
max_sum = 0
for i in word_dict:
    max_sum += i*num
    num -= 1

print(max_sum)