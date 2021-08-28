import sys
sys.stdin = open('2_swea_4836.txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    data = [list(map(int, input().split())) for _ in range(N)]

    # 종이 영역 0 ≤ r1, c1, r2, c2 ≤ 9
    paper = [[0]*10 for _ in range(10)]
    # 최종 결괏값
    result = 0

    # data = [[2, 2, 4, 4, 1], [3, 3, 6, 6, 2]]
    for info in data:
        r1, c1, r2, c2, c = info
        for i in range(r1, r2+1):
            for j in range(c1, c2+1):
                paper[i][j] += c
                if paper[i][j] == 3:
                    result += 1
    print('#{} {}'.format(tc, result))
