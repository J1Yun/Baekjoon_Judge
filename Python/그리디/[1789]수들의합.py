n = int(input())

for i in range(1, n+1):
    if n - i < 0:
        break
    n -= i
    result = i

print(result)