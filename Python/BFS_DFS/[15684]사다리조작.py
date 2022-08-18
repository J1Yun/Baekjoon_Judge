n, m, h = map(int, input().split())
line = [[0]*(n+1) for _ in range(h+1)]
for _ in range(m):
    x, y = map(int, input().split())
    line[x][y] = 1
    line[x][y+1] = -1
    
def check(data):
    for k in range(1, n+1):
        j = k
        for i in range(1, h+1):
            j += data[i][j]
        if j != k:
            return False
    return True

def dfs(cnt, idx):
    global min_cnt
    if check(line):
        min_cnt = min(min_cnt, cnt)
        return
    elif cnt == 3 or min_cnt <= cnt:
        return
    for i in range(idx, length):
        if not line[grid[i][0]][grid[i][1]] and not line[grid[i][0]][grid[i][1]+1]:
            line[grid[i][0]][grid[i][1]] = 1
            line[grid[i][0]][grid[i][1]+1] = -1
            dfs(cnt+1, i + 1)
            line[grid[i][0]][grid[i][1]] = 0
            line[grid[i][0]][grid[i][1]+1] = 0
    
grid = []
for i in range(1, h+1):
    for j in range(1, n):
        if not line[i][j] and not line[i][j+1]:
            grid.append((i, j))
length, min_cnt = len(grid), 1e9
dfs(0, 0)
if min_cnt <= 3:
    print(min_cnt)
else:
    print(-1)