n = int(input())
a = list(map(int, input().split()))
b, c = map(int, input().split())

result = 0
for people in a:
    people -= b
    result += 1
    if people > 0:
        if people % c == 0:
            result += people // c
        else:
            result += people // c + 1
            
print(result)
