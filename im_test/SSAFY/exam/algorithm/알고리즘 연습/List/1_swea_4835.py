import sys
sys.stdin = open('1_swea_4835.txt')

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    data = list(map(int, input().split()))

    # 가장 작은수 0 지정
    maximum = 0
    # 가장 큰수인 10000이 3번 나오는 경우로 지정
    minimum = 10001 * M

    # 전체 길이에서 (M-1)을 뺀만큼 범위 지정
    for i in range(N-M+1):
        # M개의 수의 합을 담을 임시값
        sub = 0
        # i부터 M개까지의 값을 전부 합한다.
        for j in range(i, i+M):
            sub += data[j]
        
        # 그 값을 계속해서 비교하기
        if sub > maximum:
            maximum = sub
        if sub < minimum:
            minimum = sub

    print(maximum - minimum)