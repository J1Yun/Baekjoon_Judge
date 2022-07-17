r, c = map(int, input().split())
data = []
for _ in range(r):
    data.append(list(input()))

def dfs(array, x, y):
    if y == c-2:
        return True
    data[x][y] = 'P'
    for i in range(3):
        nx = x + dx[i]
        if 0 <= nx and nx < r and data[nx][y+1] == '.' :
            if dfs(array + [(nx, y+1)], nx, y+1):
                return True
    return False

dx = [-1, 0, 1]
result = 0
for i in range(r):
    if data[i][1] == '.':
        if dfs([(i, 1)], i, 1):
            result += 1
print(result)