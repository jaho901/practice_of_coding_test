import sys
sys.stdin = open('practice2.txt')

# def sub(cur):


T = int(input())
for tc in range(1, T+1):
    number = list(map(int, input().split()))
    length = len(number)

    result = []

    # 이 부분 확실하게 외우기
    for i in range(1, 1<<len(number)):
        tmp = 0
        for j in range(len(number)):
            if i & (1<<j):
                tmp += number[j]
        if tmp == 0:
            result = 1
            break
    if result == []:
        result = 0
    print('#{} {}'.format(tc, result))
