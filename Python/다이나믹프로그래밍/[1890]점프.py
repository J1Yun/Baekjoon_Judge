n = int(input())
data = []
for _ in range(n):
    data.append(list(map(int, input().split())))

dp = [[0]*n for _ in range(n)]
dp[0][0] = 1
for i in range(n):
    for j in range(n):
        for k in range(1, i+1):
            if data[i-k][j] == k:
                dp[i][j] += dp[i-k][j]
        for k in range(1, j+1):
            if data[i][j-k] == k:
                dp[i][j] += dp[i][j-k]
print(dp[n-1][n-1])