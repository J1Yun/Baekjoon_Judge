from collections import deque
n, m, v = map(int, input().split())
graph = [[] for _ in range(1001)]
for _ in range(m):
    f, t = map(int, input().split())
    graph[f].append(t)
    graph[t].append(f)

for i in graph:
    i.sort()

result_dfs, result_bfs = [], []
def dfs(s, visited):
    result_dfs.append(s)
    visited[s] = 1
    for i in graph[s]:
        if not visited[i]:
            dfs(i, visited)

def bfs(s, visited):
    queue = deque([s])
    visited[s] = 1
    while queue:
        q = queue.popleft()
        result_bfs.append(q)
        for i in graph[q]:
            if not visited[i]:
                queue.append(i)
                visited[i] = 1

dfs_visited, bfs_visited = [0] * 1001, [0] * 1001
dfs(v, dfs_visited)
bfs(v, bfs_visited)
print(*result_dfs, sep=' ')
print(*result_bfs, sep=' ')



