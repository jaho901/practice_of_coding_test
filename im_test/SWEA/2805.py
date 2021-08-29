import sys
sys.stdin = open('2805.txt')

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    data = [list(map(int, input())) for _ in range(N)]
    result = 0

    i = 0
    j = N // 2
    while True:
        # 행이 반으로 가기 전까지
        if i < N // 2:
            # k를 1씩 증가시켜준다 -> 반 바로 전까지!!
            for k in range(0, N//2):
                # 가장 중간 값은 항상 더해주고
                result += data[i][j]
                # k가 1이상일 경우
                if k >= 1:
                    # 좌우로 k개씩 다 result에 더해준다.
                    for l in range(1, k+1):
                        result += data[i][j + l]
                        result += data[i][j - l]
                i += 1

        # 행이 정 중앙에 도착한 경우
        if i == N // 2:
            # 행에 존재하는 모든 값들을 더해준다.
            for k in range(N):
                result += data[i][k]
            i += 1

        # 행이 정 중앙 넘은 경우 그 전이랑 동일한 방법으로 더해준다!!
        if i > N // 2:
            for k in range(N//2-1, -1, -1):
                result += data[i][j]
                if k >= 1:
                    for l in range(1, k+1):
                        result += data[i][j+l]
                        result += data[i][j-l]
                i += 1
            break
    print('#{} {}'.format(tc, result))
                

