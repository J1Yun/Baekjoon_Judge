import sys
input = sys.stdin.readline

n = int(input())
data = list(map(int, input().split()))

d = [0] * (n+1)
d[1] = data[0]
for i in range(2,n+1):
    d[i] = data[i-1]
    for j in range(1,i//2+1):
        d[i] = max(d[i], d[i-j]+data[j-1])


print(d[n])

