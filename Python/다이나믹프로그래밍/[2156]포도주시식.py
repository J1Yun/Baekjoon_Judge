data = []
n = int(input())
for _ in range(n):
    data.append(int(input()))

d = [0] * n
d[0] = data[0]
if n > 1 :
    d[1] = data[0] + data[1]
if n > 2 :
    d[2] = max(data[0]+data[2], data[1]+data[2], data[0]+data[1])
for i in range(3,n):
    d[i] = max(d[i-2] + data[i], d[i-3] + data[i-1] + data[i], d[i-1])
    
print(max(d))