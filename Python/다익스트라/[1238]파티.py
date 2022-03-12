import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)

n, m, x = map(int, input().split())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))

distance_a = []
for i in range(1, n+1):
    hq = []
    heapq.heappush(hq, (0, i))
    d = [INF] * (n+1)
    d[i] = 0
    while hq:
        dist, now = heapq.heappop(hq)
        if d[now] < dist:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if cost < d[i[0]]:
                d[i[0]] = cost
                heapq.heappush(hq, (cost, i[0]))
    distance_a.append(d[x])
            
hq = []
heapq.heappush(hq, (0, x))
distance_b = [INF] * (n+1)
distance_b[x] = 0
while hq:
    dist, now = heapq.heappop(hq)
    if distance_b[now] < dist:
        continue
    for i in graph[now]:
        cost = dist + i[1]
        if cost < distance_b[i[0]]:
            distance_b[i[0]] = cost
            heapq.heappush(hq, (cost, i[0]))

result = 0
for i in range(1, n+1):
    result = max(result, distance_a[i-1] + distance_b[i])
    
print(result)