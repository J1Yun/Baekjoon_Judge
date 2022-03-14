import heapq
INF = int(1e9)

m, n = map(int, input().split())
graph = []
for _ in range(n):
    graph.append(list(map(int, input())))

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
result = [[INF]*m for _ in range(n)]
hq = []
heapq.heappush(hq, (0, 0, 0))
while hq:
    r, x, y = heapq.heappop(hq)
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        nr = r
        if nx < 0 or ny < 0 or nx >= n or ny >= m or result[nx][ny] != INF:
            continue 
        if graph[nx][ny] == 1:
            nr = r + 1
        if r < result[nx][ny] and result[nx][ny] >= nr:
            result[nx][ny] = nr
            heapq.heappush(hq, (nr, nx, ny))

if result[n-1][m-1] == INF:
    print(0)
else:
    print(result[n-1][m-1])