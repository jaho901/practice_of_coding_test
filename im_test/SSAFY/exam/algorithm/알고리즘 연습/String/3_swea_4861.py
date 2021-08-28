import sys
sys.stdin = open('3_swea_4861.txt')

def is_palindrome(word):
    global m
    idx = 0
    while idx + m-1 < len(word):
        pali = word[idx:idx+m]
        if pali == pali[::-1]:
            return pali
        idx += 1
    return False

T = int(input())

for tc in range(1, T+1):
    n, m = map(int, input().split())
    data = [input() for _ in range(n)]

    result = ''
    for i in range(n):
        tmp = ''
        for j in range(n):
            tmp += data[j][i]
        # 가로
        result = is_palindrome(data[i])
        if result:
            break
        # 세로
        result = is_palindrome(tmp)
        if result:
            break
    print('#{} {}'.format(tc, result))
