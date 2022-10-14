n = int(input())
data = []
for _ in range(n):
    data.append(list(map(int, input().split())))

dp = [[[0]* 3 for _ in range(n)] for _ in range(n)]
dp[0][1][0] = 1
move = {0: (0, -1), 1: (-1, 0), 2: (-1, -1)}

for i in range(n):
    for j in range(2, n):
        if data[i][j] == 1:
            continue

        for k in range(2):
            x, y = i + move[k][0], j + move[k][1]
            if x < 0:
                continue

            dp[i][j][k] = dp[x][y][k] + dp[x][y][2]

        if (i - 1 >= 0 and data[i-1][j] == 1) or data[i][j-1] == 1:
            continue

        x, y = i + move[2][0], j + move[2][1]
        if x < 0:
                continue

        dp[i][j][2] = dp[x][y][0] + dp[x][y][1] + dp[x][y][2]

print(sum(dp[-1][-1]))