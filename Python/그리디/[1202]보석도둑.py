import heapq
import sys
input = sys.stdin.readline

n, k = map(int, input().split())
arr = []
bag = []

for i in range(n):
    heapq.heappush(arr, tuple(map(int, input().split())))
for i in range(k):
    bag.append(int(input()))
bag.sort()

result = 0
temp = []
for b in bag:
    while arr and b >= arr[0][0]:
        heapq.heappush(temp, -heapq.heappop(arr)[1])
    if temp:
        result -= heapq.heappop(temp)
    elif not arr:
        break
print(result)