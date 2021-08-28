import sys
sys.stdin = open('10158.txt')

N, M = map(int, input().split())
x, y = map(int, input().split())
cnt = int(input())
c = cnt

# 문제를 보면 하나의 규칙이 떠오른다!!
# 어차피 개미는 항상 좌우로 한칸씩 이동하고 상하로도 한칸씩 이동하는 것이다!

def find_x(x, N, c):
    # c가 매우 큰 경우 어차피 개미는 좌우나 상하로 반복하기 때문에 아래와 같이 나머지로 지정해준다.
    if c > N * 2:
        c = c % (N * 2)
    while c > 0:
        # 항상 개미는 큰쪽으로 이동
        while x < N:
            x += 1
            c -= 1
            # 중간에 c가 0이 되면 해당하는 위치값을 반환
            if c == 0:
                return x
        # 큰쪽으로 이동을 다 한 경우 다시 반대로 0으로 이동
        while x > 0:
            x -= 1
            c -= 1
            # 위와 동일!
            if c == 0:
                return x


print(find_x(x, N, cnt), find_x(y, M, cnt))