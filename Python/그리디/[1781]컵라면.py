# 풀이 확인

import heapq
n = int(input())
data, hq = [], []
for _ in range(n):
    data.append(tuple(map(int, input().split())))
data.sort(key=lambda x: (x[0], -x[1]))
time, result= 1, 0
for d, c in data:
    if time <= d:
        result += c
        heapq.heappush(hq, (c, time))
        time += 1
    else:
        if hq:
            min_tmp = heapq.heappop(hq)
            if min_tmp[0] < c:
                result += (c - min_tmp[0])
                heapq.heappush(hq, (c, min_tmp[1]))
            else:
                heapq.heappush(hq, min_tmp)
print(result)