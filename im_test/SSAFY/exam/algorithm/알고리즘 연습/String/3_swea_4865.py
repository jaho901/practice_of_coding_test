import sys
sys.stdin = open('3_swea_4865.txt')

T = int(input())

for tc in range(1, T+1):
    short, long = input(), input()
    case = dict()

    for char in long:
        if char in short:
            case[char] = case.get(char, 0) + 1

    result = 0
    for num in case.values():
        if result < num:
            result = num

    print('#{} {}'.format(tc, result))

