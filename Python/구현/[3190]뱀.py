from collections import deque

n = int(input())
k = int(input())
graph = [[0]*n for _ in range(n)]
for _ in range(k):
    a, b = map(int, input().split())
    graph[a-1][b-1] = 1
l = int(input())
turn = []
for _ in range(l):
    t, d = map(str, input().split())
    turn.append((int(t), d))
    
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
nd, hx, hy = 0, 0, 0
time, i = 0, 0
queue = deque()
queue.append((hx, hy))
while 1:
    hx = hx + dx[nd]
    hy = hy + dy[nd]
    time += 1
    if hx < 0 or hx >= n or hy < 0 or hy >= n or (hx, hy) in queue:
        break
    queue.append((hx, hy))
    if graph[hx][hy] == 0:
        queue.popleft()
    else:
        graph[hx][hy] = 0
    if time == turn[i][0]:
        if turn[i][1] == 'L':
            nd = (nd - 1) % 4
        else:
            nd = (nd + 1) % 4
        if i + 1 < len(turn):
            i += 1

print(time)