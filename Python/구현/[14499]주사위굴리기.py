n, m, x, y, k = map(int, input().split())
data = []
for _ in range(n):
    data.append(list(map(int, input().split())))
command = list(map(int, input().split()))

dice = [0]*6
dx, dy = [0, 0, -1, 1], [1, -1, 0, 0]
result = []
for c in command:
    # 지도 칸 유효범위 확인
    nx, ny = x + dx[c-1], y + dy[c-1]
    if nx < 0 or nx >= n or ny < 0 or ny >= m:
        continue
    # 주사위 굴리기
    if c <= 2:
        temp = [(3, dice[3]), (0, dice[0]), (2, dice[2]), (5, dice[5])]
    else:
        temp = [(1, dice[1]), (0, dice[0]), (4, dice[4]), (5, dice[5])]
    if c % 2:
        for i in range(1, 4):
            dice[temp[i][0]] = temp[i-1][1]
        dice[temp[0][0]] = temp[-1][1]
    else:
        for i in range(3):
            dice[temp[i][0]] = temp[i+1][1]
        dice[temp[-1][0]] = temp[0][1]
    # 칸에 적힌 수 확인 후 주사위 바닥면과 복사
    if data[nx][ny]:
        dice[-1] = data[nx][ny]
        data[nx][ny] = 0
    else:
        data[nx][ny] = dice[-1]
    # 현재 좌표 갱신 및 주사위 윗면 저장
    x, y = nx, ny
    result.append(dice[0])
# 결과 출력
for r in result:
    print(r)