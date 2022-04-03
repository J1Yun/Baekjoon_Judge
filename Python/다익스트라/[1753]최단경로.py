import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)

v, e = map(int, input().split())
k = int(input())
graph = [[] for _ in range(v+1)]
for i in range(e):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    
distance = [INF] * (v+1)
distance[k] = 0
hq = []
heapq.heappush(hq, (0, k))
while hq:
    dist, now = heapq.heappop(hq)
    if distance[now] < dist:
        continue
    for i in graph[now]:
        cost = dist + i[1]
        if cost < distance[i[0]]:
            distance[i[0]] = cost
            heapq.heappush(hq, (cost, i[0]))
            
for i in range(1, v+1):
    if distance[i] == INF:
        print("INF")
    else:
        print(distance[i])