import sys
sys.stdin = open('2_swea_4843.txt')

T = int(input())
for tc in range(1, T+1):
    n = int(input())
    data = list(map(int, input().split()))

    for i in range(len(data)):
        # max값 처음 지정 & 그 인덱스 지정
        max_V = data[i]
        max_idx = i
        # min값 처음 지정 & 그 인덱스 지정
        min_V = data[i]
        min_idx = i
        # i 이후의 값들과 비교하면서 max값과 min값 변경
        for j in range(i, len(data)):
            if max_V <= data[j]:
                max_V, max_idx = data[j], j
            if min_V >= data[j]:
                min_V, min_idx = data[j], j

        # 길이가 홀수와 짝수일 때 차이가 존재하는지에 따라 다르게 지정
        if i % 2:
            data[i], data[min_idx] = data[min_idx], data[i]
        else:
            data[i], data[max_idx] = data[max_idx], data[i]

    print('#{}'.format(tc), end=' ')

    for i in range(10):
        print(data[i], end=' ')
    print()
