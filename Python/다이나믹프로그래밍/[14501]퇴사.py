import sys
input = sys.stdin.readline

data = []
n = int(input())
for _ in range(n):
    data.append(list(map(int, input().split())))

d = [0] * (n+1)
for i in range(1,n+1):
    t, p = data[i-1][0], data[i-1][1]
    if i+t-1 <= n:
        d[i+t-1] = max(d[i+t-1], d[i-1] + p)
    if d[i] < d[i-1] :
        d[i] = d[i-1]
print(max(d))
