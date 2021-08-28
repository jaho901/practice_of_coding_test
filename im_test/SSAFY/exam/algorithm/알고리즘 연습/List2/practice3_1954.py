import sys
sys.stdin = open('practice3.txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    # 값을 채워넣을 0으로 이루어진 array 생성
    data = [[0]*N for _ in range(N)]

    # 방향벡터
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]

    # while문 종료 조건이면서 채워넣을 값
    cnt = 1
    i = 0
    j = -1
    # 방향벡터의 인덱스
    k = 0

    # 모든 행렬을 다 돌아다닌 경우 종료
    while cnt <= N*N:
        nx = i + dx[k]
        ny = j + dy[k]
        # 벽을 만나거나 이미 존재하는 수를 만나면 안된다는 조건!!
        if 0 <= nx < N and 0 <= ny < N and data[nx][ny] == 0:
            data[nx][ny] = cnt
            cnt += 1
            # i와 j에 현재 위치를 계속해서 바꿔주는거 잊지말자!!
            i, j = nx, ny

        # k값이 아무리 커져도 0,1,2,3에서 놀아야하기 때문에 이렇게 지정
        else:
            k = (k+1)%4

    for i in data:
        print(*i)