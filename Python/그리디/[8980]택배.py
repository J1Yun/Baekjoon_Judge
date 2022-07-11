# 풀이 확인

n, c = map(int, input().split())
m = int(input())
in_box = []
for _ in range(m):
    in_box.append(tuple(map(int, input().split())))

in_box.sort(key=lambda x: x[1])
village = [0] * (n+1)
result = 0
for f, t, s in in_box:
    temp = s
    for i in range(f, t):
        if village[i] + temp >= c:
            temp = c - village[i]
    for i in range(f, t):
        village[i] += temp
    result += temp

print(result)