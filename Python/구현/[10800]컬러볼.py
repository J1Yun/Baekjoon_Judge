from collections import defaultdict
n = int(input())
data = []
for i in range(n):
    data.append(tuple(map(int, input().split()))+tuple([i]))
data.sort(key=lambda x: (x[1], x[0]))
sum_ball = 0
dict_ball = defaultdict(int)
dup_ball = defaultdict(int)
result, temp = [], (0, 0)
for color, size, i in data:
    if temp == (color, size):
        result.append((i, result[-1][1]))
    else:
        result.append((i, sum_ball-dict_ball[color]-dup_ball[size]))
    sum_ball += size
    dict_ball[color] += size
    dup_ball[size] += size
    temp = (color, size)
result.sort()
for i, r in result:
    print(r)