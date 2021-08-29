import sys
sys.stdin = open('6190.txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    data = list(map(int, input().split()))

    result = []
    ans = True
    for i in data:
        if i // 10 == 0:
            result.append(i)
        elif i // 10 >= 1:
            a = i
            while a // 10 > 0:
                sub = a % 10
                a = a // 10
                if sub < a%10:
                    ans = False
                    break
            if ans:
                result.append(i)
            else:
                ans = True

    result = sorted(result, reverse=True)
    print('#{} {}'.format(tc, result[0]*result[1]))
