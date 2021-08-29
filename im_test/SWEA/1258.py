import sys
sys.stdin = open('1258.txt')

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    data = []
    idx = []
    cnt = 0

    dx = [0, 1]
    dy = [1, 0]
    col_value = 0
    row_value = 0

    for i in range(N):
        x = i
        for j in range(N):
            y = j
            # 0이 아닌 수를 발견했다면!
            if arr[i][j] != 0:
                # 방향벡터를 통해 너비와 높이만을 구한다
                for k in range(2):
                    while True:
                        nx = x + dx[k]
                        ny = y + dy[k]
                        # 조건에 만족할 경우
                        if 0 <= nx < N and 0 <= ny < N and arr[nx][ny] != 0:
                            # 너비이면
                            if k == 0:
                                col_value += 1
                            # 높이이면
                            elif k == 1:
                                row_value += 1
                            x, y = nx, ny
                        # 조건 만족못할 경우
                        else:
                            # 너비일때는 현재 위치를 -1 빼주고
                            if k == 0:
                                y = ny - 1
                                break
                            # 높이까지 다 보면 다시 x와 y를 현재 위치로 바꿔준다.
                            else:
                                x, y = i, j
                                break
                # row_value와 col_value가 0부터 시작했으므로 1씩 더해준다.
                row_value += 1
                col_value += 1
            # 만약에 부분집합이 있으면
            if row_value > 0 and col_value > 0:
                # 해당하는 부분을 모두 0으로 변경하고
                for k in range(i, i+row_value):
                    for l in range(j, j+col_value):
                        arr[k][l] = 0
                # 아래와 같이 추가해준다.
                cnt += 1
                data.append([row_value, col_value, row_value*col_value])
                # 아래 값은 다시 초기화해준다.
                col_value = 0
                row_value = 0

    # 곱을 기준으로 정렬시키고
    data = sorted(data, key=lambda x:x[2])
    result = []
    # 최종 결과값에 행과 열의 인덱스만 포함시킨다.
    for i in data:
        result.append(i[0])
        result.append(i[1])

    result = [cnt] + result
    print('#{} {}'.format(tc, ' '.join(map(str, result))))
