# -*- coding: utf-8 -*-
n = int(input())

for i in range(0, n):
    num = str(i)
    sum_num = i
    for j in num:
        sum_num += int(j)
    if sum_num == n:
        break
if i == n-1:
    i = 0
print(i)
