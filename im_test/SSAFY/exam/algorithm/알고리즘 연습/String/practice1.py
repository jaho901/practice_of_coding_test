import sys
sys.stdin = open('practice1.txt')

T = int(input())

for tc in range(1, T+1):
    word = input()
    print('#{} {}'.format(tc, word[::-1]))

    # result = reversed(word)
    # print(list(result))
    result = list(reversed(word))
    print('#{} {}'.format(tc, ''.join(result)))

    result = ''
    for i in word:
        result = i + result
    print('#{} {}'.format(tc, result))


