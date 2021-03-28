# -*- coding: utf-8 -*-
"""
Created on Wed Feb 24 22:30:44 2021

@author: Jiyun
"""
n, m = map(int, input().split())
matrixA = []
matrixB = []
for i in range(n):
    matrixA.append(list(map(int, input())))
for i in range(n):
    matrixB.append(list(map(int, input())))

count = 0
for i in range(n-2):
    for j in range(m-2):
        if matrixA[i][j] != matrixB[i][j]:
            count += 1
            for k in range(3):
                for l in range(3):
                    matrixA[i+k][j+l] = 1 - matrixA[i+k][j+l]   
                    
if matrixA == matrixB:
    print(count)
else:
    print(-1)