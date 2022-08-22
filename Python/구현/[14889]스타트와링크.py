from itertools import combinations

data = []
people = []
n = int(input())
for i in range(n):
    data.append(list(map(int, input().split())))
    people.append(i)
comb = list(combinations(people, n//2))
result = int(1e9)
for i in range(len(comb)//2):
    temp = list(set(people) - set(comb[i]))
    power1, power2 = 0, 0
    for co in list(combinations(comb[i], 2)):
        power1 += data[co[0]][co[1]] + data[co[1]][co[0]]
    for co in list(combinations(temp, 2)):
        power2 += data[co[0]][co[1]] + data[co[1]][co[0]]
    result = min(result, abs(power1 - power2))
    
print(result)