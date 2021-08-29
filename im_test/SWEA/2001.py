import sys
sys.stdin = open('2001.txt')

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    data = [list(map(int, input().split())) for _ in range(N)]
    # 계속 비교해줄 최종 결과값
    maximum = 0

    # 처음 열과 행의 범위는 0부터 N-M까지 전부 순회하기 위해 이렇게 정해준다.
    for i in range(N-M+1):
        for j in range(N-M+1):
            # 행과 열이 변경될때마다 result값을 초기화시켜준다.
            result = 0
            # 해당 행과 열부터 M개의 행과 열에 속해있는 파리의 수를 모두 더해준다!
            for k in range(i, i+M):
                for l in range(j, j+M):
                    result += data[k][l]
            # 전부 더해졌을 때 maximum과 비교해주면서 계속해서 최댓값을 변경
            if maximum < result:
                maximum = result

    print('#{} {}'.format(tc, maximum))