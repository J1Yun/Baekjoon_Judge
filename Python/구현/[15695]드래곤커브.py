n = int(input())
data = []
grid = [[0] * 101 for _ in range(101)]
for _ in range(n):
    data.append(tuple(map(int, input().split())))

dx, dy = [0, -1, 0, 1], [1, 0, -1, 0]
for y, x, d, g in data:
    dragon = []
    dragon.append((x, y, d))
    grid[x][y] = 1
    nx, ny = x + dx[d], y + dy[d]
    for _ in range(g):
        length = len(dragon)
        for i in range(length-1, -1, -1):
            d = (dragon[i][2] + 1) % 4
            dragon.append((nx, ny, d))
            grid[nx][ny] = 1
            nx, ny = nx + dx[d], ny + dy[d]
    grid[nx][ny] = 1

result = 0
for i in range(100):
    for j in range(100):
        if grid[i][j] and grid[i+1][j] and grid[i][j+1] and grid[i+1][j+1]:
            result += 1

print(result)
        