n = int(input())
data = [0]
for _ in range(n):
    data.append(int(input()))
    
d = [0] * (n+1)
d[1] = data[1]
if n > 1:
    d[2] = data[1] + data[2]
for i in range(3,n+1):
    d[i] = max(d[i-2] + data[i], d[i-3] + data[i-1] + data[i])

print(d[n])