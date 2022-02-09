a, b = map(int, input().split())

count = 0
while b > a:
    if b % 10 == 1:
        b //= 10
    elif b % 2 == 0:
        b /= 2
    else :
        break
    count += 1

if a == b:
    print(count + 1)
else:
    print(-1)