n, m = map(int, input().split())
d = [[0]* m for _ in range(n)]
x, y, dir = map(int, input().split())
d[x][y] = 1
arr = [list(map(int, input().split())) for _ in range(n)]

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def turn_left():
    global dir
    dir -= 1
    if dir == -1:
        dir = 3

# 시물레이션 시작
cnt = 1
turn_time = 0
while True:
    turn_left()
    new_x = x + dx[dir]
    new_y = y + dy[dir]
        # 아직 안 가본 곳인 경우 and 그 곳이 육지인 경우
    if d[new_x][new_y] == 0 and arr[new_x][new_y] == 0:
        d[new_x][new_y] = 1 #가본곳이라고 체크
        # 이동한 위치를 현재 위치로
        x, y = new_x, new_y
        cnt += 1
        turn_time = 0
        continue

    else:
        turn_time += 1

    # 더 이상 돌 곳이 없을 경우
    if turn_time == 4:
        # 뒤로 한 칸 가기 => 이미 갔던 곳이니깐 cnt + 1 안해줌
        new_x = x - dx[dir]
        new_y = y - dy[dir]
        if arr[new_x][new_y] == 0:
            # 이동한 위치를 현재 위치로
            x, y = new_x, new_y
            # 이미 앞으로 한 칸 간 곳은 1로 되어있으므로
            # 여분의 다른 3면을 찾아서 0인 곳으로 갈 것이다.
        else:
            break
        turn_time = 0

print(cnt)