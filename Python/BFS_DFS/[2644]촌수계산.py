n = int(input())
t1, t2 = map(int, input().split())
m = int(input())
graph = [[] for _ in range(101)]
for _ in range(m):
    s1, s2 = map(int, input().split())
    graph[s1].append(s2)
    graph[s2].append(s1)

result = 0
def dfs(val, visited, num):
    global result
    if val == t2:
        result = num
    visited[val] = 1
    for i in graph[val]:
        if not visited[i]:
            dfs(i, visited, num+1)

visited = [0] * 101
dfs(t1, visited, 0)
if result:
    print(result)
else:
    print(-1)