import sys
sys.stdin = open('3_swea_1216.txt')

def is_palindrome(K):
    for i in range(100):
        for j in range(100 - K + 1):
            # 가로
            tmp = words[i][j:j + K]
            # 세로
            tmp2 = zwords[i][j:j + K]
            if tmp == tmp[::-1] or tmp2 == tmp2[::-1]:
                return K
    return 0


for _ in range(10):
    tc = input()
    words = [input() for _ in range(100)]
    zwords = []
    for i in range(100):
        tmp = ''
        for j in range(100):
            tmp += words[j][i]
        zwords.append(tmp)


    for k in range(100, 0, -1):
        ans = is_palindrome(k)
        if ans:
            break

    print("#{} {}".format(tc, ans))


