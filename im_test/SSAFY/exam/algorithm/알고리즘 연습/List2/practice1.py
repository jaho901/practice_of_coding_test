import sys
sys.stdin = open('practice1.txt')

def search(x, y, n):
    result = 0
    for k in range(4):
        nx = x + di[k]
        ny = y + dj[k]
        if 0 <= nx < n and 0 <= ny < n:
            result += abs(number[x][y] - number[nx][ny])
    return result


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    number = [list(map(int, input().split())) for _ in range(N)]
    # 값을 채워넣을 행렬 생성
    matrix = [[0] * N for _ in range(N)]

    di = [0, 1, 0, -1]
    dj = [1, 0, -1, 0]

    for i in range(N):
        for j in range(N):
            for k in range(4):
                # 우하좌상 4가지 방향 모두 고려
                ni = i + di[k]
                nj = j + dj[k]
                # 4가지 방향으로 이동했을 때 행렬안에 존재하는 값만 추가
                if 0 <= ni < N and 0 <= nj < N:
                    matrix[i][j] += abs(number[i][j] - number[ni][nj])

    # 최종 결과값
    result = 0

    for i in range(N):
        result += sum(matrix[i])

    print(result)

