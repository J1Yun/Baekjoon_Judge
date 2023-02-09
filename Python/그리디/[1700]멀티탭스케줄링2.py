n, k = map(int, input().split())
data = list(map(int, input().split()))

plug = []
result = 0
for i in range(k):
    if data[i] in plug:
        continue
    if len(plug) < n:
        plug.append(data[i])
    else:
        select, idx = 0, -1
        for p in range(n):
            new_data = data[i+1:]
            if plug[p] not in new_data:
                select = p
                break
            found = new_data.index(plug[p])
            if found > idx:
                select, idx = p, found
        plug[select] = data[i]
        result += 1

print(result)
