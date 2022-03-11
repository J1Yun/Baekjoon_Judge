import sys
input = sys.stdin.readline

result = []
t = int(input())
for _ in range(t):
    sticker = []
    n = int(input())
    for _ in range(2):
        sticker.append(list(map(int, input().split())))
    if n >= 2:
        sticker[0][1] = sticker[1][0] + sticker[0][1]
        sticker[1][1] = sticker[0][0] + sticker[1][1]
    
    for i in range(2, n):
        for j in range(2):
            sticker[j][i] = sticker[j][i] + max(sticker[abs(j-1)][i-1], sticker[abs(j-1)][i-2])
            
    result.append(max(sticker[0][n-1], sticker[1][n-1]))

for r in result:
    print(r)