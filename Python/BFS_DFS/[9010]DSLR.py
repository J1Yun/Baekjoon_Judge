from collections import deque
t = int(input())
result = []

for _ in range(t):
    before, after = map(int, input().split())

    queue = deque()
    queue.append((before, ''))
    visited = [0 for _ in range(10000)]
    visited[before] = 1

    answer = ''
    while queue:
        num, command = queue.popleft()
        if num == after:
            answer = command
            break

        if num*2 < 10000 and not visited[num*2]:
            queue.append((num*2, command+'D'))
            visited[num*2] = 1

        if num*2 >= 10000 and not visited[(num*2) % 10000]:
            queue.append(((num*2) % 10000, command+'D'))
            visited[(num*2) % 10000] = 1

        if num - 1 >= 0 and not visited[num-1]:
            queue.append((num-1, command+'S'))
            visited[num-1] = 1

        if num - 1 < 0 and not visited[9999]:
            queue.append((9999, command+'S'))
            visited[9999] = 1

        num = str(num).zfill(4)
        
        if not visited[int(num[1:]+num[0])]:
            queue.append((int(num[1:]+num[0]), command+'L'))
            visited[int(num[1:]+num[0])] = 1

        if not visited[int(num[-1]+num[:-1])]:
            queue.append((int(num[-1]+num[:-1]), command+'R'))
            visited[int(num[-1]+num[:-1])] = 1

    result.append(answer)

for r in result:
    print(r)