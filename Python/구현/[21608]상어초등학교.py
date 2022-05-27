friends = []
n = int(input())
for _ in range(n**2):
    friends.append(list(map(int, input().split())))

dx = [-1, 0, 0, 1]
dy = [0, -1, 1, 0]
result = [[0]*n for _ in range(n)]
for friend in friends:
    temp = [[0]*n for _ in range(n)]
    max_emp, max_val = [(0, 0)], [0]
    for i in range(n):
        for j in range(n):
            if result[i][j]:
                if result[i][j] in friend:
                    for k in range(4):
                        x, y = i + dx[k], j + dy[k]
                        if x < 0 or x >= n or y < 0 or y >= n:
                            continue
                        if result[x][y] == 0:
                            temp[x][y] += 1
                            count = 0
                            for t in range(4):
                                x1, y1 = x + dx[t], y + dy[t]
                                if x1 < 0 or x1 >= n or y1 < 0 or y1 >= n:
                                    continue
                                if result[x1][y1] == 0:
                                    count += 1
                            max_emp = max(max_emp, [(temp[x][y], count), (-x, -y)])
            else:
                count = 0
                for k in range(4):
                    x, y = i + dx[k], j + dy[k]
                    if x < 0 or x >= n or y < 0 or y >= n:
                            continue
                    if result[x][y] == 0:
                            count += 1
                max_val = max(max_val, [count, (-i, -j)])
    if max_emp[0][0]:
        result[-max_emp[1][0]][-max_emp[1][1]] = friend[0]
    else:
        result[-max_val[1][0]][-max_val[1][1]] = friend[0]

friends_dict = {}
answer = 0
for friend in friends:
    friends_dict[friend[0]] = friend[1:]
for i in range(n):
    for j in range(n):
        count = 0
        for k in range(4):
            x, y = i + dx[k], j + dy[k]
            if x < 0 or x >= n or y < 0 or y >= n:
                continue
            if result[x][y] in friends_dict[result[i][j]]:
                count += 1
        if count == 4:
            answer += 1000
        elif count == 3:
            answer += 100
        elif count == 2:
            answer += 10
        elif count == 1:
            answer += 1
print(answer)