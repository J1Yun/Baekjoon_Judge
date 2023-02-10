from collections import deque

n, k = map(int, input().split())
data = []
for _ in range(n):
    data.append(list(map(int, input().split())))
s, a, b = map(int, input().split())

virus = []
for i in range(n):
    for j in range(n):
        if data[i][j]:
            virus.append((data[i][j], i, j, 0))

virus.sort()
virus = deque(virus)
dx, dy = [-1, 1, 0, 0 ], [0, 0, -1, 1]

while virus:
    d, x, y, t = virus.popleft()
    if t == s:
        break
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if nx < 0 or nx >= n or ny < 0 or ny >= n:
            continue
        if data[nx][ny] == 0:
            virus.append((d, nx, ny, t+1))
            data[nx][ny] = d

print(data[a-1][b-1])
