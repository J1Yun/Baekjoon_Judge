data = []
n, m = map(int, input().split())
for _ in range(n):
    data.append(list(map(int, input().split())))
    
dx, dy = [-1, 1, 0], [0, 0, 1]
max_num = 0
def dfs(x, y, s, t, check):
    if t == 4:
        global max_num
        max_num = max(max_num, s)
        return
    for i in range(3):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx < 0 or nx >= n or ny < 0 or ny >= m or (nx, ny) in check:
            continue
        if t == 3:
            if check[0][1]==check[1][1]==check[2][1]:
                for j in [-1, 1]:
                    check_y = check[1][1] + j
                    if check_y < 0 or check_y >= m:
                        continue
                    dfs(check[1][0], check_y, s + data[check[1][0]][check_y], t + 1, check + [(check[1][0], check_y)])
            elif check[0][0]==check[1][0]==check[2][0]:
                for j in [-1, 1]:
                    check_x = check[1][0] + j
                    if check_x < 0 or check_x >= n:
                        continue
                    dfs(check_x, check[1][1], s + data[check_x][check[1][1]], t + 1, check + [(check_x, check[1][1])])
        dfs(nx, ny, s + data[nx][ny], t + 1, check + [(nx, ny)])
        
for i in range(n):
    for j in range(m):
        dfs(i, j, data[i][j], 1, [(i, j)])
print(max_num)