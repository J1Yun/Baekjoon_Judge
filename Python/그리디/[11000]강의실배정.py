import heapq
import sys
input = sys.stdin.readline

n = int(input())
array = []
for _ in range(n):
    array.append(tuple(map(int, input().split())))
array.sort(key=lambda x: x[0])

pq = []
heapq.heappush(pq, array[0][1])
for i in range(1, n):
    s = heapq.heappop(pq)
    if s <= array[i][0]:
        heapq.heappush(pq, array[i][1])
    else:
        heapq.heappush(pq, s)
        heapq.heappush(pq, array[i][1])

print(len(pq))