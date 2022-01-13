import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6) # 재귀의 깊이 변경 (RecursionError)

t = int(input())
result = []

def dfs(x, y):
    if x < 0 or x >= n or y < 0 or y >= m:
        return False
    if graph[x][y] == 1:
        graph[x][y] = 0
        dfs(x-1, y)
        dfs(x+1, y)
        dfs(x, y-1)
        dfs(x, y+1)
        return True
    return False

for _ in range(t):
    count = 0
    m, n, k = map(int, input().split())
    graph = [[0] * m for _ in range(n)]
    for _ in range(k):
        a, b = map(int, input().split())
        graph[b][a] = 1
    
    for i in range(n):
        for j in range(m):
            if dfs(i, j):
                count += 1
    result.append(count)

for i in result:
    print(i)