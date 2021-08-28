import sys
sys.stdin = open('10157.txt')

T = int(input())
for tc in range(1, T+1):
    C, R = map(int, input().split())
    K = int(input())

    arr = [[0] * C for _ in range(R)]

    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]

    i = R
    j = 0
    k = 0
    cnt = 0

    if K > C*R:
        print(0)
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

            if cnt == K:
                break

        print(ny + 1, R - nx)
            

