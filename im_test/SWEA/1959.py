import sys
sys.stdin = open('1959.txt')

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    a_list = list(map(int, input().split()))
    b_list = list(map(int, input().split()))

    # 어떤 게 더 긴 수인지를 모르기 때문에
    # 길이가 긴 수를 n과 a로 지정해주고 짦은 수를 m과 b로 지정
    if N >= M:
        n, m = N, M
        a = a_list
        b = b_list
    elif N < M:
        n, m = M, N
        a = b_list
        b = a_list

    result = 0

    # a와 b에 해당하는 모든 인덱스의 곱을 sub에 더해주고 최댓값 비교
    for i in range(n-m+1):
        sub = 0
        for j in range(m):
            sub += a[i+j] * b[j]
        if result < sub:
            result = sub

    print('#{} {}'.format(tc, result))