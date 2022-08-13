from itertools import product
from copy import deepcopy
n, m = map(int, input().split())
data, cctv, count = [], [], 0
for _ in range(n):
    data.append(list(map(int, input().split())))
for i in range(n):
    for j in range(m):
        if data[i][j]:
            count += 1
        if 1 <= data[i][j] <= 5:
            cctv.append((i, j))
dict = {1: [[0], [1], [2], [3]], 2: [[0, 2], [1, 3]], 3: [[0, 1], [1, 2], [2, 3], [3, 0]], 4: [[0, 1, 2], [1, 2, 3], [2, 3, 0], [3, 0, 1]], 5:[[0, 1, 2, 3]]}
dx, dy = [-1, 0, 1, 0], [0, 1, 0, -1]
temp, max_cc = [], 0
for x, y in cctv:
    temp.append(dict[data[x][y]])
for prod in list(product(*temp)):
    cnt = 0
    copy_data = deepcopy(data)
    for i in range(len(cctv)):
        for d in prod[i]:
            t, s = cctv[i][0], cctv[i][1]
            while 1:
                nx, ny = t + dx[d], s + dy[d]
                if nx < 0 or nx >= n or ny < 0 or ny >= m or data[nx][ny]==6:
                    break
                if copy_data[nx][ny] == 0:
                    copy_data[nx][ny] = 7
                    cnt += 1
                t, s = nx, ny
    max_cc = max(max_cc, cnt)
print(n * m - count - max_cc)