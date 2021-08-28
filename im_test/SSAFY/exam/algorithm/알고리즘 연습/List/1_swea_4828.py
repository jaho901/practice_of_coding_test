import sys
sys.stdin = open('1_swea_4828.txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    data = list(map(int, input().split()))

    maximum = data[0]
    minimum = data[0]

    for i in data:
        if maximum < i:
            maximum = i
        if minimum > i:
            minimum = i

    print(maximum - minimum)