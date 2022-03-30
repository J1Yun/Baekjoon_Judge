s = int(input())

dp = [ 0 for _ in range(s+1) ]
dp[2] = 2
if s >= 3 :
    dp[3] = 5
for i in range(4, s+1):
    temp = []
    if i % 2 == 0:
        for j in range(i//2, i):
            temp.append(dp[j]+2+j*2-i)
        dp[i] = min(temp)

print(dp[s])