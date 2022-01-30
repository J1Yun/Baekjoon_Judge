geer = []
re = []
for _ in range(4):
    geer.append(list(map(int, input())))

n = int(input())
for _ in range(n):
    re.append(tuple(map(int, input().split())))

reverse_sum = [0, 0, 0, 0]
for s, d in re:
    reverse = [0, 0, 0, 0]
    dd = d
    reverse[s-1] = d
    for i in range(s-2, -1, -1):
        temp1 = reverse_sum[i] * -1
        temp2 = reverse_sum[i+1] * -1
        if geer[i][(2+temp1)%8] != geer[i+1][(6+temp2)%8]:
            dd *= -1
            reverse[i] = dd
        else:
            break
    dd = d
    for i in range(s, 4):
        temp1 = reverse_sum[i-1] * -1
        temp2 = reverse_sum[i] * -1
        if geer[i-1][(2+temp1)%8] != geer[i][(6+temp2)%8]:
            dd *= -1
            reverse[i] += dd
        else:
            break
    for i in range(4):
        reverse_sum[i] += reverse[i]

result = 0
for i in range(4):
    temp = reverse_sum[i] * -1
    if geer[i][temp%8] == 1:
        result += 2**i

print(result)  