import sys
sys.stdin = open('3_swea_4864.txt')

def search(short, char):
    for i in range(len(short)-2, -1, -1):
        if short[i] == char:
            return len(short)-i-1
    return len(short)

def boyer_moore(short, long):
    n = len(short)
    m = len(long)
    idx = 0
    while idx <= m-n:
        j = n-1
        while j >= 0:
            if short[j] != long[idx+j]:
                print(short[j])
                print(long[idx+j])
                move = search(short, long[idx+n-1])
                print(move)
                break
            j -= 1
        if j == -1:
            return 1
        else:
            idx += move
    return 0

T = int(input())

for tc in range(1, T+1):
    short = input()
    long = input()

    result = boyer_moore(short, long)
    print('#{} {}'.format(tc, result))

