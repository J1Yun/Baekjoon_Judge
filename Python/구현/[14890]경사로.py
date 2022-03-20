import sys
input = sys.stdin.readline

graph = []
n, l = map(int, input().split())
for _ in range(n):
    graph.append(list(map(int, input().split())))

result = 0
for i in range(n):
    visited = [0] * n
    flag = True
    for j in range(1, n):
        s = graph[i][j-1] - graph[i][j]
        if s == 1:
            count = 0
            for k in range(j, j+l):
                if k < n and graph[i][k] == graph[i][j] and visited[k] == 0:
                    visited[k] = 1
                else:
                    flag = False
                    break
        elif s == -1:
            count = 0
            for k in range(j-l, j):
                if 0 <= k and graph[i][k] == graph[i][j-1] and visited[k] == 0:
                    visited[k] = 1
                else:
                    flag = False
                    break
        elif s == 0:
            continue
        else:
            flag = False
            break
    if flag:
        result += 1
        
for j in range(n):
    visited = [0] * n
    flag = True
    for i in range(1, n):
        s = graph[i-1][j] - graph[i][j]
        if s == 1:
            count = 0
            for k in range(i, i+l):
                if k < n and graph[k][j] == graph[i][j] and visited[k] == 0:
                    visited[k] = 1
                else:
                    flag = False
                    break
        elif s == -1:
            count = 0
            for k in range(i-l, i):
                if 0 <= k and graph[k][j] == graph[i-1][j] and visited[k] == 0:
                    visited[k] = 1
                else:
                    flag = False
                    break
        elif s == 0:
            continue
        else:
            flag = False
            break
    if flag:
        result += 1

print(result)