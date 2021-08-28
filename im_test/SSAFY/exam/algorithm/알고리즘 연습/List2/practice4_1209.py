import sys
sys.stdin = open('practice4.txt')

T = 10
for tc in range(1, T+1):
    N = int(input())

    data = [list(map(int, input().split())) for _ in range(100)]

    # 행의 합
    result1 = 0
    # 열의 합
    result2 = 0
    # 정대각선의 합
    result3 = 0
    # 역대각선의 합
    result4 = 0

    for i in range(100):
        # 계속해서 만들어지는 행의 합과 열의합의 초기화
        sub_1 = 0
        sub_2 = 0
        for j in range(100):
            sub_1 += data[i][j]
            sub_2 += data[j][i]
        if sub_1 > result1:
            result1 = sub_1
        if sub_2 > result2:
            result2 = sub_2
    
        # 대각선의 합 구해보자
        result3 += data[i][i]
        result4 += data[i][99-i]

    print(max(result1, result2, result3, result4))