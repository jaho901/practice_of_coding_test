import sys
sys.stdin = open('practice4.txt')

T = int(input())
for _ in range(10):
    tc, n = input().split()
    words = input().split()
    # 제환된 리스트에서 원하는 값들 추출하는 방법!! 중요하다!!
    numbers = ["ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"]

    result = ''
    for number in numbers:
        for word in words:
            if word == number:
                result += word + ' '

    print('{} {}'.format(tc, result))
