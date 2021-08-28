import sys
sys.stdin = open('10157.txt')

# snail 문제와 매우 동일한 방법
T = int(input())
for tc in range(1, T+1):
    C, R = map(int, input().split())
    K = int(input())
    # 값을 채워줄 빈 arr 생성
    arr = [[0] * C for _ in range(R)]
    # 방향벡터 생성
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]

    i = R
    j = 0
    k = 0
    cnt = 0

    # 원하는 값이 좌석 넓이보다 큰 경우 그냥 0 출력!
    if K > C*R:
        print(0)
    # 그 외의 경우는 시계방향으로 돌려주면서 그 위치에 cnt 넣어주기!
    else:
        while cnt <= C * R:
            nx = i + dx[k]
            ny = j + dy[k]

            if 0 <= nx < R and 0 <= ny < C and arr[nx][ny] == 0:
                cnt += 1
                arr[nx][ny] = cnt
                i = nx
                j = ny

            else:
                k = (k + 1) % 4

            # 만약 cnt가 우리가 원하는 K값인 경우 반복문 나가고
            if cnt == K:
                break
        # 해당하는 위치를 출력! 
        print(ny + 1, R - nx)
            

