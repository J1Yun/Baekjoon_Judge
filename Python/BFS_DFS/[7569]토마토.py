from collections import deque
m, n, h = map(int, input().split())
data = [[] for _ in range(h)]
for i in range(h):
    for _ in range(n):
        data[i].append(list(map(int, input().split())))

dx, dy, dz = [1, -1, 0, 0, 0, 0], [0, 0, -1, 1, 0, 0], [0, 0, 0, 0, -1, 1]
queue = deque()

for i in range(h):
    for j in range(n):
        for k in range(m):
            if data[i][j][k] == 1:
                queue.append((i, j, k, 0))
                data[i][j][k] = 1
            
while queue:
    x, y, z, t = queue.popleft()
    for i in range(6):
        nx, ny, nz = x + dx[i], y + dy[i], z + dz[i]
        if nx < 0 or ny < 0 or nz < 0 or nx >= h or ny >= n or nz >= m or data[nx][ny][nz] != 0:
            continue
        queue.append((nx, ny, nz, t+1))
        data[nx][ny][nz] = 1

flag = True
for i in range(h):
    for j in range(n):
        for k in range(m):
            if data[i][j][k] == 0:
                flag = False
                break
if flag:
    if t:
        print(t)
    else:
        print(0)
else:
    print(-1)