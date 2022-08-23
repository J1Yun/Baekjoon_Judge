from collections import deque

def bfs(x, y, open):
    queue = deque()
    queue.append((x, y))
    check[x][y] = 1
    open.add((x, y))
    val, count = 0, 0
    while queue:
        x, y = queue.popleft()
        val += data[x][y]
        count += 1
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= n:
                continue
            if l <= abs(data[nx][ny] - data[x][y]) <= r and not check[nx][ny]:
                queue.append((nx, ny))
                check[nx][ny] = 1
                open.add((nx, ny))
    return val, count, open 

data = []
n, l, r = map(int, input().split())
for _ in range(n):
    data.append(list(map(int, input().split())))
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
result, flag = 0, True
while flag:
    check = [[0]*n for _ in range(n)]
    all = []
    flag = False
    for i in range(n):
        for j in range(n):
            if not check[i][j]:
                val, count, open = bfs(i, j, set())
                if count > 1:
                    flag = True
                    all.append((val//count, open))
    for val, op in all:
        for x, y in op:
            data[x][y] = val
    if flag:
        result += 1
print(result)




from collections import deque

def bfs(x, y, open):
    queue = deque()
    queue.append((x, y))
    check[x][y] = 1
    open.add((x, y))
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= n:
                continue
            if l <= abs(data[nx][ny] - data[x][y]) <= r and not check[nx][ny]:
                queue.append((nx, ny))
                check[nx][ny] = 1
                open.add((nx, ny))
    temp, count = 0, 0
    for op in open:
        temp += data[op[0]][op[1]]
        count += 1
    if count > 1:
        for op in open:
            data[op[0]][op[1]] = temp // count
        return True
    else:
        return False

data = []
n, l, r = map(int, input().split())
for _ in range(n):
    data.append(list(map(int, input().split())))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
result, flag = 0, True
while flag:
    check = [[0]*n for _ in range(n)]
    flag = False
    for i in range(n):
        for j in range(n):
            if not check[i][j] and bfs(i, j, set()):
                flag = True
    if flag:
        result += 1
print(result)