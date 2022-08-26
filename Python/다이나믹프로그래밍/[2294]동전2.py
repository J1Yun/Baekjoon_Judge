n, k = map(int, input().split())
coins = set()
for _ in range(n):
    coins.add(int(input()))

dp = [1e9] * (k+1)
for c in coins:
    if c <= k:
        dp[c] = 1
for i in range(2, k+1):
    for c in coins:
        idx = i - c
        if idx > 0 and dp[idx] > 0:
            dp[i] = min(dp[i], dp[idx] + 1)

if dp[k] == 1e9:
    print(-1)
else:
    print(dp[k])