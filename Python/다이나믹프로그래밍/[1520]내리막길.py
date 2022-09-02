m, n = map(int, input().split())
data = []
for _ in range(m):
    data.append(list(map(int, input().split())))

dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
result = 0
def dfs(x, y, visited, prev):
    if (x, y) == (m-1, n-1):
        return 1
    visited[x][y] = 0
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if nx < 0 or ny < 0 or nx >= m or ny >= n or not visited[nx][ny]:
            continue
        if data[nx][ny] < prev:
            if visited[nx][ny] > 0:
                visited[x][y] += visited[nx][ny]
                continue
            temp = dfs(nx, ny, visited, data[nx][ny])
            visited[x][y] += temp 
    return visited[x][y]

visited = [[-1] * n for _ in range(m)]
result = dfs(0, 0, visited, data[0][0])
print(result)