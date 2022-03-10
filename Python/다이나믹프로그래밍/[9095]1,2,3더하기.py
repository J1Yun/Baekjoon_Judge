n = int(input())
result = []
d = [0] * 11
d[1] = 1
d[2] = 2
d[3] = 4
for i in range(n):
    x = int(input())
    for j in range(4,x+1):
        d[j] = d[j-1] + d[j-2] + d[j-3]
    result.append(d[x])

for i in range(n):
    print(result[i])

