r, c = map(int, input().split())
data = []
for _ in range(r):
    data.append(list(input()))

dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
max_count = 0
def dfs(alpha, count, x, y):
    global max_count
    max_count = max(max_count, count)
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if nx < 0 or nx >= r or ny < 0 or ny >= c:
            continue
        if data[nx][ny] not in alpha:
            alpha.add(data[nx][ny])
            dfs(alpha, count+1, nx, ny)
            alpha.remove(data[nx][ny])

dfs({data[0][0]}, 1, 0, 0)
print(max_count)