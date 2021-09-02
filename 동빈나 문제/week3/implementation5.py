

def find(arr, num, dl):
    x = 0
    y = 0
    k = 0

    cnt = 0  # 총 몇초 지났는지
    memo = [[0, 0]]  # 뱀의 몸이 있는 위치

    while True:
        nx = x + dx[k]
        ny = y + dy[k]
        # 조건 달기 -> 범위 안벗어나면서 다음 구간에 몸이 없으면
        if 0 <= nx < N and 0 <= ny < N and arr[nx][ny] != 1:
            # 만약 다음구간에 사과가 있든 없든 다음위치 1로 바꾸고 자기 몸길이에 append
            if arr[nx][ny] != 'a':  # 만약 사과가 없다면
                arr[memo[0][0]][memo[0][1]] = 0  # 자기 몸에서 가장 꼬리 부분 0으로 바꿈
                memo.pop(0)  # 그 위치 삭제
            arr[nx][ny] = 1
            memo.append([nx, ny])
            cnt += 1
            x = nx
            y = ny

            # 만약 cnt가 X에 도달하게 된다면
            if cnt in num:
                idx = num.index(cnt)
                # 그때의 C가 'D'라면 우측
                if dl[idx] == 'D':
                    k += 1
                # 'L'이면 좌측 회전
                else:
                    k -= 1
                k = k % 4

        # 젤 위의 조건을 못맞춰도 한칸 더 간 다음에 끝나니깐 cnt에 1을 더해준다.
        else:
            cnt += 1
            break
    return cnt



N = int(input())
arr = [[0] * N for _ in range(N)]
# 현재위치 1로 변경
arr[0][0] = 1

K = int(input())
apple = [list(map(int, input().split())) for _ in range(K)]


# 사과있는곳을 'a'로 채우기
for ap in apple:
    arr[ap[0] - 1][ap[1] - 1] = 'a'


L = int(input())
dir = [list(input().split()) for _ in range(L)]
num = []
dl = []
for d in dir:
    num.append(int(d[0]))
    dl.append(d[1])


dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]


print(find(arr, num, dl))